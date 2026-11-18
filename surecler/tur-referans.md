# Tür: referans

## Ne
Skili olmayan ama bilinmeye değer kütüphane ya da araç. Örnek: `mrdoob/three.js`, `FFmpeg/FFmpeg`. Bölüm: **not**. Dosya inmez.

## Kütüphanede ne durur
`kaynaklar.json` kaydı (tip T5 ya da tasarım teknolojisi için T6) ve bir not kartı: `notlar/referans/kutuphaneler.md` satırı (T5) ya da `notlar/referans/tasarim-teknolojileri.md` kartı (T6). Kartsız T5/T6 kayıt `dogrula.py`'de UYARI verir.

## Ekleme adımları
1. `yeni-repo.md` adım 1-6 (tür sırası 10; boyut istenirse `boyut-hesapla.py`, genelde gerekmez).
2. Kullanıcı "evet" derse: kaynak kaydı (`{"repo": "owner/ad", "tip": "T5"}` + `tur`, `bolum`, `tur_gerekce`, onay kaydı) ve kart/satır. Kart biçimi `rehber/03` "Prompt 11 uyumu" maddesindedir (T6: `### Ad — \`owner/repo\` · sürüm` + `**Skill:**` satırı; T5: satırın son sütununda ilgili skiller).
3. Kontroller: `python3 araclar/gelistirici-bilgisi.py --repo owner/ad`, `python3 araclar/katalog-uret.py`, `python3 araclar/dogrula.py`, `python3 araclar/kapsam-denetimi.py` (referans repoda sonradan SKILL.md çıkarsa SORUN verir), `python3 araclar/test.py`.

## Kayda yazılacak alanlar
```json
{"repo": "owner/ad", "tip": "T5", "tur": "referans", "bolum": "not",
 "tur_gerekce": "SKILL.md yok; yaygın kullanılan grafik kütüphanesi",
 "eklendi": "2026-11-18", "onay": {"kim": "kullanıcı", "tarih": "2026-11-18", "oturum": "<kısa not>", "commit": "<40 haneli sha>"}}
```

## Aylık güncelleme
Bugünkü düzen: `python3 araclar/kapsam-denetimi.py` referans repoda sonradan skil çıkıp çıkmadığına bakar. "Hâlâ var mı" ve "skil yayımlamış mı" için ayrı aday raporu HENÜZ YOK (plan adım 5).

## Projeye kurulum
Kurulmaz. Referans, öneri raporunda "bu iş için şu araç var" diye gösterilir (rapor tarafı HENÜZ YOK, plan adım 4); o zamana dek `notlar/referans/` kartı elle okunur.

## Çıkarma
`python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` (kart/satır adımı raporda çıkar).

## Bilinen sorunlar ve önlem
| Sorun | Önlem |
|---|---|
| Sonradan skil yayımlar | `kapsam-denetimi.py` SORUN verir; kayıt normal kaynak türüne taşınır (plan senaryo H, tür değişikliği ana oturumun kararıdır) |
