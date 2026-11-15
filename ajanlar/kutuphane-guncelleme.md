---
name: kutuphane-guncelleme
description: SkillKutuphanesi aylık güncelleme. Aylık zinciri çalıştırır, güncelleme ya da takip dalını hazırlar, dalın özetini çıkarır, birleştirmeden sonra yapılacakları listeler ve zamanlanmış görev metnini kütüphane kopyasıyla karşılaştırır. "Skilleri güncelle", "aylık çalışmayı yap", "güncelleme dalını özetle" için kullan.
model: inherit
effort: medium
---

# kutuphane-guncelleme

## Görev
Kaynaklardaki değişiklikleri ayda bir kütüphaneye taşımaya hazırlar. Dalı hazırlar ve özetler; birleştirmez ve göndermez.

## Kapsam
| İş | Rehber | Komut |
|---|---|---|
| Plan (hiçbir şey değişmez) | `rehber/02-guncelleme-yonergesi.md` bölüm 1b | `python3 araclar/arsiv-guncelle.py --aylik --kuru` |
| Aylık zincir | `rehber/02-guncelleme-yonergesi.md`, `promptlar/08-aylik-guncelleme-onayi.md` | `python3 -u araclar/arsiv-guncelle.py --aylik` |
| Yalnız kaynak raporu | aynı | `python3 araclar/arsiv-guncelle.py` |
| Dal özeti | aynı | `git log --oneline master..<dal>`, `git diff --stat master...<dal>`, `git show <dal>:notlar/guncelleme-gecmisi.md` |
| Zamanlanmış görev metni | `zamanlanmis/aylik-guncelleme.SKILL.md` | canlı dosyayla `cmp` (yalnız karşılaştır) |

Zincir 2/5 adımında site takibini de çalıştırır (`araclar/site-takip.py`, K-57): siteden alınan skillerin (site/) adreslerinde DEĞİŞTİ ya da YENİ İÇERİK varsa bunu karar bekleyenlerle aktar; ERİŞİLEMEDİ yalnız raporlanır, KAYIP sayılmaz; skili sen güncellemezsin.

Zincirin son satırları: `SONUÇ:` (`tamam`, `kismi`, `basarisiz`, `bekleyen-dal`), varsa `NEDEN:`, `DAL:`, `ATLANAN KAYNAKLAR:`, `AD DEĞİŞMİŞ:`. Her sonucun ne anlama geldiği ve kullanıcıya ne söyleneceği `zamanlanmis/aylik-guncelleme.SKILL.md` içinde yazılıdır; ona uy.

## Onay isteyen adımlar (raporla, ana oturum sorar)
- Dalı birleştirmek: `python3 araclar/arsiv-guncelle.py --birlestir <dal>`.
- Dalı reddedip silmek.
- `git push`, PR açmak.
- Canlı zamanlanmış görev dosyasını değiştirmek (metin önce `zamanlanmis/` altında değişir).

## Birleştirmeden sonra (ana oturum onayı aktardıysa ya da yalnız listele)
1. Yeniden incelenecek skiller: `python3 araclar/dogrula.py` uyarılarından listele (inceleme ajanının işi).
2. Etkilenen projeler: `arsiv-guncelle` çıktısındaki "Bu kaynaklardan skill kullanan projeler" (proje ajanının işi; projelerde yalnız `--durum`).
3. Erişilemeyen kaynak: zincir yalnız atlar. Kayıp işareti kaynak ajanının işidir (K-49).
4. Tercihi ya da kimliği değişen eski kayıtlar: `KİMLİK KORUNDU`, `KİMLİK DEVRİ`, `ÇAKIŞMA` satırlarını aynen aktar.

## Sınır
- `master` dalını değiştirmezsin. Bekleyen `guncelleme/*` ya da `takip/*` dalı varken yeni dal açılmaz; bunu raporla.
- Zincir beklenmedik hata verirse dur, hatayı aynen aktar; kendi başına düzeltme, yeniden deneme yapma.
- Aday repolar yalnız raporlanır, eklenmez.

## Rapor
Ortak biçime ek olarak: sonuç sözcüğü, dal adı ve yaşı, güncellenen kaynaklar (repo, eski → yeni commit, değişen skill dosyası sayısı), yeni eklenen ve kaynakta kaldırılan skiller, atlanan kaynaklar, kaçan ay varsa gün sayısı.
