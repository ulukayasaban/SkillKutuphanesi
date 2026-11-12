# 01 — Projeye ve Agent'a Skill Ekleme Süreci

## Temel kural: skill sadece verdiğin projeye eklenir

`skill-ekle.py` **yalnızca komutta verdiğin proje klasörüne** yazar. Başka projeler, global klasörler
(`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`), `~/.openmontage` ve bu kütüphanenin kendisi
**hiçbir zaman** değişmez (araç bu klasörlere yazmayı reddeder).

- Bir projede `ui-tasarimci` agent'ına `impeccable` verirsen, sadece o projedeki `ui-tasarimci` onu önyükler.
- Aynı projedeki diğer agent'lar için: Claude'da önyüklenmez (ama gerekirse Skill aracıyla çağırabilir);
  Codex'te ise o rolün `.toml` dosyasında açıkça **kapatılır**.
- Genel klasörlerdeki (~/.claude/skills, ~/.agents/skills, ~/.codex/skills) skiller bu araçla yönetilmez. Genel klasörler boşaltıldıktan sonra (rehber/12-genel-klasor-bosaltma.md) eski projeler ve agent'lar yalnız kendi proje klasöründeki skilleri görür; skill gerekiyorsa o projeye bu araçla kurulur. Programla gelen skiller bağ ile, yalnız genel klasörde kalmış eski skiller dondurma ile projeye alınır (aşağıda).

## Süreç (her seferinde aynı)

```
 1. İhtiyacı söyle ──► 2. ÖNERİ (tüm kütüphane taranır) ──► 3. KURU ÇALIŞTIRMA (ön kontrol raporu)
                                                                     │
                     6. DOĞRULAMA ◄── 5. KURULUM (yedekli) ◄── 4. Raporu oku, onay ver
```

