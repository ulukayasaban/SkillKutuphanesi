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
| `kaynaklar.json` | Hangi repolar, hangi tipte, hangi kurallarla alınır |
| `kategoriler.json`, `kategori-kurallari.json` | Alanlar/kategoriler ve otomatik atama kuralları |
| `gelistiriciler.json` | Repo sahipleri, yıldız, lisans, bakım |
| `notlar/roller-ve-profiller.md` | Tüm rol ve profillerin özeti (otomatik üretilir) |
| `notlar/` | Kapsam denetimi, geliştiriciler, teknoloji rehberi, T5/T6 referans notları, kategori inceleme raporları |
| `rehber/` | Süreç notları (aşağıda) |
| `araclar/` | Python araçları (sadece standart kütüphane + `gh` CLI) |

## Rehberler
1. [Skill ekleme süreci ve örnekler](rehber/01-skill-ekleme-sureci.md)
2. [Güncelleme yönergesi](rehber/02-guncelleme-yonergesi.md)
3. [Yeni skill / repo ekleme](rehber/03-yeni-skill-ekleme.md)
4. [Agent'a skill verirken kontrol listesi](rehber/04-kontrol-listesi.md)
5. [Riskler ve önlemler](rehber/05-risk-ve-onlemler.md)
6. [Değerlendirme ve geliştirici bilgisi](rehber/06-degerlendirme-ve-gelistirici.md)
7. [Kategori inceleme süreci](rehber/07-kategori-inceleme.md)

## Alanlar
`a-tasarim-onyuz` · `b-yazilim-gelistirme` · `c-dokuman-icerik` · `d-ai-otomasyon` · `g-video-ses-medya`
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
| `gelistirici-bilgisi.py` | Geliştirici bilgileri |
| `test.py` | Uçtan uca güvenlik testleri (geçici projede) |
| `duman-testi.py [--araclar]` | Tüm sürecin hızlı uçtan uca duman testi (git, doğrulama, kapsam, testler, tüm profiller, kurulum yaşam döngüsü, isteğe bağlı gerçek Claude/Codex) |
