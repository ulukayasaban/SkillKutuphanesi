# DURUM (her oturum önce bunu okur)

Son güncelleme: 2026-11-11

Bu klasördeki **tek geçerli not** budur. Eski planların ikisi de `rafta/` içinde; hiçbiri uygulanmaz.

## Hedef
Bilgisayarın genelindeki skill klasörleri boşaltılacak; skiller yalnız bu kütüphaneden, yalnız proje klasörüne kurulacak.
HyperFrames ve OpenMontage **programları** yerinde kalır; taşınan sadece skillerdir. Her kaldırmadan önce yedek alınır.

## İki kapı (kullanıcı söylemeden açılmaz)
| Kapı | Açan söz | O zamana kadar |
|---|---|---|
| HyperFrames, OpenMontage, genel skill klasörleri, ayar dosyaları | "işim bitti" | Sadece okunur |
| Proje klasörleri (tarama, düzenleme, Akıl Dışı'nın Claude'a geçişi) | "başla" | Girilmez, okunmaz |

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

## Adım çizelgesi
| Adım | İş | Kapı | Durum |
|---|---|---|---|
| 1 | Kütüphane içi hazırlık: skillerdeki sabit genel yol / eklenti kökü / kardeş yol taraması, kurulumda yol çevirisi, yeni ön kontrol kodları, aylık zincire yol ve program denetimi | yok (onaylı) | sürüyor: tarama tarafı bitti, kurulum tarafı kaldı (`1-adim-kalan-is.md`) |
| 2 | HyperFrames ve OpenMontage program kartları; güncelleme (önce yedek, her biri ayrı onay) | "işim bitti" | bekliyor |
| 3 | Genel klasörleri boşaltma (yedek, her kaldırma ayrı onay); aynı gün yedek silme hatırlatması | "işim bitti" | bekliyor |
| 4 | Proje taramaları, projelerde `--guncelle --kuru` önizlemesi, Akıl Dışı'nın Claude'a geçişi | "başla" | bekliyor |

## Ölçülen durum (2026-11-10, sadece okuma)
- `~/.claude/skills`: 105 girdi (81 bağlantı + 24 gerçek klasör). `~/.agents/skills`: 27 skill. `~/.codex/skills`: 11 bağlantı.
- Kurulu HyperFrames 0.9.23. OpenMontage `~/.openmontage` main dalında.

## Sonraya kalan düzeltmeler
- 3. adımın günü düzeltilecek belge satırları (bugün hâlâ doğru): `README.md` 6-7, `rehber/01-skill-ekleme-sureci.md` 12
  ("eski agent'lar genel klasörlerdeki skillerle çalışmaya devam eder").
- 2. adımda düzeltilecek: `rehber/02-guncelleme-yonergesi.md` "4) Global skiller" (güncellemeyi kuran araç değil, kütüphane oturumu yapar).
- Eklenti kökünden dosya çekme (`ek_dosyalar`) bu turda yok; lisans ve ücret onayı gerekir.

## Açık notlar
- Kütüphane `master` dalı GitHub'a gönderilmedi; kullanıcı isteyince `git push origin master`.
- İş bitince bu klasör arşivlenir (içinde proje adı geçiyor).
