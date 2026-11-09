# SkillKutuphanesi — Agent Talimatı

Bu klasör kullanıcının skill kütüphanesidir. Kullanıcı "şu projeye / şu agent'lara skill ekle" dediğinde aşağıdaki
akışı **atlamadan** izle. Ayrıntı: `rehber/01-skill-ekleme-sureci.md`, `rehber/04-kontrol-listesi.md`.

## Kesin kurallar
1. Global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) **asla** yazma,
   kopyalama, symlink koyma ya da silme. Skiller sadece kullanıcının verdiği proje klasörüne, sadece `skill-ekle.py` ile kurulur.
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
1. İhtiyacı netleştir: proje yolu, proje tipi, teknoloji, agent rolleri (bilinmiyorsa sor).
2. Öneri: `python3 araclar/skill-ekle.py <proje> --oner "<ihtiyaç>"` (tüm kütüphane taranır). Uygun profil/rolleri seç.
   Konuya uygun skiller arasında GitHub Trending'e girmiş olanları (`🔥trend`) öncele; trend tek başına seçim sebebi değildir.
3. Ön kontrol: `python3 araclar/skill-ekle.py <proje> --profil <p> [--rol …] [--skill …] --kuru`
4. Raporu kullanıcıya göster: kurulacak skiller, roller, HATA/UYARI/BİLGİ satırları ve `ek-aday` listesi
   (kütüphanede ilgili olup seçilmeyen skiller). HATA varsa nedenini ve seçenekleri açıkla, kurma.
5. Onay gelirse aynı komutu `--evet` ile çalıştır. Sonra `--dogrula` sonucunu bildir.

## Bakım isteklerinde
- "Skilleri güncelle" (aylık) → `python3 araclar/arsiv-guncelle.py` (rapor) → `--uygula --dal` (güncelleme `guncelleme/YYYY-AA`
  dalında; master değişmez) → kullanıcıya dal özetini ve `notlar/guncelleme-gecmisi.md` kaydını göster → onay gelirse
  `--birlestir <dal>`. Sonra yeniden incelenecek skilleri incele, etkilenen projeler için `skill-ekle.py <proje> --durum` / `--guncelle --kuru`.
- "Yeni skill ekledim, kontrol et" → kaynak: GitHub **"Yapay Zeka Skillleri"** listesi (tüm skill repoları tek listede).
  `python3 araclar/github-skill-listesi.py` ile YENİ repoları bul, `promptlar/07-yeni-skill-reposu-ekle.md` /
  `rehber/03-yeni-skill-ekleme.md` adımlarını uygula: **çakışma kontrolü** (aynı ad, aynı iş, aynı repoda birden fazla sürüm, global'de
  farklı sürüm) ve **ücret sınıflandırması** (`ucret-siniflandirma.json`) zorunlu; kullanıcı onayı olmadan kaynak ekleme.
- Ücret: ücretsiz yol önce. `ucretli` = ücret ödemeden hiç kullanılamayan skill (ücretli servis sadece bir seçenekse `kismen`). Ücretli skill (`ucret: ucretli`) rol çekirdeğine ancak gerekçeyle (`ucretli_bilincli`); kurulum raporunda
  ücretli skilleri ayrıca belirt. Liste: `notlar/ucretli-skiller.md`.
- Trend: `python3 araclar/github-trend.py --aday` → `notlar/github-trend.md` (trend'deki kaynaklar + aday skill repoları;
  adaylar onaysız eklenmez). Aylık güncelleme bunu otomatik çalıştırır.
- Konu takibi: `python3 araclar/konu-takip.py` (e-ticaret/Etsy, mobil… `kaynaklar.json` → `takip_konulari`) → `notlar/konu-takip.md`.
  Kullanıcı bir alan için "takip et" derse oraya konu ekle. Adaylar onaysız eklenmez; reddedileni `--karar` ile kaydet.
- Eski sürümler: bilerek çıkarılan skiller `kaynaklar.json` → `arsivden_cikarilanlar`.
- Hazır promptlar: `promptlar/` (kullanıcıya proje başlangıcı, ekleme, güncelleme, bakım için).
- Her değişiklikten sonra: `python3 araclar/kapsam-denetimi.py` (0 sorun) ve `python3 araclar/dogrula.py` (0 hata), sonra `git commit`.
- GitHub: kütüphane `ulukayasaban/SkillKutuphanesi` deposunda **private** (varsayılan dal `master`). Push ve PR **sadece kullanıcı
  isteyince**; depoyu public yapma. Aylık güncelleme PR'ı GitHub'da birleştirilmez: onaydan sonra yerelde `--birlestir`, sonra
  `git push origin master`. Ayrıntı: README "GitHub deposu (private)", `rehber/02-guncelleme-yonergesi.md`.
