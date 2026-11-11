# Onay bekleyenler (uygulama aşaması sonu, P8 toplu liste)

Her satır: ne istiyoruz, neden, hayır derseniz ne olur. Hiçbiri yapılmadı. Hepsi sizin evet demenizi bekliyor.
İlgili metinler bu klasördeki dosyalarda hazır: `p8-yama-a-claude-agents.md`, `p8-yama-b-kural-1-istisna.md`, `p8-rafa-tasima.md`,
`p1-claude-agents-md.md`, `p1-blok-kutuphane-cumlesi.md`.

## A. Talimat dosyaları ve belgeler
1. `CLAUDE.md` ve `AGENTS.md` başına işaretçi satırı ve akış/bakım maddeleri (Yama A, yedi paketin metni birleşik): yeni oturum `BASLA.md`'yi bulsun diye. Hayır derseniz: `dogrula.py` her çalışmada "CLAUDE.md ilk satırı BASLA.md'ye işaret etmiyor" uyarısı verir, `duman-testi.py` "bilinmeyen uyarı yok" adımında takılır; yeni oturum giriş belgesini kendi bulmak zorunda kalır.
2. `CLAUDE.md` kural 1'e tek istisna (Yama B): program güncellemesi ve genel klasör boşaltması işlem başına ayrı onayla ve yedekle yapılabilsin. Hayır derseniz: kural 1 olduğu gibi kalır, kütüphane oturumu `~/.openmontage` ve genel skill klasörlerine yazamaz; HyperFrames/OpenMontage güncellemesi ve boşaltma yapılamaz.
3. Yama B uygulanırsa Claude'un kendi hafıza notundaki ("global klasörlere dokunma") cümlenin de güncellenmesi: iki kural çelişmesin diye. Hayır derseniz: hafıza notu eski cümleyi söylemeye devam eder, yeni oturumlar çelişkiyi sizden sorar.
4. Proje talimat bloklarına kütüphane yolu cümlesi (P1 sorusu, metin `p1-blok-kutuphane-cumlesi.md`): proje oturumu kütüphaneye yönlendirilsin diye. Hayır derseniz: bugünkü blok metni aynen kalır (bu çalışmada böyle bırakıldı).
5. Kök dizindeki üç eski belgenin `notlar/rafta/` altına taşınması (`PLAN.md`, `Kullanılacak Promt Örneği.md`, `notlar/yerel-yapilacaklar-2026-11.md`): eski sayılar ve geçersiz kararlar yeni oturumu yanıltmasın diye. Hayır derseniz: yerlerinde kalır, hiçbir şey bozulmaz.
6. `notlar/hf-om-gecisi/DURUM.md` dosyasına "tek giriş belgesi BASLA.md" satırı ve rehber/12 işaretçisi: geçiş notu yeni giriş belgesine bağlansın diye. Hayır derseniz: DURUM.md eski kalır, `BASLA.md` onu zaten okuma sırasına koyuyor.
7. İsteğe bağlı `GEMINI.md` taslağı (yalnız Gemini CLI kurulursa): şimdi kurulu değil. Hayır derseniz: hiçbir şey olmaz.
8. `TEST_RAPORU.md`'nin `skill-calistir.py` ile yenilenmesi (uzun çalışır): rapor 2026-11-05 tarihli ve bayat. Hayır derseniz: aylık güncelleme zaten yeniler.
9. Bu çalışmanın bütün dosyalarının (yeni araçlar, belgeler, testler, `BASLA.md`, `notlar/kararlar.md`, `README.md`, `promptlar/README.md`, `promptlar/10`, `rehber/08` düzeltmeleri) commit'i: bugün hepsi izlenmeyen ya da değişmiş durumda. Hayır derseniz: dosyalar çalışma ağacında kalır, `duman-testi.py` temiz ağaç ister (`--kirli-ok` ile denenebilir).
10. `notlar/kararlar.md` K-23 eşik sayıları (5 commit/7 gün, 300 MB, 5 MB, 45 gün, gizli yedek 30 gün, diğer yedek 90 gün): araçlar bu sayılara göre uyarır. Hayır derseniz: sayıları siz söylersiniz, araç ve belge güncellenir.
11. `dogrula.py` yeni UYARI'larının ileride HATA'ya yükseltilmesi: şimdi hepsi UYARI, çünkü HATA aylık birleştirmeyi geri sardırır. Hayır derseniz: UYARI kalır.

