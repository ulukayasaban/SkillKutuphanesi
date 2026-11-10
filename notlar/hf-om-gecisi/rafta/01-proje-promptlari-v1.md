# Proje promptları (HyperFrames + OpenMontage geçişi)

Bu promptlar **projenin kendi oturumunda** kullanılır: projeyi aç, ilgili bloğu kopyala, yapıştır.
Ana plan: [00-plan.md](00-plan.md). Adım ve karar numaraları oradaki numaralardır.

## Nasıl kullanılır

1. Her projede önce **A (sadece oku ve raporla)** promptu çalışır. Projenin hiçbir dosyası değişmez.
2. Rapor `~/Documents/Claude/hf-om-raporlar/` klasörüne yazılır. Bu klasörü ilk iş olarak **kütüphane oturumu** açar
   (00-plan, adım 1.0); böylece proje oturumları sadece dosya yazar. Klasör yine de yoksa proje oturumu onu oluşturabilir.
   Rapor gelince kütüphane oturumuna dön ve "X projesinin raporu geldi" de; raporu ben okurum, sana kısa bir özet ve karar
   listesi çıkarırım.
3. **B (onaylı onarım)** promptu ancak tam yedek alındıktan (00-plan, adım 1.2 ve 1.3) ve sen raporu görüp neyin
   düzeltileceğini seçtikten sonra kullanılır.
4. **C (doğrulama)** her değişiklikten sonra çalışır.
5. Skill kurmak ya da güncellemek gerekiyorsa bunu proje oturumu yapmaz; **kütüphane oturumu** `skill-ekle.py` ile yapar.

