# Yama A: CLAUDE.md ve AGENTS.md işaretçi ve akış satırları (P8, onay bekliyor)

Durum: UYGULANMADI. `CLAUDE.md` ve `AGENTS.md` kullanıcı onayı olmadan değişmez. Bu yama kural değiştirmez; yalnız işaretçi satırı,
akış maddeleri ve bakım satırları ekler. P1, P2, P3, P4, P5, P6 ve P7'nin istediği metinler tek yamada birleştirildi
(`p1-claude-agents-md.md` bunun alt kümesidir; ikisini ayrı uygulama, yalnız bunu uygula).

Neden gerekli: `dogrula.py` `CLAUDE.md` ilk satırının `BASLA.md`'ye işaret etmesini ister. Yama uygulanana dek `dogrula.py` bu tek
UYARI'yı verir ve `duman-testi.py` "bilinmeyen uyarı yok" adımı bu yüzden başarısız olur (HATA değildir, aylık birleştirme geri sarılmaz).

## Uygulama (onaydan sonra, kütüphane klasöründe, tek komut dizisi)
1. Aşağıdaki farkı `CLAUDE.md` dosyasına uygula (metinle eşleştirerek; satır numaraları bugünkü dosyaya göredir).
2. `cp CLAUDE.md AGENTS.md`
3. `cmp CLAUDE.md AGENTS.md` sessiz olmalı.
4. `python3 araclar/dogrula.py` 0 hata; bayrak ve eski anlatım UYARI'sı olmamalı. Commit iletisi: "AGENTS.md eşitlendi".

Önerilen yamanın bayrakları bugünkü araç kaynaklarına karşı denendi (geçici ağaçta `dogrula.bayrak_denetimi`): 0 bulgu.
Düzeltmeler: aylık çalışma cümlesi P4'ün Aşama 2'si gelene dek `--aylik --kuru` + `rehber/02` yolunu söyler (P4 isteği);
`populer-tarama.py --karar` yerine `konu-takip.py --karar` (P7 isteği); "Aylık güncelle" maddesi değişmedi (P4'ün `--aylik` yazma adımı Aşama 2'de).

