# BASLA — kütüphane oturumuna giriş (her yapay zeka aracı için)

Sen bu kütüphanenin hafızasız oturumusun: önceki konuşmaları görmezsin. Bilmen gereken her şey bu klasörde yazılı.
Kütüphane: skill arşivi + araçlar. Skiller yalnız projenin içine, yalnız `skill-ekle.py` ile kurulur. HyperFrames,
OpenMontage gibi programların takibi ve güncellemesi de burada yapılır. Kullanıcı bunları kendisi izlemez; sen izlersin,
her gerçek değişiklikte onayını alırsın.

**Başka klasörden açıldıysan (Codex, Antigravity, Cursor, VS Code Copilot):** önce `cd ~/Documents/SkillKutuphanesi`.
Aşağıdaki bütün komutlar bu klasörde çalışacak biçimde yazıldı (`python3 araclar/...`); başka klasörde çalıştırma.

## 1. Okuma sırası
1. Bu dosya.
2. `CLAUDE.md` (Claude Code okur) ya da `AGENTS.md` (Codex, Antigravity, Cursor, VS Code Copilot okur). İkisi birebir aynı olmalıdır; kesin kurallar orada.
3. `notlar/kararlar.md`: kullanıcının verdiği kalıcı kararlar. Birini değiştirmeden önce kullanıcıya sor.
4. `notlar/hf-om-gecisi/DURUM.md`: yalnız çizelgesinde durumu "bitti" olmayan adım varsa oku. Hepsi bitti ise atla.
5. İsteğe uyan rehber (aşağıdaki tablo).

## 2. Oturum başı rutini
Kütüphane oturumunun ilk işi (kütüphane klasöründe):
```
python3 araclar/aylik-ozet.py --hizli
```
Çıktıyı kullanıcıya iki cümleyle söyle. Aylık çalışma 35 günü aştıysa "Aylık çalışmayı şimdi yapayım mı?" diye sor; evet derse
önce `python3 araclar/arsiv-guncelle.py --aylik --kuru` (plan, hiçbir şey değiştirmez), sonra `python3 -u araclar/arsiv-guncelle.py --aylik` (tek komut: dal hazırlar, özet verir, damga yazar; birleştirmez), dal özeti, onay, `--birlestir <dal>` (`rehber/02-guncelleme-yonergesi.md`).
Hızlıdır (yaklaşık 5 sn), ağ kullanmaz, hiçbir şey yazmaz, en çok 15 satır basar. Git durumunu, genel klasörlerde beklenmeyen girdi olup olmadığını,
yedek yaşını, son aylık çalışmayı ve karar bekleyenleri toplar.
- Sonuç `temiz`: kısa bir cümleyle söyle, başka bir şey yapma.
- Sonuç `dikkat` ya da `sorun`: en fazla 5 satırla, sade Türkçe ile söyle. Kendiliğinden düzeltme, silme, taşıma, push yapma.
- Tam özet (ayda bir ya da kullanıcı isterse): `python3 araclar/aylik-ozet.py` (ağ kullanır, bazı rapor dosyalarını yazar). Yapay zeka aracı belgelerinin bayatlığı (`python3 araclar/skill-ekle.py --araclar`) yalnız tam aylık çalışmada görünür.
- Komut yok ya da hata verirse kullanıcıya söyle; yerine tek tek çalıştır: `python3 araclar/git-durum.py --kisa`,
  `python3 araclar/genel-bekci.py --ozet-json`, `python3 araclar/yedek-denetim.py --ozet-json`.