1. **İhtiyaç:** proje tipi, kullanılacak teknoloji, agent'lar ve hangi AI araçlarıyla açılacağı (Claude Code, Codex, Antigravity, Cursor, VS Code Copilot; Windows'ta açılacak mı). Cevaba göre `--arac ortak` ya da `--arac yalniz-claude` (rehber/14).
2. **Öneri:** `--oner "..."` kütüphanedeki tüm skilleri (gizliler dahil sayılır) puanlar; hangi rolün uygun olduğunu söyler.
3. **Kuru çalıştırma:** `--kuru` ön kontrol raporunu ekrana yazar; projeye **hiçbir dosya yazmaz**. (Uygulanan kurulumun raporu `.skill-kutuphanesi/son-rapor.md`'ye kaydedilir.)
4. **Onay:** HATA varsa işlem yapılmaz. UYARI varsa sen onaylarsın (`--evet`).
5. **Kurulum:** Önce otomatik yedek alınır. Bir adım hata verirse her şey yedekten geri alınır.
6. **Doğrulama:** Her kopyanın, bağlantının, agent dosyasının ve Codex yolunun çalıştığı kontrol edilir.
7. **Kayıt:** Kurulum, güncelleme ve kaldırmadan sonra `notlar/proje-kullanimi.md` kendiliğinden yenilenir (hangi proje hangi skili
   kullanıyor; `rehber/10-proje-kullanimi.md`). Aynı adlı başka skill varsa ön kontrol `ayni-ad` satırıyla hangi kaynağın kurulduğunu
   gösterir (`rehber/09-ad-kimlik-ve-cakisma.md`).

## Örnek 1 — Yeni 3D ürün tanıtım sitesi (Next.js + R3F)

```bash
cd ~/Documents/SkillKutuphanesi
# 2) Öneri: hangi skiller ve roller?
python3 araclar/skill-ekle.py ~/Projeler/urun-3d --oner "3d ürün tanıtım sitesi scroll animasyonlu"
# 3) Kuru çalıştırma: rapor
python3 araclar/skill-ekle.py ~/Projeler/urun-3d --profil 3d-urun-sergisi --kuru
# 5) Onaylıyorsan uygula
python3 araclar/skill-ekle.py ~/Projeler/urun-3d --profil 3d-urun-sergisi --evet
# 6) Kontrol
python3 araclar/skill-ekle.py ~/Projeler/urun-3d --durum
python3 araclar/skill-ekle.py ~/Projeler/urun-3d --dogrula
```

Projede oluşan yapı:
```
urun-3d/
├─ .agents/skills/                 ← Codex okur (gerçek kopyalar)
│  ├─ design-taste-frontend/
│  ├─ impeccable/                  ← Codex'e özel sürüm
│  ├─ threejs-fundamentals--kutuphane/   ← globaldeki farklı sürümle çakışmasın diye ekli ad
│  └─ …
├─ .claude/skills/                 ← Claude okur
│  ├─ design-taste-frontend -> ../../.agents/skills/design-taste-frontend   (symlink)
│  ├─ impeccable/                  ← Claude'a özel sürüm (gerçek kopya)
│  └─ …
│  (bağlı program skilleri: .claude/skills/<ad> -> ../../.agents/skills/<ad> -> program klasörü)
├─ .claude/agents/ui-tasarimci.md        ← skills: [design-taste-frontend, ui-ux-pro-max, impeccable]
├─ .codex/agents/ui-tasarimci.toml       ← diğer proje skilleri enabled=false
├─ AGENTS.md / CLAUDE.md                 ← "Proje skilleri" bloğu (senin metnine dokunulmaz; `--blok kisa` ile tablo yerine tek paragraf)
└─ .skill-kutuphanesi/
   ├─ kilit.json                         ← hangi skill, hangi commit, hangi rol, içerik parmak izi
   ├─ son-rapor.md                       ← son ön kontrol raporu
   └─ yedek/                             ← son 10 işlemin yedeği (`--yedekler`)
```

## Örnek 2 — Var olan projeye tek agent ve birkaç skill

```bash
# Sadece bir rol
python3 araclar/skill-ekle.py ~/Projeler/site --rol motion-gelistirici --kuru
python3 araclar/skill-ekle.py ~/Projeler/site --rol motion-gelistirici --evet

# Kendi rol adınla, seçtiğin skiller
python3 araclar/skill-ekle.py ~/Projeler/site --skill lottie-animations number-flow --rol-adi animasyoncu --evet

# Rolün opsiyonel skilleri de gelsin
python3 araclar/skill-ekle.py ~/Projeler/site --rol 3d-gelistirici --opsiyonel --evet
```

## Örnek 3 — AI medya projesi

```bash
python3 araclar/skill-ekle.py ~/Projeler/reklam-videosu --profil ai-video-uretimi --kuru
```
Bu profil OpenMontage skillerini kullanır. Raporda `bagimlilik` uyarısı çıkar: komutlar `~/.openmontage` kurulumundan çalışır.
OpenMontage ve HyperFrames'in kendi skilleri kopya olarak değil bağ olarak verilir: `--program-skill openmontage:<ad>` (aşağıda "Programla gelen skiller: bağ").

## Örnek 4 — Sohbetten (Claude veya Codex'e)

> "~/Projeler/yeni-site için Next.js + GSAP landing page yapacağız; ui-tasarimci, motion ve qa agent'ları olacak. Skilleri kur."

Agent `SkillKutuphanesi/CLAUDE.md` (Codex: `AGENTS.md`) talimatına göre:
1. Hangi araçlarla açılacağını sorar ve `--arac` ile kaydeder.
2. `--oner` çalıştırır, tabloyu gösterir.
3. `--kuru` raporunu gösterir: HATA/UYARI/BİLGI satırları ve "kütüphanede şu ilgili skiller de var" listesi.
4. **Senin onayınla** `--evet` ile kurar, `--dogrula` sonucunu bildirir.

## Araç düzeni: hangi araç neyi görür
Proje iki düzenden biriyle kurulur. Seçim `kilit.json` → `araclar` (+ `arac_secimi`) alanına yazılır; güncellemeler seçimi korur.

| | `ortak` (varsayılan) | `yalniz-claude` |
|---|---|---|
| Klasörler | `.agents/skills` (gerçek kopya) + `.claude/skills` (symlink) | `.claude/skills` (gerçek kopya) |
| Rol dosyaları | `.claude/agents/*.md` + `.codex/agents/*.toml` | `.claude/agents/*.md` |
| Talimat bloğu | `CLAUDE.md` + `AGENTS.md` | `CLAUDE.md` |
| Skilleri görenler | Claude Code, Codex, Antigravity, Cursor, VS Code Copilot | Claude Code, Cursor, VS Code Copilot |
| Görmeyenler | yok | Codex, Antigravity |

- Komut: `--arac ortak` ya da `--arac yalniz-claude`. `ikisi` ve `claude` eski adlardır, hâlâ çalışır (`ikisi` = `ortak`, `claude` = `yalniz-claude`).
- Rapordaki `arac-duzeni`, `arac-gormez` ve `arac-secimi-yok` satırlarını oku; hangi aracın skilleri göreceğini orada yazar. `arac-secimi-yok` çıkıyorsa kullanıcıya hangi araçlarla açılacağını sor ve `--arac` ile kaydet.
- İstediğin zaman iki düzen arasında gidip gelebilirsin; skill içeriği değişmez, yalnız yerleşim değişir (önce yedek alınır):
```bash
python3 araclar/skill-ekle.py <proje> --arac yalniz-claude --kuru   # ne değişecek
python3 araclar/skill-ekle.py <proje> --arac yalniz-claude --evet   # uygula
python3 araclar/skill-ekle.py <proje> --arac ortak --evet           # ortak düzene dön
```
- Kurulu skiller varken `--skill ... --arac <başka düzen>` birlikte verilirse `arac-karisik` HATA'sı çıkar: önce yalnız `--arac` ile düzeni değiştir, sonra skill ekle.
- Windows'ta açılacak projelerde bugün `yalniz-claude` kullanılır (git orada symlink'i açamaz; Codex ve Antigravity göremez). Ayrıntı ve araç tablosu: `rehber/14-yapay-zeka-araclari.md`.
- Test (2026-10-21): deneme projesinde Claude ve Codex 10 skill'in hepsini listeledi. Antigravity, Cursor ve Copilot için gerçek deneme henüz yok (`yapay-zeka-araclari.json` → `denendi` boş).
- Symlink'in aynı içerikli gerçek kopyaya dönmesi (klasör kopyalanınca/commit edilince) "elle değiştirilmiş" sayılmaz.

