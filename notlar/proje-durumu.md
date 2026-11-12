# Proje durumu — kayıtlı projelerin sağlığı

> `araclar/proje-kullanimi.py --saglik` üretir; elle düzenleme. Salt okuma: hiçbir projeye ve genel skill klasörüne yazılmaz.
> Tarih yoktur: içerik yalnız durum değişince değişir. Ayrıntı: `rehber/10-proje-kullanimi.md`.

**Genel durum: dikkat**

## Projeler
| Proje | Durum | Skill (kilit/klasör) | Güncelleme var | Elle değişmiş | Kaynak yok | Kayıtsız | Kendi/elle | Araçlar | Son işlem |
|---|---|---|---|---|---|---|---|---|---|
| Akil Disi Youtube Kanali | temiz | 18/35 | 0 | 0 | 0 | 0 | 8 | claude, codex | 2026-11-12 |
| Etsy-Arif | temiz | 27/37 | 0 | 0 | 0 | 0 | 10 | claude | 2026-11-12 |
| Etsy-Yeni | dikkat | 31/31 | 0 | 0 | 0 | 0 | 0 | claude, codex (kilitte yok: varsayılan) | 2026-11-05 |
| IstatistikYoutube | temiz | 26/50 | 0 | 0 | 0 | 0 | 22 | claude | 2026-11-12 |

## Programla gelen ve donmuş skiller
> Yukarıdaki 'Skill (kilit/klasör)' klasör sayısı bağları ve donmuşları da içerir.

| Proje | Bağ | Donmuş | Kırık bağ |
|---|---|---|---|
| Akil Disi Youtube Kanali | 9 | 0 | 0 |
| IstatistikYoutube | 2 | 0 | 0 |

## Ayrıntı
### Etsy-Yeni — dikkat
- [dikkat] EMEKLİ: etsy-api (kaynak kayıp; artık güncellenmez)
- [bilgi] araç seçimi kilitte yok (varsayılan: claude, codex)

## Kayıp, taşınmış ya da hafızada olmayan
Yok.

## Takipte olmayanlar
- AntigravityTest2: takipten çıktı 2026-11-12 — Kullanıcı kararı 2026-11-12: kullanılmıyor, Çöp Kutusu'na taşındı

## Kayıtsız proje klasörleri
Tarama: `~/Documents` (derinlik 4, bağlantılar izlenmedi).
| Klasör | Sınıf | Skill | Araçlar | Not |
|---|---|---|---|---|
| `~/Documents/Claude/deneme/openmontage-fecb9a1e` | skilli | 93 | agents/codex, claude, copilot, cursor |  |
| `~/Documents/Claude/yedek/akil-disi-tam-2026-11-12/proje` | skilli | 11 | agents/codex, claude | kilit var ama izleme kapsamı dışı: --ekle |
| `~/Documents/Claude/yedek/istatistik-skill-gecisi-2026-11-12` | skilli | 45 | claude | kilit var ama izleme kapsamı dışı: --ekle |
| `~/Documents/Codex/2026-10-01/task/ECommerceProject` | skilli | 7 | agents/codex, claude |  |
| `~/Documents/IsBasvuruClaude` | skilli | 20 | agents/codex, claude |  |
| `~/Documents/IstatistikYoutube-Arsiv/status-arsiv/claudesidian-kaldirma-2026-10-18/vault-kit` | skilli | 20 | agents/codex, claude |  |
| `~/Documents/IstatistikYoutube-Arsiv/status-arsiv/vault-tam-yedek-20261018-1124` | skilli | 12 | agents/codex, claude |  |
| `~/Documents/IstatistikYoutube-Arsiv/status-arsiv/vault-tam-yedek-20261018-1242` | skilli | 20 | agents/codex, claude |  |
| `~/Documents/NewTetraTarim/ECommerceProject` | skilli | 8 | agents/codex |  |
| `~/Documents/NewTetraTarim/ECommerceProject-Archives/20261019T115632Z-codex-native/restore-probe` | skilli | 7 | agents/codex, claude |  |
| `~/Documents/NewTetraTarim/ECommerceProject-Archives/20261019T115632Z-codex-native/retired` | skilli | 1 | agents/codex, claude |  |
| `~/Documents/NewTetraTarim/ECommerceProject-Archives/20261019T115632Z-codex-native/snapshot` | skilli | 7 | agents/codex, claude |  |
| `~/Documents/Tekfen Araştırma Sonuçları` | skilli | 346 | claude |  |
| `~/Documents/Yetisio` | skilli | 6 | claude |  |
Yalnız talimat dosyası olan klasör sayısı: 15 (işlem gerekmez).

### Yoksayılanlar
| Yol | Neden | Tarih |
|---|---|---|
| `~/Documents/Istatistik template/Arkadasa-Gonderilecek/KIT` | Kullanıcı kararı: başkasına gönderilecek dağıtım paketi, önemli değil, işlem yapılmaz. | 2026-11-11 |
| `~/Documents/Psikolojik Danışman Sosyal Medya` | Kullanıcı kararı: güncel kullanılmıyor, işlem yapılmaz. | 2026-11-11 |

## Karar bekleyenler
- Kayıtsız proje: ~/Documents/Claude/deneme/openmontage-fecb9a1e (93 skill) -> --ekle ya da --yoksay
- Kayıtsız proje: ~/Documents/Claude/yedek/akil-disi-tam-2026-11-12/proje (11 skill) -> --ekle ya da --yoksay
- Kayıtsız proje: ~/Documents/Claude/yedek/istatistik-skill-gecisi-2026-11-12 (45 skill) -> --ekle ya da --yoksay
- Kayıtsız proje: ~/Documents/Codex/2026-10-01/task/ECommerceProject (7 skill) -> --ekle ya da --yoksay
- Kayıtsız proje: ~/Documents/IsBasvuruClaude (20 skill) -> --ekle ya da --yoksay
- Kayıtsız proje: ~/Documents/IstatistikYoutube-Arsiv/status-arsiv/claudesidian-kaldirma-2026-10-18/vault-kit (20 skill) -> --ekle ya da --yoksay
- Kayıtsız proje: ~/Documents/IstatistikYoutube-Arsiv/status-arsiv/vault-tam-yedek-20261018-1124 (12 skill) -> --ekle ya da --yoksay
- Kayıtsız proje: ~/Documents/IstatistikYoutube-Arsiv/status-arsiv/vault-tam-yedek-20261018-1242 (20 skill) -> --ekle ya da --yoksay
- …ve 6 kayıtsız klasör daha (--tara-kayitsiz)

## Ayar uyarıları
Yok.
