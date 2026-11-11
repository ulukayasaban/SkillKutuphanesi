# 15 — Kütüphaneye Yeni Bir Yapay Zeka Aracı Ekle

**Ne zaman:** Yeni bir yapay zeka aracı (IDE ya da CLI) kullanmaya başladın; kütüphanenin projelerde bu aracı da hesaba katmasını,
aracın hangi klasörleri okuduğunun resmi belgeden doğrulanıp `yapay-zeka-araclari.json`'a kaydedilmesini istiyorsun.
**Nerede:** Claude Code ya da Codex, **kütüphane klasöründe** (`~/Documents/SkillKutuphanesi`) açılmış oturum. Proje klasöründe yapılmaz.

```kopyala
Kütüphaneme yeni bir yapay zeka aracı ekleyeceğiz. Kütüphane: ~/Documents/SkillKutuphanesi
Önce ~/Documents/SkillKutuphanesi/AGENTS.md dosyasını oku, sonra rehber/14-yapay-zeka-araclari.md dosyasının 7. bölümünü
oku ve oradaki 1-9. adımları ATLAMADAN uygula.

Araç adı: [ARAÇ ADI]
Bu bilgisayarda kurulu mu: [evet / hayır / bilmiyorum]

Kurallar:
- Yalnız resmi belgeleri kullan (adresleri ve okuma tarihini kayda yaz). Tahmin etme; belirsiz her şey `belirsizler` listesine girsin.
- Yeni kaydı yapay-zeka-araclari.json'a yazmadan önce bana fark (diff) olarak göster ve onayımı bekle.
- Kaydı yazdıktan sonra çalıştır: python3 araclar/skill-ekle.py --araclar
- Kayıtlı bir projede ön deneme yap (hiçbir şey yazmaz): python3 araclar/skill-ekle.py <kayıtlı proje> --guncelle --kuru
  Raporda arac-duzeni satırı yeni aracı görenler ya da görmeyenler arasında anıyor mu, bana söyle.
- CLAUDE.md, AGENTS.md, README.md, araclar/dogrula.py ve araclar/test.py dosyalarını DEĞİŞTİRME (bunlar bütünleştirme işidir; gerekiyorsa bana ne yazılacağını söyle).
- Makine genelindeki skill klasörlerine, kabuk dosyalarına ve ayar dosyalarına dokunma. Aracın makine genelindeki klasörünü
  notlar/genel-klasor-tabani.json'a ekleme önerini ayrıca bana sor.
- Commit yalnız onayımdan sonra; push yok.

Bittiğinde kısa rapor ver: eklenen kayıt, --araclar çıktısı, açık kalan belirsizlikler, gerçek deneme için benden istediğin şey.
```

**Beklenen sonuç:** `yapay-zeka-araclari.json`'da aracın yeni kaydı (`denendi` boş), `skill-ekle.py --araclar` çıktısında aracın görünmesi
ve açık belirsizliklerin yazıldığı kısa bir rapor. Hiçbir proje ya da makine genelindeki klasör değişmez.
