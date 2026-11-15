> Yeni oturumsan önce `BASLA.md` dosyasını oku: okuma sırası, "hangi isteğe hangi komut" tablosu, oturum başı rutini. Kalıcı kararlar: `notlar/kararlar.md`.

# SkillKutuphanesi — Agent Talimatı

Bu klasör kullanıcının skill kütüphanesidir. Kullanıcı "şu projeye / şu agent'lara skill ekle" dediğinde aşağıdaki
akışı **atlamadan** izle. Ayrıntı: `rehber/01-skill-ekleme-sureci.md`, `rehber/04-kontrol-listesi.md`.

## Kesin kurallar
1. Global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) **asla** yazma,
   kopyalama, symlink koyma ya da silme. Tek istisna: kullanıcının o iş için adını sayarak açık onay verdiği, önce yedeği alınmış iki iş:
   (a) `rehber/11-program-yonetimi.md` adımlarıyla program güncelleme, geri alma, kaldırma; (b) `rehber/12-genel-klasor-bosaltma.md`
   adımlarıyla boşaltma. Onay yalnız adı sayılan iş içindir, genel izin sayılmaz; verilen onaylar `notlar/kararlar.md`'de kayıtlıdır.
   Skiller sadece kullanıcının verdiği proje klasörüne, sadece `skill-ekle.py` ile kurulur.
2. Elle `cp`/`ln` ile skill kurma; kilit, yedek ve ön kontrol atlanmış olur.
3. `arsiv/` altındaki orijinal skill dosyalarını düzenleme. Notlar `registry.json` (inceleme alanları) ve `notlar/` içine yazılır.
4. `--evet` sadece kullanıcı raporu görüp onayladıktan sonra; `--zorla` sadece kullanıcı açıkça isterse.
5. GitHub'da **sadece `ulukayasaban/SkillKutuphanesi`** ile işlem yapılır. Proje repolarında (Etsy-Arif, Etsy-Yeni, Akil Disi…)
   ve başka hiçbir GitHub reposunda push, PR, birleştirme, dal, issue ya da yorum işlemi yapılmaz; gerekiyorsa kullanıcıya
   anlatılır, işlemi kendisi yapar. (Projeye `skill-ekle.py` ile onaylı yerel kurulum ve kaynak repoları okumak bu kurala girmez.)
6. Skill ve kaynak **yalnızca kendi niteliğiyle** değerlendirilir (üretici, kapsam, bağımlılık, lisans, ücret, kalite, çakışma).
   `registry.json` inceleme alanlarına, `kaynaklar.json` notlarına, kartlara ve önceliğe proje adı ya da "şu projeye uyar/uymaz"
   gerekçesi yazılmaz. Hangi projenin hangi skili kullandığı tek yerde tutulur: `python3 araclar/proje-kullanimi.py` →
   `notlar/proje-kullanimi.md` (elle notlar `projeler.json`). Projeye uygunluk kurulum sırasında (`--oner` / `--kuru`) incelenir.

