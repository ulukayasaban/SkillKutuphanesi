# Kütüphane ajanları: ortak kurallar

Bu kurallar her kütüphane ajanı için geçerlidir. Kesin kurallar `CLAUDE.md` / `AGENTS.md` içindedir, kalıcı kararlar `notlar/kararlar.md` içindedir; burada yalnız ajanların çalışma biçimi yazılır. Bir kural rehberle çelişirse dur ve raporuna yaz.

1. **Çalışma yeri:** her komuttan önce `cd ~/Documents/SkillKutuphanesi`. Komutlar `python3 araclar/...` biçimindedir; başka klasörde çalıştırma.
2. **Kullanıcıyla sen konuşmazsın.** Soru, onay ve karar ana oturumun işidir. Emin olmadığın yerde dur ve raporuna yaz; tahminle ilerleme.
3. **Onay gerektiren adımı atma, raporla.** Şunlar kullanıcının o iş için verdiği açık onayı ister: bir projede herhangi bir değişiklik (kurulum, kaldırma, güncelleme, bağ, geri yükleme; K-50), yeni kaynak ekleme, kaynak çıkarma, kalıcı silme (yedekler dahil), program güncelleme ve geri alma, genel skill klasörleri, ayar, izin ve kabuk dosyaları, zamanlanmış görevler, GitHub'da her işlem (push, PR, yıldız, liste), `--evet`, `--zorla`, `--birlestir`, ücretli test. Ana oturum görev metninde "kullanıcı şunu onayladı: ..." diye açıkça yazdıysa yalnız o adımı uygula; onay başka adıma taşınmaz.
4. **Kayıt ana oturumundur:** `git commit` ve `git push` yapma, dal açma ve silme yapma. Tek istisna `arsiv-guncelle.py --aylik` komutunun kendi açtığı ve kendi kaydettiği daldır.
5. **Aynı anda tek yazar:** `registry.json`, `kaynaklar.json` ve `arsiv/` üzerinde başka bir iş sürüyorsa (`.guncelleme-kilidi` var ya da `git status --short` senin yapmadığın değişiklik gösteriyor) yazma, raporla.
6. **Dokunulmayanlar:** `arsiv/` içindeki skill dosyaları elle düzenlenmez. `programlar.json` elle biçimlenmiştir: yeniden serileştirme, yalnız hedefli metin düzenle. `registry.json` 22 MB'tır: tümünü yazdırma, küçük bir Python parçasıyla sorgula.
7. **Gizli değer yok:** `.env`, anahtar, token, parola, `~/.codex/auth.json`, `~/.hyperframes/config.json` içindeki kimlik alanları okunmaz ve yazdırılmaz. Yalnız "var" ya da "yok" de.
8. **Çalıştırılmayan komutlar:** `npx skills`, `hyperframes`, `nlm`, `uv tool`. Program sürümü dosyadan okunur. (Program ajanı, onaylı güncellemede yalnız `rehber/11-program-yonetimi.md` içinde yazan komutu çalıştırır.) `araclar/gelistirici-bilgisi.py` yardım metni basmaz; her çağrısı gerçek ağ taramasıdır.
9. **Ortam:** macOS'ta `timeout` komutu yok. `grep` ugrep'tir (günlük dosyalarında `grep -a`). zsh eşleşmeyen glob'da hata verir (tırnak kullan). Tırnaksız heredoc içinde ters tırnak ya da `$(...)` kullanma. `araclar/kapsam-denetimi.py` yaklaşık 10 dakika sürer ve ağ kullanır; `araclar/test.py` yaklaşık 3 dakika sürer; test sürerken dosya düzenleme.
10. **Kayıtlara proje adı yazılmaz** (`CLAUDE.md` kural 6). Proje bilgisi yalnız `projeler.json` ve `notlar/proje-kullanimi.md` içindedir.
11. **Danışman (yalnız Claude):** bu projede danışman modeli Opus'tur (`.claude/settings.local.json` → `advisorModel`; K-54). Danışmana yalnız şu anlarda sor: onay gerektiren bir adımı rapora koymadan önce planın doğru olup olmadığını; aynı hata ikinci kez çıktığında; işi bitti demeden önce. Rutin denetim komutlarında ve çıktısı belli işlerde sorma; her danışma ek kullanım demektir. Danışmanın önerisi onay yerine geçmez. Codex'te danışman yoktur.
12. **Rapor** (son mesajın; ana oturum okur, kullanıcı görmez; kısa ve ham veri):
    - ne yaptın (bir iki cümle),
    - değişen dosyalar (`git status --short`),
    - kontrol sonuçları sayılarıyla (ör. "dogrula 0 hata 1 uyarı"),
    - onay bekleyen adımlar ve çalıştırılacak tam komutlar,
    - emin olmadığın, yapamadığın ya da atladığın her şey.
    Başarısız kontrolü gizleme; çıktısını aynen yaz.
