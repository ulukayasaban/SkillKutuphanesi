> Yeni oturum mu? Önce [BASLA.md](BASLA.md) · kalıcı kararlar: [notlar/kararlar.md](notlar/kararlar.md)

# SkillKutuphanesi

GitHub'da yıldızladığın repolardaki agent skillerinin **yerel, tekrarsız, sürüm takipli arşivi** ve onları
**sadece seçtiğin projeye, seçtiğin agent'a** güvenli şekilde kuran araç seti. Desteklenen araçlar: Claude Code, Codex, Antigravity,
Cursor, VS Code Copilot (`yapay-zeka-araclari.json`, [rehber/14](rehber/14-yapay-zeka-araclari.md)).

- Kütüphane araçları global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) hiçbir zaman yazmaz.
  Bu klasörler 2026-11-12'de boşaltıldı (karar: `notlar/kararlar.md` K-04, K-40); yöntem ve yedek: [rehber/12](rehber/12-genel-klasor-bosaltma.md), [rehber/13](rehber/13-yedek-ve-geri-alma.md).
  Skiller yalnız projenin içine kurulur.
- Hiçbir şey otomatik kurulmaz; her kurulumdan önce ön kontrol raporu çıkar.

## Amaç
Yapay zekâ kodlama araçları (Claude Code, Codex, Antigravity, Cursor, Copilot) "skill" denen yönerge paketleriyle genişler.
GitHub'da yüzlerce repoda dağınık duran bu skilleri her projeye elle kopyalamak sürüm, çakışma ve güvenlik sorunu doğurur.
Bu depo o sorunu çözer:

- **Tek arşiv:** Yıldızlanan 127 repodaki 5.649 skill, sabit commit'le ve tekrarsız olarak `arsiv/` altında durur; 53 repo da
  skill içermeyen referans (kütüphane/teknoloji) olarak kayıtlıdır.
- **Seçerek kurulum:** Skiller projeye profil (23 proje tipi) ya da rol (31 agent rolü) seçilerek kurulur; her kurulumdan önce
  ön kontrol raporu (çakışma, ücret, lisans, bağımlılık) çıkar ve onay beklenir.
- **İzlenebilirlik:** Her kurulum projenin `.skill-kutuphanesi/kilit.json` dosyasına kaynağı ve commit'iyle yazılır; aylık
  güncelleme ayrı git dalında hazırlanır, onaydan sonra birleştirilir. Hangi projenin hangi skili kullandığı tek raporda tutulur.

## Nasıl çalışır
```
GitHub "Yapay Zeka Skillleri" listesi ─► kaynak-cek.py ─► arsiv-yerlestir.py ─► registry.json + KATALOG.md
        (yıldızlanan repolar)             (sabit commit)    (tekilleştirme, kimlik,       (inceleme, ücret, puan)
                                                             kategori, ücret)
                                                                   │
   proje ◄── skill-ekle.py --evet ◄── --kuru (ön kontrol raporu) ◄─┘  ◄── --oner "ihtiyaç" (tüm kütüphane taranır)
```
1. **Kaynak:** Yeni repo GitHub listesine eklenir; `github-skill-listesi.py` bunu bulur. Çakışma ve ücret kontrolünden sonra
   `kaynaklar.json`'a kaydedilir (`rehber/03`).
2. **Arşiv:** Repo klonlanmaz; yalnız skill klasörleri sabit commit'ten indirilir. Aynı içerik tek kopya olur, aynı adlı farklı
   skiller `ad@kaynak` kimliği alır; çıplak ad kendiliğinden el değiştirmez (`rehber/09`).
3. **Kayıt:** `registry.json` her skilin kaynağını, kategorisini, ücret sınıfını, lisansını ve elle inceleme notlarını tutar;
   `KATALOG.md` ve Türkçe rehber (`README-SKILLER.md`, `skiller/`) bundan üretilir.
4. **Kurulum:** `skill-ekle.py` önce öneri (`--oner`), sonra rapor (`--kuru`), onaydan sonra kurulum (`--evet`) yapar; her işlemden
   önce yedek alır, hata olursa geri döner. Global skill klasörlerine hiçbir zaman yazmaz.
