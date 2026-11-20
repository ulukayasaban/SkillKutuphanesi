# CHECKPOINT — SkillKutuphanesi
Son güncelleme: 2026-11-20 03:40

## Şimdi
- Plan `notlar/plan-tur-surecleri.md`: ÇEKİRDEK KAPSAM kodlandı ve birleşti (K-65). Kullanıcı süreci kapanış için durdurdu; arka planda süreç, Neon ya da worktree yok.
- Biten: tür/boyut/fihrist araçları; 199+ kaynakta tür (iki kit arşivde kalır: `urun-skil`; iki KAYIP: `tek-skil`); 6 dev koleksiyon fihriste taşındı; adım 4 (fihrist/kit kurulumu, `--kaldir`, `--rapor`, seyrek+kısmi klon) birleşti ve gerçek ağ denemesi geçti (boş projeye `awesome-copilot` içinden tek skil 7 sn); `medya_haric` (tek dosya yolu) birleşti ve 28 gereksiz medya dosyası (12,8 MB) arşivden çıktı (silinen liste: `~/Documents/Claude/SkillKutuphanesi-saklanan/silinen-medya-listesi.txt`); `dogrula.py` tür ve bölüm eksikliğini HATA sayıyor.
- Commit'siz iki dosya: `notlar/plan-tur-surecleri.md` (adım 4 "uygulandı", durum satırı) ve `status/HATALAR.md` (2 satır): bu kapanışla commit edilir.
- Son tam `test.py` 324/324 idi (tür zorunluluğu eklenmeden önce); ondan sonraki koşu yarıda kesildi. `dogrula.py` 0 hata, 1 eski uyarı (etsy-api rol).

## Sıradaki
1. `python3 araclar/test.py` tam koşu (~10 dk, arka planda; yarıda kesme) → hepsi geçmeli. Tür zorunluluğu için `dogrula.py`'ye ait bir test yoksa `araclar/testler/` altına ekle (eksik `tur`/`bolum` → HATA; tam kayıt → boş liste).
2. `python3 araclar/katalog-uret.py && python3 araclar/skill-readme.py`; `git status`te KATALOG*.md, README-SKILLER.md, notlar/ değişmişse commit (medya çıkarımından sonra yenilenmediyse).
3. `python3 araclar/kapsam-denetimi.py` (0 sorun), `python3 araclar/dogrula.py` (0 hata).
4. Genel klasör taban kaydı (kullanıcı kararı "checkpoint-kapanis ve oturum-acilis KALACAK"): git temizken ve commit'ten hemen önce `python3 araclar/genel-bekci.py --taban-yaz --yenile --evet`, sonra commit.
5. Kayıt: `notlar/kararlar.md` K-65 mevcut; medya politikası satırı "gerekli medya arşivde kalır, kurulum aracının kaynaktan alması ihtiyaç olunca" ile uyumlu mu kontrol et; plan dosyasındaki "Uygulandı" ifadeleri gerçekle tutuyor mu (adım 3 satırı). Commit.
6. Temizlik: `$TMPDIR` altında yarıda kalan testten kalmış olabilecek `tmp*` klasörleri (hangisi teste ait emin değilsen silme); `git worktree list` yalnız ana klasör; `~/.claude/settings.json`'da advisorModel yok (danışman `.claude/settings.local.json`'da).
7. Sonra kullanıcıya TEK özet: yapılanlar, kontrol sayıları, arşiv boyutu önce/sonra (419 MB → ölç: `du -sh arsiv`), kullanılan modeller, kalan kararlar.

## Karar bekleyen
- [ ] Push: yerelde 36 commit var, push edilmedi — kullanıcı isteyince `git push origin master`.
- [ ] Ertelenen işler "ihtiyaç olunca" (K-65): adım 5 (aylık çalışma türlere göre), adım 6 (Windows taşınabilir paketi), 12 eklenti paketinin kök dosyaları, köke bağlı 104 skil, repo-içi 112 skil önerisi, gerekli medyayı (özellikle 200 KB üstü) kurulum aracının kaynaktan alması.
- [ ] Kullanıcı "süreçte bir problem var" dedi ve durdurdu; problemin ne olduğunu söylemedi — söylerse düzelt.
- [ ] Trend/aday kararları (10 aday), `.claude/settings.json` ile danışmanın depoya taşınması (şu an yalnız yerel).

## Vadesi gelen / takvimli
- Aylık çalışma: son 2026-11-02; 35 günü aşarsa (2026-12-07) sor.
- Yedek silme günleri: `python3 araclar/yedek-denetim.py` (ayar-2026-11-19 30 gün).

## Çalışma düzeni (kullanıcı kararları)
- Plan adımları sormadan yürür (K-65). Sorulanlar: push, projeler, genel skill klasörleri, plan dışı yeni kaynak, K-58, git geçmişi yeniden yazma, plan dışı silme.
- İşler Gemini 4 Neon/Argon ile (`~/.local/bin/agy`), yalnız Medium; ayrı worktree, görev dosyası worktree içinde, komut gereken iş sandbox'sız (yalnız o worktree), bitince git diff/test/genel klasör md5; "SUCCESS" kanıt değil; silen kod bağımsız inceleme ister. Ayrıntı: `rehber/15-ajanlar.md` ve K-65. Kota: `~/.cache/kotalar/usage.json`; devir: `~/Documents/Claude/SkillKutuphanesi-DEVAM.md` (T1-T9 listesi; T1-T6 bitti, T7-T9 yukarıdaki sıradaki adımlar).
- Gemini havuzu 5 saatlik pencereyle yenilenir; Argon bu oturumda %20'ye indi (haftalık, 25 Kas 16:30).

## Bilinen sorunlar / dikkat
- `gh` PATH'te yok: `export PATH=/usr/local/opt/gh/bin:$PATH`.
- `dogrula.py` 1 uyarı: rol `eticaret-magaza-operasyon` içinde `etsy-api` emekli.
- Medya raporu (`~/Documents/Claude/SkillKutuphanesi-saklanan/medya-ihtiyac.*`) 17 Shopify şema dosyasını yanlış "kullanılmıyor" saymıştı (silinmedi); 141 "belirsiz" ve "gerekli" dosyalar arşivde duruyor.
- tools/denetim.sh yok; hafif kontrol yapıldı (yollar var, boş dosya yok).
