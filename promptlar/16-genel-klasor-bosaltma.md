# 16 — Genel Skill Klasörlerini Boşaltma ya da Bekçi Raporuna Bakma

**Ne zaman:** (A) Genel skill klasörlerini (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`) yeniden yedekleyip boşaltman gerektiğinde (ilk boşaltma 2026-11-12'de yapıldı, K-40; `rehber/12` başındaki "Uygulandı" notuna bak).
(B) Bekçi raporunda `YENİ`, `KAYIP`, `DEĞİŞTİ` ya da ortam anahtarı sorunu çıktığında / orada beklenmeyen bir girdi belirdiğinde.
**Nerede:** `~/Documents/SkillKutuphanesi` klasöründe. Her adım ayrı onay ister (ONAY GEREKİR); bekçi hiçbir şeyi kendisi çalıştırmaz.

## A) Boşaltma

```kopyala
~/Documents/SkillKutuphanesi'de çalış. Önce notlar/hf-om-gecisi/DURUM.md ve rehber/12-genel-klasor-bosaltma.md dosyalarını oku.
Genel skill klasörlerini boşaltma işini adım adım yürüt. Kurallar: her adımdan önce python3 araclar/genel-bekci.py ile durumu göster,
python3 araclar/genel-bekci.py --plan <adım> çıktısını (yedek, komutlar, kontrol, geri alma) bana göster ve ben "evet" demeden hiçbir komutu çalıştırma.
Bir adım bitince kontrolü çalıştır, sonucu söyle, sonra bir sonraki adımı sor. Taban dosyasını yazmak, bir ayar ya da giriş dosyasına dokunmak,
commit ve hatırlatma kurmak ayrı onay ister. Kararlanacaklar listesindeki sorulara cevap vermeden 2. adımdan öteye geçme.
Bittiğinde yedek kaydını ve silme hatırlatmasını aynı gün öner.
```

## B) Bir şey yeniden belirdi / rapor temiz değil

```kopyala
~/Documents/SkillKutuphanesi'de python3 araclar/genel-bekci.py --ayrinti çalıştır. YENİ, KAYIP, DEĞİŞTİ ya da ortam anahtarı sorunu varsa
rehber/12-genel-klasor-bosaltma.md "Bir şey yeniden belirirse" bölümünü uygula: önce kim yazdı bul, hiçbir şeyi silme, bana seçenekleri sun.
```
