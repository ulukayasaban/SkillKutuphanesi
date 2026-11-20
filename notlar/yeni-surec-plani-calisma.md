# Yeni süreç planı: ortak çalışma dosyası

> Kullanıcıyla adım adım birlikte yazılıyor (başlangıç 2026-11-21). Taslaktır; uygulanana kadar geçerli kurallar `CLAUDE.md`, `rehber/` ve `notlar/kararlar.md` içindedir.
> Önceki plan: `notlar/plan-tur-surecleri.md` (çekirdek bitti, K-65). Dünkü Opus incelemesi özeti aşağıda "Girdi 3".

## Yol haritası
1. Amaç ve acı noktaları — **TAMAM (2026-11-21)**
2. Temizlik düzeyi — **TAMAM (2026-11-21): ortadaki yol seçildi**
3. Veri düzeni: kaynak, skill, kit, program, proje kayıtları
4. Giriş süreçleri: yeni repo/skill (tür bazlı)
5. Projelerdeki skiller: kurulum, güncelleme, izleme
6. Kalite, güvenlik, ücret ve onay kuralları (kullanıcıya bağımlılık merdiveni)
7. Araçlar, ajanlar, kota ve maliyet
8. Geçiş planı ve kabul senaryoları

## Adım 1 sonucu: hedefler ve şartlar
Kullanıcı dört hedefin hepsini seçti: **sadelik, güvenilirlik, hız ve az onay, projelerdeki skiller**. Üç ek şart koydu; bunlar bütün adımları kesen kurallardır:

- **K1 Hafıza:** Süreçler tasarlanırken kullanıcının bilgisayarındaki hafıza işlemleri de değerlendirmeye girer (neyin nerede tutulduğu, çakışma, token yükü).
- **K2 Maliyet:** Kütüphane süreçleri ilerledikçe her sürecin maliyeti (token, kota, süre, disk, onay sayısı) hesaplanır; her şey net görünür.
- **K3 Bağımsızlık:** Bundan sonra eklenen repolarda süreçler kullanıcıya bağımlı olmaz: iş uçtan uca yürür, kullanıcıya yalnız kırmızı çizgi kararları gelir.

## Girdi 1: kütüphanenin bugünkü durumu (2026-11-21, sayılan)
- 2.849 skill (40 kategori; 2.454 ücretsiz, 355 kısmen, 40 ücretli), hepsi incelenmiş. 200 kaynak kaydı (tür: koleksiyon 63, referans 53, tek-skil 39, urun-skil 27, dev-koleksiyon 7, repo-ici 6, program 2, kit 1, kendi 1, site 1; 2 KAYIP). Arşiv 283 MB, fihrist 3,4 MB, `.git` 221 MB.
- 4 proje: Akil Disi Youtube Kanali (19 skill + 9 bağ), Etsy-Arif (27), Etsy-Yeni (31), IstatistikYoutube (25 + 3 bağ); toplam 102 skill, 12 program bağı. 5 program kartı.
- 37 araç (`skill-ekle.py` 4.621 satır), 15 rehber, 18 hazır istem, 12 tür süreci dosyası, 7 ajan, 324 test.
- Doğrulanan zayıflıklar: aylık zincirde "fihrist" yok; `surecler/` içinde 21 "HENÜZ YOK"; senaryo dosyası yok; aynı bilgi birçok belgede tekrar; maliyet ölçümü yok (yalnız `~/.cache/kotalar/usage.json` kota verisi ve K-62 danışman notu).

## Girdi 2: hafıza haritası (bilgisayarda bulunan, kullanıcının makinesi)
| Yer | Ne | Boyut / durum |
|---|---|---|
| Claude otomatik hafıza `~/.claude/projects/<proje>/memory/` | Geri çağrılan kararlar, tercihler | 12+ proje klasörü; bu kütüphane 20 dosya (92 KB), Akil Disi 16, Etsy-Arif 9 |
| claude-mem (`~/.claude-mem`) | Oturum gözlemleri, arama | 1,1 GB veritabanı; Ekim'den kalma `CAPTURE_BROKEN` bayrağı var ama veritabanı bugün de yazılıyor (bayrak eski görünüyor) |
| `CLAUDE.md` dosyaları | Her oturumda yüklenen kurallar | IstatistikYoutube 77 KB, Etsy-Arif 28 KB, kütüphane 16,5 KB, Akil Disi 16 KB, ev 3 KB (hepsi her oturumda token yer) |
| `status/` (kütüphane) | CHECKPOINT, DEVIR, HATALAR | 3 dosya, küçük |
| Proje ajan hafızası | `.claude/agent-memory` | IstatistikYoutube 11, Psikolojik Danışman 6 dosya |
| Antigravity / Gemini | `~/.gemini` (GEMINI.md, antigravity) | 679 MB |
| Codex | `~/.codex/memories` | var |
| Zamanlanmış görevler | `~/.claude/scheduled-tasks` | 6 görev (aylık güncelleme dahil) |

