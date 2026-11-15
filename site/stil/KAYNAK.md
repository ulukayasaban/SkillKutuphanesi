# stil: kaynak bilgisi

> Bu dosya kütüphanenin kendi notudur, skill'in parçası değildir. Asıl kopya `site/stil/KAYNAK.md`'dir: `arsiv-yerlestir.py`
> arşivdeki kopyanın yerine kendi ürettiği KAYNAK.md'yi yazar, `skill-ekle.py` KAYNAK.md'yi projeye kurmaz.
> Site takibinin makine okunur kaydı (izlenen adresler, sha256, sahip, lisans) kökteki `site-takip.json` → `stil`; takip `python3 araclar/site-takip.py`.

- **Yazar:** Smokich (YouTube: https://www.youtube.com/@DevSmokich)
- **Site:** https://smokich.gosem.dev/stil/ ("Video Stilleri")
- **Stillerin kökeni:** uzun stil prompt'ları Michael Szach'ın stil kütüphanesinden Claude Code'a uyarlanmıştır (kütüphane:
  https://szach.kit.com, GitHub'da yok). Sitenin alt bilgisindeki atıf bağlantısı bir YouTube videosudur: https://youtu.be/6_MrVEXM06E
- **Lisans:** belirtilmemiş. Kişisel kullanım; kütüphane private depoda tutar, dağıtılmaz.
- **İndirme tarihi:** 2026-11-15
- **Kütüphanedeki yeri:** yerel kaynak `yerel/site` (tip T8, siteden alınan skiller), klasör `site/stil/` (2026-11-15'e dek `kendi/stil/`; K-57)

## Kütüphanenin yaptığı değişiklikler
- `SKILL.md`: `stil-skill.md` bayt bayt aynen; sonuna "Ready-made styles (added by the library)" bölümü eklendi (`---` ile ayrılmış).
- `references/stiller/<id>.txt`: 7 uzun prompt, indirildiği gibi.
- `references/stiller/README.md`: kütüphane yazdı (11 stilin tablosu `site.js` → `STILLER`; kısa şablon `site.js` → `promptParcalari()`).

## İndirilen dosyalar (takip için)
sha256, indirilen dosyanın baytları üzerinden. Takip, bu özetlerden biri değişirse kaynağın değiştiğini anlar.

| Dosya | URL | Bayt | sha256 | Kütüphanede |
|---|---|---|---|---|
| skill | https://smokich.gosem.dev/stil/stil-skill.md | 7959 | `d9dd7d43b76b6b0eb6b96c92c27744eee3cb15efc1d16b89d2f2f798ce9506a7` | `SKILL.md` (başı) |
| site betiği | https://smokich.gosem.dev/stil/site.js | 13155 | `8cda758f49aa4a73523aa1ebc3f99c2c186fe83e81c8289e85708cd2fdbfb0f6` | alınmadı (tablo ve şablon README'ye) |
| ana sayfa | https://smokich.gosem.dev/stil/ | 26718 | `339c936768c673f3ecf4d4a5a4391db6e4ff9ba12617525254ef8c0511f54ce9` | alınmadı |
| cam | https://smokich.gosem.dev/stil/stiller-uzun/cam.txt | 40722 | `f90c1767f3d946565b033bbaee8ac2557f1d59f85c185a2980bda93fb09bc921` | `references/stiller/cam.txt` |
| risograf | https://smokich.gosem.dev/stil/stiller-uzun/risograf.txt | 44426 | `c6f711de5d68f7a5127004d6dcee4dc3b722834bf5512dac1a934eeb63b790ce` | `references/stiller/risograf.txt` |
| kesik-kagit | https://smokich.gosem.dev/stil/stiller-uzun/kesik-kagit.txt | 27405 | `814ab49559e0769a41a8bf7e0d62ca3b5727101eb61755745aab7da7a2d50d8e` | `references/stiller/kesik-kagit.txt` |
| izometrik | https://smokich.gosem.dev/stil/stiller-uzun/izometrik.txt | 45107 | `0596f5a62963f500441b2e4ee97eb98edba11d1eeb5f0ca95d41e2d2b45897db` | `references/stiller/izometrik.txt` |
| duz-vektor | https://smokich.gosem.dev/stil/stiller-uzun/duz-vektor.txt | 44770 | `864df8617ca6685c4e7148821741dcc944a03e4cfc03febab035cc2dfbbbd791` | `references/stiller/duz-vektor.txt` |
| kinetik | https://smokich.gosem.dev/stil/stiller-uzun/kinetik.txt | 37853 | `9bfe000afc5ba2fe402d9f438bf8a7ef44ce3ee3d94c624c6e443f3cf3419987` | `references/stiller/kinetik.txt` |
| parcacik | https://smokich.gosem.dev/stil/stiller-uzun/parcacik.txt | 31334 | `97863f207592c59c688c58425b1df4a013f67d5ae79d157bf493b611a65e8c4a` | `references/stiller/parcacik.txt` |
| kagit-poster | https://smokich.gosem.dev/stil/stiller-uzun/kagit-poster.txt | 156 | `ab7e8078e04e24f97a9c5e223cdf7d53d1504ce06638dd2d743612cf200afa6b` | yönlendirme, uzun prompt yok |
| konstruktivist | https://smokich.gosem.dev/stil/stiller-uzun/konstruktivist.txt | 156 | `ab7e8078e04e24f97a9c5e223cdf7d53d1504ce06638dd2d743612cf200afa6b` | yönlendirme, uzun prompt yok |
| bilim | https://smokich.gosem.dev/stil/stiller-uzun/bilim.txt | 156 | `ab7e8078e04e24f97a9c5e223cdf7d53d1504ce06638dd2d743612cf200afa6b` | yönlendirme, uzun prompt yok |
| ascii | https://smokich.gosem.dev/stil/stiller-uzun/ascii.txt | 156 | `ab7e8078e04e24f97a9c5e223cdf7d53d1504ce06638dd2d743612cf200afa6b` | yönlendirme, uzun prompt yok |
| icerik.md | doğrulanmadı (büyük olasılıkla https://smokich.gosem.dev/stil/icerik.md) | 156 | `ab7e8078e04e24f97a9c5e223cdf7d53d1504ce06638dd2d743612cf200afa6b` | yönlendirme; `site.js` kısa şablonun buradan geldiğini söyler |

Notlar:
- `ab7e8078…` sitenin ana sayfaya yönlendiren 156 baytlık HTML'sidir. Bu dört stil dosyasından birinin özeti değişirse o stilin
  uzun prompt'u gelmiş olabilir; `site.js` içindeki `UZUN_IDLER` listesi de değişir.
- Ana sayfadaki gömülü skill metni (`<script id="stil-skill">`) 2026-11-15'te `stil-skill.md` ile birebir aynıydı.
- Ana sayfada 11 stilin kısa stil kartları var (`<script type="text/plain" id="stil-<id>">`); 2026-11-15te `references/stiller/kartlar/<id>.md` dosyalarına aynen alındı (ana sayfa özeti yukarıdaki tabloda).
- Ana sayfa adresi ve `site.js` adresi ana sayfadaki bağlantılardan (`site.js?v=4`) çıkarıldı; sürüm sorgusu (`?v=4`) özete girmez.

## Güvenlik notu
- Skill, eksik araçları kendisi kurar: başsız Chrome sürücüsü (Puppeteer ya da Playwright, tam bir Chromium indirir), Whisper
  (mlx-whisper ya da openai-whisper), ffmpeg. Kurulum projede, kullanıcının bilgisiyle yapılmalı.
- Ses efekti açıksa Openverse'ten (https://api.openverse.org, anahtarsız) CC0 ses indirir ve `CREDITS.md`'ye yazar.
- Stil testinde istemi taze bir oturumda ya da alt ajanda iki üç tur çalıştırır; jeton harcar ve uzun sürer.
- Site, skili genel `~/.claude/skills/stil/` klasörüne kurmayı söyler. Kütüphanede bu yapılmaz: skill yalnız
  `python3 araclar/skill-ekle.py <proje> --skill stil` ile projeye kurulur.
- Uzun prompt'lar ve skill metninde gizli değer, anahtar ya da sistem dosyasına yazan komut yok (2026-11-15 taraması).
