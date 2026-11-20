# Program incelemesi: OpenMontage ve HyperFrames (2026-11-20)

> Elle yazılmış inceleme notu (kullanıcı isteğiyle, 2026-11-20). `notlar/program-denetimi.md` araç çıktısıdır ve her çalıştırmada yeniden yazılır; kalıcı bulgular buraya yazılır.
> Güncelleme `rehber/11-program-yonetimi.md` adımlarıyla, kullanıcının bu iki güncelleme için verdiği onayla yapıldı.

## 1. Güncellemeler
| Program | Önce | Sonra | Yedek | Not |
|---|---|---|---|---|
| HyperFrames (npm genel paket) | 0.9.37 | 0.9.71 | `~/Documents/Claude/yedek/hyperframes-2026-11-20/` (0.9.37) | 34 sürüm; sürüm notlarında kırıcı değişiklik yok; `HYPERFRAMES_SKIP_SKILLS=1` ile kuruldu; 5 skill bağı çözülüyor |
| OpenMontage (git klonu) | `fecb9a1e` | `2e003e65` | `~/Documents/Claude/yedek/openmontage-2026-11-20/` | tek commit, yalnız dört README'ye bağlantı; `git pull --ff-only`; venv'e dokunulmadı; 11/11 sabit sürüm tutuyor; 12 yerel değişiklik yerinde |

Kartlar (`programlar.json`, iki `KAYNAK.md`) güncellendi; npm integrity değeri yeni sürüme çevrildi. Yedekler `yedekler.json`'a kaydedildi. Sonradan (2026-11-20, kullanıcı "yedekleri sil" deyip seçti) bu güncellemelerin ve eski program yedeklerinin, gizli içerikli `ayar-*` ile öteki 30 günlük yedeklerin tamamı silindi (15 klasör, 623 MB; kayıtlar `durum: silindi`). Geri alma artık yedekten değil, programların kendi sürümünden (`npm install -g hyperframes@0.9.37`, `git switch --detach fecb9a1e`) yapılır. Silinmeyenler: boşaltma ve geçiş yedekleri (akil-disi-tam, istatistik-skill-gecisi, genel-skiller-tam, genel-kaldirilan, global-skills-2026-11-08) ve `deneme/openmontage-fecb9a1e`.

## 2. Bulgular
### Büyüme ve disk
- OpenMontage büyümüyor: `~/.openmontage` 4,6 GB (venv 3,3 GB, `remotion-composer/node_modules` 872 MB); venv 12 Kasım güncelleme sonrası yedekle birebir aynı, o günden beri paket eklenmemiş. `~/Movies/OpenMontage` 97 MB.
- Asıl artış `$TMPDIR` altındaki test artıklarıydı: 475 `tmp*` klasörü (3,9 GB), kaynak IstatistikYoutube projesinin `tools/kurgu/_test` betikleri (rastgele adlı `tempfile.mkdtemp()`, silinmiyordu). 11 teste çıkışta silen kod eklendi (yedek `istatistik-test-temizlik-2026-11-20`).
- Önekli artıklar (`cakisma-hf-`, `band-tara-`, `ekran-dom-`, `kart_hazir_`, `band-test-`, `arac_duz_a_`, `skill-test-`) ilk temizlikte gözden kaçmıştı; 466 klasör (376 MB) Çöp Sepeti'ne taşındı (`~/.Trash/tmp-test-artiklari-2026-11-20`).
- HyperFrames geçmiş önbelleği `~/.cache/hyperframes/history` 1,4 GB / 1.096 kayıttı: her render edilen proje dizini bir kayıt açar, kendiliğinden küçülmez; `hyperframes clean` yalnız 35,7 MB siler. Kayıtların büyük kısmı test çıktı dizinlerine (`_test/duman-cikti`, `$TMPDIR`) aitti. Projesi olmayan (185), geçici dizin (671) ve 7 günden eski (93) kayıt Çöp Sepeti'ne taşındı (`~/.Trash/hf-history-2026-11-20`, liste `~/Documents/Claude/SkillKutuphanesi-saklanan/hf-history-tenekeye-2026-11-20.txt`); 150 kayıt / 153 MB kaldı. Kayıtlar yalnız geri alma geçmişidir, render çıktıları değil.
- Test dışı araçların sızıntısı: `cakisma_tara.py` (iki yerde) ve `ekran_yazi_kontrol.py` geçici klasörü silmiyordu (düzeltildi, aşağıda). `ornek_kare.py` ve `tarayici/oku.py` zaten temizliyordu (ilk tespit yanlıştı).

### HyperFrames 0.9.71
- `hyperframes doctor` temiz; uyarılar isteğe bağlı: Kokoro, MusicGen kurulu değil; Docker kurulu ama çalışmıyor (proje bulut ve Docker kullanmaz).
- 0.9.71 render için artık sistem Chrome'unu seçiyor (`/Applications/Google Chrome.app`); önceden `~/.cache/hyperframes/chrome` içindeki headless-shell. Aynı 3 sn'lik sahne iki tarayıcıyla render edildi: mp4 dosyaları SHA-256 düzeyinde birebir aynı (90 kare). Yani bu sahnede fark yok; karmaşık sahnelerde ayrıca gözlenebilir. Zorlamak için `HYPERFRAMES_BROWSER_PATH`.
- Render sırası: başka bir render sürerken ikinci `hyperframes render` kuyrukta bekler (ölçülen bekleme ≈3 dk); iki render aynı anda koşmaz.
- IstatistikYoutube `config/tools.yaml` kaydı 0.9.37 kalmıştı ve `render_sirali.sh` bu değerle karşılaştırıyor; güncellemeden sonra `test_render_sirali_hfsurum` bu yüzden FAIL verdi. Kayıt satırı 0.9.71'e çekildi, test geçti.
- `hyperframes clean --dry-run` 35,7 MB siler; proje tarafında `.hyperframes/artifacts/checks` rapor klasörleri bırakır, sorun değil.

