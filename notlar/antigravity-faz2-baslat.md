# Antigravity: Faz 2 başlatma (Faz 1 tamam, etiket v1-faz1-tamam)

Dal: `yeni-surec-faz2` (Faz 1 dalından açıldı). Model: Orchestrator Gemini 4 Neon High (zaten seçili).

## Sırayla
1. Antigravity App'te proje `SkillKutuphanesi`, dal seçicide `yeni-surec-faz2`.
2. Aşağıdaki kutuyu yapıştır. Önce plan çıkar; planı bana ya da kendi gözünle şu 4 şeye karşı kontrol et: yalnız Faz 2 mi, projelere yazma yok mu, GitHub'a yazma/push yok mu, gerçek ağ taraması/gerçek repo girişi yok mu.
3. Bitince raporda `dogrula` 0 hata, `kapsam-denetimi` 0 sorun, `test` tamamı yeşil olmalı; olmadan commit onayı verme.

## Başlatma komutu
```text
/plan notlar/yeni-surec-plani.md dosyasını oku (bölüm 4, 5, 6, 9 Faz 2, 10, 11; Faz 1 sonucu: git tag v1-faz1-tamam). Yalnızca Faz 2 (Akış, onay ve eksik araçlar) kapsamını planla ve uygula, bu sırayla: (1) aylık zincire fihrist, kit, referans, program taraması + notlar/son-aylik-calisma.json damgası + GitHub 403/429/301/zaman aşımı koruması (kaynak asla KAYIP işaretlenmez; yarim_kaldi + kaldigi_kaynak yazılır); (2) yeni-repo onaysız KESİN giriş akışı + konu-takip.json kuyruğu (neden alanları planda yazdığı gibi) + K-58 otomatik ret (savunma amaçlı güvenlik istisnası); (3) toplu onay etki raporu aracı (aynı kaynak+skill+hedef sürüm grupları, elle_degistirildi/lisans-ücret değişen ve dondur projeler gruptan çıkar). Kesin sınırlar: toplu onay aracı YALNIZ rapor üretir, hiçbir projenin kilit.json veya skill klasörüne yazmaz; gerçek ağ taraması, gerçek yeni repo girişi ve gerçek aylık çalışma YAPMA (testler sahte verilerle çalışsın; gerçek ölçüm Faz 3'tür); GitHub'a hiçbir yazma, push, liste değişikliği yapma; arsiv/ dosyalarını silme/değiştirme, programlar.json'u yeniden serileştirme; Faz 3 işlerine (tip kaldırma, çift kayıt temizliği, ajan sadeleştirme) geçme; notlar/onceki-planlar/ altına dokunma. Planı ve değişecek dosya listesini önce bana göster, onayımı bekle. Her adımdan sonra test.py'yi koştur, kırılan test varsa düzeltmeden sonraki adıma geçme. Bitince dogrula.py, kapsam-denetimi.py (zaman aşımıyla), test.py sonuçlarını ve git diff --stat çıktısını raporla; commit öncesi benden onay al.
```

## Geri dönüş
`git switch yeni-surec-faz1` (Faz 1 hali) ya da `git switch master` (eski düzen).
