# openmontage — sürüm ve yer kaydı (kaynak kopyası YOK)

| Alan | Değer |
|---|---|
| Repo | https://github.com/OpenMontageInc/OpenMontage (eski ad: calesthio/OpenMontage; GitHub aynı repoya yönlendirir) |
| Kayıtlı commit | `fecb9a1e3cc23ef84de30b272059457a427f16f8` (dal `main`; 2026-11-12'de `c8066452` sürümünden güncellendi) |
| Lisans | AGPL-3.0 |
| Kayıt tarihi | 2026-11-12 |
| Kurulu yer | `~/.openmontage` (git klonu; `.venv` ve `remotion-composer/node_modules` ile birlikte yaklaşık 4,6 GB) |
| Anahtarlar | `~/.config/openmontage/.env` (açılmaz, yazdırılmaz) |
| Yedek klasörü | `~/Documents/Claude/yedek/openmontage-<YYYY-AA-GG>/` (güncellemeden önce; içinde `KAYIT.json`) |
| Giriş yolu | `programlar.json` → `openmontage` → `giris_yolu` |
| Doğrulama | commit `fecb9a1e3cc23ef84de30b272059457a427f16f8` (tam sha; dal adıyla onay verilmez) |
| Yerel yama kaydı | `programlar.json` → `openmontage` → `yerel_yamalar.bilinen` |

Kaynak kopyası alınmadı: klon çok büyük, kendi git geçmişi var ve yerel yamalar içerir. Kütüphane kopyası olsaydı
yamalı çalışma ağacı ile karışırdı.
Yeniden edinmek için: `git clone https://github.com/OpenMontageInc/OpenMontage` ve kayıtlı commit'e geçmek (yalnız kütüphane
oturumu, kullanıcı onayıyla; ayrıntı: kart `kurulum`). Yerel değişiklikler klonda durur, repoda yoktur (2026-11-12 ölçümü: 7 değişen izlenen dosya, 5 izlenmeyen yol; listeyi `git status` verir, güncellemede yeniden sayılır; skill notundaki 'beş yama' sayısı ve basicsr yaması ölçümle doğrulanmadı): güncellemeden önce yedeği şarttır.
Yerel klonun `origin` adresi 2026-11-12'de yeni ada çevrildi (kullanıcı onayıyla). Önceki sürüme dönüş: yedek `~/Documents/Claude/yedek/openmontage-2026-11-12/` (`KAYIT.json`, `yerel-yamalar.patch`).
Kart ve güncelleme adımları: `programlar.json` → `openmontage`, rehber: `rehber/11-program-yonetimi.md`.
