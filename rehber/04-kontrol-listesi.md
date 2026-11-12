# 04 — Agent'a Skill Verirken Kontrol Listesi

Bu listenin büyük kısmı `skill-ekle.py`'nin **ön kontrolü** tarafından otomatik yapılır. Kod adları, rapordaki
`[HATA] kod:` / `[UYARI] kod:` etiketleridir. Agent'lar (Claude/Codex) bu raporu sana göstermeden `--evet` kullanmamalıdır.

## A. Kurulumdan önce (senin kararın)
- [ ] **Kapsam:** `--oner "<ihtiyaç>"` çalıştı mı? Rapordaki `tarama` satırı tüm kütüphanenin tarandığını gösterir;
      `ek-aday:<rol>` satırları seçilmemiş ama ilgili skilleri listeler. Bunlara bilerek "hayır" de.
- [ ] **Rol başına skill sayısı:** çekirdek 3–6 skill ideal. 12'den fazlası ya da 150 KB'tan fazla SKILL.md → `baglam-yuku`.
- [ ] **Aynı işi yapan iki skill aynı role verilmedi** → `ortusme`, `ayni-skill-iki-surum`.
- [ ] **Teknoloji uyumu:** skill'in teknolojisi projenle aynı mı (React mı, vanilla mı, Three r17x mi)? KATALOG.md → Teknoloji sütunu.
- [ ] **Hangi araçlar?** Claude Code / Codex / Antigravity / Cursor / VS Code Copilot / Windows? Cevaba göre `--arac ortak` ya da `--arac yalniz-claude`; raporda `arac-duzeni`, `arac-gormez` ve `arac-secimi-yok` satırlarını oku (rehber/14). `codex-uyum` / `claude-ozel` uyarılarını da oku.

## B. Ön kontrolün denetledikleri