## B. Git, yedek ve makine
12. GitHub'a gönderilmemiş commit'lerin push'u: GitHub yedeği geride kalmasın diye. Hayır derseniz: yerelde durur, `git-durum.py` hatırlatmaya devam eder.
13. İsteğe bağlı `git bundle` ikinci kopyası: depo diskte tek yerde kalmasın diye. Hayır derseniz: yalnız yerel + GitHub kopyası olur.
14. `skill/lottiefiles-motion-design` dalının silinmesi (`git branch -d`, birleşmiş): bekleyen dal listesi temizlensin diye. Hayır derseniz: dal durur, `git-durum.py` uyarır.
15. `~/Documents/Claude/yedek/global-skills-2026-11-08` yedeğinin silinmesi: yalnız siz "sil" derseniz ve genel klasörler boşaldıktan sonra. Hayır derseniz: yedek durur.
16. `notlar/genel-klasor-tabani.json` dosyasının ilk yazımı (`genel-bekci.py --taban-yaz`, önce kuru çalışma 196 girdi gösterdi): genel klasörlerde beklenmeyen girdiyi yakalamak için. Hayır derseniz: bekçi "TABAN YOK" der, boşaltma planı çalışmaz.
17. Genel klasör boşaltmasının her adımı (yedek, kaldırma, yedek kaydı, 30 gün sonra silme hatırlatması): ancak Yama B sonrası ve adım adım. Hayır derseniz: klasörler olduğu gibi kalır.
18. Genel klasör sorularının cevapları Q1-Q9 (özellikle `~/.palmier/skills` ve `~/.gemini/config/skills` kapsamı, `openmontage` giriş skilinin yeri): boşaltma planı bunlara göre yazılır. Hayır derseniz: bu girdiler "kalacak" sayılır, bekçi soru olarak gösterir.

## C. Programlar, projeler, kaynaklar
19. HyperFrames 0.9.23 -> 0.9.34 güncellemesi (yedek, deneme, rapor; ayrı onay) ve ek ortam anahtarı tanımı: güncel sürüm için. Hayır derseniz: eski sürümde kalır, rapor "yeni sürüm var" der.
20. OpenMontage'ta 244 commit geride olan klonun güncellenmesi (yedek, deneme, rapor; ayrı onay): güncel için. Hayır derseniz: yerinde kalır.
21. OpenMontage'ın Claude Code girişinin boşaltma sonrası yeri (komut + giriş skili) ve yama dosyalarının amaçları: karar bekliyor. Hayır derseniz: kartta "karar-bekliyor" kalır.
22. `origin` adresinin yeni depo adına çevrilmesi: depo adı değiştiyse GitHub yönlendirmesine güvenmeyelim diye. Hayır derseniz: eski adres yönlendirmeyle çalışmaya devam eder.
23. `notlar/proje-durumu.md` ilk içeriğinin commit'i ve gerçek verideki kayıtsız klasörler/kayıtsız skiller için tek tek karar: proje takibi kayıtlı olsun diye. Hayır derseniz: rapor her çalışmada aynı klasörleri "kayıtsız" gösterir.
24. Etsy-Yeni'deki emekli `etsy-api` kaynağı için karar: eski kaynağın projede kalıp kalmayacağı. Hayır derseniz: rapor uyarmaya devam eder, hiçbir şey değişmez.
25. `kaynaklar.json`'a eklenen `kayip_tarihi` satırının (J-DTurner/etsy-api-skill: 2026-11-10) commit'te teyidi: kayıp kaynak uyarısı sussun diye. Hayır derseniz: `dogrula.py` o kayıt için uyarı verir.
26. Proje klasörlerindeki gerçek düzen değişiklikleri (kilitte `araclar` alanı olmayan projede ilk yazımda Araçlar sütununun "claude, codex" olması dahil): bu çalışma yalnız kütüphane içidir, projelere dokunmadı. Hayır derseniz: projeler olduğu gibi kalır.

