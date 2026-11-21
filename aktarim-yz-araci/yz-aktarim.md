# SkillKutuphanesi: başka yapay zeka aracına aktarım paketi

Hazırlandı: 2026-11-21 (ClaudeBakim projesindeki "Oturum açılış" oturumu). Bu klasörün nedeni: `README.md`. Kaynak: SkillKutuphanesi klasöründe okunan dosyalar (aşağıda "Okunanlar"). Bu dosya kendi içinde anlaşılır olacak şekilde yazıldı; yeni araca bu dosya + aşağıdaki istem verilir.

## 1. Tek paragraf özet
SkillKutuphanesi (`~/Documents/SkillKutuphanesi`), kullanıcının GitHub listesine eklediği repolardan YZ skill, kit, program ve araçları izleyen, sınıflayan, kaydeden, öneren ve **yalnız proje klasörlerine** kuran bir kütüphanedir. İşin büyük kısmı model kullanmayan Python betikleridir (`araclar/`, `skill-ekle.py` merkezde; `test.py` 324/324 geçiyor). Kullanıcının asıl isteği: **süreç kendi yürüsün, kullanıcıya yalnız kırmızı çizgi kararları gelsin; maliyet (token, kota, süre, disk, onay sayısı) ölçülüp görünsün.**

## 2. Kullanıcının istediği süreç (özet)
**Amaç:** Kullanıcının işi yalnız listeye repo eklemek. Gerisi (izleme, sınıflama, kayıt, öneri, kurulum, proje takibi, güncelleme, koruma, raporlama, hafıza) süreçte.
**Başarı:** aramak gerekmez; yeni repo soru sormaz ve öneriyi bozmaz; aylık takip kendi yürür; projeler aksamaz; işleyiş maliyeti düşük ve görünür.

**10 görev:** izleme · sınıflama (tür, kategori, ücret, risk, boyut) · kayıt (eski sürüm saklanır) · öneri · kurulum · proje takibi (skill, sürüm, güncel mi, dondurulmuş mu) · güncelleme (aylık, proje başına etki raporu) · koruma (riskli red, yedek, geri alma) · raporlama (durum + maliyet) · hafıza (tek yer, çift kayıt yok, açılış yükü az).

**Kesin kurallar**
- Skill'ler projenin içinde; genel klasörler (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) boş kalır. Skill yalnız `skill-ekle.py` ile kurulur, elle `cp`/`ln` yok.
- Kayıpsız: hiçbir skill, inceleme ya da sürüm kaybolmaz; geri dönülür.
- Riskli/saldırgan güvenlik skill'i alınmaz (istenen: otomatik, soru yok).
- Tam ücretli skill/servis de önerilir ("ücretli" etiketiyle); ilerleyiş ve para onayı kullanıcıya kalır.
- Tam uyum: Claude Code, Codex, Antigravity. Diğer YZ araçları için ek çaba ve garanti yok.
- Dondurulmuş proje raporda görünmez. Kaybolan (404) kaynak projede kullanılıyorsa kopya aynen kalır, uyarı gelir.
- GitHub'da yalnız `ulukayasaban/SkillKutuphanesi`; push yalnız kullanıcı isteyince. Gizli anahtar/parola/token değeri okunup yazılmaz.
- Kayıt dosyalarına (`registry.json` vb.) proje adı ya da "şu projeye uyar" gerekçesi yazılmaz; proje bilgisi `projeler.json` ve `notlar/proje-kullanimi.md`'de.

**Onay merdiveni**
- Onaysız: yeni repo adaptasyonu, kategori, öneri, aylık tarama, raporlar, kayıp işaretleme, yedek denetimi.
- Toplu onay: aynı skill + aynı hedef sürüm birden çok projede ise tek onay (etkilenen projeler listelenir).
- Tek tek onay: başka projeyi/süreci etkileyen her işlem (kurulum, güncelleme, kaldırma, sürüm değişikliği, elle değişmiş skill, dondurulmuş proje).
- Her zaman kullanıcıya: para, kalıcı silme, güvenlik riski, GitHub'a gönderme.

**Proje başına sürüm modu:** takip / dondur / yalnız onaylı. Güncelleme öncesi etki kontrolü (hangi dosya değişiyor, elle değişiklik var mı, hangi proje etkileniyor).

