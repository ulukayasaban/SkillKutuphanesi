# Yedek ve geri alma

Bu rehber iki şeyi söyler: yedek nereye konur, nasıl geri alınır. Kütüphanenin kendi git geçmişi, projelerin otomatik yedeği ve
kütüphane dışına alınan yedekler (ayar dosyaları, programlar, genel skill klasörleri) ayrı yerlerdedir. Hepsinin özeti burada.
Kayıt: `yedekler.json`. Denetim: `python3 araclar/yedek-denetim.py` (salt okuma, hiçbir şeyi silmez).
Git durumu: `python3 araclar/git-durum.py` (salt okuma, push etmez).

## 1. Tek kural
1. Kütüphane dışına alınan her yedek `~/Documents/Claude/yedek/` altında durur. Kütüphane klasörüne, git'e, skill klasörlerine
   (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`) ve `~/.openmontage` içine konmaz (araçlar yedekteki SKILL.md'yi skill sanar).
2. Ad: `<ne>-<YYYY-AA-GG>` (ör. `ayar-2026-11-11`, `global-skills-2026-11-08`, `hyperframes-2026-12-03`). Aynı gün ikinci yedek: sonuna `-2`.
3. Gizli bilgi olabilecek yedek (ayar dosyaları, `.env`, anahtar içeren her şey): klasör `chmod 700`, dosyalar `chmod 600`; kayıtta
   `gizli_icerir: "evet"`, `silme_gun` en çok 30. Anahtar klasörleri (`~/.config/openmontage`) ve `~/.hyperframes/config.json` hiç yedeğe alınmaz.
4. Yedek alan oturum, aynı adımda `yedekler.json`'a kayıt ekler (şablon 8. bölümde). Kayıtsız yedek, aylık özette "kayıtsız yedek" diye çıkar.
5. Yedek almak ve silmek kullanıcı onayıyla yapılır. `yedek-denetim.py` silmez; "silinebilir" der, kullanıcı onaylarsa oturum siler ve kaydı `durum: "silindi"` yapar.

## 2. Hangi yedek nerede
| Ne | Yedek nerede | Kim alır | Kayıt |
|---|---|---|---|
| Projedeki skill kurulumu | projede `.skill-kutuphanesi/yedek/<zaman>/` (son 10) | `skill-ekle.py` kendiliğinden | yedekler.json'a yazılmaz (otomatik, 10'a kırpılır) |
| Kütüphane içeriği | git geçmişi + GitHub (`ulukayasaban/SkillKutuphanesi`, private) | `git commit`, push yalnız kullanıcı isteyince | yok (git zaten kayıt) |
| Kütüphanenin ikinci kopyası (isteğe bağlı) | `~/Documents/Claude/yedek/kutuphane-<tarih>.bundle` | kullanıcı isteyince oturum | tür `git-paketi` |
| Program güncellemesi | `~/Documents/Claude/yedek/<program>-<tarih>/` | oturum, güncellemeden önce | tür `program` |
| Ayar dosyası değişikliği | `~/Documents/Claude/yedek/ayar-<tarih>/` | oturum, değişiklikten önce | tür `ayar-dosyasi` |
| Genel skill klasörü boşaltma | `~/Documents/Claude/yedek/genel-klasorler-<tarih>/` (rehber/12; eski taşıma: `global-skills-2026-11-08/`; geri yazılanlar: `geri-yazilan-<tarih>/`) | oturum, boşaltmadan önce | tür `genel-skill-klasoru` |

## 3. Geri yükleme (her gerçek geri yükleme için kullanıcıdan o anda onay al)

### Proje kurulumu
`python3 araclar/skill-ekle.py <proje> --yedekler` (liste), `--geri-al` (son yedek) ya da `--geri-al <yedek-adı>`. Geri almayı geri almak da mümkün.
Kütüphaneye ya da yedek klasörüne dokunulmaz.

### Kütüphane güncelleme dalı (guncelleme/AAAA-AA)
- Birleştirmeden önce reddetmek: `git switch master && git branch -D guncelleme/AAAA-AA` (push edildiyse `git push origin --delete <dal>`, kullanıcı isteyince).
- `--birlestir` kontrolleri geçmezse master kendiliğinden eski haline döner (araç yapar); yapılacak şey yoktur.
- Birleştirme geçti, sonradan hata fark edildi, push EDİLMEDİ: `git log --oneline --graph | head` ile birleştirme commit'ini bul, sonra
  `git revert -m 1 <birleştirme-commit>`. (`-m 1` şart: birleştirme commit'inin iki ebeveyni var; 1 = master tarafı.) `git revert HEAD` birleştirme
  commit'inde `-m` olmadan hata verir.
- Birleştirme push EDİLDİ: aynı `git revert -m 1 <birleştirme-commit>`; yeni commit olur. Push yalnız kullanıcı isteyince. `reset --hard` ve
  `push --force` kullanılmaz.
- Commit kayboldu gibi: `git reflog` son hareketleri listeler; bulunan commit için `git branch kurtar <commit>`. Silinen dal da böyle döner.
- takip/AAAA-AA dalı: birleştirmek `git merge --no-ff <dal>` (otomatik geri alma yok: sonra `dogrula.py` ve `kapsam-denetimi.py` çalıştır;
  sorun çıkarsa `git revert -m 1 <birleştirme-commit>`); reddetmek `git branch -D <dal>`.

### Program güncellemesi (HyperFrames, OpenMontage, ...)
Önce programın kartındaki `geri_alma` alanı (rehber/11) izlenir; kartta yoksa:
1. Programın çalışan işi durdurulur. 2. Yedek klasörü `<program>-<tarih>` açılır; içindekiler (yerel değişiklikler, veri klasörü, sabit sürüm listesi)
   neyin nereye döneceğini yedekteki not belirtir. 3. Kullanıcı onayıyla dosyalar yerine kopyalanır. 4. `python3 araclar/program-denetim.py` ile
   kurulu sürüm karttakiyle karşılaştırılır. Yedek, güncelleme doğrulanıp kullanıcı onaylayana kadar silinmez.

### Ayar dosyası
Yedek: `ayar-<tarih>/`. Önce bugünkü dosyanın `.onceki` kopyası alınır; sonra yedek yerine kopyalanır (`claude-settings.json.yedek` -> `~/.claude/settings.json`,
`zshrc.yedek` -> `~/.zshrc`, `zshenv.yedek` -> `~/.zshenv`). `settings.json` için doğrulama içeriği basmadan yapılır:
`python3 -c "import json,sys; json.load(open(sys.argv[1]))" ~/.claude/settings.json && echo geçerli`.
Uyarı: bu yedekler düz metin anahtar satırı içerebilir; geri yüklemek onu geri getirir. Yeni terminal açıp `env` değerini değil, yalnız satırın varlığını kontrol et.

### Genel skill klasörü
Yedek: `global-skills-<tarih>/` (`agents-skills/`, `claude-skills-linkler/`, `LISTE.md`, `geri-al.sh`). `geri-al.sh` kütüphane dışında ve sabit yollu;
çalıştırmadan önce oku, kullanıcıdan onay al. Bağlar elle de döner: önce `ls -la` ile hedeflerini yaz, sonra aynı bağı kur. `~/.agents/.skill-lock.json`
duruyorsa araç eski kayıtla skilli yeniden kurabilir: sıra ve kilit dosyası için rehber/12.

## 4. Saklama süresi ve hatırlatma
| Yedek türü | En çok ne kadar | Silme tetiği |
|---|---|---|
| Gizli içerikli (ayar dosyaları) | 30 gün | doğrulandıktan sonra `silme_gun` dolunca |
| Genel skill klasörü yedeği | kullanıcı "sil" diyene kadar | genel klasörler boşaltıldı ve kullanıcı onayladı (`silme_olay`) |
| Program yedeği | güncelleme doğrulanıp onaylanana kadar, en çok 90 gün | güncelleme onayı |
| Git paketi | 90 günden eskiyse yenisi alınır | kullanıcı isteyince |

Hatırlatma kuralı: kullanıcı yedekleri kendisi izlemez. Aylık özet aracı (`aylik-ozet.py`, P4 ile gelecek; o zamana kadar elle `yedek-denetim.py --ozet-json`) her ay bunu çalıştırır; "SİLİNEBİLİR", "gerekli mi?" ve "kayıtsız
yedek" satırları özetteki "karar bekleyenler"e düşer. Oturum açıldığında özet okunur ve bu satırlar kullanıcıya sorulur. Yeni zamanlanmış görev gerekmez.
Silme sırası: (1) kullanıcıya "şu yedek silinsin mi" sor, (2) onay gelirse `rm -r -- '<mutlak yol>'` (kalıcıdır; daha yumuşağı Çöp Sepeti'ne `mv`), (3) `yedekler.json`'da `durum: "silindi"` ve `silindi_tarih`, (4) commit.

## 5. Yeni bilgisayarda yalnız GitHub'dan kurma
Gerekenler: Python 3, git, `gh` (GitHub CLI). `gh auth login` komutunu kullanıcı kendisi çalıştırır (agent giriş yapmaz).
```bash
gh auth login                                                    # kullanıcı yapar
gh repo clone ulukayasaban/SkillKutuphanesi ~/Documents/SkillKutuphanesi
cd ~/Documents/SkillKutuphanesi
python3 araclar/dogrula.py && python3 araclar/kapsam-denetimi.py
python3 araclar/git-durum.py && python3 araclar/yedek-denetim.py && python3 araclar/program-denetim.py
```
Geri GELEN: git'in izlediği her şey: araçlar, rehberler, promptlar, roller, profiller, registry.json, `arsiv/` (3. taraf kopyalar; skillerin kendi
`.gitignore`'u yüzünden dışarıda kalmasın diye `git add -f arsiv` ile izleniyor, arsiv-guncelle.py yapar), kartlar (`programlar.json`, `projeler.json`),
`programlar/<ad>/` altındaki sabit sürüm kopyaları ve `KAYNAK.md` dosyaları, notlar.

Geri GELMEZ:
- GitHub'a gönderilmemiş commit'ler (`git-durum.py` "önde" sayısını söyler: yeni makineye geçmeden önce push iste).
- Commit edilmemiş değişiklikler ve izlenmeyen klasörler (ör. henüz commit edilmemiş `programlar/<ad>/`).
- Yalnız yerelde kalmış dallar, stash, reflog, `.git/config` içindeki ad ve e-posta.
- `.gitignore`'un dışarıda bıraktıkları: `.gecici/`, `.arsiv-yeni/`, `.arsiv-eski/`, `.guncelleme-kilidi`, `__pycache__/`, `.DS_Store`, ve yeni korumalar (`/.env*`, `/*.pem`, `/*.key`, `/yedek/`, `/.skill-kutuphanesi/`, `/*.bundle`, `/*.yedek`, `/notlar/son-aylik-calisma.json`, `/notlar/aylik-ozet.md`).
- `~/Documents/Claude/yedek/` içindekiler (kütüphane dışı) ve 6. bölümdeki bütün makine durumu.
- Programların kendisi (venv, npm paketi, `~/.openmontage` kurulumu): kartlardaki `kurulum` bölümüne (rehber/11) göre yeniden kurulur.

Klon doğrulaması: `dogrula.py` "git'e girmeyen arşiv dosyası" HATA'sı vermemeli; `git-durum.py` "arşiv dosyası git'e girmemiş" demezse klon eksiksizdir.
Kütüphane farklı bir yola klonlanırsa projelerin `kilit.json` yolları için `promptlar/09-proje-tasindi-veya-bozuldu.md`.

## 6. Makine durumu envanteri (kütüphane dışı; yalnız adlar, değer yazılmaz)
Geri yüklemede yeniden kurulacaklar. Her biri için gizli değer kopyalanmaz; yalnız "satır var mı" denetlenir.
| Ne | Yer | Not |
|---|---|---|
| Kabuk ortamı | `~/.zshrc`, `~/.zshenv` | `HYPERFRAMES_SKIP_SKILLS` satırı (DURUM.md); anahtar satırları düz metin |
| Claude ayarları | `~/.claude/settings.json` (env, izin kuralları, hook'lar), `~/.claude/CLAUDE.md` (genel talimat) | ses kaydı ve OpenMontage izinleri burada |
| Claude hafızası | `~/.claude/projects/*/memory/` | kalıcı kararlar `notlar/kararlar.md`'ye taşınır |
| Aylık zamanlanmış görev | `~/.claude/scheduled-tasks/skill-kutuphanesi-aylik-guncelleme/SKILL.md` | kütüphane dışı, yedeksiz; kütüphanedeki kopyası yoksa tek kopya budur |
| Diğer zamanlanmış görevler | `~/.claude/scheduled-tasks/` (colab, kopru görevleri) | kütüphaneyle ilgisiz, yine de makine durumu |
| Genel skill klasörleri | `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.agents/.skill-lock.json` | boşaltma sonrası içerik: rehber/12 |
| Programlar | `~/.openmontage` (venv ve sürüm sabitleri), `~/Movies/OpenMontage`, `~/.hyperframes`, npm genel `hyperframes` paketi | kartlardaki `kurulum` |
| Anahtar dosyaları | `~/.config/openmontage/.env` | yedeğe ALINMAZ; kullanıcı yeniden girer |
| Ses kaydı | `~/Documents/Claude/Kayitlar/` (betikler ve kayıtlar) | Terminal.app mikrofon izni (macOS) dosyayla geri gelmez, kullanıcı yeniden verir |
| Başlangıç ajanları | `~/Library/LaunchAgents/` (varsa) | adlar yedekte tutulur |
| GitHub oturumu | `gh auth` (`~/.config/gh/`) | kullanıcı `gh auth login` yapar |
| Projelerin kilitleri | her projede `.skill-kutuphanesi/kilit.json`, `.agents/skills`, `.claude/skills`, `CLAUDE.md`/`AGENTS.md` blokları | proje kendi git'inde; `proje_yolu` başka makinede geçersiz olur |
| Diğer araçların ayarları | Codex, Antigravity, Cursor, VS Code Copilot kendi ayar klasörleri | her aracın kendi klasörü |

Mac Time Machine'den geri yüklenirse: `~/Documents/Claude/yedek/` de geri gelir ve `zshrc.yedek` içindeki düz metin anahtar satırı da dönmüş olur;
`yedek-denetim.py` bunu "gizli içerikli" diye gösterir ve 30 günü dolunca silinmesini ister.

## 7. GitHub oturumu bitince
Belirti: `gh auth status` hata verir, `git push` 401/403 ya da "Authentication failed" yazar, `git-durum.py --uzak` "Uzak alınamadı" der.
1. Kullanıcı kendisi çalıştırır: `gh auth login` (GitHub.com, HTTPS, tarayıcıyla). Sonra `gh auth status`. Agent şifre ve token girmez.
2. Bu sırada çalışmaya devam eden yerel araçlar ("yalnız yerel mod"): `git-durum.py` (`--uzak` olmadan), `yedek-denetim.py`, `dogrula.py` (`--github` olmadan),
   `kapsam-denetimi.py`, `test.py`, `skill-ekle.py`. Durmuş olanlar: push, PR, `github-trend.py`, `kaynak-cek.py`, `arsiv-guncelle.py`, `github-skill-listesi.py`.
3. Giriş geri gelene kadar kütüphanenin tek kopyası bu Mac'tir. Kullanıcı isterse ikinci kopya: `git bundle create ~/Documents/Claude/yedek/kutuphane-<tarih>.bundle --all`
   (kütüphaneyi değiştirmez; kayıt: tür `git-paketi`; geri: `git clone <dosya>.bundle <klasör>`).
4. Token sızdığından şüphelenilirse kullanıcı GitHub'da tokenı iptal eder ve `gh auth login` ile yenisini alır.

## 8. Yeni yedek kaydı şablonu
`yedekler.json` → `yedekler` listesine:

```json
{ "kimlik": "<ne>-<YYYY-AA-GG>", "yol": "~/Documents/Claude/yedek/<kimlik>", "tur": "<tür>", "ne": "<ne yedeklendi ve neden>", "tarih": "<YYYY-AA-GG>",
  "geri_yukleme": "<adımlar; rehber/13 bölümü>", "gizli_icerir": "evet|hayir", "beklenen": ["<ad>"], "silme_gun": 30, "kayit": "KAYIT.json (yalnız program yedeğinde)" }
```

Tür değerleri: `ayar-dosyasi`, `genel-skill-klasoru`, `program`, `proje`, `kutuphane-dali`, `git-paketi`, `diger`.
Bu kayıt ZORUNLU adımdır: yedek alan her rehber (11, 12) kendi yedek adımından hemen sonra bu satırı ekletir. yedekler.json tek envanterdir; `KAYIT.json` yalnız programın geri alma verisidir (sürüm, commit), `kayit` alanı ona işaret eder.
Sonra: `python3 araclar/yedek-denetim.py` (sorun olmamalı), commit.
