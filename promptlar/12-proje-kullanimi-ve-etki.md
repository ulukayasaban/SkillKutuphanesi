# 12 — Proje Kullanımı, Etki Kontrolü ve Proje Sağlık Turu

**Ne zaman:** Bir skili ya da kaynağı kütüphaneden çıkarmadan, tercihini ya da adını değiştirmeden önce; "bu skili hangi
projelerimde kullanıyorum?" diye merak ettiğinde; aylık güncellemeden sonra hangi projelerin güncelleneceğini görmek için.
Ayrıca: aylık "projeleri kontrol et" turunda; yeni proje, taşınan/silinen proje, kayıtsız klasör ya da elle kurulu skill çıktığında.
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

Proje sağlık turu için:

```kopyala
Proje sağlık turu yap. ~/Documents/SkillKutuphanesi/AGENTS.md'yi oku (Claude ise CLAUDE.md).

1. python3 araclar/proje-kullanimi.py --saglik   → notlar/proje-durumu.md'yi üretir (projelere salt okuma; yazdığı tek dosya budur).
2. Bana sade bir özet ver: kaç proje, kaçında sorun/dikkat var; sorun varsa önce onu yaz.
3. Karar bekleyenleri tek tek, konu konu sor: güncellemesi gelen projeler (skill-ekle.py <proje> --guncelle --kuru ile göster),
   kayıtsız klasörler (kütüphaneyle yönet / yalnız izle / yoksay), KAYIP ya da TAŞINMIŞ projeler, KAYITSIZ SKILL'ler.
4. Tur bitince, bana sorarak, yalnız notlar/proje-durumu.md'yi tek başına commit et (kirli ağaç aylık güncellemeyi engeller); push yapma.
5. Onayım olmadan hiçbir şey yazma (4. adımdaki proje-durumu.md commit'i onayla birlikte yapılır); onaylarsam yalnız söylenen komutu çalıştır. Projelere, genel skill klasörlerine
   (~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage) dokunma.
```

Proje ekle / çıkar / taşındı / yoksay için:

```kopyala
Projeyi takip listesinde şu işlemi yap: [ekle <yol> | çıkar <ad> | taşındı <ad> → <yeni-yol> | yoksay <yol>]. Gerekçe: [NEDEN].
~/Documents/SkillKutuphanesi/AGENTS.md'yi oku.

1. İlgili komutu --evet OLMADAN çalıştır (proje-kullanimi.py --ekle / --cikar / --tasindi / --yoksay), planı bana göster.
2. Onaylarsam aynı komutu --evet ile çalıştır; sonra python3 araclar/proje-kullanimi.py --saglik ile sonucu doğrula.
3. Sadece projeler.json değişir. Projeye, genel klasörlere dokunma. Kayıtlara proje adı yazma (kural 6). Push yapma.
```