| Sıra | Proje | Promptlar | Dalga 1'de değişiklik |
|---|---|---|---|
| 1 | IstatistikYoutube | 1A, 1C | Üretim hattında yok. Onaylarsan taban testi kendi test klasörüne ve HyperFrames önbelleğine test çıktısı yazar. |
| 2 | Akıl Dışı Youtube Kanalı | 2A, 2A-Codex, 2B, 2C | Sadece onayladığın onarımlar. Skill kurulumu Dalga 2'de. |
| 3 | Psikolojik Danışman Sosyal Medya | 3A, 3B | Sadece yol düzeltmesi (onaylarsan; karar 11) |
| 4 | blenderTest ve diğerleri | 4A | Yok |
| 5 | Etsy-Arif | 5A | Yok (Arif'in deposu; sadece bilgi) |

Her promptun başındaki **KURALLAR** bloğu bilerek tekrar ediyor; promptlar tek başına kopyalanabilsin diye.

---

## 1A — IstatistikYoutube: oku ve raporla

Klasör: `~/Documents/IstatistikYoutube`

```kopyala
Bu projede HyperFrames ve OpenMontage ile ilgili bir düzenleme öncesi durum raporu istiyorum. Bu oturumda üretim hattının
hiçbir davranışı değişmeyecek.

KURALLAR (oturumun tamamında geçerli):
- Hiçbir dosyayı değiştirme, silme, taşıma, yeniden adlandırma. Yazacağın tek şey en alttaki rapor dosyasıdır;
  ~/Documents/Claude/hf-om-raporlar/ klasörü yoksa onu da oluşturabilirsin.
- TEK İSTİSNA (taban testi): duman.sh (bayraklı ya da bayraksız) kendi test çıktı klasörü tools/kurgu/_test/duman-cikti altını
  silip yeniden yazar, render sırasında tools/kurgu/_calisma/render.kilit dosyasına dokunur ve hyperframes tarayıcı önbelleği
  ~/.cache/hyperframes'i kullanır. Bunlar testin kendi yazdığı yerlerdir; ben onay verirsem bu yazmalar serbest, başka hiçbir
  yere yazma.
- Şu klasörlere hiç yazma: ~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage, ~/.hyperframes.
  ~/.cache/hyperframes klasörüne kendin elle yazma (yalnızca onayladığım duman.sh çalışırken hyperframes'in kendi kullanımı serbest).
- Şu komutları çalıştırma: hyperframes update / upgrade / init / clean / "skills update" / "skills check"; "npx skills"; npm install;
  npx ile yeni paket indirme; pip install; uv pip install; make setup; ~/.openmontage içinde herhangi bir git komutu.
- hyperframes ile kendiliğinden yalnızca --version ve --help çalıştırabilirsin. Render, check, preview ya da test betiği
  çalıştırmadan önce bana sor.
- .claude/settings.local.json içindeki skillOverrides ayarını değiştirme.
- .env dosyalarının içeriğini okuma, yazdırma; yalnızca var olduğunu söyle.
- Git commit, push, dal işlemi yapma.
- Emin olmadığın şeyi tahmin etme; "doğrulanmadı" yaz.

YAPILACAKLAR (taban testi dışında yalnızca okuma):
1. Taban testi: duman.sh betiğini bul ve oku. Çalıştırmadan önce bana tek paragrafta anlat:
   - bayraksız çalışınca ne yapıyor (beklenen: kur.py --check ile kontrol ve anlık görüntü; duman-cikti klasörünü silip yeniden üretir),
   - "--hf" eklenince ne ekleniyor (beklenen: yaklaşık 3 saniyelik bir render; render kilidine dokunur),
   - tahmini süre (beklenen: bayraksız birkaç dakika, --hf ile yaklaşık 1 dakika daha),
   - bugünkü çıktı klasörünün boyutu (du -sh ile).
   Betikte gördüğün bu beklentilerden farklıysa farkı yaz. Bayraksız çalıştırma için AYRI, "--hf" için AYRI onayımı iste.
   Onaylarsam şu ortam ayarlarıyla çalıştır:
   HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_AUTO_INSTALL=1 HYPERFRAMES_NO_UPDATE_CHECK=1
   Sonucu (kaç geçti / kaç kaldı, hyperframes sürümü, tarih) yaz ve daha önceki kayıtla (0.9.20 sürümünde 94 geçti / 0 kaldı)
   karşılaştır.
2. .claude/settings.local.json içindeki skillOverrides adlarını ~/.claude/skills içindeki adlarla karşılaştır:
   (a) artık genel klasörde olmayan adlar, (b) genel klasörde olup kapatılmamış adlar. Sadece listele.
3. Proje içinde "~/.openmontage/.venv/bin/python" (ya da tam yolu) geçen dosyaları say ve klasör bazında dök.
4. Proje içinde ~/.claude/skills/, ~/.agents/skills/ ya da ~/.codex/skills/ ile başlayan (ya da /Users/sabanulukaya/… tam yoluyla
   yazılmış) HER yolu "dosya:satır" olarak listele. Kodun çalıştırdığı yerleri (.py, .sh, .mjs) "ÇALIŞIR", yalnızca metinde
   geçenleri "OKUMA TALİMATI" diye işaretle. Her yol için: aynı skill projenin içinde de var mı?
5. hyperframes komutunun çağrıldığı yerleri listele: çıplak "hyperframes" mi, "npx hyperframes" mi, sürüm yazılmış mı.
6. .claude/skills içindeki skillerden .skill-kutuphanesi/kilit.json içinde kaydı OLMAYANLARI listele (ad, dosya sayısı).
   Bunlar projenin kendi skilleridir; dokunma.
7. Proje içindeki skill adlarından hangileri ~/.claude/skills içinde de aynı adla var? Her biri için içerik aynı mı farklı mı
   (KAYNAK.md ve .DS_Store hariç karşılaştır)? Farklıysa farklı olan dosyaların adlarını da yaz (yalnızca "hyperframes" için
   değil, aynı adlı her skill için).
8. Devir notlarından ya da günlüklerden bu projede hangi hyperframes sürümlerinin kullanıldığını özetle.

RAPOR: sonucu ~/Documents/Claude/hf-om-raporlar/istatistikyoutube.md dosyasına yaz (klasör yoksa oluştur). Yazamıyorsan sohbete yaz.
Biçim: önce 5 satırlık özet; sonra her bulgu için "bulgu · neyi etkiler · önerin · nasıl geri alınır" tablosu; en sonda
"doğrulanmadı" listesi. Hiçbir öneriyi uygulama.
```

## 1C — IstatistikYoutube: değişiklik sonrası doğrulama

Ne zaman: kütüphane oturumu bu projeye skill kurduktan (Dalga 2, adım 2.1) ya da bilgisayar genelinde bir paket taşındıktan
(adım 2.3) sonra.

```kopyala
Bu projede kütüphane oturumundan bir değişiklik yapıldı. Hiçbir dosyayı değiştirmeden doğrula.
KURALLAR: 1A promptundaki kuralların aynısı geçerli (dosya değiştirme yok; genel skill klasörlerine ve ~/.openmontage'a yazma yok;
hyperframes update / upgrade / init / clean / skills update ve her türlü kurulum komutu yasak; yazacağın tek şey rapor dosyası).

1. python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --dogrula   → sonucu aynen yaz.
2. Skill listende şu adlar görünüyor mu, her biri hangi klasörden geliyor:
   - projeye kurulanlar: hyperframes, hyperframes-cli, hyperframes-core, hyperframes-animation, motion-graphics
   - genel klasörde kalanlar (oradan gelmesi normal): design-dna, openmontage, nlm-skill
   Genel kopya hâlâ duruyorsa aynı adlı skilin genel klasörden görünmesi normaldir; yalnızca yaz, düzeltme.
3. Onayımla taban testini (duman.sh, sonra duman.sh --hf) aynı ortam ayarlarıyla yeniden çalıştır ve 1A'daki sonuçla karşılaştır.
   (1A madde 1'deki istisna ve "bayraksız için ayrı, --hf için ayrı onay" kuralı aynen geçerli: test yalnızca
   tools/kurgu/_test/duman-cikti, tools/kurgu/_calisma/render.kilit ve ~/.cache/hyperframes'e yazar.)
4. OpenMontage Python ortamını kullanan betiklerden bana göstereceğin kısa bir tanesinin hâlâ çalıştığını (onayımla) göster.
Sonucu ~/Documents/Claude/hf-om-raporlar/istatistikyoutube-dogrulama.md dosyasına yaz. Klasör yoksa oluştur. Yazamıyorsan sohbete yaz.
Fark varsa hiçbir şeyi düzeltme; bana bildir.
```

---

## 2A — Akıl Dışı Youtube Kanalı: oku ve raporla (Claude Code)

Klasör: `~/Documents/Akil Disi Youtube Kanali`

```kopyala
Bu projede HyperFrames ve OpenMontage ile ilgili bir düzenleme öncesi durum raporu istiyorum. Bu oturumda yalnızca OKU.

KURALLAR (oturumun tamamında geçerli):
- Hiçbir dosyayı değiştirme, silme, taşıma, yeniden adlandırma. Yazacağın tek şey en alttaki rapor dosyasıdır;
  ~/Documents/Claude/hf-om-raporlar/ klasörü yoksa onu da oluşturabilirsin (tek istisna).
- Hiçbir betiği, kompozisyonu, hyperframes.json dosyasını ya da "akil-disi-" ile başlayan skili silme, yeniden adlandırma.
- Şu klasörlere hiç yazma: ~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage, ~/.hyperframes, ~/.cache/hyperframes.
- Şu komutları çalıştırma: hyperframes update / upgrade / "upgrade --project" / init / clean / "skills update" / "skills check";
  "npx skills"; npm install; npx ile paket indirme; pip install; make setup; render; hyperframes check.
- hyperframes ile yalnızca --version ve --help çalıştırabilirsin.
- Bağlantıları (symlink) incelerken "find -L" KULLANMA (kendine dönen bağlantı var); "find -type l" ve "readlink" kullan.
- .env dosyalarının içeriğini okuma. Git commit, push, dal işlemi yapma.
- Emin olmadığın şeyi tahmin etme; "doğrulanmadı" yaz.

YAPILACAKLAR (yalnızca okuma):
1. .agents/skills ve .claude/skills içindeki bütün bağlantıları listele: adı, yazılı hedefi, hedef var mı. Kırık olanları ve
   birbirini gösteren (kendine dönen) bağlantıları ayrıca işaretle.
2. .codex/agents/*.toml dosyalarının her birinde yazılı skill yollarını çıkar. Her yol için: dosya var mı, yol projenin içinde mi
   yoksa bilgisayarın genelindeki bir klasörde mi (~/.codex/skills, ~/.agents/skills, ~/.claude/skills). Aynı skill projenin
   .agents/skills klasöründe var mı; varsa hangi klasör adıyla (ad farklı olabilir, örneğin sonunda "--kutuphane")?
3. 02_Operasyon/BECERI-KULLANIM-PLANI.json (ana dosya) ve AGENTS.md içindeki skill yollarını gerçek durumla karşılaştır.
   02_Operasyon/Oncelik_Uygulamasi_20261025/onceki/ altındaki aynı adlı kopya eski yedektir; yalnızca oku ve ayrı satırda raporla.
4. İçinde ".npm/_npx/" geçen bütün dosyaları listele (klasör bazında say). Her biri için: hangi hyperframes yolunu çağırıyor, o yol
   bugün var mı, dosya en son ne zaman değişti. Hangilerinin hâlâ kullanıldığını dosya tarihlerinden ve devir notlarından tahmin et;
   tahmin olduğunu belirt.
5. Bütün package.json ve .sh dosyalarındaki "hyperframes@" sürüm yazımlarını listele (dosya, sürüm).
5b. İçinde ".npm/_npx/" geçen her .py, .sh ve .md dosyası için bir tablo yap: dosya yolu · satır · komutun biçimi (örneğin
   ['node', '…/cli.js', 'render', …]) · en yakın package.json'ın yolu ve içinde yazılı hyperframes sürümü. Yakında package.json
   ya da sürüm yoksa "sürüm yok" yaz; sürümü tahmin etme.
6. Bütün hyperframes.json dosyalarındaki authoringSkill değerlerini listele. Bu adlar projenin içinde skill olarak var mı,
   yoksa yalnızca bilgisayarın genelinde mi duruyor?
7. .skill-kutuphanesi/kilit.json içinde kaydı OLMAYAN skilleri listele (ad, dosya sayısı, içerik özeti/sha256). "akil-disi-" ile
   başlayanlar projenin kendi skilleridir; dokunma.
8. Projedeki skill adlarından hangileri ~/.claude/skills ya da ~/.agents/skills içinde de aynı adla var? Her biri için: içerik
   aynı mı farklı mı (KAYNAK.md ve .DS_Store hariç), hangisi yeni, farklı olan dosyaların adları. (Yalnızca "hyperframes" için
   değil, aynı adlı her skill için.)
9. "~/.openmontage" geçen dosyaları say ve klasör bazında dök.
10. Proje içinde ~/.claude/skills/, ~/.agents/skills/ ya da ~/.codex/skills/ ile başlayan (ya da /Users/sabanulukaya/… tam yoluyla
    yazılmış) HER yolu "dosya:satır" olarak listele. Kodun çalıştırdığı yerleri (.py, .sh, .mjs) "ÇALIŞIR", yalnızca metinde
    geçenleri "OKUMA TALİMATI" diye işaretle. Her yol için: aynı skill projenin içinde de var mı?

RAPOR: ~/Documents/Claude/hf-om-raporlar/akil-disi.md dosyasına yaz (klasör yoksa oluştur). Yazamıyorsan sohbete yaz.
Biçim: önce 5 satırlık özet; sonra her sorun için "sorun · bugün neyi bozuyor · düzeltilmezse ne olur · önerilen düzeltme ·
nasıl geri alınır" tablosu; önerilen sıra; en sonda "doğrulanmadı" listesi. Hiçbir öneriyi uygulama.
```

## 2A-Codex — Akıl Dışı: aynı proje, Codex tarafı

Codex'te bu projeyi açıp yapıştır. Amaç: Codex'in skilleri gerçekte nereden yüklediğini öğrenmek.

```kopyala
Bu oturumda hiçbir dosyayı değiştirme, hiçbir kurulum ya da güncelleme komutu çalıştırma (hyperframes update/upgrade/init/clean,
"skills update", "npx skills", npm install, pip install yasak). Yalnızca şunları cevapla:
1. Şu anda kullanabildiğin skillerin tam listesi: her biri için ad ve yüklendiği klasörün tam yolu.
2. Aynı adda birden fazla skill görüyorsan hangileri, hangi klasörlerden?
3. .codex/agents/ altındaki ajan tanımlarında yazılı skill yollarını oku. Her yol için: dosya var mı ve o ajan çalışırken bu skili
   gerçekten yükleyebiliyor mu? Yükleyemediklerini ayrıca listele.
4. ~/.codex/skills klasöründeki skilleri görüyor musun? ~/.agents/skills klasöründekileri?
Sonucu sohbete yaz; emin olmadığın yere "doğrulanmadı" yaz.
```

## 2B — Akıl Dışı: onaylı onarım

Ne zaman: tam yedek alındıktan (00-plan 1.2 ve 1.3), 2A raporunu gördükten ve kütüphane oturumunda neyin düzeltileceğine karar
verdikten sonra (karar 10 dahil). Köşeli parantezli yerleri doldur:
- `[EŞLEME TABLOSU]`: kütüphane oturumunun verdiği "genel yol → projedeki yol" tablosu (taslağı 00-plan, adım 2.1'de).
- `[GİRİŞ ADI]`: 2A raporundaki, yolu var olmayan girişin adı.
- `[BETİK LİSTESİ]`: yalnızca hâlâ kullandığın betikler, 2A raporundaki sürümleriyle.

```kopyala
Bu projede yalnızca aşağıda yazdığım onarımları yap. Listede olmayan hiçbir şeye dokunma.

Başlamadan önce kütüphane oturumunun aldığı tam yedeğin (~/Documents/Claude/yedek/makine-2026-11-10/ altında bu projenin kopyası)
var olduğunu bana göster; yoksa hiçbir dosyaya dokunma.

KURALLAR:
- Değiştireceğin her dosyanın önce yanına aynı klasörde ".yedek-YYYYMMDD-HHMMSS" (tarih ve saat) uzantılı kopyasını al. Aynı adda
  bir yedek varsa üzerine ASLA yazma; yeni saatle yeni yedek al. Her dosyanın ilk dokunuştan önceki sha256 değerini rapor
  dosyasına yaz.
- Hiçbir dosyayı silme, taşıma, yeniden adlandırma. Hiçbir kompozisyonu, hyperframes.json dosyasını, "akil-disi-" skilini değiştirme.
- Skill klasörlerine (.agents/skills, .claude/skills) elle dosya kopyalama ya da bağlantı kurma; skill işi kütüphane oturumundan yapılır.
- hyperframes-creative bağlantı çiftine dokunma; bunun onarımı kütüphane oturumundandır.
- Başında "skill-kutuphanesi tarafından üretildi" yazan dosyaları ve "skill-kutuphanesi:basla / bitir" işaretleri arasındaki
  bölümleri elle düzeltme; onları bana bildir (kütüphane oturumundan yeniden üretilir).
- Genel klasörlere (~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage) yazma.
- hyperframes update / upgrade / init / clean / "skills update", "npx skills", npm install, pip install, render çalıştırma.
- Her onarımdan önce "şu dosyada şu satır şuna dönüşecek" diye göster ve onayımı bekle.

ONARIMLAR:
1. [EVET/HAYIR] .codex/agents/*.toml içindeki, bilgisayarın geneline giden skill yollarını aşağıdaki eşleme tablosuna göre projenin
   içindeki karşılığına çevir:
   [EŞLEME TABLOSU — kütüphane oturumundan]
   Yalnızca tabloda yazan ve hedefi projede BUGÜN var olan yolları çevir (hedef gerçek klasör olmalı; kırık ya da kendine dönen
   bağlantı olmamalı; içinde SKILL.md bulunmalı). Tabloda olmayan ya da hedefi olmayan yollara dokunma; listele (kütüphane
   oturumundan kurulacak). Adları kendin eşleştirme, tahmin etme.
2. [EVET/HAYIR] 02_Operasyon/BECERI-KULLANIM-PLANI.json içindeki var olmayan [GİRİŞ ADI — 2A raporundan al] girişinin yolunu
   projedeki doğru yola çevir. 02_Operasyon/Oncelik_Uygulamasi_20261025/onceki/ altındaki kopyaya dokunma.
3. [EVET/HAYIR] Ölü ".npm/_npx/…/hyperframes/dist/cli.js" yolu geçen betikler için: sürümü SEN seçme ve tahmin etme. 2A
   raporundaki 5b tablosunda sürümü yazılı olan betiklerde yalnızca o yol dizgisini "npx --yes hyperframes@<rapordaki sürüm>"
   ile değiştir; Python listesinin yapısını (öğe sayısı, sırası, diğer argümanlar) değiştirme, yeni kod ekleme. Sürümü raporda
   olmayan betiklere dokunma, listele; sürümü bana sorarsın. Her dosya için "şu satır şuna dönüşecek" göster, onayımı bekle.
   .md dosyalarını (README, notlar) bu onarımın dışında bırak; yalnızca listele.
   [BETİK LİSTESİ — yalnızca hâlâ kullandıkların, sürümüyle birlikte]
   Listede olmayan betiklere dokunma.

Bitince: değişen dosyaların listesini, her birinin yedeğinin adını, ilk dokunuştan önceki sha256 değerini ve "geri almak için şu
yedeği eski adına geri kopyala" satırını ~/Documents/Claude/hf-om-raporlar/akil-disi-onarim.md dosyasına yaz. Klasör yoksa oluştur.
Yazamıyorsan sohbete yaz.
```

## 2C — Akıl Dışı: doğrulama

```kopyala
Hiçbir dosyayı değiştirmeden doğrula (kurulum, güncelleme, render komutu yok; yazacağın tek şey rapor dosyası):
1. python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --dogrula   → sonucu aynen yaz.
2. .codex/agents/*.toml içindeki her skill yolu için: dosya var mı; gerçek dosya mı (kırık ya da kendine dönen bağlantı değil mi);
   yol projenin içinde mi. Hâlâ bilgisayarın geneline giden yolları ayrı listele (bunlar henüz kurulmamış skillerin yolları olabilir).
3. .agents/skills ve .claude/skills içinde kırık ya da kendine dönen bağlantı kaldı mı (hyperframes-creative çifti dahil;
   "find -L" kullanma)?
4. hyperframes.json dosyalarındaki authoringSkill adları projenin içinde skill olarak var mı?
5. "akil-disi-" skillerinin sayısı ve içerik özetleri 2A raporundakiyle aynı mı?
Sonucu ~/Documents/Claude/hf-om-raporlar/akil-disi-dogrulama.md dosyasına yaz. Klasör yoksa oluştur. Yazamıyorsan sohbete yaz.
Fark varsa düzeltme; bana bildir.
```

---

## 3A — Psikolojik Danışman Sosyal Medya: oku ve raporla

Klasör: `~/Documents/Psikolojik Danışman Sosyal Medya`

```kopyala
Bu projede OpenMontage bağlantısının durumunu raporla. Bu oturumda yalnızca OKU.

KURALLAR:
- Hiçbir dosyayı değiştirme, silme, taşıma. Yazacağın tek şey en alttaki rapor dosyasıdır; ~/Documents/Claude/hf-om-raporlar/
  klasörü yoksa onu da oluşturabilirsin (tek istisna).
- OpenMontage kurulumu, git, pip, npm, npx, make çalıştırma. ~/.openmontage ve genel skill klasörlerine yazma.
- .env dosyasının içeriğini OKUMA; yalnızca var olduğunu ve kaç satır olduğunu yaz.
- Git commit, push yapma. Emin olmadığın yere "doğrulanmadı" yaz.

YAPILACAKLAR:
1. OpenMontage'a atıf yapan bütün yerleri tablo yap: dosya, satır, yazılı yol ya da sürüm. (config/tools.yaml,
   config/openmontage-entegrasyon.md, .claude/skills/openmontage-adapter, .claude/agents/reels-kurgucu.md, ajan hafıza dosyaları,
   Vault içindeki araç durumu notu ve bulduğun diğerleri.) Her satırı üç sınıftan birine koy:
   "değiştirilecek" (hattın bugün okuduğu ayar ya da talimat) · "geçmiş kayıt, dokunulmayacak" (Uretim/ ve Vault/ altındaki
   eski kayıt ve notlar) · "skill, bildirilecek" (.claude/skills/ altındaki her şey).
2. Her yol için bugün var mı: /Users/sabanulukaya/Documents/OpenMontage (yok olmalı), /Users/sabanulukaya/.openmontage (var olmalı).
3. Projenin beklediği OpenMontage sürümü (kayıtlı commit) ne? Kurulu sürüm c806645; fark bir sorun yaratır mı, hangi araçlar için?
4. Reels hattı en son ne zaman çalıştı, çıktılar hangi klasörde?
5. .claude/skills içindeki skilleri listele; hangileri projenin kendi skili (başka yerde kopyası yok)?
6. Proje içinde ~/.claude/skills/, ~/.agents/skills/ ya da ~/.codex/skills/ ile başlayan (ya da /Users/sabanulukaya/… tam yoluyla
   yazılmış) HER yolu "dosya:satır" olarak listele. Kodun çalıştırdığı yerleri (.py, .sh, .mjs) "ÇALIŞIR", yalnızca metinde
   geçenleri "OKUMA TALİMATI" diye işaretle. Her yol için: aynı skill projenin içinde de var mı?

RAPOR: ~/Documents/Claude/hf-om-raporlar/psikolojik-danisman.md dosyasına yaz. Klasör yoksa oluştur. Yazamıyorsan sohbete yaz.
Biçim: özet; "yer · bugünkü değer · olması gereken · sınıfı · nasıl geri alınır" tablosu; iki seçenek için öneri: (a) yolları
~/.openmontage olarak düzelt, (b) hattı "pasif" diye işaretle. Hiçbir öneriyi uygulama.
```

## 3B — Psikolojik Danışman: yol düzeltmesi (onaylarsan)

Ne zaman: tam yedek alındıktan (00-plan 1.2 ve 1.3) ve karar 11'de "hat aktif, yol düzeltilsin" dedikten sonra.

```kopyala
3A raporundaki tabloya göre yalnızca OpenMontage yolunu düzelt: /Users/sabanulukaya/Documents/OpenMontage →
/Users/sabanulukaya/.openmontage. Başka hiçbir şeyi değiştirme.

Başlamadan önce kütüphane oturumunun aldığı tam yedeğin (~/Documents/Claude/yedek/makine-2026-11-10/ altında bu projenin kopyası)
var olduğunu bana göster; yoksa hiçbir dosyaya dokunma.

DEĞİŞTİRİLECEK DOSYALAR (yalnızca bunlar): config/openmontage-entegrasyon.md, config/tools.yaml, .claude/agents/reels-kurgucu.md,
.claude/agent-memory/reels-kurgucu/project_openmontage-varsayilan.md. Bu liste 3A raporuyla uyuşmuyorsa dur ve bana sor.

DOKUNULMAYACAKLAR: Uretim/ altındaki geçmiş üretim kayıtları, Vault/ altındaki notlar (Araç Durumu.md, Agent Team Yapısı.md dahil)
ve .claude/skills/ altındaki her şey. Bunlarda eski yol geçiyorsa değiştirme; sadece dosya adı ve satır numarasıyla rapora
"bana bildirildi" diye yaz.

KURALLAR:
- Değiştireceğin her dosyanın önce yanına aynı klasörde ".yedek-YYYYMMDD-HHMMSS" (tarih ve saat) uzantılı kopyasını al. Aynı adda
  bir yedek varsa üzerine ASLA yazma; yeni saatle yeni yedek al. Her dosyanın ilk dokunuştan önceki sha256 değerini rapor
  dosyasına yaz. Yedek aldığın dosyaların listesini tut.
- Toplu değiştirme (sed, replace-all) kullanma; dosya dosya, satır satır ilerle. Değişecek her satırı önce göster, onayımı bekle.
- Başında "skill-kutuphanesi tarafından üretildi" yazan dosyaları ve "skill-kutuphanesi:basla / bitir" işaretleri arasını elle
  düzeltme; bana bildir.
- OpenMontage'ı kurma, güncelleme; git, pip, npm, make çalıştırma; .env içeriğini okuma.
- Kayıtlı sürüm numarasını (commit) değiştirme; yalnızca "kurulu sürüm c806645, kayıtlı sürümden farklı" notunu rapora ekle.
- Bu proje git deposu değil; tek geri alma yolu yedeklerdir.

Bitince proje içinde "Documents/OpenMontage" geçen yer kaldı mı diye ara (".yedek-" ile başlayan uzantılı dosyaları aramanın
dışında tut) ve sonucu yaz. Sonra şunları ~/Documents/Claude/hf-om-raporlar/psikolojik-danisman-onarim.md dosyasına yaz (klasör
yoksa oluştur; yazamıyorsan sohbete yaz): değişen dosyalar; her birinin ".yedek-…" adı ve sha256 değeri; her biri için "geri almak
için şu yedeği eski adına geri kopyala" satırı; dokunulmayan ama bana bildirilen yerlerin listesi.
```

---

## 4A — blenderTest ve diğer projeler: skill dökümü

Kullanılacağı klasörler: `blenderTest`, `Etsy-Yeni`, `AntigravityTest2`, `IsBasvuruClaude`, `Yetisio`,
`Tekfen Araştırma Sonuçları`, `IstatistikYoutube-Arsiv` (hepsi `~/Documents` altında). `[AD]` yerine kısa bir proje adı yaz.

```kopyala
Bu proje klasöründeki skillerin dökümünü çıkar. Bu oturumda yalnızca OKU.

KURALLAR:
- Hiçbir dosyayı değiştirme, silme, taşıma. Yazacağın tek şey en alttaki rapor dosyasıdır; ~/Documents/Claude/hf-om-raporlar/
  klasörü yoksa onu da oluşturabilirsin (tek istisna).
- Genel klasörlere (~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage) yazma. Kurulum ya da güncelleme komutu
  çalıştırma (npm, npx, pip, hyperframes update/upgrade/init/clean, "skills update"). Git işlemi yapma.
- Bağlantıları incelerken "find -L" kullanma. .env içeriği okuma.

YAPILACAKLAR:
1. .claude/skills, .agents/skills ve skills/ altındaki her skill için: ad, gerçek klasör mü bağlantı mı, bağlantıysa hedefi ve hedef
   var mı, dosya sayısı, (varsa) KAYNAK.md'deki kaynak ve sürüm.
2. .skill-kutuphanesi/kilit.json var mı? Varsa kilitte olup klasörde olmayan ve klasörde olup kilitte olmayan skiller.
3. Kırık ve kendine dönen bağlantılar.
4. "hyperframes", "openmontage", ".npm/_npx" ve "~/.openmontage" geçen dosyaların sayısı (klasör bazında).
5. Buradaki skill adlarından hangileri ~/.claude/skills içinde de aynı adla var; içerik aynı mı farklı mı? Farklıysa farklı olan
   dosyaların adları.
6. Başka hiçbir yerde kopyası olmadığını düşündüğün (projeye özel) skiller.
7. Proje içinde ~/.claude/skills/, ~/.agents/skills/ ya da ~/.codex/skills/ ile başlayan (ya da /Users/sabanulukaya/… tam yoluyla
   yazılmış) HER yolu "dosya:satır" olarak listele. Kodun çalıştırdığı yerleri (.py, .sh, .mjs) "ÇALIŞIR", yalnızca metinde
   geçenleri "OKUMA TALİMATI" diye işaretle. Her yol için: aynı skill projenin içinde de var mı?

RAPOR: ~/Documents/Claude/hf-om-raporlar/[AD].md dosyasına yaz. Klasör yoksa oluştur. Yazamıyorsan sohbete yaz.
Tablo + 5 satırlık özet. Hiçbir öneriyi uygulama.
```

Not: `IstatistikYoutube-Arsiv` eski HyperFrames skillerinin kopyalarını taşıyor; bu klasörde hiçbir temizlik yapılmaz.

---

## 5A — Etsy-Arif: sadece bilgi (istersen)

Klasör: `~/Documents/Etsy-Arif`. Bu depo Arif'in; burada hiçbir değişiklik, commit, push ya da PR yapılmaz.

```kopyala
Bu depoda hiçbir dosyayı değiştirme; commit, push, PR, dal ya da worktree işlemi yapma. Yalnızca oku ve sohbete rapor yaz:
1. .claude/skills içindeki ffmpeg, video-edit ve playwright-recording klasörleri .skill-kutuphanesi/kilit.json'daki kayıtla
   (kaynak sürümü ve klasör özeti) uyumlu mu?
2. Bu üç skilin içeriği bu bilgisayardaki ~/.claude/skills içindeki aynı adlı skillerle aynı mı?
3. İçinde "openmontage" geçen ajan dosyaları bu skillere nasıl atıf yapıyor (hangi yol, hangi ad)?
Hiçbir öneriyi uygulama; Arif'in dosyalarına dokunma.
```

---

## Her promptta değişmeyen kurallar

- Proje oturumu **skill kurmaz, güncellemez, kaldırmaz**. Bunlar kütüphane oturumundan `skill-ekle.py` ile yapılır.
- Proje oturumu bilgisayarın genelindeki klasörlere yazmaz. Tek istisna: rapor klasörü (`~/Documents/Claude/hf-om-raporlar/`)
  ve, sadece IstatistikYoutube'da ve onayınla, taban testinin kendi yazdığı yerler.
- `hyperframes update`, `upgrade`, `init`, `clean`, `skills update`, `npx skills` hiçbir oturumda çalıştırılmaz.
- Önce rapor, sonra onay, sonra değişiklik, sonra doğrulama.
- Onarım (B) promptları tam yedek alınmadan kullanılmaz.
- Her değişikliğin yanında tarih ve saatli yedeği, sha256 değeri ve geri alma satırı olur; var olan yedeğin üzerine yazılmaz.
