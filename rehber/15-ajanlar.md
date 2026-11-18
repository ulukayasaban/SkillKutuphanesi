# 15 — Kütüphanenin kendi ajanları

Kütüphane işleri yedi ajana bölünmüştür (karar K-53, 2026-11-14). Ana oturum kullanıcıyla konuşur ve onay alır; ajanlar işi yapar ve ana oturuma rapor verir. Bu ajanlar yalnız kütüphane klasörünün içindedir; bilgisayar geneline ajan, komut ya da ayar kurulmaz.

## 1. Ajanlar
| Ajan | İşi | Model · çaba |
|---|---|---|
| `kutuphane-denetci` | Sağlık denetimi: doğrulama, kapsam, testler, git, yedekler, genel klasör bekçisi, proje sağlığı, program sürümleri. Yalnız raporlar | sonnet · medium |
| `kutuphane-kaynak` | Yeni kaynak, kendi skiller, siteden alınan skiller ve site takibi, çıkarma, kayıp kaynak, ad çakışması, güven bilgisi, adaylar, yıldız listesi | sonnet · medium |
| `kutuphane-inceleme` | Skill incelemesi: kategori, ücret, lisans, Türkçe özet, sabit yol, güvenlik | sonnet · medium |
| `kutuphane-guncelleme` | Aylık zincir, dal özeti, birleştirme sonrası liste, zamanlanmış görev metni | sonnet · medium |
| `kutuphane-program` | HyperFrames, OpenMontage, nlm, etsyotomasyon; program bağları; ortam kilitleri; genel klasörler | sonnet · medium |
| `kutuphane-proje` | Projeye öneri, ön kontrol, onaylı kurulum, proje durumu ve kaydı, rol ve profiller, araç düzenleri | sonnet · medium |
| `kutuphane-gelistirici` | Araç kodu, testler, şemalar, rehberler, istemler, kararlar, ajan dosyaları | sonnet · medium |

Yedi ajanın hepsi sonnet ile çalışır (K-60); ana oturum (takım lideri) kullanıcının o an seçtiği modelle çalışır. `inherit` yazılırsa ajan o anki oturumun modeliyle çalışır. Model ve çaba her ajanın kendi kaynak dosyasında yazılır; genel bir ayarla sabitlenmez.

## 2. Dosyalar
- **Tek kaynak:** `ajanlar/ORTAK.md` (her ajanın ortak kuralları) ve `ajanlar/kutuphane-<ad>.md` (başlık bloğu + görev tanımı). Görev tanımı kuralı kopyalamaz; ilgili rehbere ve komuta işaret eder.
- **Üretilen dosyalar** (elle düzenlenmez): `.claude/agents/kutuphane-<ad>.md` ve `.codex/agents/kutuphane-<ad>.toml`. `python3 araclar/ajan-uret.py` ikisini kaynaktan yeniden yazar.
- **Kontrol:** `python3 araclar/ajan-uret.py --kontrol` ve `python3 araclar/dogrula.py`. Kaynak hatalıysa, üretilen dosya eksikse ya da kaynakla aynı değilse, görev tanımı olmayan bir rehbere ya da araca işaret ediyorsa HATA verir. Görev tanımlarında anılan araç bayrakları da denetlenir.

## 3. Hangi araç neyi okur
| Araç | Okuduğu | Not |
|---|---|---|
| Claude Code | `.claude/agents/kutuphane-*.md` | model, çaba ve (denetçide) araç listesi başlık bloğundan |
| Codex | `.codex/agents/kutuphane-*.toml` | çaba yazılır; model yazılmaz (Codex kendi modelini kullanır); ajan başına yetki kısıtı yoktur |
| Cursor | `.claude/agents/kutuphane-*.md` | Claude dosyalarını okur |
| Antigravity, VS Code Copilot | `AGENTS.md` ve `ajanlar/*.md` | bu araçlar için ajan dosyası üretilmez; işe uyan `ajanlar/kutuphane-<ad>.md` ve `ajanlar/ORTAK.md` okunur, o rolde çalışılır |

Yeni ajan dosyaları yeni bir oturumda yüklenir; açık oturum eski listeyi görür.

