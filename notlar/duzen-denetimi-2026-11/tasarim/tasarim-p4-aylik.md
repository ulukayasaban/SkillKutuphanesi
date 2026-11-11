# P4 Aylık zincir ve tek sayfa özet — tasarım (spec)

**Önkoşul (uygulama sırası):** (0) mevcut commit edilmemiş `programlar/` işinin commit'i (kullanıcı onayıyla); (1) P3 (`.gitignore` iki satırı: damga ve özet dosyası; `git-durum`, `yedek-denetim`); (4) P7 (`kaynak-cek.py --atla`, üç `--bekleyenler --ozet-json`); P2/P5/P6/P1 `--ozet-json` çıktıları. P4 uygulaması bunların SONRASINDA, P8'den ÖNCE yapılır; bir araç henüz yoksa aylik-ozet onu `dikkat` ("araç kütüphanede yok") yapar, çökmez; gerçek doğrulama tüm paketler indikten sonra yapılır. **Uygulama iki aşamalıdır (bölüm 3.1 sonu): Aşama 1 ve Aşama 2 ayrı commit ve ayrı onayla.**

Paket: P4. Sahip olduğu dosyalar: `araclar/aylik-ozet.py` (yeni), `araclar/arsiv-guncelle.py` (düzenleme), `rehber/02-guncelleme-yonergesi.md`,
`promptlar/08-aylik-guncelleme-onayi.md`, `zamanlanmis/aylik-guncelleme.SKILL.md` (yeni), `notlar/son-aylik-calisma.json` (yeni, çalışma zamanı damgası; git'e GİRMEZ),
`araclar/testler/test_p4-aylik.py` (yeni). Başka dosyaya dokunulmaz. Kapatılan boşluklar: B1, B2 (özet kısmı), B4'ün `arsiv-guncelle.py` kısmı,
eleştiri senaryoları 4, 6, 11. Bu belge İngilizce; kullanıcıya görünen metinler ve tanımlayıcılar Türkçe, çıktıda göründüğü gibi yazılmıştır.

---------------------------------------------------------------------------------------------------------------------

## 0. Önce çözülen üç tasarım noktası (uygulayıcı yeniden karar vermeyecek)

**0.1 Damga ve özet dosyası git'e girmez; bu P3'ten ENGELLEYİCİ bir devir isteğidir.**
`notlar/son-aylik-calisma.json` ve `notlar/aylik-ozet.md` makineye özgü, izlenmeyen durumdur. İzlenseydi her koşu ağacı kirletirdi:
`duman-testi.py:61-62` (`git status --porcelain` boş olmalı), canlı görevin ön kontrol 1'i, `arsiv-guncelle.py:157` ve `:247` hepsi kırılırdı.
Bu yüzden: (a) P3 `.gitignore`'a şu iki satırı ekler: `notlar/son-aylik-calisma.json` ve `notlar/aylik-ozet.md`; bu satırlar P4 bu dosyaları
ilk kez yazmadan ÖNCE kütüphanede olmalıdır. (b) Araç da kendini korur: bu iki dosyayı yazmadan önce `git check-ignore -q <yol>` çalıştırır.
Çıkış 0 (yoksayılıyor) ya da 128 (git deposu değil, temp testi) ise yazar; çıkış 1 (yoksayılmıyor) ise YAZMAZ, "UYARI: <yol> .gitignore'da değil; ağacı kirletmemek
için yazılmadı (P3 .gitignore satırı eksik)" der ve aylik-ozet bunu `dikkat` satırı yapar. (c) rehber/02'de "damga bu makineye özgüdür, git geçmişinde yoktur" yazar.

**0.2 `--ozet-json` ve diske yazma (düzeltilmiş sözleşme).**
D4: rapor araçları en fazla KENDİ rapor dosyasını yazar. Özet zinciri master'da koşar; izli bir rapor dosyası değişirse ağaç kirlenir ve bir sonraki `--aylik` "kirli ağaç" diye durur. Bu yüzden sözleşme şöyledir:
(a) `genel-bekci.py`, `git-durum.py`, `yedek-denetim.py` ve P1/P7'nin `--araclar`/`--bekleyenler` modları `--ozet-json` ile diske HİÇBİR şey yazmaz (rapor dosyası dahil).
(b) `proje-kullanimi.py --saglik --ozet-json` `notlar/proje-durumu.md`'yi YALNIZ `--yaz` verilirse yazar (P5 sözleşmesi). `program-denetim.py --ozet-json` en fazla kendi `notlar/program-denetimi.md`'sini yazabilir (P6 "aynı koşu" dedi; P6 uygulayıcısı açıkça karar verir, tavsiyemiz: `--yaz` olmadan yazmasın). Bu iki dosya aylik-ozet'in **izinli rapor yolları**dır (`IZINLI_RAPOR_YOLLARI = ("notlar/proje-durumu.md", "notlar/program-denetimi.md")`).
(c) `aylik-ozet.py` araçları koşturmadan önce ve sonra `git status --porcelain -z` alır. Yeni kirli yol İZİNLİ listede ise sessizce kabul edilir; başka bir yol ise o aracın satırına "UYARI: <arac> --ozet-json ile dosya yazdı: <yol> (sözleşme ihlali)" eklenir ve durum `dikkat` olur.
(d) **Tam mod (kullanıcı ya da oturum elle koşar):** `proje-kullanimi.py --saglik --yaz --ozet-json` çağrılır (proje-durumu.md aylık tazelensin; P5 isteği). Dosya değiştiyse (ve ağaç koşudan önce temizdi) özet şu kararı üretir: "Rapor dosyaları yenilendi (<dosyalar>): kaydedilsin mi? (git add … && git commit; onayınla)". Otomatik commit YOK.
(e) **Zincir içinde (`arsiv-guncelle.py --aylik` çağırdığında) özet `--yazmadan` ile koşar:** `--yaz` verilmez; yenilenmiş raporlar zaten dal içinde üretilmiştir (`_uygula`/`takip` adımı `proje-kullanimi.py --saglik --yaz`, 3.1-H). Özetten sonra `aylik()` ağacı kontrol eder: ağaç koşu başında temizdi ve yalnız `IZINLI_RAPOR_YOLLARI` değişmişse bu iki dosyayı `git checkout -- <yol>` ile geri alır (yalnız kendi koşusunun ürettiği, dal içinde zaten commit'li üretilmiş dosyalar; `reset --hard` yok, master'a commit yok). Başka yol değişmişse dokunmaz, uyarır.
(f) `yol-tara.py` master'da hiç koşturulmaz: yalnız dallarda (`_uygula`, `takip`) koşar; özet yalnız `notlar/yol-denetimi.md` tarihini (bayatlık) gösterir.

**0.3 Erişilemeyen kaynak atlama: `arsiv-yerlestir.py` zaten güvenli (kanıtlandı), bayrak P7'nin `kaynak-cek.py`'sinde.**
`arsiv-yerlestir.py:455-475`: indirilmemiş ama `arsivlenen_repolar`'da olan repo `korunan_indirilmeyen`'e alınır; döngü sonunda (`:476-523`) arşiv kopyası
`shutil.copytree` ile yeni ağaca taşınır ve `skiller.append(s)` yapılır. Yani atlanan repo `:631-636` güvenlik kilidine takılmaz. Kalan tek engel
`kaynak-cek.py:238-240` (`GhBulunamadi` → `sys.exit`). P7'ye devir: `--atla owner/ad[,owner/ad]` bayrağı (bölüm 6). `arsiv-guncelle.py` bayrağı kullanmadan önce
`kaynak-cek.py --help` çıktısında `--atla` aradığı için P7 gecikse de eski davranış (durma) bozulmaz; B4'ün bu parçası "P7 bayrağı gelene kadar kapalı" olarak kapanır.

**0.4 D12 ile dal silme.** Araçlar silme yetkisi taşımaz, yalnız şunlar kalır (hepsi mevcut ya da aynı koşunun kendi dalı):
(1) `_uygula` geri alma `git branch -D <aynı koşunun açtığı dal>` (`arsiv-guncelle.py:227`, mevcut); (2) YENİ `takip()` aynı koşunun açtığı `takip/…` dalını geri alırken ya da
"değişiklik yok" olunca siler; (3) `--birlestir` sonrası `git branch -d <dal>` (`:266`, mevcut, yalnız kullanıcı onayıyla çağrılır). Hiçbir araç başka
bir dalı, uzak dalı ya da bekleyen eski dalı silmez; `aylik-ozet.py` hiçbir git yazma komutu çalıştırmaz.

---------------------------------------------------------------------------------------------------------------------

## 1. Purpose

1. Aylık zinciri tek, test edilebilir komuta indir: `python3 -u araclar/arsiv-guncelle.py --aylik` (ön kontrol, kaynak raporu, liste raporu, güncelleme ya da takip dalı,
   aylık özet, damga). Zamanlanmış görev metni kısalır; Codex/Antigravity oturumu da aynı komutu çalıştırabilir (zamanlayıcı yalnız Claude'a özgü kalır, komut değil).
2. Hiçbir tek sorun tüm zinciri susturmasın: kirli ağaç, bekleyen dal, `gh` yok/ağ yok, erişilemeyen tek kaynak "DURDU" yerine rapor + salt okuma adımlarına döner.
3. "Son aylık çalışma" damgası (`notlar/son-aylik-calisma.json`) ve kaçan ay telafisi. **Asıl tetik:** aylık zincirin asıl tetiği "oturum başı damga 35 günü aştı mı" kuralıdır (her araçta: Claude, Codex, Antigravity, Cursor, Copilot; satır `CLAUDE.md` = `AGENTS.md` içindedir, P8 eşitlik denetimi bunu sağlar). Zamanlanmış görev (yalnız Claude masaüstü uygulamasına özgü) yalnız kolaylıktır; Mac uykudayken/uygulama kapalıyken tetiklenmeyebilir. Bu yüzden hiçbir komut zamanlanmış görev metnine ya da Claude eklentisine bağlı değildir: zincirin tamamı `python3 -u araclar/arsiv-guncelle.py --aylik` komutudur, zamanlanmış görev metni yalnız bu komutu çağırır ve sonucu anlatır.
4. `araclar/aylik-ozet.py`: D4 rapor araçlarını `--ozet-json` ile toplayan, kendi kontrollerini ekleyen, `notlar/aylik-ozet.md` yazan, kullanıcıya okunacak kısa düz
   Türkçe özet basan tek sayfa. Ucuz modu (`--hizli`) oturum başı kontrolüdür.
5. Üç belge (rehber/02, promptlar/08, zamanlanmış görev kopyası) aynı komutları ve aynı `takip/*` birleştirme yolunu (`--birlestir`) söylesin.

---------------------------------------------------------------------------------------------------------------------

## 2. Existing behaviour relied on (file:line)

`araclar/arsiv-guncelle.py` (293 satır):
- `:34-40` `calistir()` `check=True` ile komut basar; `git()` hata fırlatmaz, `(returncode, stdout, stderr)` nesnesi döner. Testler bu iki fonksiyonun modül düzeyindeki `KOK`'a göre çalışmasına dayanır (modül özniteliği yamalanır).
- `:43-81` `rapor()`: T1-T4 repoları `gh_api(f"repos/{repo}/commits/HEAD")` ile kontrol eder (`:53-55`); `GhBulunamadi` → `sorunlu` (`:56-59`); diğer istisnalar yakalanmaz (çevrimdışıyken ilk repoda 4 deneme × bekleme sonra Traceback). Sonunda `dogrula.py --github` çalıştırır, çıkış kodu yok sayılır (`:80`). `etkilenen_projeler()` gerçek `proje-kullanimi.py`'yi yükler (`:84-101`).
- `:47-51` kaynakta kaldırılmış kayıt eski commit'te kalır: karşılaştırma TARİHE değil registry'deki commit'e dayanır. Bu, kaçan ayın bir sonraki koşuda otomatik telafi olmasının dayanağıdır (kural: bölüm 3, 3.1-K).
- `:104-138` `gecmis_yaz()`: kayıt biçimi `## <tarih> — \`<dal>\``, `Durum: **master'a birleştirilmeyi bekliyor**`, satırlar `- **Karar bekleyen yeni skiller** (N; …` (`:122`) ve `- **Yeniden incelenecek** (N)` (`:129`). `aylik-ozet.py` bu iki satırı dalın kopyasından okur.
- `:141` `KILIT = KOK/.guncelleme-kilidi`, `.gitignore`'da (kontrol: `.gitignore` satır `.guncelleme-kilidi`). `:144-153` `api_hakki_kontrol(gerekli=1500)`: `gh api rate_limit` başarısızsa `sys.exit("DURDU: GitHub API'ye ulaşılamıyor …")`.
- `:156-175` `uygula()`: `:157` kirli ağaç → `sys.exit("DURDU: kütüphanede kaydedilmemiş değişiklik var…")` (dosya listesi yok); `:160` API hakkı; `:163-171` canlı pid kilidi → exit, ölü pid kilidi üzerine yazılır; `:172-175` `try/finally` kilit silme.
- `:178-240` `_uygula()`: dal `guncelleme/YYYY-AA` (+`-2`…) `:182-187`; adım sırası `:189-214` (gelistirici-bilgisi, github-trend --aday, populer-tarama, konu-takip, kaynak-cek, arsiv-yerlestir, yol-tara, program-denetim, kapsam-denetimi, katalog-uret, skill-readme, skill-calistir, dogrula); tarama adımları `UYARI` ile devam eder (`:191-198, :202-206, :212`); hata → `:221-229` `reset --hard`, `clean -fdq arsiv notlar` (izlenmeyen ama yoksayılmayan dosyaları siler; yoksayılanlara dokunmaz: damga bu yüzden `.gitignore`'da olmalı), master'a dön, `branch -D <dal>`, `sys.exit(1)`.
- `:243-268` `birlestir(dal)`: dal `refs/heads/<dal>` olarak aranır, herhangi bir ad kabul edilir (`takip/*` dahil). `:247-248` kirli ağaç → exit. Birleştirme sonrası dogrula + kapsam + test.py, hata olursa master geri (`:253-259`). `:260-265` `guncelleme-gecmisi.md` "bekliyor" cümlesi yoksa dokunmaz (takip dalı için zararsız). `:266` `branch -d`.
- `:271-289` `main()`: `rapor()` her zaman çalışır; bekleyen dallar yalnız `guncelleme/*` (`:278`); rapor modu çıkışı `1 if sorunlu else 0` (`:281-282`); `:283-286` erişilemeyen kaynak varsa `--uygula` durur; `:287-288` bekleyen dal `--dal`'ı engeller.
- `araclar/duman-testi.py:88-89` rapor modunu yalnız "Traceback" yokluğuyla sınar (çıkış kodu okunmaz). Canlı görev çıkış kodunu okumaz (metin yorumlar). `test.py` ve `dogrula.py` `arsiv-guncelle`'ye değinmez (grep boş).

Diğer:
- `araclar/ortak.py:11-18` `KOK`, `REGISTRY`, `KAYNAKLAR`; `:44-56` `json_oku`/`json_yaz` (atomik); `:59-75` `GhBulunamadi`/`gh_api` (404/422 → GhBulunamadi, diğer hatalarda 2-60 sn bekleyerek 4 deneme sonra RuntimeError); `:444-448` `repo_guncel()` gerçek `kaynaklar.json`'u okur (testte yamalanır).
- `araclar/program-denetim.py:293-342`: `--cikti` bayrağı vardır; çıkış hep 0; rapor dosyası `notlar/program-denetimi.md` (P6 `--ozet-json` ekleyecek).
- `araclar/proje-kullanimi.py:148-173`: `--kontrol` (güncel değilse 1), rapor `notlar/proje-kullanimi.md`.
- `araclar/yol-tara.py:185-215`: çıkış her zaman 0, yalnız `notlar/yol-denetimi.md` yazar.
- `araclar/github-skill-listesi.py:58-94`: "AD DEĞİŞMİŞ" satırını bu araç yazar; çıkış 1 yalnız `hata` varsa (`:124, :149`); GraphQL gerektirir (bulutta çalışmaz).
- `araclar/kaynak-cek.py:212-240`: `argparse` (`--repo`); `GhBulunamadi` → `sys.exit` (`:238-240`).
- `araclar/arsiv-yerlestir.py:455-523` (korunan_indirilmeyen akışı, bölüm 0.3), `:631-636` güvenlik kilidi.
- Rapor biçimleri (aylik-ozet'in okuyacağı, değişirlerse P7/P6 bildirir): `notlar/konu-takip.md:7,15` `**odaklı aday: N**` ve `Son tarama: YYYY-AA-GG`; `notlar/populer-skiller.md:3` tarih, `:5` `## Yeni adaylar (N)`; `notlar/github-trend.md:52` bölüm başlığı `## Son taramada trend'de olup kütüphanede olmayan repolar` + tablo `| Repo | SKILL.md | Şu an |`; `notlar/program-denetimi.md:3` tarih, `YENİ SÜRÜM VAR` hücresi; `notlar/yol-denetimi.md:3` tarih; JSON: `trend.json` → `son_tarama`; `konu-takip.json` → `konular.<konu>.son_tarama`.
- Canlı zamanlanmış görev `~/.claude/scheduled-tasks/skill-kutuphanesi-aylik-guncelleme/SKILL.md` (42 satır, 7359 bayt, salt okundu): ön kontrol 1 kirli ağaçta durur (tek istisna `notlar/proje-kullanimi.md`), ön kontrol 3 `guncelleme/*` ve `takip/*` dalı varsa durur; C2 elle shell komutudur, `takip/*` birleştirmesi `git merge --no-ff` (kontrolsüz).
- `rehber/02`: `:32-33` "ilk iki adım" cümlesi, `:36` bekleyen dal kuralı, `:41-59` adım listesi (`yol-tara.py`, `program-denetim.py`, `gelistirici-bilgisi.py` listede yok), `:124-126` 3b "durur", `:148-156` takvim.
- `promptlar/08`: yalnız `guncelleme/*`.
- `.gitignore`: `.gecici/`, `.guncelleme-kilidi`, `__pycache__/` vb. var (`.gitignore` ilk 30 satır okundu).

---------------------------------------------------------------------------------------------------------------------

## 3. Changes per file

### 3.1 `araclar/arsiv-guncelle.py` (düzenleme; geriye uyumlu)

Mevcut bayraklar (`--uygula`, `--dal`, `--birlestir <dal>`, hiçbir bayrak = rapor) ve çıktı biçimleri aynen kalır. Eklenenler:

**Yeni bayraklar**
| Bayrak | Ne yapar | Çıkış |
|---|---|---|
| `--aylik` | tüm aylık zinciri koşturur (3.1-F) | 0: guncellendi/sadece-takip/kismi · 1: hata (ve `--siki` ile `kismi` → 2) |
| `--aylik --kuru` | yalnız ön kontrol + rapor + PLAN; commit, dal, damga, özet dosyası YOK (özet `--hizli` ile) | 0 |
| `--siki` (yeni; rapor modu ve `--aylik`) | yalnız burada: çevrimdışı/eksik kontrol ya da `kismi` → çıkış 2 | 2 |
| `--takip` | C2'nin Python karşılığı: `takip/YYYY-AA` dalında trend+popüler+konu+program+yol taraması (3.1-E) | 0 / 1 |
| `--damga-yaz <sonuc> [--neden "…"] [--damga-dal <dal>]` | damgayı yazar (görev metni, zincir hiç başlayamadıysa kullanır) | 0; geçersiz sonuç → `sys.exit` mesajı (1), hiçbir şey yazmaz |

`sonuc` değerleri: `guncellendi`, `sadece-takip`, `kismi`, `hata`, `durduruldu`.

**Uygulama aşamaları (ayrı commit, ayrı onay; reviewer düzeltmesi).**
- **Aşama 1 (düşük risk; yazma yolu yok):** A (sabitler/yardımcılar: `kirli_dosyalar`, `yoksayiliyor_mu`, `bekleyen_dallar`, `gh_hazir`, `kaynak_cek_atla_var`), B (`rapor()` çevrimdışı/geçici ağ toleransı, ad değişikliği), C'nin rapor modu ve bekleyen-dal satırları, I (`uygula()` kirli ağaç mesajı), J (`birlestir()` mesajları), `--aylik --kuru` (salt okuma planı) ve `araclar/aylik-ozet.py` (3.2; damga yoksa/varsa okur). Bu aşama hiçbir dal açmaz, hiçbir dosyaya (kendi md'si dışında) yazmaz. Testler: 21'den önceki A grubu + 22-29, 31(c,k).
- **Aşama 2 (yazma yolu):** D (`damga_yaz`, `--damga-yaz`), E (`takip()`), F'nin yazma adımları (`--aylik` kuru değilken), G (`gecmis_yaz`), H (`_uygula` değişiklikleri), `uygula()`'nın damgalanması, `zamanlanmis/` kopyası ve üç belgenin yazımı. Testler: 21, 30-33 ve 31'in kalanı. Aşama 2'ye geçmeden Aşama 1'in testleri ve bölüm 10'un salt okuma komutları geçmiş olmalıdır.

**A) Üst kısım (docstring + sabitler + yardımcılar)**
- Docstring'e 4 yeni bayrağı ve "çıkış 2 YALNIZ `--siki` ile: çevrimdışı/eksik kontrol" satırını ekle. `--siki` verilmezse rapor modu çıkışı eskisi gibi 0/1 kalır (eski kodu okuyan her çağıran etkilenmez).
- `:30-31` altına modül sabitleri: `DAMGA = KOK/"notlar"/"son-aylik-calisma.json"`, `OZET_RAPORU = KOK/"notlar"/"aylik-ozet.md"`,
  `URETILEN_NOTLAR = ("notlar/proje-kullanimi.md", "notlar/proje-durumu.md", "notlar/program-denetimi.md", "notlar/yol-denetimi.md")` (yalnız NEDEN metni ve `aylik()` özet sonrası geri alma için; commit için KULLANILMAZ), `ESIK_DAL_GUN = 45`, `ESIK_KACAN_GUN = 35`,
  `SONUCLAR = ("guncellendi","sadece-takip","kismi","hata","durduruldu")`; durum değişkenleri `ATLANAN = []`, `ADI_DEGISEN = {}`, `ULASILAMAYAN = []`, `CEVRIMDISI = False` (her `rapor()` başında sıfırlanır).
  Testler `KOK, GECMIS, KILIT, DAMGA, OZET_RAPORU, REGISTRY, KAYNAKLAR` özniteliklerini birlikte yamalar (hepsi `KOK`'tan import anında türediği için tek başına `KOK` yamalamak yetmez).
- Yeni yardımcılar (`git()`'ten sonra):
  - `kirli_dosyalar() -> list[tuple[str,str]]`: `git status --porcelain -z`; `(XY, yol)`; `R`/`C` girdisinde bir sonraki NUL parçası eski yoldur, atlanır. `.gitignore`'daki dosyalar `porcelain`'de zaten çıkmaz; hiçbir yol AYIKLANMAZ (0.1).
  - `yoksayiliyor_mu(yol) -> bool`: `git check-ignore -q <yol>`; 0 → True, 128 → True (depo değil), 1 → False.
  - `bekleyen_dallar() -> list[dict]`: `git branch --list 'guncelleme/*' 'takip/*' --format=%(refname:short)`; her dal için `{"dal", "gun"` (= `(bugun - date.fromtimestamp(int(git log -1 --format=%ct <dal>)))`, `.days`), `"birlesmis"` (`git merge-base --is-ancestor <dal> master` çıkışı 0)`}`.
  - `gh_hazir() -> (ok: bool, kalan: int|None, neden: str)`: `gh api rate_limit --jq .resources.core.remaining`, `timeout=30`; `FileNotFoundError` → `(False, None, "gh kurulu değil")`; `TimeoutExpired` → `(False, None, "zaman aşımı")`; returncode≠0 ya da sayı değil → `(False, None, "gh oturumu yok ya da ağ yok")`.
  - `damga_oku() -> dict` (dosya yok/bozuksa `{}`), `damga_yaz(sonuc, dal=None, neden="", atlanan=None, ad_degisen=None) -> bool` (3.1-D).
  - `kilit_al()`: `uygula()`'daki `:163-171` bloğunun taşınmış hâli (davranış aynı; canlı pid → `sys.exit("DURDU: başka bir güncelleme sürüyor …")`, ardından `KILIT.write_text(...)`). `uygula()` ve `takip()` bunu çağırır; `finally: KILIT.unlink(missing_ok=True)` her ikisinde.
  - `kaynak_cek_atla_var() -> bool`: `[sys.executable, araclar/kaynak-cek.py, --help]` çıktısında `--atla` var mı.

**B) `rapor()` (`:43-81`)** — imza ve dönüş `(degisen, sorunlu, ayrinti)` aynı; eski → yeni:
1. Başa: `ok, kalan, neden = gh_hazir()`. Başarısızsa: `UYARI: GitHub'a ulaşılamıyor (<neden>). Kaynak karşılaştırması ATLANDI; yalnız yerel kontroller yapıldı.` yaz, `CEVRIMDISI=True`, `dogrula.py`'yi `--github` OLMADAN çalıştır (`:80`'in yerel hâli), `etkilenen_projeler` çağırma, `return [], [], {}`. (Eski: ilk repoda uzun bekleme + Traceback.) Çıkış kodu ETKİLENMEZ (aşağıda C).
2. Döngüde `except GhBulunamadi` aynen (`sorunlu`), mesaj biçimi `! {repo}: erişilemiyor` ön eki KORUNUR, devamı: `(silinmiş, private ya da adı değişmiş olabilir). Arşiv kopyası korunuyor. İpucu: B adımındaki github-skill-listesi.py "AD DEĞİŞMİŞ" satırına bak.`
3. YENİ `except Exception as e` (geçici ağ/hız sınırı): `ULASILAMAYAN.append(repo)`, `! {repo}: şimdilik kontrol edilemedi ({kısa hata})`; art arda 3 başarısızlıkta döngü kesilir: `UYARI: art arda 3 kaynak kontrol edilemedi; kalanlar atlandı (ağ/hız sınırı).` ve kalan repolar `ULASILAMAYAN`'a eklenir. Başarılı bir kontrol sayacı sıfırlar.
4. YENİ ad değişikliği (bedava, ek çağrı yok): başarılı `commits/HEAD` yanıtındaki `html_url` (`https://github.com/<sahip>/<ad>/commit/<sha>`) regex `github\.com/([^/]+/[^/]+)/commit/` ile okunur; küçük harfle `repo` ve `repo_guncel(repo)`'dan farklıysa `ADI_DEGISEN[repo] = <yeni ad>` ve yazdır: `~ AD DEĞİŞMİŞ: {eski} -> {yeni} (yeni kaynak DEĞİL; kaynaklar.json'da 'repo'yu yeni adla değiştir, eski adı "eski_adlar"a yaz; rehber/09)`. `html_url` yoksa sessizce geçilir. DOĞRULANMADI (bu aşamada `gh api` yasak): uygulayıcı bilinen bir taşınmış repoyla bir kez dener; tutmuyorsa kod bırakılır, yedek yol `github-skill-listesi.py` adımıdır (B), ve bu not rehber/02'ye yazılır.
5. Sonda "Tüm kaynaklar güncel." koşulu `not degisen and not ULASILAMAYAN`; `ULASILAMAYAN` doluysa `Kontrol edilemeyen kaynak: N (geçici); sonra tekrar çalıştır.` yazılır.

**C) `main()` rapor modu ve `--uygula` kapısı (`:271-289`)** — eski → yeni:
- `--damga-yaz` en başta (ağsız) işlenir; sonra `--birlestir` (aynen), `--aylik`, `--takip`.
- Rapor modu çıkış kodu: eski `1 if sorunlu else 0` AYNEN (varsayılan; reviewer düzeltmesi: çıkış 2 varsayılan davranış DEĞİL). Çevrimdışılık ya da kontrol edilemeyen kaynak ayrı satır olarak yazılır (`UYARI: …` ve `Kontrol edilemeyen kaynak: N`), çıkış 0 kalır. `--siki` verilirse ve `sorunlu` boşken `CEVRIMDISI`/`ULASILAMAYAN` doluysa çıkış **2**. Okuyanlar: `duman-testi.py:88-89` (yalnız "Traceback"), canlı görev (çıkış kodu okumaz), yeni `--aylik` (fonksiyonu doğrudan çağırır). `--siki` ve 2 rehber/02'de belgelenir.
- `:278-280` bekleyen dal satırı: `bekleyen_dallar()` ile her iki desen, yaş ve uyarılar: `Onay bekleyen dal: guncelleme/2026-11 (12 gün önce hazırlandı)`; yaş > `ESIK_DAL_GUN` → `UYARI: <dal> 45 günden eski: birleştir (--birlestir <dal>) ya da sil (git branch -D <dal>).`; `birlesmis` → `<dal> zaten master'a birleşmiş; silebilirsin: git branch -d <dal>`. (Eski çıktı satırının ilk sözcükleri aynı: "Onay bekleyen".)
- `:283-286` erişilemeyen kaynak: eski "DURDU" yalnız `kaynak_cek_atla_var()` False ise aynen kalır. True ise: `UYARI: erişilemeyen kaynak(lar) atlanacak (arşiv kopyaları korunur): …` yazılır, `ATLANAN = sorunlu` atanır ve devam edilir. `ULASILAMAYAN` doluysa `--uygula` yeni mesajla durur: `DURDU: N kaynak şimdilik kontrol edilemedi (geçici ağ/hız sınırı: …). Sonra tekrar çalıştır. Hiçbir şey değişmedi.`
- `:287-288` bekleyen dal engeli iki desenle (`guncelleme/*` ve `takip/*`), mesaj aynı biçim.
- Tek başına `--uygula --dal` (aylık komutsuz) başarılı biçimde bitince `damga_yaz("guncellendi", dal=<yeni dal>)`; `_uygula` hatasında `sys.exit(1)` yakalanıp `damga_yaz("hata", neden=<kısa>)` sonra yeniden `raise`. `--aylik` içindeyken çift damga yazılmaması için modül bayrağı `_AYLIK_ICINDE`.

**D) `damga_yaz()` ve damga dosyası** (`notlar/son-aylik-calisma.json`, yerel, izlenmez):
```json
{
  "surum": 1,
  "son_calisma": "2026-12-01T10:41:07+03:00",
  "son_sonuc": "guncellendi",
  "son_dal": "guncelleme/2026-12",
  "son_neden": "",
  "son_basarili": "2026-12-01T10:41:07+03:00",
  "atlanan_kaynaklar": ["J-DTurner/etsy-api-skill"],
  "ad_degisen": {"eski/ad": "yeni/ad"},
  "gecmis": [{"zaman": "2026-12-01T10:41:07+03:00", "sonuc": "guncellendi", "dal": "guncelleme/2026-12", "neden": ""}]
}
```
Kurallar: zaman `datetime.now().astimezone().isoformat(timespec="seconds")`; `son_basarili` yalnız `guncellendi`/`sadece-takip` ile güncellenir; `gecmis` en yeni üstte, en çok 12 kayıt; yazım `ortak.json_yaz` (atomik); yazmadan önce `yoksayiliyor_mu(DAMGA)` (0.1) değilse yazılmaz ve `False` döner; bozuk eski dosya yok sayılıp yeniden başlanır; geçersiz `sonuc` → `ValueError` (CLI'da `sys.exit`).

**E) `takip()` (yeni; eski C2 shell'inin karşılığı, eksikleri kapatır)**
1. Ön koşullar: master'da değilse ya da `kirli_dosyalar()` doluysa `sys.exit` (dosya listesiyle; 3.1-F zaten bunları önceden eler); `bekleyen_dallar()` doluysa `sys.exit`; `gh_hazir()` başarısızsa `sys.exit("DURDU: GitHub'a ulaşılamıyor…")`; `kilit_al()`.
2. Dal: `takip/YYYY-AA`, varsa `-2`, `-3`… (`:182-187` kalıbı); `git switch -q -c <dal>`.
3. Adımlar (her biri `subprocess.run`, çıkış kodu kontrol edilir): `github-trend.py --aday`, `populer-tarama.py`, `konu-takip.py`, `program-denetim.py`, `yol-tara.py`, `proje-kullanimi.py --saglik --yaz` (H-2; yalnız `--saglik` varsa) → hata `UYARI` + `eksik` listesine (zinciri durdurmaz, `_uygula` kalıbı); `katalog-uret.py`, `dogrula.py` → `calistir()` (hata → geri alma). Eski C2'ye göre yenilikler: populer-tarama, program-denetim, yol-tara eklendi; `konu-takip` çıkış 1'i "konu takibi eksik" uyarısı (eskiden geri alma).
4. Üç ağ taraması (trend, popüler, konu) HEPSİ başarısızsa: geri al, sonuç `kismi`, neden `taramalar yapılamadı (ağ?)`.
5. Değişiklik yoksa (`git status --porcelain` boş): master'a dön, dalı sil (0.4-2), sonuç `sadece-takip`, `dal=None`, çıktı `Takip: değişiklik yok.`
6. Değişiklik varsa: `git add -A`, `git commit -q -m "Aylık trend + konu takibi (YYYY-AA-GG)"`, master'a dön; yazdır: `Takip '<dal>' dalında hazır; master değişmedi.` / `Onayla: python3 araclar/arsiv-guncelle.py --birlestir <dal>` / `Reddet: git branch -D <dal>`.
7. İstisna (`CalledProcessError`, `SystemExit`, `Exception`): geri alma `_geri_al_guvenli(dal, master_sha)` ile (yeni küçük yardımcı; `_uygula`'nın MEVCUT `:221-229` bloğu AYNEN kalır, yalnız `takip()` yenisini kullanır). Kurallar: (i) başlangıçta ağacın temiz olduğu `kirli_dosyalar() == []` ile doğrulanmış ve `master_sha = git rev-parse master` kaydedilmiştir; (ii) `reset --hard` ve `clean -fdq -- notlar` YALNIZ `git branch --show-current == <bu koşunun açtığı dal>` ise çalışır; değilse hiçbir şey silmez, `UYARI: geri alma yapılamadı (beklenmeyen dal); elle kontrol et` basar; (iii) sonra master'a dön, `master_sha` değiştiyse `UYARI`; (iv) `git branch -D` yalnız bu koşunun açtığı dalı siler. Sonuç `hata`, çıkış 1. Damga/özet dosyaları `.gitignore`'da olduğu için `clean` onlara dokunmaz. Test 30(e) ve yeni 30(g): başlangıçta temiz olmayan ağaçta `takip()` HİÇ başlamaz (reset çalışmaz); dal değişmişse geri alma reddedilir.
8. `_AYLIK_ICINDE` değilse sonucu damgalar.

**F) `aylik()` (yeni)** — sıra ve kararlar:
```
AYLIK ZİNCİR — <tarih>
0. Kilit: canlı pid → sys.exit (damga YAZMAZ; başka koşu sürüyor).
1. Kaçan ay: damga_oku(); son_calisma yok ya da > ESIK_KACAN_GUN (35) gün → "KAÇAN AY: son çalışma <N> gün önce (<tarih>). Bu koşu kaçan ayı da kapsar." (K kuralı, aşağıda)
2. Engeller listesi (yazma adımlarını kapatır; salt okuma adımları yine çalışır):
   - dal master değil           -> "dal '<x>' (master değil)"
   - kirli ağaç                 -> kirli_dosyalar() boş değil: HER ZAMAN engel (master'a otomatik commit YOK; reviewer düzeltmesi).
                                   NEDEN: "kirli ağaç (N dosya): <ilk 10>". Tüm kirli yollar URETILEN_NOTLAR'daysa NEDEN'e eklenir:
                                   "yalnız rapor dosyaları değişmiş (<adlar>); onayınla kaydet (git add <adlar> && git commit) ya da geri al
                                   (git checkout -- <adlar>)". aylik-ozet bunu karar_bekleyen yapar: "Rapor dosyaları değişmiş: kaydedilsin mi?"
   - bekleyen dal               -> bekleyen_dallar() boş değil: "bekleyen dal: <dal> (<gün> gün)" (log özeti ayrıca basılır)
   - gh yok / ağ yok            -> gh_hazir() başarısız: "GitHub'a ulaşılamıyor (<neden>)"
3. Rapor (A): gh varsa rapor() çalışır (engel olsa da; salt okuma). gh yoksa rapor() yerel moda düşer (3.1-B-1).
4. Liste raporu (B): gh varsa `github-skill-listesi.py` subprocess; çıkış≠0 ya da zaman aşımı -> "UYARI: yıldız listesi kontrolü yapılamadı" (zinciri durdurmaz; GraphQL bulutta çalışmaz).
4b. Başlangıç görüntüsü: `baslangic_temiz = (engel yok)`; `master_sha = git rev-parse master`. (Zincir içindeki geri alma kuralları bunlara dayanır.)
5. Engel YOKSA yazma adımı:
     degisen varsa -> kaynak_cek_atla_var() değilse ve sorunlu doluysa: sonuç kismi, neden "erişilemeyen kaynak var; kaynak-cek.py --atla yok (P7)"
                      aksi hâlde uygula(degisen, ayrinti, True)   [ATLANAN = sorunlu]
     degisen yoksa -> takip()
   Engel VARSA -> hiçbir dal açılmaz; sonuç kismi, neden = engellerin birleşimi.
6. Aylık özet: subprocess `python3 araclar/aylik-ozet.py --yazmadan` (kuru ise `--hizli`); stdout aynen basılır; çıkış kodu yok sayılır (hata → "UYARI: aylık özet üretilemedi"). `--yazmadan` = `proje-kullanimi.py` `--yaz`sız (0.2-e). Ardından özet-sonrası temizlik: `baslangic_temiz` ve şu an branch master ise `kirli_dosyalar()` yalnız `IZINLI_RAPOR_YOLLARI` içeriyorsa onları `git checkout -- <yol>` ile geri alır ve "Rapor dosyaları özet için üretilmişti; dalda zaten var, geri alındı" basar; başka kirli yol varsa dokunmaz, "UYARI: ağaç kirli (…); sonraki aylık koşu bunu engel sayar" der.
7. Damga: damga_yaz(sonuc, dal, neden, ATLANAN, ADI_DEGISEN) (kuru ise yazılmaz).
8. Son satırlar (görev metni bunları grep'ler):
     SONUÇ: guncellendi | sadece-takip | kismi | hata
     NEDEN: <tek satır>            (yalnız kismi/hata)
     DAL: <dal>                    (yalnız dal açıldıysa)
     ATLANAN KAYNAKLAR: a/b, c/d   (varsa)
     AD DEĞİŞMİŞ: eski -> yeni     (varsa)
   Çıkış: hata → 1; `--siki` ile kismi → 2; diğerleri 0.
```
`--kuru` ek davranışı: adım 5, 6'daki geri alma ve 7 çalışmaz (adım 6 `--hizli` ile salt okuma çalışır); çıktıya `PLAN: <ne yapılacaktı: güncelleme dalı / takip dalı / yalnız rapor (engeller: …)>` yazılır.

**K kuralı (kaçan ay telafisi).** Kaçan ay için ayrı bir telafi koşusu YOKTUR ve gerekmez: (a) `rapor()` karşılaştırmasını takvime değil registry'deki commit'e dayandırır (`:47-51, :60`), bir koşu birikmiş tüm kaynak değişikliklerini tek dalda yakalar; (b) dal adı koşunun ayını taşır; (c) trend/popüler/konu taraması anlık görüntüdür, geriye dönük doldurulmaz (kayıp yoktur, yalnız geçmiş seyrek kalır); (d) bekleyen dal varsa kaçan ay beklemede kalır ve `aylik-ozet` bunu "karar bekleyen" diye gösterir; (e) damga 35 günü aşınca her ajan oturumu (`aylik-ozet.py --hizli`) kullanıcıya sorar ve evet derse `--aylik` koşar (Claude zamanlayıcısı olmayan Codex/Antigravity için tek tetikleyici budur).

**G) `gecmis_yaz()` (`:104-138`)**: `ATLANAN` doluysa kayda bir madde: `- **Erişilemeyen (atlanan) kaynaklar** (N): `a/b`, … (arşiv kopyaları korundu; kaynaklar.json'da 'tip': 'KAYIP' yapılması kullanıcı kararı)`; `ADI_DEGISEN` doluysa `- **Adı değişmiş kaynaklar** (N): `eski` -> `yeni` (kaynaklar.json düzeltmesi kullanıcı kararı)`. Diğer satırlar aynen (aylik-ozet regex'leri bu iki satıra DOKUNMAZ).

**H) `_uygula()` (`:189-214`)**: (1) `:199`: `calistir(sys.executable, "araclar/kaynak-cek.py")` → `ATLANAN` doluysa `…, "--atla", ",".join(ATLANAN)` eklenmiş hâli. (2) `program-denetim` adımından (`:205-206`) hemen sonra tek yeni, `UYARI`'lı (zinciri durdurmayan) adım: `proje-kullanimi.py --saglik --yaz` yalnız `proje-kullanimi.py --help` çıktısında `--saglik` varsa (P5 gelmeden eski davranış); amaç `notlar/proje-durumu.md`'nin dal içinde tazelenip commit'lenmesi (0.2-e). `takip()` aynı adımı içerir. Başka adım değişmez. Hata yolu aynen.

**I) `uygula()` (`:156-175`)**: `:157-159` mesajı dosya listesiyle: `DURDU: kütüphanede kaydedilmemiş değişiklik var (N dosya): <ilk 10 yol>[ … +K]. Önce kaydet (git commit) ya da geri al. Aylık görev için: python3 araclar/arsiv-guncelle.py --aylik (kirli ağaçta salt okuma rapor üretir).` Davranış (exit) aynı.

**J) `birlestir()` (`:243-268`)**: `:244-246` mesajı iki deseni listeler; `:247-248` kirli mesaj dosya listeli; gerisi aynen. Böylece `takip/*` ve `guncelleme/*` AYNI yolla (kontrol + otomatik geri alma) birleşir; belgelerdeki `git merge --no-ff` yönergesi kalkar.

Değişmeyenler (bilerek): `rapor()`'un çıktı satır biçimleri (yeni satırlar eklenir), `calistir`, `git`, `etkilenen_projeler`, `_uygula` adım sırası, `birlestir` kontrol zinciri, kilit dosyası biçimi, `--dal`/`--uygula` anlamı.

---

### 3.2 `araclar/aylik-ozet.py` (yeni; salt okuma; ~320 satır; yalnız standart kütüphane)

**CLI**
```
python3 araclar/aylik-ozet.py                # TAM: araçları koşturur, notlar/aylik-ozet.md yazar, kısa özeti basar
python3 araclar/aylik-ozet.py --hizli        # UCUZ (oturum başı): ağ yok, yazma yok, ≤ ~10 sn, ≤ 15 satır. Takma ad: --oturum (aynı davranış; P8 metinlerinde --hizli yazılır)
python3 araclar/aylik-ozet.py --yazmadan     # TAM ama proje-kullanimi'na --yaz VERMEZ (arsiv-guncelle --aylik içinden; 0.2-e)
python3 araclar/aylik-ozet.py --ozet-json    # D4: stdout'ta tek JSON nesnesi, başka çıktı yok
python3 araclar/aylik-ozet.py --siki         # sonuç 'sorun' ise çıkış 1 (varsayılan her zaman 0)
gizli (test): --kok <dizin> (varsayılan ortak.KOK)  --cikti <md yolu>  --zaman-asimi <sn, 180>  --gorev-yolu <yol>  --arac-listesi-json <json> (varsayılan listeyi değiştirir)
```
Çıkış: 0 (araç doğru çalıştıysa bulgu ne olursa olsun); 1 yalnız `--siki` + `sorun`. Çıktı dışında yazdığı tek dosya `notlar/aylik-ozet.md` (yalnız tam modda; 0.1 kontrolü geçerse). Git'e yazmaz (`fetch`, `branch`, `commit` YOK; yalnız `branch --list`, `log`, `status`, `merge-base`, `show`, `check-ignore`, `rev-list`).

**Sabitler**: `ESIK_CALISMA=35`, `ESIK_CALISMA_SORUN=70`, `ESIK_RAPOR=45`, `ESIK_DAL=45`, `SATIR_SINIRI=300` (basılan her satır kırpılır; D9: araç yalnız bunu basar, `.env`/anahtar dosyası hiç açılmaz).
**Araç listesi tek kaynaktan (reviewer düzeltmesi).** `ARACLAR_TAM = ORTAK_LISTE + EK_TAM`, tekrarsız (anahtar `(ad, bayraklar)`):
- `ORTAK_LISTE`: `from ortak import OZET_ARACLARI` (P8'in listesi: `git-durum`, `yedek-denetim`, `genel-bekci`, `program-denetim`, `proje-kullanimi --saglik`; duman ile aynı liste, ayrışmaz). `ortak.py` import edilemezse ya da `OZET_ARACLARI` yoksa (P8 henüz inmedi) aynı beş araçlık sabit yedek kullanılır. Giriş `(ad, [bayraklar])`, `ad` `.py`'siz.
- `EK_TAM` (P4'e özgü; hepsi AĞSIZ, anında, yazmaz, `--ozet-json`): `("skill-ekle", ["--araclar"])` (P1: yapay-zeka-araclari.json yaşı/sürümleri), `("konu-takip", ["--bekleyenler"])`, `("github-trend", ["--bekleyenler"])`, `("populer-tarama", ["--bekleyenler"])` (P7). P8 isterse bunları da `OZET_ARACLARI`'na ekler (aylik-ozet tekrarlamaz).
- Tam modda `proje-kullanimi` girişine `--yaz` eklenir (0.2-d; `--yazmadan` ya da `--hizli` ise eklenmez).
- `ARACLAR_HIZLI`: `ARACLAR_TAM` içinden adı `{genel-bekci, git-durum, yedek-denetim}` olanlar + `EK_TAM`'ın dördü (hepsi yerel/ağsız). `program-denetim` ve `proje-kullanimi` hızlı modda KOŞMAZ. Araçlar en çok 4 paralel (`concurrent.futures.ThreadPoolExecutor`) koşar; hızlı modda toplam ≲ 10 sn. Not: rehber/14 yapay-zeka-araclari bayatlığını artık hızlı modda da gösterir.

**Veri yapısı**: kontrol = `{"ad", "durum": temiz|dikkat|sorun, "satirlar": [str], "karar_bekleyen": [str]}` (D4 ile aynı). Genel durum = en kötü kontrol; herhangi bir `karar_bekleyen` varsa en az `dikkat`.

**Fonksiyonlar (sırayla)**
1. `arac_kos(kok, ad, bayraklar, zaman_asimi)`: `[sys.executable, kok/araclar/<ad>, *bayraklar, "--ozet-json"]`, `cwd=kok`, `stdin=DEVNULL`, `capture_output`, `timeout`. Sonuç:
   - dosya yok → `dikkat`, "<ad>: araç kütüphanede yok (atlandı)";
   - `TimeoutExpired` → `dikkat`, "<ad>: zaman aşımı (<n> sn)";
   - çıkış ≠ 0 ve geçerli JSON yok → `dikkat`, "<ad>: çalışmadı (çıkış <k>): <stderr son satırı, 200 karaktere kırpık>";
   - stdout'tan JSON: önce tamamı, olmazsa SON `{` ile başlayan satır; şema doğrulama (`arac` str, `durum` ∈ üçlü, `satirlar` ve `karar_bekleyen` str listesi) bozuksa → `dikkat`, "<ad>: çıktı biçimi bozuk";
   - geçerliyse aynen kullanılır (çıkış kodu yok sayılır). Sonuca `calisti: bool` işareti konur (dosya yok / zaman aşımı / çalışmadı / bozuk → False); `bekleyen_notlar` yedek yolu buna bakar.
   Hiçbir araç hatası aylik-ozet'i düşürmez; her araç bağımsızdır.
2. `damga_kontrol(kok, bugun)`: `notlar/son-aylik-calisma.json` oku.
   - dosya yok (yeni makine, taze klon, damga hiç yazılmamış; damga ve özet git'te olmadığı için taze klonda hep böyledir): önce yedek tarih aranır: `notlar/guncelleme-gecmisi.md` ilk 60 satırında `^## (\d{4}-\d{2}-\d{2})` ile bulunan EN YENİ kayıt tarihi (izlidir, taze klonda da vardır). Bulunduysa `gun` bundan hesaplanır ve aşağıdaki 35/70 gün kuralı aynen uygulanır (satır: "Aylık çalışma damgası yok; son kayıtlı güncelleme <tarih> (<gun> gün önce)"). Bulunamazsa (ilk kurulum): durum `temiz`, satır "Aylık çalışma damgası yok (ilk kurulum ya da yeni makine); ilk aylık çalışma yapılınca oluşur", KARAR YOK (taze klonda her oturumda soru üretmez).
   - `gun = (bugun - date(son_calisma)).days`; `gun > 35` → `dikkat` (`> 70` → `sorun`), satır "Aylık çalışma <gun> gündür yapılmadı (son: <tarih>) — kaçan ay var"; karar aynı soru.
   - `son_sonuc` ∈ {kismi, hata, durduruldu} → `dikkat`, satır "Son çalışma yarım kaldı: <son_sonuc> — <son_neden>"; `son_basarili` 35 günden eskiyse ek satır "Son başarılı çalışma <n> gün önce".
   - temizse satır "Son aylık çalışma <tarih> (<gun> gün önce): <son_sonuc>". `atlanan_kaynaklar` doluysa bilgi satırı "Erişilemeyen kaynak(lar): … (kalıcıysa kaynaklar.json'da tip KAYIP yapılması senin kararın)" ve karar satırı bu cümlenin kısa hâli. `ad_degisen` doluysa satır + karar "Adı değişen kaynak: eski → yeni; kaynaklar.json düzeltilsin mi?".
3. `dal_kontrol(kok, bugun)`: `git branch --list 'guncelleme/*' 'takip/*'`; yaş (`git log -1 --format=%ct <dal>`); `merge-base --is-ancestor`.
   - her dal: satır "Bekleyen dal <dal> (<gun> gün önce hazırlandı)"; karar "<dal> dalı onayını bekliyor: incelenip birleştirilsin mi? (promptlar/08)"; `gun > 45` → `dikkat` + satır "<dal> 45 günden eski; birleştir ya da sil".
   - `guncelleme/*` dalının `notlar/guncelleme-gecmisi.md`'si `git show <dal>:notlar/guncelleme-gecmisi.md` (ilk 80 satır) okunur: regex `\*\*Karar bekleyen yeni skiller\*\* \((\d+)` ve `\*\*Yeniden incelenecek\*\* \((\d+)\)`; N>0 → karar "<dal>: <N> yeni skill karar bekliyor (kaynaklar.json 'dahil'/'haric')" / "<dal>: <N> skill yeniden incelenecek (rehber/07)".
   - `birlesmis` dal → satır "<dal> zaten master'a birleşmiş; silebilirsin (git branch -d <dal>)", karar YOK.
   - git yoksa/depo değilse `temiz` + satır "git deposu değil".
4. `rapor_yasi(kok, bugun)`: tablo (ad, dosya, tarih kaynağı). Tarih bulunamazsa satır "tarih okunamadı", durum etkilenmez; > 45 gün → `dikkat`:
   `github-trend` (`trend.json` → `son_tarama`), `konu-takip` (`konu-takip.json` → `konular.*.son_tarama` en yenisi; yoksa md regex `Son tarama: (\d{4}-\d{2}-\d{2})`), `populer-skiller` (`notlar/populer-skiller.md` 3. satır ilk tarih), `program-denetimi` (md 3. satır), `yol-denetimi` (md 3. satır), `DURUM.md` (`notlar/hf-om-gecisi/DURUM.md`, `Son güncelleme: (tarih)`; dosya yoksa atlanır).
5. `bekleyen_notlar(kok)` (karar bekleyenler; her ayrıştırma kendi `try/except` içinde; hata → satır "okunamadı: <dosya>", çökme yok). **Birincil yol: araç çıktısı.** Aday sayıları ve adları `konu-takip`, `github-trend`, `populer-tarama` `--bekleyenler --ozet-json` kontrollerinin (EK_TAM) `karar_bekleyen`'inden gelir; markdown başlıkları/cümleleri regex'le OKUNMAZ (P7 rapor biçimini değiştirebilir). **Yedek yol (regex)** yalnız ilgili kontrolün `calisti == False` olduğunda (araç yok/çalışmadı/bozuk çıktı) ve md dosyası varsa:
   | Kaynak | Ayrıştırma (yalnız yedek) | Üretilen karar |
   |---|---|---|
   | `notlar/konu-takip.md` | `\*\*odaklı aday: (\d+)\*\*` değerlerinin toplamı | "<N> odaklı aday repo karar bekliyor (notlar/konu-takip.md)" |
   | `notlar/populer-skiller.md` | `^## Yeni adaylar \((\d+)\)` | "<N> yeni aday repo (notlar/populer-skiller.md)" |
   | `notlar/github-trend.md` | başlık `## Son taramada trend'de olup kütüphanede olmayan repolar` sonrası tablo; `\|\s*([^\|]+?)\s*\|\s*(\d+)\s*\|`, sayı > 0 | "<N> trend aday repo (SKILL.md içeren; notlar/github-trend.md)" |
   | `notlar/program-denetimi.md` | yalnız `program-denetim` kontrolü çalışmadıysa; `\|` satırında `YENİ SÜRÜM VAR`; ilk hücre program adı | "<program>: yeni sürüm var, güncelleme onayı bekliyor (rehber/11)" |
   Yedek yol kullanıldığında kontrol satırına "yedek okuma (araç çalışmadı)" notu düşer. Regex bozulursa "okunamadı", çökme yok.
   **Her zaman (araçtan bağımsız): `notlar/kararlar.md` (P8).** (a) `## Karar bekleyenler` bölümündeki `^\s*[-*]\s*\[ \]\s+(.+)$` kutuları karar olarak eklenir (satırın kendisi, kırpık). (b) `## Kabul edilen bekleyenler` bölümü (aşağıda 5b).
   **5a. Aday triyajı (B2 'aylık en fazla N aday' kuralının özet kısmı; reviewer boşluğu).** Üç aday aracının her birinin `karar_bekleyen` listesi özette TEK satıra indirilir: "<arac>: <N> aday karar bekliyor; ilk 5: a, b, c, d, e (… +K daha; tam liste: notlar/aylik-ozet.md)" ve kapatma yönergesi ("konu-takip.py --karar owner/ad eklendi|reddedildi|izle"). `ADAY_GOSTER = 5`. Tam liste md'de durur. Aday sayısı `len(karar_bekleyen)` olarak sayılır (araçlar en çok 10/konu listeler; "en az N" ifadesi kullanılır). Aylık kaç adayın karara bağlanacağı (N) kullanıcı sorusudur: `notlar/kararlar.md` → "Henüz sonuçlanmamış sorular" (P8 el değiştirmesi, bölüm 6); sorunun cevabı gelene kadar özet yalnız gösterir, sınır koymaz.
   **5b. Kabul edilenler (kapanmış kararlar tekrar çıkmaz).** `notlar/kararlar.md`'de `## Kabul edilen bekleyenler (aylık özette susturulur)` başlığı altındaki her `- <ifade>` satırı (isteğe bağlı sonek ` | AAAA-AA-GG`: bu tarihten sonra susturma biter) bir süzgeçtir: herhangi bir araç/kaynak karar cümlesi, ifadeyi (küçük harf, en az 8 karakter) İÇERİYORSA özetten çıkarılır ve satırlar tarafında "(kabul edildi: susturuldu)" sayımı tutulur. Yalnız `karar_bekleyen` süzülür, `durum` ve dikkat satırları etkilenmez. Böylece P3/P5/P6'nın tekrarlayan cümleleri tek ortak listeyle kapatılır (P2 taban 'kabul edildi'si ayrı kalır). Eksik/bozuk başlık → süzgeç yok, çökme yok.
   **5c. Kayıp (erişilemeyen) kaynak, ayda bir kez.** Damga `atlanan_kaynaklar` her koşuda yeniden yazıldığı için aynı kayıp her ay çıkabilirdi. Kural: kaynak `kaynaklar.json`'da `tip == "KAYIP"` (kararı verilmiş ve işaretlenmiş) ise karar OLUŞMAZ, yalnız bilgi satırı "KAYIP işaretli kaynak: <repo>"; değilse karar: "<repo> kaynakta erişilemiyor: KAYIP olarak işaretlensin mi? (rehber/03 E3; kaynak-cikar.py --repo <repo> --kuru)". İşaretlemeyi yazan ayrı bir bayrak YOKTUR (kasıtlı: P7'nin `rehber/03` E3 adımı elle, onayla; `kayip_tarihi` orada yazılır); `--kayip-isaretle` P4'te de P7'de de yapılmaz (P7'nin `kaynak-cikar.py` dışında yazan bayrak olmadığını belgelemesi istenir, bölüm 6). Kullanıcı "kabul ediyorum, işaretleme" derse ifade 5b listesine girer.
   `DURUM.md` düzyazısı ayrıştırılmaz (yanlış pozitif; bölüm 8).
   Sayı 0 ise karar üretilmez. Rapor dosyası yoksa sessiz atlanır.
6. `gorev_kopyasi_kontrol(kok, gorev_yolu)`: `<kok>/zamanlanmis/aylik-guncelleme.SKILL.md` ile canlı dosyanın (`~/.claude/scheduled-tasks/skill-kutuphanesi-aylik-guncelleme/SKILL.md`; `--gorev-yolu` ile değişir) SHA-256'sı; canlı dosya yoksa (başka makine/araç) bilgi satırı yok; farklıysa BİLGİ satırı (durum etkilemez, `duman-testi` "0 uyarı" kuralını bozmasın diye): "Zamanlanmış görev metni kütüphane kopyasından farklı; güncellemek için onay gerekir (rehber/02 'Zamanlanmış görev')". Karar: "Zamanlanmış görev metni güncellensin mi?" yalnız kütüphane kopyası canlıdan YENİ ise değil, farklıysa (iki yön de kullanıcıya sorulur). Yalnız TAM modda.
7. `yerel_git(kok)` (yalnız `--hizli`; `git-durum` yedeği): `git status --porcelain -z | sayı`, `git rev-list --left-right --count origin/master...master` (ağ yok; son bilinen uzak izle); satırlar "Kaydedilmemiş değişiklik: N dosya", "Uzaktan <n> commit önde (gönderilmedi)". `git-durum.py` varsa hızlı modda o tercih edilir ve bu fonksiyon atlanır.
7b. `rapor_degisti_kontrol(kok)` (yalnız tam mod, `git status --porcelain -z`): kirli yollar tümüyle `IZINLI_RAPOR_YOLLARI` ya da `notlar/proje-kullanimi.md`/`notlar/yol-denetimi.md` içindeyse karar "Rapor dosyaları yenilendi (<adlar>): kaydedilsin mi? (git add … && git commit, onayınla)"; başka kirli yol varsa bilgi satırı "Kütüphanede kaydedilmemiş değişiklik: N dosya" (karar yok; git-durum zaten gösterir). `--yazmadan` modunda (zincir içi) bu kontrol atlanır (aylik() kendi geri alma adımını yapar).
8. `birlestir_ozet(...)`: genel durum, `karar_bekleyen` birleşik liste (tekrarlar elenir; 5b süzgeci uygulanır; sıra: damga → dal → rapor dosyaları kararı → programlar/araçlar → aday özet satırları → kararlar.md kutuları). `--hizli` çıktısı en çok 3 karar + 3 dikkat maddesi gösterir (toplam ≤ 15 satır).
9. Çıktılar: `md_yaz`, `ozet_metni`, `ozet_json`.

**`notlar/aylik-ozet.md` biçimi** (yalnız tam mod; her seferinde yeniden yazılır):
```
<!-- aylik-ozet: {"zaman":"2026-12-01T10:41:07+03:00","mod":"tam","durum":"dikkat","araclar":{"genel-bekci":"temiz","git-durum":"dikkat"},"karar_sayisi":3} -->
# Aylık Özet

> `araclar/aylik-ozet.py` üretir · 2026-12-01 · salt okuma · git'e girmez (yerel). Hızlı kontrol: `python3 araclar/aylik-ozet.py --hizli`

## Durum: DİKKAT

## Senin kararını bekleyenler (3)
1. …

## Aylık çalışma
Son çalışma 2026-11-02 (29 gün önce): guncellendi · son başarılı: aynı

## Kontroller
| Kontrol | Durum | Özet |
|---|---|---|
| genel-bekci | temiz | … |
### genel-bekci
- satır…

## Rapor yaşları
| Rapor | Son tarih | Gün | Durum |
```
`--hizli` aynı md'yi OKUR (yalnız ilk satırdaki yorum JSON'u): "Son tam özet: <zaman> (<n> gün önce) durum <durum>"; tam özet 45 günden eskiyse `dikkat` satırı.

**Özet metni (stdout) ve `--ozet-json`**
- Metin biçimi ve cümleler bölüm 4'te. `--ozet-json`: `{"arac":"aylik-ozet","durum":…,"satirlar":[ozet metni satırları],"karar_bekleyen":[…]}`; bu modda md yine yazılır (tam mod) ama stdout'a yalnız JSON gider; `--hizli --ozet-json` birlikte desteklenir (yazma yok).
- `--siki`: `durum == "sorun"` → çıkış 1.

**Davranış garantileri**: araç ağ kullanmaz (alt araçlar kullanabilir: yalnız `program-denetim`); `--hizli` alt süreç olarak yalnız `ARACLAR_HIZLI` + `git` koşturur, her biri `timeout=20`; herhangi bir alt kontrol istisnası o kontrolün `dikkat` satırına çevrilir; hiçbir koşulda Traceback basılmaz (`main()` en dışta yakalar: "UYARI: aylık özet tamamlanamadı: <neden>", çıkış 0).

---

### 3.3 `zamanlanmis/aylik-guncelleme.SKILL.md` (yeni; kütüphane kopyası, bölüm 4'te tam metin)
Yeni klasör `zamanlanmis/`. İçerik canlı görev metninin önerilen yeni hâlidir (bölüm 4.4). Kütüphane kopyası KAYNAK DOĞRUDUR: değişiklik önce burada yapılır, kullanıcı onayıyla canlıya kopyalanır. `aylik-ozet.py` iki dosyanın farkını bilgi olarak gösterir (3.2-6). Kapsam tarayıcıları dokunmaz (`zamanlanmis/` `arsiv/` dışında; kontrol: bölüm 10 grep'i).

### 3.4 `rehber/02-guncelleme-yonergesi.md` (düzenleme)
Eski → yeni (satır numaraları dosyanın şimdiki hâli):
- `:13` kutu notuna ekle: "Güncelleme sürerken…" cümlesinden sonra "Bekleyen bir dal varken yeni dal açılmaz; dal 45 günden eskiyse rapor uyarır."
- `:32-33` "Otomatik aylık rapor" maddesi → şu metinle değiştir: "**Aylık zincir tek komut:** `python3 -u araclar/arsiv-guncelle.py --aylik` (zamanlanmış görev bunu her ayın 1'inde 10:00'da çalıştırır; elle de çalıştırılabilir, Codex/Antigravity oturumunda da). Sırası: ön kontrol → kaynak raporu → yıldız listesi raporu → (değişiklik varsa) `guncelleme/YYYY-AA` dalı, (yoksa) `takip/YYYY-AA` dalı → aylık özet → damga. **Birleştirmez.**" ve ardından bölüm 4.5'teki "sonuç tablosu".
- `:36` ve `:37` arasına: "`--birlestir` hem `guncelleme/*` hem `takip/*` dalı için tek yoldur (kontroller + otomatik geri alma). `git merge --no-ff` ile elle birleştirme KULLANILMAZ."
- `:41-59` adım listesine ekle: `-1. gelistirici-bilgisi.py` (`arsiv-guncelle.py:189`), `2b. yol-tara.py` (sabit yol taraması → `notlar/yol-denetimi.md`, hata zinciri durdurmaz), `2c. program-denetim.py` (→ `notlar/program-denetimi.md`, hata zinciri durdurmaz). Sıra kodla aynı olmalı (`:189-214`).
- Yeni bölüm `## 1b) Aylık zincir tek komut, kaçan ay, çevrimdışı` (`:39` ile `:41` arasına): komut, `--kuru` (yan etkisiz plan), ön kontrol/engel tablosu (kirli ağaç, master değil, bekleyen dal, GitHub yok), "kısmi" sonucun anlamı, **kaçan ay kuralı (K)**, çıkış kodları (rapor modu 0/1/**2**), damganın yeri ve "bu makineye özgü, git geçmişinde yok" notu, oturum başı `aylik-ozet.py --hizli`, `gh auth login` yönergesi ("kendi terminalinde `gh auth login`; tarayıcıda onayla; sonra `--aylik`").
- `## 1b` içine "**Asıl tetik**" paragrafı: aylık zincirin asıl tetiği oturum başı `aylik-ozet.py --hizli`'nin damga yaşı kuralıdır (35 gün); zamanlanmış görev yalnız kolaylıktır, her araçta (Claude, Codex, Antigravity, Cursor, Copilot) aynı komut çalışır. Kirli ağaç kuralı: master'da rapor dosyaları dahil kaydedilmemiş değişiklik varsa zincir yazma adımını yapmaz (`kismi`); commit için kullanıcı onayı gerekir (otomatik commit yok). Tam özet (`aylik-ozet.py`, tüm kontroller) ayda bir ya da kullanıcı isteyince; hızlı özet yalnız yerel/ağsız kontrolleri ve `yapay-zeka-araclari.json` bayatlığını gösterir. Kabul edilen bekleyenler `notlar/kararlar.md` 'Kabul edilen bekleyenler' bölümüne yazılır (özette bir daha çıkmaz); kayıp kaynak kararı rehber/03 E3.
- Yeni bölüm `## 1c) Zamanlanmış görev metni`: kopya `zamanlanmis/aylik-guncelleme.SKILL.md`, canlı yol, **değiştirme prosedürü (kullanıcı onayı gerekir)**: (1) `diff -u <canlı> zamanlanmis/aylik-guncelleme.SKILL.md` göster; (2) yedek: `cp <canlı> ~/Documents/Claude/yedek/zamanlanmis-gorev-<tarih>.SKILL.md`; (3) kopyala: `cp zamanlanmis/aylik-guncelleme.SKILL.md <canlı>`; (4) doğrula: `cmp` ve `python3 araclar/arsiv-guncelle.py --aylik --kuru`; geri alma = yedeği geri kopyalamak. "Zamanlayıcı Mac uykudayken ya da Claude uygulaması kapalıyken tetiklenmez; kaçırılan görevin sonradan çalışıp çalışmadığı doğrulanmadı."
- `:94-98` "Geri alma": ekle: birleştirme commit'i için `git revert -m 1 <birleştirme-commit>` (`--no-ff` birleştirme olduğu için `-m 1` şart); push edilmişse geri alma da yeni bir commit'tir ve `git push origin master` ile ayrıca (kullanıcı isteyince) gönderilir; **force-push yok**. (B5'in `rehber/02` parçası; P3 bu parça için dosyaya dokunmaz.)
- `:124-126` 3b: "`--uygula` durur" → "`--uygula` artık erişilemeyen kaynağı atlar, arşiv kopyasını korur ve raporlar (kaynak-cek.py `--atla` destekliyorsa; yoksa eskisi gibi durur). Kalıcıysa `tip`'i `KAYIP` yap." ve 3c'ye: "`arsiv-guncelle.py` raporu da `AD DEĞİŞMİŞ` satırı basabilir (commit yanıtındaki `html_url`'den); asıl kaynak `github-skill-listesi.py` raporudur."
- `:148-156` takvim tablosuna satırlar: "Ayda bir | `arsiv-guncelle.py --aylik`", "Her oturum başında | `aylik-ozet.py --hizli`", "Kaçan ay | aynı komut; tek koşu hepsini kapsar".
- `:152-153` "İstediğin zaman" satırlarına "(aylık zincirde de çalışır)" ekle.

### 3.5 `promptlar/08-aylik-guncelleme-onayi.md` (yeniden yazım; tam metin bölüm 4.6)
`kopyala` bloğu korunur; kapsam genişler: `guncelleme/*` + `takip/*`, `sonuç: kismi`, karar bekleyenler, program/proje, kaçan ay.

### 3.6 `notlar/son-aylik-calisma.json`
Dosya KAYIT bu pakette TOHUM olarak yazılmaz (kütüphanede izlenmez); ilk gerçek `--aylik`/`--damga-yaz` koşusu oluşturur. Biçim 3.1-D. Dosya yokken `aylik-ozet` "damga yok" der (bu bir hata değil, ilk kez durumudur).

### 3.7 `araclar/testler/test_p4-aylik.py` — bölüm 5.

---------------------------------------------------------------------------------------------------------------------

## 4. User-facing texts (Türkçe, çıktıda göründüğü gibi)

### 4.1 `aylik-ozet.py` tam mod stdout
```
Aylık özet — 2026-12-01 · durum: DİKKAT
Aylık çalışma: son çalışma 2026-11-02 (29 gün önce), sonuç: guncellendi.
Senin kararını bekleyen 3 şey:
  1. guncelleme/2026-11 dalı onayını bekliyor: incelenip birleştirilsin mi? (promptlar/08)
  2. hyperframes: yeni sürüm var, güncelleme onayı bekliyor (rehber/11)
  3. konu-takip: en az 4 aday karar bekliyor; ilk 5: a/b, c/d, e/f, g/h (kapatmak: konu-takip.py --karar owner/ad eklendi|reddedildi|izle)
Dikkat gerektirenler:
  • git-durum (dikkat): Uzaktan 9 commit önde (gönderilmedi)
  • rapor yaşı (dikkat): populer-skiller 48 gün eski
Ayrıntı: notlar/aylik-ozet.md
```
Damga yoksa ve yedek tarih de yoksa: `Aylık çalışma: damga yok (ilk kurulum ya da yeni makine).` (soru yok). Karar yoksa: `Senin kararını bekleyen bir şey yok.` Dikkat yoksa: `Dikkat gerektiren bir şey yok.` (en çok 8 madde, fazlası `… +K daha: notlar/aylik-ozet.md`).

### 4.2 `--hizli` stdout
Her şey temizse tek satır: `Aylık özet (hızlı): her şey yolunda · son aylık çalışma 12 gün önce (guncellendi).`
Aksi hâlde 4.1 biçimi, başlık `Aylık özet (hızlı kontrol) — <tarih> · durum: <DURUM>`, sonda `Tam özet için: python3 araclar/aylik-ozet.py`. Hızlı çıktı en çok 15 satır (3 karar + 3 dikkat maddesi + başlıklar).

### 4.3 `arsiv-guncelle.py` yeni/değişen mesajlar
- `UYARI: GitHub'a ulaşılamıyor (<neden>). Kaynak karşılaştırması ATLANDI; yalnız yerel kontroller yapıldı.`
- `! <repo>: erişilemiyor (silinmiş, private ya da adı değişmiş olabilir). Arşiv kopyası korunuyor. İpucu: B adımındaki github-skill-listesi.py "AD DEĞİŞMİŞ" satırına bak.`
- `! <repo>: şimdilik kontrol edilemedi (<hata>)` · `UYARI: art arda 3 kaynak kontrol edilemedi; kalanlar atlandı (ağ/hız sınırı).`
- `~ AD DEĞİŞMİŞ: <eski> -> <yeni> (yeni kaynak DEĞİL; kaynaklar.json'da 'repo'yu yeni adla değiştir, eski adı "eski_adlar"a yaz; rehber/09)`
- `UYARI: erişilemeyen kaynak(lar) atlanacak (arşiv kopyaları korunur): a/b, c/d`
- `DURDU: N kaynak şimdilik kontrol edilemedi (geçici ağ/hız sınırı: …). Sonra tekrar çalıştır. Hiçbir şey değişmedi.`
- `Onay bekleyen dal: <dal> (<N> gün önce hazırlandı)` · `UYARI: <dal> 45 günden eski: birleştir (--birlestir <dal>) ya da sil (git branch -D <dal>).` · `<dal> zaten master'a birleşmiş; silebilirsin: git branch -d <dal>`
- `DURDU: kütüphanede kaydedilmemiş değişiklik var (N dosya): <yollar>. Önce kaydet (git commit) ya da geri al. Aylık görev için: python3 araclar/arsiv-guncelle.py --aylik (kirli ağaçta salt okuma rapor üretir).`
- `KAÇAN AY: son çalışma <N> gün önce (<tarih>). Bu koşu kaçan ayı da kapsar.`
- `Takip: değişiklik yok.` · `Takip '<dal>' dalında hazır; master değişmedi.` · `Onayla: python3 araclar/arsiv-guncelle.py --birlestir <dal>` · `Reddet: git branch -D <dal>`
- `AYLIK ZİNCİR — <tarih>` · `Ön kontrol: kirli ağaç (N dosya): …` · `yalnız rapor dosyaları değişmiş (<adlar>); onayınla kaydet ya da geri al` · `PLAN: …` · `SONUÇ: …` `NEDEN: …` `DAL: …` `ATLANAN KAYNAKLAR: …` `AD DEĞİŞMİŞ: …`
- `UYARI: notlar/son-aylik-calisma.json .gitignore'da değil; ağacı kirletmemek için yazılmadı (P3 .gitignore satırı eksik).`
- Çıkış kodu 2 açıklaması (docstring): `2 = GitHub'a ulaşılamadı ya da bazı kaynaklar kontrol edilemedi (yalnız yerel kontroller yapıldı)`.

### 4.4 `zamanlanmis/aylik-guncelleme.SKILL.md` — tam metin
````markdown
---
name: skill-kutuphanesi-aylik-guncelleme
description: Ayda bir skill kütüphanesinin aylık zincirini çalıştırır (rapor, güncelleme ya da takip dalı, aylık özet); master'ı değiştirmez, birleştirme kullanıcı onayıyla.
---

Görev: ~/Documents/SkillKutuphanesi skill kütüphanesinin AYLIK ZİNCİRİNİ çalıştır ve raporla. Yanıtı Türkçe yaz.
(Bu metnin kütüphanedeki kopyası `zamanlanmis/aylik-guncelleme.SKILL.md`'dir; değişiklik önce orada yapılır, canlı dosya kullanıcı onayıyla güncellenir.)

Kesin kurallar:
- `master` dalını elle DEĞİŞTİRME. Birleştirme (`--birlestir`) YAPMA; bu her zaman kullanıcının onayıyla, ayrı bir oturumda yapılır.
  İstisna YOK: master'a commit de atma. `--aylik` komutu master'da kirli ağaç görürse (rapor dosyaları dahil) yazma adımını yapmaz ve nedenini yazar; commit için kullanıcıdan onay iste.
- Global skill klasörlerine (~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage) ve kullanıcının projelerine dokunma.
- push yapma, PR açma (kütüphanenin GitHub deposu `ulukayasaban/SkillKutuphanesi` private; push/PR sadece kullanıcı isteyince, ayrı oturumda). Başka hiçbir GitHub reposunda işlem yapma. `arsiv/` altındaki skill dosyalarını elle düzenleme. GitHub'da yıldız/liste değiştirme; yeni kaynak EKLEME (sadece aday olarak raporla).
- `git reset --hard`, `git clean`, `git branch -D` kendi başına ÇALIŞTIRMA (komutun kendi açtığı ve kendi geri aldığı dal dışında hiçbir şeye dokunma).
- Hiçbir dalı SİLME (komutun kendi açtığı ve kendi geri aldığı dal hariç). Bekleyen eski dalları olduğu gibi bırak.
- Bir adım hata verirse dur, hatayı olduğu gibi raporla; kendi başına düzeltmeye çalışma. Kaynak dosyalarını (kaynaklar.json, registry.json…) elle değiştirme.

Adımlar:
1. `cd ~/Documents/SkillKutuphanesi && python3 -u araclar/arsiv-guncelle.py --aylik` komutunu çalıştır (15–40 dk sürebilir; bitmesini bekle, çıktısını sonuna kadar oku). Komut (zamanlanmış görev metnine ya da Claude eklentisine bağlı değildir; Codex/Antigravity oturumu da aynısını çalıştırır) kendisi sırayla şunları yapar: ön kontrol (master mı, ağaç temiz mi, bekleyen dal var mı, `gh` oturumu var mı), kaynak raporu, yıldız listesi raporu (`github-skill-listesi.py`), kaynaklarda değişiklik varsa `guncelleme/YYYY-AA` dalında güncelleme, yoksa `takip/YYYY-AA` dalında trend + popüler + konu + program + yol taraması, aylık özet (`aylik-ozet.py`) ve damga (`notlar/son-aylik-calisma.json`). Çıktının son satırları: `SONUÇ:`, varsa `NEDEN:`, `DAL:`, `ATLANAN KAYNAKLAR:`, `AD DEĞİŞMİŞ:`; ayrıca `KAÇAN AY:` satırı olabilir.
2. Komut hiç başlamadıysa ya da Traceback ile bittiyse (zamanlanmış görev asıl tetik değildir: damga 35 günü aştığında her oturum başında `aylik-ozet.py --hizli` kullanıcıya sorar): `python3 araclar/arsiv-guncelle.py --damga-yaz durduruldu --neden "<tek cümle neden>"` çalıştır, sonra `python3 araclar/aylik-ozet.py`; ikisini raporla ve dur.
3. `SONUÇ: guncellendi` ya da `SONUÇ: sadece-takip` ise dalı incele (`<dal>` = `DAL:` satırı): `git branch --show-current` (master olmalı), `git status --short` (boş olmalı), `.guncelleme-kilidi` YOK; `git log --oneline master..<dal>`, `git diff --stat master...<dal> | tail -1`, `git show <dal>:notlar/guncelleme-gecmisi.md | head -30` (guncelleme dalında), `git show <dal>:notlar/github-trend.md | head -60`, `git show <dal>:notlar/konu-takip.md | head -80`.
4. `SONUÇ: kismi` ise güncelleme yapılmadı; `NEDEN:` satırını olduğu gibi aktar ve kullanıcıya ne yapacağını söyle: kirli ağaç → listelenen dosyaları kaydetmesi (git commit) ya da geri alması; bekleyen dal → `promptlar/08` ile incelemesi; "GitHub'a ulaşılamıyor" → kendi terminalinde `gh auth login` yapması, sonra aynı komutu yeniden çalıştırması (yerel kontroller yine de çalıştı); "master değil" → master'a dönmesi. Komutun yaptığı salt okuma raporları ve aylık özet bu durumda da geçerlidir.
5. `SONUÇ: hata` ise komut dalını kendi geri aldı; hata satırını aktar, tekrar deneme.
6. Kaçan ay: çıktıda `KAÇAN AY:` satırı varsa raporun başına "Son çalışma <N> gün önce; bu koşu kaçan ayı da kapsıyor" yaz. Ayrı bir telafi adımı YOK: karşılaştırma tarihe değil kayıtlı commit'e dayanır.

Rapor biçimi:
- Başlık: "SkillKutuphanesi aylık güncelleme — <tarih>"
- **Sonuç:** güncellendi (dal adı) / sadece takip (dal adı ya da "değişiklik yok") / kısmi (neden) / hata
- **Kaçan ay:** varsa `KAÇAN AY:` satırı; yoksa "yok"
- **Güncellenen kaynaklar:** tablo (repo · eski→yeni commit · değişen skill dosyası) ya da "yok" (guncelleme-gecmisi.md kaydından)
- **Etkilenen skiller:** içeriği değişen, yeni eklenen, kaynakta kaldırılan, yeniden incelenecek
- **Etkilenen projeler:** arsiv-guncelle çıktısındaki "Bu kaynaklardan skill kullanan projeler"; öneri: `skill-ekle.py <proje> --durum` / `--guncelle --kuru`. Projelere dokunma.
- **Erişilemeyen ve adı değişen kaynaklar:** `ATLANAN KAYNAKLAR:` ve `AD DEĞİŞMİŞ:` satırları ile çıktıdaki "KİMLİK KORUNDU", "KİMLİK DEVRİ", "ÇAKIŞMA" satırları (yoksa "yok"). Karar kullanıcınındır (kaynaklar.json: `tip: KAYIP`, `eski_adlar`, `ad_devral`).
- **GitHub trend / Konu takibi / Yeni yıldızlanan repolar:** ilgili dosyalardan (adaylar EKLENMEZ).
- **Senin kararını bekleyenler:** aylık özetin "Senin kararını bekleyen N şey" listesi AYNEN.
- **Dikkat gerektirenler:** aylık özetin "Dikkat gerektirenler" listesi AYNEN.
- **Kullanıcının yapması gereken:** dalı inceleyip onaylarsa "güncelleme dalını birleştir" demesi (her iki dal türü için: `python3 araclar/arsiv-guncelle.py --birlestir <dal>`; kontroller geçmezse master kendiliğinden geri döner); reddederse `git branch -D <dal>`. Aday eklemek isterse "şu adayları ekle" (rehber/03-yeni-skill-ekleme.md). Birleştirmeden sonra yeniden incelenecek skiller ve projeler için `skill-ekle.py <proje> --durum`.
- **GitHub (isteğe bağlı) hatırlatması:** raporun sonuna şu notu MUTLAKA ekle: "GitHub'a göndermek istersen: (a) birleştirmeden ÖNCE inceleme kaydı için 'dalı push et ve PR aç' de → `git push -u origin <dal>` + `gh pr create --base master --head <dal>`; (b) birleştirmeden SONRA 'GitHub'a gönder' de → `git push origin master` (PR açıldıysa kendiliğinden merged olur) + `git push origin --delete <dal>`. Güncelleme PR'ı GitHub'daki Merge düğmesiyle birleştirilmez; birleştirme her zaman yerelde `--birlestir` ile yapılır (rehber/02, 'GitHub'a gönderme')."
````

### 4.5 rehber/02 "sonuç tablosu" (1b bölümünde)
| `SONUÇ:` | Anlamı | Ne yapılır |
|---|---|---|
| `guncellendi` | kaynaklarda değişiklik vardı; `guncelleme/YYYY-AA` dalı hazır | incele, onayla (`--birlestir`) ya da reddet (`git branch -D`) |
| `sadece-takip` | değişiklik yoktu; `takip/YYYY-AA` dalı (ya da "değişiklik yok") | aynı |
| `kismi` | yazma adımı yapılmadı (kirli ağaç, bekleyen dal, master değil, GitHub yok); salt okuma raporları ve özet çalıştı | `NEDEN:` satırındaki işi yap, sonra yeniden çalıştır |
| `hata` | bir adım düştü; koşunun kendi açtığı dal geri alındı | hatayı oku |

### 4.6 `promptlar/08-aylik-guncelleme-onayi.md` — tam metin
````markdown
# 08 — Aylık Zincir Sonucunu İnceleme ve Onay

**Ne zaman:** Ayın 1'indeki otomatik görev (ya da elle `python3 -u araclar/arsiv-guncelle.py --aylik`) "güncelleme `guncelleme/YYYY-AA` dalında hazır", "takip `takip/YYYY-AA` dalında hazır" ya da "kısmi" dedi; ya da oturum başındaki hızlı özet "aylık çalışma 35 günden fazladır yapılmadı" dedi.
**Nerede:** `~/Documents/SkillKutuphanesi` klasöründe.

```kopyala
Skill kütüphanemin aylık zincir sonucunu incele. ~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/02-guncelleme-yonergesi.md'yi oku.
1. Önce özeti çalıştır ve bana oku: python3 araclar/aylik-ozet.py ("Senin kararını bekleyen" listesi ve "Dikkat gerektirenler").
   Son çalışma 35 günden eskiyse bana sor: "Aylık çalışmayı şimdi yapayım mı?" Evet derse python3 -u araclar/arsiv-guncelle.py --aylik
   (tek koşu kaçan ayı da kapsar; ayrı telafi yok). Özet "rapor dosyaları değişmiş, kaydedilsin mi?" derse bana sor; onaylarsam git add <o dosyalar> && git commit.
   Bir kararı bana sorduktan sonra "kabul ettim" dersem notlar/kararlar.md 'Kabul edilen bekleyenler' bölümüne ifadeyi yaz (özette tekrar çıkmasın).
2. Bekleyen dalları bul: git branch --list 'guncelleme/*' 'takip/*'
3. Her dal için göster: git log --oneline master..<dal>, git diff --stat master...<dal> | tail -1.
   guncelleme/* dalında ayrıca git show <dal>:notlar/guncelleme-gecmisi.md'nin en üstteki kaydı; takip/* dalında
   git show <dal>:notlar/github-trend.md | head -60 ve git show <dal>:notlar/konu-takip.md | head -80.
4. Bana özetle: hangi kaynaklar güncellendi; içeriği değişen / yeni / kaynakta kaldırılan skiller; yeniden incelenecekler;
   rollerde kullanılan skillerden etkilenen var mı; yeni ücretli skill var mı; erişilemeyen ya da adı değişen kaynak var mı
   (kaynaklar.json düzeltmeleri benim kararım: tip KAYIP, eski_adlar, ad_devral); karar bekleyen yeni skiller (kaynaklar.json dahil/haric).
5. Onayımı bekle. Dal 45 günden eskiyse bunu söyle.
   - Onaylarsam (iki dal türü için de aynı yol): python3 araclar/arsiv-guncelle.py --birlestir <dal>
     (kontroller geçmezse master kendiliğinden geri döner; sonucu bana bildir). git merge --no-ff ile elle birleştirme YAPMA.
     Ardından guncelleme dalında 'yeniden-incelenecek' skilleri rehber/07-kategori-inceleme.md ile incele ve kaydet.
   - Reddedersem: git branch -D <dal>
6. Sonuç "kismi" ise NEDEN satırını açıkla ve çözümü söyle: kirli ağaç → dosyaları kaydet ya da geri al (onayımla); bekleyen dal →
   yukarıdaki adımlar; GitHub yok → benim terminalimde gh auth login.
7. Son olarak etkilenen projeleri listele: python3 araclar/proje-kullanimi.py --repo <güncellenen her kaynak>
   ve onlar için hatırlat: skill-ekle.py <proje> --durum / --guncelle --kuru (bkz. promptlar/05).
   Çıktıda 'KİMLİK KORUNDU' ya da 'AD DEĞİŞMİŞ' satırı varsa bana ayrıca göster (rehber/09-ad-kimlik-ve-cakisma.md).
8. Program güncellemesi bekleyenler (özet listesinde "yeni sürüm var") ayrı onay ister: promptlar/13.
```
````

---------------------------------------------------------------------------------------------------------------------

## 5. Tests — `araclar/testler/test_p4-aylik.py`

Kural: yalnız `tempfile` dizinleri ve sahte veri; gerçek `~`, gerçek kütüphane, gerçek `gh`, gerçek `~/Documents` KULLANILMAZ.
Donanım: dosya başında `HOME=<tmp>` ve `PATH=<tmp>/bin:` + sistem yolu ayarı (alt süreçler dahil), git kimliği `GIT_AUTHOR_NAME/EMAIL`, `GIT_COMMITTER_NAME/EMAIL`, `GIT_CONFIG_GLOBAL=/dev/null`; sahte `gh` betiği `<tmp>/bin/gh` (modlar: ok `5000` yazar, `fail` çıkış 1, `yok` = dosya silinir). `arsiv-guncelle.py` `importlib.util.spec_from_file_location("arsiv_guncelle", …)` ile yüklenir ve şunlar yamalanır: `KOK, GECMIS, KILIT, DAMGA, OZET_RAPORU, REGISTRY, KAYNAKLAR`, `gh_api`, `etkilenen_projeler` (boş döner; gerçek `projeler.json`/`~/Documents` okunmasın), `ortak.repo_guncel`/`_TAKMA_ADLAR` (`{}`). Sahte kütüphane: `git init -b master` + `.gitignore` (`.guncelleme-kilidi`, `.gecici/`, `notlar/son-aylik-calisma.json`, `notlar/aylik-ozet.md`) + `araclar/` altında sahte araçlar (python betikleri; `--help`, `--ozet-json`, çıkış kodları ve "yazma girişimi" için ayarlanabilir). Son satır: `N/N test geçti`; hata varsa çıkış 1. Çalıştırma: `python3 araclar/testler/test_p4-aylik.py`.

A. `aylik-ozet.py` (`--kok <tmp>` ile alt süreç olarak):
 1. Geçerli `--ozet-json` çıktılı 5 sahte araç → özet satırları ve `karar_bekleyen`'ler birleşir, tekrarlar elenir.
 2. Eksik araç dosyası → `dikkat`, "araç kütüphanede yok", çıkış 0, diğerleri çalışır.
 3. Araç çıkış 1 + çöp stdout → "çalışmadı (çıkış 1)"; diğer araçlar etkilenmez.
 4. Şema bozuk (`durum: "kötü"`) → "çıktı biçimi bozuk".
 5. Araç uyur (`--zaman-asimi 1`) → "zaman aşımı".
 6. Araç stdout'a JSON'dan önce çöp satır basar → son `{` satırı alınır.
 7. Damga: yok → `dikkat` + karar sorusu; 10 gün → temiz; 40 gün → `dikkat` "kaçan ay"; 80 gün → `sorun`; `son_sonuc: kismi` → "yarım kaldı"; `atlanan_kaynaklar` → bilgi + karar.
 8. Dallar: temp git deposunda `guncelleme/2026-10` (commit tarihi 50 gün önce, `GIT_COMMITTER_DATE`/`GIT_AUTHOR_DATE`) → "45 günden eski" `dikkat`; taze `takip/…` → listelenir, uyarı yok; zaten birleşmiş dal → "silebilirsin", karar yok; dal içi `guncelleme-gecmisi.md` "Karar bekleyen yeni skiller** (3;" → karar satırı.
 9. Not ayrıştırma (YEDEK regex yolu; `--bekleyenler` araçları yokken): konu-takip iki konu (odaklı aday 1 + 3) → "4 odaklı aday"; populer `## Yeni adaylar (12)`; trend tablosu 3 satır (biri 0) → 2; `kararlar.md` işaretsiz iki kutu (+ işaretli bir kutu yok sayılır); bozuk/boş/eksik dosyalar → "okunamadı"/sessiz, çökme yok.
10. Rapor yaşı: populer tarihi 60 gün önce → `dikkat`; trend.json taze → temiz; tarih bulunamazsa → "tarih okunamadı", durum etkilenmez.
11. `--hizli`: yalnız `genel-bekci`, `git-durum`, `yedek-denetim` ve dört EK_TAM sahte aracı işaret dosyası bırakır; `program-denetim` ve `proje-kullanimi` işaretleri YOK; çıktı ≤ 15 satır; `notlar/aylik-ozet.md` yazılmaz; çıkış 0.
12. `--hizli` ve tam özet yoksa / tam özet 50 gün eskiyse davranış (md ilk satır yorum JSON'undan okunur).
13. `--ozet-json`: stdout TAM olarak tek JSON nesnesi (`json.loads` başarılı; anahtarlar tam `arac, durum, satirlar, karar_bekleyen`; `arac == "aylik-ozet"`); stdout'ta başka metin yok.
14. `--siki`: `sorun` → çıkış 1; `dikkat` → 0; `--siki`'siz `sorun` → 0.
15. Tam mod `notlar/aylik-ozet.md` yazar: ilk satır geçerli yorum-JSON, "Senin kararını bekleyenler" başlığı var; `.gitignore` satırı yoksa (git deposu içinde, yoksayılmıyor) DOSYA YAZILMAZ ve `dikkat` satırı çıkar (0.1).
16. Sözleşme ihlali: `--ozet-json` ile izli (izinli listede OLMAYAN) dosyaya yazan sahte araç → o araç satırında "sözleşme ihlali" + `dikkat`; `proje-durumu.md`/`program-denetimi.md` yazan sahte araç → ihlal SAYILMAZ; uyumlu araçlarla tam özet SONRASI `git status --porcelain` BOŞ (md/damga yoksayılıyor).
17. Zamanlanmış görev farkı: aynı dosyalar → satır yok; farklı → bilgi satırı (durum değişmez); canlı dosya yok → satır yok.
18. Özet metni: karar varken "Senin kararını bekleyen N şey:", yokken "Senin kararını bekleyen bir şey yok."; hızlı + temiz → tek satır "her şey yolunda".
19. Gizlilik: araç `satirlar` içine 400 karakterlik satır koyar → basılan satır ≤ 300 karakter; çıktıda `.env` içeriği okunmaz (sahte `.env` dosyası kütüphane köküne konur, içeriği hiçbir çıktıda geçmez).
20. Salt okuma: tam mod öncesi/sonrası temp kütüphanenin dosya ağacı özeti (md hariç) ve `git status` aynı; hiçbir dal/commit oluşmamış.

B. `arsiv-guncelle.py` (modül içi, yamalı):
21. `damga_yaz`/`damga_oku`: yuvarlak gidiş-dönüş; `son_basarili` yalnız guncellendi/sadece-takip'te değişir; `gecmis` 12'de kırpılır, en yeni üstte; geçersiz `sonuc` → `ValueError`, dosya değişmez; bozuk eski dosya → yeniden başlar; yoksayılmayan yol → yazılmaz (`False`).
22. `kirli_dosyalar`: `M`, `??`, yeniden adlandırma (`R`) ve boşluklu/Türkçe karakterli yollar doğru ayrışır; `.gitignore`'daki damga listede yok.
23. `uygula()` kirli ağaçta: `SystemExit` mesajı dosya adlarını ve `--aylik` önerisini içerir; kilit dosyası oluşmaz.
24. `gh_hazir`: sahte gh ok → `(True, 5000, "")`; çıkış 1 → `(False, None, …)`; gh yok → "gh kurulu değil"; zaman aşımı → "zaman aşımı".
25. `rapor()` çevrimdışı: `gh_api` HİÇ çağrılmaz (sayaç 0), `CEVRIMDISI=True`, `([], [], {})`, çıktıda "ATLANDI", Traceback yok, `dogrula.py` `--github`'suz çağrılır.
26. `rapor()`: `gh_api` 404 (`GhBulunamadi`) → `sorunlu` (mesaj "erişilemiyor" ön ekiyle); RuntimeError ×3 art arda → döngü kesilir, kalanlar `ULASILAMAYAN`; RuntimeError sonra başarı → sayaç sıfırlanır.
27. Ad değişikliği: `html_url` farklı sahip/ad → `ADI_DEGISEN`; `eski_adlar` ile zaten eşleşen → yok; `html_url` yok → sessiz.
28. `main()` `--uygula` kapısı: sahte `kaynak-cek.py --help` `--atla` içerir + `sorunlu` var → devam (kaydedici `uygula`), `ATLANAN` dolu; `--help` içermez → eski "DURDU … 'KAYIP'" mesajı; `ULASILAMAYAN` doluysa yeni "DURDU: N kaynak şimdilik kontrol edilemedi".
29. `bekleyen_dallar`: yaşlar doğru; 46 günlük → rapor modu çıktısında "45 günden eski"; birleşmiş dal "zaten master'a birleşmiş".
30. `takip()`: (a) değişiklik yok → dal silinir, master'dayız, damga `sadece-takip`, `dal` None; (b) sahte tarama bir `notlar/` dosyasını değiştirir → `takip/YYYY-AA` dalı + commit, master HEAD değişmez; (c) bir tarama çıkış 1 → UYARI, zincir sürer; (d) üç ağ taraması da çıkış 1 → geri alma, `kismi`; (e) `dogrula.py` çıkış 1 → geri alma, dal yok, `hata`, çıkış 1, damga dosyası (yoksayılan) silinmemiş; (f) aynı ay ikinci çağrı → `takip/YYYY-AA-2`.
31. `aylik()` (kütüphane içi fonksiyonlar yamalı, sahte araçlar): (a) kirli (izli olmayan farklı dosya) → hiçbir dal açılmaz, sonuç `kismi`, NEDEN dosyaları sayar, salt okuma adımları (rapor + özet) çalıştı, damga yazıldı; (b) yalnız `notlar/program-denetimi.md` değişik → engel SAYILIR, hiçbir commit atılmaz (master HEAD aynı), NEDEN'de "yalnız rapor dosyaları değişmiş" ve dosya adı geçer; `--aylik` çıktısı karar önerir; (c) `--kuru` → commit/dal/damga yok, "PLAN:" basılır; (d) bekleyen dal → `kismi`; (e) master değil → `kismi`; (f) gh yok → `kismi`, "GitHub'a ulaşılamıyor", özet yine çalışır; (g) temiz + `degisen=[]` → `takip()` çağrılır, `sadece-takip`; (h) temiz + `degisen=[repo]` → `uygula()` çağrılır, `guncellendi`; (i) `degisen` + `sorunlu` + `--atla` yok → `kismi`; (j) damga 40 gün eski → "KAÇAN AY:" satırı; (k) çıktının son satırları `SONUÇ:` biçiminde; çıkış kodu: hata → 1, diğer → 0; (l) çift damga yok (aylık içinde tek kayıt); (m) zincir içi özet `--yazmadan` ile çağrılır (sahte aylik-ozet argümanları kaydeder: `--yaz` YOK), özet sonrası izinli rapor yolu kirlendiyse `git checkout --` ile geri alınır, başka kirli yol varsa dokunulmaz.
32. Eski davranış korunumu: `--birlestir olmayan/dal` → eski "Dal yok: … Bekleyen güncelleme dalları: …" mesajı (iki desen listelenir); rapor modu değişiklik yokken çıkış 0; modül `import` edilirken yan etki yok (dosya yazılmaz, ağ çağrısı yok).
34. Aday triyajı (aylik-ozet): üç aday aracı toplam 23 aday döner → her araç için tek karar satırı, en çok 5 ad + "+K daha"; `kararlar.md` `## Kabul edilen bekleyenler` bölümündeki ifade (ör. bir repo adı) olan karar süzülür; sonek tarih geçmişse süzgeç kalkar; 8 karakterden kısa ifade yok sayılır.
35. Araç listesi: `ortak.OZET_ARACLARI` olan sahte `ortak` ile liste birleşir (tekrarsız); `ortak` yoksa/özniteliği yoksa sabit yedek kullanılır; EK_TAM dört araç koşar; `--hizli` bu dört + üç yerel aracı koşar, `program-denetim`/`proje-kullanimi` koşmaz; `--oturum` `--hizli` ile aynı çıktıyı verir; tam modda `proje-kullanimi` bayraklarında `--yaz` var, `--yazmadan`'da yok.
36. Bekleyen not birincil/yedek: `--bekleyenler` aracı geçerli JSON verirse md regex'i HİÇ okunmaz (md'yi bozuk koy: sonuç etkilenmez); araç çalışmazsa md regex'i devreye girer ve "yedek okuma" notu çıkar.
37. Damga yok: (a) taze klon, `guncelleme-gecmisi.md` en yeni kayıt 50 gün önce → 35 gün kuralı (`dikkat` + soru); (b) kayıt 10 gün önce → `temiz`; (c) hiçbir tarih yok → `temiz`, "ilk kurulum", karar YOK.
38. Kayıp kaynak: damga `atlanan_kaynaklar` + `kaynaklar.json` `tip: KAYIP` → karar yok (bilgi satırı); `KAYIP` değilse karar var; kararlar.md kabul listesinde ise karar yok.
33. D12: `takip()`'in sildiği tek dal kendi açtığı dal (önceden var olan `guncelleme/x` ve `takip/eski` dalları testte KORUNMUŞ olmalı).

---------------------------------------------------------------------------------------------------------------------

## 6. Hand-off requests to other packages (ENGELLEYİCİ olanlar işaretli)

**P3 (ENGELLEYİCİ, P4 dosyaları ilk yazmadan önce):** `.gitignore` sonuna iki satır: `notlar/son-aylik-calisma.json` ve `notlar/aylik-ozet.md`.
P3 `rehber/02`'ye dokunmaz: B5'in geri alma/`revert -m 1` parçası P4 tarafından `rehber/02` 3.4'te yazılır (P3 yalnız `README.md` geri yükleme listesi).

**P2, P3, P5, P6 (ENGELLEYİCİ sözleşme; aylik-ozet buna dayanır):** her `--ozet-json` çağrısı (a) stdout'a yalnız tek JSON nesnesi yazar `{"arac","durum","satirlar","karar_bekleyen"}`; (b) diske HİÇBİR dosya yazmaz (rapor dosyası dahil; rapor yalnız `--ozet-json`'suz modda yazılır); (c) çıkış kodu 0 (bulgu ne olursa olsun; `--siki` yalnız normal modda); (d) kütüphane kök dizininden (`cwd`) çalışır; (e) `karar_bekleyen` her madde düz Türkçe tek cümle ≤200 karakter, değer/anahtar içermez (D9), yalnız GERÇEKTEN kullanıcı kararı gerektiren şeyler. Ek: `genel-bekci.py`, `git-durum.py`, `yedek-denetim.py` ağ kullanmaz (`git fetch` DAHİL YOK), ≤10 sn (oturum başı `--hizli` bunları koşturur). `proje-kullanimi.py --saglik --ozet-json` ve `program-denetim.py --ozet-json` ağ/yavaş olabilir (yalnız tam modda). `program-denetim.py` `karar_bekleyen` örneği: "hyperframes 0.9.23 → 0.9.33: güncelleme onayı bekliyor".

**P7:** (1) `kaynak-cek.py` `--atla owner/ad[,owner/ad]`: listedeki repolar için `repo_agaci`/indirme yapılmaz, `UYARI: <repo> atlandı (arşiv kopyası korunur)` basılır, `manifest["kayitlar"]`'a eklenmez; çıkış kodu geri kalan her şey başarılıysa 0 (arsiv-yerlestir bunları zaten korur: `arsiv-yerlestir.py:455-523`). Bayrak olmadan `:238-240` davranışı aynen kalır. `kaynak-cek.py --help` çıktısında `--atla` geçmeli (P4 buna bakar). (2) **Alındı (kabul):** `konu-takip.py`, `github-trend.py`, `populer-tarama.py` `--bekleyenler --ozet-json` (ağsız, anında, dosya yazmaz, D4 şekli) aylik-ozet'in BİRİNCİL aday kaynağıdır; markdown regex'leri yalnız araç çalışmazsa yedektir (bölüm 3.2-5), bu yüzden P7 rapor başlıklarını değiştirirse aylik-ozet kırılmaz (yalnız yedek yol etkilenir). (2b) P7 `kaynak-cikar.py` dışında `kaynaklar.json`'a `tip: KAYIP`/`kayip_tarihi` yazan başka bir bayrak OLMADIĞINI rehber/03 E3'te belgeler (aylik-ozet 'KAYIP işaretlensin mi' sorar; kaydı elle onayla yazan adım P7'nin E3'üdür). (2c) Mevcut `J-DTurner/etsy-api-skill` KAYIP kaydına `kayip_tarihi` eklenmesi P7 uygulamasında yapılır (P7 G-KAYIP UYARI'sı ilk koşuda tetiklenmesin); P4 bu kaydı karar saymaz (3.2-5c). (3) B2'nin kalan parçaları (`ortak.elenecekler()`, tek `--karar`, `izle` anlamı) P7'de.

**P8:** (1) `CLAUDE.md`/`AGENTS.md`/`BASLA.md`: oturum başı satırı: "Kütüphane oturumunun ilk işi: `python3 araclar/aylik-ozet.py --hizli`; çıktıyı kullanıcıya iki cümleyle söyle. Aylık çalışma 35 günü aştıysa 'Aylık çalışmayı şimdi yapayım mı?' diye sor; evet derse `python3 -u araclar/arsiv-guncelle.py --aylik`." (2) `CLAUDE.md`/`AGENTS.md` "Bakım isteklerinde" aylık satırı: `"Skilleri güncelle" (aylık) → python3 -u araclar/arsiv-guncelle.py --aylik (ön kontrol, rapor, güncelleme/takip dalı, özet, damga) → kullanıcıya dal özeti ve notlar/aylik-ozet.md → onay gelirse --birlestir <dal> (iki dal türü için aynı)`; eski üç adım yorumda kalabilir. (4) `notlar/kararlar.md`: `## Karar bekleyenler` bölümü, her madde `- [ ] <düz cümle>` (aylik-ozet bunları toplar; tamamlanınca `[x]`). (3) `araclar/test.py`: araclar/testler/ altındaki dosyaları alt süreç olarak koşturan bölüm (D5); P4 başka satır istemez. (5) `dogrula.py`: P4 için ek denetim İSTENMEZ (görev kopyası farkı `aylik-ozet.py`'de bilgi olarak kapatıldı; dogrula'da UYARI yapılırsa `duman-testi.py:72` "0 uyarı" kırılır). (6) Eğer prompt bayrak denetimi tüm promptlara genişletilirse promptlar/08'deki bayraklar: `--aylik`, `--birlestir`, `--kuru`, `--damga-yaz` (hepsi gerçek).

**P8 (ek, bayrak adı ve listeler; reviewer düzeltmeleri):**
- (7) **Bayrak adı: `--hizli`.** P4 `--hizli` tanımlar ve `--oturum`'u aynı davranışla takma ad olarak kabul eder (`--hizli --ozet-json` ve `--oturum --ozet-json` ikisi de geçerli). P8 `BASLA.md`, `CLAUDE.md`, `AGENTS.md` ve duman adım 11'de `--oturum` yerine **`--hizli`** yazsın (P8 bayrak denetimi `--hizli`'yi kaynak metninde bulur). `--hizli` ağsız, yazmasız ve ≤ 15 satırdır (P8 şartı karşılanır) ve `--ozet-json` destekler.
- (8) `ortak.OZET_ARACLARI`: P4 bu listeyi `from ortak import OZET_ARACLARI` ile okur (liste ayrışmaz). P4'e özgü dört ağsız ek (`skill-ekle --araclar`, `konu-takip|github-trend|populer-tarama --bekleyenler`) aylik-ozet'te EK_TAM'dadır; P8 isterse bunları da `OZET_ARACLARI`'na ekler (duman da koşturur); aylik-ozet tekrarlamaz. `proje-kullanimi` girişine P4 yalnız tam modda `--yaz` ekler.
- (9) `notlar/kararlar.md` ek bölümleri: `## Karar bekleyenler` (`- [ ] <düz cümle>`; aylik-ozet toplar, tamamlanınca `[x]`) ve `## Kabul edilen bekleyenler (aylık özette susturulur)` (satırlar `- <ifade>` ya da `- <ifade> | AAAA-AA-GG`; aylik-ozet ifadeyi içeren karar cümlelerini susturur; ifade ≥ 8 karakter). "Henüz sonuçlanmamış sorular"a madde: "Aylık özet/triyaj: ayda en çok kaç aday repo karara bağlansın (N)? Cevaplanana kadar özet yalnız ilk 5 adı gösterir, sınır koymaz."
- (10) Not (kapsam notu P4'ten P8'e): rehber/14 aylık kontrolün tam modda (`aylik-ozet.py`) yapıldığını, hızlı modun yapay-zeka-araclari bayatlığını (`--araclar`) da gösterdiğini yazsın; `BASLA.md` 'araç' bölümünde "Windows'ta `skill-ekle.py` çalışmaz" notu P8'dedir (P1 rehber/14'te var). `promptlar/10-kutuphane-saglik-kontrolu.md` satır 8 eski "44 güvenlik testi" sayısı ve `rehber/08-test-sureci.md` test dosyası paragrafı P8'e atanmıştır (P4 dokunmaz).

**P6:** `program-denetim.py --ozet-json` koşusunun `notlar/program-denetimi.md`'yi yazıp yazmadığını P6 uygulayıcısı AÇIKÇA belirler ve spec'ine yazar. P4 iki durumda da çalışır (dosya `IZINLI_RAPOR_YOLLARI`'ndadır). Tavsiye: yalnız `--yaz` verilince yazsın (master'ın temiz kalması için); P4 `program-denetim`'e `--yaz` VERMEZ.

**P5:** istek (`proje-kullanimi.py --saglik --ozet-json --yaz`) kabul: P4 tam modda bunu çağırır ve dosya aylık tazelenir; zincir içinde (`--yazmadan`) `--yaz` verilmez, tazeleme dal içinde `_uygula`/`takip` adımıyla olur (3.1-H).

**P1:** `skill-ekle.py --araclar --ozet-json` (ağsız, kilitsiz, yazmaz) aylik-ozet tarafından çağrılır: kabul (P4 EK_TAM'ında). Proje `CLAUDE.md`/`AGENTS.md` bloğunda kütüphane yolunun yazılı olması (başka klasörden açılan oturum için) P1'in işidir; P4 dokunmaz.

---------------------------------------------------------------------------------------------------------------------

## 7. Needs the user's approval (gerçek değişiklik sırasında ayrı ayrı)

1. **Canlı zamanlanmış görev metninin değiştirilmesi** (`~/.claude/scheduled-tasks/skill-kutuphanesi-aylik-guncelleme/SKILL.md`, kütüphane dışı): prosedür rehber/02 1c'de (diff göster → yedek → kopyala → `--aylik --kuru` ile doğrula). Metni DEĞİŞTİRME, bu pakette yalnız kütüphane kopyası yazılır.
2. **(Kaldırıldı)** `--aylik` master'a HİÇ commit atmaz (reviewer düzeltmesi); rapor dosyaları değişmişse commit kullanıcı onayıyla (kullanıcı "kaydet" derse oturum `git add <adlar> && git commit` yapar). Zincir içinde izinli rapor yolları dal içinde üretilir ve master'daki kopyaları `git checkout --` ile geri alınır (kendi koşusunun ürünü; onay gerekmez, kullanıcıya yazılır).
3. **Davranış değişikliği:** erişilemeyen tek kaynak artık `--uygula`'yı durdurmaz (P7 `--atla` gelince) ve `--dal` artık `takip/*` bekleyen dalıyla da engellenir.
4. **Aşama 2'ye geçiş ve ilk gerçek `--aylik` koşusu** (Aşama 1 testleri ve salt okuma komutları geçtikten sonra ayrı onay); (ağ, GitHub API hakkı, dal + commit üretir; 15-40 dk) ve ilk günde kirli ağaç: şu an 9 değişmiş + 2 izlenmeyen yol var (`git status`); koşudan önce kullanıcı bunları kaydetmeli ya da koşu "kismi" döner.
5. **`.gitignore` satırları** (P3 sahibi) ve `git branch -D`, `--birlestir`, push (her biri kural gereği kullanıcı isteğiyle; P4 hiçbirini kendiliğinden yapmaz).
6. **`gh auth login`** gerekirse kullanıcı kendi terminalinde yapar (etkileşimli; araç yapamaz).

---------------------------------------------------------------------------------------------------------------------

## 8. Deferred and why

- **`kaynak-cek.py --atla` uygulaması** (B4'ün kaydın atlanması parçası): dosya P7'nin; P4 yalnız çağırır ve bayrak yoksa eski davranışa düşer. `arsiv-yerlestir.py` değişikliği gerekmedi (0.3).
- **`kaynaklar.json`'u otomatik düzeltme** (`KAYIP` işaretleme, `eski_adlar` yazma): kural 6 ve "kaynak ekleme/çıkarma kullanıcı onayı"; yalnız raporlanır. `--kayip-isaretle` bayrağı YAPILMAZ (ne P4'te ne P7'de; elle E3 adımı onayla). Tekrarlayan aylık raporlama 3.2-5c ile (KAYIP işareti ya da kabul listesi) kapatıldı.
- **"Ayda en çok N aday" sınırının kendisi:** değer kullanıcı sorusudur (kararlar.md sorular bölümü); P4 yalnız en çok 5 adı gösterir ve toplamı yazar.
- **Zamanlayıcıya bağımlı olmayan tetik:** yapıldı (asıl tetik damga kuralı); Mac uykudayken kaçan görevin sonradan çalışması hâlâ doğrulanmadı.
- **Proje `CLAUDE.md`/`AGENTS.md` içinde kütüphane yolu denetimi** ve P8 sahipli rehber/08, promptlar/10 satır 8 düzeltmeleri: P1/P8'in (bölüm 6).
- **`DURUM.md` düzyazısından karar çıkarmak:** "onay bekliyor" cümleleri tarihli ve sonradan çözülmüş olabilir (yanlış pozitif). Yerine yapılandırılmış `notlar/kararlar.md` onay kutuları (P8).
- **Zamanlayıcı bildirimi / kaçan görev uyarısı:** zamanlayıcı kütüphane dışında ve yalnız Claude'a özgü; yerine oturum başı `--hizli` + 35 gün kuralı. Mac uykudayken kaçırılan görevin uyanınca çalışıp çalışmadığı doğrulanmadı.
- **Aylık koşuda `yol-tara.py`'nin master'da çalışması:** izli dosya yazar (0.2); yalnız dallarda koşar, özet yaşını gösterir.
- **Proje başına `skill-ekle.py --durum` toplu raporu / kayıtsız proje keşfi:** P5'in `--saglik` aracı özet zincirine girer.
- **B2'nin kalanı** (`elenecekler()`, `izle` tek anlam, `dogrula.py` rapor yaşı UYARI, "ayda en çok N adayı karara bağla" kuralı): `ortak.py`/`dogrula.py` P8'in, tarayıcılar P7'nin. P4 yalnız yaşı görünür kılar (özet).
- **Çoklu bekleyen dalın otomatik çözümü / otomatik birleştirme:** hiçbir zaman otomatik değil (kullanıcı onayı).
- **Rename tespitinin (`html_url`) gerçek GitHub'da doğrulanması:** bu aşamada `gh api` yasak; uygulayıcı kontrol eder, tutmazsa kod bırakılır (B adımı yedek).
- **Tek koşu içinde iki oturumun aynı master'da çalışması çatışması:** `.guncelleme-kilidi` yalnız `skill-ekle.py`'yi bekletir; `--aylik` ağaç temizliğini ve dal durumunu denetler ama başka bir oturumun elle master'da çalışmasını engelleyemez. Rehber/02'ye "aylık zincir sürerken kütüphanede başka iş yapma" notu eklenir (3.4-1b).

---------------------------------------------------------------------------------------------------------------------

## 9. Risks and how the implementer verifies nothing existing broke

| Risk | Doğrulama |
|---|---|
| `rapor()` yeni ağ/`gh_hazir` çağrısı rapor modunu yavaşlatır/bozar | `python3 araclar/arsiv-guncelle.py` (rapor) önce/sonra çıktı karşılaştır: eski satırlar aynen; `duman-testi.py:88` "Traceback yok" |
| Kirli ağaç `--uygula` kapısı mesajı değişti | `uygula()` testi (23); `:157` anlamı (çıkış 1) aynı |
| Çıkış kodu 2 yeni | `grep -rn "arsiv-guncelle" araclar/ promptlar/ rehber/ zamanlanmis/` ile okuyanlar listelenir: yalnız `duman-testi.py:88-89` (kod okumaz) |
| `kilit_al()` çıkarımı kilit davranışını değiştirir | test 23 + elle: sahte canlı pid kilidi → "başka bir güncelleme sürüyor", ölü pid → üzerine yazılır |
| `takip()` yeni; yarım kalırsa master'da kalıntı | test 30 (a-f): geri alma sonrası `git status` temiz, dal yok, master HEAD aynı |
| Damga/özet dosyaları ağacı kirletir | test 15, 16; gerçek kütüphanede `git check-ignore -v notlar/son-aylik-calisma.json notlar/aylik-ozet.md` iki satır (P3 `.gitignore`) |
| `--ozet-json` araçları izli dosya yazar | test 16 + `aylik-ozet` ihlal tespiti (izinli: proje-durumu.md, program-denetimi.md) |
| `reset --hard`/`clean` gözetimsiz çalışır | yalnız `takip()` kendi dalında, başlangıç temizliği ve dal adı doğrulanmışsa (3.1-E-7); testler 30(e,g); master'a commit yok (31b) |
| Aşama 1/2 birbirine karışır | Aşama 1 commit'inde `damga_yaz`, `takip`, `--damga-yaz` YOK (grep); ayrı onay |
| Başka paket rapor biçimi değiştirir | test 9; regex kopmasında `okunamadı` satırı çıkar, çökme yok |
| Yeni `zamanlanmis/aylik-guncelleme.SKILL.md` skill sayılır | `grep -n "SKILL.md" araclar/kapsam-denetimi.py araclar/dogrula.py araclar/katalog-uret.py araclar/skill-calistir.py` (kökte `**/SKILL.md` taraması varsa dosya adı farklı: `aylik-guncelleme.SKILL.md`, ve `arsiv/` dışı); sonra `python3 araclar/kapsam-denetimi.py` 0 sorun ve `python3 araclar/dogrula.py` 0 hata (SAHİP P8 olmasa da uygulayıcı bir kez koşturur) |
| Mevcut testler | `python3 araclar/test.py` ve `python3 araclar/dogrula.py` önce/sonra aynı sonuç; `araclar/duman-testi.py` yalnız P8 entegrasyonundan sonra |
| `html_url` ile ad tespiti yanlış alarm | yalnız `rapor()` bilgi satırı; hiçbir dosya yazmaz |

---------------------------------------------------------------------------------------------------------------------

## 10. Acceptance (bitti sayılma kanıtı; hepsi salt okuma ya da temp)

```bash
cd ~/Documents/SkillKutuphanesi
python3 araclar/testler/test_p4-aylik.py                      # son satır "N/N test geçti", çıkış 0
python3 araclar/aylik-ozet.py --hizli                         # < ~5 sn, Traceback yok, hiçbir dosya yazılmaz (git status aynı)
python3 araclar/aylik-ozet.py --ozet-json | python3 -c "import sys,json; d=json.load(sys.stdin); assert set(d)=={'arac','durum','satirlar','karar_bekleyen'}"
python3 araclar/aylik-ozet.py                                  # notlar/aylik-ozet.md yazar; çıktı bölüm 4.1 biçiminde; eksik araçlar 'dikkat' (P2/P3/P5/P6 gelince temiz)
git check-ignore -v notlar/son-aylik-calisma.json notlar/aylik-ozet.md   # İKİ satır çıktı (P3 .gitignore, ENGELLEYİCİ)
git status --porcelain                                         # aylik-ozet çalıştırmasından SONRA da aynı (yeni kirli yol yok)
python3 araclar/arsiv-guncelle.py                              # rapor modu: eski satırlar + yeni bekleyen dal/yaş satırları; Traceback yok; yalnız okuma (notlar/ içinde izli dosya değişmez)
python3 araclar/arsiv-guncelle.py --aylik --kuru               # PLAN: … ; commit/dal/damga YOK (git status ve `git branch` aynı, damga dosyası oluşmadı)
python3 araclar/aylik-ozet.py --oturum --ozet-json | python3 -c "import sys,json; json.load(sys.stdin)"   # takma ad çalışır
python3 araclar/aylik-ozet.py --hizli | wc -l                  # ≤ 15
python3 araclar/arsiv-guncelle.py --damga-yaz bilinmeyen       # çıkış ≠ 0, hiçbir dosya yazılmadı  (geçerli sonuçla DENEME; gerçek damgayı yalnız gerçek koşu yazar)
# üç belge aynı komutları söylüyor:
for f in rehber/02-guncelleme-yonergesi.md promptlar/08-aylik-guncelleme-onayi.md zamanlanmis/aylik-guncelleme.SKILL.md; do
  for k in -- '--aylik' '--birlestir' 'takip/' 'aylik-ozet.py'; do [ "$k" = "--" ] && continue; grep -q -- "$k" "$f" || echo "EKSİK: $f içinde '$k' yok"; done; done
grep -n "git merge --no-ff" rehber/02-guncelleme-yonergesi.md promptlar/08-aylik-guncelleme-onayi.md zamanlanmis/aylik-guncelleme.SKILL.md   # yalnız "kullanılmaz/YAPMA" uyarı satırları
grep -c -- '--damga-yaz' zamanlanmis/aylik-guncelleme.SKILL.md rehber/02-guncelleme-yonergesi.md    # her ikisinde ≥1
python3 araclar/dogrula.py && python3 araclar/kapsam-denetimi.py                              # 0 hata / 0 sorun (zamanlanmis/ dosyası skill sayılmamış)
```
Ek elle kanıt (uygulayıcı, tek seferlik, onay gerektirmez): (1) bilinen taşınmış bir repo için `rapor()` fonksiyonunu çağıran bir betikle `html_url` ad tespitinin çalıştığı ya da çalışmadığı not edilir; (2) canlı görev dosyasıyla kütüphane kopyası `diff -u` edilip kullanıcıya gösterilir (DEĞİŞTİRİLMEZ).

---------------------------------------------------------------------------------------------------------------------

## 11. Review changes (inceleme sonrası son sürüm)

**Uygulananlar (zorunlu düzeltmeler):**
1. **Hand-off alıcısı / araç listesi:** `ARACLAR_TAM` artık `ortak.OZET_ARACLARI` (+ sabit yedek) + P4 `EK_TAM` (`skill-ekle --araclar`, `konu-takip|github-trend|populer-tarama --bekleyenler`; hepsi ağsız `--ozet-json`); hızlı modda yalnız ağsız/yerel olanlar. Aday sayıları önce `--bekleyenler` JSON'undan, md regex'leri yalnız yedek (3.2-5). Bölüm 6'da "P1: yok" yerine P1 kabulü yazıldı.
2. **`--ozet-json` ve yazma:** sözleşme cümlesi düzeltildi (0.2): yalnız aracın kendi `notlar/` raporu yazılabilir; `genel-bekci`, `git-durum`, `yedek-denetim` (ve `--araclar`/`--bekleyenler`) hiç yazmaz. `proje-kullanimi.py --saglik --yaz` tam modda çağrılır; `program-denetim` için izinli yol. Zincir içinde `--yazmadan` kullanılır ve dal içinde üretilen rapor dosyaları master'dan `git checkout --` ile geri alınır; bu yüzden ağaç kirlenmez.
3. **Uygulama sırası:** başa "Önkoşul" satırı eklendi (0 programlar commit'i → P3 → P1 → P2/P5/P6 → P7 → P4 → P8).
4. **Bayrak adı:** `--hizli` kalır, `--oturum` takma ad (aynı davranış); P8'e `--hizli` yazması istendi; `--hizli` ağsız, yazmasız, ≤ 15 satır, `--ozet-json` destekli.
5. **Risk azaltma:** master'a otomatik commit KALDIRILDI (kirli ağaç her zaman engel; NEDEN ve karar_bekleyen "kaydedilsin mi?"); `reset --hard`/`clean` yalnız kendi dalında, başlangıç temizliği ve dal adı doğrulanınca; rapor çıkış kodu 2 varsayılan DEĞİL (yalnız `--siki`); çevrimdışılık ayrı satır, çıkış 0. Uygulama iki aşamaya bölündü (3.1 başı).
6. (İsteğe bağlı, kabul) **Tetik cümlesi:** asıl tetik oturum başı damga kuralı; zamanlanmış görev kolaylık; komutlar zamanlanmış görev/Claude eklentisine bağlı değil (1-3, 4.4, rehber/02 1b).

**Sahipsiz boşluklardan alınanlar:** B2 triyaj kuralı (özet kısmı: en çok 5 ad + toplam; N sorusu P8'in kararlar.md'sine, 3.2-5a); "damga yok / taze klon" tanımı (3.2-2, `guncelleme-gecmisi.md` yedek tarihi, ilk kurulumda soru yok); ortak "kabul edildi" listesi (3.2-5b, kararlar.md); tekrarlayan kayıp-kaynak raporu (3.2-5c). `--kayip-isaretle`: yapılmaz, belgelendi (bölüm 6/8). `rehber/14` aylık-tam-mod notu P8'e iletildi.

**Reddedilen / başkasına bırakılan:** promptlar/10 satır 8 "44 güvenlik testi" ve rehber/08 paragrafı P4 dosya listesinde değil → P8'e (bölüm 6, P8-10). Proje bloğunda kütüphane yolu P1'in işi. Windows/GEMINI.md zaten ertelenmiş (kapsam dışı). `program-denetim`'e `--yaz` verme isteği reddedildi: bayrak P6'da yok/belirsiz, P6 karar versin; P4 iki durumu da tolere eder.

**Doğrulanmadı (uygulayıcı kontrol eder):** `html_url` ile ad tespiti (3.1-B-4), P6 `--ozet-json` yazma davranışı, `proje-kullanimi.py --help`'te `--saglik` varlığı (H-2 koşulu).
