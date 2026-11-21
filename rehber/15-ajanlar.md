# 15 — Kütüphanenin kendi ajanları

Kütüphane işleri 4 role bölünmüştür (`notlar/yeni-surec-plani.md` bölüm 8): **ana oturum** kullanıcıyla konuşur, onay alır, `konu-takip.json` kuyruğunu sunar, git commit ve `olcum.jsonl` kapanışını yapar; 3 alt-ajan (`kutuphane-kaynak`, `kutuphane-inceleme`, `kutuphane-denetci`) işi yürütür ve ana oturuma rapor verir. Bu ajanlar yalnız kütüphane klasörünün içindedir; bilgisayar geneline ajan, komut ya da ayar kurulmaz.

## 1. Roller ve Ajanlar
| Rol / Ajan | İşi | Model · çaba |
|---|---|---|
| **Ana oturum** (ajan dosyası yok) | Ön-kapı, rol yönlendirme, onay merdiveni, `konu-takip.json` kuyruk sunumu, **tüm git commit'leri**, `olcum.jsonl` kapanışı | oturum modeli |
| `kutuphane-denetci` | Denetim yapan: 3'lü çıkış kapısı (`dogrula`, `kapsam-denetimi`, `test`), aylık etki raporu ve toplu onay grupları, `son-aylik-calisma.json`, genel bekçi, proje sağlığı. Yalnız raporlar | inherit · medium |
| `kutuphane-kaynak` | Kaynak işini yapan: yeni repo girişi (`tur-belirle`, `boyut-hesapla`), `ADAY` tür önerisi, fihrist/katalog/`not` üretimi, kendi skiller, site takibi, kayıp kaynak, ad çakışması, güven bilgisi | inherit · medium |
| `kutuphane-inceleme` | İnceleme yapan: ilk kurulum öncesi derin güvenlik ve prompt enjeksiyonu okuması, `skill-calistir` testi, lisans/ücret değişikliği, yeni proje skill öneri raporu, kategori incelemesi | inherit · medium |

Alt-ajanların hepsi `inherit` (o anki oturumun modeli) ve `medium` çaba ile çalışır; sabit modele veya araca kilitlenmez. Model ve çaba her ajanın kendi kaynak dosyasında yazılır.

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
5. İşlerin kesiştiği yerler: kayıp kaynağı denetçi bulur, kaynak rolü (`durum: "kayip"`) işaretler. Güncellemeden sonra yeniden incelenecek skiller ve ilk kurulum öncesi derin kapı inceleme rolüne gider. Tüm git commit'leri, `konu-takip.json` toplu kuyruk sunumu ve proje kurulum onayları ana oturumda kalır.

## 5. Danışman
Bu projede danışman kullanılmaz (K-62, token tasarrufu). `.claude/settings.local.json` içinde `advisorModel` anahtarı yoktur; ajanlar danışman modele sormaz (`ajanlar/ORTAK.md` madde 11). Yeniden açmak yalnız kullanıcı isterse: o dosyaya `"advisorModel"` yazılır; genel `~/.claude/settings.json` içine yazılmaz.

## 6. Sınırlar
- Denetçi düzeltme yapmaz; ama çalıştırdığı denetim araçları kendi rapor dosyalarını (`notlar/` altı) yazar. Claude'da denetçiye dosya düzenleme araçları verilmez; komut çalıştırma yetkisi kalır (denetimler komuttur) ve bu yetki komut bazında kısıtlanamaz. Codex'te ajan başına kısıt yoktur. Yani denetçinin "yalnız kontrol komutu çalıştır" sınırı talimata dayanır.
- Onay kuralları ajanlarla değişmez: `CLAUDE.md` kesin kurallar, K-49 (kayıp kaynak), K-50 (projelerde onaysız işlem yok).

## 7. Ajan eklemek ya da değiştirmek
1. `ajanlar/kutuphane-<ad>.md` dosyasını yaz ya da düzenle. Başlık bloğu: `name` (dosya adıyla aynı), `description` (tek satır; ne zaman kullanılacağını söyler), `model`, `effort`, isteğe bağlı `tools`.
2. Kapsam başka bir ajanla çakışmasın; çakışıyorsa hangisinin sahibi olduğunu iki dosyada da yaz. Yeni ajan açmadan önce işin mevcut bir ajanın alanına girip girmediğine bak.
3. `python3 araclar/ajan-uret.py`, sonra `python3 araclar/ajan-uret.py --kontrol`, `python3 araclar/dogrula.py` ve `python3 araclar/test.py` (`araclar/testler/test_p12-ajanlar.py` her ajanın bu rehberde ve `CLAUDE.md` tablosunda anıldığını denetler).
4. Bu dosyadaki tabloyu ve `CLAUDE.md` "Ajanlar" tablosunu güncelle (`cp CLAUDE.md AGENTS.md`).
5. Bir ajanı kaldırmak: kaynak dosyasını sil, `python3 araclar/ajan-uret.py` üretilmiş dosyalarını da siler.

## 8. Neon (Antigravity) ile çalışma düzeni ve kota
Kütüphane geliştirme ve bakım görevleri Gemini 4 Neon / Argon (Antigravity CLI `agy`) ile yalnız **Medium** eforda yürütülür (K-65):

- **Worktree ve görev dosyası:** Dosya değiştiren her iş ayrı bir git worktree'de açılır (`git worktree add ../SK-neon-<iş> -b neon/<iş>`). Görev talimatı (`NEON-GOREV.md` vb.) worktree klasörünün içine yazılır (sandbox klasör dışını okuyamaz) ve commit'e dahil edilmez.
- **Sandbox ve komut kalıbı:** Sandbox yalnız saf rapor işlerinde kullanılır; komut çalıştırması gereken işler sandbox'sız ama yalnız kendi worktree'si içinde çalışır. Canlı izleme kalıbı:
  ```bash
  agy ... --output-format stream-json | python3 araclar/neon-izle.py --sonuc <dosya>
  ```
- **Doğrulama ve inceleme:** Çıktıdaki `"SUCCESS"` ifadesi tek başına kanıt sayılmaz; iş bitince `git diff --stat`, test/doğrulama çıktısı ve genel skill klasörlerinin (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`) değişmediği kontrol edilir. Silme veya yazma yapan her kod bağımsız ikinci bir Neon incelemesinden geçmeden kullanılmaz; ağ gerektiren yollar birleştirmeden önce gerçek ağla uçtan uca denenir.
- **Kota ve devir:** Kota verisi `~/.cache/kotalar/usage.json` dosyasından okunur. Havuzlar: **Gemini** (Neon / Hydrogen / Flash), **Argon** ve **Claude / GPT**. Bir modelin kalan kotası, 5 saatlik ve haftalık pencerenin küçük olanıdır:
  - **≥ %30:** Normal çalışma.
  - **%15 – %30:** Yeni büyük adım başlatılmaz.
  - **< %15:** Mevcut adım güvenle bitirilir ve durulur.
  - **< %5:** Hemen durulur.
  Başka havuzda kota bolsa o havuza geçilir; oturum devir notu depo dışında `~/Documents/Claude/SkillKutuphanesi-DEVAM.md` dosyasında tutulur.