Henüz yapılmadı: bu hafızaların içeriklerini çakışma açısından okuma (adım 3 ve 7'de yapılacak).

## Girdi 3: dünkü Opus incelemesi (özet)
Öneri: yerinde devam; yalnız süreç katmanı temiz bir dalda baştan yazılsın. Kanıtlı bulgular: aylık zincir fihristi bilmiyor, `surecler/` eskimiş, senaryo dosyası yok, `.gecici/` 52 MB kalıntı, 6 kaydın `tur_gerekce`si boş, ComposioHQ gerekçesi eski, K-60..K-66 yanlış bölümde. Opus haftalık kotası yüzünden (133 saat) devam edemedi.


## Adım 2: geçmiş planların ve bugünkü süreçlerin doğrulanması (2026-11-21, kanıtlı)

### Geçmiş planlar ne durumda
| Plan | Durum | Kanıt |
|---|---|---|
| Eski `notlar/rafta/PLAN.md` (451 satır) ve yerel yapılacaklar | Rafta, kullanılmıyor | `notlar/rafta/OKU.md` |
| HF/OM geçişi (`notlar/hf-om-gecisi/`) | Tamamlandı (genel klasörler 2026-11-12'de boşaltıldı; bugün HF 0.9.71 / OM 2e003e65) | `DURUM.md`, K-40..K-66, `genel-bekci` TEMİZ |
| Düzen denetimi (A1–A7, B1–B9, paketler P1–P8) | Uygulandı ve testli | 324/324 test (p1..p19), `BASLA.md`, `genel-bekci.py`, `aylik-ozet.py`, `rehber/12`, `kaynak-cikar.py` vb. var. **C (isteğe bağlı, 5 grup) tek tek doğrulanmadı** |
| Tür planı (`plan-tur-surecleri.md`) | Adım 1–4 uygulandı; **5 (aylık zincir) ve 6 (Windows) yapılmadı** | plan §17, 200/200 kayıtta tür |

### Doğrulanan eksikler (önem sırasıyla)
1. **Aylık zincir fihristi ve kiti bilmiyor.** `arsiv-guncelle.py`/`aylik-ozet.py` içinde "fihrist" 0 kez geçiyor; `--aylik --kuru` 70 kaynakta güncelleme dalı planlıyor, fihristteki 6 dev koleksiyon ve kit çıktıda yok. İlk gerçek aylık vade 2026-12-07.
2. **Aylık damga dosyası yok** (`notlar/son-aylik-calisma.json`, yerel/gitignore): zincir "ilk kurulum ya da yeni makine" sanıyor.
3. **Belgeler eski:** `surecler/` içinde 21 "HENÜZ YOK": 12'si artık uygulanmış adım 4'e ait (belge eskimiş), 7'si gerçekten yapılmamış adım 5'e ait, 2 başka. Plan §13.5'in öngördüğü senaryo dosyası yok.
4. **Bazı araçlar `--help`'e cevap vermiyor, doğrudan çalışıyor:** `arsiv-yerlestir.py`, `duman-testi.py`, `gelistirici-bilgisi.py`, `kapsam-denetimi.py` (zaman aşımı), `listeye-ekle.py` ("geçersiz repo adı: --help"). Yanlışlıkla çalıştırma riski.
5. **Testsiz araç:** `ceviri-tr.py`, `neon-izle.py`.
6. **Proje bağlarında kayıtlı sürüm eski:** `skill-ekle --durum` "güncel" diyor ama "bağlandığında 0.9.35 / fecb9a1e / 0.15.8, kart şimdi 0.9.71 / 2e003e65 / 0.16.5". Hangi proje hangi program sürümünü gerçekte kullanıyor, ölçülmüyor.
7. **Bekçi gürültüsü:** `~/.claude/skills/.trash` (uygulamanın çöp klasörü) dosya sayısı değiştikçe (14 → 15 → 1) alarm veriyor.
8. **Bekleyen girdiler:** 4 yıldızlı repo kütüphanede yok (`echris6/motion-video-kit`, `howseen-ai/claude-motion-design`, `tugrawork-creator/saas-motion-kit`, `storytold/pdfcraft`); 10 trend/popüler aday kararı.
9. **Kayıt temizliği (Opus bulgusu, kısmen doğrulandı):** `kararlar.md`'de K-60..K-66 "Kabul edilen bekleyenler" başlığı altında (aylık özet bu bölümü susturma listesi okuyor); 6 kayıtta `tur_gerekce` yok; ComposioHQ dev-koleksiyon gerekçesi eski; `.gecici/` 52 MB kalıntı.

### Hafıza (K1) ölçümü
- Açılışta her oturumda yüklenen: `CLAUDE.md` 16,5 KB + ev `CLAUDE.md` 3 KB + `MEMORY.md` 3,5 KB ≈ 23 KB; oturum başı okunan `BASLA.md` 9,5 KB + `CHECKPOINT.md` 4 KB. Bayt/3 ile kabaca ≈ 12 bin token (tahmin), üstüne claude-mem enjeksiyonu (bu oturumda ≈ 10 bin "okunan" token gözlendi).
- Hafıza dosyaları (20 dosya, 50 KB): kontrol edilen 8 kuralın 8'i hem hafızada hem repo belgelerinde yazılı (GitHub yalnız kütüphane, kayıp kaynak, konu konu, Neon düzeni, projelerde onaysız işlem yok, plan adımları sormadan, kaynak değerlendirme, yedek silme). Çift kayıt = biri eskirse çelişir.
- İçerik çakışması taraması (hafızaların birbiriyle çelişmesi) henüz tam yapılmadı.

### Maliyet (K2) ölçümü
- Araçlar token/maliyet ölçmüyor; yalnız `neon-izle.py` agy toplam token yazıyor, kota için `~/.cache/kotalar/usage.json` var. Gerçek örnek: Opus high iki koşu ≈ 330 bin token ≈ haftalık Claude/GPT havuzunun ≈ %38'i.
- Kullanılabilir veri kaynakları: Claude oturum kayıtları (46 dosya, 1,1 GB; `claude-mem:agent-cost-report` becerisi), agy `result` olayı, kota dosyası.

### Karar için sonuç
Süreç katmanının çekirdeği (araçlar, kayıtlar, testler, bağlar) çalışıyor; sorunlar belge eskimesi, aylık zincirin eksik adımı, ölçüm eksikliği ve çift hafıza. Tam sıfırlama bu sorunların hiçbirini çözmek için gerekli değil; 4 projenin kilit bağlarını ve 2.849 inceleme kaydını riske atar. Öneri: **veri ve araçlar yerinde, süreç/belge/hafıza katmanı baştan yazılır** (planda "ortadaki yol"). Karar kullanıcıda.

## Girdi 4: token ölçümü (2026-11-21, Claude oturum kayıtlarından sayıldı; faturalama değil, plan limitinin nasıl saydığı bilinmiyor)
Son 7 gün, yeni girdi (girdi + önbellek yazma) + çıktı, milyon token:
| Proje | Yeni girdi + çıktı | Pay |
|---|---|---|
| Akil Disi Youtube Kanali | 181 | %34 |
| IstatistikYoutube | 172 | %32 |
| claude-mem gözlemci oturumları (arka plan, çoğu Haiku) | 81 | %15 |
| **SkillKutuphanesi** | **74** | **%14** |
| diğerleri (Claude uygulaması, Etsy-Arif, ...) | 30 | %5 |
Toplam ≈ 538 M.

Kütüphane projesi 2026-10-21'den bugüne (22 etkin gün, 716 kayıt dosyası, 50.748 model turu): 460 M yeni girdi, 65 M çıktı, 14,6 G önbellek okuma. En ağır günler: 10 Kasım (82 M), 21 Ekim (69 M), 31 Ekim (58 M), 11 Kasım (49 M). Model dağılımı (çıktı): Opus 5.5 25 M, Sonnet 5.5 24 M, Fable 5.2 10 M, Fable 5.1 4 M.
**Ortalama bağlam ≈ 288 bin token/tur**: konuşma uzadıkça her mesajda tüm geçmiş yeniden okunuyor; yapısal maliyet budur.
Kullanım: Claude haftalık ≈ %74 (beklenen %45), Fable haftalık %64, Antigravity Claude/GPT haftalık ≈ %88 (kullanım dosyası 2026-11-20/21).

## Karar (adım 2, kullanıcı 2026-11-21): ORTADAKİ YOL
- **Yerinde kalır:** 2.849 incelenmiş skill (`registry.json`), `kaynaklar.json`, `arsiv/`, `fihrist/`, `kitler.json`, `programlar.json`, `projeler.json`, araçlar ve 324 test, 4 projenin `kilit.json` bağları, git geçmişi, `yedekler.json`.
- **Baştan, sade yazılır:** `CLAUDE.md`/`AGENTS.md`, `BASLA.md`, rehberler, hazır istemler, `surecler/` dosyaları, hafıza düzeni (neyin nerede tutulacağı), maliyet kaydı.
- **Plana iş olarak girer:** yukarıdaki 9 doğrulanmış eksik.
- Tam sıfırlama yapılmaz (4 projenin bağlarını ve inceleme kayıtlarını riske atar, eksiklerin hiçbirini çözmek için gerekli değil).

## Açık soru (adım 3)
Veri düzeni: kaynak, skill, kit, program ve proje kayıtlarının hangisi tek doğru kaynak olacak, hangileri üretilmiş görünüm olacak?
