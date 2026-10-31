# 01 — Projeye ve Agent'a Skill Ekleme Süreci

## Temel kural: skill sadece verdiğin projeye eklenir

`skill-ekle.py` **yalnızca komutta verdiğin proje klasörüne** yazar. Başka projeler, global klasörler
(`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`), `~/.openmontage` ve bu kütüphanenin kendisi
**hiçbir zaman** değişmez (araç bu klasörlere yazmayı reddeder).

- Bir projede `ui-tasarimci` agent'ına `impeccable` verirsen, sadece o projedeki `ui-tasarimci` onu önyükler.
- Aynı projedeki diğer agent'lar için: Claude'da önyüklenmez (ama gerekirse Skill aracıyla çağırabilir);
  Codex'te ise o rolün `.toml` dosyasında açıkça **kapatılır**.
- Eski projelerin ve eski agent'ların, global klasörlerdeki skilleri kullanmaya devam eder.

## Süreç (her seferinde aynı)

```
 1. İhtiyacı söyle ──► 2. ÖNERİ (tüm kütüphane taranır) ──► 3. KURU ÇALIŞTIRMA (ön kontrol raporu)
                                                                     │
                     6. DOĞRULAMA ◄── 5. KURULUM (yedekli) ◄── 4. Raporu oku, onay ver
```

1. **İhtiyaç:** proje tipi, kullanılacak teknoloji, agent'lar.
2. **Öneri:** `--oner "..."` kütüphanedeki tüm skilleri (gizliler dahil sayılır) puanlar; hangi rolün uygun olduğunu söyler.
3. **Kuru çalıştırma:** `--kuru` ön kontrol raporunu ekrana yazar; projeye **hiçbir dosya yazmaz**. (Uygulanan kurulumun raporu `.skill-kutuphanesi/son-rapor.md`'ye kaydedilir.)
4. **Onay:** HATA varsa işlem yapılmaz. UYARI varsa sen onaylarsın (`--evet`).
5. **Kurulum:** Önce otomatik yedek alınır. Bir adım hata verirse her şey yedekten geri alınır.
6. **Doğrulama:** Her kopyanın, bağlantının, agent dosyasının ve Codex yolunun çalıştığı kontrol edilir.

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
├─ AGENTS.md / CLAUDE.md                 ← "Proje skilleri" bloğu (senin metnine dokunulmaz)
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
1. `--oner` çalıştırır, tabloyu gösterir.
2. `--kuru` raporunu gösterir: HATA/UYARI/BİLGI satırları ve "kütüphanede şu ilgili skiller de var" listesi.
3. **Senin onayınla** `--evet` ile kurar, `--dogrula` sonucunu bildirir.

## Projeyi Codex Desktop'ta / Claude'da açtığında
- **Claude Code:** proje skillerini `.claude/skills`'ten, agent'ları `.claude/agents`'tan otomatik görür.
- **Codex:** skillleri `.agents/skills`'ten, agent'ları `.codex/agents`'tan görür.
- 2026-10-21 testi: deneme projesinde iki araç da 10 skill'in hepsini listeledi.

### Sadece Claude kullanan proje (`--arac claude`)
Proje Codex kullanmıyorsa (ya da Windows'ta açılıyorsa: git orada symlink'i açamaz) skiller `.claude/skills` altında
**gerçek kopya** olur; `.agents/skills`, `.codex/agents` ve AGENTS.md bloğu kurulmaz. Seçim `kilit.json` → `araclar`'a
yazılır; sonraki `--skill`/`--guncelle` bu düzene uyar. Geri dönüş: `--arac ikisi`.
```bash
python3 araclar/skill-ekle.py <proje> --arac claude --kuru     # ne değişecek
python3 araclar/skill-ekle.py <proje> --arac claude --evet     # uygula (önce yedek; içerik değişmez)
```
Not: symlink'in aynı içerikli gerçek kopyaya dönmesi (klasör kopyalanınca/Windows) artık "elle değiştirilmiş" sayılmaz.

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
