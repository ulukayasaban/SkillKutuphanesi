# 08 — Aylık Güncelleme Dalını İnceleme ve Onay

**Ne zaman:** Ayın 1'indeki otomatik görev "güncelleme `guncelleme/YYYY-AA` dalında hazır" dedi.
**Nerede:** `~/Documents/SkillKutuphanesi` klasöründe.

```kopyala
Skill kütüphanemin aylık güncelleme dalını incele. ~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/02-guncelleme-yonergesi.md'yi oku.
1. Bekleyen dalı bul: git branch --list 'guncelleme/*'
2. Dalda ne değişti göster: git log --oneline master..<dal>, git diff --stat master...<dal> | tail -1,
   ve git show <dal>:notlar/guncelleme-gecmisi.md'nin en üstteki kaydı.
3. Bana özetle: hangi kaynaklar güncellendi, içeriği değişen / yeni / kaynakta kaldırılan skiller, yeniden incelenecekler,
   rollerde kullanılan skillerden etkilenen var mı, yeni ücretli skill var mı.
4. Onayımı bekle.
   - Onaylarsam: python3 araclar/arsiv-guncelle.py --birlestir <dal>
     (kontroller geçmezse master kendiliğinden geri döner; sonucu bana bildir)
     Ardından 'yeniden-incelenecek' skilleri rehber/07-kategori-inceleme.md ile incele ve kaydet.
   - Reddedersem: git branch -D <dal>
5. Son olarak projelerim için hatırlat: skill-ekle.py <proje> --durum / --guncelle --kuru (bkz. promptlar/05).
```
