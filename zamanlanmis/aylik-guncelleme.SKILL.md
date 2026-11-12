---
name: skill-kutuphanesi-aylik-guncelleme
description: Ayda bir skill kütüphanesinin aylık zincirini tek komutla çalıştırır (ön kontrol, kaynak raporu, güncelleme ya da takip dalı, tek sayfa özet, damga); master'ı değiştirmez, birleştirme kullanıcı onayıyla.
---

Görev: ~/Documents/SkillKutuphanesi skill kütüphanesinin AYLIK ZİNCİRİNİ tek komutla çalıştır, sonucu kullanıcıya TEK SAYFA özet olarak oku ve onun kararını bekleyenleri listele. Yanıtı Türkçe, sade yaz.
(Bu metnin kütüphanedeki kaynağı `zamanlanmis/aylik-guncelleme.SKILL.md`'dir; değişiklik önce orada yapılır, canlı dosya kullanıcı onayıyla güncellenir.)

Kesin kurallar:
- `master` dalını DEĞİŞTİRME. Birleştirme (`--birlestir`) YAPMA; bu her zaman kullanıcının onayıyla, ayrı bir oturumda yapılır. Master'a commit de atma.
- push yapma, PR açma (kütüphanenin GitHub deposu `ulukayasaban/SkillKutuphanesi` private; push/PR sadece kullanıcı isteyince, ayrı oturumda). Başka hiçbir GitHub reposunda işlem yapma. GitHub'da yıldız/liste değiştirme.
- Global skill klasörlerine (~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage) ve kullanıcının projelerine dokunma. `arsiv/` altındaki skill dosyalarını ve `kaynaklar.json`, `registry.json` gibi kayıt dosyalarını elle düzenleme; yeni kaynak EKLEME (adaylar sadece raporlanır).
- Hiçbir dalı SİLME, `git reset --hard`, `git clean`, `git branch -D` çalıştırma (komutun kendi açtığı ve kendi geri aldığı dal dışında). Bekleyen eski dalları olduğu gibi bırak.
- Erişilemeyen kaynağı kendiliğinden `KAYIP` işaretleme: bu kullanıcının onaylı kararıdır (komut yalnız "bu ay erişilemedi" diye raporlar).
- Bir adım beklenmedik hata verirse dur, hatayı olduğu gibi raporla; kendi başına düzeltmeye çalışma.

Adımlar:
1. `cd ~/Documents/SkillKutuphanesi && python3 -u araclar/arsiv-guncelle.py --aylik` komutunu çalıştır (15–40 dk sürebilir; bitmesini bekle, çıktısını sonuna kadar oku). Komut kendisi sırayla yapar: 1/5 ön kontrol (master mı, ağaç temiz mi, bekleyen dal var mı, `gh` oturumu var mı), 2/5 kaynak raporu, 3/5 güncelleme (kaynaklarda değişiklik varsa `guncelleme/YYYY-AA` dalı; yoksa `takip/YYYY-AA` dalında trend + popüler + konu taraması; erişilemeyen kaynak atlanır), 4/5 aylık özet (program denetimi, proje sağlığı, yedekler, git durumu, bekçi), 5/5 damga (`notlar/son-aylik-calisma.json`). Son satırlar: `SONUÇ:` (`tamam`, `kismi`, `basarisiz` ya da `bekleyen-dal`), varsa `NEDEN:`, `DAL:`, `ATLANAN KAYNAKLAR:`, `AD DEĞİŞMİŞ:`. Çıktıda `KAÇAN AY:` satırı olabilir.
2. `SONUÇ: tamam` ve `DAL:` satırı varsa dalı incele (`<dal>` = `DAL:` satırı): `git branch --show-current` (master olmalı), `git status --short` (boş olmalı), `.guncelleme-kilidi` YOK; `git log --oneline master..<dal>`, `git diff --stat master...<dal> | tail -1`, `git show <dal>:notlar/guncelleme-gecmisi.md | head -30` (guncelleme dalında), `git show <dal>:notlar/github-trend.md | head -60`, `git show <dal>:notlar/konu-takip.md | head -80`. `DAL:` yoksa kaynaklarda ve takipte yeni bir şey çıkmamıştır.
3. `SONUÇ: kismi` ise güncelleme yapılmadı (salt okuma rapor ve özet yine çalıştı): `NEDEN:` satırını olduğu gibi aktar ve kullanıcıya ne yapacağını söyle. Kirli ağaç → listelenen dosyaları kaydetmesi (git commit, onayıyla) ya da geri alması; "GitHub'a ulaşılamıyor" → kendi terminalinde `gh auth login` çalıştırıp tarayıcıda onaylaması, sonra komutun yeniden çalıştırılması; master dışında → master'a dönmesi; kaynaklar geçici kontrol edilemedi → bir süre sonra yeniden çalıştırması.
4. `SONUÇ: bekleyen-dal` ise önceki ayın dalı hâlâ onay bekliyor: yeni dal AÇILMADI. Çıktıdaki dal adını ve yaşını söyle (45 günden eskiyse özellikle belirt). Salt okuma rapor ve özet yine çalıştı; onları da oku. Kullanıcıya iki yol sun: dalı incelemesi ve onaylarsa "güncelleme dalını birleştir" demesi (`python3 araclar/arsiv-guncelle.py --birlestir <dal>`), ya da reddedip `git branch -D <dal>` demesi; sonra komut yeniden çalıştırılır. Dalı kendin birleştirme, silme.
5. `SONUÇ: basarisiz` ise komut kendi açtığı dalı geri aldı ve master'a döndü: `NEDEN:` satırını aktar, tekrar deneme, düzeltmeye çalışma.
6. Komut hiç başlamadıysa ya da Traceback ile bittiyse: hatayı olduğu gibi aktar ve dur (hızlı özet için `python3 araclar/aylik-ozet.py --hizli` çalıştırabilirsin). Damga yazılmamış olabilir; kullanıcıya söyle.
7. Çıktıda `KAÇAN AY:` satırı varsa raporun başına "Son çalışma <N> gün önce; bu koşu kaçan ayı da kapsıyor" yaz. Ayrı bir telafi adımı YOK.

Rapor biçimi (kullanıcıya TEK SAYFA, düz Türkçe):
- Başlık: "SkillKutuphanesi aylık güncelleme — <tarih>"
- **Sonuç:** tamam (dal adı ya da "yeni bir şey yok") / kısmi (neden) / bekleyen dal (dal, yaş) / başarısız (neden)
- **Aylık özet:** komutun 4/5 adımındaki tek sayfa özeti kısaltmadan oku ("Senin kararını bekleyen N şey" ve "Dikkat gerektirenler" listeleri aynen).
- **Güncellenen kaynaklar ve skiller:** `guncelleme-gecmisi.md` kaydından: repo · eski→yeni commit · değişen skill dosyası; içeriği değişen, yeni eklenen, kaynakta kaldırılan, yeniden incelenecek skiller; "Etkilenen projeler" (arsiv-guncelle çıktısındaki "Bu kaynaklardan skill kullanan projeler"; öneri: `skill-ekle.py <proje> --durum` / `--guncelle --kuru`; projelere dokunma). Yoksa "yok".
- **Erişilemeyen ve adı değişen kaynaklar:** `ATLANAN KAYNAKLAR:` ve `AD DEĞİŞMİŞ:` satırları ile çıktıdaki "KİMLİK KORUNDU", "KİMLİK DEVRİ", "ÇAKIŞMA" satırları (yoksa "yok"). Karar kullanıcınındır (kaynaklar.json: `tip: KAYIP`, `eski_adlar`, `ad_devral`).
- **GitHub trend, konu takibi, yeni yıldızlanan repolar:** ilgili dosyalardan kısaca; adaylar EKLENMEZ.
- **Senin kararını bekleyenler:** numaralı liste (bekleyen dal, yeni aday repolar, rapor dosyaları kaydedilsin mi, erişilemeyen kaynak KAYIP olsun mu, program güncellemesi, zamanlanmış görev metni vb.). Hiçbirini kendin yapma.
- **Kullanıcının yapması gereken:** dalı inceleyip onaylarsa "güncelleme dalını birleştir" demesi (her iki dal türü için `python3 araclar/arsiv-guncelle.py --birlestir <dal>`; kontroller geçmezse master kendiliğinden geri döner); reddederse `git branch -D <dal>`. Aday eklemek isterse "şu adayları ekle" (rehber/03-yeni-skill-ekleme.md). Birleştirmeden sonra yeniden incelenecek skiller ve projeler için `skill-ekle.py <proje> --durum`.
- **GitHub (isteğe bağlı) hatırlatması:** raporun sonuna şu notu MUTLAKA ekle: "GitHub'a göndermek istersen: (a) birleştirmeden ÖNCE inceleme kaydı için 'dalı push et ve PR aç' de → `git push -u origin <dal>` + `gh pr create --base master --head <dal>`; (b) birleştirmeden SONRA 'GitHub'a gönder' de → `git push origin master` (PR açıldıysa kendiliğinden merged olur) + `git push origin --delete <dal>`. Güncelleme PR'ı GitHub'daki Merge düğmesiyle birleştirilmez; birleştirme her zaman yerelde `--birlestir` ile yapılır (rehber/02, 'GitHub'a gönderme')."
