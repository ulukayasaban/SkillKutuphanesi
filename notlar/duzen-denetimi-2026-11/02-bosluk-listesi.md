**Bölüm 2: Boşluk listesi (kaynaklar tekrarlar birleştirilerek)**

Dosya: /private/tmp/claude-501/-Users-sabanulukaya-Documents-SkillKutuphanesi/50d6b09a-ea20-4d05-8336-58e58084ecab/scratchpad/plan/bosluklar.md. Dosyada yalnızca bölüm 1 (araç tablosu ve tek düzen paragrafı) var. Bölüm 2-4 aşağıdadır. Bu denetimde kütüphane dosyalarını ayrıca okumadım, bulgular girdideki kanıtlara dayanır.

**Düzen özeti.** Gerçek `.agents/skills` klasörü ile `AGENTS.md` düzeni Codex, Antigravity, Cursor, Copilot ve Gemini CLI (alias) tarafından okunur. Claude buna ek olarak `.claude/skills` (symlink, Windows'ta kopya) ve `CLAUDE.md` ister, çünkü `AGENTS.md`'yi yalnızca `CLAUDE.md` yoksa okur. Gemini CLI için `GEMINI.md` gerekir. Rol dosyaları yalnızca Claude (`.claude/agents`) ve Codex (`.codex/agents`) için üretilir. Gemini CLI bu Mac'te kurulu değil, Copilot CLI de değil.

**(A) Genel klasörler boşaltılmadan önce kapanmalı**
- **A1. Çok araçlı kurulum desteği yok** (akış 01, 09, 11)
  - Kanıt: `ARACLAR` yalnızca claude/codex (`skill-ekle.py:64`). `--arac claude` `.agents/skills` kopyasını siler. `GEMINI.md` hiç yazılmıyor. Araç sorusu hiçbir akışta sorulmuyor. Antigravity için kilit alanı yok.
  - En küçük değişiklik: `rehber/01`'e araç tablosu ekle (bölüm 1'deki gibi). `--arac claude` seçilince "diğer araçlar skill görmez" BİLGİ satırı ver. İlk kurulumda hangi düzenin seçildiğini BİLGİ olarak yaz ve kilide `araclar` alanını yaz. `GEMINI.md` bloğunu ekle (kullanıcı onayıyla).
  - Dokunulacaklar: `skill-ekle.py`, `rehber/01`, `rehber/04`, `CLAUDE.md`, `AGENTS.md`, `promptlar/01,03`, `test.py`.
- **A2. Genel klasör bekçisi ve taban dosyası yok** (akış 08, 04, 09)
  - Kanıt: `microsoft-foundry` 2026-11-11'de `~/.agents/skills`'e kendiliğinden yazıldı, kimse fark etmedi. Atlama listesi `test.py` ve `duman-testi.py`'de ayrı ayrı kopya. `~/.gemini/skills`, `~/.cursor/skills`, `~/.copilot/skills` ve `~/.agents/.skill-lock.json` izlenmiyor.
  - En küçük değişiklik: salt okuma `araclar/genel-bekci.py` yaz. `notlar/genel-klasor-tabani.json` ile karşılaştırsın. Her yol için sahip alanı olsun (uygulama, kullanıcı, HyperFrames, OpenMontage, skills aracı). Taban yalnızca onayla `--taban-yaz` ile yazılsın. `~/.cursor/skills-cursor`, `~/.codex/skills/.system` ve `synced` kalıcı izinli olsun. `HYPERFRAMES_SKIP_SKILLS` satırı üç dosyada var mı baksın (değer yazdırmadan). Komutlar, ajanlar ve global talimat dosyalarının girdi sayısını da izlesin.
  - Dokunulacaklar: yeni `genel-bekci.py`, `ortak.py`, `test.py`, `duman-testi.py`.
