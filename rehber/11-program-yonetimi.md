# 11 — Program yönetimi (skill olmayan yapılar)

Kütüphane yalnızca skilleri değil, kullanıcının kütüphaneye "dahil et" dediği **programları** da takip eder: kendi sürümü,
kendi kurulumu olan yapılar. Program skill değildir; `skill-ekle.py` ile projeye kurulmaz. İki tür kart var:
- **Kaynak kopyalı** (varsayılan, `kopya` alanı yok): kaynak `programlar/<ad>/kaynak/` altında durur. Örnek: `etsyotomasyon`.
- **Yerinde** (`"kopya": "yerinde"`): kaynak kopyalanmaz; program bu bilgisayarda kurulu haliyle izlenir. Örnek: `hyperframes`, `openmontage`.

## Nerede ne var
- `programlar.json` — her program için kart: repo, kütüphanedeki sürüm/commit, kurulum yolları (Windows/macOS/kaynaktan),
  veri yeri, bağlantı, ağ, güncelleme adımları, `asla` listesi.
- `programlar/<ad>/kaynak/` — programın sabit sürümdeki kaynak kopyası (değiştirilmez; yalnız kaynak kopyalı kartta).
  `programlar/<ad>/KAYNAK.md` — repo, sürüm/commit, lisans, alınmayan klasörler (yerinde kartta: neden kopya yok, nasıl yeniden edinilir) ve
  kartla tutarlı sürüm/commit metni (`python3 araclar/program-denetim.py --sema` bunu denetler).
- `kaynaklar.json` — programın reposu kayıtlıdır ve kayıtta `"program": "<ad>"` alanı bulunur (GitHub listesiyle eşleşme ve kapsam
  denetimi için). Tip repoya göre değişir: T5 ya da skill barındıran T1/T2.
- `notlar/referans/kutuphaneler.md` — programın tek satırlık özeti (yalnız T5 kayıtta).
- `notlar/program-denetimi.md` — `python3 araclar/program-denetim.py` çıktısı.
- Kartta `skill_koku` — programın kendi skill klasörlerini taşıyan klasör (programla gelen skiller projeye bağ olarak verilir; aşağıda "Programla gelen skiller ve projelerdeki bağlar").

## Yeni program eklemek (kullanıcı "dahil et" deyince)
Önce türü seç: program küçük ve repodan kurulabiliyorsa kaynak kopyalı; büyükse (venv, node_modules, kendi git klonu), kendini
güncelliyorsa ya da zaten bu bilgisayarda kurulu ve yerel değişiklik taşıyorsa yerinde. Yerinde kart için 1. ve 3. adım aynıdır,
2. adımın yerine aşağıdaki "Yerinde program" bölümündeki alanlar doldurulur.
1. Repoyu oku: SKILL.md var mı (varsa normal skill akışı, `03-yeni-skill-ekleme.md`), lisans, son release, bağımlılıklar,
   ağ trafiği, kendini güncelleyip güncellemediği, anahtar istiyor mu.
2. Son release etiketinin kaynağını ayrı bir geçici klasöre indir (`gh api repos/<repo>/tarball/<etiket>`), çalıştırma;
   demo/medya (`docs/`) ve CI (`.github/`) hariç `programlar/<ad>/kaynak/`'a kopyala; `KAYNAK.md` yaz.
3. `programlar.json`'a kart, `kaynaklar.json`'a kayıt (`program` alanıyla), T5 ise `kutuphaneler.md`'ye satır. Repo skill barındırıp
   `kaynaklar.json`'da zaten T1/T2 kayıtlıysa yeni kayıt açma, mevcut kayda `program` alanını ekle; T1/T2 kayıtta `kutuphaneler.md` satırı aranmaz.
4. `python3 araclar/listeye-ekle.py owner/ad` (GitHub listesi), sonra her zamanki kontroller ve commit.

## Yerinde program (kopyasız)
**Ne zaman:** program çok büyük ya da kendi sürümünü kendi yönetiyor (npm genel paketi, git klonu + venv). Kopya hemen eskirdi
ya da yerel yamalarla karışırdı. Kütüphane yalnızca *neyin kurulu olduğunu, hangi sürümün onaylı olduğunu ve nasıl güncelleneceğini* tutar.

