# 05 — Riskler, Karanlık Senaryolar ve Önlemler

Her satır gerçek bir hata olasılığıdır. "Nasıl yakalanır" sütunu, sorunun hangi araçla otomatik tespit edildiğini gösterir.

## Kaynak ve arşiv

| # | Senaryo | Önlem | Nasıl yakalanır |
|---|---|---|---|
| 1 | Bir repodaki skill sessizce atlanır | Her SKILL.md için karar kaydı; bağımsız ikinci sayım | `kapsam-denetimi.py` → açıklanamayan > 0 ise çıkış 1 |
| 2 | `skill.md` (küçük harf) gibi farklı yazım | Dosya adı büyük/küçük harf duyarsız aranır | `kaynak-cek.py`, `kapsam-denetimi.py` |
| 3 | Skill'in adı `test` / `examples` diye hariç tutulur | Hariç desenleri sadece **üst** klasöre uygulanır (React `test` skill'i bu yüzden kurtarıldı) | kapsam denetimi "haric" listesi |
| 4 | Aynı repoda aynı adlı ama farklı içerikli iki skill | İçerik karşılaştırılır; farklıysa `ayri-surum`/`alternatif` olarak saklanır | denetim kararı `ayri-surum` |
| 5 | Claude ve Codex için ayrı uyarlanmış sürümler (impeccable 22 sürüm) | Claude sürümü → `.claude/skills`, Codex sürümü → `.agents/skills` | registry `varyantlar` |
| 6 | Başka AI araçlarının (Cursor, Gemini, Kiro…) kopyaları karışır | `ayna-baska-arac` olarak kaydedilir, kurulmaz | denetim |
| 7 | İç içe skill (ag-kit `game-development/*`) kaybolur | Alt skill ayrıca kaydedilir, `ust_skill` not edilir | `alt-skill` bilgisi |
| 8 | Aynı repo iki kayda bölünüp (T1+T4) karar çakışır | Kararlar "güç" sırasıyla birleşir (arşivde > kopya > hariç > kapsam dışı) | denetim |
| 9 | GitHub dosya ağacı çok büyük olup kesilir | `truncated` görülürse indirme durur | `kaynak-cek.py` HATA |
| 10 | Dosya inmez / yarım iner | Her dosya 4 kez denenir; beklenen ve inen dosya sayısı karşılaştırılır | `kaynak-cek.py`, `arsiv-yerlestir.py` HATA |
| 11 | SKILL.md'nin gösterdiği dosya arşivde yok (atlanan video vb.) | Göreli bağlantılar kontrol edilir; `../<kardeş>/` hedefi arşivdeki kardeş skillde varsa kırık değil `kardes_bagimliliklari` sayılır | `kirik_baglantilar`, ön kontrol UYARI |
| 11a | Kardeş skill projeye kurulmaz ya da `<ad>--kutuphane` gibi farklı adla kurulur, `../<kardeş>/` yolları kırılır | Kurulumda kardeş yolları projedeki ada çevrilir (eşleme `kilit.json` → `kardes`); `--guncelle` eşleme değişince yeniden yazar | `kardes-eksik` UYARI, `kardes-yol` BİLGİ |
| 12 | Repo silinir / private olur | Arşiv kopyası kalır; commit SHA KAYNAK.md'de | `arsiv-guncelle.py` gh hatası |
| 13 | Repo kötü niyetli bir değişiklik alır | Güncelleme önce **rapor** verir, sen onaylarsın; git ile geri alınır; scriptler hiçbir zaman otomatik çalıştırılmaz | `arsiv-guncelle.py` (rapor modu) |
| 14 | Kategori kuralı yanlış eşleşir | KATALOG gözden geçirilir; elle düzeltme `kategori_elle: true` ile kalıcı | kategori incelemesi |
| 15 | Elle yazdığın inceleme notları güncellemede silinir | `ELLE_ALANLAR` korunur | — |
| 16 | Yeni yıldızlanan repo unutulur | `dogrula.py --github` yıldızları kaynaklar.json ile karşılaştırır | UYARI |
| 17 | Kütüphane reposuna (T5/T6) sonradan skill eklenir | Kapsam denetimi referans repolarını da tarar | denetim SORUN |