## Programla gelen skiller: bağ

Karar K-28: OpenMontage ve HyperFrames gibi programların kendi skilleri projeye **kopyalanmaz** ve hep kurulu programın sürümü olur. Projeye programın kendi skill klasörüne **bağ** (symlink) verilir; tek kaynak kurulu programdır, program güncellenince bağ kendiliğinden güncel kalır.

```bash
# proje yolunu ÖNCE yaz (--program-skill ve --dondur birden çok değer alır)
python3 araclar/skill-ekle.py <proje> --program-skill openmontage:ffmpeg hyperframes:hyperframes --kuru
python3 araclar/skill-ekle.py <proje> --program-skill openmontage:ffmpeg hyperframes:hyperframes --evet
```
- Her skill adıyla yazılır: `PROGRAM:AD`. `PROGRAM:*` (programın hepsi) yoktur; proje durumu açık ve gözden geçirilebilir kalsın diye.
- Kaynak, program kartındaki (`programlar.json`) `skill_koku` klasörünün altındaki `<AD>` klasörüdür ve içinde `SKILL.md` olmalıdır. Kartta `skill_koku` yoksa ya da boşsa programın skili yok sayılır (HATA `program-skillsiz`).
- `--profil/--rol/--skill` ile aynı çalışmada kullanılabilir. Roller kütüphane skilleri içindir: bağlı skiller rol dosyalarına yazılmaz, projedeki tüm ajanlar görür.
- Program klasörüne hiçbir şey yazılmaz; bağı kaldırmak yalnız bağı siler.

