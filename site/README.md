# site/ — web sitesinden alınan skiller

Bu klasör kütüphanenin ikinci yerel kaynağıdır (kaynak tipi T8, `kaynaklar.json` → `yerel/site`): GitHub'da bulunmayan, kullanıcının
sitesini verdiği ve oradan alınmış skiller. Kullanıcının kendi yazdığı skiller burada değil, `kendi/` klasöründedir (K-57). Her skill bir
klasördür (`site/<ad>/SKILL.md` ve yanındaki dosyalar, `site/<ad>/KAYNAK.md` kütüphanenin kaynak notu). Depo private'tır.

Kurallar:
- Her `site/<ad>/` için kökteki `site-takip.json`'da kayıt ZORUNLUDUR: sahip, lisans, site adresi ve izlenen dosyaların sha256'sı.
  Kaydı olmayan site skili ya da `kendi/` altını gösteren kayıt `dogrula.py`'de HATA verir.
- Sahip ve lisans skill başına gerçek değerle yazılır ("Kendi (özel)" kullanılmaz); `arsiv-yerlestir.py` kayda buradan alır.
- Kaynak GitHub'a sorulmaz, KAYIP sayılmaz. Sitenin değişip değişmediğini `python3 araclar/site-takip.py` söyler (aylık zincir de
  çalıştırır; rapor `notlar/site-takip.md`). Araç bu klasöre hiç yazmaz.
- Güncelleme her seferinde kullanıcı onayıyla, elle: `rehber/03-yeni-skill-ekleme.md` → B3.
- Sitede GitHub reposu çıkarsa skill normal kaynağa geçirilir (rehber/03 A1..A9) ve buradaki kopya emekli olur.

Şu an: `stil` (Smokich'in "Video Stilleri" sitesi, https://smokich.gosem.dev/stil/; 7 hazır uzun stil prompt'u ve 11 kısa stil kartı;
kaynak, dosya özetleri ve güvenlik notu `stil/KAYNAK.md`'de).

Bu klasör asıl kaynaktır; `arsiv/` altındaki kopyası ondan üretilir (arşive elle dokunulmaz).
