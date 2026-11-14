# 12 — Genel skill klasörlerini bekleme ve boşaltma

Bu rehber iki işi anlatır: (1) makinedeki genel skill klasörlerinde beklenmeyen bir şey belirdi mi diye bakmak (`araclar/genel-bekci.py`),
(2) bu klasörleri yedekli ve adım adım boşaltmak. Boşaltma yalnız **kütüphane oturumunda** yapılır, **her adım ayrıca kullanıcı onayı**
ister ("ONAY GEREKİR"); "başla" demek toplu onay değildir. Bekçi hiçbir şeyi silmez, taşımaz, yazmaz: komut metni yazdırır, çalıştırmaz.
Yedek ve geri alma ilkeleri: `rehber/13-yedek-ve-geri-alma.md`. Boşaltma kararlarının ve geçişin durumu: `notlar/hf-om-gecisi/DURUM.md`.
Hazır komut: `promptlar/16-genel-klasor-bosaltma.md`.

**Uygulandı (2026-11-12, K-40):** boşaltma bu rehberle yapıldı; aşağıdaki adımlar bir sonraki sefer için hâlâ geçerli yöntemdir. Pratikte fark: girdiler `rm` ile
silinmedi, `~/Documents/Claude/yedek/genel-kaldirilan-2026-11-12` içine TAŞINDI (ayrıca tam kopya `genel-skiller-tam-2026-11-12`). İki HyperFrames klasörü
(`hyperframes`, `hyperframes-cli`) ve üç skill (`design-dna`, `openmontage`, `nlm-skill`) adım sırasından önce taşındı, çünkü bir proje geçişi bunu gerektirdi; bağımlıları yoktu.
Q1-Q9 kararları yanıtlandı (`notlar/kararlar.md` K-32..K-41). Bugün bekçi tabanı boş duruma göre yazılıdır; tablodaki "Boşaltma sonrası" sütunu artık gerçek durumdur.

## Neyi izliyoruz

| Bölge | Yol | Normalde kim yazar | Boşaltma sonrası |
|---|---|---|---|
| claude | `~/.claude/skills` | kullanıcı (bağlar, gerçek klasörler), HyperFrames | boşaltılacak (istisnalar kalacak) |
| agents | `~/.agents/skills` | `skills` aracı, HyperFrames | boşaltılacak |
| kilit | `~/.agents/.skill-lock.json` | `skills` aracı, HyperFrames | boşaltılacak (taşınır) |
| codex | `~/.codex/skills` | Codex, eski HyperFrames bağları | bağlar boşaltılacak; `playwright` ve `.system` kalır |
| gemini, cursor, copilot | `~/.gemini/skills`, `~/.cursor/skills`, `~/.copilot/skills` | HyperFrames aynası | boş olmalı |
| gemini-* | `~/.gemini/*/skills` (antigravity, antigravity-cli, config ...) | araç kendisi | kalacak (boşaltma adımlarında yok) |
| komutlar, ajanlar | `~/.claude/commands`, `~/.claude/agents` | kullanıcı | kalacak (yalnız var mı bakılır) |
| talimat | `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`, `~/.copilot/copilot-instructions.md` | kullanıcı | kalacak (içeriğine bakılmaz) |
| kesif-* | bilinmeyen `~/.<ad>/skills` | bilinmiyor | kalacak; araç mı değil mi kullanıcı karar verir |

Hiç izlenmeyenler ("KALIR, izlenmiyor"): `~/.openmontage` (programın kendi ağacı; `program-denetim.py` bakar), eklenti klasörleri
(`~/.claude/plugins`), `~/.config/openmontage`. Bunlar onaylı program güncellemelerinde meşru olarak değişir.

**Kalıcı satıcı girdileri** (tabanda `izinli`; YENİ/KAYIP/DEĞİŞTİ üretmez): `~/.claude/skills/synced` (Claude uygulamasının hesap skili
senkronu), `~/.codex/skills/.system` (Codex'in yerleşik skilleri), `~/.cursor/skills-cursor` (Cursor'un yerleşik skilleri). Yenisini eklemek:
kullanıcı onayıyla taban dosyasındaki `izinli` listesine satır ekle, sonra `--taban-yaz --yenile --evet` (onay gerekir).