**Maliyet:** kurulum/yeniden kurma token'ı kabul; hedef **tekrarlayan işlerin** (yeni repo, aylık takip, kurulum, güncelleme, onarım) işleyiş maliyeti. Sayısal hedef önce ölçülür, sonra konur. İstenen ilke: model yalnız karar gereken yerde, gerisi betik.

**Çalışma düzeni:** sade Türkçe, konu konu, adımda tek soru; plan dosyası tek hafıza; planlama kısa oturumlarda (bağlam ≈288 bin token/tur olunca pahalı, kütüphane haftalık token'ın ≈%14-17'si).

## 3. Bugünkü durum ile istenen arasındaki fark
(Kaynak: `notlar/istenen-ve-mevcut-karsilastirma.md`, 2026-11-21)
- **Hazır:** kurulum (`skill-ekle.py`, kilit, yedek, `--geri-al`), genel klasörlerin boş olması, kayıpsızlık, tek tek onay kuralı, program güncelleme, kısa oturum düzeni.
- **Yok (4 şey):** yeni repoda onaysız uçtan uca yürüme · toplu onay · proje sürüm modu (takip/dondur/yalnız onaylı) · maliyet raporu.
- **Yarım:** izleme (aylık zincir fihrist ve kiti taramıyor; `son-aylik-calisma.json` damgası yok), sınıflama (`tip` ve `tur` yan yana; ücret/kategori kararı hâlâ LLM incelemesiyle), öneri (yeni repo profil/role kendiliğinden girmiyor), güncelleme (etki raporu dosya düzeyinde değil), koruma (riskli red otomatik değil), hafıza (çift kayıt, açılış yükü yüksek).
- **En büyük fark yön:** bugün sistem her yeni şeyde kullanıcıya soruyor; istenen, sorunun yalnız kırmızı çizgilerde gelmesi.
- **Vade 2026-12-07:** aylık zincirin fihrist/kit adımı ve damga dosyası asgari düzeltilmeli (son kayıtlı aylık çalışma 2026-11-02).
- Plan durumu: yol haritasında adım 1-3 tamam (hedefler, temizlik düzeyi, veri düzeni = tam ayrım aşamalı); **adım 4-9 açık** (giriş süreçleri, projelerdeki skiller, onay kuralları, token/maliyet süreçleri, araçlar-ajanlar-kota, geçiş planı ve kabul senaryoları). Kullanıcı planı "sonra" diye beklemeye aldı.

## 4. Yeni aracın okuyacağı dosyalar (sırayla)
Hepsi `~/Documents/SkillKutuphanesi` altında. Önce `cd` oraya.
1. `BASLA.md` (giriş, "hangi istek hangi komut" tablosu)
2. `AGENTS.md` (Codex/Antigravity için; `CLAUDE.md` ile aynı)
3. `notlar/istenen-surec.md` (kullanıcının istediği süreç, tam metin)
4. `notlar/istenen-ve-mevcut-karsilastirma.md`
5. `notlar/yeni-surec-plani-calisma.md` (adım 4-9 burada; bu dosyayı ben yalnız başından okudum)
6. `status/CHECKPOINT.md`, `notlar/kararlar.md` (kalıcı kararlar K-numaralı; değiştirmeden önce kullanıcıya sor)
7. İhtiyaç olursa: `rehber/` (15 dosya), `promptlar/` (17 hazır istem), `surecler/`, `ajanlar/`.