| Kod | Seviye | Ne demek | Ne yapmalı |
|---|---|---|---|
| `global-baglanti` / `proje-disi-baglanti` | HATA* | Projedeki `.claude`/`.agents`/`.codex` klasörü symlink ile global ya da proje dışı bir yere gidiyor | Symlink'i kaldır, gerçek klasör yap |
| `ayni-klasor` | HATA* | `.claude/skills` ve `.agents/skills` aynı klasör | İkisini ayrı klasör yap (araç kendisi bağlar) |
| `gecersiz-rol-adi` | HATA* | Rol adı küçük harf/rakam/- dışında karakter içeriyor | Geçerli ad ver |
| `kendi-agent-dosyan` | HATA* | `.claude/agents/<rol>.md` ya da `.codex/agents/<rol>.toml` senin dosyan | Rolü başka adla ekle |
| `global-cakisma-yeni` | UYARI | Kurulumdan sonra globale aynı adlı farklı skill eklenmiş (Claude'da global kazanır; genel klasörler boş olduğundan yalnız orada bir şey yeniden belirirse) | `--kaldir` + yeniden ekle (ekli adla kurulur) |
| `kaynak-yok` | UYARI | Kurulu skill'in kaynağı kütüphanede artık yok | Projede olduğu gibi kalır; başka repo'nunki otomatik konmaz |
| `onarilacak` | BİLGİ | Eksik/bozuk kurulum (`--guncelle` onarır) | — |
| `ucretli` | UYARI | Skill **ancak** ücretli bir API/abonelik/lisansla çalışır; ücretsiz kullanım yolu yok (`notlar/ucretli-skiller.md`) | Ücretsiz alternatifini seç; gerekiyorsa bilerek onayla |
| `kismen-ucretli` | BİLGİ | Ücret ödemeden kullanılabilir (ücretsiz katman/kota ya da ücretli servis sadece bir seçenek); bazı yollar ücretli | Agent'a ücretsiz yolu önce kullanmasını söyle (`promptlar/06`) |
| `ucret-belirsiz` | UYARI | Ücret durumu sınıflandırılmamış | `ucret-siniflandirma.json`'a ekle |
| `emekli` | UYARI | Eski/emekli sürüm (yerine geçeni var) | Yerine geçeni kur |
| `bulunamadi` | HATA* | İstenen skill kütüphanede yok | `--ara <kelime>` ile doğru adı bul |
| `isim-cakismasi` | HATA* | İki farklı skill aynı klasör adına kurulacaktı | Birini çıkar |
| `projede-kendi-skillin` | HATA | Projede kütüphaneden gelmemiş aynı adlı skill var | Dokunulmaz. Seninkini yeniden adlandır ya da `--zorla` (yedeklenir) |
| `farkli-kaynak` | HATA* | O ad projede başka bir kaynaktan kurulu | Önce `--kaldir` |
| `elle-degistirilmis` | HATA | Kurulu skill sonradan elle değiştirilmiş | Değişikliği korumak için dokunma; ezmek için `--zorla` |
| `onyukleme-siniri` | HATA* | Rolde 32'den fazla skill (Claude sınırı) | Rolü böl |
| `baglam-yuku` | UYARI | Rol çok fazla skill/metin önyükleyecek | Opsiyonelleri çıkar |
| `ortusme` | UYARI | Aynı örtüşme grubundan birden çok birincil ya da aynı skill'in iki sürümü | Birini seç |
| `alternatif-surum` | UYARI | Tercih edilen değil, alternatif sürüm seçildi | Bilerek seçtiysen sorun yok |
| `ayni-ad` | BİLGİ | Aynı adda birden fazla skill var; kurulan kimlik, kaynağı ve diğer sürümler listelenir | Yanlış kaynaksa tam kimliği yaz: `--skill <ad@kaynak>` (`rehber/09`) |
| `codex-uyum` | UYARI | SKILL.md'de Claude'a özgü araç adları var | Codex mantığı uygular; kritik işte test et |
| `claude-ozel` | UYARI | Konu Claude Code'a özel (plugin/hook) | Codex agent'ına verme |
| `bagimlilik` | UYARI | Başka bir kurulum gerekir (ör. OpenMontage) | Kurulumun hazır olduğundan emin ol |
| `kirik-baglanti` | UYARI | SKILL.md'nin gösterdiği bir dosya yok (kardeş skilldeki hedefler sayılmaz) | Kaynak repoda da yoksa önemsiz; değilse kategoriyi incele |
| `kardes-eksik` | UYARI/BİLGİ | Skill başka bir kardeş skill'e dayanıyor (`../<kardeş>/` ya da kardeşin genel yolu). UYARI: kardeş projeye kurulmuyor ya da istenen dosya arşivde yok. BİLGİ: kardeş de kuruluyor, sorun kendiliğinden çözülür | UYARI ise önerilen `--skill <id>` ile kardeşi de ekle |
| `kardes-yol` | BİLGİ | Kardeş skill de kuruluyor; kurulan kopyada kardeşe giden yollar (`../<kardeş>/…` ya da sabit genel yol) projedeki adına çevrilir | Bilgi; elle bir şey gerekmez |
| `yol-yerellestirme` | BİLGİ | Skill metninde bilgisayarın genel klasörüne giden sabit yollar var; kurulan kopyada proje içi yola çevrilecek (arşivdeki orijinal değişmez) | Bilgi; elle bir şey gerekmez |
| `genel-yol` | UYARI | Skill kendi (ya da başka skill'in) genel klasör yoluna dayanıyor ama bu yol otomatik çevrilemiyor: betik içinde, kurulum anlatan dosyada, karışık dosyada ya da dosya arşivde yok | Satırı oku; skill projede çalışmayabilir. Gerekirse yama yaz ya da kurma |
| `eklenti-koku` | UYARI/BİLGİ | Skill eklenti kökündeki dosyalara dayanıyor; bu dosyalar arşive alınmamış, düz kurulumda o adımlar çalışmaz. BİLGİ: başka bir seçenek de sunuluyor | UYARI ise o adımları elle hazırla ya da skill'i kurma |
| `skil-disi-yol` | UYARI | Skill, kendi klasörünün dışına çıkan bir yola dayanıyor ve hedef dosya arşivde yok | Kaynak repoda dosyayı ara; yoksa skill eksik çalışır |
| `genele-yazabilir` | UYARI/BİLGİ | Skill bilgisayarın genel skill/agent klasörüne dosya kopyalıyor (UYARI) ya da bunu ajan adımı olarak anlatıyor (BİLGİ). Kütüphane kuralı genel klasöre yazmayı yasaklar | O adımı ajanın çalıştırmasına izin verme |
| `yol-istisna` | BİLGİ | Bazı yol bulguları `yol-istisnalari.json` kaydıyla kapsandı (öğretici metin) | Bilgi |
| `istisna-eskidi` | UYARI | `yol-istisnalari.json` kaydı artık tutmuyor, dosyalar değişmiş | Kaydı yeniden doğrula ya da sil |
| `kardes-farkli-kaynak` | UYARI | Skill'in beklediği kardeş, projede ya da kurulumda başka bir kaynaktan aynı adla duruyor | Doğru kardeşi kur ya da önce eskisini `--kaldir` ile çıkar |
| `lisans` | UYARI | Lisans belirtilmemiş | Ticari projede dikkat |
| `dusuk-puan` | UYARI | Değerlendirme < 50 (D) | Alternatife bak |
| `yapi` | UYARI/BİLGİ | Frontmatter sorunları (uzun açıklama, standart dışı ad, otomatik çağrılamaz) | Ad kurulumda otomatik düzeltilir |
| `tetiklenmez` | UYARI | description yok/çok kısa/1024'ten uzun ve registry'de `aciklama_duzeltme` yazılmamış: kurulunca agent skill'i doğru durumda seçemez | `registry.json`'a `aciklama_duzeltme` yaz (`rehber/03-yeni-skill-ekleme.md` → "Description ve tetiklenme") |
| `yama` | BİLGİ | Kurulan kopyada `yamalar/<id>/` altındaki düzeltilmiş dosya kullanılır (ör. sözdizimi hatalı betik) | Bilgi; arşivdeki orijinal değişmez |
| `aciklama-onarim` | BİLGİ | Description kurulan kopyada düzeltilir (registry `aciklama_duzeltme`; yorum arkasındaki frontmatter başa alınır, YAML'ı bozan description tırnaklanır). `--guncelle` mevcut kurulumlara da uygular | Bilgi; arşivdeki orijinal değişmez |
| `ekli-ad` | BİLGİ | Globalde farklı bir sürüm olduğu için `--kutuphane` ekli adla kurulur | Agent dosyaları bu adı kullanır |
| `hesap-cakismasi` | BİLGİ | Claude hesabında (claude.ai, `~/.claude/skills/synced/`) aynı adlı skill var; agent onu (`anthropic-skills:<ad>`) seçerdi. Proje `.claude/settings.json` → `skillOverrides` ile hesaptaki o projede `off` yapılır; `--dogrula` denetler, `--guncelle` onarır | Hesaptakini istiyorsan değeri `"on"` yap (araç dokunmaz) |
| `globalde-ayni` | BİLGİ | Globalde birebir aynısı var (genel klasörler boş; yalnız orada bir şey yeniden belirirse) | Sorun değil |
| `arac-surumu` | BİLGİ | Claude ve Codex'e ayrı uyarlanmış sürümler kurulacak | — |
| `alt-skill` | BİLGİ | Başka bir skill'in alt klasörü | Üst skill'i de kurmak isteyebilirsin |
| `gizli-katalog` | BİLGİ | Entegrasyon ya da repo-içi katalogdan | — |
| `incelenmedi` | BİLGİ | Kategori incelemesi henüz yapılmadı | Kritik işte SKILL.md'yi oku |
| `arac-duzeni` | BİLGİ | Projenin araç düzeni (`ortak` / `yalniz-claude`), seçimin yapılıp yapılmadığı, skilleri görenler ve görmeyenler | Doğru araçlar listelendi mi bak; değilse `--arac` ile düzeni değiştir |
| `arac-gormez` | BİLGİ | Bu düzende bazı kurulu araçlar (ör. Codex, Antigravity) projedeki skilleri görmez | Onları da kullanacaksan `--arac ortak` |
| `arac-secimi-yok` | BİLGİ | Araç düzeni hiç seçilmedi; varsayılan `ortak` uygulanıyor | Kullanıcıya hangi araçlarla açılacağını sor, `--arac` ile kaydet |
| `arac-cift-okuma` | BİLGİ | Cursor ve VS Code Copilot hem `.agents/skills` hem `.claude/skills` okur; aynı skill iki kez listelenebilir (denenmedi) | Görürsen kullanıcıya bildir (rehber/14 bölüm 9) |
| `arac-symlink` | BİLGİ | `.claude/skills` bağları symlink; Windows'ta ya da `core.symlinks` kapalı git'te düz metne döner | Windows'ta açılacaksa `--arac yalniz-claude` |
| `arac-rolsuz` | BİLGİ | Rol dosyaları yalnız Claude ve Codex için üretilir; diğer araçlarda her ajan tüm proje skillerini görür | Bilgi |
| `arac-mutlak-yol` | BİLGİ | `.codex/agents/*.toml` bu bilgisayarın mutlak yollarını içerir; proje taşınırsa Codex rol dışı skilleri kapatamaz | Kütüphanenin olduğu Mac'te `--yenile` |
| `arac-belge-yok` | BİLGİ | `yapay-zeka-araclari.json` okunamadı; araç satırları atlandı | Dosyayı onar (kurulum etkilenmez) |
| `arac-karisik` | HATA | `--arac` ile düzen değişiyor ama projede eski düzende kurulu skiller var | Önce yalnız `--arac <düzen> --kuru`, sonra `--evet`; ardından skill ekle |

**HATA\*** = `--zorla` ile de geçilemez (güvenlik/tutarlılık). Diğer HATA'lar `--zorla` ile, önce yedek alınarak geçilebilir.

## C. Kurulumdan sonra
- [ ] `--dogrula` → ✅ (kopya, symlink, SKILL.md adı = klasör adı, agent dosyaları, Codex yolları, yarım kurulum yok)
- [ ] `--durum` → her skill "güncel"
- [ ] `notlar/proje-kullanimi.md` yenilendi (araç kendisi yapar; kütüphanede bir sonraki bakımda commit edilir)
- [ ] Claude'da: projeyi aç, alt-agent listesinde rol görünüyor mu (`/agents`)
- [ ] Codex'te: `codex exec "list available skills"` proje skillerini gösteriyor mu
- [ ] Proje git'teyse `.agents/`, `.claude/`, `.codex/`, `.skill-kutuphanesi/kilit.json` commit edilebilir;
      araç ilk yedekte `.skill-kutuphanesi/.gitignore` dosyasını kendisi yazar (`yedek/`)
- [ ] `arac-duzeni` satırı doğru araçları listeledi mi; `arac-secimi-yok` çıkıyorsa kullanıcıya soruldu ve `--arac` ile kaydedildi
- [ ] Antigravity / Cursor / Copilot'ta gerçek deneme yapıldıysa `yapay-zeka-araclari.json` → `denendi`'ye yazıldı

## D. Agent'lar için kural (CLAUDE.md / AGENTS.md'de de yazılı)
1. Önce `--oner`, sonra `--kuru`. Raporu **olduğu gibi** kullanıcıya göster.
2. HATA varsa kurulum yapma; nedenini ve çözüm seçeneklerini söyle.
3. UYARI varsa kullanıcı açıkça onaylamadan `--evet` kullanma. `--zorla`'yı sadece kullanıcı isterse kullan.
4. Kurulumdan sonra `--dogrula` sonucunu bildir.
5. Global skill klasörlerine elle dosya kopyalama, symlink ya da silme yapma.
6. Hangi araçlarla açılacağını sormadan ilk kurulum yapma (`arac-secimi-yok`).
(Not: bu 6. kural kütüphanenin CLAUDE.md / AGENTS.md dosyalarında "Skill ekleme akışı" 1. adımında yazılıdır.)
