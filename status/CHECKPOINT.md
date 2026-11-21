# CHECKPOINT — SkillKutuphanesi
Son güncelleme: 2026-11-21 06:32

## Şimdi
- **Yeni süreç planı BEKLEMEDE (kullanıcı "sonra" dedi).** `notlar/onceki-planlar/istenen-surec.md` TAMAM: kullanıcının istediği süreç (amaç, 10 görev, kurallar, onay kuralları, proje/sürüm, maliyet, 13 senaryo); 5 soru kapandı. `notlar/onceki-planlar/yeni-surec-plani-calisma.md`: adım 1-3 tamam (hedefler; ortadaki yol; veri düzeni = tam ayrım aşamalı, uygulama geçiş planına bağlı), token ölçümü, pazar denemesi sonucu, devam istemi.
- Kullanıcı kararları (2026-11-21): skill'ler proje klasöründe kalır, genel klasörler boş (kesin); pazar/genel önbellek yolu elendi; tam ücretli skill de önerilir (ilerleyişi kullanıcıya kalır); dondurulmuş proje raporda görünmez; kaybolan kaynak projede kullanılıyorsa uyarı gelir; maliyet hedefi önce ölçüm sonra sayı; diğer YZ araçlarına ek çaba yok (tam uyum Claude Code, Codex, Antigravity); yeni repo/aylık takipte kullanıcıya bağımlılık yok; kurulum token'ı kabul, hedef işleyiş maliyeti.
- Bu oturumda ayrıca: HyperFrames 0.9.37→0.9.71, OpenMontage fecb9a1e→2e003e65 (duman 142/1, K-66); genel klasör tabanı yenilendi; yedekler silindi; `advisorModel` genel ayardan kaldırıldı; `test.py` 324/324; test artıkları (824 MB) tenekeye (`~/.Trash/test-artiklari-2026-11-21`). Arka planda çalışan süreç yok (Antigravity uygulamasının kendi `agy --hub` süreci bizim değil).

## Sıradaki
1. Yeni oturumda `notlar/onceki-planlar/istenen-surec.md` ve `notlar/onceki-planlar/yeni-surec-plani-calisma.md` oku; **istenen süreci bugünkü kütüphaneyle karşılaştır** (her istek: hazır / yarım / yok), çıktıyı yeni bir notlara yaz, sonra plan adım 4'ten sürdür (adım 7'de yeni repo ve aylık takip maliyetini ölç).
2. **Vade 2026-12-07:** aylık zincir fihristi ve kiti bilmiyor, `notlar/son-aylik-calisma.json` damgası yok (zincir "ilk kurulum" sanıyor). Vadeden önce asgari düzeltme (plan adım 5'in küçük hali) yapılmalı.
3. Kayıt bakımı: 6 kaydın `tur_gerekce`si boş, ComposioHQ gerekçesi eski, `kararlar.md`'de K-60..K-66 "Kabul edilen bekleyenler" altında, `surecler/` içinde 12 eskimiş "HENÜZ YOK", `.gecici/` 52 MB.

## Karar bekleyen
- [ ] Push: 21 commit yerelde (`git push origin master`), kullanıcı isteyince.
- [ ] Kullanılmayan 164 kaynağın kopyası (arşivde dursun mu, yalnız kayıt mı): kayıpsız yol önerildi, karar verilmedi.
- [ ] Trend/popüler 10 aday + listede olup kütüphanede olmayan 4 repo (`echris6/motion-video-kit`, `howseen-ai/claude-motion-design`, `tugrawork-creator/saas-motion-kit`, `storytold/pdfcraft`).
- [ ] Kalan eski yedekler (`akil-disi-tam` 3,4 GB, `istatistik-skill-gecisi`, `genel-skiller-tam`, `genel-kaldirilan`, `global-skills-2026-11-08`): silme yalnız "sil" deyince.
- [ ] IstatistikYoutube `tools/kurgu/_test/duman-cikti` (62 MB, test çıktısı): tenekeye taşınsın mı (proje, onay gerekir).
- [ ] claude-mem gözlemcisi haftalık token'ın ≈%15'i (çoğu Haiku): kısılsın mı (kullanıcı ayarı).

## Vadesi gelen / takvimli
- 2026-12-07 — aylık çalışma vadesi (son kayıtlı 2026-11-02; hızlı özet DİKKAT).
- ≈2026-12-12 — `~/Documents/Claude/deneme/openmontage-fecb9a1e` (2,9 GB) silme günü; kullanıcı "şimdilik silme" dedi.
- ≈2026-11-26 — Antigravity Claude/GPT haftalık kota açılışı (Opus agy çalışmaz: `RESOURCE_EXHAUSTED`, 133 saat).

## Bilinen sorunlar / dikkat
- `gh` PATH'te yok: `export PATH=/usr/local/opt/gh/bin:$PATH`.
- `genel-bekci` DİKKAT 1: `~/.claude/skills/.trash` (uygulamanın çöp klasörü) dosya sayısı değiştikçe alarm (gürültü; tasarım düzeltmesi planda).
- `kapsam-denetimi.py` bir kez 15 dk takıldı (CPU %0); zaman aşımıyla çalıştır. 5 araç `--help`'e cevap vermiyor, doğrudan çalışıyor: `arsiv-yerlestir.py`, `duman-testi.py`, `gelistirici-bilgisi.py`, `kapsam-denetimi.py`, `listeye-ekle.py`; `ceviri-tr.py` ve `neon-izle.py` testsiz.
- Proje bağlarında kayıtlı program sürümü eski (hyperframes 0.9.35 / openmontage fecb9a1e / nlm 0.15.8; kartlar 0.9.71 / 2e003e65 / 0.16.5): `--durum` "güncel" diyor.
- Sistem: kütüphane `test.py` 324/324, `dogrula.py` 0 hata 1 eski uyarı (etsy-api), yedek denetimi TEMİZ.
- tools/denetim.sh yok; hafif kontrol yapıldı (CHECKPOINT'teki yollar var).

## Çalışma düzeni (kullanıcı kararları)
- Sade Türkçe, konu konu, bir adımda tek soru; plan dosyası tek hafıza; planlama konuşmaları kısa oturumda (oturum bağlamı ≈288 bin token/tur, kütüphane haftalık token'ın ≈%14'ü). Yan konu açma.
- Projelerde (kütüphane dışı) açık onay olmadan işlem yok (K-50); genel skill klasörlerine yazılmaz; GitHub'da yalnız bu depo, push yalnız istenince.
- Silme: kullanıcı "sil" ya da "tenekeye" dediğinde; test artıkları tenekeye.
