# 14 — Yapay Zeka Araçları: Hangi Araç Neyi Okur

Bu belge, kütüphanenin projeye yazdığı tek klasör düzeninin hangi yapay zeka araçlarına hizmet ettiğini, düzenin nasıl seçildiğini,
projeyi başka bilgisayara ya da Windows'a götürürken neyin bozulduğunu ve yeni bir araç eklenince ne yapılacağını anlatır.
Araçlara ait makine okunur veri `yapay-zeka-araclari.json` dosyasındadır; bu belgedeki tablolar onun kopyasıdır, **çelişirse JSON geçerlidir**.

## 1. Neden bu belge
`skill-ekle.py` projeye tek bir yerleşim yazar: `.agents/skills` (gerçek kopya), `.claude/skills` (symlink), rol dosyaları ve
`CLAUDE.md` / `AGENTS.md` blokları. Antigravity, Cursor ve Copilot için ayrı dosya yazmaya gerek yoktur: okudukları klasörler zaten vardır.
Eksik olan, bu seçimin ne anlama geldiğinin ve hangi aracın neyi göremeyeceğinin açıkça yazılmasıydı. Bu belge onu söyler.

## 2. Hangi araç neyi okur
| Araç | Proje skill klasörleri | Talimat dosyaları | Rol dosyası | Son doğrulama |
|---|---|---|---|---|
| Claude Code (kurulu) | `.claude/skills` | `CLAUDE.md` | `.claude/agents/*.md` (üretilir) | 2026-11-11 |
| Codex (kurulu) | `.agents/skills` | `AGENTS.md` | `.codex/agents/*.toml` (üretilir) | 2026-11-11 |
| Antigravity (kurulu) | `.agents/skills` | `AGENTS.md`, `GEMINI.md` | `.agents/agents/*.md` (üretilmez) | 2026-11-11 |
| Cursor (kurulu) | `.agents/skills`, `.cursor/skills`, `.claude/skills`, `.codex/skills` | `AGENTS.md` | `.cursor/agents/*.md` (üretilmez) | 2026-11-11 |
| VS Code Copilot (kurulu) | `.github/skills`, `.claude/skills`, `.agents/skills` | `.github/copilot-instructions.md` | `.github/agents/*.agent.md` (üretilmez) | 2026-11-11 |
| Gemini CLI (kurulu değil) | `.gemini/skills`, `.agents/skills` | `GEMINI.md` | `.gemini/agents/*.md` (üretilmez) | 2026-11-11 |
| Copilot CLI (kurulu değil) | `.github/skills`, `.claude/skills`, `.agents/skills` | `.github/copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | `.github/agents/*.agent.md` (üretilmez) | 2026-11-11 |

Notlar:
- Doğrulanmamış her şey JSON'da `belirsizler` listesindedir (ör. symlink desteği Claude dışında belgede yok). Gerçek deneme yapılırsa `denendi`'ye yazılır; şu an hiçbir araçta deneme yapılmış değildir.
- Antigravity hem `AGENTS.md` hem `GEMINI.md` dosyasını birlikte okur. Cursor ve VS Code Copilot `.claude/skills` klasörünü de okur.
- Gemini CLI ve Copilot CLI bu Mac'te kurulu değildir; kayıtları bilgi içindir (`destek: istege-bagli`).

## 3. Düzen seçimi
Kurulumdan önce kullanıcıya sor: **"Bu proje hangi araçlarla açılacak?"** Cevaba göre:

| Durum | Düzen |
|---|---|
| Codex ya da Antigravity kullanılacak | `ortak` |
| Yalnız Claude Code (Cursor ve VS Code Copilot da açabilir) | `yalniz-claude` (Cursor ve Copilot `.claude/skills`'i okur; `AGENTS.md` bloğunu görmezler; Codex ve Antigravity hiçbir şey görmez) |
| Windows'ta da açılacak | bugün `yalniz-claude` (Codex ve Antigravity orada göremez; bölüm 5) |
| Bilinmiyor | `ortak` (varsayılan); kullanıcı cevap verince `--arac ortak` ile kaydet |
| Gemini CLI kullanılacak (kurulu değil) | `ortak` (`.agents/skills`'i okur). `GEMINI.md` dosyasını da okur; kütüphane o dosyayı yazmaz (bölüm 6) |

Kaydetmek için: `--arac <düzen> --kuru` ile bak, sonra `--evet`; raporda `arac-duzeni` satırını kontrol et.
Eski adlar çalışır: `ikisi` = `ortak`, `claude` = `yalniz-claude`.

## 4. Projede ne oluşur
```
ortak                                      yalniz-claude
├─ .agents/skills/<skill>/  (gerçek)       ├─ .claude/skills/<skill>/  (gerçek)
├─ .claude/skills/<skill> -> ../../.agents └─ .claude/agents/<rol>.md
│                 /skills/<skill>          ├─ CLAUDE.md  (skill bloğu)
├─ .claude/agents/<rol>.md                 └─ .skill-kutuphanesi/ (kilit.json, yedek/, .gitignore)
├─ .codex/agents/<rol>.toml
├─ CLAUDE.md + AGENTS.md  (aynı skill bloğu)
└─ .skill-kutuphanesi/ (kilit.json, yedek/, .gitignore)

Her iki düzende ayrıca (rehber/01 "Programla gelen skiller: bağ" ve "Dondurma"):
  <program-skill>   (bağ -> program klasörü; ortak: .agents/skills'te mutlak bağ + .claude/skills'te göreli bağ; yalniz-claude: .claude/skills'te mutlak bağ)
  <donmuş-skill>/   (gerçek klasör, projenin kendi skili; yerleşimi kütüphane skilleriyle aynı)
```

## 5. Başka bilgisayara ve Windows'a kopyalama
Taşınanlar: `.agents`, `.claude`, `.codex`, `CLAUDE.md`, `AGENTS.md`, `.skill-kutuphanesi/kilit.json`. Bozulabilecekler:
1. **Symlink'ler:** Windows'ta ve `core.symlinks` kapalı git'te `.claude/skills` altındaki bağlar düz metin dosyasına döner; `ortak` düzen orada güvenli değildir.
2. **Mutlak yollar:** `.codex/agents/*.toml` bu Mac'in mutlak yollarını içerir; başka yerde Codex rol dışı skilleri kapatamaz. Kütüphanenin olduğu Mac'te `--yenile` ile düzelt.
3. **Kilit yolu:** `kilit.json` → `proje_yolu` uymaz; `--dogrula` "proje taşınmış" der; `--yenile` düzeltir.
4. **Satır sonları:** Windows'ta satır sonu çevirisi dosya parmak izlerini değiştirip Mac'te yanlış "elle değiştirilmiş" gösterebilir. Projeye şu `.gitattributes` satırları önerilir (araç yazmaz, yalnız öneridir): `.agents/skills/** -text` ve `.claude/skills/** -text`.
5. **Kütüphane yok:** Windows'ta kütüphane yoktur; skill ekleme/güncelleme yalnız kütüphanenin olduğu Mac'te yapılır. Projedeki `CLAUDE.md` / `AGENTS.md` bloğu bugün bunu kısa blokta söyler; kütüphane yolunu ve "kütüphane oturumu iste" cümlesini bloğa eklemek onay bekliyor (`notlar/duzen-denetimi-2026-11/onay-bekleyen/p1-blok-kutuphane-cumlesi.md`).
6. **Program bağları:** Bağlı program skilleri başka bilgisayarda ya da Windows'ta çalışmaz (mutlak yol); git'e konursa Windows'ta düz metin dosyasına döner (bağ yolları `.gitignore`'a girmeli). Donmuş skiller gerçek klasördür, kopyalanabilir. Windows'ta `--program-skill` ve `--dondur` reddedilir.
7. **Araç Windows'ta çalışmaz:** `skill-ekle.py` Windows'ta kendini reddeder (symlink, `kill -0` ve Mac yolları).

**Projeyi başka Mac'e kopyaladım:** kütüphaneli Mac'te `--dogrula`; `proje taşınmış` çıkarsa `--yenile`; sonra tekrar `--dogrula`.
**Projeyi Windows'ta açacağım:** önce `--arac yalniz-claude --kuru`, onaylarsa `--evet`; Windows'ta yalnız Claude Code (ve Cursor/VS Code Copilot) skilleri görür.

## 6. GEMINI.md
Kütüphane `GEMINI.md` dosyası **yazmaz**. Antigravity `AGENTS.md` ile `GEMINI.md` dosyasını birikimli okuduğu için aynı blok iki dosyada iki kez yüklenirdi; yalnız Gemini CLI kullanan biri için gerekir ve o kurulu değildir.
Gemini CLI kurulursa ya da kullanıcı isterse isteğe bağlı bir `GEMINI.md` bloğu ayrıca tasarlanır ve onay ister; bugün çalışan bir komut yoktur.

## 7. Yeni bir yapay zeka aracı eklendiğinde
(Aynı akış `promptlar/15-yeni-yapay-zeka-araci.md` içinde yürütülür; kütüphane oturumunda yapılır.)
1. Kullanıcıya aracın adını ve kurulu olup olmadığını sor; `python3 araclar/skill-ekle.py --araclar` çalıştır (kurulu durumu görünür).
2. YALNIZ resmi belgeleri oku: proje skill klasörleri, talimat dosyaları, rol dosyası biçimi, symlink, aynı ad önceliği, makine genelinde yazdığı klasörler, sürüm komutu. Tarihi ve adresleri yaz. Belirsiz ya da net olmayan her şey `belirsizler`'e girer; tahmin yok.
3. `yapay-zeka-araclari.json`'a kayıt ekle (en yakın kaydı kopyala, her alanı doldur, `denendi: []`); JSON geçerli kalsın.
4. Uyum kontrolü: araç `.agents/skills` ya da `.claude/skills` okuyorsa zaten hizmet alıyordur. İkisini de okumuyorsa `destek: "yok"` yaz, kullanıcıya söyle ve dur: yeni bir düzen kod değişikliğidir ve onay ister (doğaçlama yapma).
5. Makine genelindeki klasörler: `kullanici_koku` ve `genel_skill_okur` bilgi amaçlı doldurulur. Sonra kullanıcının O ANKİ onayıyla aracın makine genelindeki skill klasörü `notlar/genel-klasor-tabani.json` → `ek_klasorler` içine eklenir (bekçinin okuduğu TEK yer; bu JSON onu tekrarlamaz). Ardından `python3 araclar/genel-bekci.py` temiz olmalıdır.
6. `python3 araclar/skill-ekle.py --araclar` çalıştır (kayıt okunuyor, sürüm okunuyor); sonra `python3 araclar/dogrula.py`.
7. Kayıtlı bir projede deneme: `skill-ekle.py <proje> --guncelle --kuru`. `arac-duzeni` satırı yeni aracı görenler ya da görmeyenler arasında anmalıdır. Göremiyorsa düzeni değiştirmek isteyip istemediğini kullanıcıya sor.
8. Gerçek deneme: küçük bir deneme projesini yeni araçta aç, skilleri listelemesini iste; tarih ve sonucu `denendi`'ye yaz. İlgili `belirsizler` satırını ancak bu denemeden sonra sil.
9. Farkı kullanıcıya göster; commit yalnız onayla, push yalnız kullanıcı isterse.

## 8. Aylık kontrol
`python3 araclar/skill-ekle.py --araclar` (makineye bakar, hiçbir şey yazmaz; yalnız `claude`, `codex`, `gemini`, `copilot` için `--version` çalıştırır, başka komut çalıştırmaz). Çıktı:
- `temiz`: kayıtlı sürümler makinedekiyle aynı ve hiçbir belge 45 günden eski değil.
- `dikkat`: en az bir karar satırı var. Karar satırları şunlardır: belge 45 günden eski; kayıtlı sürüm makinedekinden farklı; kurulu görünen araç bulunamadı; kurulu olmayan araç bulundu. Her biri için o aracın resmi sayfalarını yeniden oku, kaydı ve `dogrulama_tarihi`'ni güncelle; davranış değiştiyse gerçek denemeyi tekrarla.
- `sorun`: dosya yok, bozuk ya da bir kayıtta zorunlu alan eksik; önce dosyayı onar.
Makine okunur özet: `--araclar --ozet-json` (tek JSON nesnesi; `--siki` ile `sorun` durumunda çıkış 1).
Not: aylık özet aracı (`aylik-ozet.py`) bu kontrolü yalnız TAM kipte çalıştırır; hızlı oturum başı kipi (`--hizli`) araç belgesi eskimesini göstermez. Bu yüzden eskime yalnız tam aylık çalışmada ya da elle `--araclar` ile görünür.

## 9. Belirsizlikler ve nasıl denenir
Bir aracın proje skilli gerçekten görüp görmediğini denemek için küçük bir deneme projesine skill kur, aracı o projede aç ve skilleri listelemesini iste:
- Claude Code: oturumda skill listesine bak (`/skills` ya da Skill aracı).
- Codex: `codex exec "list available skills"` (rehber/04).
- Antigravity, Cursor, VS Code Copilot: aracın sohbetinden "bu projedeki skilleri listele" de; `ortak` düzende aynı skill iki kez çıkıyor mu bak (Cursor ve Copilot iki klasörü de okur).
Sonucu `yapay-zeka-araclari.json` → `denendi`'ye (tarih + sonuç) yaz.

## 10. Bilinen sınırlar
- Rol dosyaları yalnız Claude ve Codex için üretilir (Cursor `.claude/agents` dosyalarını da okur). Antigravity, Cursor ve Copilot'ta her ajan projedeki tüm skilleri görür.
- `ortak` düzende Cursor ve Copilot aynı skilli iki kez listeleyebilir (belgede yok, denenmedi).
- Kütüphane makine genelinde hiçbir skill kurmaz.
- Program skilleri bağdır: araç düzeni seçimi (ortak/yalniz-claude) bağın yerini değiştirir ama içeriği hiç kopyalamaz. Bağlı skillin Codex, Antigravity ve Cursor tarafından keşfedildiği sınanmadı (Claude Code'da çalışır); program kurulu değilse bağ asılı kalır (`--dogrula` kırık sayar). Gerçek araçla sınama ayrı adım.
- `skill-ekle.py` Windows'ta çalışmaz; aynı projede iki oturumdan aynı anda çalıştırma (proje kilidi yok).