- **A3. Boşaltma prosedürü, yedek ve geri alma yazılı değil** (akış 08, 12, 09)
  - Kanıt: Sıra yalnızca `DURUM.md`'de taslak. `~/.codex/skills` bağları boşaltılacak iki klasöre gidiyor, sıra bozulursa kırılır. Bağ listesi yedeği henüz alınmamış. `geri-al.sh` kütüphane dışında ve sabit yollu. `.skill-lock.json` kalırsa araç eski kayıtla yeniden kurar.
  - En küçük değişiklik: `rehber/12-genel-klasor-bosaltma.md` yaz (sıra, her adım öncesi `ls -la` bağ listesi, ayrı onay, kilit dosyası yedeği, taban yazma, "genel klasöre yazabilenler" tablosu). Vendor klasörleri (`skills-cursor`, `.system`) hariç tutulsun. `CLAUDE.md` ve `AGENTS.md`'ye tek satır bağ ekle.
  - Dokunulacaklar: yeni `rehber/12`, `CLAUDE.md`, `AGENTS.md`, `DURUM.md`.
- **A4. Program giriş yolu, kurulum, geri alma ve çıkarma eksik** (akış 07, 08)
  - Kanıt: OpenMontage kartı ~74 bağı `~/.claude/skills`'te anlatıyor. Global `CLAUDE.md` openmontage skilini oradan yükletiyor. Kartlarda `giris_yolu`, `kurulum`, `geri_alma` yok. `rehber/11`'de geri alma ve çıkarma bölümü yok. Codex/Antigravity/Cursor için OpenMontage ve HyperFrames giriş yöntemi yazılı değil.
  - En küçük değişiklik: Kartlara `giris_yolu`, `kurulum`, `geri_alma`, `ortam_anahtarlari`, `disariya_yazar` ekle. `rehber/11`'e "Boşaltma sonrası program erişimi", "Yeni makineye kurulum", "Geri alma" ve "Programı çıkarma" bölümleri ekle. `test.py` zorunlu alanları denetlesin.
  - Dokunulacaklar: `programlar.json`, `rehber/11`, `test.py`.
- **A5. Kural çelişkileri ve eski belgeler** (akış 02, 04, 07, 08, 09, 11)
  - Kanıt: Kural 1 "genel klasörlere asla yazma" ile onaylı program güncellemesi ve boşaltma çelişiyor. `CLAUDE.md`/`AGENTS.md` satır 51 "sabit kopya" diyor, gerçekte HyperFrames/OpenMontage yerinde kart. `README.md:6-7` ve `rehber/01:12` genel klasörleri normal sayıyor. `PLAN.md`, `TEST_RAPORU.md`, kökteki eski prompt kopyası ve `yerel-yapilacaklar` eski. `CLAUDE.md` ile `AGENTS.md` eşitliğini denetleyen yok.
  - En küçük değişiklik: Kural 1'e "onaylı, yedekli program güncellemesi ve onaylı boşaltma hariç" istisnası ekle. Program satırını düzelt. Eski belgeleri rafa taşı. `dogrula.py`'ye `CLAUDE.md` ile `AGENTS.md` eşitlik HATA'sı ekle. Eski kalıp denetimini boşaltma günü ayrı commit'te aç. `CLAUDE.md` değişimi kullanıcı onayı ister.
  - Dokunulacaklar: `CLAUDE.md`, `AGENTS.md`, `README.md`, `rehber/01`, `PLAN.md`, `TEST_RAPORU.md`, `dogrula.py`.
- **A6. Taze ajan giriş belgesi, kalıcı kararlar ve oturum başı kontrolü yok** (akış 11, 09, 12, 04, 06)
  - Kanıt: `CLAUDE.md`/`AGENTS.md`/`README.md` `DURUM.md`'yi göstermiyor. Claude hafızasındaki kararlar (konu konu ilerle, yedek silme hatırlatması şart, güncellemeler kütüphane oturumundan) repoda yok. Codex veya Antigravity oturumu bunları göremez.
  - En küçük değişiklik: Köke `BASLA.md` yaz (okuma sırası, "hangi isteğe hangi komut"). Kalıcı kararları `notlar/kararlar.md`'ye taşı. `CLAUDE.md`/`AGENTS.md` ilk satırı "önce BASLA.md" desin. "Oturum başında `aylik-ozet.py` oku" satırı ekle.
  - Dokunulacaklar: yeni `BASLA.md`, `notlar/kararlar.md`, `CLAUDE.md`, `AGENTS.md`.