## Proje kurulumu

| # | Senaryo | Önlem | Nasıl yakalanır |
|---|---|---|---|
| 18 | Global klasörlere yanlışlıkla yazılır | Araç global klasörlere, `~/.openmontage`'a, kütüphaneye ve ev dizinine yazmayı reddeder | güvenlik kontrolü |
| 19 | Globaldeki aynı adlı skill proje skill'ini ezer (Claude'da kişisel > proje) | Globalde farklı içerik varsa `--kutuphane` ekli adla kurulur; içteki yol referansları da düzeltilir | `ekli-ad` |
| 20 | Kullanıcının kendi skill'inin üzerine yazılır | Kilitte olmayan aynı adlı klasör → HATA | `projede-kendi-skillin` |
| 21 | Elle değiştirilmiş skill güncellemede ezilir | Kurulu içerik parmak izi kilitte; farklıysa HATA | `elle-degistirilmis` |
| 22 | Kurulum yarıda kesilir | Önce geçici klasöre kopyalanır, sonra yerine taşınır; hata olursa yedekten geri alınır | `--dogrula` "yarım kalmış kurulum" |
| 23 | Yanlış kurulum yapıldı | Her işlem öncesi yedek (son 10) | `--geri-al [ad]`, `--yedekler` |
| 24 | SKILL.md `name` ≠ klasör adı (Codex/Claude tanımaz) | Proje kopyasında ad klasöre eşitlenir | `--dogrula` |
| 25 | Bir agent'a çok fazla skill → bağlam dolar | Rol sınırları (12 skill / 150 KB / Claude 32) | `baglam-yuku`, `onyukleme-siniri` |
| 26 | Codex'te allowlist yok, her agent her skill'i görür | Rol dışı proje skilleri `[[skills.config]] enabled=false` ile kapatılır | `.codex/agents/*.toml` |
| 27 | `disable-model-invocation` skill önyüklenemez | Claude agent listesine konmaz; talimatta "elle çağır" yazar | `yapi` UYARI |
| 28 | Proje taşınınca Codex mutlak yolları bozulur | Kilitte proje yolu; farklıysa uyarır | `--dogrula` → `--yenile` |
| 29 | AGENTS.md/CLAUDE.md'deki kendi metnin bozulur | Sadece işaretli blok yeniden yazılır | — |
| 30 | Symlink'i desteklemeyen ortam (Windows, bazı zip/bulut) | Codex kopyası gerçek klasör; Claude için gerekirse `.claude/skills/<ad>` klasörüne kopya konabilir | `--dogrula` ".claude bağlantısı çalışmıyor" |
| 31 | Yedek klasöründeki SKILL.md'leri araçlar skill sanır | Yedekler `.skill-kutuphanesi/yedek/` altında, skill klasörlerinin dışında | — |
| 32 | Agent onaysız kurulum yapar | Etkileşimsiz çalışmada UYARI varsa `--evet` olmadan durur; HATA'da `--zorla` gerekir | ön kontrol |
| 33 | Skill kendi yolunu içeriyor (`.claude/skills/impeccable/scripts`) ve yeniden adlandırılır | Proje kopyasında bu yollar da yeni ada çevrilir | `ekli-ad` bilgisi |
| 34 | OpenMontage skilleri OpenMontage kurulmadan kullanılır | `bagimlilik` uyarısı | ön kontrol UYARI |
| 35 | API anahtarı gerektiren skill (AI medya, Composio) | Teknoloji etiketi `api-anahtari`; rol talimatı "anahtarı koda yazma" der | KATALOG |

## Bağımsız teknik incelemeden sonra kapatılanlar (2026-10-21)