**Kart ne taşır** (`programlar.json`; şema v2 alanları aşağıdaki "Kart şeması (v2)" tablosundadır):
- `"kopya": "yerinde"`, `repo`; `kaynak_kopyasi` OLMAZ.
- `yerinde`: `tur` = `npm-global` (`yol`, `paket`) ya da `git-checkout` (`yol`, `dal`). `yol` içinde `~` olabilir.
- `kutuphane_surumu` (npm) ya da `kutuphane_commit` (git, tam sha): kütüphane oturumunun en son kaydettiği ve onayladığı kurulu sürüm.
- İsteğe bağlı: `venv` (yol içinde göreli) ve `sabit_surumler` (venv'de yükseltilmemesi gereken paketler: tam sürüm ya da `<5` gibi kısıt).
- Ayrıca: ne yapar, lisans, ücret sınıfı, veri yeri, kendini güncelleme ve skill yazma davranışı, güncelleme adımları, `asla` listesi.
- `programlar/<ad>/KAYNAK.md` ve `kaynaklar.json`'da repo kaydında `"program": "<ad>"` gerekir (`araclar/test.py` bunu denetler).
  Test programın bu bilgisayarda kurulu olmasını istemez.

**`program-denetim.py` ne bildirir:** üç değer: *karttaki*, *kurulu* (şimdi; `package.json`, salt okuma git, dist-info dosyalarından;
program ya da venv çalıştırılmaz) ve *son* (npm kayıt defteri ya da GitHub API'si; `git fetch` yapılmaz). Durum sözcükleri:

| Durum | Anlamı | Ne yapılır |
|---|---|---|
| `güncel` | Kurulu = karttaki, son sürümden geride değil | Bir şey yapılmaz |
| `YENİ SÜRÜM VAR` | Kurulu = karttaki, ama daha yeni sürüm var | Kullanıcıya sürüm farkı ve özet sun; onay gelirse güncelleme adımlarını uygula |
| `KART ESKİ` | Kurulu sürüm karttan farklı: onaylı kayıt olmadan değişmiş (programın kendi güncellemesi olabilir) | Sebebi bul, kullanıcıya söyle; onaylıysa kartı ve `KAYNAK.md`'yi kurulu sürüme çek, değilse nedenini araştır |
| `bu bilgisayarda kurulu değil` | Yol yok; kütüphane programın kurulu olmadığı bir makinede de klonlanır | Hata değil; bir şey yapılmaz |
| `öğrenilemedi` | Ağ ya da ayrıştırma hatası | Sonra yeniden dene; sürüm kararı verme |

Git kartında rapor "N geride" ve yerel değişiklik sayısını (değişen izlenen dosya, izlenmeyen yol) da yazar. `sabit_surumler` varsa
kaç sabitin tuttuğu ve tutmayanlar listelenir. Rapor `notlar/program-denetimi.md` içindeki "Yerinde izlenen programlar" tablosundadır.

**Güncelleme her zaman: önce yedek, sonra ayrı onay.** Her güncelleme için kullanıcıdan ayrıca onay alınır (önceki onay sonrakini
kapsamaz). Önce yedek (yerel değişiklikler, veri klasörü, sabit sürüm listesi), onaydan sonra yalnızca kütüphane oturumu günceller,
sonra yeniden denetim ve kart güncellemesi. Yedek yalnız `~/Documents/Claude/yedek/<program>-<YYYY-AA-GG>/` klasörüne alınır (içinde `KAYIT.json` bulunur: aşağıda "Yedek kaydı"); kütüphane
klasörüne ve git'e asla konmaz. `~/.hyperframes` yedeğinde `config.json` alınmaz, `~/.config/openmontage` anahtar klasörü hiç
kopyalanmaz. Yedek, güncelleme doğrulanıp onaylanana kadar saklanır; silmek için kullanıcıya sorulur. Programın kendi kendine güncellemesi ya da skill yazması kartta açıkça yazılıdır;
bunu durduran anahtarlar (ortam değişkenleri) kartta listelenir. Ortam değişkenini ajan kendiliğinden tanımlamaz: gerekeni söyler; kullanıcı ya kendisi tanımlar ya da ajana açıkça "tanımla" der (kabuk dosyalarının yedeği önce alınır).

## Takip ve güncelleme
- `python3 araclar/program-denetim.py` durumu raporlar (salt okuma, çıkış 0). Kaynak kopyalı kartta kütüphanedeki sürümü GitHub'daki
  son sürümle karşılaştırır; yerinde kartta karttaki, kurulu ve son değeri karşılaştırır (yukarıdaki bölüm).
- Yeni sürüm varsa, yalnız kaynak kopyalı kart için: CHANGELOG özeti → kullanıcı onayı → kaynak kopyasını yeni etiketten yenile,
  `KAYNAK.md` ve kartı güncelle, commit → programı kullanan makinelerde kullanıcıyla birlikte yenile.
- Yeni sürüm varsa, yerinde kart için: kopya yenilenmez. Güncelleme adımları bu belgede "Taze ajan: istek → adımlar" başlığındadır;
  güncellemeden sonra yeniden denetim yapılır, `kutuphane_surumu` ya da `kutuphane_commit` ile `KAYNAK.md` güncellenir, commit atılır.

## Programla gelen skiller ve projelerdeki bağlar
Kural (K-28): programın kendi skilleri (OpenMontage `.agents/skills/*`, HyperFrames `dist/skills/*`) projeye KOPYALANMAZ ve her zaman kurulu programın sürümüdür.
- Kart alanı `skill_koku`: skill klasörlerinin üst klasörü (`~/` ya da mutlak; boş metin = programın skili yok). Gerçek klasör `<skill_koku>/<ad>/SKILL.md` kaynaktır; kartın serbest `skilleri` listesi esas alınmaz.
- Proje bağı: `python3 araclar/skill-ekle.py <proje> --program-skill PROGRAM:AD --kuru`, onayla `--evet` (rehber/01). Kayıt projenin kilidinde (`dis_skiller`); kütüphane hangi projenin neye bağlı olduğunu `python3 araclar/proje-kullanimi.py --program <ad>` ile gösterir.
- Güncellemeden önce: `program-denetim.py --oncesi <ad>` 'bağlar' satırları: `TAMAM bağlar` (bağlar çözülüyor), `UYARI bağ kırılacak: <proje>: <skill>` (git klonunda hedef commit yerel depodaysa o commit'te skill klasörü yok), `BİLGİ hedef commit yerel depoda yok` ya da `paket indirilmeden ... bilinemez`. Ağ ve `git fetch` yoktur; kırılacak bağ kullanıcıya söylenir.
- Güncellemeden sonra: aynı komut ya da `program-denetim.py` kırık bağı gösterir. `GÜNCELLENECEK BİR ŞEY YOK` görünümünde ve normal raporda kırık bağ HATA'dır; program kurulu değilse ya da güncelleme bekleniyorsa UYARI'dır. 'bağlar' satırı hiçbir zaman `HAZIR DEĞİL` sebebi olmaz (program yeniden kurulacaksa bağlar zaten kırık görünür).
- Kırık bağ: program kuruluysa projede `skill-ekle.py <proje> --yenile`; program o skili bıraktıysa `--kaldir <ad>`; hangisinin yapılacağı kullanıcıya sorulur.
- Programı çıkarmadan önce tüm bağları `proje-kullanimi.py --program <ad>` ile listele: program kalkınca hepsi kırılır.
- Bağın Codex/Antigravity/Cursor tarafından keşfedildiği gerçek araçla sınanmadı (Claude Code'da çalışır); program kurulu değilse bağ asılı kalır.

## Kurallar
- Program kopyası proje deposuna konmaz; projeye yalnızca kullanım notu (hangi ekran/komut kullanılır, hangisi kullanılmaz) yazılır. Programın skilleri de projeye kopyalanmaz, bağ verilir.
- Yerinde programlarda yalnız kütüphane oturumu güncelleme yapar; `npx`, `pip install -U`, `git pull`, `make setup` gibi komutlar onaysız
  çalıştırılmaz. Bu, `CLAUDE.md` kural 1'in (genel klasörlere yazma yok) kartlı programlar için tek istisnasıdır: yalnız kullanıcının o
  güncelleme için verdiği ayrı onayla ve kartın adımlarıyla. Giriş yolları ve genel klasörleri boşaltma işlemleri `rehber/12`'dedir.
- Anahtar, şifre, oturum dosyalarını agent girmez, açmaz, yazdırmaz; hesap bağlama adımlarını kullanıcı yapar.
- Kartlarda proje adı ve "şu projeye uyar" yazılmaz (kütüphane kuralı 6); projeye uygunluk kurulum sırasında incelenir.

## Kart şeması (v2)
Kartlar iki katmanlıdır. `python3 araclar/program-denetim.py --sema` kartları denetler; `--sema --siki` HATA varsa çıkış 1 verir (yalnız
güncelleme adımlarında kullanılır). Kütüphane kapıları (`dogrula.py`, `test.py`) kart bulgularını yalnız UYARI sayar: unutulmuş bir kart alanı
aylık birleştirmeyi durdurmaz. Yeni program için boş iskelet: `python3 araclar/program-denetim.py --iskelet kaynak|npm-global|git-checkout`
(`<DOLDUR>` yazan her yeri doldur, sonra `--sema` temiz olsun).

**Çekirdek alanlar** (eksikse HATA): `giris_yolu`, `kurulum`, `geri_alma`, `cikarma`, `yedek` (yerinde kartta zorunlu, kaynak kartta isteğe bağlı), `ortam_anahtarlari` (boş liste olabilir).
**İsteğe bağlı alanlar** (yokluğu bildirilmez; var ama geçersizse UYARI): `disariya_yazar`, `tedarik_dogrulama`, `kirici_surum`, `gizli_dosyalar`, `yerel_yamalar`, `skill_koku`.

| Alan | Şekil | Ne için |
|---|---|---|
| `giris_yolu` | `kural`, `kilavuz`, `calistirma`, `karar`, `hepsi` ya da `araclar` (5 araç anahtarı) | Genel klasörler boşaltılınca bir ajan programa nasıl ulaşır |
| `kurulum` | `adimlar`, `dogrulama` (+ `on_kosullar`, `yapma`; etsyotomasyon'da eski `windows/macos/kaynaktan` anahtarları durur) | Yeni makineye kurulum |
| `geri_alma` | `ne_zaman`, `adimlar`, `dogrulama`, `sinir` | Eski sürüme dönüş |
| `cikarma` | `makineden`, `dokunulmaz` | Bilgisayardan kaldırma |
| `yedek` | `kok`, `tazelik_gun` (1-30), `zorunlu` (`KAYIT.json` şart), `yasak_adlar` | Güncelleme öncesi yedek kuralı |
| `ortam_anahtarlari` | liste: `ad`, `beklenen`, `gerekli`, `nerede`, `not` | Programın kendi kendine yazmasını durduran anahtarlar |
| `gizli_dosyalar` | yol listesi | Anahtar/kimlik dosyaları: yalnız var/yok bakılır, açılmaz |
| `disariya_yazar` | liste: `yol`, `tur`, `ne`, `yedeklenir`, `dogrulandi` | Programın kendi klasörü dışında yazdığı yerler |
| `yerel_yamalar` | `kural`, `bilinen` (yol/tur/amac/yedek/yeniden_uygula), `yedekleme`, `rehber` | Git klonundaki yerel değişikliklerin kaydı |
| `kirici_surum` | `kural`, `surum_hatti` ya da `esik_commit`, `izle_dosyalar`, `deneme_klasoru`, `deneme_disk_gb` | Kırıcı sürüm adayını bulma kuralı |
| `tedarik_dogrulama` | `yayinci`, `ozet` (tür/değer), `kural` | Üçüncü taraf ikili ya da paket için doğrulama kaydı |
| `skill_koku` | metin: `~/` ya da mutlak yol; boş = programın skili yok | Programın skill klasörlerinin üst klasörü (projelere bağ kaynağı). Mutlak/`~/` değilse HATA; kurulu programda klasör yoksa UYARI |

Kartlara gizli değer, parola, anahtar ve proje adı yazılmaz; `--sema` bunları da denetler. Uzun anlatım kartta değil bu belgededir.

## Boşaltma sonrası program erişimi (giriş yolları)
Genel skill klasörleri (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`) boşaltılınca bir ajan programlara bu klasörlerden ulaşamaz.
Her kartın `giris_yolu` alanı, hangi aracın programa nasıl ulaşacağını yazar. Beş durum sözcüğü:
`yerinde` (yol bugün var ve boşaltmadan sonra da kalır), `program-klasoru` (programın kendi kılavuz dosyalarıyla; oturum program klasöründe açılır
ya da istem kılavuzu okutur), `proje-skili` (projeye `skill-ekle.py` ile kurulan skill ya da komut satırı dosyası), `karar-bekliyor` (kullanıcı kararı
bekliyor), `yok` (desteklenmiyor).

| Program | Araç | Durum | Yol / nasıl |
|---|---|---|---|
| hyperframes | hepsi | proje-skili | `/usr/local/bin/hyperframes`; skiller projeye `skill-ekle.py --skill <kimlik>` ile kurulur |
| openmontage | claude-code | karar-bekliyor | bugün `~/.claude/commands/openmontage.md` komutu + `~/.claude/CLAUDE.md` satırı + `~/.claude/skills/openmontage` |
| openmontage | codex, antigravity, cursor, vscode-copilot | program-klasoru | oturumu `~/.openmontage` klasöründe aç (`AGENTS.md`, `CODEX.md` orada) ya da istemde "önce `~/.openmontage/AGENT_GUIDE.md` oku" yaz |
| etsyotomasyon | hepsi | yok | araç-özel giriş yok; komut satırı ve localhost paneli |

Açık kullanıcı kararı: boşaltmadan sonra OpenMontage'in Claude Code girişinin (komut + giriş skili) yeri. Karar gelince kartta `giris_yolu.araclar.claude-code`
(`durum`, `yol`, `nasil`) kullanıcı onayıyla güncellenir. Her boşaltma adımından sonra `python3 araclar/program-denetim.py --oncesi hyperframes` ve
`--oncesi openmontage` çalıştırılır: `giriş yolu` ve `ortam` satırları TAMAM/BİLGİ kalmalıdır; yol değişirse kart güncellenir (kullanıcı onayıyla).

## Yeni makineye kurulum
Kartın `kurulum` alanı yazar (`on_kosullar`, `adimlar`, `dogrulama`, `yapma`). Sıra hep aynı: önce ortam anahtarları (örnek `HYPERFRAMES_SKIP_SKILLS=1`; kullanıcı tanımlar
ya da ajana açıkça yaptırır), sonra kurulum, sonra `python3 araclar/program-denetim.py` ve `--oncesi <ad>` ile denetim. Kurulumu kütüphane oturumu, kullanıcının
ayrı onayıyla yapar; Etsy/API anahtarı ve hesap bağlama adımlarını kullanıcı yapar. Sürüm hep karttaki sürümdür (`latest` yazılmaz).

## Yedek kaydı (KAYIT.json)
Her güncellemeden önce yedek klasörü açılır: `~/Documents/Claude/yedek/<program>-<YYYY-AA-GG>[-N]/` (aynı gün ikinci yedek `-2`). Kütüphane klasörüne ve git'e asla.
Klasöre `.env`, `token.json`, `credentials.json`, `auth.json` ve kartın `yedek.yasak_adlar` listesindeki adlar (HyperFrames için `config.json`) konmaz; ön kontrol bulursa durur.
`KAYIT.json` biçimi (gizli değer yok):
```
{"program": "openmontage", "tarih": "2026-11-12",
 "onceki": {"surum": "", "commit": "c8066452325cb57c8fc1ba8c2a71b6e8842e6b65"},
 "hedef": "<yeni sürüm ya da sha, bilinmiyorsa boş>", "icerik": ["yerel-yamalar.patch", "izlenmeyen-yollar.txt", "pip-freeze.txt", "bag-listesi.txt"], "not": ""}
```
npm kartında `onceki.surum` dolu, git kartında `onceki.commit` dolu; öteki boş. `tarih` klasör tarihiyle aynı olmalıdır. Yedek kurulu sürümün yedeği olmalıdır
(ön kontrol `onceki` değerini kurulu sürümle karşılaştırır).

**HyperFrames yedeği** (kartın `yedek.zorunlu`: `KAYIT.json`, `hyperframes-veri`, `paket`):
```
YEDEK=~/Documents/Claude/yedek/hyperframes-$(date +%Y-%m-%d); mkdir -p "$YEDEK/hyperframes-veri"
rsync -a --exclude config.json ~/.hyperframes/ "$YEDEK/hyperframes-veri/"
cp -R /usr/local/lib/node_modules/hyperframes "$YEDEK/paket"
python3 - "$YEDEK" <<'PY'
import datetime, json, pathlib, sys
y = pathlib.Path(sys.argv[1])
onceki = json.load(open("/usr/local/lib/node_modules/hyperframes/package.json"))["version"]
json.dump({"program": "hyperframes", "tarih": datetime.date.today().isoformat(), "onceki": {"surum": onceki, "commit": ""},
           "hedef": "<hedef sürüm>", "icerik": ["hyperframes-veri", "paket"], "not": ""},
          open(y / "KAYIT.json", "w"), ensure_ascii=False, indent=2)
PY
```
**OpenMontage yedeği** (`yerel-yamalar.patch`, `izlenmeyen-yollar.txt`, `pip-freeze.txt`, `bag-listesi.txt`, `KAYIT.json`; `~/.config/openmontage` anahtar klasörüne dokunulmaz):
```
YEDEK=~/Documents/Claude/yedek/openmontage-$(date +%Y-%m-%d); mkdir -p "$YEDEK/izlenmeyen"
git -C ~/.openmontage diff --binary > "$YEDEK/yerel-yamalar.patch"
git -C ~/.openmontage ls-files --others --exclude-standard --directory -z | (cd ~/.openmontage && xargs -0 du -sk) > "$YEDEK/izlenmeyen-yollar.txt"
# kartta yedek: "kopya" olan izlenmeyen yolları kopyala (örnek; liste karttaki yerel_yamalar.bilinen'den alınır)
(cd ~/.openmontage && rsync -aR remotion-composer/remotion.config.ts remotion-composer/src/Explainer.tsx.bak-2026-09-20 remotion-composer/src/Explainer.tsx.bak-2026-09-30 .agents/skills/gsap-plugins/SKILL.md.2026-10-15-oncesi "$YEDEK/izlenmeyen/")
python3 araclar/program-denetim.py --pin-listesi openmontage > "$YEDEK/pip-freeze.txt"
for l in ~/.claude/skills/*; do [ -L "$l" ] && readlink "$l" | grep -q '/\.openmontage/' && echo "$(basename "$l") -> $(readlink "$l")"; done > "$YEDEK/bag-listesi.txt"
python3 - "$YEDEK" <<'PY'
import datetime, json, pathlib, subprocess, sys
y = pathlib.Path(sys.argv[1])
sha = subprocess.check_output(["git", "-C", str(pathlib.Path.home() / ".openmontage"), "rev-parse", "HEAD"], text=True).strip()
json.dump({"program": "openmontage", "tarih": datetime.date.today().isoformat(), "onceki": {"surum": "", "commit": sha},
           "hedef": "<hedef sha>", "icerik": ["yerel-yamalar.patch", "izlenmeyen-yollar.txt", "pip-freeze.txt", "bag-listesi.txt"], "not": ""},
          open(y / "KAYIT.json", "w"), ensure_ascii=False, indent=2)
PY
```
**etsyotomasyon**: yalnız `KAYIT.json` (önceki sürüm); `~/.etsyotomasyon` anahtar ve oturum klasörü kopyalanmaz. Yedek klasörü, güncelleme doğrulanıp kullanıcı onaylayana kadar
saklanır; silmeden önce kullanıcıya sorulur.

## Güncellemeden önce: ön kontrol (--oncesi)
`python3 araclar/program-denetim.py --oncesi <ad> [--hedef <sürüm ya da sha>] [--cevrimdisi] [--tedarik]` salt okunur: hiçbir şey yazmaz, kurmaz, indirmez, `git fetch` yapmaz.
Her satır `SEVİYE  kontrol  metin` biçimindedir (TAMAM, BİLGİ, UYARI, HATA, ATLANDI). Önce dört durum satırı sonucu belirler:
`şema` (kart çekirdek alanları geçerli mi), `kurulu` (program bu bilgisayarda var mı), `kart` (kurulu sürüm karttakiyle aynı mı), `son` (daha yeni sürüm var mı).
Sonra sekiz ana kontrol (ve bağ varsa dokuzuncu, `bağlar`):
1. `yedek`: bugünden en çok `tazelik_gun` gün eski yedek klasörü var mı, `KAYIT.json` geçerli ve kurulu sürümün yedeği mi, `zorunlu` dosyalar var mı, içinde yasak adlı (`.env`, `config.json`...) dosya yok mu.
2. `sabit sürümler`: venv'deki paketler karttaki sabit sürümlerle aynı mı (fark varsa düzeltmeden devam edilmez).
3. `ortam`: gerekli ortam anahtarı kaç yerde tanımlı (değer asla yazdırılmaz).
4. `yerel değişiklik` (git klonu): her yerel değişiklik kartta `yerel_yamalar.bilinen` listesinde mi; `kayıtsız yerel değişiklik` varsa durulur.
5. `repo`: repo GitHub'da var mı, taşınmış mı, origin adresi eski mi.
6. `giriş yolu`: kartın giriş yolu dosyaları duruyor mu.
7. `gizli`: anahtar/kimlik dosyası var mı (yalnız var/yok; açılmaz).
8. `kırıcı`: kırıcı sürüm adayı mı, yeni commit'ler yamalı dosyaya dokunuyor mu, deneme için disk yeterli mi.
9. `bağlar`: bu programın skillerine bağlı proje varsa (kilitlerde `dis_skiller`) hedefler şimdi var mı ve git klonunda hedef sürümde de olacak mı (`bağ kırılacak`). Kırık bağ yalnız güncelleme dışı görünümde HATA'dır, `HAZIR DEĞİL` sebebi olmaz. Hiç bağ yoksa satır görünmez.
Sonuç sözcüğü: `HAZIR`, `HAZIR DEĞİL (n engel)`, `GÜNCELLENECEK BİR ŞEY YOK`, `KURULU DEĞİL`. UYARI engel değildir ama okunur. `--cevrimdisi` ağa hiç gitmez (ağ isteyen satırlar `atlandı: çevrimdışı`).
Çıkış kodu: 0 araç çalıştı (ne bulursa bulsun); `--siki` ile `HAZIR DEĞİL` ise 1; program adı yoksa 2. `--ozet-json` aynı sonucu tek JSON nesnesi olarak verir ve dosya yazmaz.
**"HAZIR" demeden güncelleme başlamaz.** `HAZIR` yine de kullanıcı onayı yerine geçmez.

## Kırıcı sürüm (önce ayrı klasörde dene)
Kartın `kirici_surum` alanı kuralı yazar: npm kartında `surum_hatti` (0.x sürümde `minor` değişimi kırıcıdır), git kartında `esik_commit` (kurulu commit'ten bu kadar ileride)
ve `izle_dosyalar` (yeni commit'ler bunlardan birini değiştirirse) ve yamalı dosyaya dokunan commit'ler. Aday çıkarsa güncelleme önce `deneme_klasoru` altında
(`~/Documents/Claude/deneme/<program>-<hedef>`; kütüphane ve git dışında) denenir; `/usr/local`, `~/.openmontage` ve kütüphaneye dokunulmaz. Deneme `gecme_olcutu`'nu geçmeden
gerçek güncelleme için onay istenmez. Deneme klasörü silinmez, silmek için kullanıcıya sorulur.

**HyperFrames** (deneme ~1 GB):
1. `mkdir -p ~/Documents/Claude/deneme/hyperframes-<hedef>`.
2. Ortamda `HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_AUTO_INSTALL=1 HYPERFRAMES_NO_UPDATE_CHECK=1` tanımlıyken: `npm install --prefix <deneme klasörü> hyperframes@<hedef>` (genel kuruluma dokunmaz).
3. `<deneme klasörü>/node_modules/.bin/hyperframes --version` hedef sürümü yazmalı.
4. Kullanıcının seçtiği bir kompozisyonda lint, sonra çıktısı deneme klasörüne giden bir render. `init`, `skills`, `update` ÇALIŞTIRILMAZ (skill yazar).
5. Sonuç raporlanır.
Geçme ölçütü: `--version` hedefi yazdı; lint hatasız; render çıktısı açılıyor; genel skill klasörlerinde yeni girdi yok.

**OpenMontage** (deneme ~8 GB boş disk gerekir):
1. Disk: en az 8 GB boş (ön kontrol söyler). `mkdir -p ~/Documents/Claude/deneme`.
2. `git clone --local ~/.openmontage ~/Documents/Claude/deneme/openmontage-<hedef-ilk-8-hane>` (yerel klon, ağ yok; çalışma ağacı yamaları taşınmaz).
3. Yalnız deneme klonunda: `git remote set-url origin https://github.com/OpenMontageInc/OpenMontage.git`, `git fetch origin main`, `git checkout --detach <hedef>`.
4. Deneme klonunda yeni venv: `uv venv --python 3.10 .venv`; `requirements.txt` kurulur, sonra karttaki `sabit_surumler` yeniden uygulanır (`pip install paket==sürüm`). `make setup` ÇALIŞTIRILMAZ; `~/.openmontage/.venv`'e dokunulmaz.
5. Anahtar dosyası deneme klonuna kopyalanmaz ve bağlanmaz; ücretsiz yerel araçlarla preflight çalıştırılır (openmontage skilindeki "Command pattern" bölümü).
6. Karttaki her `yeniden_uygula: true` yama yolu için yeni sürümdeki dosya kullanıcıya gösterilir: yama hâlâ gerekli mi, çakışıyor mu.
7. Sonuç raporlanır.
Geçme ölçütü: preflight hatasız; sabit paketler karşılaştırmada aynı; her yama dosyası için karar verildi (uygula / yeni sürümde gereksiz / çakışıyor).

**etsyotomasyon** (deneme ~1 GB):
1. Yeni kaynağı ayrı klasöre aç (`~/Documents/Claude/deneme/etsyotomasyon-<hedef>`).
2. Ayrı venv: `python3 -m venv <klasör>/.venv && <klasör>/.venv/bin/pip install <klasör>/kaynak`.
3. `etsyotomasyon --help` çalıştır; anahtar dosyası bağlanmaz.
Geçme ölçütü: kurulum hatasız; `--help` çalışıyor.

## Yerel yamalar (git klonu)
Klonda repoda olmayan değişiklikler (OpenMontage'de dokuz izlenen dosya, izlenmeyen yollar ve venv yaması) kartın `yerel_yamalar.bilinen` listesinde kayıtlıdır: yalnız yol ve amaç,
kod ya da gizli değer değil. Kartta kayıtlı olmayan bir değişiklik `--oncesi` çıktısında `kayıtsız yerel değişiklik` olarak görünür ve güncelleme durur.
Yama içeriği kütüphaneye değil, yedek klasörüne (`yerel-yamalar.patch`, `izlenmeyen-yollar.txt`) alınır. Amacı henüz yazılmamış yamalar `ölçülmedi` ya da "kullanıcıya sorulur" olarak durur; tahmin yazılmaz.
Güncelleme sırası:
1. Güncellemeden önce: yedek klasörüne `git diff --binary > yerel-yamalar.patch`, `izlenmeyen-yollar.txt` ve "kopya" olan izlenmeyen yollar alınır; `KAYIT.json` yazılır.
2. Güncelleme `git pull --ff-only` ile yapılır (merge ve rebase yok). Yerel değişikliklerle çakışan dosya varsa git hiçbir şeyi değiştirmeden durur; o zaman çakışan dosyaların yeni sürümdeki farkı kullanıcıya gösterilir.
3. Çakışan dosya için kullanıcı onaylarsa: yalnız o dosya `git checkout -- <yol>` ile eski haline getirilir (yaması yedekte), pull yapılır, sonra `git apply --3way --include=<yol> yerel-yamalar.patch` ile geri uygulanır. Çakışma işareti kalırsa durulur, kullanıcıya sorulur.
4. Çakışmayan yamalar pull sonrası yerinde kalır. Her `yeniden_uygula: true` yolun hâlâ değişik olduğu `program-denetim.py --oncesi openmontage` çıktısındaki "kayıtlı ama değişmemiş" satırından anlaşılır; yama upstream'e girdiyse ya da kaybolduysa kullanıcıya söylenir.
5. Venv yaması (`tur: venv`) dosya okunarak denetlenir; `pip install` ile venv'e dokunulmaz.
Yeni yama eklemek: kullanıcıyla amacı yazılır, karta `bilinen` satırı olarak eklenir.

## Geri alma
Önceki sürüm, güncellemeden önce yazılan `KAYIT.json` içindeki `onceki` alanındadır; yedeksiz güncelleme yapılmadığı için geri alma her zaman mümkündür. Geri alma için de kullanıcıdan AYRI onay alınır.
Adımlar kartın `geri_alma` alanındadır; özet:
- **HyperFrames**: `HYPERFRAMES_SKIP_SKILLS=1` tanımlıyken `npm install -g hyperframes@<onceki.surum>` (tek sürüm). Registry sürümü kaldırdıysa yedekteki `paket` klasörü onayla yerine konur; veri bozulduysa `hyperframes-veri` geri kopyalanır. Sonra kart, `KAYNAK.md` ve `tedarik_dogrulama.ozet` önceki değere çevrilir.
- **OpenMontage**: `git -C ~/.openmontage switch --detach <onceki.commit>`. `git reset --hard`, `git checkout -B` ve `git clean` KULLANILMAZ (yerel yamaları ezer). Çakışan dosya olursa yalnız o dosyada `git checkout -- <yol>`, `switch`, sonra `git apply --3way --include=<yol> yerel-yamalar.patch`. Venv bozulduysa yedekteki `pip-freeze.txt` ile `pip install --no-deps -r` (onayla). Ayrık HEAD ön kontrolde UYARI verir; `git switch main` yalnız kullanıcı isterse.
- **etsyotomasyon**: kaynak kopyası kütüphane git geçmişinden geri alınır (`git checkout <önceki commit> -- programlar/etsyotomasyon`, onayla); programı kullanan makinede önceki release ya da kaynaktan kurulum yeniden yapılır. `~/.etsyotomasyon` hiç kopyalanmaz ve geri alınmaz.
Geri almadan sonra kart, `KAYNAK.md` ve (varsa) `tedarik_dogrulama.ozet` önceki değere çevrilir, `--sema --siki` ve `program-denetim.py` ile doğrulanır, commit atılır.

## Programı çıkarma
İki ayrı iş vardır; her biri ayrı onay ister.
**(A) Kütüphaneden çıkarma**
1. `python3 araclar/proje-kullanimi.py --program <ad>`: programın skillerine bağlı projeler (hedef var mı); karttaki `skilleri` kimlikleri için ayrıca `--skill <kimlik>`. Kullanıcıya söylenir; program kalkınca tüm bağlar kırılır.
2. Kullanıcı onayı (neyin silineceği adı ve "geri dönüşü git geçmişindedir" notuyla).
3. Kart `programlar.json`'dan çıkarılır.
4. `programlar/<ad>/` silinir. `kaynak/` kopyası kalıcı bir silmedir (git geçmişi saklar); ne silineceği söylenir ve sorulur.
5. `kaynaklar.json` kaydındaki `"program": "<ad>"` alanı kaldırılır (kayıt yalnız program için açıldıysa kaydı `rehber/03` kaynak çıkarma yoluyla çıkar); `notlar/referans/kutuphaneler.md` satırı kaldırılır.
6. GitHub listesinden çıkarmak kullanıcının kendi işidir.
7. `python3 araclar/kapsam-denetimi.py` 0 sorun, `python3 araclar/dogrula.py` 0 hata, `python3 araclar/program-denetim.py --sema --siki`, sonra commit (commit geri almadır: `git revert`).
**(B) Bilgisayardan kaldırma**: kartın `cikarma.makineden` adımları; önce yedek, anahtar ve veri klasörlerine (`cikarma.dokunulmaz`) hiç dokunulmaz, genel klasör işleri `rehber/12`'dedir.

## Taze ajan: istek → adımlar
Kütüphane oturumunun önceki konuşma belleği yoktur: `CLAUDE.md`/`AGENTS.md`'yi, bu belgeyi ve ilgili kartı okuyarak başlar. Hazır istem: `promptlar/13-program-kur-guncelle.md`.

**"HyperFrames'i güncelle"** (npm-global)
0. `cd ~/Documents/SkillKutuphanesi`; `CLAUDE.md`/`AGENTS.md` ve bu başlığı oku; `git status` (kirli ağaç varsa kullanıcıya söyle, kart değişikliğini başka işle karıştırma).
1. `python3 araclar/program-denetim.py --sema --siki` → 0 hata, değilse dur.
2. `python3 araclar/program-denetim.py` → hyperframes satırı. `KART ESKİ` ise dur, sebebi bul (program kendini güncellemiş olabilir), kullanıcıya söyle.
3. `python3 araclar/program-denetim.py --oncesi hyperframes` → engelleri oku. `KIRICI ADAYI` varsa yukarıdaki "Kırıcı sürüm" deneme adımlarını ayrı klasörde uygula, sonucu raporla. `python3 araclar/proje-kullanimi.py --program hyperframes` ve 'bağlar' satırları kullanıcıya söylenir.
4. Kullanıcıya sun: kurulu → hedef sürüm, release notu özeti, kırıcı adayı mı, yedek yeri. Sor: "HyperFrames'i <kurulu> sürümünden <hedef> sürümüne güncelleyeyim mi? Önce yedek alırım. Bu onay yalnız bu güncelleme için geçerli."
5. Onaydan sonra yedeği al (yukarıdaki "Yedek kaydı" HyperFrames komutları).
6. `--oncesi hyperframes` tekrar → `SONUÇ: HAZIR`.
7. `HYPERFRAMES_SKIP_SKILLS=1 npm install -g hyperframes@<hedef>` (izin hatası olursa dur, kullanıcıya sor).
8. `python3 araclar/program-denetim.py` → kurulu = hedef. Genel klasörlerde yeni girdi var mı bak (genel-bekci varsa çalıştır). `program-denetim.py --oncesi hyperframes --cevrimdisi` 'bağlar' satırlarında HATA olmamalı; olursa projeye göre `--yenile`/`--kaldir` için kullanıcıya sor.
9. Kartı güncelle: `kutuphane_surumu`, `programlar/hyperframes/KAYNAK.md`, `tedarik_dogrulama.ozet` (`--oncesi hyperframes --tedarik` registry değerini karşılaştırır); `--sema --siki`, `kapsam-denetimi.py`, `dogrula.py`; commit.
10. Özetle ve hatırlat: "Yedek `~/Documents/Claude/yedek/hyperframes-<tarih>/` klasöründe duruyor; güncellemeyi doğruladığında silmek istersen söyle."

**"OpenMontage'i güncelle"** (git-checkout)
0-2. Yukarıdaki gibi, `openmontage` için.
3. `python3 araclar/program-denetim.py --oncesi openmontage` (+ `proje-kullanimi.py --program openmontage` ve 'bağlar'/'bağ kırılacak' satırları kullanıcıya söylenir): engeller yedek, `kayıtsız yerel değişiklik` (kullanıcıyla `yerel_yamalar.bilinen`'e yaz), sabit sürüm farkı ya da `KIRICI ADAYI` olabilir (çok commit gerideyse deneme klasörü şart).
4. Kırıcı adayıysa "Kırıcı sürüm" deneme adımları; geçme ölçütü geçmeden devam yok.
5. Kullanıcıya sun: kurulu → hedef commit (tam sha), kaç geride, `requirements.txt` farkı (GitHub compare çıktısı; `git fetch` için ayrı onay), yamalı dosyalarla çakışma listesi. Sor: "OpenMontage'i <kurulu 8 hane> -> <hedef 8 hane> güncelleyeyim mi? Önce yerel yamaları ve sabit paket listesini yedeklerim; paket sürümlerini yükseltmem. Bu onay yalnız bu güncelleme için geçerli."
6. Yedek: "Yedek kaydı" OpenMontage komutları.
7. `--oncesi openmontage` → HAZIR.
8. `git -C ~/.openmontage fetch origin main` ve `git pull --ff-only` (onay 5. adımdaki cümleyle verildi; `origin` adresi değiştirilmez); çakışma olursa "Yerel yamalar" 2-3. adımlar.
9. Bağımlılıklar: `requirements.txt` farkı varsa kullanıcıya göster; `make setup` olduğu gibi çalıştırılmaz; gereken adımlar tek tek, `HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_AUTO_INSTALL=1 HYPERFRAMES_NO_UPDATE_CHECK=1` tanımlıyken; `pip install -U` yok.
10. `--oncesi`/denetim: sabit sürümler N/N, kurulu = hedef; yamalar yerinde ("kayıtlı ama değişmemiş" olmamalı); `~/.claude/skills` bağları kırık mı; `program-denetim.py --oncesi openmontage --cevrimdisi` 'bağlar' satırlarında HATA olmamalı (olursa projeye göre `--yenile`/`--kaldir` için kullanıcıya sor).
11. preflight (openmontage skilindeki komut).
12. Kart: `kutuphane_commit`, `KAYNAK.md`, `tedarik_dogrulama.ozet.deger`, `yerel_yamalar.bilinen` (kaybolan/yeni yama); `--sema --siki`, testler, commit.
13. Yedek silme hatırlatması.

**"etsyotomasyon'u güncelle"** (kaynak kopyalı): `--sema --siki`, `program-denetim.py`, `--oncesi etsyotomasyon`, CHANGELOG özeti + ayrı onay, yedek (`KAYIT.json`), kaynak kopyasını yeni etiketten yenile, `KAYNAK.md` ve kartı güncelle, commit.
**"Yeni program ekle"**: `--iskelet <tür>` ile iskeleti al, doldur, `--sema` temiz olsun; "Yeni program eklemek" bölümünün adımları (repoyu oku, kaynak kopyası ya da yerinde kart, `kaynaklar.json` kaydı, `listeye-ekle.py`); `--oncesi <ad>` ile kuru deneme; kontroller, commit.
**"Programı kaldır"** / **"geri al"**: yukarıdaki "Programı çıkarma" ve "Geri alma" bölümleri.

## Aylık takip
Aylık özet `python3 araclar/program-denetim.py --ozet-json` komutunu çalıştırır (tek JSON nesnesi verir, dosya yazmaz, çıkış 0). `YENİ SÜRÜM VAR`, `KART ESKİ`, `kırıcı adayı` ve kart şeması bulguları kullanıcıya soru olur;
hiçbir zaman kendiliğinden güncelleme yapılmaz. `karar_bekleyen` metinleri sürüm taşır (örnek `hyperframes 0.9.23 -> 0.9.34 güncellemesi: kullanıcı onayı bekliyor`): kapatılmış bir karar o sürüm için tekrar sorulmaz, yeni hedef sürüm yeni soru üretir.
