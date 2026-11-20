# Yeni süreç planı: ortak çalışma dosyası

> Kullanıcıyla adım adım birlikte yazılıyor (başlangıç 2026-11-21). Taslaktır; uygulanana kadar geçerli kurallar `CLAUDE.md`, `rehber/` ve `notlar/kararlar.md` içindedir.
> Önceki plan: `notlar/plan-tur-surecleri.md` (çekirdek bitti, K-65). Dünkü Opus incelemesi özeti aşağıda "Girdi 3".

## Yol haritası
1. Amaç ve acı noktaları — **TAMAM (2026-11-21)**
2. Temizlik düzeyi: yerinde / temiz dal / sıfırdan; ne kalır, ne gider
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

## Açık soru (adım 2)
Temizlik düzeyi: yerinde devam / temiz dalda süreç katmanını baştan yaz / tüm kütüphaneyi sıfırlayıp baştan kur. Önerim: ortadaki (veri ve projeler yerinde, süreç ve belge katmanı baştan).
