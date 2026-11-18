# Tür: dev koleksiyon

## Ne
200 ve üstü skil içeren depo. Örnek: `ComposioHQ/awesome-claude-skills` (864 skil), `github/awesome-copilot` (472). Bölüm: **fihrist**. Skil dosyaları arşive ALINMAZ; skiller tek tek incelenmez, repo bir bütün olarak değerlendirilir
(üretici, lisans, ücret, kalite).

## Kütüphanede ne durur
- `fihrist/<owner>__<ad>.json`: her skilin adı, tek cümlelik açıklaması, klasör yolu; reponun o günkü commit'i (biçim: `fihrist/README.md`).
- `kaynaklar.json` içinde kayıt (`bolum: fihrist`).
Arşivde bu repodan dosya YOKTUR (tek istisna: bir projede kurulu olan skil; plan bölüm 12).

## Ekleme adımları
1. `yeni-repo.md` adım 1-6 (tür sırası 5: 200 ve üstü; boyut için `boyut-hesapla.py owner/ad`).
2. Kaynak kaydı (aşağıdaki alanlar) ve onay kaydı (`rehber/03` A4; `onay.commit` repo sabit commit'i). `dahil`/`haric` ile repo-içi ve kopya klasörler dışarıda bırakılır; ücret için `ucret-siniflandirma.json`.
3. Fihrist: `python3 araclar/fihrist-uret.py owner/ad --kuru` (özet: kaç skil, kaç SKILL.md okunamadı), sonra `python3 araclar/fihrist-uret.py owner/ad`. Repo indirilmez.
4. `python3 araclar/kaynak-cek.py --repo owner/ad` ÇALIŞTIRILMAZ (bu kaynak arşive çekilmez; araç `bolum: fihrist` kaydı atlar). `arsiv-yerlestir.py` bu kaynak için çalıştırılmaz.
5. Kontroller: `python3 araclar/dogrula.py --github` (fihrist dosyası yoksa ya da şeması bozuksa HATA), `python3 araclar/kapsam-denetimi.py` (bu kaynağın SKILL.md'leri "bilerek arşiv dışı" sayılır), `python3 araclar/test.py`. Commit ana oturumdadır.

## Kayda yazılacak alanlar
```json
{"repo": "owner/ad", "tip": "T1", "oncelik": 6, "haric": ["^\\.github/"], "tur": "dev-koleksiyon", "bolum": "fihrist",
 "tur_gerekce": "472 SKILL.md (200 sınırının üstünde): fihrist",
 "ne_ister": "skile göre değişir", "ne_indirir": "skile göre değişir", "tek_basina": true,
 "son_kontrol": {"tarih": "2026-11-18", "commit": "<40 haneli sha>"},
 "arac_uyumu": {"claude": true, "codex": true, "antigravity": true, "windows": true},
 "boyut": {"kutuphane_kb": 350, "kurulum_mb": 0, "hesaplanamayan": ["skile göre değişir"], "tarih": "2026-11-18"},
 "eklendi": "2026-11-18", "onay": {"kim": "kullanıcı", "tarih": "2026-11-18", "oturum": "<kısa not>", "commit": "<40 haneli sha>"}}
```
`tip` T1'dir (içerik skil reposudur; entegrasyon skilleri ayrı kayıtsa T4); arşive çekilmemesini `bolum: fihrist` sağlar. Böylece mevcut kayıtlara `tur`/`bolum` eklemek tip değiştirmeyi gerektirmez (plan adım 3).
`kutuphane_kb` fihristin disk boyutu değil, alınacak skillerin tahmini kaynak boyutudur (`boyut-hesapla.py`).

## Aylık güncelleme
Fihrist yenilenir: `python3 araclar/fihrist-uret.py owner/ad` eklenen, silinen ve adı değişen skilleri raporlar; `inceleme` notları korunur. Dosya inmez. Aylık zincire bağlanması HENÜZ YOK (plan adım 5): o zamana dek komut elle çalıştırılır.

## Projeye kurulum
HENÜZ YOK (plan adım 4). Planlanan: seçilen skil GitHub'dan geçici klasöre alınır, inceleme yapan taraf o an inceler, sonuç rapora girer, kullanıcı onaylarsa kurulur; kurulan sürüm projenin kilidine yazılır; bir ihtiyaç için fihristten en çok üç aday gösterilir,
arşivde aynı işi yapan incelenmiş skil varsa önce o önerilir. Bugün: fihristten bir skil istenirse kurulum yapılmaz; ana oturum kullanıcıya "henüz yok" der.

## Çıkarma
Kaynak kaydı ve fihrist dosyası silinir: `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` etkiyi ve sıralı adımları verir (fihrist dosyasını silme adımı 5b olarak listelenir). Projelerde kurulu skiller kalır ("kaynağı kütüphanede yok" notu).

## Bilinen sorunlar ve önlem
| Sorun | Önlem |
|---|---|
| Önceden inceleme yok, kalite bilinmiyor | Raporda "ilk kez inceleniyor"; incelenen skilin sonucu fihristteki `inceleme` alanına yazılır, aynı sürüm tekrar incelenmez |
| Öneri kalabalığı | Bir ihtiyaç için en çok üç aday (HENÜZ YOK, plan adım 4) |
| Skil kaynaktan silindi ama projede kurulu | Projede çalışır; yeni kurulumda önerilmez; yenilemede "silinen" olarak görünür |
| Aynı skil hem arşivde hem fihristte | Arşivdeki kayıt geçerlidir; fihristteki satır `arsivde: true` alır |
| İnternet yok | Kurulmaz; raporda "internet gerekli" |
| Fihrist açıklaması 300 karakterde kesilir | Tam metin kaynakta; kurulum anında okunur |
