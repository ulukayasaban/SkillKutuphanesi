# DURUM (her oturum önce bunu okur)

Son güncelleme: 2026-11-10

**Geçen adım:** yok. Plan 2. sürüme küçültüldü; hiçbir adım uygulanmadı.
**Sıradaki tek iş:** kullanıcıdan "evet" beklemek (`KISA-OZET.md` sorular).
**Onaydan sonraki ilk iş:** Adım 0 (kapsam-denetimi onarımı, aylık görevi duraklatma).

## Kararlar (tarihli)
- 2026-11-10: Skiller yerinden oynatılmayacak. Taşıma, yeni taşıma aracı ve eski 13 karar rafta (`rafta/`).
- 2026-11-10: 75 OpenMontage bağlantısı yerinde kalır.
- 2026-11-10: IstatistikYoutube, `motion-doctrine`, `talking-head-recut` hiçbir taşımaya girmez.
- 2026-11-10: Diğer araçların genel talimat dosyalarına kural yazılmaz (kullanıcı kararı).

## Adım çizelgesi
| Adım | İş | Kim | Durum |
|---|---|---|---|
| 0 | Kütüphane denetimini onar, aylık görevi duraklat | Ben | bekliyor (onay) |
| 1 | Dondurma komutu | Kullanıcı | yapılmadı |
| 2 | Skill ve araç yedeği | Ben | bekliyor (onay) |
| 3 | Durum raporu | Ben | bekliyor |
| 4 | Hazır metinler (yasak listesi, OpenMontage yamaları, 2 küçük düzeltme) | Ben hazırlar, kullanıcı uygular | bekliyor |
| 5 | Projeler kendini denetler | Kullanıcı yapıştırır | bekliyor |
| Kapanış | Aylık görevi yeniden aç (kullanıcıya sorarak) | Ben | bekliyor |

## Açık notlar
- Kütüphane `master` dalı GitHub'a gönderilmedi; kullanıcı isteyince `git push origin master`.
- `kapsam-denetimi.py` Adım 0 bitene kadar çalışmıyor; aradaki commit'ler bu kontrol olmadan yapıldı.
- Kurulu HyperFrames 0.9.23 güncelleme günlüğünde yok (8 Kasım); nasıl kurulduğu doğrulanmadı.
- İş bitince bu klasör arşivlenir (içinde proje adı geçiyor).