- **A7. Duman testi ve kirli ağaç hedef durumla uyumsuz** (akış 11, 04, 07)
  - Kanıt: `duman-testi.py:63-64` genel klasör parmak izi değişmeyecek diyor. `:72` "0 uyarı" bekliyor ama `dogrula.py:120` emekli rol için uyarı veriyor. Ağaç kirli (9 değişik dosya, `programlar/hyperframes` ve `programlar/openmontage` izlenmiyor), master origin'in 9 commit önünde.
  - En küçük değişiklik: Duman testi parmak izini "testin kendisi yazmadı" olarak değiştir. Bilinen uyarı kabul listesi ekle veya rolden emekli skili çıkar. Önce commit (kullanıcı onayıyla), sonra duman testi.
  - Dokunulacaklar: `duman-testi.py`, `dogrula.py`, `roller/*`.

**(B) Aylık sürdürülebilirlik**
- **B1. Aylık görev kırılgan** (akış 04, 06, 10, 11)
  - Kanıt: Kirli ağaçta sessizce durur. Bekleyen dal sonraki ayı kilitler. C1 ve C2 aynı çalışma ağacında dal değiştirir. `program-denetim.py` ve `yol-tara.py` yalnızca `--uygula` içinde koşuyor. Son çalışma tarihi tutulmuyor. Görev tanımı git dışında ve yedeksiz. C2'de `populer-tarama.py` yok. `takip/*` dalının birleştirme adımı yazılı değil.
  - En küçük değişiklik: Görev SKILL.md'yi şöyle değiştir: dur yerine rapor yaz ve salt okuma adımlarını yine çalıştır. C1 ve C2'den bağımsız `program-denetim` ve `yol-tara` adımı ekle. `notlar/son-aylik-calisma.txt` yaz. Bekleyen dal 45 günü geçince uyar. Görev SKILL.md kopyasını kütüphaneye al ve `dogrula.py` farkı denetlesin. `promptlar/08`'e `takip/*` birleştirme ve ret adımı yaz.
  - Dokunulacaklar: `~/.claude/scheduled-tasks/.../SKILL.md` (onayla), `arsiv-guncelle.py`, `rehber/02`, `promptlar/08`.
- **B2. Tek "karar bekleyenler" ve aylık özet yok** (akış 04, 10, 11)
  - Kanıt: Bekleyenler 7 dosyaya dağınık. 320 aday öncelik ve triyajsız. Trend raporu verilen kararları okumuyor. "izle" kararı iki araçta farklı çalışıyor. Raporların bayatlığı denetlenmiyor (`populer-skiller.md` 2026-11-04, 21 kütüphane reposunu hâlâ "yeni aday" sayıyor).
  - En küçük değişiklik: Salt okuma `araclar/aylik-ozet.py` ile `notlar/aylik-ozet.md` (aylık özet, bekleyenleri toplar). `ortak.py`'de tek `elenecekler()` ve `--karar`. "izle" tek anlamlı olsun (ayrı "İzlenenler" bölümü). Rapor yaşı 45 günü geçince `dogrula.py` UYARI versin. Aylık en fazla N adayı karara bağla kuralı yaz.
  - Dokunulacaklar: yeni `aylik-ozet.py`, `ortak.py`, `github-trend.py`, `konu-takip.py`, `populer-tarama.py`, `dogrula.py`.
- **B3. Proje takibi: sağlık, kayıtsız, taşınan ve silinen** (akış 01, 05, 03)
  - Kanıt: Aylık zincir kayıtlı projelerin sağlığına bakmıyor. Kayıtsız projeler görünmüyor (`IsBasvuruClaude`, `Yetisio`, `Psikolojik Danışman Sosyal Medya`, `Tekfen`). Taşınan veya silinen proje sessizce kaybolur. Takipten çıkarma akışı yok. `elle-kurulan.json`'u yazan araç yok. Projenin kendi yazdığı skiller rapora girmiyor. Kilitte olup kütüphanede olmayan (yetim) skiller yakalanmıyor.
  - En küçük değişiklik: `proje-kullanimi.py`'ye salt okuma `--saglik`, `--tara-kayitsiz`, `--yetim`. `projeler.json`'a `bilinen_projeler` ve `yoksay` alanları ekle. Çıktıyı `notlar/proje-durumu.md`'ye yaz. `rehber/10`'a kısa bölümler ekle.
  - Dokunulacaklar: `proje-kullanimi.py`, `projeler.json`, `rehber/10`, `promptlar/12`, `dogrula.py`.