## D. Aylık çalışma
27. Aylık çalışmanın Aşama 2'ye geçişi (damga dosyası, `takip/` dalı, gerçek `--aylik` koşusu, zamanlanmış görev kopyası, rehber/02 1c): otomatik aylık zincir için. Hayır derseniz: aylık çalışma bugünkü elle yolla (`--aylik --kuru`, `--uygula --dal`, `--birlestir`) sürer.
28. Canlı zamanlanmış görev metninin (`~/.claude/scheduled-tasks`) güncellenmesi: kütüphanedeki kopyayla aynı olsun diye. Hayır derseniz: canlı görev eski metinle çalışır.
29. Davranış değişikliklerinin commit onayıyla bildirilmesi: `takip/*` dalı engeli, çevrimdışı `--uygula` "DURDU" demesi, `--kuru` ile hiçbir şey yazmama. Hayır derseniz: eski davranışa dönüş için ilgili commit geri alınır.
30. `kaynak-cek.py --atla` bayrağının aylık `--uygula` tarafından kullanılması: erişilemeyen kaynak güncellemeyi durdurmasın diye. Hayır derseniz: erişilemeyen kaynak güncellemeyi durdurur.

## E. Ek kalemler (son inceleme ile eklendi)
31. Windows'ta Codex ve Antigravity skilleri görsün mü (ortak kopya, P1 sorusu 1): `kararlar.md` satır 43'te açık. Hayır derseniz: Windows projelerinde yalnız Claude klasörü kurulur.
32. etsyotomasyon release ikilisi için sha256 kaydı (indirme gerektirir, onay şart): tedarik doğrulaması tam olsun diye. Hayır derseniz: ikili doğrulanmadan kalır, rapor bunu söyler.
33. Boşaltma sonrası ikinci adım (P2 adım 2): giriş skili, slash komutları ve global CLAUDE.md düzenlemeleri, ortam anahtarı satırı ve isteğe bağlı `launchctl setenv`. Hayır derseniz: bu adım yapılmaz, yalnız rapor çalışır.
34. P2 zamanlanmış tek seferlik hatırlatma ve `yedekler.json` hatırlatma satırı: yedek silme gününü unutmayalım diye. Hayır derseniz: hatırlatma yalnız oturum başı özetinde görünür.
35. Yeni kaynak eklemeleri, `listeye-ekle.py` ile GitHub listesine yazma ve trend/popüler aday kararları (P7): her biri tek tek onayla yapılır. Hayır derseniz: aday listede bekler, hiçbir şey eklenmez.
36. `kaynak-cek.py` çevrimdışı rapor kipinde çıkış kodu değişti (eskiden 1, şimdi 0; yalnız `--siki` ile 2) ve bekleyen dal satırı "Onay bekleyen dal: ..." oldu: canlı zamanlanmış görev metninin bu satıra ya da çıkış koduna bağlı olup olmadığını okuyarak kontrol edeceğiz; 28. kalemle birlikte onaylanır.
37. Aylık özetteki `zamanlanmis-gorev` satırı, kütüphane kopyası (`zamanlanmis/aylik-guncelleme.SKILL.md`) yazılmadığı için bugün "temiz" der; bu kasıtlıdır (kopya Aşama 2'de). 28. kalemle birlikte onaylanır.
38. Yedek ve arşiv klasörlerinin proje takibinde "yoksay" listesine alınması: `~/Documents/IstatistikYoutube-Arsiv` ve `~/Documents/NewTetraTarim/ECommerceProject-Archives` (`proje-kullanimi.py --yoksay YOL --altini-da`). Hayır derseniz: aylık özet bu klasörleri her seferinde karar bekleyen olarak sayar.