## 5. Yeni araca verilecek istem (kopyala-yapıştır)
```
Sen planlama yardımcısısın. Hedef: SkillKutuphanesi'nin "yeni süreç planı"nı (adım 4-9) kullanıcıyla birlikte tamamlamak. Kod yazma, dosya değiştirme, kurulum yapma: yalnız planla.

Önce şunları oku (salt okunur, ~/Documents/SkillKutuphanesi): BASLA.md, AGENTS.md, notlar/istenen-surec.md, notlar/istenen-ve-mevcut-karsilastirma.md, notlar/yeni-surec-plani-calisma.md, status/CHECKPOINT.md, notlar/kararlar.md.

Kurallar:
- Sade Türkçe. Konu konu ilerle. Bir mesajda en fazla 1 soru.
- Kullanıcının verdiği kararları (notlar/kararlar.md, istenen-surec.md) sorgulama; çelişki görürsen göster ve sor.
- Her öneride yaklaşık token/kota/süre maliyetini ve neyi azalttığını yaz. Model yalnız karar gereken yerde; gerisi betik.
- Kırmızı çizgiler: genel skill klasörlerine yazma yok, GitHub'da yalnız ulukayasaban/SkillKutuphanesi, push yok, silme yok, gizli anahtar okuma yok.
- Bilmediğin ya da doğrulamadığın şeyi "doğrulanmadı" diye işaretle.

Sıra: plan adım 4'ten başla (giriş süreçleri: yeni repo/skill, tür bazlı, onaysız uçtan uca). Her adımda: (1) bugünkü durum, (2) istenen, (3) önerilen yol, (4) maliyet, (5) kabul senaryosu (olay → süreç → kullanıcıya ne gelir). Adım bitince "getirme paketi" üret (aşağıdaki biçim) ve kullanıcıya göster.

Getirme paketi biçimi (tek sayfa):
- Karar: ne kararlaştırıldı (3-5 madde, K-numarası verilecekse öner).
- Yapılacak: dosya/araç adlarıyla değişiklik listesi (hangi betik, hangi belge).
- Bitti ölçütü: hangi komut/test neyi göstermeli.
- Maliyet: kurulum + her çalışmada tahmini.
- Açık soru: kullanıcıya kalan.
```

## 6. Claude'a ne getirilsin (öneri)
Planlama başka araçta, **uygulama ve doğrulama Claude'da** (betik çalıştırma, `test.py`, `dogrula.py`, kilit/yedek akışı Claude Code'da hazır ve kuralları orada yazılı). Her adım için **tek sayfalık getirme paketi** getirin; sohbet dökümü getirmeyin.

Getirme paketi yeterli olması için içermesi gerekenler:
1. Kararlar (kısa, madde madde).
2. Değişecek dosya ve araç adları.
3. Bitti ölçütü (hangi komut hangi sonucu vermeli).
4. Kabul senaryoları (en az: yeni repo, aylık kontrol, dondurulmuş proje, riskli repo, 404 kaynak).
5. Açık sorular.

Neden böyle: Claude'da uzun planlama oturumu her turda ≈288 bin token yeniden okutuyor (kütüphane notu). Kısa paket + kısa oturum bunu önler. Tahmini: bir getirme paketi 1-2 bin token; uygulama oturumları adım başına ayrı, kısa.

Önerilen sıra: (1) 2026-12-07 öncesi asgari düzeltme (fihrist/kit + damga), (2) adım 4, (3) adım 5-6 (sürüm modu, toplu onay), (4) adım 7 (maliyet ölçümü; önce ölçüm, sonra hedef).

## 7. Karar bekleyenler (kütüphane CHECKPOINT'inden)
- Push: 21 commit yerelde.
- Kullanılmayan 164 kaynağın kopyası arşivde dursun mu.
- 10 trend/popüler aday + listede olup kütüphanede olmayan 4 repo.
- Eski yedekler (en büyüğü 3,4 GB) silme: yalnız kullanıcı "sil" deyince.
- claude-mem gözlemcisi haftalık token'ın ≈%15'i: kısılsın mı.

## 8. Okunanlar ve okunmayanlar
Okundu: `BASLA.md`, `notlar/istenen-surec.md`, `notlar/istenen-ve-mevcut-karsilastirma.md`, `status/CHECKPOINT.md`, `promptlar/README.md`, `CLAUDE.md` başı, `notlar/yeni-surec-plani-calisma.md` ilk ~6 KB.
**Okunmadı** (yeni araç okumalı): `notlar/kararlar.md` (45 KB), `notlar/plan-tur-surecleri.md` (49 KB), `yeni-surec-plani-calisma.md` kalanı (adım 4-9 ayrıntısı), `rehber/*` (237 KB), `surecler/*`, `ajanlar/*`. Bu dosyadaki bilgi yalnız okunanlara dayanır; sayılar kaynak dosyalardan aktarıldı, yeniden saymadım.
