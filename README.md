# SkillKutuphanesi

GitHub'da yıldızladığın repolardaki agent skillerinin **yerel, tekrarsız, sürüm takipli arşivi** ve onları
**sadece seçtiğin projeye, seçtiğin agent'a** Claude Code + Codex için güvenli şekilde kuran araç seti.

- Global skill klasörlerin (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) **değişmez**;
  eski agent'ların onlarla çalışmaya devam eder. Yeni projeler skillerini buradan alır.
- Hiçbir şey otomatik kurulmaz; her kurulumdan önce ön kontrol raporu çıkar.

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
| `KATALOG.md` | Tüm görünür skiller: kategori, ne yapar, teknoloji, Codex uyumu, puan (otomatik üretilir) |
| `registry.json` | **Tek gerçek kaynak**: her skill'in kaydı (kaynak, commit, kategori, uyum, geliştirici, puan, inceleme notları) |
| `arsiv/<alan>/<kategori>/<skill>/` | Skill'in orijinal dosyaları + `KAYNAK.md` |
| `arsiv/_varyantlar/<skill>/<claude|codex>/` | Araca özel uyarlanmış sürümler |
| `arsiv/_bilesenler/` | Skillerle gelen komut/agent dosyaları (otomatik kurulmaz) |
| `roller/`, `profiller/` | Agent rolleri (rol → skiller) ve proje tipleri (profil → roller) |
| `kaynaklar.json` | Hangi repolar, hangi tipte, hangi kurallarla alınır; `arsivden_cikarilanlar` (bilerek çıkarılan eski sürümler) |
| `trend.json`, `notlar/github-trend.md` | GitHub Trending geçmişi ve raporu |
| `konu-takip.json`, `notlar/konu-takip.md` | Konu takibi (aday repolar, değerlendirme kararları) |
| `kategoriler.json`, `kategori-kurallari.json` | Alanlar/kategoriler ve otomatik atama kuralları |
| `gelistiriciler.json`, `notlar/guven-siralamasi.md` | Agent için güven ve referans rehberi (karar kuralları, kategori → en güvenilir kaynak/skill, referans kütüphanesi → ilgili skiller); repo sahipleri ve GitHub güven puanı: yıldız, yıldız hızı, katkıcı, commit, fork, izleyici, sürüm; kaynaklar arası sıra ve derece (referans kütüphaneleri ayrı sıralı) |
| `notlar/roller-ve-profiller.md` | Tüm rol ve profillerin özeti (otomatik üretilir) |
| `notlar/ucretli-skiller.md`, `ucret-siniflandirma.json` | Ücretli / kısmen ücretli skiller ve gerekçeleri (sınıflandırma elle, liste otomatik) |
| `notlar/` | Kapsam denetimi, geliştiriciler, teknoloji rehberi, T5/T6 referans notları, kategori inceleme raporları |
| `rehber/` | Süreç notları (aşağıda) |
| `araclar/` | Python araçları (sadece standart kütüphane + `gh` CLI) |

## Hazır promptlar
Yeni projelerde ve bakımda kopyala-yapıştır kullanılacak 11 prompt: [promptlar/README.md](promptlar/README.md)

## Rehberler
1. [Skill ekleme süreci ve örnekler](rehber/01-skill-ekleme-sureci.md)
2. [Güncelleme yönergesi](rehber/02-guncelleme-yonergesi.md)
3. [Yeni skill / repo ekleme](rehber/03-yeni-skill-ekleme.md)
4. [Agent'a skill verirken kontrol listesi](rehber/04-kontrol-listesi.md)
5. [Riskler ve önlemler](rehber/05-risk-ve-onlemler.md)
6. [Değerlendirme ve geliştirici bilgisi](rehber/06-degerlendirme-ve-gelistirici.md)
7. [Kategori inceleme süreci](rehber/07-kategori-inceleme.md)

## Alanlar
`a-tasarim-onyuz` · `b-yazilim-gelistirme` · `c-dokuman-icerik` · `d-ai-otomasyon` · `g-video-ses-medya` · `h-is-alanlari` (e-ticaret/pazaryeri dahil) · `i-bilim-muhendislik`
· gizli: `e-entegrasyon-katalogu` (Composio), `f-repo-ici` (repo katkı skilleri)

## Araçlar
| Komut | Ne yapar |
|---|---|
| `skill-ekle.py` | Projeye ekle / öner / listele / durum / doğrula / güncelle / kaldır / geri al |
| `arsiv-guncelle.py [--uygula --dal] [--birlestir <dal>]` | Aylık güncelleme: rapor → `guncelleme/YYYY-AA` dalında güncelleme → onayla master'a birleştirme |
| `kaynak-cek.py` → `arsiv-yerlestir.py` | İndir → tekilleştir, kategorile, değerlendir |
| `kapsam-denetimi.py` | Her SKILL.md'nin açıklandığını bağımsız doğrular |
| `katalog-uret.py` | KATALOG ve notları üretir |
| `dogrula.py [--github]` | Tutarlılık; yıldızlı ama tanımsız repo |
| `gelistirici-bilgisi.py` | Geliştirici bilgileri + GitHub güven puanı/sıralaması → `notlar/guven-siralamasi.md` |
| `konu-takip.py [--konu X] [--rapor] [--karar repo karar neden]` | Takip edilen alanlarda (e-ticaret/Etsy, mobil…) GitHub'da yeni skill repolarını arar → `notlar/konu-takip.md`; değerlendirilenler tekrar gösterilmez |
| `github-trend.py [--rapor] [--aday]` | GitHub Trending takibi: trend'e giren kaynaklar (değerlendirme +10/+6/+2, öneride öne alma), trend'deki aday skill repoları → `notlar/github-trend.md` |
| `github-skill-listesi.py [--duzenle]` | GitHub 'Yapay Zeka Skillleri' listesi: kütüphanenin tüm kaynakları tek listede (başka skill listesi yok); yeni/kopya/eksik raporu, `--duzenle` yıldızlar ve taşır |
| `test.py` | Uçtan uca güvenlik testleri (geçici projede) |
| `duman-testi.py [--araclar]` | Tüm sürecin hızlı uçtan uca duman testi (git, doğrulama, kapsam, testler, tüm profiller, kurulum yaşam döngüsü, isteğe bağlı gerçek Claude/Codex) |
