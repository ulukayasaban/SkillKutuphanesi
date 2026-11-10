# 11 — Program yönetimi (skill olmayan yapılar)

Kütüphane yalnızca skilleri değil, kullanıcının kütüphaneye "dahil et" dediği **programları** da takip eder: kendi sürümü,
kendi kurulumu olan yapılar (örnek: `etsyotomasyon`). Program skill değildir; `skill-ekle.py` ile projeye kurulmaz.

## Nerede ne var
- `programlar.json` — her program için kart: repo, kütüphanedeki sürüm/commit, kurulum yolları (Windows/macOS/kaynaktan),
  veri yeri, bağlantı, ağ, güncelleme adımları, `asla` listesi.
- `programlar/<ad>/kaynak/` — programın sabit sürümdeki kaynak kopyası (değiştirilmez). `programlar/<ad>/KAYNAK.md` — repo,
  sürüm, commit, lisans, alınmayan klasörler.
- `kaynaklar.json` — programın reposu `tip: T5` + `"program": "<ad>"` (GitHub listesiyle eşleşme ve kapsam denetimi için).
- `notlar/referans/kutuphaneler.md` — programın tek satırlık özeti.
- `notlar/program-denetimi.md` — `python3 araclar/program-denetim.py` çıktısı.

## Yeni program eklemek (kullanıcı "dahil et" deyince)
1. Repoyu oku: SKILL.md var mı (varsa normal skill akışı, `03-yeni-skill-ekleme.md`), lisans, son release, bağımlılıklar,
   ağ trafiği, kendini güncelleyip güncellemediği, anahtar istiyor mu.
2. Son release etiketinin kaynağını ayrı bir geçici klasöre indir (`gh api repos/<repo>/tarball/<etiket>`), çalıştırma;
   demo/medya (`docs/`) ve CI (`.github/`) hariç `programlar/<ad>/kaynak/`'a kopyala; `KAYNAK.md` yaz.
3. `programlar.json`'a kart, `kaynaklar.json`'a T5 kaydı (`program` alanıyla), `kutuphaneler.md`'ye satır.
4. `python3 araclar/listeye-ekle.py owner/ad` (GitHub listesi), sonra her zamanki kontroller ve commit.

## Takip ve güncelleme
- `python3 araclar/program-denetim.py` kütüphanedeki sürümü GitHub'daki son sürümle karşılaştırır (salt okuma, çıkış 0).
- Yeni sürüm varsa: CHANGELOG özeti → kullanıcı onayı → kaynak kopyasını yeni etiketten yenile, `KAYNAK.md` ve kartı güncelle,
  commit → programı kullanan makinelerde kullanıcıyla birlikte yenile.

## Kurallar
- Program kopyası proje deposuna konmaz; projeye yalnızca kullanım notu (hangi ekran/komut kullanılır, hangisi kullanılmaz) yazılır.
- Anahtar, şifre, oturum dosyalarını agent girmez, açmaz, yazdırmaz; hesap bağlama adımlarını kullanıcı yapar.
- Kartlarda proje adı ve "şu projeye uyar" yazılmaz (kütüphane kuralı 6); projeye uygunluk kurulum sırasında incelenir.
