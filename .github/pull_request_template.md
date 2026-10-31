## Ne değişti
<!-- Kısa özet: hangi araç / rehber / rol / kaynak / skill -->

## Tür
- [ ] Araç (`araclar/`) ya da test
- [ ] Rehber, prompt, not
- [ ] Rol / profil
- [ ] Kaynak ekleme / çıkarma (`kaynaklar.json`)
- [ ] Aylık güncelleme (`guncelleme/YYYY-AA`), **yerelde `--birlestir` ile birleştirilir, Merge düğmesi kullanılmaz**

## Kontroller (yerelde çalıştırıldı)
- [ ] `python3 araclar/kapsam-denetimi.py`: 0 sorun
- [ ] `python3 araclar/dogrula.py`: 0 hata
- [ ] `python3 araclar/test.py`: tümü geçti
- [ ] Global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) dokunulmadı
- [ ] `arsiv/` altındaki orijinal skill dosyaları elle düzenlenmedi

## Kaynak / skill değişikliğinde
- [ ] Çakışma kontrolü yapıldı (aynı ad, aynı iş, aynı repoda birden fazla sürüm, global'de farklı sürüm)
- [ ] Ücret sınıflandırması (`ucret-siniflandirma.json`); ücretli skiller burada belirtildi:
- [ ] Silme/ekleme kullanıcı onayıyla; etkilenen projeler (`skill-ekle.py <proje> --durum`):
