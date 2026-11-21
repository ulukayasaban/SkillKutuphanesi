# Tür: kendi ve site

## Ne
- **Kendi:** kullanıcının kendi yazdığı skiller (`kendi/<ad>/`, kaynak `yerel/kendi`, tip T7).
- **Site:** GitHub'da bulunmayan, kullanıcının sitesini verdiği skiller (`site/<ad>/`, kaynak `yerel/site`, tip T8, K-57).
Bunları kullanıcı getirir; `yeni-repo.md` soru sırasına girmezler. Bölüm: **arşiv**. İkisi de GitHub'a sorulmaz, ağ gerekmez, KAYIP sayılmaz.

## Kütüphanede ne durur
`kendi/<ad>/` ya da `site/<ad>/` klasörü, arşivde kopyası, `registry.json` kaydı; site için ayrıca `site-takip.json` kaydı (sahip, lisans, izlenen dosyaların sha256'sı; eksikse `dogrula.py` HATA).

## Ekleme adımları
Tek kaynak `rehber/03-yeni-skill-ekleme.md` B2 (kendi) ve B3 (site); örnek `kendi/README.md`, `site/README.md`. Özet:
1. Kendi: klasör `kendi/<ad>/` altına konur; kategori ve ücret satırı yazılır; `python3 araclar/kaynak-cek.py --repo yerel/kendi` (ağ yok), `python3 araclar/arsiv-yerlestir.py`.
2. Site: dosyalar yalnız GET ile indirilir, `site/<ad>/` altına konur, `KAYNAK.md` ve `site-takip.json` kaydı yazılır (`python3 araclar/site-takip.py --kayit-denetle`), sonra `python3 araclar/kaynak-cek.py --repo yerel/site`, `python3 araclar/arsiv-yerlestir.py`. Kullanıcı onayı olmadan eklenmez; lisansı belirtilmemişse onay kaydında `lisans_onay` gerekir.
3. Kontroller: `python3 araclar/kapsam-denetimi.py`, `python3 araclar/dogrula.py`, `python3 araclar/test.py`. Commit ana oturumdadır.
Boyut: yerel klasörün gerçek boyutu `python3 araclar/boyut-hesapla.py --yerel <klasör>` ile ölçülür.

## Kayda yazılacak alanlar
Kaynak kaydı bir kez açılmıştır (`yerel/kendi`, `yerel/site`); yeni skil bu kayda eklenir, yeni kaynak kaydı açılmaz. Eksik kalan tür alanları (`tur`: `kendi` ya da `site`, `bolum`: `arsiv`) plan adım 3'te yazılır.
Site skili için `site-takip.json` kaydı alanları `rehber/03` B3'tedir.

## Aylık güncelleme
Kendi: `kendi/` değişmişse aylık zincir değişen kaynak sayar. Site: `python3 araclar/site-takip.py` (aylık zincir de çalıştırır; rapor `notlar/site-takip.md`; ERİŞİLEMEDİ KAYIP sayılmaz). Site güncellemesi her seferinde kullanıcı onayıyla, elle (`rehber/03` B3 "Güncelleme").

## Projeye kurulum
Arşivden (`skill-ekle.py`), `tur-koleksiyon.md` ile aynı.

## Çıkarma
Kendi: klasör silinir (kullanıcı onayı; kendi skilleri yedeksiz silinmez, `rehber/13`). Site: sitede GitHub reposu çıkarsa skil normal kaynak olarak eklenir ve `site/` kopyası emekli olur (`rehber/03` B3, H).

## Bilinen sorunlar ve önlem
| Sorun | Önlem |
|---|---|
| Kendi skil halka açık bir skille aynı adı taşır | `rehber/09`: çıplak ad kendiliğinden el değiştirmez; yeni gelen `ad@yerel` olur |
| Site değişti, kopya eskidi | `site-takip.py` raporlar; güncelleme onayla ve elle |
| Site skilinin lisansı belirsiz | `site-takip.json` `lisans: belirtilmemiş` yazar; onay kaydında `lisans_onay` |