## Her gün kullanım

```
python3 araclar/genel-bekci.py              # rapor; makineye yazmaz (kütüphanede notlar/genel-bekci.md güncellenir; yazmasın istersen --rapor-yok)
python3 araclar/genel-bekci.py --ayrinti    # bölge sayıları ve hâlâ duran boşaltılacak girdiler
python3 araclar/genel-bekci.py --ozet-json  # tek satır JSON (oturum başı ve aylık zincir)
python3 araclar/genel-bekci.py --siki       # yalnız durum "sorun" ise çıkış kodu 1
```

Satırlar: `YENİ` (tabanda olmayan girdi), `KAYIP` (kalacak girdi yok), `DEĞİŞTİ` (bağ hedefi, klasördeki dosya sayısı/boyutu ya da kilit dosyası
değişti), `KIRIK BAĞ`, `YENİ KLASÖR` (tabanda olmayan skill klasörü). Durumlar: `temiz` (beklenen durum), `dikkat` (bakılacak şey var,
acil değil), `sorun` (tabanda olmayan skill/kilit girdisi ya da `HYPERFRAMES_SKIP_SKILLS` satırı eksik). Boşaltılacak girdilerin durması
beklenen durumdur ("boşaltılacak girdi duruyor: N") ve `temiz` sayılır.
Taban dosyası (`notlar/genel-klasor-tabani.json`) yoksa `TABAN YOK` (dikkat) görünür; ilk taban kullanıcı onayıyla yazılır:
önce `python3 araclar/genel-bekci.py --taban-yaz` (kuru çalışma, hiçbir şey yazmaz), sonra onay gelirse `--evet` eklenir.
Ortam kontrolü yalnız şunu söyler: `HYPERFRAMES_SKIP_SKILLS satırı: 3 dosyanın 3'ünde var.` (`~/.zshenv`, `~/.zshrc`, `~/.claude/settings.json`).
Değeri, başka satırları ve anahtarları hiçbir çıktıda göstermez.

## Boşaltmadan önce kararlanacaklar

Her soruyu kullanıcı yanıtlar; yanıtlar `notlar/kararlar.md`'ye (yoksa `DURUM.md`'ye) yazılır. 2. adımdan öteye bunlar yanıtlanmadan geçilmez.

1. Q1 `openmontage` giriş skili nerede yaşasın? Seçenekler: (A) `~/.claude/skills/openmontage` tek istisna olarak kalsın (taban: `--kalacak`), (B) kütüphaneye taşınıp projeye kurulsun, (C) yalnız slash komutu olsun. Öneri A.
2. Q2 Dört slash komutu (`animated-drawing`, `backlot`, `ink-art`, `openmontage`) `~/.claude/commands`'ta kalır; `~/.claude/skills/...` gösteren metinleri `~/.openmontage/...` olarak düzeltilir (dosya başına onay).
3. Q3 Genel `~/.claude/CLAUDE.md` içindeki "~80 bağlı skill her oturumda yüklenir" cümleleri yeniden yazılır; `global-skill-links.txt` eski kayıt olarak kalır.
4. Q4 HyperFrames'in emekli skilleri (`hyperframes-core`, `-animation`, `-creative`, `-keyframes`, `-audio`, `motion-graphics`): kütüphaneye mi, projede dondurulmuş kopya mı. Adım 5b'yi engeller.
5. Q5 `youtube-arama`, `nlm-skill` ve 142 dosyalık `design-dna` nereye gitsin.
6. Q6 Codex, Claude'a geçen projede kullanılacak mı; projede kopya kalacak mı.
7. Q7 `~/.codex/skills/playwright` kalır (kalacak); `~/.claude/skills/.trash` bırakılır (öneri) ya da temizlenir.
8. Q8 `~/.palmier/skills` ve `~/.gemini/config/skills` hangi araca ait; kapsamda mı yoksa yoksayılsın mı (karar sonrası `izinli`/`ek_klasorler`).
9. Q9 Kabul edilmiş kırılma (karar verildi): "Psikolojik Danışman Sosyal Medya" ve "Istatistik template/Arkadasa-Gonderilecek/KIT" için işlem yapılmaz, engel sayılmaz; genel skill çağrıları boşaltmadan sonra çalışmaz. Bekçi bunları hiç listelemez.

