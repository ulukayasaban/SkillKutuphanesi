# DURUM (her oturum önce bunu okur)

Son güncelleme: 2026-11-11

Bu klasördeki **tek geçerli not** budur. Eski planların ikisi de `rafta/` içinde; hiçbiri uygulanmaz.

## Hedef
Bilgisayarın genelindeki skill klasörleri boşaltılacak; skiller yalnız bu kütüphaneden, yalnız proje klasörüne kurulacak.
HyperFrames ve OpenMontage **programları** yerinde kalır; taşınan sadece skillerdir. Her kaldırmadan önce yedek alınır.

## İki kapı (kullanıcı söylemeden açılmaz)
| Kapı | Açan söz | O zamana kadar |
|---|---|---|
| HyperFrames, OpenMontage, genel skill klasörleri, ayar dosyaları | "işim bitti" (2026-11-11 söylendi, AÇIK) | Her değişiklik ayrı onayla |
| Proje klasörleri (tarama, düzenleme, Akıl Dışı'nın Claude'a geçişi) | "başla" (2026-11-11 söylendi, AÇIK) | Tarama okuma; her kurulum, kaldırma, taşıma ayrı onayla |

Tek istisna: kütüphanenin kendi rutin kontrolleri (`dogrula.py`, `test.py`, `proje-kullanimi.py`) her projenin
`.skill-kutuphanesi/kilit.json` dosyasını okur; yazmaz.

## Kararlar (tarihli)
- 2026-11-09: 27 eski genel skill yedeğe taşındı (`~/Documents/Claude/yedek/global-skills-2026-11-08`). Yedek, kullanıcı "sil" diyene kadar durur.
- 2026-11-10: Genel klasörler boşaltılacak (önceki "skiller yerinden oynamaz" kararının yerini aldı).
- 2026-11-10: Akıl Dışı Codex'ten Claude'a geçer; geçişi proje içinde kütüphane oturumu yapar.
- 2026-11-10: Proje taraması kullanıcı kendi işini bitirip haber verince başlar.
- 2026-11-10: HyperFrames, OpenMontage ve benzeri yapıların takibi, kontrolü ve güncellemesi kütüphane oturumunda; her güncelleme ayrı onayla.
- 2026-11-10: Diğer araçların genel talimat dosyalarına kural yazılmaz; hazır metin de verilmez.
- 2026-11-10: Yedek silme zamanı gelince kullanıcıya hatırlatılır. Hatırlatma, genel klasörler gerçekten boşaltıldığı gün kurulur.
- 2026-11-10 gece: "Bunlara dokunmadan yapman gerekenleri yap" → 1. adım (kütüphane içi hazırlık) onaylandı.
- 2026-11-11: Kullanıcı "işim bitti" dedi → 1. kapı AÇIK (HyperFrames, OpenMontage, genel skill klasörleri, ayar dosyaları).
  Bu söz toplu onay değildir: her güncelleme, kaldırma, taşıma ve ayar değişikliği önce yedek, sonra ayrı onayla yapılır.
  Proje kapısı ("başla") KAPALI.
- 2026-11-11 (aynı akşam): Kullanıcı "işlemlerimi bitirdim … proje kapısı başla" dedi → 2. kapı da AÇIK. Proje taraması (salt okuma)
  başladı. Bu söz de toplu onay değildir: projeye kurulum raporu görülüp onaylanınca, her kaldırma ve ayar değişikliği ayrı onayla.
- 2026-11-11 (gece): Kullanıcı "koymamız gerekiyorsa koy" dedi → `HYPERFRAMES_SKIP_SKILLS=1` iki yere yazıldı:
  `~/.zshrc` (son satır) ve `~/.claude/settings.json` → `env`. Yedek: `~/Documents/Claude/yedek/ayar-2026-11-11/`
  (`zshrc.yedek`, `claude-settings.json.yedek`; geri almak = yedeği yerine kopyalamak). Doğrulandı: yeni terminal görüyor, JSON geçerli,
  iki dosyada da yalnız bu satır değişti. AÇIK: terminal açmadan çalışan kabuklar (`zsh -c`, `zsh -lc`; Codex, Antigravity) `~/.zshrc`
  okumaz, ayarı görmez. Kapatmak için aynı satır `~/.zshenv`'e gerekir (dosya var); kullanıcıya soruldu, onay bekliyor.
  Açık Claude oturumları ayarı yeniden başlayınca görür.
- 2026-11-11 (gece, devam): Kullanıcı "eklememiz gerekiyorsa ekle" dedi → aynı satır `~/.zshenv` sonuna da yazıldı (yedek aynı klasörde
  `zshenv.yedek`). Doğrulandı: temiz ortamda `zsh -c` ve `zsh -lc` ikisi de `SKIP=1` görüyor. Kalan tek açık: Dock'tan açılan ve kabuk
  başlatmadan süreç çalıştıran uygulamalar (nadir); gerekirse `launchctl setenv`, ayrı onayla.
