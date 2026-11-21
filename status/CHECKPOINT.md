# CHECKPOINT — SkillKutuphanesi
Son güncelleme: 2026-11-20 06:45

## Şimdi
- **Yeni süreç planı (beklemede, 2026-11-21):** `notlar/istenen-surec.md` TAMAM (kullanıcının istediği süreç, bütün sorular kapandı); `notlar/yeni-surec-plani-calisma.md` adım 1-3 tamam. Sıradaki: istenen süreci bugünkü kütüphaneyle karşılaştır (hazır/yarım/yok), sonra adım 4. Yeni oturumda önce bu iki dosyayı oku.
- Plan `notlar/plan-tur-surecleri.md`: ÇEKİRDEK KAPSAM bitti ve kapanış adımları tamamlandı (2026-11-20 06:45). Arka planda süreç, Neon ya da worktree yok.
- Bu oturumda: tür/boyut/fihrist/medya çekirdeği (K-65) kapandı; `test.py` 324/324, `dogrula.py` 0 hata 1 eski uyarı (etsy-api rol), `kapsam-denetimi` 0 sorun, `genel-bekci` TEMİZ (taban yenilendi, `checkpoint-kapanis` ve `oturum-acilis` kalacak). Tür zorunluluğu testleri `test_p15` (+3) ve eski sahte kayıtlar `test_p8/p14/p19` düzeltildi.
- Programlar güncellendi (K-66): HyperFrames 0.9.37 → 0.9.71, OpenMontage `fecb9a1e` → `2e003e65`; duman testi 142 geçti / 1 FAIL (projenin eski HF sürüm kaydı, düzeltildi). Bulgular `notlar/program-incelemesi-2026-11-20.md`. Güncelleme yedekleri kullanıcı kararıyla silindi.
- Arşiv 419 MB → 283 MB. `~/.claude/settings.json`dan `advisorModel` kaldırıldı (yedek `ayar-2026-11-20`; danışman yalnız `.claude/settings.local.json`'da).
- IstatistikYoutube (kullanıcı onayıyla): 13 test/araç dosyasına geçici klasör temizliği, `config/tools.yaml` HF kaydı 0.9.71; yedek `istatistik-test-temizlik` silindi (geri dönüş yok, proje git kullanmıyor).

## Sıradaki
1. Kullanıcı isteyince: ertelenen işler (aşağıda), trend adayları, aylık çalışma.
2. Bu oturumun son commit'i push edilmedi (varsa `git log origin/master..master`).

## Karar bekleyen
- [ ] Ertelenen işler "ihtiyaç olunca" (K-65): plan adım 5 (aylık çalışma türlere göre), adım 6 (Windows taşınabilir paketi), 12 eklenti paketinin kök dosyaları, köke bağlı 104 skil, repo-içi 112 skil önerisi, gerekli medyayı (200 KB üstü) kurulum aracının kaynaktan alması.
- [ ] Trend/aday kararları (10 aday: `python3 araclar/konu-takip.py --bekleyenler`).
- [ ] `.claude/settings.json` ile danışmanın depoya taşınması (şu an yalnız yerel).
- [ ] Önceki "süreçte problem var" bildirimi: problemin ne olduğu söylenmedi.
- [ ] Kalan yedekler (boşaltma/geçiş: akil-disi-tam 3,4 GB, istatistik-skill-gecisi, genel-skiller-tam, genel-kaldirilan, global-skills-2026-11-08) ve `deneme/openmontage-fecb9a1e` (2,9 GB, ~12 Aralık): silme yalnız kullanıcı "sil" deyince.
- [ ] IstatistikYoutube: `cakisma_tara.py`/`ekran_yazi_kontrol.py` sızıntı düzeltmesi yapıldı; `test_muzik_akis_kapi.py` yavaş (>150 sn), zaman aşımında temizlik çalışmaz.

## Vadesi gelen / takvimli
- Aylık çalışma: son 2026-11-02; 35 günü aşarsa (2026-12-07) sor.
- `deneme/openmontage-fecb9a1e` silme günü ~2026-12-12 (kullanıcı "şimdilik silme" dedi).

## Çalışma düzeni (kullanıcı kararları)
- Plan adımları sormadan yürür (K-65). Sorulanlar: push, projeler, genel skill klasörleri, plan dışı yeni kaynak, K-58, git geçmişi yeniden yazma, plan dışı silme.
- İşler Gemini 4 Neon/Argon ile (`~/.local/bin/agy`), yalnız Medium; ayrı worktree, görev dosyası worktree içinde, komut gereken iş sandbox'sız (yalnız o worktree), bitince git diff/test/genel klasör md5; "SUCCESS" kanıt değil; silen kod bağımsız inceleme ister. Ayrıntı: `rehber/15-ajanlar.md` ve K-65. Kota: `~/.cache/kotalar/usage.json`; devir: `~/Documents/Claude/SkillKutuphanesi-DEVAM.md` (T1-T9 listesi; T1-T6 bitti, T7-T9 yukarıdaki sıradaki adımlar).
- Gemini havuzu 5 saatlik pencereyle yenilenir; Argon bu oturumda %20'ye indi (haftalık, 25 Kas 16:30).

## Bilinen sorunlar / dikkat
- `gh` PATH'te yok: `export PATH=/usr/local/opt/gh/bin:$PATH`.
- `dogrula.py` 1 uyarı: rol `eticaret-magaza-operasyon` içinde `etsy-api` emekli.
- Medya raporu (`~/Documents/Claude/SkillKutuphanesi-saklanan/medya-ihtiyac.*`) 17 Shopify şema dosyasını yanlış "kullanılmıyor" saymıştı (silinmedi); 141 "belirsiz" ve "gerekli" dosyalar arşivde duruyor.
- tools/denetim.sh yok; hafif kontrol yapıldı (yollar var, boş dosya yok).