| # | Senaryo | Önlem |
|---|---|---|
| 36 | Öncelik değişince aynı `id` başka repo'nun skill'ini gösterir; güncelleme yanlış içeriği kurar | Kilit ve inceleme notları kaynağa (repo + yol) bağlı; kaynak yoksa `kaynak-yok`, asla başka repo |
| 37 | Sadece Claude/Codex sürümü değişir, güncelleme görünmez | Kurulum parmak izi = ana + araç sürümleri |
| 38 | SKILL.md aynı, scriptleri farklı iki klasör "kopya" sayılır, farklı dosyalar kaybolur | Kopya tespiti tüm klasör içeriğiyle |
| 39 | `.DS_Store` / `__pycache__` "elle değiştirildi" alarmı | Parmak izinde yok sayılır |
| 40 | Kullanıcının kendi `.claude/agents/<rol>.md` dosyası ezilir | Etiketsiz dosya → `kendi-agent-dosyan` (zorlanamaz) |
| 41 | `--rol-adi ../../x` ile proje dışına dosya yazılır | Rol adı doğrulanır (zorlanamaz) + yazımda ikinci kontrol |
| 42 | `.claude/skills` → `.agents/skills` ya da globale symlink: kurulum kendini siler / globale yazar | `proje_yapisi_kontrol` (zorlanamaz) |
| 43 | Global durum registry'de eski kalır; sonradan eklenen global skill görülmez | Kurulum anında canlı okunur; `global-cakisma-yeni` |
| 44 | Global durum değişince aynı skill ikinci adla tekrar kurulur | Kurulu kaynağın adı kilitten alınır, değişmez |
| 45 | Güncelleme kaydedilmemiş elle düzenlemeleri de commit'ler | `--uygula` temiz git ağacı ister |
| 46 | Değişiklik yokken `git commit` hata verir, geçici dosyalar önceden silinmiştir | Sadece değişiklik varsa commit; geçiciler en sonda silinir |
| 47 | Force-push / silinen repo betiği çökertir | `GhBulunamadi` yakalanır, raporlanır; `KAYIP` tipi kopyaları korur |
| 48 | Arşiv yer değiştirdikten sonra registry yazılamaz → uyumsuzluk | Registry önce geçiciye yazılır; ikisi art arda yer değiştirir; JSON yazımı atomik |
| 49 | Araç sürümünün bir dosyası inmez ama kontrolden geçer | Araç sürümü dosya sayısı da kontrol edilir |
| 50 | İndirme yarıda kesilir, manifest eski kalır | Manifest her repodan sonra yazılır |
| 51 | Aynı reponun iki kaydı farklı commit'lerden iner | Repo başına tek commit |
| 52 | Gövdedeki ```yaml name:``` örneği değiştirilir; CRLF bozulur | Ad sadece frontmatter'da değişir; bayt düzeyinde yazım |
| 53 | Çok satırlı `description` ilk satırını kaybeder | Frontmatter okuyucu düzeltildi |
| 54 | `--kuru` yine de rapor dosyası yazar | `--kuru` hiçbir dosya yazmaz |
| 55 | Silinen Claude symlink'i onarılmaz | `ekle`/`--guncelle` onarır; `--durum` gösterir |
| 56 | Doğrulama Codex'te açık kalan rol dışı skilleri, symlink hedefini, blokları görmez | `--dogrula` hepsini kontrol eder |
| 57 | `kaldir`/`yenile` hata verirse yarım kalır; geri alma geri alınamaz | Hepsi yedek + otomatik geri alma; `--geri-al <ad>`; 10 yedek |
| 58 | Bozuk işaret (sadece başlangıç) kullanıcı metnini yutar | Bozuk işarette dosyaya dokunulmaz, HATA |
| 59 | `İ` küçültülünce Türkçe eşleme bozulur | Türkçe küçük harf dönüşümü |
| 60 | `gh` oturumu yoksa yeni repo kontrolü sessizce atlanır | Açık UYARI |
| 61 | Arşivdeki dosyalar elle değiştirilir ya da araç sürümü kaybolur | `dogrula.py` içerik parmak izlerini yeniden hesaplar |
| 62 | Kapsam denetimi araç sürümü kararlarını doğrulamaz | Registry + diskte kontrol edilir |

## İlk güncellemede (2026-10-22) bulunan ve kapatılanlar

| # | Senaryo | Önlem |
|---|---|---|
| 63 | Geliştirici skill'leri kaynakta kaldırır (HyperFrames iş akışı skilleri emekliye ayrıldı); güncelleme onları arşivden ve rollerden düşürür | Kaynakta kaldırılan skill arşivde kalır, `kaynak_durumu: kaynakta-kaldirildi`; ön kontrolde `kaynakta-kaldirildi` UYARI, dogrula'da rol UYARISI, katalogda 🗄️emekli |
| 64 | Skill'in kendi `.gitignore`'u arşiv dosyalarını git'ten gizler (embedded-captions `transcript.json`) → git yedeği eksik | Commit'ler `git add -f arsiv` ile; dogrula git'e girmeyen arşiv dosyasını HATA sayar |