- **B4. Skill kaynağı çıkarma, emekli ve kayıp repo akışı** (akış 03, 02)
  - Kanıt: Çıkarma tamamen elle JSON ve `gh` işi. `CLAUDE.md` bu akışa işaret etmiyor. `rehber/03` etkiyi `find ~` ile arıyor, `proje-kullanimi.py`'yi anmıyor. Tek KAYIP repo tüm aylık `--uygula`'yı durduruyor (`J-DTurner/etsy-api-skill`, bir projede kurulu). Repo taşınması otomatik yakalanmıyor.
  - En küçük değişiklik: `rehber/03`'e "kaynak/skill çıkar" bölümü yaz. `CLAUDE.md`/`AGENTS.md`'ye madde ekle. `araclar/kaynak-cikar.py` (`--kuru`, onayla, `geri-al`). `arsiv-guncelle.py`'ye `--kayip-isaretle` ve `AD DEĞİŞMİŞ` raporu ekle. `rehber/09` adım 3 listesini tamamla (`programlar.json`, `konu-takip.json`, `projeler.json`).
  - Dokunulacaklar: `rehber/03`, `rehber/09`, `arsiv-guncelle.py`, yeni `kaynak-cikar.py`, `listeye-ekle.py`.
- **B5. Git takibi** (akış 06, 04, 11, 12)
  - Kanıt: Master origin'in 9 commit önünde. Hiçbir araç ahead/behind raporlamıyor. `.gitignore`'da `.env`/`*.key` deseni yok. Depo private mi doğrulanmıyor. Boyut büyümesi izlenmiyor. Birleşmiş artık dal var (`skill/lottiefiles-motion-design`). `git revert` için `-m 1` ve push sonrası geri alma adımı yazılı değil. Yeni makinede geri yükleme listesi yok.
  - En küçük değişiklik: Salt okuma `araclar/git-durum.py` yaz (ahead/behind, kirli dosya, izlenmeyen klasör, boyut eşiği, public ise uyarı, gizli desen taraması). Oturum başı ve aylık görev çağırsın (push yine yalnız kullanıcı isteğiyle). `.gitignore`'a `.env*`, `*.pem`, `*.key` ekle. `rehber/02` geri alma ve `README` geri yükleme listesini yaz.
  - Dokunulacaklar: yeni `git-durum.py`, `.gitignore`, `rehber/02`, `README.md`.
- **B6. Yedek envanteri ve hatırlatma** (akış 12, 04, 07)
  - Kanıt: Yedek kuralı `rehber/11` ve `DURUM.md` arasında dağınık. Silme tetiği geçiş notunda. Yedek yaşı hiçbir araçta yok. Ayar yedeği düz metin API anahtarı içerebilir. Proje yedeği yalnız Claude/Codex dosyalarını kapsıyor. `.skill-kutuphanesi/yedek` git'e girebilir. Proje yedeği 10'a kırpılıyor.
  - En küçük değişiklik: `rehber/12-yedek-ve-geri-alma.md`, `yedekler.json` (yol, tür, tarih, silme tetiği, `gizli_icerir`) ve `araclar/yedek-denetim.py` yaz. Aylık raporda göster, kendi silme. `yedekle()` ilk yedekte `.skill-kutuphanesi/.gitignore` yazsın.
  - Dokunulacaklar: yeni `yedek-denetim.py`, `yedekler.json`, `skill-ekle.py` (`yedekle`), `rehber/12`.
- **B7. Program denetimi sert kontroller** (akış 07, 04)
  - Kanıt: `program-denetim.py` yedek varlığını ve ortam anahtarını denetlemiyor. 404 ağ hatası yutuluyor ve `eski_adlar`'a bakılmıyor. Çıkışı hep 0, "KART ESKİ" sessiz (HyperFrames 0.9.23 → 0.9.33, OpenMontage 244 commit geride). `etsyotomasyon` (üçüncü taraf, imzasız exe) için doğrulama alanı yok. Programı kullanan projeler kayıtlı değil.
  - En küçük değişiklik: `program-denetim.py`'ye `--oncesi <ad>` (yedek, sabit sürüm, ortam anahtarı) ve KAYIP/TAŞINMIŞ ayrımı ekle. Kart şemasını tüm kartlar için `test.py`'de denetle. `etsyotomasyon` kartına `dogrulama` alanı ekle. Programlar için projeyle eşleme `proje-kullanimi.py`'de.
  - Dokunulacaklar: `program-denetim.py`, `programlar.json`, `test.py`, `rehber/11`.
