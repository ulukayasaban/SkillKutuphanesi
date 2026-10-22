# 05 — Projedeki Skillerin Durumu, Güncelleme, Kaldırma, Geri Alma

## 5a — Durum ve güncelleme

```kopyala
Bu projedeki kütüphane skillerinin durumunu kontrol et ve gerekiyorsa güncelle. Kütüphane: ~/Documents/SkillKutuphanesi
1. python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --durum
2. python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --dogrula
3. Güncelleme varsa önce rapor: python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --guncelle --kuru
4. Raporu göster: hangi skill güncellenecek, 'elle-degistirilmis' olan var mı (onlar EZİLMEZ), 'kaynak-yok' olan var mı,
   'inceleme-eskidi' (yeniden incelenecek) olan var mı. Onayımı bekle.
5. Onaylarsam: --guncelle --evet, sonra --dogrula. Bittiğinde "oturumu yeniden aç" diye hatırlat.
```

## 5b — Skill kaldır

```kopyala
Bu projeden kütüphane skillerinden [skill-adi / hepsi]'ni kaldır. Önce ne silineceğini göster, onayımı bekle:
python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --kaldir [skill-adi | hepsi]
(uyarı varsa --evet'i ancak ben onaylayınca ekle). Kütüphaneden gelmeyen skillere ve benim dosyalarıma dokunma.
```

## 5c — Geri al

```kopyala
Son skill işlemini geri al. Önce yedekleri listele ve hangisine döneceğimizi bana sor:
python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --yedekler
Onaylarsam: python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --geri-al [yedek-adi]
```
