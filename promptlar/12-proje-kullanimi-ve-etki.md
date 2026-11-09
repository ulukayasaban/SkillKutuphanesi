# 12 — Proje Kullanımı ve Etki Kontrolü

**Ne zaman:** Bir skili ya da kaynağı kütüphaneden çıkarmadan, tercihini ya da adını değiştirmeden önce; "bu skili hangi
projelerimde kullanıyorum?" diye merak ettiğinde; aylık güncellemeden sonra hangi projelerin güncelleneceğini görmek için.
**Nerede:** Claude Code ya da Codex, `~/Documents/SkillKutuphanesi` klasöründe. Ayrıntı: `rehber/10-proje-kullanimi.md`,
`rehber/09-ad-kimlik-ve-cakisma.md`.

```kopyala
[SKILL KİMLİĞİ ya da owner/repo] için etki kontrolü yap. ~/Documents/SkillKutuphanesi/AGENTS.md'yi oku.

1. python3 araclar/proje-kullanimi.py            → raporu yenile (projelere dokunmaz).
2. python3 araclar/proje-kullanimi.py --skill [KİMLİK]   ya da   --repo [owner/ad]   → kullanan projeleri listele.
3. python3 araclar/skill-ekle.py --listele --ara [AD]    → aynı adlı tüm sürümleri, kimliklerini ve durumlarını göster.
4. roller/ ve profiller/ içinde bu ad geçiyor mu bak.
5. Bana tablo ver: proje | kurulu ad | kimlik | kaynak@commit | rol. Sonra önerini yaz:
   - hiçbir yerde kullanılmıyorsa işlem serbest,
   - kullanılıyorsa hangi projede ne yapılmalı (skill-ekle.py <proje> --durum / --guncelle --kuru / --kaldir).
6. Onayım olmadan hiçbir kaydı, kimliği ya da tercihi değiştirme; projelerde kurulum yapma.

Kurallar: çıplak ad kendiliğinden el değiştirmez (devir: kaynaklar.json → ad_devral, onayımla). Kayıtlara proje adı yazma;
projeye özel not gerekiyorsa projeler.json → notlar'a yaz. Global skill klasörlerine dokunma, push yapma.
```
