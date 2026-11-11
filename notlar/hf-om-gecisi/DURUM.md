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
- Sıra: boşluk denetimi (BİTTİ) → tasarım (BİTTİ 2026-11-11 gece) → uygulama (kütüphane içinde; SIRADAKİ) → inceleme → üç kontrol → commit.
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
