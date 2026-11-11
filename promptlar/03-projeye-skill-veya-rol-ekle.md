# 03 — Çalışan Projeye Skill ya da Rol Ekle

**Ne zaman:** Proje devam ediyor; yeni bir ihtiyaç çıktı (ör. animasyon, 3D, test, video) ve bir skill ya da agent rolü eklemek istiyorsun.

```kopyala
Bu projeye kütüphanemden yeni bir [skill / agent rolü] ekleyeceğiz. Kütüphane: ~/Documents/SkillKutuphanesi
Önce ~/Documents/SkillKutuphanesi/AGENTS.md dosyasını oku.

İhtiyaç: [ör. "sayfalara scroll animasyonu eklenecek" / "3D ürün görüntüleyici"]

Projede araç düzeni kayıtlıysa (--durum satırı "düzen: ..."), ona uy; "arac-secimi-yok" çıkıyorsa bana hangi araçlarla açılacağını sor ve --arac ile kaydet.

1. Projede şu an ne kurulu, bak:
   python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --durum
2. İhtiyaca uygun skill/rol öner (zaten kurulu olanları ve aynı işi yapanları ayıkla):
   python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --oner "[ihtiyaç]"
3. ÇAKIŞMA KONTROLÜ: önereceğin her skill için, projede zaten kurulu bir skille aynı örtüşme grubunda olup olmadığını
   (aynı işi yapan iki birincil skill), aynı skillin başka bir sürümünün kurulu olup olmadığını ve ücretli olup olmadığını bana söyle.
4. Ön kontrol:
   python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" [--rol <rol> | --skill <skill...> --rol-adi <mevcut-rol>] --kuru
5. Raporu göster (HATA, ÇAKIŞMA, ÜCRETLİ ayrı ayrı). Onayımı bekle; onaylarsam --evet, sonra --dogrula.
6. Bittiğinde "oturumu yeniden aç" diye hatırlat.

Kurallar: global skill klasörlerine dokunma, skill kopyalama, --zorla kullanma (ben istemedikçe).
```

**İpuçları:**
- Var olan bir role skill eklemek: `--skill <ad> --rol-adi <rol>`
- Rolün opsiyonel skillerini de almak: `--rol <rol> --opsiyonel`
- Bir rol 12'den fazla skill / 150 KB'tan fazla yük alırsa `baglam-yuku` uyarısı çıkar; rolü bölmeyi düşün.
