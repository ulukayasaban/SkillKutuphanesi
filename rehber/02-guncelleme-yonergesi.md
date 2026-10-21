# 02 — Skill Güncelleme Yönergesi

Güncelleme **iki ayrı katmanda** yapılır. Kütüphane güncellenince projeler kendiliğinden değişmez;
her projeyi sen ayrıca güncellersin. Böylece çalışan bir proje habersiz bozulmaz.

```
GitHub repoları ──(1) arsiv-guncelle.py──► SkillKutuphanesi ──(2) skill-ekle.py --guncelle──► Proje
                                             (git kayıt noktası)                    (proje yedeği)
```

## 1) Kütüphaneyi güncelleme (önerilen: ayda bir)

```bash
cd ~/Documents/SkillKutuphanesi
python3 araclar/arsiv-guncelle.py            # SADECE RAPOR: hangi repoda yeni commit var, hangi skill dosyaları değişti,
                                             # yıldızlarına yeni repo eklenmiş mi
python3 araclar/arsiv-guncelle.py --uygula   # değişiklik varsa: yeniden indir → yerleştir → kapsam denetimi → katalog →
                                             # doğrula → geçici dosyaları sil → git kayıt noktası
```

`--uygula` önce iki şeyi şart koşar: kütüphanede **kaydedilmemiş değişiklik olmayacak** (elle düzenlemeni önce `git commit` et) ve tüm kaynaklara **erişilebilecek**. Sonra bu sırayla çalışır; herhangi bir adım hata verirse durur ve **git kaydı atmaz**:
1. `kaynak-cek.py` — tüm kaynaklar sabit commit'ten yeniden iner (indirme hatası varsa durur).
2. `arsiv-yerlestir.py` — tekilleştirme, kategori, değerlendirme. **Elle yaptığın inceleme alanları korunur**
   (`ozet_tr`, `kullanim_alani`, `teknoloji`, `roller`, `kalite`, `ortusme_grubu`, `kategori_elle`…).
3. `kapsam-denetimi.py` — her SKILL.md'nin açıklandığını bağımsız olarak doğrular.
4. `katalog-uret.py` — KATALOG.md ve rehberleri yeniden üretir.
5. `dogrula.py` — roller/profiller var olan skillere mi bakıyor, tekrar isim var mı.
6. `git commit` — kayıt noktası.

### Güncellemeden sonra kontrol et
- `git -C ~/Documents/SkillKutuphanesi show --stat HEAD` → hangi skiller değişti.
- Rollerde kullanılan bir skill **kaldırıldıysa** `dogrula.py` HATA verir → rol dosyasını düzelt.
- Bir skill'in globaldeki durumu değiştiyse (ör. global sürüm güncellendi) kurulum adı değişebilir;
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
git -C ~/Documents/SkillKutuphanesi revert HEAD              # son güncellemeyi geri al
```

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

## 3) Skill'i projede özelleştirmek istersen
Kütüphane kopyasını elle değiştirmek yerine:
1. Skill'i kendi adınla kopyala (ör. `.claude/skills/benim-tasarim-kurallarim/`). Bu senin skill'in olur; araç ona hiç dokunmaz.
2. Ya da kütüphanede `registry.json`'a not ekle ve iyileştirmeyi kaynağa (GitHub) öner.

## 3b) Bir kaynak repo silinirse / private olursa
`arsiv-guncelle.py` bunu `! erişilemiyor` diye raporlar ve `--uygula` durur. `kaynaklar.json`'da o kaydın `tip` alanını
`"KAYIP"` yap: arşivdeki kopyalar ve registry kayıtları korunur (`kaynak_durumu: kayip`), projeler etkilenmez.

## 4) Global skiller
Global klasörlerdeki skiller (OpenMontage, addyosmani…) **bu sistemle güncellenmez**; onları kuran araç günceller
(ör. OpenMontage için `/openmontage`). Kütüphane bunları sadece okur ve `globalde` alanında karşılaştırır.

## Güncelleme takvimi (öneri)
| Ne zaman | Ne |
|---|---|
| Ayda bir | `arsiv-guncelle.py` raporu → gerekirse `--uygula` |
| Yeni repo yıldızladığında | `arsiv-guncelle.py` raporu "yıldızlı ama kaynaklar.json'da yok" der → `03-yeni-skill-ekleme.md` |
| Projeye başlamadan önce | `skill-ekle.py <proje> --durum` |
| Büyük sürüm (ör. GSAP 4, three r200) | İlgili kategori incelemesini tekrarla (`07-kategori-inceleme.md`) |