- **B8. Yeni kaynak akışı kapıları** (akış 02)
  - Kanıt: Lisans, yol taraması ve güvenlik taraması kapı değil (`yol-tara.py` çıkışı hep 0, güvenlik taraması yok). Kaynak kaydında onay/tarih alanı yok. Test adımı rehber, prompt ve zincirde farklı sıralarda. `kaynaklar.json` şeması denetlenmiyor. `github-skill-listesi.py --ekle` onay sormuyor. Eklemenin geri alma yolu yazılı değil. `dogrula.py` uyarıda çıkış 0 veriyor.
  - En küçük değişiklik: `dogrula.py --siki` ve `lisans_onay`, `eklendi`, `onay` alanları ekle. Çözülemeyen yol için UYARI/HATA. Salt okuma güvenlik taraması ekle. `rehber/03` adım 4'ü tek sıraya indir (prompt 07 aynı olsun), geri alma 3 satırı ve kirli ağaçta dur kuralı ekle.
  - Dokunulacaklar: `dogrula.py`, `kaynak-cek.py`, `yol-tara.py`, `github-skill-listesi.py`, `rehber/03`, `promptlar/07`.
- **B9. Araç yönetim akışı eksik** (akış 09, 01, 11)
  - Kanıt: Yeni AI aracı ekleme akışı yazılı değil. Elle doğrulama tarihi ve aylık "araç belgesi değişti mi" kontrolü yok. `promptlar/` içinde program, kaynak çıkarma ve yeni araç istemleri yok.
  - En küçük değişiklik: `araclar.json` yaz (ad, proje skill klasörü, talimat dosyası, son doğrulama tarihi). `rehber/01`'e "Yeni AI aracı" bölümü ekle. `promptlar/13-15` yaz. Aylık zincire "araç belgeleri değişti mi" notu ekle.
  - Dokunulacaklar: `araclar.json`, `rehber/01`, `promptlar/*`, `dogrula.py`.

