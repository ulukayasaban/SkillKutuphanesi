# kendi/ — kullanıcının kendi skilleri

Bu klasör kütüphanenin yerel kaynağıdır (kaynak tipi T7, `kaynaklar.json` → `yerel/kendi`): GitHub'da olmayan, YALNIZ kullanıcının
kendi yazdığı skiller. Bir web sitesinden alınan (kullanıcının yazmadığı, GitHub'da da olmayan) skiller buraya konmaz: `site/<ad>/`,
kaynak `yerel/site` (T8), takip kaydı `site-takip.json` zorunlu (`site/README.md`, rehber/03 B3, K-57). Her skill bir klasördür (`kendi/<ad>/SKILL.md` ve yanındaki
dosyalar). Depo private'tır. `node_modules/` ve `package-lock.json` alınmaz (`.gitignore`); `.env`, `*.pem`, `*.key` gibi gizli
görünen dosya adları kaynak-cek.py tarafından atlanır ve uyarı verir.

Şu an: `openmontage` (OpenMontage giriş skili; `/openmontage`, `/backlot`, `/ink-art`, `/animated-drawing`, `/reel` isteklerini de yönlendirir),
`youtube-arama`, `antigravity-gorsel`. (`stil` 2026-11-15'te `site/stil/` klasörüne taşındı: siteden alınmış bir skill, K-57.) (`nlm-skill` 2026-11-12'de buradan çıkarıldı: nlm programının paketiyle gelir, projelere kopya değil program bağı olarak verilir: `skill-ekle.py <proje> --program-skill nlm:nlm-skill`; kart `programlar.json` → `nlm`. Arşivdeki eski kopyası emekli olarak durur, yeni kurulumda kullanılmaz.)

Bu klasör asıl kaynaktır; `arsiv/` altındaki kopyası ondan üretilir (arşive elle dokunulmaz). Düzenleme ve yeni skill ekleme:
`rehber/03-yeni-skill-ekleme.md` → "Kendi skillerim (yerel kaynak)".

Eski sürümler: bu skillerin makine genelindeki eski halleri (global klasörlerdeki kopyalar) geri dönüş için tam yedekte durur:
`~/Documents/Claude/yedek/genel-skiller-tam-2026-11-12/`.