Yerleşim (mutlak yol bu Mac'teki program klasörüdür):

| Düzen | Bağ |
|---|---|
| `ortak` | `.agents/skills/<ad>` -> mutlak program klasörü; `.claude/skills/<ad>` -> `../../.agents/skills/<ad>` |
| `yalniz-claude` | `.claude/skills/<ad>` -> mutlak program klasörü (`.agents/skills/<ad>` yok) |

Kilitte (`.skill-kutuphanesi/kilit.json`) kütüphane skillerinden ayrı `dis_skiller` anahtarı tutulur (eski sürümler bu anahtarı görmez, zarar vermez):
```json
"dis_skiller": { "ffmpeg": { "ad": "ffmpeg", "tur": "program-bag", "program": "openmontage",
  "hedef": "/Users/<ev>/.openmontage/.agents/skills/ffmpeg", "tarih": "2026-11-12",
  "program_surum": "fecb9a1e…", "program_surum_turu": "commit" } }
```
Bağın hedefi kayda güvenilerek değil karttaki `skill_koku` ile `ad`'dan yeniden türetilir; kilitteki hedef karttakinden farklıysa `--dogrula` söyler, `--yenile` yeni hedefe bağlayıp kilidi düzeltir. Kilitteki geçersiz kayıtlar (yol bileşeni olamayacak ad, bilinmeyen tür, göreli hedef) yok sayılır ve `--dogrula` bildirir.

Sonraki komutlar:
- `--durum`: bağ `programla güncel (bağ)` görünür; kırıksa `BAĞ KIRIK`.
- `--dogrula`: kırık bağ (program klasörü yok / skill yok), yanlış yere giden ya da yerine gerçek klasör konmuş bağ, kırık bağlar çıkış 1 verir.
- `--guncelle`: dış skiller hiçbir zaman "güncellenecek" sayılmaz; tek bilgi satırı ve kırık bağ için UYARI `bag-kirik` verir.
- `--yenile`: eksik bağları yeniden kurar (hedef yoksa kurmaz, asılı bağ bırakmaz; gerçek klasöre dokunmaz). `--arac` ile düzen değişince bağlar yeni düzene döşenir.
- `--kaldir <ad>`: yalnız iki bağı siler, program klasörüne dokunulmaz. Slot elle gerçek klasöre çevrilmişse HATA `bag-degismis` (`--zorla` geçmez). `--kaldir hepsi` yalnız kütüphane skillerini kaldırır; bağlara ve donmuşlara adla bakılır.

Dikkat:
- Bağ makineye özeldir (mutlak yol): başka bilgisayarda ve Windows'ta çalışmaz; paylaşılan bir git deposuna girmesin (`.gitignore`'a ekle ya da yalnız bu Mac'te kullan). Proje bir git deposuysa ve bağ yolları ignore edilmiyorsa UYARI `bag-git-izlenir`; araç proje `.gitignore`'una yazmaz.
- Bağlı skillin Codex, Antigravity ve Cursor tarafından keşfedildiği sınanmadı; Claude Code'da çalışır. Program kurulu değilse bağ asılı kalır (`--dogrula` kırık sayar).
- Program güncellenmeden önce `python3 araclar/program-denetim.py --oncesi <program>` hangi bağların kırılacağını göstermelidir (rehber/11). Bu kısım ayrı bir adımda eklenir; o zamana kadar program güncellemesinden sonra `--dogrula` ile bak.

## Dondurma

Yalnız bir genel klasörde (ör. `~/.claude/skills`) kalmış ve hiçbir program ya da kütüphane kaynağının artık vermediği eski bir skill projenin kendi skili olarak **dondurulur**: araç içeriği bir kez kopyalar, kilide `tur: "donmus"` yazar, kütüphane onu bir daha güncellemez ve kaynağını izlemez.

```bash
python3 araclar/skill-ekle.py <proje> --dondur ~/.claude/skills/eski-skill --kuru
python3 araclar/skill-ekle.py <proje> --dondur ~/.claude/skills/eski-skill --evet
```
- Yerleşim kütüphane skilleriyle aynıdır (`ortak`: gerçek klasör `.agents/skills/<ad>` + `.claude/skills/<ad>` göreli bağı; `yalniz-claude`: gerçek klasör `.claude/skills/<ad>`). Kaynaktaki dosya bağları çözülür; kopyada bağ kalmaz. İçerik hiç değiştirilmez.
- Reddedilen durumlar (hepsi `--zorla` ile geçilemez): `dondur-yol` (mutlak yol değil), `dondur-ad` (geçersiz klasör adı), `dondur-kaynak-yok` (klasör ya da SKILL.md yok), `dondur-program-skili` (skill bir programla geliyor: `--program-skill` kullan), `dondur-kutuphane-adi` (projede aynı adlı kütüphane skili var), `dondur-kendisi` (kaynak projenin kendi klasöründe), `dondur-gizli` (`.env`, `.npmrc`, `id_rsa*`, `*.pem`, `*.key`, `credentials`, `.ssh`, `.git` gibi gizli değer taşıyabilecek dosya/klasör adı; dosyalar açılmaz, yalnız adlara bakılır), `dondur-dis-baglanti` (klasör bağı, klasör dışına giden ya da bozuk dosya bağı), `dondur-ozel-dosya` (FIFO/soket), `dondur-cok-buyuk` (200 MB, 5000 dosya ya da 2000 klasör üstü). Sınır bilerek sıkıdır: kaynak klasörün içinde tek bir dosya bağı bile klasör dışına gidiyorsa ya da bozuksa dondurma durur (klasör içinde kalan dosya bağları sorun değildir). Ayrıca `dondur-kendisi`, kaynak projeyi kendi içinde barındırıyorsa da verilir. Bağ kurarken: aynı `--program-skill` komutu yeniden çalışınca bağın yerinde elle konmuş gerçek klasör varsa `bag-gercek-klasor` ile durur (klasör silinmez).
- UYARI (`--evet` ister): `dondur-buyuk` (50 MB üstü), `dondur-ad-farkli` (SKILL.md içindeki ad klasör adından farklı). `node_modules`, `__pycache__`, `.venv` kopyalanmaz (BİLGİ). Kopyanın içeriği taranmaz: proje deposuna koymadan önce dosyalara bak.
- `--kaldir <ad>` donmuş kopyayı önce yedeğe alır (`--geri-al` ile dönülür); yedekler yalnız son 10 işlemde tutulur, kalıcı saklamak için yedek klasörünü başka yere kopyala. Donmuş kopya sonradan düzenlenmişse `--kaldir` UYARI `dondurma-degismis` verir.
- Donmuş skill düzenlenebilir; `--dogrula` içeriği karşılaştırmaz, `--guncelle` dokunmaz. Yeniden dondurmak için önce `--kaldir`, sonra `--dondur`.

## Kaldırma / geri alma
```bash
python3 araclar/skill-ekle.py <proje> --kaldir gsap-core --evet   # tek skill
python3 araclar/skill-ekle.py <proje> --kaldir hepsi --evet       # kütüphaneden gelen her şey
python3 araclar/skill-ekle.py <proje> --geri-al                   # son işlemi geri al
python3 araclar/skill-ekle.py <proje> --yedekler                  # yedekleri listele
python3 araclar/skill-ekle.py <proje> --geri-al <yedek-adi>       # belirli bir yedeğe dön (geri almayı geri almak dahil)
```
`--kaldir` sadece kütüphaneden gelmiş ve elle değiştirilmemiş skilleri siler. Senin eklediğin skillere dokunmaz.

## Proje taşındıysa
Codex agent dosyalarında mutlak yol vardır. Proje klasörünü taşıdıysan ya da yeniden adlandırdıysan:
```bash
python3 araclar/skill-ekle.py <yeni-yol> --yenile
```
Başka bilgisayara ya da Windows'a kopyalandıysa rehber/14 bölüm 5. `skill-ekle.py` Windows'ta çalışmaz; skill ekleme/güncelleme kütüphanenin olduğu Mac'te yapılır.

## Dikkat edilecekler
- Silmeden önce başka skillerin ona bağlı (kardeş yol) olup olmadığına bak: `python3 araclar/proje-kullanimi.py --skill <kimlik>` ve projedeki `.skill-kutuphanesi/kilit.json` → `kardes` alanı. Tek elle değişmiş skill yüzünden güncelleme duruyorsa kullanıcıya göster; kararını al (`--zorla` ya da skili geri yükle).
- Aynı projede iki oturumdan aynı anda skill-ekle çalıştırma (proje kilidi yok); ikinci oturumu açmadan önce ilkinin bittiğine bak.
- Araç ilk yedekte `.skill-kutuphanesi/.gitignore` dosyasını kendisi yazar (`yedek/` satırı); yedekler git'e girmez.
- `--kuru` her işlemde hiçbir dosya yazmaz (`--yenile`, `--blok` ve `--geri-al` dahil).