5. **Bakım:** `arsiv-guncelle.py` aylık olarak kaynakların yeni commit'lerini ayrı dalda getirir; `dogrula.py`, `kapsam-denetimi.py`
   ve `test.py` her değişiklikten sonra çalışır. HyperFrames ve OpenMontage gibi skill olmayan programlar `programlar.json` ile izlenir.

## Hızlı başlangıç
```bash
cd ~/Documents/SkillKutuphanesi
python3 araclar/skill-ekle.py --oner "next.js landing page gsap animasyonlu"          # ne kullanmalıyım?
python3 araclar/skill-ekle.py ~/Projeler/site --profil landing-page --kuru            # ön kontrol raporu
python3 araclar/skill-ekle.py ~/Projeler/site --profil landing-page --evet            # kur
python3 araclar/skill-ekle.py ~/Projeler/site --dogrula                               # kontrol
```

## Klasörler
| Yol | İçerik |
|---|---|
| `README-SKILLER.md`, `skiller/` | **Türkçe skill rehberi:** tüm skiller ne işe yarar, ne zaman kullanılır, nasıl çağrılır (`araclar/skill-readme.py` üretir; çeviriler `aciklama-tr.json`, `araclar/ceviri-tr.py`) |
| `KATALOG.md` | Tüm görünür skiller: kategori, ne yapar, teknoloji, Codex uyumu, puan (otomatik üretilir) |
| `TEST_RAPORU.md` | Skill çalıştırma testi: her skill kurulup yükleme/bağlantı/betik sözdizimi sınanır, örneklem gerçek agent'la denenir (`araclar/skill-calistir.py`) |
| `yamalar/<skill id>/` | Kurulan kopyada orijinalin yerine geçen düzeltilmiş dosyalar (arşiv değişmez; `rehber/03`) |
| `registry.json` | **Tek gerçek kaynak**: her skill'in kaydı (kaynak, commit, kategori, uyum, geliştirici, puan, inceleme notları) |
| `arsiv/<alan>/<kategori>/<skill>/` | Skill'in orijinal dosyaları + `KAYNAK.md` |
| `arsiv/_varyantlar/<skill>/<claude|codex>/` | Araca özel uyarlanmış sürümler |
| `arsiv/_bilesenler/` | Skillerle gelen komut/agent dosyaları (otomatik kurulmaz) |
| `roller/`, `profiller/` | Agent rolleri (rol → skiller) ve proje tipleri (profil → roller) |
| `kaynaklar.json` | Hangi repolar, hangi tipte, hangi kurallarla alınır; `arsivden_cikarilanlar` (bilerek çıkarılan eski sürümler) |
| `trend.json`, `notlar/github-trend.md` | GitHub Trending geçmişi ve raporu |
| `notlar/proje-kullanimi.md` · `projeler.json` | Hangi proje hangi skili kullanıyor (proje bilgisinin tek yeri; `araclar/proje-kullanimi.py` üretir, elle notlar `projeler.json`) |
| `notlar/populer-skiller.md` | GitHub'da popüler skill repoları (REST araması, adayda SKILL.md sayımı; `araclar/populer-tarama.py`) |
| `konu-takip.json`, `notlar/konu-takip.md` | Konu takibi (aday repolar, değerlendirme kararları) |
| `kendi/`, `site/` | Yerel kaynaklar: `kendi/` yalnız kullanıcının kendi yazdığı skiller (`yerel/kendi`, T7); `site/` web sitesinden alınan, GitHub'da olmayan skiller (`yerel/site`, T8; `site/README.md`, K-57) |
| `site-takip.json`, `notlar/site-takip.md` | Site skillerinin zorunlu kaydı (sahip, lisans, site, izlenen adresler ve sha256) ve son site takibi raporu (rapor git dışı) |
| `kategoriler.json`, `kategori-kurallari.json` | Alanlar/kategoriler ve otomatik atama kuralları |
| `gelistiriciler.json`, `notlar/guven-siralamasi.md` | Agent için güven ve referans rehberi (karar kuralları, kategori → en güvenilir kaynak/skill, referans kütüphanesi → ilgili skiller); repo sahipleri ve GitHub güven puanı: yıldız, yıldız hızı, katkıcı, commit, fork, izleyici, sürüm; kaynaklar arası sıra ve derece (referans kütüphaneleri ayrı sıralı) |
| `notlar/roller-ve-profiller.md` | Tüm rol ve profillerin özeti (otomatik üretilir) |
| `notlar/ucretli-skiller.md`, `ucret-siniflandirma.json` | Ücretli / kısmen ücretli skiller ve gerekçeleri (sınıflandırma elle, liste otomatik) |
| `notlar/` | Kapsam denetimi, geliştiriciler, teknoloji rehberi, T5/T6 referans notları, kategori inceleme raporları |
| `BASLA.md`, `notlar/kararlar.md` | Yeni oturumun giriş belgesi (okuma sırası, hangi isteğe hangi komut) ve kullanıcının kalıcı kararları |
| `yapay-zeka-araclari.json` | Desteklenen yapay zeka araçları: hangi klasörü ve talimat dosyasını okur, doğrulama tarihi (`rehber/14`) |
| `yedekler.json` | Makine geneli yedeklerin envanteri: ne, nerede, nasıl geri yüklenir (`rehber/13`; `araclar/yedek-denetim.py` okur) |
| `programlar.json`, `programlar/` | Skill olmayan programlar (HyperFrames, OpenMontage, etsyotomasyon): kartlar ve kaynak kayıtları (`rehber/11`) |
| `rehber/` | Süreç notları (aşağıda) |
| `araclar/` | Python araçları (sadece standart kütüphane + `gh` CLI) |