| 65 | Aylık güncelleme doğrudan master'ı değiştirir, kötü bir kaynak değişikliği fark edilmeden yayılır | Güncelleme `guncelleme/YYYY-AA` dalında; master sadece `--birlestir` ile ve kontroller geçerse değişir; geçmiş `notlar/guncelleme-gecmisi.md` |

| 66 | Tek repo eklerken (`kaynak-cek --repo X`) geçici klasör boşsa yerleştirme diğer TÜM skilleri arşivden düşürür | İndirilmeyen kaynaklar olduğu gibi korunur; boş manifestte yerleştirme başlamaz; önceki bir skill kaybolursa güvenlik kilidi arşive dokunmadan durur (`--kayba-izin-ver` yalnız bilerek) |
| 67 | Ücretli servis gerektiren skill fark edilmeden role/projeye girer, beklenmedik maliyet | `ucret-siniflandirma.json` (elle, gerekçeli), ön kontrolde `ucretli` UYARI, öneride ücretsizler önde, rol çekirdeğinde ücretli skill dogrula UYARISI, `notlar/ucretli-skiller.md` |
| 68 | Yeni repoda aynı adlı iki farklı SKILL.md (lemo-opuscar) | İçerik karşılaştırması: biri tercih, diğeri `ad@kaynak` alternatif; projeye birlikte aynı adla kurulamaz |
| 69 | Skill repoları birden çok GitHub listesinde dağınık; yeni eklenen skill gözden kaçar | Tek kaynak liste "Yapay Zeka Skillleri"; `github-skill-listesi.py` YENİ/kopya/eksik raporu, dogrula --github "YENİ SKILL REPOSU" uyarısı |
| 70 | Kısmi indirmede yeni skill, korunan (indirilmeyen) aynı adlı skill ile aynı kimliği alır → arşiv kurulumu `FileExistsError` ile durur | Korunan skill kimliğini korur; yeni skill `ad@kaynak`'a taşınır (`KİMLİK:` satırı). Kurulumlar kaynağa (repo+yol) bağlı olduğu için kimlik değişimi projeleri bozmaz |
| 71 | Elle verilen tercih (`durum_elle`) kısmi indirmede öncelik kuralıyla ezilir (ör. 1 KB'lık yönlendirme `remotion` OpenMontage'ı geçti) | Çakışma çözümü `durum_elle`'yi önceliğin önüne koyar; iki tur üst üste çalıştırılıp kararlılık doğrulandı |
| 72 | Toplama repolarında içeriği olmayan "yönlendirme" skilleri (sadece upstream linki; open-design'da 82 tane) öneride öne çıkar | Elle `kalite: 1` + `kalite_notu`; puan düşer, `--oner` alt sıralara iter. Upstream'deki tam sürümü ya da kütüphanedeki eşini kullan |
| 73 | Yeni ad kuralı başka repodaki aynı adlı skillin kategorisini sessizce değiştirir | `ad_kurallari` kaydında `repo` alanı: kural sadece o repoya uygulanır; ekleme sonrası eski kayıtların kategori farkı (git HEAD'e göre) kontrol edilir |

## Bilinen sınırlar (bilinçli)
- Kategori ve teknoloji etiketleri **ilk aşamada otomatiktir**; kesin bilgi kategori incelemesiyle gelir (`07-kategori-inceleme.md`).
- Değerlendirme puanı GitHub verisinden hesaplanır; içerik kalitesini ölçmez. Elle `kalite` (1–5) verince %40 ağırlıkla katılır.
- Codex'in alt-agent'a sadece belirli skilleri **verme** (allowlist) özelliği yok; kapatma (denylist) ile çözülür.
- Komut/agent bileşenleri (`arsiv/_bilesenler/`) arşivlenir ama otomatik kurulmaz; gerekirse elle `.claude/commands/` içine kopyalanır.
