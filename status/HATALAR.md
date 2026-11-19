# Hata kaydı
- 2026-11-18 | İlk boyut hesabı gerçeğin %25-40'ını buldu | Yalnız doğrudan bağımlılıklar sayılıyordu | Hesap yöntemi gerçek kurulu bir örnekle sınanmadan kullanılmaz
- 2026-11-18 | Yeni kit kaydında "yol kapısı çalışmadı" uyarısı | Arşivde dosyası olmayan kaynak için yol taraması çalıştı | Yeni kayıt türü eklenince bütün denetimler o türle bir gerçek kayıtta denenir
- 2026-11-19 | Neon'un ilk taşıma kodunda 3 kritik hata (not kaybı, kullanılan skil silme, ortak klasör silme) | Kodu yazan model kendi kodunu yeterince sınamadı | Silme yapan her kod ikinci, bağımsız bir model incelemesinden geçmeden kullanılmaz
- 2026-11-19 | zsh'te `$a` ile verilen argümanlar bölünmedi, üç ön rapor "repo biçimi" hatası verdi | zsh değişkenleri kelimelere bölmez | Argümanı değişkenle verme; komutu açık yaz ya da `"$@"` kullan
- 2026-11-19 | Arka plan işi "başarısız" göründü, gerçekte kontroller temizdi | `grep -c` eşleşme yokken çıkış 1 döndürür | Sayım için `grep -c ... || true` kullan; çıkış kodunu tek başına sonuç sayma
- 2026-11-19 | Neon'un çıktısı ilk kurulumda canlı görünmüyordu | `-p` yalnız son sonucu yazar | Neon her zaman `stream-json | neon-izle.py` ile çalıştırılır
