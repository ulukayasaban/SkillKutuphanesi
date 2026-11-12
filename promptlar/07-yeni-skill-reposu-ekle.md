# 07 — Yeni Skill Reposunu Kütüphaneye Ekle ("kontrol et")

**Ne zaman:** GitHub'da yeni bir skill reposunu yıldızlayıp **"Yapay Zeka Skillleri"** listesine ekledin.
**Nerede:** Claude Code, Codex, Antigravity ya da başka bir ajan, `~/Documents/SkillKutuphanesi` klasöründe. Tek adım sırası: `rehber/03-yeni-skill-ekleme.md` A1..A9.

```kopyala
Yapay Zeka Skillleri listeme yeni repolar ekledim, kontrol et ve kütüphaneye dahil et.
~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/03-yeni-skill-ekleme.md'yi oku. rehber/03'teki A1..A9 sırasını ATLAMADAN, aynı sırayla uygula:

1. A1: git status temiz mi (değilse dur ve söyle); dogrula başlangıç sayısını not et; python3 araclar/github-skill-listesi.py (YENİ / AD DEĞİŞMİŞ) ve
   python3 araclar/github-trend.py --aday. AD DEĞİŞMİŞ yeni kaynak değildir (rehber/09). Program mı skill mi karar kutusuna bak.
2. A2: Her yeni repo için incele ve bana tablo halinde göster: ne yapıyor, kaç SKILL.md ve nerede, lisans, son güncelleme,
   ÜCRET (ücretli = ücret ödemeden HİÇ kullanılamıyor; ücretli servis sadece bir seçenekse ya da ücretsiz katman varsa kısmen), GitHub trend durumu,
   güvenlik okuması (proje dışına yazma, ağdan kod indirme), Claude'a özgü araç gereksinimi, tip (T1–T6) ve kategori önerisi, ve program mı skill mı.
   ÇAKIŞMA KONTROLÜ (zorunlu): aynı ADLI skill (registry.json 'ad'; içerik aynı mı farklı mı), aynı İŞİ yapan skill (ortusme_grubu; birincil/tamamlayıcı/alternatif),
   repo içinde aynı adlı birden fazla SKILL.md, aynı adlı kendi skill'in (global klasörler 2026-11-12'de boşaltıldı; orada bir şey yeniden belirdiyse onlar da).
   Kural: çıplak ad kendiliğinden el değiştirmez; yeni gelen ad@kaynak olur. Ad aynı, iş farklıysa eski kaydı durum_elle ile tercih sabitle ve iki kayda fark notu yaz.
   Çıplak adı bilerek devretmek (ad_devral) için önce python3 araclar/proje-kullanimi.py --skill <ad> ve rolleri kontrol et, bana sor.
   Değerlendirmeyi yalnızca repo/skill'in kendi niteliğiyle yap; notlara ve öncelik gerekçesine proje adı ya da "şu projeye uyar" yazma.
3. A3: Bulgularını ve kararını gerekçeleriyle göster. Onayımı bekle. Lisans belirtilmemiş / NOASSERTION / AGPL ise ayrıca sor.
4. Onaylarsam A4-A8'i rehber/03'teki sırayla yap (kayıt + onay kaydı, gelistirici-bilgisi, kaynak-cek --repo, yol-tara --repo --siki, arsiv-yerlestir,
   kapsam-denetimi, katalog-uret, skill-readme, skill-calistir --skill <yeni kimlikler>, dogrula --github, inceleme, test, duman-testi, tek commit).
   Her adımda rehberdeki durma koşullarına uy. Eski kayıtların kategori/durum/ücret farkını git HEAD'deki registry ile karşılaştır; rollerde kullanılan
   bir adın tercihi değiştiyse (aynı ad, farklı iş) durum_elle ile sabitle.
5. A8: Yeni skilleri rehber/07-kategori-inceleme.md'ye göre incele (ozet_tr, kullanım, teknoloji, kalite, örtüşme rolü, ücret notu); gerekirse rollere/profillere ekle
   (ücretli skill çekirdeğe ancak gerekçeyle).
6. A9: GitHub'a yazma yalnız repo listede değilse ve bana sorduktan sonra: listeye-ekle.py. github-skill-listesi.py --ekle/--duzenle kullanma. Push yapma.
7. Özet ver: eklenen skiller, kararlar (tercih/alternatif/örtüşme), ücret ve lisans durumu, etkilenen roller, commit, geri alma komutu (git revert <commit>).

Aday kararı verdiğim repoları hemen konu-takip.py --karar ile deftere yaz (eklendi / reddedildi / izle). Kurallar: global skill klasörlerine dokunma,
arsiv/ altındaki skill dosyalarını elle düzenleme, push yapma, onaysız ekleme yapma.
```
