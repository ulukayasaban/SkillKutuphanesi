# 14 — Kaynağı / Skili Kütüphaneden Çıkar, Kayıp Kaynağı Ele Al

**Ne zaman:** Bir skill reposunu ya da tek bir skili kütüphaneden çıkarmak, ya da GitHub'da kaybolan bir kaynağı ele almak istediğinde.
**Nerede:** herhangi bir ajan, `~/Documents/SkillKutuphanesi` klasöründe. Adımlar: `rehber/03-yeni-skill-ekleme.md` "D) Kaynak / skill KALDIRMAK" ile D, E, G, H (etki raporu araçla, çıkarma D adımlarıyla elle).

```kopyala
Şu kaynağı/skili kütüphaneden çıkarmak istiyorum: <owner/ad ya da skill kimliği>. (Kayıpsa: şu kaynak GitHub'da kayboldu: <owner/ad>.)
~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/03-yeni-skill-ekleme.md (D ve E bölümleri) dosyasını oku ve atlamadan uygula:

1. git status --short boş olmalı; değilse dur ve bana söyle.
2. python3 araclar/kaynak-cikar.py --repo <owner/ad> --kuru --github   (tek skill için --skill <kimlik> --kuru). Çıktıyı OLDUĞU GİBİ bana göster:
   engeller, projeler, roller/profiller, dikkatler. Bu araç yalnız okur.
3. D0: gerekçeyi içerikle doğrula (örnek SKILL.md oku; "daha iyi alternatif" diyorsan onu da oku). Onayımı bekle. Programa bağlı ("program" alanlı) kaynakta dur ve rehber/11'e bak.
4. Onaylarsam aracın yazdığı ADIMLAR'ı sırayla uygula; her projeden skill kaldırmak için ayrıca bana sor. Kaynak kayıpsa önce E bölümü: kaydı silme, tip'i KAYIP yap.
5. kapsam-denetimi, dogrula, test sonuçlarını göster; tek commit at; commit numarasını ve geri alma komutunu (git revert <commit>) söyle.
6. GitHub yıldızı/listesini bana sor; kendiliğinden kaldırma. Push yapma.
Kurallar: global skill klasörlerine dokunma, arsiv/ altındaki dosyaları elle düzenleme, --kayba-izin-ver kullanma, proje adlarını kayıt dosyalarına yazma.
```
