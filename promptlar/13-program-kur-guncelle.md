# 13 — Program Kur, Güncelle, Geri Al, Kaldır

**Ne zaman:** HyperFrames, OpenMontage, etsyotomasyon gibi programları (skill olmayan yapılar) bu bilgisayara kurarken, güncellerken,
eski sürüme döndürürken ya da kütüphaneden/bilgisayardan çıkarırken; ya da yeni bir programı kütüphaneye dahil ederken.
**Nerede:** Claude Code ya da Codex, `~/Documents/SkillKutuphanesi` klasöründe. Ayrıntı: `rehber/11-program-yonetimi.md`.

```kopyala
[PROGRAM ADI: hyperframes / openmontage / etsyotomasyon / yeni] için [KUR / GÜNCELLE / GERİ AL / KALDIR / DAHİL ET] işlemi yap.
~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/11-program-yonetimi.md dosyalarını oku (aklında önceki konuşma yok; her şeyi dosyadan öğren).

1. python3 araclar/program-denetim.py --sema --siki   → kartlar geçerli mi (0 hata değilse dur, bana söyle).
2. python3 araclar/program-denetim.py                 → durum (KART ESKİ ise dur, sebebini bul).
3. GÜNCELLE için: python3 araclar/program-denetim.py --oncesi [PROGRAM]   → engelleri ve 'KIRICI ADAYI' satırını oku.
   KIRICI ADAYI ise rehber/11 → 'Kırıcı sürüm' deneme adımlarını AYRI klasörde uygula, sonucu raporla.
3b. python3 araclar/proje-kullanimi.py --program [PROGRAM]  → bağlı projeler. Adım 3'ün çıktısındaki 'bağlar' satırlarına da bak ('bağ kırılacak' varsa bana söyle).
4. Bana sun: sürüm farkı, değişiklik özeti, kırıcı adayı mı, yedeğin yeri. Bu işlem için AYRI onayımı sor (önceki onay geçerli değil).
5. Onayımdan sonra rehber/11 → "Taze ajan: istek → adımlar" altındaki o programın adımlarını sırayla yürüt; önce yedek (KAYIT.json dahil),
   sonra --oncesi 'HAZIR' demeden değişiklik yapma.
6. GERİ AL için kartın geri_alma adımları (rehber/11 → "Geri alma"); KALDIR için rehber/11 → "Programı çıkarma" (kütüphaneden ve bilgisayardan ayrı ayrı onay).
7. DAHİL ET için: python3 araclar/program-denetim.py --iskelet [kaynak|npm-global|git-checkout] > geçici dosya, doldur, --sema temiz olsun,
   sonra rehber/11 → "Yeni program eklemek".
8. Bitince: program-denetim.py yeniden, --sema --siki, kapsam-denetimi.py, dogrula.py; commit. Yedek klasörünü silme, silmek için bana hatırlat ve sor.
8b. Güncellemeden sonra program-denetim.py yeniden: 'bağlar' satırlarında HATA kalmamalı; kırık bağ için bana sor (--yenile ya da --kaldir).

Kurallar: anahtar/.env/oturum dosyalarını açma. pip install -U, make setup (onaysız), npx, hyperframes init/skills/update çalıştırma.
Ortam değişkeni (HYPERFRAMES_SKIP_SKILLS vb.) ben istemeden tanımlama. Genel skill klasörlerine ve kabuk dosyalarına dokunma
(yalnız onayla ve rehber/11'deki adımla). Push yapma; kartlara proje adı yazma.
```