### OpenMontage `2e003e65`
- Araç kaydı (`tool_registry`) hatasız yükleniyor: 164 araç, 24 grup; kullanılamayan araçların büyük kısmı anahtarsız (beklenen).
- `pip check`: yalnız `manim 0.19.1` numpy>=2 ister, kurulu numpy 1.26.4; `import manim` çalışıyor. Sabit sürüm yüzünden bilinen uyuşmazlık, düzeltilmez.
- `.python-version` 3.11 ve Makefile 3.10 diyor, venv 3.10.21: yukarı akım tutarsızlığı, sorun yok.
- `.node-version` 22.23.4, kurulu Node v26.13.1: Remotion CLI `compositions` listesini veriyor; sorun yok.
- `corpus_builder` DEGRADED: yapılandırılmış kaynak sayısı toplamdan az demek, bozuk değil. `minimax_*` araçları `MINIMAX_API_KEY` olmadığı için kapalı (beklenen).
- Güncelleme ön kontrolü `gfpgan/` yaması için "kayıtlı ama değişmemiş" bilgisi veriyor (yama upstream'e girmiş ya da kaybolmuş olabilir); kartta açık iş.
- Giriş yolu UYARI'sı (`claude-code: .claude/skills/openmontage/SKILL.md`) kütüphane klasöründe arama yaptığı için çıkıyor; skill iki projede (Akil Disi Youtube Kanali, IstatistikYoutube) var.
- Venv ve `remotion-composer/node_modules` dışında dikkat çeken büyük yer: `~/Documents/Claude/deneme/openmontage-fecb9a1e` (2,9 GB, silme günü ~12 Aralık, kullanıcı "şimdilik silme" dedi) ve `~/.cache/huggingface` (6 GB, Whisper large-v3 2,9 GB dahil, hepsi Eylül tarihli).

## 3. Duman testi (IstatistikYoutube `tools/kurgu/_test/duman.sh --hf --qa`)
- Güncellemeden önceki koşu: 133 geçti / 0 FAIL, ama bölüm 9'da (qa_tam) yarıda kesildi (çıkış 143). Ayrı çalıştırılan HF 3 sn alfa render (duman bölüm 10): geçti, 36 sn, VP9 1080×1920, alfa 0..255.
- Güncellemeden sonraki tam koşu: sonuç aşağıdaki "Sonuç" başlığında.

### Sonuç
- **142 geçti, 1 FAIL**, süre yaklaşık 27 dk (makine yükü 25-38; WindowServer, Google Drive ve contactsd CPU yiyordu, bizim süreçlerimiz değil). Tek FAIL `test_render_sirali_hfsurum`: `config/tools.yaml` HyperFrames kaydı 0.9.37 kalmıştı; kayıt 0.9.71 yapılınca test tek başına geçti (4/4 OK).
- Önceden eksik kalan bölümler bu koşuda tamamlandı: 9 `qa_tam` (whisper "birebir"), 10 HF 3 sn alfa render (`.webm` 45.878 bayt, güncelleme öncesiyle aynı boyut; sistem Chrome ile), 11 GSAP eklentileri ve `test_yaklasma --render`, 12 `kaba_cizim` ve `serbest_sahne`; sonda "arka planda artık süreç yok" kontrolü 200 sn bekleme sonrası geçti.
- Sistem Chrome / headless-shell karşılaştırması: aynı sahne iki tarayıcıyla birebir aynı mp4 (SHA-256 aynı).

### Düzeltilen araç sızıntıları (IstatistikYoutube, yedek `istatistik-test-temizlik-2026-11-20/kurgu`)
- `tools/kurgu/cakisma_tara.py` (iki yerde: `cakisma-hf-`, `band-tara-`) ve `tools/kurgu/ekran_yazi_kontrol.py` (`ekran-dom-`) geçici klasörü okuma sonrası ve hata yolunda siliyor. `test_cakisma_hf`, `test_band_tara`, `test_cakisma_tara`, `test_qa_yanlis_alarm`, `test_sahne_tasima` geçti; koşudan sonra bu öneklerde yeni klasör kalmadı.
- 11 test dosyasına `atexit` temizliği eklenmişti (önceki adım).

## 4. Açık işler
- `.python-version` / `.node-version` ve `manim` uyuşmazlığı için işlem gerekmiyor.
- Çöp Sepeti'ne taşınanlar (HF geçmişi 1,29 GB, TMPDIR artıkları ~0,4 GB) kullanıcı sepeti boşaltana kadar disk yer kaplar.
- IstatistikYoutube `config/tools.yaml` HyperFrames kaydı güncellendi (yedek `istatistik-test-temizlik-2026-11-20/config`). Projenin `status/handoff-defteri.md` satırı bu oturumda yazılmadı; proje oturumu kendi kaydını tutar.
- Yeni sürümde Chrome seçimi değişti: karmaşık bir sahnede (GSAP eklentileri, video kaynakları) görüntü farkı çıkarsa `HYPERFRAMES_BROWSER_PATH` ile eski headless-shell'e dönülebilir.
- Güncelleme yedekleri silindi; HyperFrames'i 0.9.37'ye döndürmek gerekirse `HYPERFRAMES_SKIP_SKILLS=1 npm install -g hyperframes@0.9.37`, OpenMontage için `git -C ~/.openmontage switch --detach fecb9a1e3cc23ef84de30b272059457a427f16f8`. Yerel yamalar çalışma ağacında durur (git switch bunları ezmez; yine de önce `git status` bak).
