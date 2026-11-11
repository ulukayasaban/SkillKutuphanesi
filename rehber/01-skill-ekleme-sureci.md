# 01 — Projeye ve Agent'a Skill Ekleme Süreci

## Temel kural: skill sadece verdiğin projeye eklenir

`skill-ekle.py` **yalnızca komutta verdiğin proje klasörüne** yazar. Başka projeler, global klasörler
(`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`), `~/.openmontage` ve bu kütüphanenin kendisi
**hiçbir zaman** değişmez (araç bu klasörlere yazmayı reddeder).

- Bir projede `ui-tasarimci` agent'ına `impeccable` verirsen, sadece o projedeki `ui-tasarimci` onu önyükler.
- Aynı projedeki diğer agent'lar için: Claude'da önyüklenmez (ama gerekirse Skill aracıyla çağırabilir);
  Codex'te ise o rolün `.toml` dosyasında açıkça **kapatılır**.
- Genel klasörlerdeki (~/.claude/skills, ~/.agents/skills, ~/.codex/skills) skiller bu araçla yönetilmez. Genel klasörler boşaltıldıktan sonra (rehber/12-genel-klasor-bosaltma.md) eski projeler ve agent'lar yalnız kendi proje klasöründeki skilleri görür; skill gerekiyorsa o projeye bu araçla kurulur.

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