## GitHub deposu (private)
Kütüphane [ulukayasaban/SkillKutuphanesi](https://github.com/ulukayasaban/SkillKutuphanesi) deposunda **private** tutulur;
varsayılan dal `master` (araçlar `ANA_DAL = "master"` kullanır).

- **Neden private:** `arsiv/` üçüncü taraf repolardan alınmış skillerin kopyalarını içerir; bazılarının lisansı yok ya da belirsiz
  (`NOASSERTION`). Depo herkese açık yapılmaz, başkasıyla paylaşılmadan önce lisanslar ayrıca incelenir.
- **Yerel kopya asıl kopyadır.** Tüm araçlar `~/Documents/SkillKutuphanesi` üzerinde çalışır; GitHub yedek ve inceleme (PR) kaydıdır.
  Push ve PR **sadece kullanıcı isteyince** yapılır; aylık zamanlanmış görev hiçbir şey push etmez.
- **Gönderilmeyenler** (`.gitignore`): `.gecici/`, `.arsiv-yeni/`, `.arsiv-eski/`, `.guncelleme-kilidi`, `__pycache__/`, `.DS_Store`,
  `/.env*`, `/*.pem`, `/*.key`, `/*.p12`, `/*.pfx`, `/programlar/**/.env`, `/yedek/`, `/.skill-kutuphanesi/`, `/*.bundle`, `/*.yedek`
  ve makineye özgü iki dosya (`notlar/son-aylik-calisma.json`, `notlar/aylik-ozet.md`).
- **Başka bilgisayarda kurmak:** Python 3 (sadece standart kütüphane) + `gh` CLI (`gh auth login`) yeterli.
  ```bash
  gh repo clone ulukayasaban/SkillKutuphanesi ~/Documents/SkillKutuphanesi
  cd ~/Documents/SkillKutuphanesi && python3 araclar/dogrula.py && python3 araclar/kapsam-denetimi.py
  ```
  Projelerin `kilit.json` dosyaları kütüphane yolunu tutar; kütüphane farklı bir yola klonlanırsa `promptlar/09-proje-tasindi-veya-bozuldu.md`.
  Tam geri kurma listesi, geri gelmeyenler ve makine durumu: [rehber/13-yedek-ve-geri-alma.md](rehber/13-yedek-ve-geri-alma.md).
  **GitHub'a gönderilmemiş commit'ler klonda yoktur; önce `python3 araclar/git-durum.py` çalıştır.** Klondan sonra `python3 araclar/dogrula.py`
  ve `python3 araclar/git-durum.py`; skill'lerin kendi `.gitignore` dosyaları yüzünden eksik gelen arşiv dosyası `dogrula.py` tarafından HATA olarak gösterilir.

### Değişiklik süreci (PR)
| Değişiklik | Akış |
|---|---|
| Araç, rehber, rol/profil, not | Dal aç → değiştir → `kapsam-denetimi.py` (0 sorun) + `dogrula.py` (0 hata) + `test.py` → commit → push → PR (`master`'a) → incele → GitHub'da birleştir → yerelde `git switch master && git pull` |
| Aylık güncelleme (`guncelleme/YYYY-AA`) | `arsiv-guncelle.py --uygula --dal` → dalı push et, PR aç (inceleme kaydı) → onay → **yerelde** `--birlestir <dal>` → `git push origin master` (PR kendiliğinden "merged" olur) → `git push origin --delete <dal>` |

Aylık güncelleme PR'ı GitHub'daki **Merge düğmesiyle birleştirilmez**: `--birlestir` birleştirmeden sonra doğrulama/kapsam/testleri
çalıştırır ve başarısızsa `master`'ı otomatik geri alır; bu güvence sadece yerel birleştirmede vardır. Ayrıntı: [rehber/02](rehber/02-guncelleme-yonergesi.md#githuba-gönderme-private-depo).
PR açıklaması `.github/pull_request_template.md` kontrol listesiyle gelir.

## Hazır promptlar
Yeni projelerde ve bakımda kopyala-yapıştır kullanılacak 16 prompt: [promptlar/README.md](promptlar/README.md)

## Rehberler
1. [Skill ekleme süreci ve örnekler](rehber/01-skill-ekleme-sureci.md)
2. [Güncelleme yönergesi](rehber/02-guncelleme-yonergesi.md)
3. [Yeni skill / repo ekleme](rehber/03-yeni-skill-ekleme.md)
4. [Agent'a skill verirken kontrol listesi](rehber/04-kontrol-listesi.md)
5. [Riskler ve önlemler](rehber/05-risk-ve-onlemler.md)
6. [Değerlendirme ve geliştirici bilgisi](rehber/06-degerlendirme-ve-gelistirici.md)
7. [Kategori inceleme süreci](rehber/07-kategori-inceleme.md)
8. [Test süreci](rehber/08-test-sureci.md): otomatik kontroller, gerçek agent testi, Claude hesabıyla ad çakışması
9. [Ad, kimlik ve çakışma kuralları](rehber/09-ad-kimlik-ve-cakisma.md): çıplak ad el değiştirmez, aynı ad farklı iş, ad devri, repo adı değişirse
10. [Proje kullanımı](rehber/10-proje-kullanimi.md): hangi proje hangi skili kullanıyor; proje bilgisinin tek yeri
11. [Program yönetimi](rehber/11-program-yonetimi.md): HyperFrames, OpenMontage ve benzeri programların kurulumu, güncellemesi, geri alınması
12. [Genel klasör boşaltma](rehber/12-genel-klasor-bosaltma.md): bilgisayarın genelindeki skill klasörlerini yedekleyip boşaltma
13. [Yedek ve geri alma](rehber/13-yedek-ve-geri-alma.md): yedek envanteri, git geri alma, yeni bilgisayara geri kurma
14. [Yapay zeka araçları](rehber/14-yapay-zeka-araclari.md): hangi araç hangi klasörü ve talimat dosyasını okur, yeni araç ekleme

## Alanlar
`a-tasarim-onyuz` · `b-yazilim-gelistirme` · `c-dokuman-icerik` · `d-ai-otomasyon` · `g-video-ses-medya` · `h-is-alanlari` (e-ticaret/pazaryeri dahil) · `i-bilim-muhendislik`
· gizli: `e-entegrasyon-katalogu` (Composio), `f-repo-ici` (repo katkı skilleri)

## Araçlar
| Komut | Ne yapar |
|---|---|
| `skill-ekle.py` | Projeye ekle / öner / listele / durum / doğrula / güncelle / kaldır / geri al |
| `arsiv-guncelle.py [--uygula --dal] [--birlestir <dal>]` | Aylık güncelleme: rapor → `guncelleme/YYYY-AA` dalında güncelleme → onayla master'a birleştirme |
| `kaynak-cek.py [--atla owner/ad]` → `arsiv-yerlestir.py` | İndir → tekilleştir, kategorile, değerlendir |
| `kapsam-denetimi.py` | Her SKILL.md'nin açıklandığını bağımsız doğrular |
| `katalog-uret.py` | KATALOG ve notları üretir |
| `dogrula.py [--github]` | Tutarlılık; yıldızlı ama tanımsız repo |
| `gelistirici-bilgisi.py` | Geliştirici bilgileri + GitHub güven puanı/sıralaması → `notlar/guven-siralamasi.md` |
| `site-takip.py [--skill ad] [--yazmadan] [--indir] [--siki] [--kayit-denetle]` | Site skillerinin kaynak sitesi değişti mi (yalnız GET): AYNI / DEĞİŞTİ / YENİ İÇERİK / ERİŞİLEMEDİ → `notlar/site-takip.md`; `--indir` değişenleri kütüphane dışına indirir; skili güncellemez (rehber/03 B3) |
| `konu-takip.py [--konu X] [--rapor] [--karar repo karar neden] [--bekleyenler]` | Takip edilen alanlarda (e-ticaret/Etsy, mobil…) GitHub'da yeni skill repolarını arar → `notlar/konu-takip.md`; değerlendirilenler tekrar gösterilmez |
| `github-trend.py [--rapor] [--aday]` | GitHub Trending takibi: trend'e giren kaynaklar (değerlendirme +10/+6/+2, öneride öne alma), trend'deki aday skill repoları → `notlar/github-trend.md` |
| `proje-kullanimi.py [--skill id] [--repo owner/ad]` · `--saglik` / `--tara-kayitsiz` / `--ekle` / `--cikar` / `--tasindi` / `--yoksay` | Projelerin `kilit.json` dosyalarını okur → `notlar/proje-kullanimi.md`; bir skili/kaynağı kullanan projeleri listeler (silmeden, tercih değiştirmeden önce); proje sağlığı → `notlar/proje-durumu.md`; proje ekle/çıkar/taşındı/yoksay (yalnız `projeler.json`) |
| `github-skill-listesi.py [--duzenle] [--ekle owner/ad …]` | GitHub 'Yapay Zeka Skillleri' listesi: kütüphanenin tüm kaynakları tek listede (başka skill listesi yok); yeni/kopya/eksik/adı değişen raporu, `--duzenle` yıldızlar ve taşır, `--ekle` kütüphanede olmayan repoyu yalnızca listeye koyar (kütüphaneye eklemez) |
| `test.py` | Uçtan uca güvenlik testleri (geçici projede) |
| `duman-testi.py [--araclar] [--kirli-ok]` | Tüm sürecin hızlı uçtan uca duman testi (git, doğrulama, kapsam, testler, tüm profiller, kurulum yaşam döngüsü, isteğe bağlı gerçek Claude/Codex) |
| `aylik-ozet.py [--hizli]` | Oturum başı özeti: git, genel klasörler, yedek, program, proje, aday kararları; `--hizli` ağsız ve yazmasız (en çok 15 satır) |
| `git-durum.py [--kisa] [--ozet-json]` | Git durumu (push gecikmesi, bekleyen dal, büyük dosya); salt okuma |
| `yedek-denetim.py [--ozet-json]` | `yedekler.json` envanterini denetler (yaş, gizli içerik, silme hatırlatması); hiçbir şey silmez |
| `genel-bekci.py [--ozet-json] [--taban-yaz]` | Genel skill klasörlerinde beklenmeyen girdi var mı; boşaltma planı (`--plan`); salt okuma |
| `program-denetim.py [--oncesi ad] [--sema]` | Programların (HyperFrames, OpenMontage…) sürüm ve güncelleme öncesi kontrolü, kart şeması → `notlar/program-denetimi.md` |
| `kaynak-cikar.py [--repo owner/ad] [--kuru]` | Bir kaynağı ya da skili çıkarmadan önce etki, adımlar ve geri alma planı (yalnız okur) |
| `yol-tara.py [--repo owner/ad] [--siki]` | Skillerdeki sabit genel yol taraması; yeni kaynak için "yol kapısı" |
| `listeye-ekle.py owner/ad` | Kütüphanede olmayan bir repoyu yıldızlar ve 'Yapay Zeka Skillleri' listesine koyar (kendi onay sorusunu sorar; kütüphaneye eklemez) |