## Hazırlık (adım 0)

Hepsi komutla doğrulanır; biri tutmuyorsa başlanmaz.
- Kütüphane ağacı temiz ve işlenmiş: `git status --short` boş.
- Taban yazılmış ve işlenmiş (`notlar/genel-klasor-tabani.json`) ve `python3 araclar/genel-bekci.py` = `temiz`.
- Proje kapısı kararları (Q4-Q6) verilmiş; `CLAUDE.md`/`AGENTS.md` kural-1 istisnası onaylanmış ve işlenmiş.
- Açık kalan okumalar bitmiş: 5 zamanlanmış görev, `~/.claude/bin`, `plugin-sources`, `marketplaces`, `~/Library` (`DURUM.md` "Hâlâ okunmadı").
- Başka oturum çalışmıyor; gün adıyla sabit bir yedek klasörü var (`~/Documents/Claude/yedek/genel-klasorler-<YYYY-AA-GG>/`).
- Yedek için yer var: `df -h ~` 1 GB'den fazla boş gösterir.

## Adımlar

Komutlar elle yazılmaz: `python3 araclar/genel-bekci.py --plan <adım>` çıktısı kullanıcıya gösterilir, "evet" gelince çalıştırılır.
Plan önkoşulları sağlanmazsa (`DURDUR`: taban yok, rapor `sorun`, önceki adım bitmemiş, bağımlı bağ var) hiç komut üretmez.
Her adımda: Amaç, Sıra nedeni, Yedek, Komut, Kontrol, Geri alma, Onay.

### Adım 1 Anahtar (hiçbir şey kaldırılmaz)
- Amaç: `HYPERFRAMES_SKIP_SKILLS=1` üç yerde de var.
- Sıra nedeni: ilk iş bu; çünkü boşaltmadan sonra HyperFrames `init`/`skills`/`update` çalışırsa skilleri yeniden yazar.
- Kontrol: rapor satırı `3 dosyanın 3'ünde var`. Eksikse hangi dosya olduğunu söyle; kabuk ya da ayar dosyasını ajan kendisi düzenlemez, kullanıcı karar verir.
- İsteğe bağlı, ayrı onay: Dock'tan açılan uygulamalar için `launchctl setenv HYPERFRAMES_SKIP_SKILLS 1` (yeniden başlatmada kalmaz; yalnız Dock uygulamasının yazdığı görülürse).
- Onay: ONAY GEREKİR (ayar dosyasına satır eklenecekse).

### Adım 2 Giriş yerleri (kullanıcı dosyaları; her biri ayrı onay)
- Amaç: 2a `openmontage` giriş skili, 2b dört slash komutu, 2c genel `CLAUDE.md` satırları (Q1-Q3 kararlarına göre).
- Sıra nedeni: her klasörde `openmontage` yüklenmesini söyleyen yerler bunlar; 4. adım önce çalışırsa video istekleri sessizce başarısız olur.
- Yedek: her dosyanın kopyası `$YEDEK/giris/` altına. Kontrol: temp klasörden başlatılan yeni oturumda "openmontage skilini oku" çalışır. Bekçi düzenlenen dosyalar için bir şey söylemez (içerik izlenmez).
- Geri alma: dosyayı `$YEDEK/giris/` içinden geri kopyala. Onay: ONAY GEREKİR (her dosya için ayrı).

