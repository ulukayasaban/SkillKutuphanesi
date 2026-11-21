# İstenen süreç: Skill Kütüphanesi

> Yalnız istenen süreç; mevcut süreçlerden bahsetmez. İşaretsiz = senin dediğin; (öneri) = benim eklediğim, onay bekliyor. Ortak plan: `notlar/yeni-surec-plani-calisma.md`.

## Amaç
GitHub listene eklediğin repolardan işe yarayan YZ skill, kit, program ve araçları süreç kendi izler, sınıflar, kaydeder, önerir ve projelere kurar. **Senin işin: listeye repo eklemek.**
Başarı: aramak gerekmez; yeni repo soru sormaz ve öneriyi bozmaz; aylık takip kendi yürür; projeler aksamaz; işleyiş maliyeti düşük ve görünür.

## Görevler
1. **İzleme:** liste taranır; yeni, değişen, kaybolan repo bulunur.
2. **Sınıflama:** tür, kategori, ücret, risk, boyut kurallarla belirlenir.
3. **Kayıt:** eski sürümler saklanır; gereksiz kopya taşınmaz.
4. **Öneri:** yeni repo öneri işlemine adapte olur; yeni proje için öneri raporu çıkar.
5. **Kurulum:** seçilen skill projeye kurulur.
6. **Proje takibi:** hangi skill, hangi sürüm, güncel mi, dondurulmuş mu.
7. **Güncelleme:** aylık kontrol, her proje için etki raporu.
8. **Koruma:** riskli repo reddi, yedek, geri alma.
9. **Raporlama:** durum ve maliyet.
10. **Hafıza ve kontrol:** neyin nerede tutulduğu tek yerde; çift kayıt yok; açılış yükü az.

## Kurallar
- Süreç yazılı kurallara göre kendini sürdürür; yeni repo ve aylık kontrolde sana bağımlı olmaz; her tür kendi sürecinden geçer.
- **Skill'ler projenin içinde, genel klasörler boş** (kesin). Kopyanın kütüphanede nerede durduğu önemsiz; **projeye özgü takip şart.**
- **Kayıpsız:** hiçbir skill, inceleme ya da sürüm kaybolmaz; eski sürüm silinmez, geri dönülür.
- Riskli ve saldırgan güvenlik skill'i alınmaz; otomatik, soru yok (öneri).
- **Tam ücretli skill/servis önerilmez:** kayıtta etiketli durur, sen isteyince kullanılır (o zaman para onayı sana gelir). Ücretsiz ve kısmen ücretsiz (ücretsiz katmanı olan) olanlar normal önerilir.
- Claude Code, Codex, Antigravity ile tam uyum; diğer YZ araçlarında da çalışır.
- Karar, inceleme ve ölçüm katmanları tam uyumlu; tek giriş; aynı bilgi tek yerde.
- Kısa oturumlar; plan dosyası tek hafıza; her şey kayıtlı ve görünür.
- Programların yedekli güncellenmesi olsa iyi olur, zorunlu değil.

## Onay
- **Onaysız:** yeni repo adaptasyonu, kategori, öneri. (öneri) aylık tarama, kayıt yenileme, kullanılmayan 404 kaynağı işaretleme, raporlar, yedek denetimi.
- **Toplu:** aynı işlem birden çok projede aynıysa tek onay. (öneri) "aynı" = aynı skill + aynı hedef sürüm; etkilenen projeler listelenir.
- **Tek tek:** başka projeyi ya da proje sürecini etkileyen her işlem. (öneri) kurulum, güncelleme, kaldırma, sürüm değişikliği, elle değişmiş skill, dondurulmuş proje.
- **Her zaman sana:** para, kalıcı silme, güvenlik riski, GitHub'a gönderme.

## Projeler ve sürümler
Proje başına: skill, sürüm, kaynak, son işlem, durum. Sürüm modu: **takip / dondur** (güncellenmesin, raporda da görünmez) **/ yalnız onaylı**. Güncelleme öncesi etki kontrolü: hangi dosya değişiyor, elle değişiklik var mı, hangi proje etkileniyor (öneri). Uygulama onaylı; her güncelleme geri alınabilir.

## Maliyet
Kurulum maliyeti önemsiz; **işleyiş maliyeti hedef** (yeni repo, aylık takip, kurulum, güncelleme, onarım). Her işlemde token, kota, süre, disk, onay sayısı kaydedilir ve raporlanır. (öneri) YZ yalnız karar gereken yerde, gerisi betik. **Sayısal hedefler önce ölçüm yapılıp sonra konur** (yeni repo ve aylık takip birer kez ölçülür).

## Senaryolar (olay → süreç → sana ne gelir)
- Listene yeni repo (yeni tür dahil) → tarar, sınıflar, kaydeder, önerilere ekler, öneriyi bozmaz → hiçbir şey.
- Riskli ya da saldırgan repo → otomatik reddeder → hiçbir şey.
- Yeni proje başlıyor → öneri raporu → rapor ve kurulum onayı.
- Aylık kontrol → tüm türleri tarar, projeler için öneri ve etki raporu → yalnız projeyi etkileyenler.
- Aynı skill'in yeni sürümü 3 projede → tek toplu öneri → tek onay.
- Dondurulmuş proje → güncellemeye dokunmaz, raporda da yer vermez → hiçbir şey.
- Güncelleme projeyi aksatabilir → etki raporu, geri dönüş hazır → tek tek onay; sorun çıkarsa önceki sürüme döner, kısa bildirim.
- Kaynak repo silinir (404) → kullanılmıyorsa işaretler; kullanılıyorsa projedeki kopya aynen kalır, projeye dokunmaz → kullanılıyorsa uyarı gelir.
- Tam ücretli skill/servis → etiketler, hiçbir öneriye koymaz → hiçbir şey (sen isterse para onayı).
- Başka YZ aracı açılır → aynı proje skill'lerini görür → hiçbir şey.
- Ağ yok ya da adım hata verir → durur, projede değişiklik yapmaz, devam noktasını kaydeder; oturum yarıda kesilirse plan dosyasından sürer → hata bildirimi.
- Aylık maliyet raporu → token, kota, süre, disk, onay sayısı → kısa rapor.
- Program (ör. HyperFrames) yeni sürüm → yedekli güncelleme önerir (isteğe bağlı) → onay.

## Netleşecek sorular
1. "Diğer YZ araçlarında çalışsın": hangi araçlar ve ne kadar?