- 2026-11-11 (gece, devam): Kullanıcı yeniden başlatma zamanını benden bekliyor ("bana yeniden başlatmam gereken zamanı söyle"). Söylenecek an:
  arka plan işleri bitip kütüphane commit edildikten sonra. Kullanıcı ayrıca şunu istedi: bütün düzen kullandığı tüm yapay zeka araçlarında
  çalışacak; skill, kütüphane, güncelleme, proje takibi, git takibi, aylık takip, ekleme ve silme akışlarının hepsi eksiksiz ve sürdürülebilir
  kurulacak; HyperFrames ve OpenMontage gibi programların kurulumu da buradan yönetilecek. O sırada Claude'da başka oturum çalışmıyor.
  Çalışma sırası: boşluk denetimi (akışlar + araç uyumu) → tasarım → uygulama → inceleme. Çalışma kâğıtları scratchpad `plan/`.

## Adım çizelgesi
**2026-11-12: 2., 3. ve 4. adımlar TAMAMLANDI** (program güncellemeleri; genel klasörlerin boşaltılması K-40; proje geçişleri K-38 IstatistikYoutube, K-41 Akıl Dışı). Aşağıdaki satırlar o günün öncesini anlatır; kalan işler "Düzen denetimi" bölümündeki "GÜNCEL (2026-11-12 08:40)" notundadır.

| Adım | İş | Kapı | Durum |
|---|---|---|---|
| 1 | Kütüphane içi hazırlık: skillerdeki sabit genel yol / eklenti kökü / kardeş yol taraması, kurulumda yol çevirisi, yeni ön kontrol kodları, aylık zincire yol ve program denetimi | yok (onaylı) | bitti (2026-11-11; özet `1-adim-kalan-is.md`) |
| 2 | HyperFrames ve OpenMontage program kartları; güncelleme (önce yedek, her biri ayrı onay) | "işim bitti" | kartlar ve "yerinde" kart türü yazıldı (2026-11-11); anahtar üç yere kondu (`~/.zshenv`, `~/.zshrc`, `settings.json`); güncellemeler onay bekliyor (HF 0.9.23 → 0.9.33, OM 244 commit geride) |
| 3 | Genel klasörleri boşaltma (yedek, her kaldırma ayrı onay); aynı gün yedek silme hatırlatması | "işim bitti" | başlamadı; önce 4. adımdaki bağımlılıklar çözülür |
| 4 | Proje taramaları, projelerde `--guncelle --kuru` önizlemesi, Akıl Dışı'nın Claude'a geçişi | "başla" | kayıtlı 5 proje ve kayıtsız klasörler + Claude sistem dosyaları tarandı (2026-11-11); küçük açıklar aşağıda; kurulum ve geçiş onay bekliyor |

## Ölçülen durum (2026-11-10, sadece okuma)
- `~/.claude/skills`: 105 girdi (81 bağlantı + 24 gerçek klasör). `~/.agents/skills`: 27 skill. `~/.codex/skills`: 11 bağlantı.
- Kurulu HyperFrames 0.9.23. OpenMontage `~/.openmontage` main dalında.

