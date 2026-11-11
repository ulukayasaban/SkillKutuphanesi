# 08 — Aylık Güncelleme Dalını İnceleme ve Onay

**Ne zaman:** Ayın 1'indeki otomatik görev "güncelleme `guncelleme/YYYY-AA` dalında hazır" ya da "takip `takip/YYYY-AA` dalında hazır" dedi;
ya da oturum başındaki hızlı özet (`python3 araclar/aylik-ozet.py --hizli`) "aylık çalışma 35 günden fazladır yapılmadı" ya da bekleyen dal dedi.
**Nerede:** `~/Documents/SkillKutuphanesi` klasöründe.

```kopyala
Skill kütüphanemin aylık güncelleme sonucunu incele. ~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/02-guncelleme-yonergesi.md'yi oku.
1. Önce özeti çalıştır ve bana oku: python3 araclar/aylik-ozet.py ("Senin kararını bekleyen" listesi ve "Dikkat gerektirenler").
   Aylık çalışma 35 günden eskiyse bana sor; evet derse güncellemeyi rehber/02'deki yolla yap (önce: python3 araclar/arsiv-guncelle.py --aylik --kuru ile planı göster).
   Özet "rapor dosyaları yenilendi, kaydedilsin mi?" derse bana sor; onaylarsam git add <o dosyalar> && git commit.
   Bir kararı bana sorduktan sonra "kabul ettim" dersem notlar/kararlar.md "Kabul edilen bekleyenler" bölümüne ifadeyi yaz (özette tekrar çıkmasın).
2. Bekleyen dalları bul: git branch --list 'guncelleme/*' 'takip/*'
3. Her dal için göster: git log --oneline master..<dal>, git diff --stat master...<dal> | tail -1.
   guncelleme/* dalında ayrıca git show <dal>:notlar/guncelleme-gecmisi.md'nin en üstteki kaydı; takip/* dalında
   git show <dal>:notlar/github-trend.md | head -60 ve git show <dal>:notlar/konu-takip.md | head -80.
4. Bana özetle: hangi kaynaklar güncellendi; içeriği değişen / yeni / kaynakta kaldırılan skiller; yeniden incelenecekler;
   rollerde kullanılan skillerden etkilenen var mı; yeni ücretli skill var mı; erişilemeyen ya da adı değişen kaynak var mı
   (kaynaklar.json düzeltmeleri benim kararım: tip KAYIP, eski_adlar, ad_devral); karar bekleyen yeni skiller (kaynaklar.json dahil/haric).
5. Onayımı bekle. Dal 45 günden eskiyse bunu söyle.
   - Onaylarsam (iki dal türü için de aynı yol): python3 araclar/arsiv-guncelle.py --birlestir <dal>
     (kontroller geçmezse master kendiliğinden geri döner; sonucu bana bildir). git merge --no-ff ile elle birleştirme YAPMA.
     Ardından guncelleme dalında 'yeniden-incelenecek' skilleri rehber/07-kategori-inceleme.md ile incele ve kaydet.
   - Reddedersem: git branch -D <dal>
6. Etkilenen projeleri listele: python3 araclar/proje-kullanimi.py --repo <güncellenen her kaynak>
   ve onlar için hatırlat: skill-ekle.py <proje> --durum / --guncelle --kuru (bkz. promptlar/05).
   Çıktıda 'KİMLİK KORUNDU' ya da 'AD DEĞİŞMİŞ' satırı varsa bana ayrıca göster (rehber/09-ad-kimlik-ve-cakisma.md).
7. Program güncellemesi bekleyenler (özet listesinde "yeni sürüm var") ayrı onay ister: promptlar/13.
```
