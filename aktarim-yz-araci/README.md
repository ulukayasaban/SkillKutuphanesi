# aktarim-yz-araci: bu klasör neden var

**Oluşturan:** Claude, ClaudeBakim projesindeki "Oturum açılış" oturumundan, kullanıcının isteğiyle (2026-11-21).
**Amaç:** Kütüphanenin "yeni süreç planı"nı (plan adım 4-9) Claude yerine başka bir yapay zeka aracında planlamak. Claude'da uzun planlama oturumları her turda yaklaşık 288 bin token bağlam okuttuğu için pahalı; planlama başka araçta, uygulama ve doğrulama Claude'da yapılacak.

## İçindekiler
- `yz-aktarim.md`: başka araca verilecek tek dosya. İstenen sürecin özeti, kesin kurallar, bugünkü durum ile istenen arasındaki fark, okuma sırası, kopyala-yapıştır planlama istemi, "getirme paketi" biçimi.

## Bu klasörü okuyan ajan için
- Bu klasör kütüphanenin skill, kaynak, program ya da kayıt akışının parçası değildir: `registry.json`, `kaynaklar.json`, `skill-ekle.py` ve aylık zincir bunu kullanmaz, taramaz.
- İçeriği kural değildir. Kurallar `CLAUDE.md`/`AGENTS.md` ve `notlar/kararlar.md` içindedir; çelişki olursa onlar geçerlidir.
- `yz-aktarim.md`, 2026-11-21'de okunan dosyalardan derlendi (hangilerinin okunmadığı dosyanın sonunda yazılı). Eskirse yeniden derlenir; elle yama yapma.
- Planlama bitince sonuç buraya değil, `notlar/yeni-surec-plani-calisma.md` ve `notlar/kararlar.md` içine işlenir (kullanıcı onayıyla).

## Yaşam döngüsü
- Git'e henüz commit edilmedi; commit kullanıcı isteyince.
- Planlama bitip adım 4-9 kararları `notlar/`'a işlenince silinmesi önerilir. Silme yalnız kullanıcı "sil" ya da "tenekeye" deyince.