### Adım 3 Codex bağları (`--plan 3`)
- Amaç: `~/.codex/skills` içindeki HyperFrames/Claude bağlarını kaldırmak (`playwright` ve `.system` kalır).
- Sıra nedeni: bu bağlar `~/.claude/skills` ve `~/.agents/skills` içine gider; hedefler önce giderse Codex klasöründe kırık bağ kalır.
- Yedek: bağ listesi (yol ve hedef, `readlink`) `bag-listesi-codex.tsv`; yalnız bağın kendisi `rm --` ile gider (`-r` yok).
- Kontrol: `python3 araclar/genel-bekci.py --yedek-dogrula "$YEDEK"` ve `python3 araclar/genel-bekci.py`. Geri alma: tsv'den `ln -s` döngüsü (çakışmayı atlar, bildirir). Onay: ONAY GEREKİR.

### Adım 4 `~/.claude/skills` bağları (`--plan 4`)
- Amaç: bağları kaldırmak (yaklaşık 81).
- Sıra nedeni: bağlar listeden kayıpsız geri yazılır, bu yüzden gerçek klasörlerden önce gider; `~/.agents/skills`'e giden bağlar 6. adımdan önce temizlenir. `~/.openmontage` ağacına dokunulmaz.
- Yedek/Kontrol/Geri alma: adım 3 gibi (`bag-listesi-claude.tsv`). Geri yazma `global-skill-links.txt`'den değil tsv'den yapılır (o dosya eski). Onay: ONAY GEREKİR.

### Adım 5a HyperFrames kopyaları, 5b diğer gerçek klasörler (`--plan 5a`, `--plan 5b`)
- Amaç: 5a sahibi `hyperframes` olan gerçek klasörler (HyperFrames sürümünden ve kütüphaneden yeniden üretilir); 5b geri kalan gerçek klasörler.
- Sıra nedeni: 5b yalnız Q4-Q6 kararlarından sonra; projeler bu skillerden bazılarını okuyor.
- Yedek: klasörler `mv` ile `$YEDEK/claude-skills/` içine taşınır (aynı diskte atomik; planın ilk komutu aynı disk kontrolüdür, farklıysa durur). Taşınan klasörün dosya sayısı ve boyutu `--yedek-dogrula` ile tabandaki sayılarla karşılaştırılır; bu doğrulama geçmeden sonraki adıma geçilmez, çünkü yedek tek kopyadır.
- Geri alma: klasörü tek tek `mv` ile geri koy (planın geri alma satırları çakışmayı denetler). Onay: ONAY GEREKİR (5a ve 5b ayrı).

### Adım 6 `~/.agents/skills` ve skill kilit dosyası (`--plan 6`)
- Sıra nedeni (en son): `skills` aracı ve HyperFrames kilidi "kurulu" sayar; klasörler gidip kilit kalırsa sonraki `npx skills` bayat kayıtlardan yeniden kurar; kilit önce giderse neyin kurulu olduğu görünmez olur. Buraya giden bağlar 3-4. adımlarda gitmiştir.
- Boş `skills` klasörleri yerinde bırakılır (bekçi onları izler; HyperFrames aynası zaten yeniden yaratır).
- Yedek: kilit dosyasının önce `cp -p` kopyası, sonra `mv` (yarım kalmış taşımaya karşı iki kopya). Onay: ONAY GEREKİR.

### Adım 7 Kapanış (`--plan 7`)
- Aynalar (`~/.gemini/skills`, `~/.cursor/skills`, `~/.copilot/skills`, antigravity klasörleri) boş ya da yok mu: `--ayrinti`.
- Tabanı yenile: `python3 araclar/genel-bekci.py --taban-yaz --yenile --evet` (ONAY GEREKİR; "kabul edildi" listesi gösterilir; Q1/Q7 istisnaları için `--kalacak YOL`). Sonuç `temiz` olmalı.
- Kütüphane commit'i (onayla); yedek kaydı ve silme hatırlatması aynı gün (aşağıda); `DURUM.md`, `rehber/02`, `README.md` boşaltma satırları güncellenir (ayrı onay); açık Claude ve Codex oturumları yeniden başlatılır (eski skill listesini tutarlar).

**Tüm süreci geri alma sırası:** 6, 5b, 5a, 4, 3 (klasörler bağlardan önce; geri konan bağlar kırık kalmaz), sonra 2. adımdaki dosyalar. Sonunda bekçi tabanla aynı olmalı (`temiz`).

## Geri yazma: kim yazabilir, nasıl yakalanır

