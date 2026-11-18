# Hazır Promptlar

Yeni projelerde ve kütüphane bakımında **kopyala-yapıştır** kullanılacak promptlar. Claude Code, Codex, Antigravity, Cursor ve VS Code Copilot'ta aynen çalışır.

**Nasıl kullanılır:** İlgili dosyayı aç → `kopyala` bloğundaki metni al → `[KÖŞELİ PARANTEZ]` alanlarını doldur → Claude Code ya da
Codex Desktop'ta **proje klasöründe** (kütüphane bakımı için `~/Documents/SkillKutuphanesi`'de) açılmış oturuma yapıştır.

| # | Dosya | Ne zaman |
|---|---|---|
| 01 | [01-yeni-proje-skill-kurulumu.md](01-yeni-proje-skill-kurulumu.md) | Yeni projeye başlarken skilleri ve hazır agent rollerini kurmak |
| 02 | [02-kendi-agentlarimla-kurulum.md](02-kendi-agentlarimla-kurulum.md) | Agent'larını kendin tanımladıysan, sadece skilleri kurmak |
| 03 | [03-projeye-skill-veya-rol-ekle.md](03-projeye-skill-veya-rol-ekle.md) | Çalışan projeye yeni bir skill ya da agent rolü eklemek |
| 04 | [04-proje-amaci-ve-is-dagitimi.md](04-proje-amaci-ve-is-dagitimi.md) | Projenin amacını yazdırmak, işleri agent'lara dağıtmak |
| 05 | [05-proje-skill-durumu-guncelleme.md](05-proje-skill-durumu-guncelleme.md) | Projedeki skillerin durumuna bakmak, güncellemek, kaldırmak, geri almak |
| 06 | [06-ucretsiz-yol-onceligi.md](06-ucretsiz-yol-onceligi.md) | Agent'ın ücretli servislerden kaçınmasını sağlamak |
| 07 | [07-yeni-skill-reposu-ekle.md](07-yeni-skill-reposu-ekle.md) | GitHub "Yapay Zeka Skillleri" listesine eklediğin yeni repoları kütüphaneye almak (tek ekleme sırası A1..A9) |
| 08 | [08-aylik-guncelleme-onayi.md](08-aylik-guncelleme-onayi.md) | Aylık güncelleme dalını incelemek ve birleştirmek / reddetmek |
| 09 | [09-proje-tasindi-veya-bozuldu.md](09-proje-tasindi-veya-bozuldu.md) | Proje klasörü taşındı, skiller görünmüyor, bir şeyler bozuldu |
| 10 | [10-kutuphane-saglik-kontrolu.md](10-kutuphane-saglik-kontrolu.md) | Kütüphanenin tamamını kontrol ettirmek (duman testi) |
| 11 | [11-guvenilir-skill-secimi-mevcut-proje.md](11-guvenilir-skill-secimi-mevcut-proje.md) | Projesini bilen başka bir agent'a SkillKutuphanesi'nden (salt okunur) güvenilir, çakışmasız skill seçtirip projeye kurdurmak; sonraki seferlerde aynı düzende devam |
| 12 | [12-proje-kullanimi-ve-etki.md](12-proje-kullanimi-ve-etki.md) | Bir skili/kaynağı hangi projeler kullanıyor (silmeden önce etki); aylık proje sağlık turu; proje ekle/çıkar/taşındı/yoksay |
| 13 | [13-program-kur-guncelle.md](13-program-kur-guncelle.md) | HyperFrames, OpenMontage ya da başka bir programı kurmak, güncellemek, geri almak, çıkarmak ya da yeni program kaydetmek |
| 14 | [14-kaynak-cikar.md](14-kaynak-cikar.md) | Kütüphaneden bir kaynak repoyu ya da skili çıkarmak (etki, yedek, geri alma ile) |
| 15 | [15-yeni-yapay-zeka-araci.md](15-yeni-yapay-zeka-araci.md) | Yeni bir yapay zeka aracı kullanmaya başlayınca kütüphaneye tanıtmak, ya da aracın okuma düzeni değişince kontrol etmek |
| 16 | [16-genel-klasor-bosaltma.md](16-genel-klasor-bosaltma.md) | Genel skill klasörlerini yedekleyip boşaltmak ya da orada beklenmeyen bir girdi belirince bakmak |
| 17 | [17-repo-turune-gore-ekle.md](17-repo-turune-gore-ekle.md) | Yeni bir repoyu türüne göre (koleksiyon, tek skil, dev koleksiyon, kit, program, referans) tek soruyla kütüphaneye eklemek; adımlar `surecler/` klasöründe |

**Değişmeyen kurallar (her promptta geçerli):**
- Global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) dokunulmaz (tek istisna: onaylı program güncellemesi ve onaylı boşaltma, promptlar/13 ve 16).
- Skiller sadece `skill-ekle.py` ile kurulur; elle kopyalanmaz.
- Önce `--kuru` (rapor), sonra senin onayın, sonra `--evet`.
- **Çakışma:** aynı adlı skill, aynı işi yapan iki birincil skill, global'de farklı sürümü olan skill (genel klasörler boş; yalnız orada bir şey belirirse) ve kendi dosyaların raporda
  HATA/UYARI olarak görünür; çözülmeden kurulum yapılmaz.
- **Ad:** çıplak ad kendiliğinden el değiştirmez; aynı adlı başka skill varsa rapor `ayni-ad` satırıyla kurulan kaynağı gösterir
  (`rehber/09-ad-kimlik-ve-cakisma.md`). Kayıtlara proje adı yazılmaz; proje bilgisi `notlar/proje-kullanimi.md`'dedir.
- **Ücret:** ücretli skiller raporda `ucretli` UYARISI ile görünür; ücretsiz yol her zaman önce. Liste: `notlar/ucretli-skiller.md`.
- Skill/agent kurduktan sonra Codex/Claude oturumunu **yeniden aç** (skiller oturum başında okunur).