## Skill ekleme akışı
1. İhtiyacı netleştir: proje yolu, proje tipi, teknoloji, agent rolleri ve hangi AI araçlarıyla açılacağı (Claude Code / Codex / Antigravity / Cursor / VS Code Copilot; Windows'ta açılacak mı). Cevaba göre --arac ortak ya da --arac yalniz-claude ver; rapordaki arac-duzeni, arac-gormez, arac-secimi-yok satırlarını kullanıcıya göster (rehber/14-yapay-zeka-araclari.md). Bilinmiyorsa sor.
2. Öneri: `python3 araclar/skill-ekle.py <proje> --oner "<ihtiyaç>"` (tüm kütüphane taranır). Uygun profil/rolleri seç.
   Konuya uygun skiller arasında GitHub Trending'e girmiş olanları (`🔥trend`) öncele; trend tek başına seçim sebebi değildir.
3. Ön kontrol: `python3 araclar/skill-ekle.py <proje> --profil <p> [--rol …] [--skill …] --kuru`
4. Raporu kullanıcıya göster: kurulacak skiller, roller, HATA/UYARI/BİLGİ satırları ve `ek-aday` listesi
   (kütüphanede ilgili olup seçilmeyen skiller). HATA varsa nedenini ve seçenekleri açıkla, kurma.
5. Onay gelirse aynı komutu `--evet` ile çalıştır. Sonra `--dogrula` sonucunu bildir.

## Ajanlar (kütüphanenin kendi ajanları, K-53)
Ana oturum kullanıcıyla konuşur ve onay alır; iş aşağıdaki tabloya göre uygun ajana verilir. Tek kaynak `ajanlar/kutuphane-<ad>.md` ve
`ajanlar/ORTAK.md`; Claude (`.claude/agents/`) ve Codex (`.codex/agents/`) dosyaları bundan üretilir: `python3 araclar/ajan-uret.py`
(üretilen dosya elle düzenlenmez; `dogrula.py` farkı HATA sayar). Ajan dosyası okumayan araç (Antigravity, VS Code Copilot) işe uyan
`ajanlar/` dosyasını ve `ajanlar/ORTAK.md`'yi okuyup o rolde çalışır. Ajanlar onay gerektiren adımı atmaz, commit ve push yapmaz;
aynı anda yalnız bir ajan kütüphaneye yazar. Model ve çaba her ajanın kendi kaynak dosyasındadır. Ayrıntı: `rehber/15-ajanlar.md`.

| İş | Ajan |
|---|---|
| Sağlık kontrolü, oturum başı ve iş sonu denetimi | `kutuphane-denetci` |
| Yeni kaynak, kendi skiller, siteden alınan skiller (`site/`), kaynak çıkarma, kayıp kaynak, ad çakışması, adaylar | `kutuphane-kaynak` |
| Skill incelemesi (kategori, ücret, lisans, Türkçe özet, güvenlik) | `kutuphane-inceleme` |
| Aylık güncelleme, dal özeti, zamanlanmış görev metni | `kutuphane-guncelleme` |
| Programlar, program bağları, ortam kilitleri, genel skill klasörleri | `kutuphane-program` |
| Projeye öneri ve kurulum, proje durumu ve kaydı, rol ve profiller, araç düzenleri | `kutuphane-proje` |
| Araç kodu, testler, rehberler, hazır istemler, kararlar, ajan dosyaları | `kutuphane-gelistirici` |

## Bakım isteklerinde
- Oturum başı: kütüphane oturumunun ilk işi `python3 araclar/aylik-ozet.py --hizli` (salt okuma, ağsız); çıktıyı kullanıcıya iki cümleyle söyle. Aylık çalışma 35 günü aştıysa "Aylık çalışmayı şimdi yapayım mı?" diye sor; evet derse aşağıdaki "Skilleri güncelle" maddesindeki tek komutu çalıştır. `dikkat`/`sorun` varsa kendiliğinden düzeltme, silme, push yok. Ayrıntı: `BASLA.md`.
- "Skilleri güncelle" (aylık) → tek komut `python3 -u araclar/arsiv-guncelle.py --aylik` (önce istenirse `--aylik --kuru` planı): ön kontrol, kaynak
  raporu, `guncelleme/YYYY-AA` (kaynak değişmişse) ya da `takip/YYYY-AA` dalı, tek sayfa özet, damga `notlar/son-aylik-calisma.json`
  (`tamam`/`kismi`/`basarisiz`/`bekleyen-dal`). Birleştirmez, push etmez; erişilemeyen kaynağı atlar (zamanlanmış görev KAYIP işaretlemez; kütüphane oturumu K-49'a göre işaretler); bekleyen
  dal varken yeni dal açmaz. Özeti ve "karar bekleyenler" listesini kullanıcıya oku → dal özeti ve `notlar/guncelleme-gecmisi.md` kaydı → onay gelirse
  `--birlestir <dal>`. Sonra yeniden incelenecek skilleri incele, etkilenen projeler için `skill-ekle.py <proje> --durum` / `--guncelle --kuru`.
  Ayrıntı: `rehber/02-guncelleme-yonergesi.md` bölüm 1b.
- "Yeni skill ekledim, kontrol et" → kaynak: GitHub **"Yapay Zeka Skillleri"** listesi (tüm skill repoları tek listede).
  `python3 araclar/github-skill-listesi.py` ile YENİ repoları bul, `promptlar/07-yeni-skill-reposu-ekle.md` /
  `rehber/03-yeni-skill-ekleme.md` adımlarını uygula: **çakışma kontrolü** (aynı ad, aynı iş, aynı repoda birden fazla sürüm, aynı adlı kendi skill; genel klasörler 2026-11-12'de boşaltıldı, "global'de farklı sürüm" maddesi yalnız orada bir şey yeniden belirirse önemlidir) ve
  **ücret sınıflandırması** (`ucret-siniflandirma.json`) zorunlu; tek ekleme sırası `rehber/03-yeni-skill-ekleme.md` A1..A9, onay kaydı zorunlu; kullanıcı onayı olmadan kaynak ekleme.
- Ücret: ücretsiz yol önce. `ucretli` = ücret ödemeden hiç kullanılamayan skill (ücretli servis sadece bir seçenekse `kismen`). Ücretli skill (`ucret: ucretli`) rol çekirdeğine ancak gerekçeyle (`ucretli_bilincli`); kurulum raporunda
  ücretli skilleri ayrıca belirt. Liste: `notlar/ucretli-skiller.md`.
- Trend: `python3 araclar/github-trend.py --aday` → `notlar/github-trend.md` (trend'deki kaynaklar + aday skill repoları;
  adaylar onaysız eklenmez). Aylık güncelleme bunu otomatik çalıştırır.
- Popüler skiller: `python3 araclar/populer-tarama.py` → `notlar/populer-skiller.md` (GitHub REST araması + adayda SKILL.md sayımı;
  yıldız listesi/GraphQL ve trending sayfası okunamayan ortamlarda da çalışır). Adaylar onaysız eklenmez; karar `konu-takip.py --karar` (aşağıda "Aday kararları").
- Konu takibi: `python3 araclar/konu-takip.py` (e-ticaret/Etsy, mobil… `kaynaklar.json` → `takip_konulari`) → `notlar/konu-takip.md`.
  Kullanıcı bir alan için "takip et" derse oraya konu ekle. Adaylar onaysız eklenmez; reddedileni `--karar` ile kaydet.
- Proje kullanımı: hangi projenin hangi skili kullandığı `notlar/proje-kullanimi.md`'de (kaynak: projelerin `kilit.json`'u; elle
  notlar `projeler.json`). `skill-ekle.py` her değişiklikten sonra yeniler; elle: `python3 araclar/proje-kullanimi.py`
  (`--skill <kimlik>` / `--repo owner/ad`: silmeden, tercih değiştirmeden, ad devretmeden önce). Ayrıntı: `rehber/10-proje-kullanimi.md`.
- Ad ve çakışma: çıplak ad kendiliğinden el değiştirmez (yeni gelen `ad@kaynak` olur); aynı ad farklı işse eski kayıt `durum_elle`
  ile tercih sabitlenir; bilerek devir `kaynaklar.json` → `ad_devral` ve kullanıcı onayıyla. Repo GitHub'da taşınırsa `repo`
  güncellenir, eski ad `eski_adlar`'a yazılır. Ayrıntı: `rehber/09-ad-kimlik-ve-cakisma.md`.
- Programlar (skill olmayan yapılar: HyperFrames, OpenMontage, nlm, etsyotomasyon): `programlar.json` kartları; HyperFrames, OpenMontage ve nlm `kopya: yerinde` (bu bilgisayarda kurulu haliyle izlenir; nlm = uv tool, PyPI paketi). Her güncelleme, geri alma ve kaldırma kullanıcının AYRI onayıyla ve önce yedekle yapılır: `rehber/11-program-yonetimi.md` → "Taze ajan: istek → adımlar", hazır istem `promptlar/13-program-kur-guncelle.md`. Önce `python3 araclar/program-denetim.py --oncesi <ad>` "HAZIR" demelidir. Projeye `skill-ekle.py` ile kurulmaz.
- Programla gelen skiller (K-28): OpenMontage, HyperFrames ve nlm (`nlm-skill`) skilleri projeye KOPYALANMAZ; `python3 araclar/skill-ekle.py <proje> --program-skill PROGRAM:AD --kuru` ile programın kendi klasörüne BAĞ verilir (kart: `skill_koku`; klasör adı skill adından farklıysa `skill_klasorleri`, ör. `nlm:nlm-skill`), kilit: `dis_skiller`. Kaynağı artık hiçbir yerde verilmeyen eski skill `--dondur <yol>` ile projenin kendi skili olarak dondurulur (kütüphane güncellemez). Program güncellemesinden önce ve sonra `python3 araclar/proje-kullanimi.py --program <ad>` ve `program-denetim.py --oncesi <ad>` ('bağlar' satırları); ayrıntı: `rehber/01`, `rehber/11`.
- Proje takibi: aylık ya da "projeleri kontrol et" denince `python3 araclar/proje-kullanimi.py --saglik` (`notlar/proje-durumu.md`; projelere salt okuma, kayıtsız klasörleri de tarar). Yeni proje / çıkar / taşındı / yoksay: `--ekle`, `--cikar`, `--tasindi`, `--yoksay` (yalnız `projeler.json` değişir, önce plan, onayla `--evet`). Ayrıntı: `rehber/10-proje-kullanimi.md`, `promptlar/12-proje-kullanimi-ve-etki.md`.
- Git ve yedek: `araclar/git-durum.py`, `araclar/yedek-denetim.py` (salt okuma); yedek ve geri alma kuralı `rehber/13-yedek-ve-geri-alma.md`. Her yedek `yedekler.json`'a kaydedilir. Push yalnız kullanıcı isteyince.
- Genel klasörler (2026-11-12'de boşaltıldı, K-40): beklenmeyen girdi için `python3 araclar/genel-bekci.py` (yalnız okur, hiçbir şeyi silme). Yeniden boşaltma yalnız `rehber/12-genel-klasor-bosaltma.md` ile, her adım ayrı onayla; hazır istem `promptlar/16-genel-klasor-bosaltma.md`.
- Kaynak/skill çıkarma, emekli, kayıp kaynak: `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` (yalnız okur: etki + sıralı adımlar + geri alma); onayla uygula. Ayrıntı: `rehber/03-yeni-skill-ekleme.md` bölüm D-G, `promptlar/14-kaynak-cikar.md`.
- Aday kararları: `python3 araclar/konu-takip.py --karar owner/ad eklendi|reddedildi|izle "neden"` (`populer-tarama.py --karar` kullanma); bekleyenler: `python3 araclar/konu-takip.py --bekleyenler` (üç kaynağı özetler).
- Yeni AI aracı: `rehber/14-yapay-zeka-araclari.md` bölüm 7 ve `promptlar/15-yeni-yapay-zeka-araci.md`; aylık araç belgesi kontrolü: `python3 araclar/skill-ekle.py --araclar`.
- `CLAUDE.md` ve `AGENTS.md` birebir aynı tutulur: birini değiştirince `cp CLAUDE.md AGENTS.md`; `dogrula.py` farkı HATA sayar.
- Kendi skillerim (yerel kaynak T7, `kendi/` klasörü, `yerel/kendi` kaydı): GitHub'a sorulmaz. Düzenleme: `kendi/<ad>/` düzenle → `python3 araclar/kaynak-cek.py --repo yerel/kendi` (ağ yok) → `arsiv-yerlestir.py` → kontroller → projede `--durum`/`--guncelle`. Ayrıntı: `rehber/03` B2, `kendi/README.md`. `kendi/` yalnız kullanıcının kendi yazdığı skiller içindir.
- Web sitesinden alınan (GitHub'da olmayan) skill (K-57) → `site/<ad>/`, kaynak `yerel/site` (T8), `site-takip.json` kaydı zorunlu (sahip, lisans, izlenen dosyaların sha256'sı; eksikse `dogrula.py` HATA), `kendi/`'ye konmaz. Site değişti mi: `python3 araclar/site-takip.py` (aylık zincir de çalıştırır; rapor `notlar/site-takip.md`, ERİŞİLEMEDİ KAYIP sayılmaz). Güncelleme her seferinde kullanıcı onayıyla, elle. Sitede GitHub reposu çıkarsa normal kaynağa (rehber/03 A1..A9) geçirilir ve `site/` kopyası emekli olur. Ayrıntı: `rehber/03` B3, `site/README.md`.
- Kayıp kaynak (K-49, kullanıcı 2026-11-12): GitHub'da gerçekten yok olan (404; `gh auth status` sağlam, yeni ada taşınmamış) ve hiçbir projede kullanılmayan
  kaynak kullanıcıya SORULMADAN `tip: KAYIP` yapılır (`rehber/03` E; arşiv kopyası kalır, rol/profillerden çıkarılır, sonuç bir cümleyle bildirilir). Bir projede
  kullanılıyorsa önce kullanıcıya sorulur. Kaynağı kayıp ya da kaynakta kaldırılmış skill yeni kurulumda kullanılmaz: `--oner` ve `ek-aday` göstermez, role/profile eklenmez.
- Eski sürümler: bilerek çıkarılan skiller `kaynaklar.json` → `arsivden_cikarilanlar`.
- Hazır promptlar: `promptlar/` (kullanıcıya proje başlangıcı, ekleme, güncelleme, bakım için).
- Her değişiklikten sonra: `python3 araclar/kapsam-denetimi.py` (0 sorun) ve `python3 araclar/dogrula.py` (0 hata), sonra `git commit`.
- GitHub: kütüphane `ulukayasaban/SkillKutuphanesi` deposunda **private** (varsayılan dal `master`). Push ve PR **sadece kullanıcı
  isteyince**; depoyu public yapma. Aylık güncelleme PR'ı GitHub'da birleştirilmez: onaydan sonra yerelde `--birlestir`, sonra
  `git push origin master`. Ayrıntı: README "GitHub deposu (private)", `rehber/02-guncelleme-yonergesi.md`.
