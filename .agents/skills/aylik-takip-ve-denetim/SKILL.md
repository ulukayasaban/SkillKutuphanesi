---
name: aylik-takip-ve-denetim
description: Aylık güncelleme taramasını, etki raporunu, toplu onay gruplamasını ve commit öncesi 3'lü çıkış kapısını yürütür (Denetim yapan rolü).
---

# Aylık Takip, Toplu Onay ve Denetim (Denetim Yapan Rolü)

## Ön-Kapı
- `git status --short` boş değilse başlama.
- Önceki tur yarım kaldıysa `son-aylik-calisma.json` içindeki `kaldigi_kaynak` kontrol noktasından devam et.

## Adımlar
1. **Tam kapsamlı tarama (Python):** Arşiv (`arsiv-guncelle.py --aylik`), fihrist, katalog (`kitler.json`, `programlar.json`), `not` ve `site-takip.py` (yalnız rapor; `site` güncellemesi her zaman kullanıcı onaylı elle yapılır) taranır.
2. **Hata ve değişiklik ayrımı:**
   - HTTP `403`/`429`/`5xx`/timeout -> geçici hata (KAYIP yazma).
   - Kesin `404`/`410` -> kullanılmayanı onaysız işaretle; projede kullanılanın yerel kopyasını silme, `durum: "kaynak_404"` uyarısı yaz.
   - `301` yönlendirme -> yeni kayıt açma, mevcut kaynağın adresini güncelle.
   - Lisans veya ücret (`ucret-siniflandirma.json`) değişen kaynak -> toplu gruptan çıkar, tekil onaya ayır.
3. **Etki raporu ve toplu onay gruplaması:**
   - `dondur` modundaki projeleri rapordan tamamen çıkar.
   - Aynı `kaynak + skill_adi + hedef_surum` üçlüsüne geçecek, `elle_degistirildi: false` ve lisans/ücret değişmemiş projeleri tek toplu grupta topla (`takip` modu otomatik dahil; `yalniz_onayli` açık onay ister).
   - `elle_degistirildi: true` skill'leri ayrı tekil onay satırına al.
4. **Atomik uygulama:** Onaylanan her projede yedek al -> güncelle -> `kilit.json` yaz -> doğrula. Hata çıkarsa yalnız o projeyi `--geri-al` ile geri al.
5. **3'lü çıkış kapısı ve kapanış:** `dogrula` (0 hata) + `kapsam-denetimi` (0 sorun) + `test` (%100 yeşil) doğrula; `son-aylik-calisma.json` ve `olcum.jsonl` güncelle.
