# Tasarım özeti (2026-11-11, salt okuma tasarım turu)

Sekiz iş paketinin son tasarımı `tasarim/tasarim-p*.md` dosyalarında. Bu dosya özet, erteleme, onay ve açık kalanları toplar.

Uygulama sırası: P3 → P1 → P2 + P5 + P6 → P7 → P4 → P8 (CLAUDE/AGENTS Yama A; Yama B ayrı onayla) → genel klasör boşaltması.

## p1-arac-destegi

Aşama 1 (şimdi yapılacak): skill-ekle.py'de --arac ortak / yalniz-claude takma adları (eski ikisi/claude çalışır), kilitte arac_secimi alanı, arac-* BİLGİ rapor satırları (hangi araç skilleri görür/görmez), arac-karisik HATA'sı, --araclar salt-okur komutu (+ --ozet-json, --siki; araç belgesi/sürüm kontrolü), --kuru'nun --yenile/--geri-al/--blok'ta uyulması, yedekte .skill-kutuphanesi/.gitignore (yalnız yedek/), JSON'dan korunan yollar (~/.gemini, ~/.cursor, ~/.copilot), Windows koruması.
yapay-zeka-araclari.json: {surum, araclar:[liste]}, 7 kayıt; anahtarlar claude-code, codex, antigravity, cursor, vscode-copilot (+ isteğe bağlı gemini-cli, copilot-cli). makine_geneli_yazar çıkarıldı; genel klasör listesinin tek sahibi P2 ek_klasorler.
Proje CLAUDE.md/AGENTS.md bloklarına kütüphane yolu ve "kütüphane oturumuna yönlendir" cümlesi eklenir (onaya bağlı, Q3).
rehber/14, promptlar/15 yeni; rehber/01, rehber/04, promptlar/01-05, 09, 11 güncellenir (Aşama 2 bayrak adları yazılmaz).
Aşama 2 (tasarlandı, yapılmayacak): GEMINI.md/--gemini-md, --haric, kaldir kardeş UYARI'sı ve boş rol temizliği, proje kilidi (yerine rehber/01 ve promptlar/09'da uyarı), ortak-kopya (Q1'e bağlı).
Önkoşul sırası spec başına eklendi (P3, sonra P1; P6/P8 P1 anahtarlarına, P4/P8 --araclar --ozet-json'a dayanır).

**Dosyalar**
- araclar/skill-ekle.py: düzenleme, Aşama 1 için yaklaşık +130 satır
- yapay-zeka-araclari.json: yeni, kök klasör, yaklaşık 360 satır, 7 kayıt
- rehber/14-yapay-zeka-araclari.md: yeni, yaklaşık 170 satır
- rehber/01-skill-ekleme-sureci.md: düzenleme (eski genel klasör cümlesi, araç düzeni bölümü, iki oturum uyarısı)
- rehber/04-kontrol-listesi.md: düzenleme (araç sorusu, arac-* satırları, .gitignore maddesi)
- promptlar/01, 02, 03, 04, 05, 09, 11: düzenleme (araç sorusu, düzen değiştirme, kopyalama dalı)
- promptlar/15-yeni-yapay-zeka-araci.md: yeni, yaklaşık 40 satır
- araclar/testler/test_p1-arac-destegi.py: yeni, yaklaşık 300 satır (A, B, C, F, H, I grupları; D, E, G Aşama 2)

**Ertelenen**
- GEMINI.md bloğu ve --gemini-md: Gemini CLI kurulu değil (D1), Antigravity AGENTS.md'yi okuyor
- --haric: yeni kod yolu, kazancı küçük; geçici yol kullanıcı kararı (--zorla ya da geri yükle)
- kaldir() kardeş bağımlılık UYARI'sı ve boş rol temizliği: --kaldir davranışını ve test.py'yi etkiler
- Proje kilidi .islem-kilidi: yerine rehber/01 ve promptlar/09'da 'aynı projede iki oturum' uyarısı
- ortak-kopya düzeni (M2): Q1 Windows kararına bağlı
- Antigravity, Cursor, Copilot, Gemini CLI için rol dosyası üretimi: format doğrulanmadı
- Codex [[skills.config]] name biçimi, CRLF uyarısı ve otomatik .gitattributes, gerçek araç denemeleri (denendi boş kalır)
- Düzeltme önerisindeki --arac takma adlarının ertelenmesi reddedildi: yaklaşık 8 satır, kilit değeri değişmiyor, A1'in özü

**Onay isteyen**
- Q1: Windows'ta açılan projelerde Codex ve Antigravity skilleri görsün mü (ortak-kopya, Aşama 2)
- Q3: proje CLAUDE.md/AGENTS.md bloklarına kütüphane yolu ve 'kütüphane oturumunda yap' cümlesi eklensin mi (mevcut projelerde sonraki yazımda blok uzar)
- Q4: ilk yazımda kilitte araclar yoksa notlar/proje-kullanimi.md'de '—' yerine 'claude, codex' görünür ve otomatik commit olur
- Herhangi bir kayıtlı projenin düzenini değiştirmek (ör. Etsy-Arif yalniz-claude -> ortak), yeni aracın genel klasörünü ek_klasorler'e eklemek, bu paketin commit'i: her biri o sırada onay ister; push yalnız kullanıcı isteyince

**Riskler**
- kilit_yaz artık ilk yazımda araclar yazıyor (aynı etkin değer); proje-kullanimi.md'de görünür değişiklik
- --kuru düzeltmesi eski hatalı davranışı değiştirir; test.py ve duman-testi.py'de --yenile --kuru yazmasına dayanan test olmadığı grep ile doğrulanacak
- Blok metni değişikliği (Q3) mevcut projelerde sonraki yazımda görünür; testlerin kapanış cümlesine dayanmadığı grep ile doğrulandı
- Korunan yol listesi büyüyor (~/.gemini, ~/.cursor, ~/.copilot); kayıtlı projeler ~/Documents altında
- Proje kilidi yok: aynı projede iki oturum aynı anda yazabilir; yalnız yazılı uyarı ve yedek var
- Antigravity, Cursor, Copilot'ta skill görünürlüğü ve çift listeleme denenmedi; belirsizler korunur, denendi boş
- --araclar dış komut çalıştırır (claude --version, codex --version); salt okur, 10 sn zaman aşımı, testler sahte komut kullanır
- Belge ile kod kayması: dogrula.py prompt 11 ve rehber/04'te yalnız kodda var olan bayrak ve kodlar yazılabilir; Aşama 2 adları yazılmamalı

## p2-genel-bekci

Final spec (revised). Read-only watchdog araclar/genel-bekci.py watches the machine-wide skill folders of 5 tools, lock file, commands, agents and instruction files against a baseline notlar/genel-klasor-tabani.json (written only with --taban-yaz --evet after user approval).
Reports YENİ/KAYIP/DEĞİŞTİ/KIRIK BAĞ/YENİ KLASÖR plus an owner per entry. Checks the HYPERFRAMES_SKIP_SKILLS line in 3 files (presence only, read line by line, fixed error phrases).
--ozet-json gives one JSON object and writes nothing. --plan <step> prints (never runs) backup, command, check and rollback text; --yedek-dogrula verifies the backup.
Review change: instruction, command and agent files are watched for existence only (no bytes/mtime), so user edits to ~/.claude/CLAUDE.md create no noise; DEĞİŞTİ stays for link targets, skill folders and the lock file.
rehber/12 holds the 10-section emptying procedure, the reappearance procedure and the backup-deletion reminder; promptlar/16 holds two ready prompts. Prerequisite line and order added. YENİ KLASÖR gives the 'new AI tool folder (rehber/14)' decision sentence.

**Dosyalar**
- araclar/genel-bekci.py: new, about 500 lines, stdlib only
- notlar/genel-klasor-tabani.json: new, generated only after user approval, not hand-written
- rehber/12-genel-klasor-bosaltma.md: new, about 250 lines Turkish, 10 sections
- promptlar/16-genel-klasor-bosaltma.md: new, about 50 lines, 2 prompts
- araclar/testler/test_p2-genel-bekci.py: new, about 40 cases, temp dirs only

**Ertelenen**
- Rest of the environment inventory (LaunchAgents, .env presence, venv pins): other packages and secret-bearing files
- launchctl getenv and Dock-app environment: not testable, stays an open gap
- Watching plugins, ~/.config/openmontage and ~/.openmontage trees: covered by P6 program audit
- Reading yapay-zeka-araclari.json automatically: ek_klasorler plus the YENİ KLASÖR safety net cover it
- --temizle auto-remediation: deliberately not built (D7)
- Windows paths and GEMINI.md rules

**Onay isteyen**
- First baseline write (--taban-yaz --evet) and every refresh
- Each emptying step 3, 4, 5a, 5b, 6, and the choice of move versus copy
- Step 2 edits to the user's entry skill, slash commands and global CLAUDE.md
- Adding the key line to any file; optional launchctl setenv
- Scheduled one-time reminder and the yedekler.json row
- CLAUDE.md/AGENTS.md rule-1 exception
- Deleting any backup (30 days and explicit 'sil')
- Decisions Q1-Q9 before emptying

**Riskler**
- Reading shell files that hold a plain-text key: line-by-line single-regex match, fixed phrases, leak test
- False alarms from vendor folders and unknown ~/.<x>/skills (izinli list, discovery, accept by refresh)
- mv leaves the backup as the single copy until step 7: --yedek-dogrula, lock copied and moved, same-device check
- Baseline drift if emptying is abandoned midway
- Exit-code rule: report mode follows D4, action modes exit 1 on refusal

## p3-yedek-git

Üç salt okuma parçası ve bir rehber eklenir. araclar/git-durum.py: gönderilmemiş commit sayısı ve yaşı, kirli ağaç, izlenmeyen klasör, artık ya da bekleyen dal, repo boyutu, yeni büyük dosya, gizli ad kalıbı, eksik .gitignore koruması, arsiv içinde gizlenen dosya ve istenirse GitHub görünürlüğü. araclar/yedek-denetim.py + yedekler.json: kütüphane dışı yedeklerin tek envanteri (var mı, yaş, izin, yanlış yer, kayıtsız klasör, silinebilir liste); hiçbir şey silmez. rehber/13: tek kural, geri yükleme adımları, saklama süresi, yeni makinede GitHub'dan kurma, makine durumu envanteri ve GitHub oturumu bitince ne yapılır. .gitignore'a kök düzeyine bağlı koruma bloğu eklenir; bu blok artık P4'ün yerel damga ve özet dosyası için iki satırı da içerir. Her iki araç --ozet-json, --kisa, --rapor, --siki destekler ve yalnız standart kütüphane kullanır. Bu revizyonda: P4'ün iki .gitignore satırı eklendi, yedek klasörü adı P2'nin adıyla (genel-klasorler-<tarih>) birleştirildi, P2'nin beş isteği tek tek yanıtlandı, P6 'program-yedegi' türü 'program' olarak eşlendi, yedekler.json tek envanter oldu (isteğe bağlı 'kayit' alanı P6'nın KAYIT.json'una işaret eder) ve spec başına uygulama sırası (Önkoşul) yazıldı.

**Dosyalar**
- araclar/git-durum.py: yeni, ~330 satır
- araclar/yedek-denetim.py: yeni, ~310 satır (kayıtsız klasörde bilinen ad kalıpları ve 'kayit' alanı denetimi eklendi)
- yedekler.json: yeni, ~40 satır, 2 kayıt (ayar-2026-11-11 gizli içerir, global-skills-2026-11-08)
- rehber/13-yedek-ve-geri-alma.md: yeni, ~225 satır
- .gitignore: düzenleme, 6 satırın sonuna kök düzeyine bağlı blok; P4 için /notlar/son-aylik-calisma.json ve /notlar/aylik-ozet.md dahil
- araclar/testler/test_p3-yedek-git.py: yeni, 42 test (40-42 bu revizyonda eklendi)

**Ertelenen**
- Projelerdeki .skill-kutuphanesi/yedek klasörlerinin envanteri: otomatik ve 10'a kırpılıyor, proje listesi P5'te; P5 sonrası --projeler bayrağı düşünülebilir
- .skill-kutuphanesi/.gitignore yazımı: skill-ekle.py P1'in, devir isteği yazıldı
- Taze klon için tek komutlu bootstrap betiği: rehber/13'teki beş komut yeterli, ikinci yol bakım yükü olur
- pre-commit hook: .git/hooks izlenmez ve klonda gelmez; tespit git-durum ile yapılıyor
- git LFS ve büyük dosya politikası, git gc önerisi: yalnız eşik ve karar satırı
- Windows davranışı: izin denetimi atlanır, test edilmedi
- Yedek bütünlük (hash) ve geri yükleme provası: elle ve onayla
- Sahipsiz boşlukların hiçbiri P3 dosyalarına dokunmuyor; hiçbiri alınmadı

**Onay isteyen**
- Uygulama sırası: önce commit edilmemiş programlar/ işinin commit'i (kullanıcı onayıyla), sonra P3, ardından P1, P2+P5+P6, P7, P4, P8, CLAUDE/AGENTS Yama B ve en son genel klasör boşaltması
- .gitignore eklemeleri (kütüphane kuralı gereği onaylı)
- Yeni eşikler: 5 commit ya da 7 gün, .git 300 MB, yeni dosya 5 MB, bekleyen dal 45 gün, gizli yedek en çok 30 gün, diğer yedekler 90 günde sorulur
- Yedek oluşturma, geri yükleme, silme ve silme_olay_tamam değişikliği her seferinde o anda
- Ayar dosyalarının (settings.json, .zshrc, .zshenv) ve genel skill klasörlerinin geri yüklenmesi, her dosya ayrı onayla
- İsteğe bağlı git bundle ikinci kopyası (ikinci_kopya_iste şimdilik false)
- skill/lottiefiles-motion-design birleşmiş dalının silinmesi, programlar/hyperframes ve programlar/openmontage commit'i, 9 commit'in push'u: yalnız kullanıcı isterse
- Zamanlanmış görev metni değişikliği P3'ün değil, P4'ün önerisi ve onaylıdır

**Riskler**
- Yeni .gitignore desenleri izlenen bir şeyi gizleyebilir: hepsi kök düzeyine bağlı ve tam ad; önce/sonra git status ve git ls-files -ci sayısı (1) karşılaştırılır; iki P4 dosyası bugün izlenmiyor (doğrulandı)
- P4 P3'ten önce uygulanırsa aylik-ozet dosyayı yazmaz; sıra Önkoşul satırıyla sabitlendi
- Araçlardan biri yanlışlıkla yazabilir: varsayılan yazma yok, yalnız --rapor; testler ağaç anlık görüntüsü ve --no-optional-locks ile doğrular
- Yavaş ya da takılan git/gh: her alt süreçte zaman aşımı, hata bilgi satırına düşer
- Gizli ad taramasında yanlış alarm: arsiv/ ve .example sonekleri hariç, varsayılan çıkış 0
- yedekler.json ile P6 KAYIT.json'un çift kayıt riski: tek envanter ve 'kayit' işaret alanı ile kapatıldı; P2/P6 metinlerinin uyarlanması bu paketin dışında
- gizli_icerir 'hayir' (global-skills yedeği) varsayıma dayanır: uygulayıcı yalnız adları listeleyerek doğrular
- Test dosyası adında tire var: importlib ile yol üzerinden yüklenir

## p4-aylik

Aylık zincir tek komut olur: `arsiv-guncelle.py --aylik`. Sırası: ön kontrol, kaynak raporu, yıldız listesi raporu, güncelleme ya da takip dalı, özet, damga. Master'a commit atılmaz; kirli ağaç her zaman yazma adımını durdurur ve `kismi` döner.
Yeni `aylik-ozet.py` rapor araçlarını `--ozet-json` ile toplar. Araç listesi `ortak.OZET_ARACLARI` (yoksa sabit yedek) ile P4'ün dört ağsız ekinden gelir: `skill-ekle --araclar` ve üç `--bekleyenler`. Aday sayıları önce bu araçlardan okunur, md regex'i yalnız yedektir.
Özet: en çok 5 aday adı ve toplam gösterir; `notlar/kararlar.md` kabul listesindeki kararları susturur; KAYIP işaretli kaynağı bir daha sormaz. Damga yoksa `guncelleme-gecmisi.md` tarihine bakar, o da yoksa soru üretmez.
`--hizli` (takma ad `--oturum`) ağsız, yazmasız ve 15 satır altındadır. `--yazmadan` zincir içi içindir.
`proje-kullanimi.py --saglik --yaz` tam modda çağrılır. Zincirde tazeleme dal içinde yapılır; özet sonrası master'daki izinli rapor kopyaları `git checkout --` ile geri alınır.
`reset --hard` ve `clean` yalnız `takip()`'in kendi dalında çalışır, başlangıç temizliği ve dal adı doğrulanınca. Rapor çıkış kodu 2 yalnız `--siki` ile verilir.
Uygulama iki aşamalıdır, ayrı commit ve onayla. Aşama 1: rapor toleransı, `--aylik --kuru`, `aylik-ozet.py`. Aşama 2: `--takip`, damga, `--aylik` gerçek koşusu, belgeler.
Belgeler: `rehber/02` güncellenir, `promptlar/08` yeniden yazılır, `zamanlanmis/aylik-guncelleme.SKILL.md` kütüphane kopyası yazılır. Asıl tetik oturum başı damga 35 gün kuralıdır; zamanlayıcı yalnız kolaylıktır.
Test dosyası `test_p4-aylik.py` 38 test içerir. Spec 11 bölümdür; bölüm 11 inceleme değişikliklerini ve reddedilenleri listeler.

**Dosyalar**
- araclar/aylik-ozet.py: yeni, ~350 satır, yalnız standart kütüphane, salt okuma, tek yazdığı dosya notlar/aylik-ozet.md
- araclar/arsiv-guncelle.py: düzenleme, ~230 satır, iki aşamada; geriye uyumlu
- rehber/02-guncelleme-yonergesi.md: düzenleme, bölüm 1b ve 1c ile asıl tetik paragrafı
- promptlar/08-aylik-guncelleme-onayi.md: yeniden yazım
- zamanlanmis/aylik-guncelleme.SKILL.md: yeni, canlı görev metninin kütüphane kopyası (canlıya kopyalamak onay ister)
- notlar/son-aylik-calisma.json: koşu zamanı damgası, git'e girmez, tohum yazılmaz
- araclar/testler/test_p4-aylik.py: yeni, 38 test, yalnız temp dizin ve sahte veri

**Ertelenen**
- `kaynak-cek.py --atla` uygulaması P7'nindir; bayrak gelene kadar eski 'durma' davranışı sürer
- `--kayip-isaretle` bayrağı yapılmaz. KAYIP işaretleme P7'nin rehber/03 E3 adımıdır, elle ve onayla
- 'Ayda en çok N aday' değerinin kendisi kullanıcı sorusudur; kararlar.md'ye P8 yazar. Özet yalnız 5 ad gösterir
- `DURUM.md` düzyazısından karar çıkarma yapılmaz (yanlış pozitif)
- `yol-tara.py` master'da koşmaz, yalnız dallarda
- Zamanlayıcının uyku ya da kapalı uygulamada sonradan çalışıp çalışmadığı doğrulanmadı
- `html_url` ile ad tespiti gerçek GitHub'da doğrulanmadı; tutmazsa kod bırakılır, yedek yol github-skill-listesi.py
- promptlar/10 satır 8 ve rehber/08 paragrafı, proje bloğunda kütüphane yolu denetimi: P8/P1'e devredildi
- Windows ve GEMINI.md kapsam dışı

**Onay isteyen**
- Canlı zamanlanmış görev metninin (~/.claude/scheduled-tasks/…/SKILL.md) değiştirilmesi: diff göster, yedek al, kopyala, doğrula. Bu pakette yalnız kütüphane kopyası yazılır
- Aşama 2'ye geçiş ve ilk gerçek `--aylik` koşusu (ağ, GitHub API hakkı, dal ve commit üretir, 15-40 dk; kirli ağaç önce kaydedilmeli)
- Davranış değişikliği: erişilemeyen tek kaynak `--uygula`'yı durdurmaz (P7 `--atla` gelince); `--dal` artık `takip/*` bekleyen dalıyla da engellenir
- `--aylik` master'a commit atmaz. Rapor dosyaları değişmişse commit kullanıcı onayıyla yapılır
- `gh auth login` gerekirse kullanıcı kendi terminalinde yapar
- `--birlestir`, `git branch -D`, push: her biri yalnız kullanıcı isteğiyle

**Riskler**
- `html_url` ile ad tespiti doğrulanmadı; yanlış alarm yalnız bilgi satırıdır, dosya yazmaz
- P6 `--ozet-json` koşusu `program-denetimi.md`'yi yazarsa master kirlenir. Zincir içinde `git checkout --` ile geri alınır, elle koşuda commit sorusu çıkar
- Zincir içi geri alma yalnız koşu başında temiz ağaçta ve yalnız izinli iki rapor yolunda çalışır. Aksi halde uyarır, dokunmaz
- `takip()` yarım kalırsa kalıntı riski: geri alma kendi dalında ve doğrulanmış dal adıyla; testler 30(e,g), 31b
- Çıkış kodu 2 yalnız `--siki` ile geldiği için eski çağıranlar etkilenmez
- Önkoşullar (P3 `.gitignore`, P7 `--atla`, diğer paketlerin `--ozet-json` araçları) gelmeden gerçek doğrulama tam olmaz; eksik araç `dikkat` olur, çökme yok
- `zamanlanmis/aylik-guncelleme.SKILL.md` skill sayılabilir: kapsam-denetimi ve dogrula'nın `**/SKILL.md` taraması bir kez grep ve koşuyla doğrulanır
- Aday sayısı araçların listelediği en çok 10 kayıttan türer ('en az N' denir); tam sayı için aracın kendi çıktısına bakılır
- Kabul listesi süzgeci alt dize eşleşmesidir; ≥8 karakter kuralı ve tarih sonekiyle sınırlandı, yine de fazla geniş bir ifade başka kararı susturabilir

## p5-proje-takibi

P5 ilk sürümde küçültüldü. araclar/proje-kullanimi.py'ye eklenenler: --saglik (notlar/proje-durumu.md, salt okuma), --tara-kayitsiz (kilitsiz skilli klasörleri bulur; yoksay yolları hiç açılmaz), --ozet-json [--yaz], --siki. projeler.json'ı yalnız dört yazıcı değiştirir: --ekle, --cikar, --tasindi, --yoksay (önce plan, onaydan sonra --evet). Çıkış kodu: giriş noktası genel olarak değişmez; eski kipler (bayraksız, --skill, --repo, düz --kontrol) kabukta hep 0 kalır. Gerçek 1 yalnız --saglik/--tara-kayitsiz --siki ve --kontrol --siki ile gelir. projeler.json'a 4 yeni anahtar: kayitsiz_tarama, yoksay (2 kayıt, D10), bilinen_projeler (5 proje), kendi_skilleri (akil-disi-*). Ertelenenler: --yetim, --program, --elle-taslak, --bilinenleri-yaz, --yoksay-kaldir, program_kullanimi (B7'nin proje tarafı). Spec'in başına Önkoşul/uygulama sırası eklendi. P1'in iki isteği devir bölümünde kabul edildi: kilitte olmayan skill klasörleri KAYITSIZ SKILL olur, araclar alanı olmayan ya da varsayılan seçimli kilit için BİLGİ satırı çıkar ve hata vermez. P1'in --ekle BİLGİ isteği ertelendi.

**Dosyalar**
- araclar/proje-kullanimi.py: düzenleme, 184 satırdan yaklaşık 480 satıra
- projeler.json: düzenleme, 4 yeni anahtar, eski anahtarlar aynı
- rehber/10-proje-kullanimi.md: düzenleme, 39 satır korunur, yaklaşık 60 satır eklenir
- promptlar/12-proje-kullanimi-ve-etki.md: düzenleme, 2 yeni kopyala bloğu
- araclar/testler/test_p5-proje-takibi.py: yeni, yaklaşık 20 test
- notlar/proje-durumu.md: yeni, araç üretir (elle düzenlenmez)

**Ertelenen**
- --yetim, --elle-taslak, --bilinenleri-yaz, --yoksay-kaldir: --saglik ve elle düzenleme aynı işi görüyor; yüzey 760 satırdan küçültüldü
- program_kullanimi ve --program (B7'nin proje tarafı, HyperFrames/OpenMontage hangi projede): ertelendi; bilgi şimdilik notlar/hf-om-gecisi/DURUM.md'de; P6'dan istek gelirse eklenir
- P1'in 'kurulum sonrası kapsam dışı proje için BİLGİ --ekle' ve proje_raporunu_yenile'nin projeler.json'a yazması isteği: reddedildi (ağacı kirletir); P1 devir bölümüne 'ertelendi: P5 --saglik zaten kapsam dışı projeyi listeler' yazılacak
- İki aracın aynı anda skill-ekle çalıştırmasına karşı proje kilidi: skill-ekle.py (P1) işi
- Windows'ta çalıştırma: test edilmedi, rehber öyle yazıyor
- Bozuk kilit.json'un bayraksız raporu çökertmesi (oku() L48): D2 gereği dokunulmadı, --saglik KİLİT OKUNAMIYOR der
- Proje başına git durumu ve yedek envanteri: P3'ün işi

**Onay isteyen**
- Uygulama onayı = projeler.json'ın içeriğinin onayı: iki yoksay kaydı (Psikolojik Danışman, İstatistik KIT; 2026-11-11), beş bilinen_projeler kaydı, Akıl Dışı için kendi_skilleri (akil-disi-*)
- Yazıcıların (--ekle, --cikar, --tasindi, --yoksay) her gerçek kullanımı o anda kullanıcı onayı ister: önce plan, açık evetten sonra --evet
- Aylık turda kayıtsız her skilli klasör için karar: kütüphaneyle yönet, yalnız izle ya da yoksay
- Gerçek takip işleri (taşınan proje için --yenile, bayat projeler için --guncelle, yetim için --kaldir, elle-kurulan.json yazımı) skill-ekle.py üzerinden ayrı onayla; P5 yapmaz
- notlar/proje-durumu.md'nin aylık commit'i (P4 karar verir); push yalnız kullanıcı isterse

**Riskler**
- projeleri_bul'a eklenen takipten-cikti filtresi bugünkü rapor çıktısını değiştirmemeli: koruma, uygulamadan önce ve sonra --kontrol ve notlar/proje-kullanimi.md'nin shasum'u aynı olmalı
- Kayıtsız tarama kullanıcı klasörlerini geziyor: yalnız klasör adı ve işaret adı bakılır, dosya içeriği ve .env açılmaz; yoksay yolları hiç açılmaz (os.scandir/lstat/stat kayıt testiyle kanıtlanır), bağlantılar izlenmez, derinlik ve klasör sayısı sınırlı
- skill-ekle.py dinamik yükleniyor; P1 işlev imzalarını ya da durum() sırasını değiştirirse test 23 ve test 6 yüksek sesle kırılır (istenen davranış)
- dogrula çıktısının metnine dayalı süzme (DOGRULA_TEKRAR, DIKKAT_DOGRULA): P1 cümleleri değiştirirse testler yakalar
- Aynı klasör adına sahip iki proje desteklenmez (AYNI AD İKİ YOL uyarısı)
- NFC/NFD (Danışman) yol eşleşmesi: _norm ve test 15 ile kapalı
- KAYIP mantığı yalnız kütüphane Mac'inde çalışır; başka makinede/bulutta bilinen_projeler dolu olsa da sessiz kalır

## p6-programlar

P6 programlar.json kartlarını iki katmanlı şemaya taşır: zorunlu çekirdek (giris_yolu, kurulum, geri_alma, cikarma, yedek, ortam_anahtarlari) ve isteğe bağlı alanlar (disariya_yazar, tedarik_dogrulama, kirici_surum, gizli_dosyalar, yerel_yamalar). program-denetim.py yeni kipler kazanır: --sema, --oncesi <ad> (4 durum satırı + 8 ana kontrol: yedek, sabit sürüm, ortam anahtarı, yerel değişiklik, repo, giriş yolu, gizli dosya, kırıcı aday), --iskelet, --pin-listesi, --ozet-json (diske hiçbir şey yazmaz), --siki, --cevrimdisi. 404 / ağ hatası / taşınmış repo ayrımı yapılır. Uzun prosedür metinleri (deneme adımları, yama uygulama adımları) kartlardan çıkıp rehber/11'e gider. Kart bulguları kütüphane geneli kapılarda (dogrula, test.py, --birlestir) UYARI olur; yalnızca bozuk programlar.json HATA'dır. rehber/11 yeni bölümleri, KAYNAK.md ek satırları, promptlar/13 ve test dosyası yazılır. Güncelleme, geri alma ve kaldırma otomatikleşmez: yedek, ön kontrol ve kullanıcının ayrı onayı ile adım adım yürür. Önkoşul sırası belgenin başında yazılıdır.

**Dosyalar**
- araclar/program-denetim.py: düzenleme, yaklaşık +700 satır (mevcut davranış, imzalar ve çıkış kodu korunur)
- programlar.json: düzenleme, 3 karta çekirdek ve isteğe bağlı alanlar eklenir (hedef: toplam 330 satır altı)
- rehber/11-program-yonetimi.md: düzenleme, 10 yeni bölüm (şema, giriş yolları, kurulum, yedek kaydı, ön kontrol, kırıcı sürüm, yerel yamalar, geri alma, çıkarma, taze ajan adımları, aylık takip)
- programlar/hyperframes/KAYNAK.md, programlar/openmontage/KAYNAK.md, programlar/etsyotomasyon/KAYNAK.md: düzenleme, birkaç satır
- promptlar/13-program-kur-guncelle.md: yeni, yaklaşık 30 satır
- araclar/testler/test_p6-programlar.py: yeni, yaklaşık 60-70 test

**Ertelenen**
- Güncelleme yürütücüsü (kendiliğinden yedekleyip kuran araç): D7 ve kullanıcı onayı kuralı
- --kayit-oneri yardımcısı: --sema KAYNAK.md tutarlılık denetimi yeterli
- Proje-program eşlemesi (B7 proje tarafı): P5'in işi
- OpenMontage 9 yamasının amacı ve basicsr yaması: ölçülmedi, tahmin yazılmaz; kullanıcıya sorulur
- etsyotomasyon release sha256 değeri: indirme gerektirir, onay ister
- Çalışan render denetimi (ps/lsof): salt-okur kapsam dışı
- Yedek silme hatırlatma zamanlaması: P3 ve P4
- Windows, Gemini CLI ve Copilot CLI girişleri: D1
- --oncesi'nden çıkarılan dışarıya yazar kontrolü ve varsayılan tedarik kontrolü (yalnız --tedarik bayrağıyla)
- npm provenance ve git imza doğrulaması: stdlib dışı araç gerekir

**Onay isteyen**
- Her gerçek güncelleme ayrı onay ister: HyperFrames 0.9.23 -> 0.9.33 ve OpenMontage (244 commit, git pull --ff-only)
- Geri alma, makineden kaldırma ve kütüphaneden kaldırma (programlar/<ad>/kaynak/ kalıcı silme) ayrı ayrı
- Yedek ve deneme klasörlerinin silinmesi her zaman sorulur
- HYPERFRAMES_NO_AUTO_INSTALL ve HYPERFRAMES_NO_UPDATE_CHECK tanımlamak (kabuk ve ayar dosyalarına yazar)
- OpenMontage origin adresini değiştirmek
- CLAUDE.md ve AGENTS.md 51. satır metni ve kural 1 istisnası (P8)
- OpenMontage boşaltma sonrası Claude Code giriş yeri kararı: kartta karar-bekliyor
- OpenMontage 9 yamasının amacının kullanıcıya sorulup karta yazılması
- etsyotomasyon release ikilisi için sha256 kaydı (indirme gerekir)
- commit edilmemiş programlar/ işinin commit'i; push yalnız kullanıcı isteyince

**Riskler**
- npm_son_surum ve git_son imzaları değişirse araclar/test.py:1620-1621 gerçek ağa gider: imzalar aynı, yalnız yan etkili _SON_HATA sözlüğü eklenir
- Bozuk veya eski şekilli kartlar main'i çökertebilir: sema_denetle try/except içinde, çıkış 0 kalır (test 25)
- --ozet-json stdout'a başka çıktı sızdırabilir: tüm koşu redirect_stdout(stderr) altında, test 26
- git status yol ayrıştırması (yeniden adlandırma, tırnaklı yol, izlenmeyen klasör) yama durumunu yanlış raporlayabilir: test 16 ve gerçek git init testi (test 22)
- ~/.zshrc okunurken gizli değer sızabilir: yalnız anahtar adı ve var/yok türetilir, test 15 sahte sırrın çıktıda olmadığını doğrular
- gizli_dosyalar yalnız lexists ile bakılır, dosya açılmaz (test 18)
- Kartlar uzayabilir: uzun metinler rehber/11'e taşındı; bütçe wc -l ile uygulamada ölçülür
- P5'in --program sorgusu belirsiz: yedek yol hazır
- Kart tek başına eksik alan yüzünden kütüphane doğrulamasını düşüremez: kapılar UYARI, yalnız bozuk JSON HATA

## p7-kaynak-yasam

Spec inceleme sonrası daraltıldı ve zorunlu düzeltmeler uygulandı (10 bölüm + bölüm 11 'Review changes').
1) kaynak-cek.py --atla owner/ad[,..] (K4) eklendi: büyük/küçük harf duyarsız, repo_agaci/indirme yok, 'UYARI: <repo> atlandı (arşiv kopyası korunur)', manifest'e girmez, kalan başarılıysa çıkış 0, bayrak yoksa :238-240 aynen, --help'te görünür, sahte repo_agaci ile test. arsiv-yerlestir.py:471-474 korumasını kodda yeniden doğruladım.
2) --kayip-isaretle iki tarafta da 'ertelendi'; P7 devrinden (c) silindi, P4'e satır 505 düzeltmesi yazıldı.
3) Başa 'Önkoşul' satırı (sıra 0-8; P7 4. sırada, P4'ten önce).
4) dogrula devri yeniden yazıldı: hepsi UYARI (HATA yok), yeni-kayıt kontrolleri yalnız HEAD'de olmayan kayıtta, mevcut 181 kayıt asla yeni sayılmaz, HATA'ya yükseltme ayrı kullanıcı onayı. P8 testine 'EMEKLI tipli/bilinmeyen anahtarlı kayıt aylık dogrula'yı geçirir' vakası zorunlu.
5) Kapsam daraltıldı: ekleme sırası A0..A17 -> A1..A9; github-trend, populer-tarama, github-skill-listesi değişmez; kaynak-cek K1/K3 ve listeye-ekle L2/L3 ertelendi. Şimdi kalanlar: kaynak-cikar.py --kuru, --atla, lisans_riskli, yol-tara --siki, listeye-ekle harf hatası düzeltmesi, konu-takip ortak eleme + doğrulanmış --karar + tek --bekleyenler (üç kaynağı özetler, kaynak başına en çok 5 ad), rehber/03,09, promptlar/07,14, kayip_tarihi veri düzeltmesi.
6) Sahipsiz boşluklardan alınanlar: B2 triyajı (en çok 5 ad + toplam; N sorusu P8 kararlar.md'ye), KAYIP kaydına kayip_tarihi, promptlar/10 satır 8 ve rehber/08 P8'e açıkça devredildi.

**Dosyalar**
- araclar/kaynak-cikar.py: yeni, ~400 satır (yalnız --kuru etki raporu, adımlar, geri alma, --json, --github okuma)
- araclar/kaynak-cek.py: düzenleme ~40 satır (--atla, atla_kumesi, RISKLI_LISANS, lisans_riskli)
- araclar/yol-tara.py: düzenleme ~50 satır (--siki, kapi_kontrol)
- araclar/listeye-ekle.py: düzenleme ~6 satır (küçük harf üyelik anahtarı) + docstring
- araclar/konu-takip.py: düzenleme ~150 satır (elenecekler/eleniyor/aday_mi, karar_uygula, İzlenenler bölümü, --bekleyenler [--ozet-json] [--siki])
- rehber/03-yeni-skill-ekleme.md: düzenleme (A1..A9, D-H bölümleri, karar kutusu, yeni alanlar)
- rehber/09-ad-kimlik-ve-cakisma.md: düzenleme ~15 satır
- promptlar/07-yeni-skill-reposu-ekle.md: yeniden yazım (A1..A9)
- promptlar/14-kaynak-cikar.md: yeni, ~20 satır
- araclar/testler/test_p7-kaynak-yasam.py: yeni, 34 test, ~700 satır
- kaynaklar.json: tek satır veri düzeltmesi (J-DTurner/etsy-api-skill kayip_tarihi), kullanıcı onayıyla
- DEĞİŞMEZ (bilerek): araclar/github-trend.py, araclar/populer-tarama.py, araclar/github-skill-listesi.py

**Ertelenen**
- github-trend.py ve populer-tarama.py yeniden yapılanması: aylık zincirin adımları, risk/fayda düşük; populer --karar izle hatası rehber/03 F ile belgeyle kapatıldı
- github-skill-listesi.py --evet/--geri-al/onay/yedek ve listeye-ekle L2/L3: kullanıcının onaylamadığı davranış değişikliği (etkileşimsiz kabukta durur); A9 yalnız listeye-ekle.py'yi adlandırır
- kaynak-cek.py K1 (erken hata) ve K3 (özet bloğu): mevcut çıkış kodunu/çıktıyı değiştirir; yerine rehber/03 A5 okuma talimatı
- --yeniden-ac ve tekrar_bak: nadir; elle düzenleme yeter
- --kayip-isaretle: kayıp işaretleme kullanıcı kararı; rehber/03 E3 elle adım geçerli (P4 ve P7 ikisi de uygulamıyor)
- kaynak-cikar.py --uygula: çıkarma nadir, güvenli sürüm maliyeti yüksek
- toplu karar dosyası, program adayı keşfi, SKILL.md güvenlik tarayıcısı: ayrı tasarım/başka paket

**Onay isteyen**
- Her yeni kaynak eklemesi (A3) ve riskli lisans sorusu; her kaynak/skill çıkarma (D1), projeden skill kaldırma proje başına ayrı
- GitHub'a yazma (listeye-ekle.py) ve yıldız/liste kaldırma; push yalnız kullanıcı isterse
- Kayıp işaretleme/geri dönüş (E3/E4, elle), emekli etme (H)
- Aday kararları (--karar eklendi/reddedildi/izle): karar kullanıcının
- kaynaklar.json'da J-DTurner/etsy-api-skill kaydına tek alanlık kayip_tarihi ekleme (2026-11-10)
- CLAUDE.md/AGENTS.md değişiklikleri (P8 üzerinden)
- Herhangi bir dogrula kapısını UYARI'dan HATA'ya yükseltme (ayrı, sonraki karar)

**Riskler**
- yol-tara çıkış kodu sözleşmesi (test.py:501-503,519-520; arsiv-guncelle.py:201-203): --siki isteğe bağlı, bayraksız davranış aynı
- kaynak-cek.py aylık zincirin aracı: --atla varsayılan boş, eski yol aynı; test eski HATA durmasını doğrular
- konu-takip raporu görünür biçimde değişir (3 izlenen repo ayrı bölüme geçer, 67 karışık harfli anahtar eşleşir); konu-takip.py --rapor test için çalıştırılmamalı
- tara() aylık zincirde: yalnız üyelik testi ve bilinenler imzası değişir
- kaynak-cikar.py 22 MB registry'yi bir kez yükler; proje bilgisi yoksa karar asla 'hazir' olmaz
- github-trend/populer-tarama bilinen eksikleri kalır (trend tablosu reddedilenleri gösterir, populer --karar izle gizler): yalnız belgeyle azaltıldı
- dogrula UYARI sayısı artarsa A7 karşılaştırması kullanıcıya gösterir; HATA yok olduğu için aylık zincir geri alınmaz
- kaynaklar.json tek satır düzenleme json_yaz ile yeniden biçimlenmemeli (git diff --stat 1 ekleme)

## p8-butunluk

Son spec 11 bölümlü (bölüm 11 = inceleme değişiklikleri). Önkoşul sırası başa yazıldı: 0 programlar commit'i, P3, P1, P2/P5/P6, P7, P4, en son P8, sonra Yama B, sonra boşaltma.
Tek cümlelik birleştirme kuralı: dogrula.py'ye eklenen her yeni denetim UYARI. HATA yalnız bozuk var olan JSON ve CLAUDE.md ile AGENTS.md farkı. Eksik dosya, şema, P7 kapıları (G-ONAY, G-LISANS, G-YOL, G-ONAY-CIKAR, G-KAYIP, G-TIP) hepsi UYARI. P7 kapıları yalnız HEAD'e göre yeni kayıtta çalışır.
--oturum her yerde --hizli oldu (BASLA, CLAUDE/AGENTS maddesi, duman adım 11, P4-A isteği). P4'ün 35 gün sorusu ve oturum başı cümlesi aynen girdi.
E4, P1'in gerçek dosyasına göre yeniden yazıldı: araclar bir liste, anahtar kümesi `anahtar` alanından, tarih alanı dogrulama_tarihi, 120 gün kuralı kalktı.
6.2 devir kaydı P1, P2, P3, P4, P5, P6, P7 satırlarıyla doldu. Her isteğin kararı yazıldı.
kararlar.md'ye `## Karar bekleyenler` (`- [ ]` kutuları), `## Kabul edilen bekleyenler (aylık özette susturulur)` ve N sorusu eklendi.
Patch A'ya P1 adım 1 metni, P7'nin iki maddesi, 'Yeni skill ekledim' düzeltmesi ve P4'ün aylık satırı girdi. Yama B tek metin olarak sabitlendi; P2 ve P6 yalnız ona atıf yapar.
Kaldırılanlar: BILINEN_UYARILAR, dogrula --siki, dogrula'daki rapor ve DURUM bayatlığı. Bayatlık tablosu ortak.rapor_yasi_satirlari olarak aylik-ozet'e (P4, isteğe bağlı) verildi. Duman'da emekli-rol uyarısı için tek yerel, bitiş tarihli süzgeç var.
OZET_ARACLARI'na skill-ekle --araclar ve üç --bekleyenler aracı eklendi. Duman program-denetim'i --oncesi hyperframes --cevrimdisi ile koşar.
Test dosyası yalnız geçici dizin ve sahte veri kullanır; gerçek depo maddeleri kabul bölümüne (10) taşındı.
Sahipsiz boşluklardan alınanlar: B2 N sorusu, promptlar/10 satır 8, rehber/08 paragrafı, BASLA'ya Windows notu, ortak 'kabul edilen' listesi.

**Dosyalar**
- BASLA.md: yeni, ~110 satır
- notlar/kararlar.md: yeni, K-01..K-23, değişen kararlar, sorular (N dahil), Karar bekleyenler, Kabul edilen bekleyenler
- CLAUDE.md ve AGENTS.md: Yama A ile ~+14 satır, tek cp ile eşit; Yama B ayrı onaylı commit
- README.md: düzenleme (araç, rehber 11-14, prompt sayısı, araç satırları)
- promptlar/README.md: düzenleme (sıra, satır 12, satırlar 13-16)
- araclar/dogrula.py: düzenleme, ~+220 satır (denetimler A, A2, B, B2, C, E1-E6, F, H, K; yazdırma bloğuna dokunulmaz)
- araclar/ortak.py: düzenleme, dosya sonuna ekleme (genel izler, OZET_ARACLARI 9 araç, ozet_json_gecerli, RAPOR_YASI, rapor_yasi_satirlari)
- araclar/duman-testi.py: düzenleme (kirli-ok, yerel emekli-rol süzgeci, adım 10 ve 11)
- araclar/test.py: düzenleme (alt_testler yükleyici, parmak_izi ortağa, P6 --sema kontrolü)
- araclar/testler/test_p8-butunluk.py: yeni, 26 durum
- notlar/rafta/OKU.md ve üç belgenin taşınması (PLAN.md, Kullanılacak Promt Örneği.md, yerel-yapilacaklar-2026-11.md): onayla
- promptlar/10-kutuphane-saglik-kontrolu.md satır 8 ve rehber/08-test-sureci.md paragraf: küçük düzenleme, sahipsizden alındı

**Ertelenen**
- dogrula.py --siki ve bilinen-uyarı kabul listesi: bakım yükü nedeniyle alınmadı, ihtiyaç doğarsa 10 satırlık iş
- Rapor ve DURUM bayatlığı dogrula'da yok: yalnız aylik-ozet tam modunda, P4 isteğe bağlı kabul ederse
- Antigravity, Cursor, VS Code Copilot için gerçek araç duman adımı: başsız komut doğrulanmadı
- GEMINI.md oluşturma: D1 gereği kapalı, yalnız kod taslağı ve isteğe bağlı A2 denetimi
- --kayip-isaretle bayrağı: P4 ve P7 ikisi de ertelendi, rehber/03 E3 elle adım olarak kalır
- kaynak-cikar --json duman satırı: P7 kendi testleriyle kapsıyor
- dogrula --ozet-json
- GLOBAL_KLASORLER'i Cursor, Gemini, Copilot klasörlerine genişletmek: P1 dosya davranışını değiştirir, D2
- Windows ve CRLF/.gitattributes denetimleri: kullanıcı kararı bekliyor

**Onay isteyen**
- CLAUDE.md ve AGENTS.md Yama A (P1, P2, P3, P4, P5, P6, P7 metinleri birleşik, kural değişmez, tek cp ile eşitlenir)
- Yama B (kural 1 istisnası) ayrı commit, ilk boşaltma ya da program güncellemesinden önce, kullanıcının açık evetiyle; ardından Claude hafızasındaki skill-kutuphanesi.md notunu güncelleyip güncellememe sorusu
- PLAN.md, Kullanılacak Promt Örneği.md, yerel-yapilacaklar-2026-11.md dosyalarını notlar/rafta/'ya git mv ile taşıma
- promptlar/10 satır 8 ve rehber/08 küçük belge düzenlemeleri
- Her commit kullanıcı onayıyla; 10 commit push edilmemiş durumda, push yalnız kullanıcı isteyince
- Yeni dogrula UYARI'larından birini HATA'ya yükseltmek ayrı gelecek karar
- İsteğe bağlı GEMINI.md taslağı ve git bundle ikinci yedek kullanıcıya ait
- DURUM.md güncellemesi kütüphane oturumunda
- TEST_RAPORU.md yenilemek için skill-calistir.py çalıştırmak yalnız istek üzerine

**Riskler**
- Yeni dogrula denetimi aylık --birlestir'i geri sardırabilir: birleştirme kuralı ve test durumu 20 (HATA yolu yalnız iki)
- Bayrak denetimi (F) yanlış pozitif verebilir: statik eşleştirme, aynı backtick aralığı, ilk koşuda bulgu listesi commit mesajında
- Duman adım 11 tüm paketler inmeden kırmızı olur: yalnız kabulde koşulur; program-denetim --cevrimdisi ile ağa çıkmaz
- Parmak izi daha çok klasörü kapsıyor: HyperFrames ya da başka araç aynı anda yazarsa yanlış başarısızlık, mesaj girdileri listeler
- CLAUDE.md ~14 satır uzar: ayrıntı BASLA.md'de
- P7 kapıları commit sonrası görünmez olur (yalnız HEAD'e göre yeni kayıt): bilerek, rehber/03 A9 commit öncesi dogrula çalıştırır
- Eski kaynak kayıtları G-TIP kuralına takılırsa kural gevşetilir, 181 kayıt düzenlenmez
- Kuralın tek taraflı CLAUDE.md düzenlemesi: HATA ile hemen görünür
- Tasarım aşamasında arsiv-guncelle.py --help yanlışlıkla başlatıldı, durduruldu, hiçbir şey yazmadığı doğrulandı (bölüm 9)

## Kontrol notları

Genel durum: sekiz spec iyi ayrılmış, dosya sahipliği ihlali yok (her paket yalnız kendi dosyalarını düzenliyor; ortak dosya istekleri devir bölümlerinde, test.py/dogrula.py/ortak.py/duman/CLAUDE/AGENTS/README yalnız P8'de). D5 (kendi test dosyası, N/N test geçti, geçici dizin) hepsinde var; yalnız P8 testleri 26, 33-36 ve P1 test 44 gerçek depoyu okuyor, kabul bölümüne taşınmalı. D4 --ozet-json: P2, P3, P5, P6, P7 ve P1 (--araclar) sözleşmeye uygun; P5 `--yaz` yalnız istenirse yazar. Asıl sorunlar uygulama arayüzlerinde: (1) --oturum / --hizli adı, (2) P3 .gitignore'da P4'ün iki satırı yok, (3) P7'de --atla yok, (4) P1 anahtar/biçim (copilot, liste) P6-P8 beklentisine uymuyor, (5) P4 P1 ve P7'nin --ozet-json araçlarını çağırmıyor ve proje-kullanimi'ye --yaz vermiyor, (6) P8 devir kaydı P1, P4, P7 için henüz yazılmamış. Kapsam: A1-A7 ve B1-B9 kapanıyor (B4'ün --atla parçası ve B2 'N aday' kuralı düzeltmelere bağlı); 12 senaryo ve eleştirmen bölüm 2 ile 4 kapalı ya da gerekçeyle ertelenmiş (Windows ortak-kopya, rol dosyaları, uygulayan kaynak-cikar, kaçan görev bildirimi). Uygulama sırası: 0 mevcut işin commit'i, 1 P3, 2 P1, 3 P2 + P5 + P6, 4 P7, 5 P4, 6 P8 (CLAUDE/AGENTS Yama A, ardından ayrı onaylı Yama B), 7 genel klasör boşaltması. Zorunlu düzeltmeler uygulanmadan P4 ve P8 yazılırsa duman-testi ve --hizli gerçek depoda 'araç yok/çalışmadı' dikkat satırları üretir."]

Genel olarak tasarımlar D1-D12'ye büyük ölçüde uyuyor: makineye, kabuk dosyalarına, ayarlara, zamanlanmış göreve ve proje klasörlerine yazan bir araç yok (P4 zamanlanmış görev metnini kütüphane kopyası olarak veriyor, P2/P6 yalnız plan ve ön kontrol basıyor), git fetch yalnız P3'te açık --uzak bayrağıyla, push hiçbir yerde yok, dal silme yalnız aracın kendi açtığı dalda ve mevcut --birlestir yolunda. Sırlar yalnız varlık olarak denetleniyor (P2 ve P6 testleri sahte sır ile sızıntı sınıyor). Kayıt, kaynaklar ve kartlara proje adı yazılmıyor; proje adları yalnız P8'in notlar/kararlar.md karar günlüğünde ve P5'in projeler.json'ında geçiyor, bu D8'e aykırı değil.\n\nEn büyük riskler yazma ya da gizlilik değil, geriye uyumluluk ve gürültü: (1) dogrula.py'nin aylık --uygula/--birlestir içinde HATA ile master'ı geri aldığı bilindiği halde P2, P6, P7 yeni kontrolleri HATA olarak istiyor ve bu P8'in 'yalnız UYARI' ilkesiyle çelişiyor; tek bir birleştirme kuralı gerekli. (2) P5'in giriş noktası çıkış kodu değişikliği test.py:1681'i gerçek veriyle kırabilir. (3) P4 ile P8 arasında bayrak adı uyuşmazlığı var (--hizli / --oturum). (4) P4 zincirinde gözetimsiz master commit'i ve reset --hard. (5) P2'nin talimat dosyası mtime izlemesi her ay gürültü üretir.\n\nAşırı inşa: skill-ekle.py (P1 Aşama 2), arsiv-guncelle.py (P4 --takip ve damga), kaynak-cek.py/konu-takip.py/github-trend.py/populer-tarama.py (P7 yeniden yapılanma), proje-kullanimi.py (P5 yüzey genişlemesi) için en büyük sadeleştirme kazancı ertelemede. Hepsini iki aşamaya bölmek ve ilk aşamada yalnız salt okur raporları, --atla bayrağını, rehber metinlerini ve BİLGİ satırlarını almak D2'ye en yakın yol. Taze bir Codex/Antigravity ajanı BASLA.md ve AGENTS.md'den çalışabilir; Claude'a özgü tek bağımlılık zamanlanmış görev ve Claude hafızası, ikisi için de oturum başı --hizli ve notlar/kararlar.md karşılığı var, yeter ki tetik zamanlanmış göreve değil damga kuralına dayansın."

## Tasarım turunda sahipsiz görülen maddeler (düzeltme turunda paketlere dağıtıldı; uygulamada teyit edilir)

- B2 'aylık en fazla N adayı karara bağla' triyaj kuralı: P7 'P4/P8 işi' diye erteledi, P4 ve P8 almadı (320 aday birikimi). Öneri: P4 aylik-ozet aday satırlarında en fazla 5 aday adı + toplam sayı gösterir; N değeri kullanıcı sorusu olarak kararlar.md 'Henüz sonuçlanmamış sorular'a girsin.
- `--kayip-isaretle` (kayip_tarihi yazan işaretleme): P7 P4'ün, P4 P7'nin işi sayıyor. Ya P7 `kaynak-cikar.py` dışında ayrı yazan bayrak olmadığını belgeler ya da kullanıcı onayıyla elle E3 adımı kalır (düzeltmede 'ertelendi' önerildi).
- promptlar/10-kutuphane-saglik-kontrolu.md satır 8 eski '44 güvenlik testi' sayısı: P8 'sahipsiz' dedi, hiçbir paketin listesinde yok. Öneri: P8'e atanır (tek satır, sayıyı sil).
- rehber/08-test-sureci.md: P8 araclar/testler/ yükleyicisini test.py'ye eklediğinde test sürecini anlatan belge bayatlar; kimsenin dosya listesinde yok (P8'in sahip listesinde değil). Öneri: P8 tek paragraf ekler (araclar/testler/test_<paket>.py, son satır N/N test geçti).
- Mevcut kaynaklar.json KAYIP kaydında (J-DTurner/etsy-api-skill) kayip_tarihi yok: P7 G-KAYIP UYARI'sı ilk koşuda tetiklenir; P7 'aynı değişiklikte ekle ya da bilinen uyarı' dedi, P8 bilinen uyarı listesi (en çok 5, bitiş tarihli) bunu hesaba katmıyor. Karar: kayip_tarihi kaydı P7 uygulamasında eklenir.
- P4'ün `aylik-ozet.py --hizli` ve P8'in duman/BASLA çağrısı yapay-zeka-araclari.json bayatlığını (`--araclar`) hızlı modda göstermiyor; yalnız tam modda: kabul edilebilir ama rehber/14 aylık kontrolün tam modda olduğunu açık yazmalı.
- P6 `--ozet-json` koşusunun notlar/program-denetimi.md'yi yazıp yazmadığı belirsiz (P6 'aynı koşu', P4 'diske yazmaz'): P6 uygulayıcısı açıkça karar vermeli ve P4 sözleşmesi buna göre yazılmalı (bkz. p4 düzeltmesi).
- Windows (Q1/M2) ve Gemini CLI GEMINI.md: bilinçli ertelendi, kullanıcı kararı bekliyor; kapsam açığı sayılmaz ama BASLA 'araç' bölümünde Windows'ta skill-ekle.py çalışmaz notu P8'de olmalı (P1 rehber/14'te var).
- Hiçbir paket yeni makinede/taze klonda 'damga yok' durumunu tanımlamıyor: notlar/son-aylik-calisma.json ve notlar/aylik-ozet.md gitignore'da, bu yüzden taze klonda ilk oturum başı --hizli her seferinde '35 gün geçti' sorusu üretir. Sahip: P4 (damga yoksa 'ilk kurulum, soru yok' diye davransın).
- Yeni araçların (genel-bekci, git-durum, yedek-denetim, proje-kullanimi --saglik, program-denetim --ozet-json) --ozet-json çıktısında 'karar_bekleyen' tekrarlı cümleler aylık özette birikir; kapatılmış kararın (kabul edildi) nerede tutulup bir daha çıkmayacağı yalnız P2 taban 'kabul edildi' listesinde var, P3/P5/P6 için yok. Sahip: P4 aylik-ozet ortak bir 'kabul edildi' listesi (örneğin notlar/kararlar.md onay kutuları) okumalı.
- CLAUDE.md ve AGENTS.md Codex/Antigravity'de ilk okunan dosyalar, ancak BASLA.md, rehber/12-14 komutları 'python3 araclar/...' biçiminde cwd'nin kütüphane kökü olmasını varsayıyor; proje klasöründen açılan bir Codex/Antigravity oturumunda kütüphane yolu bilinmiyor. Hiçbir paket proje CLAUDE.md/AGENTS.md bloğunda kütüphane yolunun nerede yazılı olduğunu denetlemiyor (P1 'tam blok cümlesi' yalnız ekleme/silme yasağını anıyor). Sahip: P1 (blok cümlesine kütüphane yolunu ve 'kütüphane oturumuna yönlendir' ifadesini koy, Q3 ile birlikte).
- promptlar/10-kutuphane-saglik-kontrolu.md satır 8'deki eski '44 güvenlik testi' sayısı: P8 sahipsiz olarak işaretledi, hiçbir pakete atanmadı. Sahip: P8.
- Aylık güncellemede P7 'kayıp kaynak' E akışı ile P4 'kısmi sonuç' arasında kayıp repo için kaynaklar.json kaydını kimin işaretleyeceği (kayip_tarihi) yalnız elle; aylık özet bunu karar_bekleyen yapıyor ama kaydı yazan araç yok (kasıtlı), bu yüzden kayıp kaynak her ay yeniden raporlanır. Sahip: P4 (aynı kaynağı ayda bir kez raporla ya da 'bilinen kayıp' listesinden çıkar).