## Fark (`diff -u CLAUDE.md <yamalı>`)
```diff
@@ -1,3 +1,5 @@
+> Yeni oturumsan önce `BASLA.md` dosyasını oku: okuma sırası, "hangi isteğe hangi komut" tablosu, oturum başı rutini. Kalıcı kararlar: `notlar/kararlar.md`.
+
 # SkillKutuphanesi — Agent Talimatı
 
 Bu klasör kullanıcının skill kütüphanesidir. Kullanıcı "şu projeye / şu agent'lara skill ekle" dediğinde aşağıdaki
@@ -18,7 +20,7 @@
    `notlar/proje-kullanimi.md` (elle notlar `projeler.json`). Projeye uygunluk kurulum sırasında (`--oner` / `--kuru`) incelenir.
 
 ## Skill ekleme akışı
-1. İhtiyacı netleştir: proje yolu, proje tipi, teknoloji, agent rolleri (bilinmiyorsa sor).
+1. İhtiyacı netleştir: proje yolu, proje tipi, teknoloji, agent rolleri ve hangi AI araçlarıyla açılacağı (Claude Code / Codex / Antigravity / Cursor / VS Code Copilot; Windows'ta açılacak mı). Cevaba göre --arac ortak ya da --arac yalniz-claude ver; rapordaki arac-duzeni, arac-gormez, arac-secimi-yok satırlarını kullanıcıya göster (rehber/14-yapay-zeka-araclari.md). Bilinmiyorsa sor.
 2. Öneri: `python3 araclar/skill-ekle.py <proje> --oner "<ihtiyaç>"` (tüm kütüphane taranır). Uygun profil/rolleri seç.
    Konuya uygun skiller arasında GitHub Trending'e girmiş olanları (`🔥trend`) öncele; trend tek başına seçim sebebi değildir.
 3. Ön kontrol: `python3 araclar/skill-ekle.py <proje> --profil <p> [--rol …] [--skill …] --kuru`
@@ -27,19 +29,20 @@
 5. Onay gelirse aynı komutu `--evet` ile çalıştır. Sonra `--dogrula` sonucunu bildir.
 
 ## Bakım isteklerinde
+- Oturum başı: kütüphane oturumunun ilk işi `python3 araclar/aylik-ozet.py --hizli` (salt okuma, ağsız); çıktıyı kullanıcıya iki cümleyle söyle. Aylık çalışma 35 günü aştıysa "Aylık çalışmayı şimdi yapayım mı?" diye sor; evet derse önce `python3 araclar/arsiv-guncelle.py --aylik --kuru`, sonra `rehber/02-guncelleme-yonergesi.md` yolu (`--uygula --dal`). `dikkat`/`sorun` varsa kendiliğinden düzeltme, silme, push yok. Ayrıntı: `BASLA.md`.
 - "Skilleri güncelle" (aylık) → `python3 araclar/arsiv-guncelle.py` (rapor) → `--uygula --dal` (güncelleme `guncelleme/YYYY-AA`
   dalında; master değişmez) → kullanıcıya dal özetini ve `notlar/guncelleme-gecmisi.md` kaydını göster → onay gelirse
   `--birlestir <dal>`. Sonra yeniden incelenecek skilleri incele, etkilenen projeler için `skill-ekle.py <proje> --durum` / `--guncelle --kuru`.
 - "Yeni skill ekledim, kontrol et" → kaynak: GitHub **"Yapay Zeka Skillleri"** listesi (tüm skill repoları tek listede).
   `python3 araclar/github-skill-listesi.py` ile YENİ repoları bul, `promptlar/07-yeni-skill-reposu-ekle.md` /
-  `rehber/03-yeni-skill-ekleme.md` adımlarını uygula: **çakışma kontrolü** (aynı ad, aynı iş, aynı repoda birden fazla sürüm, global'de
-  farklı sürüm) ve **ücret sınıflandırması** (`ucret-siniflandirma.json`) zorunlu; kullanıcı onayı olmadan kaynak ekleme.
+  `rehber/03-yeni-skill-ekleme.md` adımlarını uygula: **çakışma kontrolü** (aynı ad, aynı iş, aynı repoda birden fazla sürüm, aynı adlı kendi skill; genel klasörler boşaltıldıktan sonra "global'de farklı sürüm" maddesi geçersiz) ve
+  **ücret sınıflandırması** (`ucret-siniflandirma.json`) zorunlu; tek ekleme sırası `rehber/03-yeni-skill-ekleme.md` A1..A9, onay kaydı zorunlu; kullanıcı onayı olmadan kaynak ekleme.
 - Ücret: ücretsiz yol önce. `ucretli` = ücret ödemeden hiç kullanılamayan skill (ücretli servis sadece bir seçenekse `kismen`). Ücretli skill (`ucret: ucretli`) rol çekirdeğine ancak gerekçeyle (`ucretli_bilincli`); kurulum raporunda
   ücretli skilleri ayrıca belirt. Liste: `notlar/ucretli-skiller.md`.
 - Trend: `python3 araclar/github-trend.py --aday` → `notlar/github-trend.md` (trend'deki kaynaklar + aday skill repoları;
   adaylar onaysız eklenmez). Aylık güncelleme bunu otomatik çalıştırır.
 - Popüler skiller: `python3 araclar/populer-tarama.py` → `notlar/populer-skiller.md` (GitHub REST araması + adayda SKILL.md sayımı;
-  yıldız listesi/GraphQL ve trending sayfası okunamayan ortamlarda da çalışır). Adaylar onaysız eklenmez; karar `--karar`.
+  yıldız listesi/GraphQL ve trending sayfası okunamayan ortamlarda da çalışır). Adaylar onaysız eklenmez; karar `konu-takip.py --karar` (aşağıda "Aday kararları").
 - Konu takibi: `python3 araclar/konu-takip.py` (e-ticaret/Etsy, mobil… `kaynaklar.json` → `takip_konulari`) → `notlar/konu-takip.md`.
   Kullanıcı bir alan için "takip et" derse oraya konu ekle. Adaylar onaysız eklenmez; reddedileni `--karar` ile kaydet.
 - Proje kullanımı: hangi projenin hangi skili kullandığı `notlar/proje-kullanimi.md`'de (kaynak: projelerin `kilit.json`'u; elle
@@ -48,7 +51,14 @@
 - Ad ve çakışma: çıplak ad kendiliğinden el değiştirmez (yeni gelen `ad@kaynak` olur); aynı ad farklı işse eski kayıt `durum_elle`
   ile tercih sabitlenir; bilerek devir `kaynaklar.json` → `ad_devral` ve kullanıcı onayıyla. Repo GitHub'da taşınırsa `repo`
   güncellenir, eski ad `eski_adlar`'a yazılır. Ayrıntı: `rehber/09-ad-kimlik-ve-cakisma.md`.
-- Programlar (skill olmayan yapılar, ör. etsyotomasyon): kullanıcı "dahil et" deyince `programlar.json` kartı + `programlar/<ad>/kaynak/` sabit sürüm kopyası; takip `python3 araclar/program-denetim.py` → `notlar/program-denetimi.md`; güncelleme onayla. Projeye `skill-ekle.py` ile kurulmaz. Ayrıntı: `rehber/11-program-yonetimi.md`.
+- Programlar (skill olmayan yapılar: HyperFrames, OpenMontage, etsyotomasyon): `programlar.json` kartları; HyperFrames ve OpenMontage `kopya: yerinde` (bu bilgisayarda kurulu haliyle izlenir). Her güncelleme, geri alma ve kaldırma kullanıcının AYRI onayıyla ve önce yedekle yapılır: `rehber/11-program-yonetimi.md` → "Taze ajan: istek → adımlar", hazır istem `promptlar/13-program-kur-guncelle.md`. Önce `python3 araclar/program-denetim.py --oncesi <ad>` "HAZIR" demelidir. Projeye `skill-ekle.py` ile kurulmaz.
+- Proje takibi: aylık ya da "projeleri kontrol et" denince `python3 araclar/proje-kullanimi.py --saglik` (`notlar/proje-durumu.md`; projelere salt okuma, kayıtsız klasörleri de tarar). Yeni proje / çıkar / taşındı / yoksay: `--ekle`, `--cikar`, `--tasindi`, `--yoksay` (yalnız `projeler.json` değişir, önce plan, onayla `--evet`). Ayrıntı: `rehber/10-proje-kullanimi.md`, `promptlar/12-proje-kullanimi-ve-etki.md`.
+- Git ve yedek: `araclar/git-durum.py`, `araclar/yedek-denetim.py` (salt okuma); yedek ve geri alma kuralı `rehber/13-yedek-ve-geri-alma.md`. Her yedek `yedekler.json`'a kaydedilir. Push yalnız kullanıcı isteyince.
+- Genel klasörler: beklenmeyen girdi ya da boşaltma için `python3 araclar/genel-bekci.py` (yalnız okur, hiçbir şeyi silme). Boşaltma yalnız `rehber/12-genel-klasor-bosaltma.md` ile, her adım ayrı onayla; hazır istem `promptlar/16-genel-klasor-bosaltma.md`.
+- Kaynak/skill çıkarma, emekli, kayıp kaynak: `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` (yalnız okur: etki + sıralı adımlar + geri alma); onayla uygula. Ayrıntı: `rehber/03-yeni-skill-ekleme.md` bölüm D-G, `promptlar/14-kaynak-cikar.md`.
+- Aday kararları: `python3 araclar/konu-takip.py --karar owner/ad eklendi|reddedildi|izle "neden"` (`populer-tarama.py --karar` kullanma); bekleyenler: `python3 araclar/konu-takip.py --bekleyenler` (üç kaynağı özetler).
+- Yeni AI aracı: `rehber/14-yapay-zeka-araclari.md` bölüm 7 ve `promptlar/15-yeni-yapay-zeka-araci.md`; aylık araç belgesi kontrolü: `python3 araclar/skill-ekle.py --araclar`.
+- `CLAUDE.md` ve `AGENTS.md` birebir aynı tutulur: birini değiştirince `cp CLAUDE.md AGENTS.md`; `dogrula.py` farkı HATA sayar.
 - Eski sürümler: bilerek çıkarılan skiller `kaynaklar.json` → `arsivden_cikarilanlar`.
 - Hazır promptlar: `promptlar/` (kullanıcıya proje başlangıcı, ekleme, güncelleme, bakım için).
 - Her değişiklikten sonra: `python3 araclar/kapsam-denetimi.py` (0 sorun) ve `python3 araclar/dogrula.py` (0 hata), sonra `git commit`.
```
