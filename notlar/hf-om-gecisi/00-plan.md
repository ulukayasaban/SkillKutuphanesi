# HyperFrames + OpenMontage planı (2. sürüm, eleştiriden sonra)

Durum: **onay bekliyor, hiçbir adım uygulanmadı.** Tarih: 2026-11-10.
Kısa hâli: `KISA-OZET.md`. Nerede kaldığımız: `DURUM.md`. Eski plan: `rafta/`. Eleştiri: `ELESTIRI.md`.

## 1. Tek cümle
Skilleri yerinden oynatmıyoruz. Tek gerçek tehlikeyi (kendiliğinden güncelleme) kapatıyoruz, yedek alıyoruz,
durumu görünür kılıyoruz ve **duruyoruz**.

## 2. Plan neden küçüldü
- Eski plan skilleri bilgisayarın genelinden kütüphaneye taşıyordu. Eleştiri bunun faydasını kanıtlayamadı, riskini gösterdi.
- "Bilgisayarın genelinde duran skill, projenin içindeki skilin önüne geçer" varsayımı **doğrulanmadı**.
- İki projede genel klasöre sabit yol var (aşağıda 7. bölüm). Taşıma bunları bozar.
- IstatistikYoutube'un kendi skill denetimi var ve 07.11'de "genel skillere dokunulmaz" kararı alınmış.
- Emekli skiller zaten kütüphanenin git geçmişinde duruyor (`620f7a135`, `622c984cc^`). Ayrıca saklamaya gerek yok.

