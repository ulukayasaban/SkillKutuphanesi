# Fihrist

Dev koleksiyonların (200 ve üstü skilli depo; kayıtta `bolum: fihrist`) skil listesi. Skil dosyaları arşive ALINMAZ; burada yalnız her skilin adı,
tek cümlelik açıklaması ve kaynaktaki yolu durur. Bir projeye kurulurken seçilen skil o gün GitHub'dan alınır ve incelenir
(`notlar/plan-tur-surecleri.md` bölüm 5.5; süreç: `surecler/tur-dev-koleksiyon.md`).

- Dosya: `fihrist/<owner>__<ad>.json`. Üretim ve yenileme: `python3 araclar/fihrist-uret.py owner/ad [--kuru]` (repo indirilmez; elle düzenlenmez,
  tek istisna `inceleme` notu).
- İçerik: `{repo, commit, tarih, skil_sayisi, skiller: [{ad, aciklama, yol, arsivde?, inceleme?}]}`.
  - `yol`: skilin klasör yolu (`""` = repo kökündeki SKILL.md); `registry.json` içindeki `kaynak_yol` ile aynıdır.
  - `aciklama`: SKILL.md frontmatter `description`, boşlukları tek aralığa indirilmiş, en çok 300 karakter.
  - `arsivde: true`: aynı skil arşivde de var; arşivdeki kayıt geçerlidir.
  - `inceleme: {commit, tarih, sonuc, not}`: bu skil kurulum anında bir kez incelendiyse sonucu; aynı sürüm tekrar incelenmez.
    Yenilemede aynı `yol` için korunur.
- Yenileme eklenen, silinen ve adı değişen skilleri raporlar; kayıt değişince `commit` ve `tarih` güncellenir.
- Denetim: `python3 araclar/dogrula.py` (`bolum: fihrist` olan kaynağın dosyası yoksa HATA; şema hatası HATA; kaynağı olmayan dosya UYARI).
