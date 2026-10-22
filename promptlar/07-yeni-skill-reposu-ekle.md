# 07 — Yeni Skill Reposunu Kütüphaneye Ekle ("kontrol et")

**Ne zaman:** GitHub'da yeni bir skill reposunu yıldızlayıp **"Yapay Zeka Skillleri"** listesine ekledin.
**Nerede:** Claude Code ya da Codex, `~/Documents/SkillKutuphanesi` klasöründe. Ayrıntılı adımlar: `rehber/03-yeni-skill-ekleme.md`.

```kopyala
Yapay Zeka Skillleri listeme yeni repolar ekledim, kontrol et ve kütüphaneye dahil et.
~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/03-yeni-skill-ekleme.md'yi oku ve adımları ATLAMADAN uygula:

1. python3 araclar/github-skill-listesi.py  → "YENİ" bölümündeki repoları listele.
   python3 araclar/github-trend.py --aday  → trend'deki aday skill repolarını da listele (eksik alanlarımıza uyanları işaretle).
2. Her yeni repo için incele ve bana tablo halinde göster: ne yapıyor, kaç SKILL.md var ve nerede, lisans, son güncelleme,
   ÜCRET (ücretli = ücret ödemeden HİÇ kullanılamıyor; ücretli servis sadece bir seçenekse ya da ücretsiz katman varsa kısmen),
   GitHub trend durumu, çalışırken proje dışına yazıyor mu/ağdan kod indiriyor mu,
   tip önerisi (T1–T6) ve kategori önerisi.
3. ÇAKIŞMA KONTROLÜ (zorunlu): her SKILL.md için
   - kütüphanede aynı ADLI skill var mı (registry.json 'ad'); varsa içerik aynı mı farklı mı, hangisi 'tercih' olmalı (oncelik),
   - aynı İŞİ yapan skill var mı (ortusme_grubu); yeni skill birincil mi, tamamlayıcı mı, alternatif mi olmalı,
   - repo içinde aynı adlı birden fazla SKILL.md var mı (araç sürümleri / farklı sürümler),
   - global klasörlerde aynı adlı farklı skill var mı (kurulumda '--kutuphane' ekli ad alır).
   Bulgularını göster ve kararını gerekçeleriyle öner. Onayımı bekle.
4. Onaylarsam: kaynaklar.json'a ekle (tip, oncelik, gerekirse dahil/haric/bagimlilik), gerekirse kategori-kurallari.json ve
   ucret-siniflandirma.json'a ekle; sonra:
   python3 araclar/gelistirici-bilgisi.py
   python3 araclar/kaynak-cek.py --repo <owner/ad>      (her yeni repo için)
   python3 araclar/arsiv-yerlestir.py                   (güvenlik kilidi: başka skill kaybolursa durur)
   python3 araclar/kapsam-denetimi.py                   (0 sorun olmalı)
   python3 araclar/katalog-uret.py
   python3 araclar/dogrula.py                           (0 hata, 0 uyarı olmalı)
   Eski kayıtların kategori/durum/ücret farkını git HEAD'deki registry ile karşılaştır; rollerde kullanılan bir adın tercihi
   değiştiyse (aynı ad, farklı iş) durum_elle ile sabitle.
   python3 araclar/github-skill-listesi.py --duzenle  (yeni repoları yıldızla, 'Yapay Zeka Skillleri' listesine koy)
5. Yeni skilleri rehber/07-kategori-inceleme.md'ye göre incele (ozet_tr, kullanım, teknoloji, kalite, örtüşme rolü, ücret notu).
6. Gerekirse rollere/profillere ekle (ücretli skill çekirdeğe ancak gerekçeyle). python3 araclar/test.py ve
   python3 araclar/duman-testi.py çalıştır; hepsi geçerse git add -A && git add -f arsiv && git commit.
7. Özet ver: eklenen skiller, kararlar (tercih/alternatif/örtüşme), ücret durumu, etkilenen roller.

Kurallar: global skill klasörlerine dokunma, arsiv/ altındaki skill dosyalarını elle düzenleme, push yapma.
```