## Yeniden ölçüm (2026-11-11 akşam, sadece okuma; 1. kapı açıldıktan sonra)
- Genel klasörler: `~/.claude/skills` 75 OpenMontage bağlantısı + 6 göreli bağlantı (`~/.agents`'e) + 17 HyperFrames gerçek kopyası +
  4 kişisel/başka (`openmontage`, `youtube-arama`, `nlm-skill`, `design-dna`) + `synced/` (Claude uygulamasının, dokunulmaz).
  `~/.agents/skills` 28 klasör (yeni: `microsoft-foundry`, 2026-11-11 04:07, `skills` aracıyla; kütüphanede yok).
  `~/.codex/skills` 11 bağlantı + `playwright` + `.system` (Codex'in, dokunulmaz).
- HyperFrames: kurulu 0.9.23, son 0.9.33. Skilleri genel klasöre `init` / `skills` / `update` komutları yazar; kurulum ve render yazmaz.
  Durduran anahtar `HYPERFRAMES_SKIP_SKILLS=1`, hiçbir yerde tanımlı değil. Ayna hedefleri: `~/.gemini/skills`, `~/.cursor/skills`,
  `~/.gemini/antigravity/skills` (klasör varsa). Tek dosya her başlatıcıyı kapsamaz (terminal `~/.zshrc`, Claude `settings.json` env).
- OpenMontage: yerel `c806645` (2026-10-16), uzak 244 commit ileride; 9 izli dosyada yerel değişiklik, 6 izlenmeyen yol;
  yerel `origin` eski adı gösteriyor. Genel bağlantıları OM kurmuyor (elle, 2026-09-08); güncelleme yeniden oluşturmaz.
- Yalnız genelde duran içerik: HyperFrames'in artık dağıtmadığı 14 skill + `hyperframes-media`, `website-to-video`; `design-dna`
  genel kopyası kütüphanedekinden 134 dosya fazla. Bunlar kullanım doğrulanmadan ve yedek geri yüklenebilir görülmeden silinmez.
- Sonuç: gerçek silmelerin çoğu proje kapısına bağlı (hangi projenin neye dayandığı okunamıyor). 1. kapıyla yapılabilenler:
  program kartları, güncellemeler, geri yazmayı durduran anahtar, `openmontage` giriş skili ile komut yollarının yeni yeri.
- Boşaltma sırası (taslak): anahtar → giriş skili ve komut yolları → Codex bağlantıları → `~/.claude` bağlantıları (liste
  yedeğinden geri alınır, manifestten değil) → `~/.claude` gerçek klasörler → `~/.agents` (kilit dosyasıyla). Son üçü proje kapısından sonra.
- Ayrıntı (çalışma kâğıdı, kalıcı değil): oturum scratchpad `adim23/`.
- Yan gözlem (bu işten bağımsız): `~/.zshrc` içinde düz metin bir API anahtarı satırı var; değer okunmadı. Anahtar konusu açılınca kullanıcıya söylenecek.

## Proje taraması (2026-11-11 gece, sadece okuma; kayıtlı 5 proje)
- **Genel klasörlere bağlı değil:** AntigravityTest2 (9 skill), Etsy-Yeni (31), Etsy-Arif (27 kütüphane + 10 elle; elle olanlara dokunulmaz).
  Güncelleme önizlemesi: AntigravityTest2 ve Etsy-Arif'te birer `ui-ux-pro-max` yol çevirisi önerisi; Etsy-Yeni'de değişiklik yok.
- **Bağlı: IstatistikYoutube.** Genelden 8 skill okuyor (`status/skill-global.yaml`): hyperframes, hyperframes-cli, hyperframes-animation,
  hyperframes-core, motion-graphics, design-dna (142 dosyalı genel kopya), openmontage, nlm-skill. Boşaltınca kırılacak yerler:
  `video_dna.py:18`, `kapak_dna_kontrol.py:14`, `skill_durum.py` kapısı, `hyperframes-shorts/SKILL.md:22`.
- **Bağlı: Akıl Dışı.** Codex düzeninde (`AGENTS.md` + `.codex/config.toml` + 7 `akil_*.toml`, her birinde 8 sabit skill yolu; 4'ü zaten yok).
  Genelden okuduğu: hyperframes-creative, -animation, -keyframes, -audio, hyperframes-registry, captions-overlay, motion-doctrine, seam-craft,
  talking-head-recut (yalnız `gsap.min.js`), hyperframes, imagegen (Codex'e özgü, Claude karşılığı yok). 8 kendi `akil-disi-*` skili kilitte değil.
- **Kullanıcı kararı bekleyenler:** HyperFrames'in artık dağıtmadığı eski skiller (hyperframes-core, -animation, -creative, -keyframes, -audio,
  motion-graphics) kütüphaneye mi alınacak, projede donmuş kopya mı kalacak; `openmontage`, `nlm-skill`, `youtube-arama`, 142 dosyalı `design-dna`
  nerede yaşayacak; Akıl Dışı geçişten sonra Codex'i de kullanacak mı.
- Ayrıntı (çalışma kâğıdı, kalıcı değil): oturum scratchpad `proje/` (ilk tarama), `proje2/` (boşluk taraması).

## Boşluk taraması (2026-11-11 gece, sadece okuma; kayıtsız klasörler, Claude sistem dosyaları, başlatıcılar, ev geneli)
- **Genel klasörlere bağlı değil:** IsBasvuruClaude (20 skill, bağlantılar proje içi), Yetisio, Tekfen Araştırma Sonuçları (346 kopya skill),
  CrmProject2, LinkedinSabanIsBasvurusu, OyleSaniyordukChatGpt, MacBilgisayarTemizleme, Oyak-OrduPazariNew, NewTetraTarim, EtsyEski, Kantin,
  `Documents/Codex/.../ECommerceProject`, LaunchAgents (plistler skill okumuyor; biri `~/.openmontage` venv'ini kullanıyor, program kalıyor).
- **Bağlı: Psikolojik Danışman Sosyal Medya.** `youtube-arama` skilini genelden okuyor (`.claude/agents/rakip-analisti.md:17`). Ayrı kırıklık
  (boşaltmadan bağımsız): OpenMontage için sabit `~/Documents/OpenMontage` yolunu gösteriyor, bu klasör diskte yok.
- **Bağlı: `Documents/Istatistik template/Arkadasa-Gonderilecek/KIT`** (eleştiri okumasında bulundu). `KURULUM.md:34-36` skilleri
  `~/.claude/skills` altına kurduruyor; `hyperframes-shorts/SKILL.md:15-29` hyperframes-core, motion-doctrine, motion-design, design-dna çağırıyor.
  Bu bir dağıtım paketi (başkasına gönderilecek); nasıl ele alınacağı kullanıcıya sorulacak.
- **KARAR (kullanıcı, 2026-11-11 gece):** Psikolojik Danışman Sosyal Medya güncel kullanılmıyor, İstatistik KIT paketi de önemli değil.
  İkisinde de **işlem yapılmaz** (kurulum, düzeltme, yeniden tarama yok); boşaltmayı engellemezler. Boşaltınca bu ikisinde genel skil
  çağrıları çalışmaz, kullanıcı bunu bilerek kabul etti. Psikolojik'in `Vault`/`Uretim` içleri için son tarama da gerekmez.
- **Bağlı: `~/.claude` kendisi.** `CLAUDE.md:4,6` ve `commands/openmontage.md`, `ink-art.md`, `animated-drawing.md` `openmontage` skilini ve
  ~80 OpenMontage skilini genelden bekliyor. Boşaltmadan önce bu satırların ve komutların yeni yeri kararlaştırılır (kullanıcı onayı).
- **Pasif:** `Documents/IstatistikYoutube-Arsiv/kaldirilan-sistemler-2026-10-19/` genel yolu anıyor (arşiv; çalıştırılırsa kırılır).
- **Hâlâ okunmadı (küçük açık):** 5 zamanlanmış görevin içeriği (colab-*, kopru-*), `~/.claude` altında `bin`, `plugin-sources`, `marketplaces`,
  Psikolojik projesinin `Vault`/`Uretim` içleri, `~/Library`. Boşaltma gününden önce kısa bir son tarama yapılır.
- Düzeltme: bir alt okuma "`~/.codex/skills` yok" dedi; yanlış. Aynı gece yeniden bakıldı, klasör duruyor (13 girdi).

## Düzen denetimi (2026-11-11 gece, sadece okuma; kullanıcının geniş isteği)
İstek: bütün düzen, kullanılan tüm yapay zeka araçlarında çalışsın; skill ekleme/silme, güncelleme, proje takibi, git takibi,
aylık takip ve HF/OM gibi programların kurulum/güncelleme yönetimi eksiksiz ve sürdürülebilir olsun.
- Sıra: boşluk denetimi (BİTTİ) → tasarım (BİTTİ 2026-11-11 gece) → uygulama (kütüphane içinde; 2026-11-11 21:45'te BAŞLADI,
  kullanıcı "uygulamaya geç, başlat" dedi; Claude yeniden başlatıldı, anahtar oturumda görünüyor) → inceleme → üç kontrol → commit.
  Uygulama yarıda kalırsa: çalışma ağacındaki commit edilmemiş dosyalar yarım iştir; `git status` ile bak, paket sırasına göre devam et.
  ONAY (kullanıcı, 2026-11-11 gece, "evet ekle"): `CLAUDE.md` ve `AGENTS.md` sonuna yeni rehberleri gösteren yönlendirme satırları
  (Yama A) eklenecek; mevcut kurallar değişmez. Uygulama bitince hazırlanan metinle eklenir. Kural 1 istisnası (Yama B) bu onaya dahil DEĞİL.
  ONAY (kullanıcı, 2026-11-12 00:04, "openmontage güncelleme işlemlerini bu şekilde tamamlayalım"): OpenMontage güncellemesi
  `rehber/11` yoluyla yapılacak: önce yedek (`~/Documents/Claude/yedek/openmontage-2026-11-12/`), sonra AYRI deneme klasörü
  (`~/Documents/Claude/deneme/openmontage-<hedef>`; çalışan kuruluma dokunulmaz), yamalı dört dosya için kullanıcıya tek tek sorulur.
  Asıl kurulumun güncellenmesi bu onaya dahil DEĞİL: deneme geçince kullanıcıya yeniden sorulur. Uygulama işi kaydedildikten sonra başlar.
  UYGULAMA BİTTİ (2026-11-12 00:10): 8 paket yazıldı, incelendi; son test 312/312. Ardından onaylı işler yapıldı: `CLAUDE.md`/`AGENTS.md`
  Yama A + Yama B (kural 1 istisnası), üç eski belge `notlar/rafta/` altına, birleşmiş `skill/lottiefiles-motion-design` dalı silindi.
  TOPLU ONAY (2026-11-12, `notlar/kararlar.md` K-24..K-27): aşağıdaki işler sırası gelince yeniden sorulmadan yapılır (her birinde önce
  yedek; kontrol başarısızsa ya da durum anlatılana uymuyorsa dur ve sor). SIRA:
  1. Kütüphaneyi kaydet + push. 2. Gerçek veriye bağlı test iddiaları ve `test.py` izleme listesi düzeltmesi (aşağıda "Uygulamadan kalanlar").
  3. OpenMontage: yedek → deneme klasörü → (geçerse) asıl güncelleme → origin adresi. 4. HyperFrames güncellemesi + ek iki kilit.
  5. IstatistikYoutube. 6. Akıl Dışı (Codex → Claude). 7. Etsy-Arif: yalnız kütüphanenin kurduğu skiller. 8. Claude genel notu + üç komut.
  9. AntigravityTest2 → Çöp Kutusu (önce `projeler.json` kaydından çıkar). 10. Bekçi taban dosyası → tam yedek → sınıf sınıf boşaltma →
  yedek silme hatırlatması. 11. Aylık görev metni (Aşama 2) + canlı görev. 12. Son kontroller + push.
  DURUM 2026-11-12 03:20: 1 ve 2 BİTTİ (push edildi; test açıkları kapandı). 3 BİTTİ: OpenMontage `c8066452` → `fecb9a1e`
  (244 commit, yalnız ileri sarma); yedek `~/Documents/Claude/yedek/openmontage-2026-11-12/` (yedekten birebir geri dönüş sınandı);
  deneme klasörü `~/Documents/Claude/deneme/openmontage-fecb9a1e` duruyor (silinmedi). Kullanıcı kararı: `Explainer.tsx` ve
  `face_restore.py` yeni sürüm haliyle kaldı, eski yerel halleri yedekte; diğer 7 yerel değişiklik yerinde. Venv: yalnız certifi
  yükseldi, pythainlp + importlib_resources eklendi; 11 sabit sürüm aynı. 75 skill bağı sağlam, derleme ve programın kendi kontrolü
  hatasız; origin yeni adrese çevrildi. Kullanıcı kendi projesinde sınayacak ve sonucu söyleyecek; "yedekleri silme" dedi.
  Geri dönüş gerekirse: `rehber/11` → "Geri alma" + yedekteki `KAYIT.json`, `yerel-yamalar.patch`, `pip-freeze.txt`.
  4 BİTTİ (2026-11-12 03:45): HyperFrames 0.9.23 → 0.9.35 (`npm install -g hyperframes@0.9.35`, üç kilit tanımlıyken); sürüm notlarında
  kırıcı değişiklik yok; genel skill klasörleri güncelleme öncesi ve sonrası aynı. Yedek `~/Documents/Claude/yedek/hyperframes-2026-11-12/`.
  Ek iki kilit (`HYPERFRAMES_NO_AUTO_INSTALL`, `HYPERFRAMES_NO_UPDATE_CHECK`) `~/.zshenv`, `~/.zshrc`, `~/.claude/settings.json` içine
  eklendi; önceki halleri `~/Documents/Claude/yedek/ayar-2026-11-12/`. settings.json'daki yeni anahtarlar bir sonraki Claude oturumunda
  geçerli olur (acil değil). HyperFrames komutu çalıştırılarak sınanmadı; kullanıcı kendi projesinde sınayacak.
  YÖN DEĞİŞİKLİĞİ (K-28, 2026-11-12): programla gelen skiller projeye kopyalanmaz, programın kendi skill klasörüne BAĞLANIR
  (`skill-ekle.py --program-skill PROGRAM:AD`); yalnız genel klasörde kalan eski kuşak skiller projeye DONDURULUR (`--dondur YOL`).
  Bu iki yol kütüphaneye ekleniyor (tasarım `notlar/duzen-denetimi-2026-11/tasarim/tasarim-p9-program-skilleri.md`).
  HAZIRLIK BİTTİ (salt okuma, 2026-11-12): `notlar/hf-om-gecisi/istatistik-hazirlik-2026-11-12.json` ve
  `akildisi-etsyarif-harita-2026-11-12.json` (harita, sürüm karşılaştırması, adım listesi, karşı inceleme, kullanıcıya sorulacaklar).
  - IstatistikYoutube (git deposu değil; 23 kütüphane + 22 kendi skili zaten proje içinde): `hyperframes`, `hyperframes-cli` →
    HyperFrames paketine bağ; `hyperframes-core`, `-animation`, `-creative`, `motion-graphics` → dondur; `design-dna`, `openmontage`,
    `nlm-skill` kullanıcının, yerinde kalır; OpenMontage'ın bağlı skillerini proje kullanmıyor (hepsi kapalı). Sabit yollar:
    `hyperframes-shorts/SKILL.md` 22, `runtime-plan/SKILL.md` 25 ve kural metinleri (CLAUDE.md 106, docs, config/tools.yaml,
    status/skill-global.yaml). Kullanıcı OpenMontage/HyperFrames'i bu projede sınıyor; sonucunu söylemeden projeye dokunulmaz.
  - Akıl Dışı (git deposu değil; Codex düzeni + 24 kütüphane skili): `hyperframes-keyframes` ve `hyperframes-audio`nun TEK kopyası
    `~/.agents/skills` içinde (hiçbir yedekte yok): dondurulmadan `~/.agents` boşaltılmaz. `-creative`, `-animation` de dondurulur;
    `hyperframes` pakete bağlanır; altı OpenMontage skili bağlanabilir (bu proje de OpenMontage kullanıyor; K-27 tam doğru değil).
    Kullanıcıya sorulacaklar var: Codex dosyaları kalsın mı, 10:00/20:00 izleme nereye, görsel üretim aracı, rol dosyaları.
  - Etsy-Arif: genel klasöre bağımlılık yok, 27 kütüphane skili arşivle birebir; yapılacak tek iş `ui-ux-pro-max` yol çevirisi
    (`--guncelle`) ve Arif'in 5 kayıtsız skilini yalnız kütüphane tarafında `kendi_skilleri` olarak yazmak. ffmpeg, video-edit,
    playwright-recording bu projede kopya kalır (proje Windows'la paylaşılıyor; bağ taşınmaz). Projede git işlemi yapılmaz.
  DURUM 2026-11-12 sabah (kararlar K-28..K-35 `notlar/kararlar.md`'de; okumadan devam etme):
  - BİTTİ: bağ/dondur kurulum yolu (commit 0f50e43e2, push edildi; `--program-skill`, `--dondur`). Tam yedek
    `~/Documents/Claude/yedek/genel-skiller-tam-2026-11-12` (üç genel klasör, komutlar, genel not, 92 bağlık liste; yedekler.json'da).
    Etsy-Arif: `ui-ux-pro-max` yol çevirisi kuruldu, doğrulama temiz; projede 4 dosya değişti (kullanıcı gönderecek); Arif'in 5 skili
    kütüphanede `kendi_skilleri` olarak kayıtlı. Kullanıcı OpenMontage güncellemesini sınadı: sorun yok (K-30).
  - SÜRÜYOR: kütüphanedeki HyperFrames (ab66e5b) ve OpenMontage (fecb9a1) kaynak kopyaları `guncelleme/2026-11-hf-om` dalında
    güncellendi (kontroller geçti; commit atılmadı). Dalda yeniden inceleme (14 skill), `pika-h3-flex` ücret sınıfı ve dogrula'daki
    sıfıra bölme uyarısı düzeltiliyor. Bitince: dalda commit → master'a `--no-ff` birleştir → push.
  - GÜNCEL (2026-11-12 05:45): kaynak güncellemesi master'a birleşti ve push edildi (bf55a0fd1). Kullanım bildirimi kilidi üç ayar
    dosyasına eklendi (K-36; aşağıdaki soru KAPANDI). Bekçi tabanı yazıldı (`notlar/genel-klasor-tabani.json`, 196 girdi).
    IstatistikYoutube HF GEÇİŞİ YAPILDI: iki program bağı (`hyperframes`, `hyperframes-cli`), `motion-doctrine` güncellendi,
    11 tarif notu `.claude/skills/hyperframes-shorts/tarifler/`, kural metinleri ve `skill_durum.py`/`skill-global.yaml` yeni düzene
    göre; proje yedeği `~/Documents/Claude/yedek/istatistik-skill-gecisi-2026-11-12`. Genel klasörden yalnız `hyperframes` ve
    `hyperframes-cli` taşındı (`genel-kaldirilan-2026-11-12`; bağımlısı yoktu; rehber/12 sırası dışı, gerekçe yedekler.json'da).
    Kanalın `skill_durum.py` sonucu: TEMİZ, 0 FAIL. Kullanıcının yapacağı: yeni Claude oturumunda sınama; `skill_durum.py --onayla`
    (iki bağ için taban; kanalın kendi onay adımı). AÇIK: `tools/kural_kopya_tara.py` bağlı `hyperframes/references/sound.md`
    içindeki ses değerini bulgu sayıyor (tarama listesinden bağlı skilleri çıkarmak kanal kararı); proje `.claude/settings.json`'a
    paket skill klasörü için okuma izni önerisi (izin dosyası: yalnız kullanıcı isterse).
    GÜNCEL (06:55-07:10): yerel kaynak T7 (`kendi/`) kütüphanede (commit 501bb9fab, push edildi): `openmontage`, `youtube-arama`,
    `nlm-skill` (anlık kopya, nlm 0.15.8). Genel klasörden taşınanlar (`genel-kaldirilan-2026-11-12`): 75 OpenMontage bağı,
    `hyperframes`, `hyperframes-cli`, `design-dna`, `openmontage`, `nlm-skill`. IstatistikYoutube'a kütüphaneden `design-dna`,
    `openmontage`, `nlm-skill` kuruldu (26 kütüphane skili + 2 program bağı); design-dna `node_modules` eski kopyadan konuldu, ölçüm
    çıktısı eskiyle birebir aynı; `kapak_dna_kontrol.py` ve `video_dna.py` yolu proje içine çevrildi. Kalan metin düzeltmeleri
    (kurallar, yaml, skill_durum) bir alt ajanda sürüyor. `~/.claude/CLAUDE.md` OpenMontage bölümü ve üç genel komut projedeki
    skili gösterecek şekilde güncellendi; kart `giris_yolu.claude-code` = proje-skili. Bağ kurulum sınaması: 83 skill (80 OM + 3 HF)
    geçici projede kuruldu, 83/83 sağlam, gerçek Claude oturumu gördü, boş klasörde görünmedi, kaldırma programı etkilemedi.
    Genel klasörde kalan (24): eski HyperFrames skilleri ve Akıl Dışı'nın Codex zincirinin kullandıkları, `youtube-arama`, `.trash`, `synced`.
    Boşaltmanın geri kalanı Akıl Dışı geçişinden SONRA (Codex bağları `~/.claude/skills` ve `~/.agents/skills` içine bakıyor).
    Not: bekçi `~/.palmier/skills` ve `~/.gemini/config/skills` klasörlerini buldu (başka uygulamaların kendi klasörleri; "kalacak").
  - GÜNCEL (2026-11-12 08:40): BOŞALTMA TAMAM (K-40) ve AKIL DIŞI GEÇİŞİ TAMAM (K-41); IstatistikYoutube TAMAM (K-38). Bekçi TEMİZ,
    taban boş duruma göre yenilendi. Yedek silme hatırlatması 2026-11-19 10:00 (K-39).
    KALAN İŞLER: (1) HyperFrames 0.9.35 → 0.9.37 (yeni sürüm çıktı; rehber/11 adımlarıyla, yeni yedek gerekir). (2) AntigravityTest2 →
    Çöp Kutusu (önce `proje-kullanimi.py --cikar`). (3) Aylık zincir Aşama 2 + canlı zamanlanmış görev metni. (4) `rehber/11`, `rehber/12`
    ve kartlarda boşaltma öncesini anlatan eski cümleler; `giris_yolu` diğer araçlar. (5) Küçük araç eksikleri: `kardes-eksik` uyarısı
    program bağını kardeş saymıyor; `nlm-skill` anlık kopya (program kartı + bağ istenirse `yerinde.tur` genişletilmeli).
    (6) Kullanıcıya sorulacaklar: Akıl Dışı izleme otomasyonu, görsel aracı. (7) Etsy-Yeni'deki emekli `etsy-api`.
    (8) Kullanıcı Akıl Dışı ve IstatistikYoutube'u yeni oturumda sınayacak; sorun olursa yedekten geri dönülür.
  - KAPANIŞ (2026-11-12 akşamüstü; K-48..K-51): Akıl Dışı geçişi bu oturumda TAMAMLANDI sayılır (kullanıcı projeyi Claude'da kendi oturumunda
    sürdürüyor; kalan izin/otomasyon/model işleri orada). Projelerde onaysız işlem yok (K-50). Kayıp kaynak kuralı (K-49). HyperFrames 0.9.38 ve
    nlm 0.16.2 güncellemeleri ile aday repolar kullanıcı isteyene kadar bekler (K-48). IstatistikYoutube'da kullanıcı geçiş sonrası sorun bildirdi;
    yedeğe dönüp dönmeme kararı kullanıcıda (yedekler: `istatistik-skill-gecisi-2026-11-12` kökü + `genel-skiller-tam-2026-11-12`); kütüphane oturumu dokunmaz.
  - EK (2026-11-12 öğleden sonra; K-46, K-47): nlm üçüncü program olarak kartlı (`uv-tool`), `nlm-skill` IstatistikYoutube'da program bağı
    (kopya kaldırıldı; `kendi/` altında artık yalnız `openmontage` ve `youtube-arama`). Kendi skillerin güncelleme yolu ayrı bir kopyada
    uçtan uca sınandı (düzenle → işle → proje güncelleme görür → uygula → geri al; elle değişiklik ve kaynaktan kaldırma fark edilir): sorun yok.
    AÇIK: nlm 0.15.8 → 0.16.2 ve HyperFrames 0.9.37 → 0.9.38 güncellemeleri kullanıcı kararında; Etsy-Yeni `etsy-api` hatırlatması 2026-11-19 10:30;
    Akıl Dışı izinlerini kullanıcı kendisi ayarlayacak.
  - SON DURUM (2026-11-12 öğle; kararlar K-24..K-45): GEÇİŞ TAMAMLANDI. Genel skill klasörleri boş (bekçi TEMİZ); IstatistikYoutube,
    Akıl Dışı ve Etsy-Arif yeni düzende ve doğrulandı; OpenMontage `fecb9a1e`, HyperFrames 0.9.37; kütüphanede program bağı
    (`--program-skill`), dondurma (`--dondur`), kendi skiller (`kendi/`, T7), aylık zincir (`--aylik`) ve canlı görev metni yenilendi;
    AntigravityTest2 Çöp Kutusu'nda; Akıl Dışı izleme görevi Claude'da (Codex otomasyonunu kullanıcı durduracak).
    AÇIK KALANLAR: (1) kullanıcı iki kanalı yeni oturumda sınayacak; (2) yedekler 2026-11-19 hatırlatmasıyla sorulacak (12 kayıt,
    `yedekler.json`); (3) [kapandı 2026-11-12, K-46] `nlm-skill` program kartı + bağ oldu; (4) aday repolar
    (trend/popüler) kullanıcı kararı bekliyor; (5) Etsy-Yeni'deki emekli `etsy-api`; (6) Etsy-Arif'teki 4 değişen dosyayı kullanıcı
    Arif'e gönderecek; (7) proje izin ayarları (Akıl Dışı) kullanıcı isterse.
  - ESKİ SORU (kapandı): HyperFrames kullanım bildirimini bilgisayar genelinde kapatmak için
    üç ayar dosyasına `HYPERFRAMES_NO_TELEMETRY=1` eklensin mi. Cevap yoksa yalnız proje ayarında kapatılır.
  - SIRADAKİ: (1) IstatistikYoutube: plan `hf-gecis-ve-kendi-skiller-2026-11-12.json` → `istatistik` + `istatistik_inceleme.son_adimlar`
    (K-31: eski kuşak dondurulmaz; `hyperframes`, `hyperframes-cli` pakete BAĞ; karşılığı tam olmayan 11 tarif kanalın kendi tarif
    notu olarak proje skiline alınır, ad listesi değişmez; 29 dosya düzeltmesi; proje git deposu değil, önce dosya yedeği).
    (2) Kendi skiller (K-32): `design-dna` kütüphane kopyası + `npm install`; `openmontage` giriş skili ve `youtube-arama` kütüphaneye
    yerel kaynak (T7, araç işi gerekir); `nlm-skill` program kartı + bağ; genel komutlar ve genel nottaki OpenMontage bloğu.
    (3) Akıl Dışı (K-33): önce proje + Codex dosyaları yedeği; plan aynı json → `akildisi` + `akildisi_inceleme`.
    (4) Boşaltma `rehber/12`: `~/.agents/skills` EN SON (Akıl Dışı'dan sonra); sonra bekçi tabanı, yedek silme hatırlatması.
    (5) Aylık görev Aşama 2 + canlı görev metni. (6) AntigravityTest2 → Çöp Kutusu (önce `projeler.json` kaydı).
  Uygulamadan kalanlar ((a) ve (b) 2026-11-12'de kapandı): (a) `ortak.py` izleme listesi / `test.py` parmak izi Cursor, Gemini, Copilot klasörlerini de sayıyor; aylık
  birleştirmede sahte başarısızlık verebilir; (b) `test_p6`, `test_p1`, `test_p5` içinde gerçek veriye bağlı birkaç iddia var (program
  güncellenince kırılır); (c) aylık Aşama 2 (damga, `--takip`, `--atla` kullanımı, `zamanlanmis/aylik-guncelleme.SKILL.md`);
  (d) `--kayip-isaretle` yok, elle; (e) kayıtsız arşiv klasörleri için `--yoksay` (onay listesi 38).
  Eski not (artık geçersiz): Bu turda YAPILMAYANLAR (onay bekler, metinleri `notlar/duzen-denetimi-2026-11/onay-bekleyen/` içine yazılır): `CLAUDE.md`/`AGENTS.md`
  ekleri, eski belgeleri rafa kaldırma, gerçek makine için taban dosyası, canlı zamanlanmış görev metni, proje bloklarına kütüphane yolu.
- Tasarım: `notlar/duzen-denetimi-2026-11/04-tasarim-ozeti.md` (özet, ertelenen, onay isteyen, riskler) ve `tasarim/tasarim-p*.md` (8 paket).
  Uygulama sırası: P3 → P1 → P2 + P5 + P6 → P7 → P4 → P8 (CLAUDE/AGENTS Yama A; kural 1 istisnası olan Yama B ayrı onayla) → boşaltma.
  Uygulama makineye, projelere, ayar dosyalarına ve zamanlanmış göreve yazmaz; sadece kütüphane içi araç, rehber ve test ekler.
  Uygulamadan önce kullanıcıya sorulacaklar: `.gitignore` eklemeleri, `CLAUDE.md`/`AGENTS.md` Yama A, eski belgeleri rafa kaldırma,
  proje bloklarına kütüphane yolu cümlesi (P1 Q3), `projeler.json` ilk içeriği (P5).
- Sonuçlar: `notlar/duzen-denetimi-2026-11/` (`01-arac-tablosu.md`, `02-bosluk-listesi.md`, `03-elestiri.md`, `arac-arastirmasi.json`).
  158 doğrulanmış boşluk; A1-A7 boşaltmadan önce kapanmalı, B1-B9 aylık sürdürülebilirlik, C isteğe bağlı; 8 iş paketi (P1-P8).
- Kullanıcıya tek tek sorulacak altı soru `02-bosluk-listesi.md` sonunda. Onay isteyenler: `CLAUDE.md` kural 1 istisnası,
  zamanlanmış görev metni, `.gitignore`, eski belgeleri rafa kaldırma, artık dalı silme, taban dosyasını yazma, her push.
- Yeniden başlatma: `settings.json` içindeki anahtar yeni Claude oturumunda geçerli olur. Kullanıcıya "şimdi yeniden başlat" demek
  bende; arka planda iş yokken ve kütüphane kaydedilmişken söylenir.
- Yeni görülen: `buluslan/ecommerce-competitor-analyzer` kaynağına erişilemiyor (kapsam denetimi; `tip: KAYIP` kararı kullanıcıda).

## Sonraya kalan düzeltmeler
- 3. adımın günü düzeltilecek belge satırları (bugün hâlâ doğru): `README.md` 6-7, `rehber/01-skill-ekleme-sureci.md` 12
  ("eski agent'lar genel klasörlerdeki skillerle çalışmaya devam eder").
- `rehber/02-guncelleme-yonergesi.md` "4) Global skiller" düzeltildi (2026-11-11).
- `CLAUDE.md` kesin kural 1 ile program kartlarındaki güncelleme adımları çelişiyor (kartlar `~/.openmontage` içinde onaylı güncellemeyi
  anlatıyor). Kurala "onaylı program güncellemesi hariç" istisnası ve "Programlar" satırına `kopya: yerinde` notu kullanıcı onayıyla eklenecek.
- Eklenti kökünden dosya çekme (`ek_dosyalar`) bu turda yok; lisans ve ücret onayı gerekir.

## Açık notlar
- Kütüphane `master` dalı GitHub'a gönderilmedi; kullanıcı isteyince `git push origin master`.
- İş bitince bu klasör arşivlenir (içinde proje adı geçiyor).
