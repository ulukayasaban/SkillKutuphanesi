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
| 11 | SKILL.md'nin gösterdiği dosya arşivde yok (atlanan video vb.) | Göreli bağlantılar kontrol edilir | `kirik_baglantilar`, ön kontrol UYARI |
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
| 23 | Yanlış kurulum yapıldı | Her işlem öncesi yedek (son 5) | `--geri-al` |
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

## Bilinen sınırlar (bilinçli)
- Kategori ve teknoloji etiketleri **ilk aşamada otomatiktir**; kesin bilgi kategori incelemesiyle gelir (`07-kategori-inceleme.md`).
- Değerlendirme puanı GitHub verisinden hesaplanır; içerik kalitesini ölçmez. Elle `kalite` (1–5) verince %40 ağırlıkla katılır.
- Codex'in alt-agent'a sadece belirli skilleri **verme** (allowlist) özelliği yok; kapatma (denylist) ile çözülür.
- Komut/agent bileşenleri (`arsiv/_bilesenler/`) arşivlenir ama otomatik kurulmaz; gerekirse elle `.claude/commands/` içine kopyalanır.