## 4. Çalışma biçimi
1. Ana oturum isteği alır, `CLAUDE.md` "Ajanlar" tablosuna göre ajanı seçer ve görevi verir. Kullanıcının verdiği onay varsa görev metnine "kullanıcı şunu onayladı: ..." diye yazar.
2. Ajan onay gerektiren adımı atmaz, raporlar (`ajanlar/ORTAK.md` madde 3). Kullanıcıya soruyu ana oturum sorar.
3. Aynı anda yalnız bir ajan kütüphaneye yazar. Yalnız okuyan ajanlar (denetçi; rapor modundaki diğerleri) yan yana çalışabilir. İnceleme ajanının kopyaları farklı kategorilerde yan yana okuyabilir, kayıt dosyasına sırayla yazılır.
4. İş bitince ana oturum kontrolleri çalıştırır ya da denetçiye verir (`python3 araclar/kapsam-denetimi.py`, `python3 araclar/dogrula.py`, gerekirse `python3 araclar/test.py`), sonra kaydı kendisi atar. Ajanlar commit ve push yapmaz.
5. İşlerin kesiştiği yerler: kayıp kaynağı denetçi bulur, kaynak ajanı işaretler. Program güncellenince program ajanı raporlar, proje ajanı projelerdeki bağlara bakar. Yeni yapay zeka aracında kuralı proje ajanı yazar, kod gerekiyorsa geliştirici yapar. Güncellemeden sonra yeniden incelenecek skiller inceleme ajanına gider.

## 5. Danışman (yalnız Claude)
- Bu projede danışman modeli **Opus**'tur: `.claude/settings.local.json` → `"advisorModel": "opus"` (K-54). Dosya yereldir, git'e girmez (genel git yok sayma kuralı); başka bilgisayarda yeniden yazılır. Genel `~/.claude/settings.json` içine yazılmaz.
- Claude'da danışman ajan başına seçilemez; proje için tek değerdir. Her ajan devralır ve Claude danışmanın ajanın modelinden zayıf olmadığını kendisi denetler:

| Ajanın modeli | Danışmanı |
|---|---|
| Sonnet (denetçi, inceleme) | Opus (bir üst) |
| Oturum Sonnet ise (diğer beş ajan) | Opus |
| Oturum Opus ise | Opus (aynı düzey) |
| Oturum Fable ise | danışman devreye girmez (Fable'ın altındaki model danışman olamaz) |

- Ne zaman sorulur: `ajanlar/ORTAK.md` madde 11. Danışman önerisi kullanıcı onayı yerine geçmez.
- Değiştirmek: kullanıcı isterse yalnız bu dosyadaki değer değişir (`fable`, `opus`, `sonnet`; kapatmak için anahtarı sil). Fable bazı planlarda ayrıca kredi harcar.
- Codex, Cursor, Antigravity, VS Code Copilot için danışman yoktur.

## 6. Sınırlar
- Denetçi düzeltme yapmaz; ama çalıştırdığı denetim araçları kendi rapor dosyalarını (`notlar/` altı) yazar. Claude'da denetçiye dosya düzenleme araçları verilmez; komut çalıştırma yetkisi kalır (denetimler komuttur) ve bu yetki komut bazında kısıtlanamaz. Codex'te ajan başına kısıt yoktur. Yani denetçinin "yalnız kontrol komutu çalıştır" sınırı talimata dayanır.
- Onay kuralları ajanlarla değişmez: `CLAUDE.md` kesin kurallar, K-49 (kayıp kaynak), K-50 (projelerde onaysız işlem yok).

## 7. Ajan eklemek ya da değiştirmek
1. `ajanlar/kutuphane-<ad>.md` dosyasını yaz ya da düzenle. Başlık bloğu: `name` (dosya adıyla aynı), `description` (tek satır; ne zaman kullanılacağını söyler), `model`, `effort`, isteğe bağlı `tools`.
2. Kapsam başka bir ajanla çakışmasın; çakışıyorsa hangisinin sahibi olduğunu iki dosyada da yaz. Yeni ajan açmadan önce işin mevcut bir ajanın alanına girip girmediğine bak.
3. `python3 araclar/ajan-uret.py`, sonra `python3 araclar/ajan-uret.py --kontrol`, `python3 araclar/dogrula.py` ve `python3 araclar/test.py` (`araclar/testler/test_p12-ajanlar.py` her ajanın bu rehberde ve `CLAUDE.md` tablosunda anıldığını denetler).
4. Bu dosyadaki tabloyu ve `CLAUDE.md` "Ajanlar" tablosunu güncelle (`cp CLAUDE.md AGENTS.md`).
5. Bir ajanı kaldırmak: kaynak dosyasını sil, `python3 araclar/ajan-uret.py` üretilmiş dosyalarını da siler.