| Yazan | Nereye | Nasıl durur | Bekçi nasıl görür |
|---|---|---|---|
| HyperFrames `init`, `skills`, `skills update`, `update` | `~/.claude/skills`, `~/.agents/skills`, kilit, aynalar | `HYPERFRAMES_SKIP_SKILLS=1` (Dock uygulamaları kapsanmaz) | YENİ |
| `npx skills add -g` | `~/.agents/skills`, kilit | anahtar durdurmaz; bazı skill metinlerinde geçer | YENİ |
| Claude uygulaması (`synced`), Codex (`.system`, `playwright`), Cursor (`skills-cursor`) | kendi klasörleri | izinli | görünmez |
| Elle ya da ajanla `cp`/`ln` | herhangi biri | kural 1 | YENİ |
| Antigravity ve benzeri yeni araç klasörü | `~/.gemini/*/skills`, `~/.<ad>/skills` | - | YENİ KLASÖR |
| Time Machine / başka Mac'ten geri yükleme | her yer | - | her yerde YENİ/KAYIP: önce tam raporu oku |
| VS Code uzantıları, kabuk dosyasını yeniden yazan kurulum betikleri | aşağıdaki bölüm | aşağıdaki bölüm | YENİ (karar metninde `yazan`), anahtar satırında ipucu |

## Genel alana kendiliğinden yazan uygulamalar

Bekçi bunları tanır: YENİ girdinin karar metnine `yazan: ...; durdurmak: ...` eki gelir, `--ayrinti` uzantı kimliğini ve kanıtın yerini ekler.
Tek kaynak `araclar/genel-bekci.py` içindeki `BILINEN_YAZICILAR` tablosudur; aşağısı onun açıklamasıdır. Durdurma her zaman kullanıcı onayıyla yapılır (ayar dosyası).

