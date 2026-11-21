# İstenen süreç ↔ bugünkü kütüphane (2026-11-21)

> Kaynak: `notlar/onceki-planlar/istenen-surec.md`. Ölçüt: **hazır** (istenen gibi çalışıyor) / **yarım** (var ama eksik ya da elle) / **yok**. Kanıt: araç bayrakları, `kilit.json`, `surecler/`, zamanlanmış görev metni, `registry.json`/`kaynaklar.json` sayımları (bu oturumda okundu). Sınanmayan yerler "doğrulanmadı" diye işaretli.

## Görevler
| # | İstek | Durum | Bugün ne var / ne eksik |
|---|---|---|---|
| 1 | İzleme: yeni, değişen, kaybolan repo | **yarım** | `github-skill-listesi.py`, `github-trend.py`, `populer-tarama.py`, `konu-takip.py`, `arsiv-guncelle.py --aylik`, `KAYIP` işareti var. Eksik: aylık zincir **fihristi ve kiti taramıyor**, `son-aylik-calisma.json` damgası yok, listeye eklenen repoyu kendiliğinden yakalayan süreç yok (yeni repo kullanıcı isteğiyle işleniyor). |
| 2 | Sınıflama: tür, kategori, ücret, risk, boyut | **yarım** | `tur-belirle.py`, `boyut-hesapla.py`, kategori/ücret kuralları var, 200/200 kayıtta tür. Eksik: iki sınıflandırma yan yana (`tip` ve `tur`), skil kayıtlarında 138 senkron bozukluk; 6 kayıtta `tur_gerekce` boş; ücret ve kategori kararı hâlâ LLM incelemesiyle, kurallarla değil. |
| 3 | Kayıt: eski sürüm saklanır, gereksiz kopya taşınmaz | **yarım** | Eski sürüm git geçmişinde, `kilit.json` commit sabitliyor, `yedekler.json`, `medya_haric` var. Eksik: kullanılmayan 164 kaynak hâlâ arşivde tam duruyor (karar bekliyor); skill başına "inceleme hangi commit için" bilgisi yok. |
| 4 | Öneri: yeni repo öneriye adapte olur, yeni proje için rapor | **yarım** | `--oner`, `--rapor`, 23 profil, 31 rol, kit, fihrist kurulumu var. Eksik: yeni repo profil/rollere kendiliğinden girmiyor (rol ve profil elle); yeni repoda öneriyi bozmama garantisi yazılı değil (doğrulanmadı). |
| 5 | Kurulum: seçilen skill projeye | **hazır** | `skill-ekle.py` (ön kontrol, `--evet`, `--dogrula`, yedek, `--geri-al`, `--kaldir`, `--arac`), kilitli, proje klasörüne, genel klasörlere yazmaz. |
| 6 | Proje takibi: skill, sürüm, güncel mi, dondurulmuş mu | **yarım** | `kilit.json` (repo, commit, klasör hash'i, kurulu hash), `proje-kullanimi.py --saglik`, `--durum`. Eksik: **proje başına sürüm modu yok** (takip / dondur / yalnız onaylı); `--dondur` farklı anlam (kaynağı kaybolan skili projenin kendi skili yapar); "son işlem" alanı yok; program sürümü eski kalıyor, `--durum` "güncel" diyor. |
| 7 | Güncelleme: aylık, proje başına etki raporu | **yarım** | `arsiv-guncelle.py --aylik`, dal + özet, "bu kaynaklardan skill kullanan projeler", `--guncelle --kuru`, `--birlestir`. Eksik: fihrist/kit yok, etki raporu "hangi dosya değişiyor / elle değişiklik var mı" düzeyinde değil, toplu öneri yok. |
| 8 | Koruma: riskli red, yedek, geri alma | **yarım** | K-58 + `surecler/tur-riskli.md`, `yedek-denetim.py`, `--geri-al`, `rehber/13`. Eksik: riskli reddi otomatik değil ("ana oturum kullanıcıya bildirir"); kullanıcıya soru gidiyor. |
| 9 | Raporlama: durum ve maliyet | **yarım** | Durum: `aylik-ozet.py`, `proje-durumu.md`, `git-durum.py`. **Maliyet raporu yok**: araçlar token, kota, süre, disk, onay sayısı ölçmüyor (yalnız `neon-izle.py` agy toplamı, kota dosyası). |
| 10 | Hafıza ve kontrol: tek yer, çift kayıt yok, açılış yükü az | **yarım** | `BASLA.md`, `status/`, `kararlar.md` var. Eksik: aynı kural hem hafızada hem belgede (8/8 çift); açılışta ≈23 KB (`CLAUDE.md` 16,5 + ev 3 + `MEMORY.md` 3,5) + `BASLA.md` 9,5; `surecler/`'de 8 dosyada eski "HENÜZ YOK"; senaryo dosyası yok. |

## Kurallar
| İstek | Durum | Not |
|---|---|---|
| Süreç kendini sürdürür, yeni repo ve aylık kontrolde kullanıcıya bağımlı olmaz | **yok / ters** | Aylık görev master'a dokunmaz, yeni kaynak eklemez, "adaylar onaysız eklenmez" (CLAUDE.md, zamanlanmış görev metni). Yani bugünkü kural istenenin tersi: yeni repo her seferinde onay ister. |
| Skill'ler projede, genel klasörler boş | **hazır** | 2026-11-12 boşaltma, `genel-bekci` (gürültülü: `.trash` alarmı). |
| Kayıpsız, eski sürüm silinmez, geri dönülür | **hazır** | Git geçmişi, `yedekler.json`, `--geri-al`. |
| Riskli ve saldırgan skill alınmaz, otomatik, soru yok | **yarım** | Kural var, soru da var (bkz. görev 8). |
| Tam ücretli skill de "ücretli" etiketiyle önerilir | **yarım** | `ucret` sınıfı, kurulum raporunda ÜCRETLİ uyarısı, `ucretli-skiller.md`; ücretli skill rol çekirdeğine ancak gerekçeyle girer. İstenen "önerilir, ilerleyiş kullanıcıya kalır" ile uyumu doğrulanmadı. |
| Claude Code, Codex, Antigravity tam uyum; diğerleri ek çabasız | **yarım** | `--arac ortak/yalniz-claude`, `yapay-zeka-araclari.json`, `--araclar` kontrolü var; Codex ve Antigravity için ayrı kurulum sınaması yazılı değil (doğrulanmadı). Windows (Etsy-Arif) planda 6. adımda yapılmadı. |
| Tek giriş, aynı bilgi tek yerde | **yarım** | `BASLA.md` giriş; çift kayıt var (görev 10). |
| Kısa oturum, plan dosyası tek hafıza | **hazır** (uygulanıyor) | `CHECKPOINT`, plan dosyası. |
| Programlar yedekli güncellenir (isteğe bağlı) | **hazır** | `rehber/11`, `program-denetim.py --oncesi`, HF/OM bu oturumda güncellendi. |

## Onay kuralları
| İstek | Durum | Not |
|---|---|---|
| Onaysız: yeni repo adaptasyonu, kategori, öneri, aylık tarama, raporlar, 404 işaretleme | **yarım** | Aylık tarama, rapor, kayıp işaretleme (K-49) onaysız. Yeni repo adaptasyonu onaylı (yukarıya bak). |
| Toplu onay (aynı skill + aynı sürüm, birden çok proje) | **yok** | Her proje ayrı `--evet`; toplu öneri üreten araç yok. |
| Tek tek onay (proje etkileyen her işlem) | **hazır** | K-50: projelerde açık onaysız işlem yok. |
| Her zaman kullanıcıya: para, kalıcı silme, güvenlik riski, GitHub'a gönderme | **hazır** | CLAUDE.md kesin kurallar. |

## Senaryolar (13)
| Senaryo | Durum |
|---|---|
| Listene yeni repo → hiçbir şey sorulmaz | **yok** (onay istiyor, `surecler/yeni-repo.md` tek mesajla soruyor) |
| Riskli repo → otomatik red | **yarım** |
| Yeni proje → öneri raporu ve kurulum onayı | **hazır** |
| Aylık kontrol → yalnız projeyi etkileyenler | **yarım** (fihrist/kit yok; sade proje filtresi yok, tüm özet geliyor) |
| Aynı skill yeni sürümü 3 projede → tek toplu onay | **yok** |
| Dondurulmuş proje raporda görünmez | **yok** (mod yok; `yoksay` listesi projeyi tümden izlemeden çıkarıyor, ayrı iş) |
| Güncelleme projeyi aksatabilir → etki raporu, geri dönüş, kısa bildirim | **yarım** (geri alma var; otomatik geri dönüş ve etki düzeyi yok) |
| Kaynak 404 → kullanılıyorsa projeye dokunmaz, uyarı | **yarım** (kullanılmıyorsa sormadan KAYIP; kullanılıyorsa önce sorulur, "kullanılıyorsa uyarı" tek başına otomatik değil) |
| Tam ücretli skill → etiketli öneri | **yarım** |
| Başka YZ aracı aynı skill'leri görür | **yarım** (düzen var, sınama yok) |
| Ağ yok / hata → durur, projeye dokunmaz, devam noktası kaydeder | **yarım** (aylık zincir durup raporluyor, "kismi/basarisiz"; devam noktası damgası yok) |
| Aylık maliyet raporu | **yok** |
| Program yeni sürüm → yedekli güncelleme önerisi | **hazır** |

## Özet sayım
- Görev: 1 hazır, 9 yarım. Kural/onay/senaryo: çoğu yarım; **yok** olanlar dört: yeni repoda onaysız yürüme, toplu onay, proje sürüm modu (dondur/takip/yalnız onaylı), maliyet raporu.
- İstenenle bugünkü arasındaki en büyük fark **yön**: bugün sistem her yeni şeyde kullanıcıya soruyor (CLAUDE.md, zamanlanmış görev, `yeni-repo.md`); istenen, sorunun yalnız kırmızı çizgilerde gelmesi.

## Plan adımlarına karşılık
- 4 (giriş süreçleri): yeni repo uçtan uca onaysız; riskli otomatik red; aylık zincire fihrist ve kit.
- 5 (projelerdeki skiller): sürüm modu, toplu öneri, etki raporu, kaybolan kaynak uyarısı, program sürümü gerçek takibi.
- 6 (onay merdiveni): yukarıdaki onay tablosu.
- 7 (maliyet): ölçüm araçları ve aylık rapor.
- 3'ün veri düzeni, hafıza (görev 10) ve belge temizliği ayrı iş paketi.
- **Vade 2026-12-07 öncesi asgari:** aylık zincirin fihrist/kit adımı ve damga dosyası.