## 3. Bugünkü durum (ölçüldü, 2026-11-10)
| Konu | Durum |
|---|---|
| HyperFrames aracı | 0.9.23, `/usr/local/lib/node_modules/hyperframes` (110 MB). Yayındaki en yeni: 0.9.29 |
| Kendiliğinden güncelleme | 17 Ekim – 7 Kasım arasında 7 kez olmuş (`~/.hyperframes/auto-update.log`). Dondurma ayarı **yok** |
| Kurulu 0.9.23'ün kaynağı | 8 Kasım'da kurulmuş ama günlükte yok. Nasıl kurulduğu **doğrulanmadı**; dondurmanın bu yolu kapatıp kapatmadığı bilinmiyor |
| OpenMontage | `~/.openmontage`, commit `c806645`. Kaynağın en az 21 commit / 86 dosya gerisinde (7 Kasım'daki yerel kayda göre) |
| OpenMontage'daki yerel değişiklik | 9 dosyada yama + kayıt dışı dosyalar (`gfpgan/`, `clips_cache/`, `remotion.config.ts`, 3 eski kopya) |
| OpenMontage Python ortamı | 3.3 GB, sürümler sabit (Python 3.10, torch 2.2.2, numpy 1.26.4). Kaynak 3.10 ve üstünü kabul ediyor ama güncel paketler bu sabit sürümleri bozabilir: **yeniden kurulmaz** |
| Python ortamının bağlı olduğu yer | `~/.local/share/uv/python/cpython-3.10-macos-x86_64-none` (212 MB). Bu olmadan ortam açılmaz |
| OpenMontage'ın kullandığı HyperFrames | Genelde kurulu olan (0.9.23). Ayrı bir kopyası yok |
| `~/.claude/skills` | 104 kayıt: 75 OpenMontage bağlantısı, 6 bağlantı `~/.agents/skills`'e, 21 gerçek klasör, 2 yerleşik |
| `~/.agents/skills` | 27 gerçek klasör (16'sı HyperFrames kaynaklı, 11'i yerel) |
| `~/.codex/skills` | 13 kayıt (11 bağlantı, `playwright`, `.system`) |
| HyperFrames skilleri | Kaynak bugün 9 skill yayınlıyor; 14'ü emekli oldu |
| Bağlantı kaydı | `~/.config/openmontage/global-skill-links.txt`: 79 satır, 4'ü ölü (`gsap-core`, `gsap-performance`, `gsap-plugins`, `gsap-timeline`) |
| Aynı adlı skiller | Genel OpenMontage bağlantılarının 18'i kütüphanedeki bir skille aynı adda (GSAP 4, Three.js 10, Vercel 3, video-edit 1) |
| Yedek | Yok. Time Machine kapalı. Takılı disk "ADIL HD" uygun değil (exFAT, 4.6 GB boş) |
| Claude yasak listesi | `~/.claude/settings.json` içinde `deny` kuralı yok |
| Kütüphane denetimi | `kapsam-denetimi.py` çöküyor: `J-DTurner/etsy-api-skill` GitHub'da yok (404) |
| Projeler | Akıl Dışı, IstatistikYoutube, Psikolojik Danışman git deposu değil: bozulursa tek kurtarma yolu yedek |

## 4. Adımlar
Her adımın sahibi yazılı. "Ben" = bu kütüphane oturumu. Bir adım bitmeden sonrakine geçilmez.

**Adım 0 – Kütüphane denetimini onar (ben, onayla)**
- `araclar/kapsam-denetimi.py`: silinmiş kaynak görünce çökmesin, "GitHub'da yok, KAYIP" diye yazsın ve devam etsin.
- `J-DTurner/etsy-api-skill` kaydına "erişilemiyor" notu. Arşivdeki kopyası silinmez.
- Aylık zamanlanmış görev (`skill-kutuphanesi-aylik-guncelleme`, sıradaki çalışma 2026-12-01 10:00) iş bitene kadar duraklatılır; kapanışta yeniden açılır.
- Bitti sayılır: `kapsam-denetimi.py` ve `dogrula.py` hatasız çalışır.

**Adım 1 – Dondurma (sen, tek komut)**
```bash
printf '\n# HyperFrames: skiller ve arac kendiliginden guncellenmesin (SkillKutuphanesi plani)\nexport HYPERFRAMES_SKIP_SKILLS=1\nexport HYPERFRAMES_NO_AUTO_INSTALL=1\nexport HYPERFRAMES_NO_UPDATE_CHECK=1\n' >> ~/.zshenv
```
- Kontrol (sen): yeni bir Terminal penceresinde `env | grep HYPERFRAMES` → tam 3 satır.
- Kontrol (ben): Claude'un kendi komut satırında ve `bash -c "env | grep HYPERFRAMES"` ile de bakarım. Orada görünmüyorsa rapora yazarım.
- Ne sağlar: `hyperframes` komutunun **kendi** güncellemesi ve skill yazması kapanır (Terminal/zsh'ten başlayan işlerde).
- Ne sağlamaz: `npx skills`, `make setup`, `pip install -U`, `git pull` bunu dinlemez. Onlar için Adım 4'teki yasak listesi var.
- Bilinmeyen: Terminal dışından başlayan işler (uygulamalar, zamanlanmış görevler) ve 8 Kasım'daki günlüksüz kurulum yolu. Adım 3 raporu sürümü izler.
- Geri alma: `~/.zshenv` içinden `# HyperFrames:` satırını ve altındaki 3 `export` satırını sil.

**Adım 2 – Skill ve araç yedeği (ben)**
- Yer: `~/Documents/Claude/yedek/makine-<tarih>/` (kütüphane deposunun dışında).
- İçine girenler: `~/.claude/skills`, `~/.agents`, `~/.codex/skills`, `~/.config/openmontage`, `~/.hyperframes`, kurulu HyperFrames aracı,
  `~/.openmontage` (Python ortamıyla), ortamın bağlı olduğu `~/.local/share/uv/python/cpython-3.10-macos-x86_64-none`, model önbellekleri (`~/.cache/hyperframes`, `~/.cache/huggingface`, `~/.piper`, `~/.u2net`),
  dört proje klasörü (Akıl Dışı, IstatistikYoutube, IstatistikYoutube-Arsiv, Psikolojik Danışman).
- Küçük ama değerli dosyalar: `~/.claude/projects/*/memory/`, `~/.claude/settings.json`, `~/.codex/config.toml`, `~/.zshenv`.
- Anahtar dosyaları (onay verirsen): açılmadan kopyalanır, içeriği hiçbir yere yazdırılmaz, izinleri `700/600`. Harici diske **konmaz**.
- Kapsam dışı: oturum geçmişleri (`~/.claude/projects` 5.9 GB, `~/.codex` 4.6 GB). Etsy-Arif ve Yetisio git deposu: sadece kaydedilmemiş dosyaları alınır.
- Boyut ve süre: yaklaşık 30 GB, çok sayıda küçük dosya var; ilk kopya birkaç on dakika sürebilir. Mac açık kalsın. Başlamadan `du` ile ölçerim (boş yer: ~154 GB).
- Başlamadan: çalışan bir video üretimi olmadığına bakarım.
- Yöntem: yeni araç yazılmaz. `rsync -a` (bayrakları önce küçük bir deneme klasöründe denerim; olmazsa `ditto`).
- Doğrulama: iki tarafta da dosya listesi + `shasum -a 256` karşılaştırması; bağlantılar için `find -type l` + `readlink` karşılaştırması.
  Saatlik çalışan işlerin yazdığı durum/günlük klasörleri karşılaştırmadan çıkarılır.
- Python ortamı için söz: "yedekte dosya olarak duruyor; gerekirse paket listesinden yeniden kurulur". Paket listesi (`uv pip freeze`) yedeğe eklenir.
  Ek kontrol: yedekteki Python `python3.10 -c "import sys"` ile açılıyor mu.
- İkinci kopya: sadece uygun disk varsa (APFS, en az ~32 GB boş). Önce `diskutil info /Volumes/<disk>` ile bakılır.
- Sınır: HyperFrames'in eski sürümleri (0.8.142/0.8.143) diskte yok, yedeklenemez. Sürümü geri alma sözü verilmez.

**Adım 3 – Durum raporu (ben, sadece okur)**
- Bilgisayarın genelindeki skiller, sürümler, bağlantılar, 18 aynı adlı skill, bağlantı kaydındaki 4 ölü satır.
- Koruma yerinde mi: 3 ortam değişkeni duruyor mu, yasak listesi duruyor mu, HyperFrames sürümü değişmiş mi.
- Projelerde genel klasöre sabit yol taraması: `grep -rIE --exclude-dir=node_modules '/\.(codex|agents|claude)/skills' .`
- Çıktı: genel kısım `notlar/makine-durumu.md` (proje adı yazılmaz); proje kısmı `~/Documents/Claude/hf-om-raporlar/`.
- Bunu küçük, sadece okuyan bir betikle yaparım (`araclar/makine-rapor.py`). Aylık güncellemenin sonunda da çalışır ve sürüm değişmişse söyler.

**Adım 4 – Senin uygulayacağın hazır metinler (ben hazırlarım, sen uygularsın)**
- Claude yasak listesi (`~/.claude/settings.json` → `permissions.deny`). Taslak:
  `Bash(*make setup*)`, `Bash(pip install *-U*)`, `Bash(pip install *--upgrade*)`, `Bash(npx skills *)`,
  `Bash(hyperframes update*)`, `Bash(hyperframes init*)`, `Bash(hyperframes skills *)`, `Bash(git*pull*)`.
  - Bu kurallarda `~` çalışmaz; o yüzden klasör adı yazılamıyor. Son satır Claude'un **her projede** `git pull` yapmasını engeller
    (sen Terminal'de yine yaparsın). İstemezsen o satır çıkar; o zaman OpenMontage'da `git pull` sadece söze kalır.
  - Liste, sana verilmeden önce bir deneme oturumunda sınanır. Codex'i kapsamaz.
- OpenMontage yamalarını kayda alma (sen çalıştırırsın):
  `cd ~/.openmontage && git switch -c yerel-yamalar && git add -u && git add remotion-composer/remotion.config.ts && git commit -m 'yerel yamalar'`
  (`gfpgan/` ve `clips_cache/` eklenmez. Depo sonra `yerel-yamalar` dalında kalır; `main` dalına dönülmez, yoksa yamalar görünmez olur.)
- `openmontage` skilinin 62. satırındaki "beş araç" → 9 dosya düzeltmesi.
- Bağlantı kaydındaki 4 ölü satırın silinmesi.

**Adım 5 – Projeler kendini denetler (sen yapıştırırsın, sadece okur)**
- `01-proje-promptlari.md` içindeki kısa promptları ilgili proje oturumuna yapıştırırsın. Rapor `~/Documents/Claude/hf-om-raporlar/` altına düşer.
- Ben raporları okur, sana tek sayfada özetlerim.

**Kapanış (ben, sana sorarak):** duraklatılan aylık görev yeniden açılır. Açılana kadar aylık sürüm kontrolü yoktur.

**Sonra: dur.** Raporlarda gerçek bir arıza yoksa iş burada biter.

## 5. Koruma neye dayanıyor
Koruma = 3 ortam değişkeni + yasak listesi + aylık rapordaki kontrol.
- Bu **tam engel değildir.** Yasak listesi Claude'un olağan komut yazımını durdurur; başka yazımla ya da başka araçla aşılabilir.
- Aşılırsa rapor bunu **önlemez**, en geç bir ay sonra gösterir. O zaman yedekten dönülür.
- Dosya kilitleme (`chflags uchg`) kullanılmaz.

## 6. Koordinasyon: skill işleri tek yerden
- Bu bilgisayarda skill kurma, güncelleme, kaldırma **sadece bu kütüphane oturumunda** konuşulur.
- Proje oturumları skill kurmaz, güncellemez. İhtiyaç olursa bana yazarsın.
- Yeni bir yapay zekâ aracı kurarken "skilleri içe aktar / eşitle" sorusuna **hayır** dersin.
- Diğer araçların genel talimat dosyalarına kural yazılmaz (bu senin kararın). Bu yüzden güvence: yasak listesi + aylık rapor.
- Sık olan olaylar ve kimin ne yapacağı: `02-yapilacaklar-listesi.md`.

**Kütüphanede değişecekler (hepsi küçük):**
- `kapsam-denetimi.py`: silinmiş kaynakta çökmeme (Adım 0).
- Yeni, sadece okuyan `araclar/makine-rapor.py` ve çıktısı `notlar/makine-durumu.md` (Adım 3).
- Aylık güncelleme akışının sonuna bu raporun eklenmesi; `CLAUDE.md` "Bakım isteklerinde" bölümüne tek satır.
- Değişmeyenler: kural 1 (genel klasörlere yazmama), `skill-ekle.py`, arşiv araçları, kayıt yapısı.

## 7. Dokunulmayacaklar
- **IstatistikYoutube**: kendi denetimi var (`tools/skill_durum.py`, `status/skill-global.yaml`). Hiçbir taşımaya girmez.
- **`motion-doctrine`** ve **`talking-head-recut`**: Akıl Dışı'nın üretim betikleri bunlara genel klasörden sabit yolla bağlı. Yerinden oynamaz.
- **75 OpenMontage bağlantısı** yerinde kalır: `openmontage` skili alt skilleri adıyla yüklüyor. Liste uzunluğu rahatsız ederse proje başına kapatılır (`skillOverrides`).
- **OpenMontage güncellenmez.** Yerel yamalar ve sabit Python ortamı kaybolur.
- **Etsy-Arif**: Arif'in deposu; işleri kendi oturumunda.
- `faceless-explainer` ve `general-video` yalnızca eski üretim kayıtlarında geçiyor; projelere kurulmaz.

## 8. Rafta (ancak gerçek arıza çıkarsa, ayrı onayla)
- Skilleri bilgisayarın genelinden kütüphaneye/projelere taşıma (eski "2. aşama").
- Yeni taşıma aracı (`makine.py --tasi / --geri-koy / --dondur`), "dondurulmuş" kayıtlar, `ad_sabit`, kural 1'e istisna.
- `arsiv-guncelle.py` ve `arsiv-yerlestir.py` değişiklikleri.
- 75 OpenMontage bağlantısını kaldırma.
- Eski planın 13 karar sorusu.
Açılırsa önce `ELESTIRI.md` içindeki 7, 9, 14, 22 numaralı düzeltmeler uygulanır.

## 9. Durma ölçütü ve kapsam dışı
- Biter: Adım 0–5 tamam, raporlarda arıza yok, aylık görev yeniden açıldı, `DURUM.md` "bitti" diyor. Sonra bu klasör arşivlenir.
- Arıza çıkarsa: sadece o arıza için ayrı, küçük bir öneri getiririm.
- Proje dosyasına yazan her iş için ön şart: yedek 24 saatten yeni; o projede başka oturum ya da video üretimi çalışmıyor.
- Kapsam dışı: bulut oturumları, ikinci bilgisayar, Codex'in yasak listesi, oturum geçmişlerinin yedeği.

## 10. Asla yapılmayacaklar
- Silip baştan kurma yok. Silme yok; gerekirse yedeğe taşıma.
- `hyperframes skills update`, `hyperframes update`, `hyperframes init`, `npx skills …` çalıştırılmaz.
- Kurulu HyperFrames aracı kaldırılmaz: OpenMontage onu sürüm belirtmeden çağırıyor; kaldırılırsa internetten en yenisini çeker.
- `~/.openmontage` içinde ben git komutu çalıştırmam. Kimse `git pull`, `git checkout .`, `git reset --hard`, `git clean`, `make setup`, `pip install -U` çalıştırmaz.
- `~/.agents/.skill-lock.json` elle düzenlenmez.
- Ben şunlara yazmam, sadece hazır metin veririm: `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`, ayar dosyaları, anahtar dosyası, `~/.zshenv`.
- Anahtar dosyasının içeriği okunmaz, yazdırılmaz.
- Kütüphane dışındaki hiçbir GitHub deposunda işlem yok. İstemeden push yok.

## 11. Sözlük
- **Bilgisayarın genelinde duran skill**: `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills` içindeki; her projede görünür.
- **Projenin içindeki skill**: proje klasöründeki; sadece o projede görünür.
- **Dondurma**: aracın kendini ve skillerini kendiliğinden güncellemesini kapatmak.
- **Bağlantı**: asıl klasörü gösteren kısayol (symlink). Asıl klasör giderse bağlantı ölür.
- **Yama**: OpenMontage dosyalarında bu bilgisayara özel yapılmış düzeltme.
- **Yasak listesi**: Claude'un çalıştırmayı reddedeceği komutlar (`permissions.deny`).
- **Rafta**: şimdilik yapılmayacak; ancak gerekirse ve ayrı onayla açılır.