**(C) İsteğe bağlı**
- `kaldir()` kardeş skill bağımlılığına ve boş rol dosyasına bakmasın (`skill-ekle.py:1223`). `--kaldir hepsi` sonrası kilit ve blok temizliği ile "projeyi takipten çıkar" adımı.
- `guncelle()` tek elle değişmiş skili HATA yerine UYARI ile atlasın (`--haric`). Windows için `.gitattributes` önerisi ve CRLF farkı için ayrı uyarı kodu.
- Git'siz projeler için zip uyarısı. `.skill-kutuphanesi/yedek` için `.gitignore` zorunluluğu.
- Reddedilen aday için `tekrar_bak` tarihi. Aday program keşfi (SKILL.md'siz repolar). `--karar` doğrulaması ve toplu karar dosyası. Aday eleme harf duyarlılığı.
- `ad_devral` yaşam döngüsü. `parmak_izi` kopyasını `ortak.py`'ye taşıma. `promptlar/README` sıralaması. `git bundle` ikinci yedek. Depo görünürlük kontrolü (`gh repo view`).

**Bölüm 3: İş paketleri (dosya kümeleri ayrık)**
- **P1 Araç desteği.** Sahibi: `skill-ekle.py`, `araclar.json`, `rehber/01`, `rehber/04`, `promptlar/01,03`. Bitti sayılır: `--arac` seçimi ve `GEMINI.md` bloğu çalışır, BİLGİ satırları çıkar, kilitte `araclar` yazılır. Kanıt: `test.py` yeni testleri, `skill-ekle.py --kuru` geçici projede, `duman-testi`.
- **P2 Genel klasör bekçisi ve boşaltma rehberi.** Sahibi: yeni `genel-bekci.py`, `notlar/genel-klasor-tabani.json`, `rehber/12-genel-klasor-bosaltma.md`. Bitti: bekçi çıkış 0/1 verir, vendor klasörleri izinli, prosedür yazılı. Kanıt: bekçi gerçek klasörde, `test.py`.
- **P3 Yedek ve git durumu.** Sahibi: `git-durum.py`, `yedek-denetim.py`, `yedekler.json`, `rehber/12-yedek-ve-geri-alma.md`, `.gitignore`, `README.md`. Bitti: iki araç salt okuma çalışır, iki mevcut yedek kayıtlı. Kanıt: araçlar elle çalıştırılır, `test.py`.
- **P4 Aylık görev ve özet.** Sahibi: `aylik-ozet.py`, `arsiv-guncelle.py`, görev SKILL.md kopyası, `rehber/02`, `promptlar/08`, `notlar/son-aylik-calisma.txt`. Bitti: kirli ağaçta dur yerine rapor, `program-denetim` ve `yol-tara` C1 ve C2'de, 35 gün uyarısı. Kanıt: `arsiv-guncelle.py` rapor modu, `test.py`.
- **P5 Proje takibi.** Sahibi: `proje-kullanimi.py`, `projeler.json`, `rehber/10`, `promptlar/12`, `notlar/proje-durumu.md`. Bitti: `--saglik`, `--tara-kayitsiz`, `--yetim` çalışır, kayıtsız klasörler listelenir. Kanıt: araç çıktısı, `dogrula.py` (ilgili satır).
- **P6 Programlar.** Sahibi: `program-denetim.py`, `programlar.json`, `rehber/11`, `promptlar/13`. Bitti: kartlar yeni alanlarla, `--oncesi` çalışır, 404 ayrımı yapılır. Kanıt: `test.py` kart denetimi, `program-denetim.py` (yazma kendi çıktı dosyasına).
- **P7 Kaynak yaşam döngüsü.** Sahibi: `kaynak-cek.py`, `yol-tara.py`, `github-skill-listesi.py`, `kaynak-cikar.py`, `listeye-ekle.py`, `rehber/03`, `rehber/09`, `promptlar/07,14`, `github-trend.py`, `konu-takip.py`, `populer-tarama.py`. Bitti: çıkarma ve geri alma tek komut, eleme tek fonksiyon, `izle` tek anlam. Kanıt: `test.py`, `dogrula.py`, `kapsam-denetimi.py`.
- **P8 Belge, kural ve doğrulama bütünlüğü (en son).** Sahibi: `CLAUDE.md`, `AGENTS.md`, `BASLA.md`, `notlar/kararlar.md`, `README.md` (P3 ile `.gitignore`/geri yükleme bölümü çakışırsa P3'ten sonra), `PLAN.md`, `TEST_RAPORU.md`, `dogrula.py`, `duman-testi.py`, `ortak.py`. Bitti: kural 1 istisnası, eşitlik denetimi, eski belgeler rafta. Kanıt: `dogrula.py` 0 hata, `duman-testi.py`.
- Sıra notu: P8 ve `dogrula.py` değişiklikleri (P4, P5, P7 isteyebilir) en sonda birleşir. Önce commit, sonra genel klasör boşaltması.

**Bölüm 4: Yalnız kullanıcının karar verebileceği sorular**
1. Genel klasörler boşaldıktan sonra HyperFrames ve OpenMontage'ın Claude dışındaki araçlarda (Codex, Antigravity, Cursor) girişini hangi yolla kurayım: proje `AGENTS.md` notu mu, tek giriş skili mi?
2. Gemini CLI ve Copilot CLI bu Mac'te kurulu değil; yine de `GEMINI.md` ve `.github` düzenini şimdiden kurulumda desteklemeli miyim, yoksa yalnız kurulu araçları (Claude, Codex, Antigravity, Cursor, VS Code Copilot) mı?
3. Windows'ta açılan projelerde (Etsy-Arif) varsayılan düzen kopya mı olsun (symlink yerine, aylık güncelleme kopyayı yenilesin)?
4. Aylık görev yalnız Claude zamanlamasıyla mı koşsun, yoksa her ajan oturumu açılışında 35 gün geçtiyse özet çıkarıp sana mı sorsun?
5. `CLAUDE.md` ve `AGENTS.md`'yi (kural 1 istisnası, `BASLA.md` satırı, kalıcı kararlar) değiştirmeme onay veriyor musun?
6. Kütüphane dışında tek yedek olan private GitHub'a 9 commit'lik birikimi push edeyim mi (ayrıca `git bundle` ikinci yedek ister misin)?