## 3. Hangi istek, hangi rehber, hangi komut
| Kullanıcı ne diyor | Rehber / istem | İlk komut (hepsi önce rapor, değişiklik onayla) |
|---|---|---|
| "Şu projeye skill kur" | `rehber/01-skill-ekleme-sureci.md`, `promptlar/01-yeni-proje-skill-kurulumu.md` | `python3 araclar/skill-ekle.py <proje> --oner "<ihtiyaç>"`, sonra `--kuru`, onay, `--evet`, `--dogrula` Programla gelen skiller (OpenMontage/HyperFrames) kopyalanmaz: `--program-skill PROGRAM:AD` (bağ); kaynağı artık hiçbir yerde verilmeyen eski skiller `--dondur <yol>` (donmuş). Kendi skillerin `kendi/` klasöründen `--skill` ile kurulur. |
| Hangi AI araçlarını kullanıyor / yeni araç ekle | `rehber/14-yapay-zeka-araclari.md`, `promptlar/15-yeni-yapay-zeka-araci.md` | `yapay-zeka-araclari.json` oku; kurulumda `--arac` seçimini sor (`python3 araclar/skill-ekle.py --araclar` belge kontrolü) |
| "Yeni skill ekledim, kontrol et" (yeni kaynak) | `rehber/03-yeni-skill-ekleme.md` A1..A9, `promptlar/07-yeni-skill-reposu-ekle.md` | `python3 araclar/github-skill-listesi.py`, çakışma ve ücret kontrolü, onaysız ekleme yok |
| Kendi skilimi kütüphaneye al / kendi skilimi düzenledim | `rehber/03-yeni-skill-ekleme.md` B2, `kendi/README.md` | `python3 araclar/kaynak-cek.py --repo yerel/kendi` (ağ yok), sonra `python3 araclar/arsiv-yerlestir.py`; projede `skill-ekle.py <proje> --durum` |
| Bir kaynağı ya da skili çıkar | `rehber/03-yeni-skill-ekleme.md` "D) Kaynak / skill KALDIRMAK" (etki raporu araçla, çıkarma D adımlarıyla elle), `promptlar/14-kaynak-cikar.md` | `python3 araclar/proje-kullanimi.py --skill <kimlik>` (etki), sonra `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` |
| "Skilleri güncelle" (aylık) | `rehber/02-guncelleme-yonergesi.md`, `promptlar/08-aylik-guncelleme-onayi.md` | `python3 araclar/arsiv-guncelle.py --aylik --kuru`, sonra `python3 -u araclar/arsiv-guncelle.py --aylik` (tek komut), dal özeti, onay, `--birlestir <dal>` |
| Projeleri kontrol et, proje ekle/çıkar/taşındı | `rehber/10-proje-kullanimi.md`, `promptlar/12-proje-kullanimi-ve-etki.md` | `python3 araclar/proje-kullanimi.py --saglik` (kayıtsız klasörleri de tarar; yazıcılar: `--ekle`, `--cikar`, `--tasindi`, `--yoksay`, önce plan, onayla `--evet`); bağ ve donmuş skiller `--saglik`te görünür |
| Git durumu, push gecikmesi, geri alma | `rehber/02-guncelleme-yonergesi.md`, `rehber/13-yedek-ve-geri-alma.md` | `python3 araclar/git-durum.py --kisa` (push yalnız kullanıcı isteyince) |
| HyperFrames / OpenMontage / başka program: kur, güncelle, geri al, çıkar | `rehber/11-program-yonetimi.md`, `promptlar/13-program-kur-guncelle.md` | `python3 araclar/program-denetim.py --oncesi <ad>` "HAZIR" demeden dokunma (gerçek yazma yalnız kural 1 istisnasıyla: bkz. madde 6) Güncellemeden önce ve sonra projelerdeki bağlar: `python3 araclar/proje-kullanimi.py --program <ad>`. |
| Genel skill klasörlerinde beklenmeyen girdi var / yeniden boşalt (boşaltma 2026-11-12'de yapıldı, K-40) | `rehber/12-genel-klasor-bosaltma.md`, `promptlar/16-genel-klasor-bosaltma.md` | `python3 araclar/genel-bekci.py` (yalnız okur); her adım ayrı onay (yeniden boşaltma yalnız kural 1 istisnasıyla: bkz. madde 6) |
| Yedek, geri alma, yedek silme hatırlatması | `rehber/13-yedek-ve-geri-alma.md` | `python3 araclar/yedek-denetim.py` (silmez; silmeyi kullanıcı onaylar) |
| Kütüphane sağlık kontrolü | `promptlar/10-kutuphane-saglik-kontrolu.md` | `python3 araclar/dogrula.py`, `python3 araclar/duman-testi.py` (temiz ağaç ister; commit öncesi `--kirli-ok`) |
| Yeni bilgisayar / klon | `README.md` "Başka bilgisayarda kurmak", `rehber/13-yedek-ve-geri-alma.md` | `python3 araclar/dogrula.py`, `python3 araclar/git-durum.py` |
| Ad çakışması, aynı ad farklı skill | `rehber/09-ad-kimlik-ve-cakisma.md` | `python3 araclar/proje-kullanimi.py --skill <kimlik>` |
| Proje taşındı ya da bozuldu | `promptlar/09-proje-tasindi-veya-bozuldu.md` | `python3 araclar/skill-ekle.py <proje> --dogrula` |

**Hangi iş hangi ajan:** kütüphanenin yedi ajanı vardır; iş-ajan tablosu `CLAUDE.md` "Ajanlar" bölümünde, çalışma biçimi `rehber/15-ajanlar.md` içindedir. Ajan kullanmayan araç da işe uyan `ajanlar/kutuphane-<ad>.md` dosyasını okuyup o kapsamla çalışır.

## 4. Her zaman geçerli kurallar
1. Kullanıcıyla konu konu, sade Türkçe ile konuş; plan belgesi yığma; en fazla bir soru sor.
2. Gerçek değişiklik (kurulum, kaldırma, taşıma, güncelleme, ayar dosyası, genel klasör, silme) önce rapor, sonra kullanıcının ayrı onayı. Önceki onay sonrakini kapsamaz.
3. GitHub'da yalnız `ulukayasaban/SkillKutuphanesi`; push ve PR yalnız kullanıcı isteyince; depo private kalır.
4. Kayıt dosyalarına (`registry.json`, `kaynaklar.json`, `programlar.json` kartları, öncelik) proje adı ya da "şu projeye uyar" gerekçesi yazılmaz. Proje bilgisi `projeler.json` ve `notlar/proje-kullanimi.md`'de.
5. Bilmediğin ya da çelişen bir durumda dur, kullanıcıya sade sor. Gizli anahtar, parola, token değerini asla okuyup yazma; yalnız var mı yok mu söyle.
6. Genel skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) yazma: `CLAUDE.md` kural 1'in istisnası onaylandı (K-24) ve yalnız `rehber/11` ile `rehber/12` adımları içindir; her işe ayrı onay. Genel skill klasörleri 2026-11-12'de boşaltıldı (K-40): orada skill kurulmaz, beliren girdiyi bekçi bildirir.

## 5. Hangi araç hangi dosyayı okur
Claude Code: `CLAUDE.md`. Codex, Antigravity, Cursor, VS Code Copilot: `AGENTS.md`. Gemini CLI ve Copilot CLI bu bilgisayarda kurulu değil,
`GEMINI.md` yok. Windows'ta `skill-ekle.py` çalışmaz; Windows'ta açılan projeler için karar bekliyor (`notlar/kararlar.md` sorular, `rehber/14-yapay-zeka-araclari.md`).
Kurulurlarsa `rehber/14-yapay-zeka-araclari.md` "Yeni AI aracı" yolu izlenir.

## 6. İş bitince
`python3 araclar/kapsam-denetimi.py` (0 sorun), `python3 araclar/dogrula.py` (0 hata), gerekirse `python3 araclar/test.py`;
sonra commit önerisini kullanıcıya söyle (onaysız commit yok). `CLAUDE.md` değiştirdiysen `cp CLAUDE.md AGENTS.md` yap.