| Uygulama | Ne yazar, ne zaman | Tanıma ölçütü | Kalıcı durdurma | Kanıt |
|---|---|---|---|---|
| VS Code **Foundry Toolkit** (`ms-windows-ai-studio.windows-ai-studio`) | `~/.agents/skills/microsoft-foundry` ve kilit (kaynak `microsoft/azure-skills`); her etkinleşmede skill yoksa kurar (2026-11-13 olayı) | ad `microsoft-foundry` (kilit olsa da olmasa da) | VS Code kullanıcı ayarı `"windowsaistudio.autoCheckFoundrySkill": false` (2026-11-14'te yazıldı) | `~/Library/Application Support/Code/logs/<oturum>/window1/exthost/ms-windows-ai-studio.windows-ai-studio/Foundry Toolkit.log` içinde `[FoundrySkill] ... Installing` |
| VS Code **GitHub Copilot for Azure** (`ms-azuretools.vscode-azure-github-copilot`) | 30 günde bir "Azure skills kurayım mı?" diye sorar; "Install" denirse `microsoft/azure-skills` skillerini `~/.agents/skills` içine (adlar kurulum anında uzaktan listelenir), `~/.github/hooks/azureSkills*` ve `~/.agents/.copilot-for-azure-skills-manifest.json` yazar | kilitte kaynak `microsoft/azure-skills` (ad ne olursa olsun) ya da ad manifestin `skills` listesinde | bildirimde "Don't Ask Again" (uzantının ayarı yok); tuttuğu: `~/Library/Application Support/Code/User/globalStorage/ms-azuretools.vscode-azure-github-copilot/skills-state.json` içinde `toastDismissedPermanently: true` | manifest dosyası; `.../exthost/ms-azuretools.vscode-azure-github-copilot/@azure.log` |
| Kabuk dosyasını yeniden yazan kurulum betiği (2026-11-14: başka bir programın `# >>> ... >>>` kurulum bloğu eklenirken `~/.zshrc` yeniden yazıldı) | `HYPERFRAMES_*` kilit bloğunu siler | anahtar satırı `EKSİK: ~/.zshrc (satır yok)` ya da `~/.zshenv`; satıra "kurulum betiği" ipucu eklenir | satırlar dosyanın sonuna geri eklenir (onayla); sonra bekçi "3 dosyanın 3'ünde var" demeli | dosyanın değişme saati ve yeni eklenen blok |

Not: `microsoft-foundry` `microsoft/azure-skills` deposunda da var; Copilot for Azure kurulumu da onu yazabilir. Ad Foundry Toolkit'e bağlanır; manifest varsa iki uzantıya da bak.
Manifest ve `~/.github/hooks` bekçinin izlediği yerler değildir (yalnız tanıma için okunur); Copilot for Azure skilleri geri gelirse bu dosyalar da onayla temizlenir.

**Tabloya yeni yazıcı eklemek:** `BILINEN_YAZICILAR` içine bir satır (`adlar` ya da `kaynak`/`manifest`, `yazan`, `durdur`, `kimlik`, `kanit`; karar satırı 300 karakteri aşmasın)
ve `araclar/testler/test_p2-genel-bekci.py` içine sahte ev testi; sonra bu tabloya bir satır. Kanıtsız yazıcı eklenmez: önce günlükte ya da uzantı kodunda yazan yeri bul.

## Bir şey yeniden belirirse

1. Hiçbir şeyi silme. `python3 araclar/genel-bekci.py --ayrinti` çalıştır.
2. Girdinin `sahip`ine ve rapordaki anahtar satırına bak (kilit kaynağı sahip sütunundan anlaşılır; geçmiş dosyaları okunmaz). Karar metninde `yazan:` eki varsa yazan ve durdurma yolu "Genel alana kendiliğinden yazan uygulamalar" bölümündedir; yoksa yazanı bul ve o tabloya ekle.
3. Kullanıcıya seçenekleri sun: (a) istenmeyen yazıcı: önce nedeni durdur (anahtar, talimat metni), sonra onayla girdiyi `~/Documents/Claude/yedek/geri-yazilan-<YYYY-AA-GG>/` içine bağ listesiyle taşı (ONAY GEREKİR); (b) istenen skill: bir projeye aittir, `skill-ekle.py` ile kurulur, genel klasöre değil; (c) kalıcı satıcı girdisi: taban `izinli` listesine eklenir, sonra `--taban-yaz --yenile --evet` (onay gerekir).
4. Raporu yeniden çalıştır: `temiz` olmalı.
5. Aynı şey ikinci kez geri gelirse yazıcıyı açık sorun olarak kullanıcıya bildir; döngüye girme.

## Yedek silme hatırlatması

Boşaltmanın son günü aynı gün: `yedekler.json` satırı (yol `~/Documents/Claude/yedek/genel-klasorler-<tarih>/`, tür `genel-klasor`, silme tetiği "30 gün geçince VE kullanıcı sil deyince") ve
tek seferlik zamanlanmış hatırlatma önerilir (ONAY GEREKİR; metni `--plan 7` çıktısındadır). Süre dolunca: önce bekçi `temiz` mi bak, sonra kullanıcıya "Yedeği silelim mi?" diye sor;
açık "evet" gelmeden hiçbir şey silinmez. Önceki iki yedek (`global-skills-2026-11-08`, `ayar-2026-11-11`) için de aynı kural geçerlidir; `ayar-2026-11-11` içinde düz metin anahtar satırı olabilir, hatırlatırken içeriği yazdırma.

## Yeni bir yapay zeka aracı eklenince

Aracın genel skill klasörü kullanıcı onayıyla taban dosyasındaki `ek_klasorler` listesine eklenir (`rehber/14-yapay-zeka-araclari.md`);
unutulursa bekçi o klasörü `YENİ KLASÖR` olarak bildirir. Sonra `python3 araclar/genel-bekci.py` temiz olmalıdır.

## İlgili dosyalar

`araclar/genel-bekci.py` (araç), `notlar/genel-klasor-tabani.json` (taban; onayla yazılır), `notlar/genel-bekci.md` (rapor), `promptlar/16-genel-klasor-bosaltma.md`,
`rehber/13-yedek-ve-geri-alma.md`, `rehber/11-program-yonetimi.md`, `notlar/hf-om-gecisi/DURUM.md`.
