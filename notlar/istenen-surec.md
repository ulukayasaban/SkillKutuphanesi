# İstenen süreç: Skill Kütüphanesi (kullanıcının istediği hâliyle)

> Bu belge yalnız **ne istendiğini** anlatır; mevcut süreçlerden ve araçlardan bahsetmez. Kaynak: kullanıcının 2026-11-21 tarihli sözleri. `[Senin]` = kullanıcının dediği, `[Önerim]` = benim eklediğim, onay bekliyor.
> Ortak çalışma dosyası: `notlar/yeni-surec-plani-calisma.md`.

## 1. Tanıtım
**Ne:** GitHub listelerinde yıldızlanan repolardan işe yarayan yapay zeka skill, kit, program ve araçlarını kendi kendine izleyen, sınıflayan, kaydeden, öneren ve projelere güvenle kuran süreç.
**Kimin için:** Tek kullanıcı. Süreci otomasyon ve yapay zeka ajanları yürütür.
**Kullanıcının tek işi:** GitHub listesine repo eklemek `[Senin]`. Gerisini süreç yürütür.
**Başarı ölçütleri**
1. Yeni projeye başlarken skill aramak gerekmez; öneri hazırdır.
2. Yeni repo eklenince kullanıcıya soru gelmez; süreç adapte olur, öneri işlemi bozulmaz.
3. Aylık kontrol kendi yürür.
4. Projeler aksamaz; hiçbir değişiklik izlenmeden yapılmaz.
5. İşleyiş maliyeti düşük ve görünürdür.

## 2. Süreç görevleri
| # | Görev | Ne yapar | Onay |
|---|---|---|---|
| 1 | İzleme | GitHub listelerini düzenli tarar; yeni, değişen, kaybolan repoyu bulur | Onaysız |
| 2 | Sınıflama | Repoyu türüne göre ayırır; kategori, ücret, risk ve boyut kurallarla belirlenir | Onaysız |
| 3 | Kayıt | Repo kaydı tutulur; eski sürümler saklanır; bilgisayarda gereksiz kopya taşınmaz | Onaysız |
| 4 | Öneri | Yeni repo mevcut öneri işlemlerine uyar; yeni proje için öneri raporu hazırlanır | Onaysız |
| 5 | Kurulum | Seçilen skill projeye kurulur | Proje onayı |
| 6 | Proje takibi | Her proje için hangi skill, hangi sürüm, güncel mi, dondurulmuş mu tutulur | Onaysız (okuma) |
| 7 | Güncelleme | Aylık kontrol; her proje için güncelleme önerisi ve etki raporu | Hazırlık onaysız, uygulama onaylı |
| 8 | Koruma | Riskli repo reddi, yedek, geri alma, genel klasörlerin boş kalması | Otomatik |
| 9 | Raporlama | Durum ve maliyet raporu | Onaysız |
| 10 | Kontrol ve hafıza | Takip ve kontrol işlemlerinin yürümesi; neyin nerede tutulduğu tek yerde | Otomatik |

## 3. Temel ilkeler
- **Kurallı ve planlı:** Süreç, yazılı kurallara göre kendini sürdürür; yeni repo ve aylık kontrolde kullanıcıya bağımlı olmaz `[Senin]`.
- **Tür bazlı:** Her repo türüne uygun süreçten geçer `[Senin]`.
- **Skill'ler projenin içinde durur, genel klasörler boş kalır:** kesin kural `[Senin]`. Kurulumun kütüphane içinde nerede tutulduğu önemsizdir; önemli olan projeye özgü takiptir `[Senin]`.
- **Kayıpsız:** Hiçbir skill, inceleme veya sürüm kaybolmaz; eski sürümler silinmez, geri dönülebilir `[Senin]`.
- **Güvenlik:** Riskli ve saldırgan güvenlik skill'leri alınmaz `[Senin]`; bu karar otomatiktir, kullanıcıya soru gitmez `[Önerim]`.
- **Uyumluluk:** Claude Code, Codex ve Antigravity ile tam uyumlu; diğer yapay zeka araçlarında da çalışır `[Senin]`.
- **Katmanlar uyumlu:** Karar, inceleme ve ölçüm katmanları birbirleriyle tam uyumlu çalışır `[Senin]`.
- **Sade:** Tek giriş, aynı bilgi birden fazla yerde yazılmaz `[Senin]`.
- **Kısa oturumlar, tek hafıza:** Plan dosyası tek hafızadır, her şey kayıtlıdır ve görünürdür `[Senin]`.
- **Programlar (ör. HyperFrames, OpenMontage) yedekli güncellenir:** olması iyi olur, zorunlu değil `[Senin]`.

## 4. Onay kuralları
**Onaysız çalışır (kütüphane içi, geri alınabilir)** `[Senin]` + `[Önerim]`
Yeni repo geldiğinde: izleme, sınıflama, kategori, ücret ve risk etiketi, kayıt, öneri hazırlama `[Senin]`. Ayrıca `[Önerim]`: aylık tarama, fihrist ve kayıt yenileme, kaybolan kaynağı işaretleme (kullanılmıyorsa), maliyet ve durum raporu, yedek denetimi, hata bildirimi.

**Toplu onay:** Aynı işlem birden fazla projede **aynıysa** tek onayla `[Senin]`. `[Önerim]` "Aynı işlem": aynı skill, aynı hedef sürüm, etkilenen projelerin listesi onay metninde görünür.

**Tek tek onay:** Başka projeleri ilgilendiren ya da projenin sürecini etkileyen her işlem `[Senin]`. `[Önerim]`: kurulum, güncelleme, kaldırma, sürüm değişikliği, projede elle değiştirilmiş skill'e dokunma, dondurulmuş projeye dokunma.

**Her zaman kullanıcıya (kırmızı çizgi)** `[Senin]`: para (ücretli servis), kalıcı silme, güvenlik riski, GitHub'a gönderme.

## 5. Projeler ve sürümler
- **Proje bazlı takip:** her proje için skill listesi, sürümü, kaynağı, son işlem tarihi, durumu `[Senin]`.
- **Sürüm modu (proje başına)** `[Senin: güncellemek istemediğim projeler olabilir]`: takip et / **dondur** (güncellenmesin, raporda yalnız görünür) / yalnız onaylı güncelle.
- **Etki kontrolü** `[Senin: projeleri aksatabilir]`: güncellemeden önce hangi dosyalar değişiyor, projede elle değişiklik var mı, hangi proje etkileniyor; sonuç raporda, uygulama onaylı `[Önerim]`.
- **Geri dönüş:** her güncelleme geri alınabilir; eski sürüm saklanır `[Senin]`.
- Sürüm işlemleri her türlü duruma karşı kontrol edilir `[Senin]`.

## 6. Uyumluluk
Tam uyum: Claude Code, Codex, Antigravity. Çalışma garantisi aranan ek hedef: diğer yapay zeka araçları (ör. Cursor, Copilot, Gemini CLI) `[Senin]`. `[Önerim]` ortak açık skill biçimi ve ortak giriş dosyası kullanılır, araç başına tek ek kural yazılmaz.

## 7. Maliyet
- **Kurulum maliyeti önemsizdir** `[Senin]`. **İşleyiş maliyeti** (yeni repo ekleme, aylık takip, proje kurulumu, güncelleme, hata onarımı) hedeftir `[Senin]`.
- Her işlem için token, kota, süre, disk ve onay sayısı kaydedilir ve raporlanır `[Senin]`.
- `[Önerim]`: yapay zeka yalnız kural dışı ya da karar gereken yerde çalışır; geri kalanı betik. Hedef değerler sayısal olarak birlikte belirlenir.

## 8. Hafıza ve kontrol
Neyin nerede tutulduğu tek yerde yazılıdır; çift kayıt yoktur; oturum açılış yükü azdır; takip ve kontrol işlemleri kendi yürür `[Senin]`.

## 9. Senaryolar (olay → süreç ne yapar → sana ne gelir)
| # | Olay | Süreç ne yapar | Sana ne gelir |
|---|---|---|---|
| S1 | GitHub listene yeni repo eklenir | Tarar, türünü bulur, kategori/ücret/risk yazar, kaydeder, önerilere ekler | Hiçbir şey (isteğe bağlı kısa özet) |
| S2 | Yeni repo riskli ya da saldırgan güvenlik içeriklidir | Otomatik reddeder, yalnız not düşer | Hiçbir şey |
| S3 | Yeni proje başlıyor | Proje tipine göre öneri raporu hazırlar | Rapor ve kurulum onayı |
| S4 | Aylık kontrol | Tüm türleri tarar, değişenleri kayda geçirir, projeler için güncelleme önerisi ve etki raporu hazırlar | Yalnız projeyi etkileyen öneriler |
| S5 | Aynı skill'in yeni sürümü 3 projede kurulu | Tek bir toplu öneri hazırlar | Tek toplu onay |
| S6 | Bir proje "dondurulmuş" | Güncellemeye dokunmaz, raporda yalnız "yeni sürüm var" der | Hiçbir şey |
| S7 | Güncelleme projeyi aksatabilir | Etki raporu verir, uygulamayı onaya bırakır, geri dönüş hazır tutar | Onay (tek tek) |
| S8 | Güncelleme sonrası sorun | Önceki sürüme döner, nedenini kayda yazar | Kısa bildirim |
| S9 | Kaynak repo silinir (404) | Kullanılmıyorsa işaretler; projede kullanılıyorsa projeye dokunmaz | Yalnız kullanılıyorsa uyarı |
| S10 | Ücretli skill/servis çıkar | Ücretli etiketler, otomatik önermez | Kurulumda para onayı |
| S11 | Yeni tür bir repo gelir | Tür kuralıyla adapte olur; öneri işlemi bozulmaz | Hiçbir şey |
| S12 | Başka yapay zeka aracı açılır | Aynı proje skill'lerini görür | Hiçbir şey |
| S13 | Ağ yok ya da bir adım hata verir | Durur, projede hiçbir değişiklik yapmaz, devam noktasını kaydeder | Hata bildirimi |
| S14 | Aylık maliyet raporu | Token, kota, süre, disk, onay sayısını yazar | Kısa rapor |
| S15 | Program (ör. HyperFrames) yeni sürüm çıkarır | Yedekli güncelleme önerir (isteğe bağlı) | Onay |
| S16 | Oturum yarıda kesilir | Plan dosyasından kaldığı yerden sürer | Hiçbir şey |

## 10. Netleşmesi gerekenler
1. **Ücretli skill/servis:** `[Önerim]` etiketle, otomatik önerme, kurulumda ayrı para onayı.
2. **Dondurulmuş proje:** aylık raporda yalnız "yeni sürüm var" mı denmeli?
3. **Kaybolan kaynak** projede kullanılıyorsa: projedeki kopya aynen kalır, uyarı gelir mi?
4. **Maliyet hedefleri:** yeni repo ve aylık takip için kabul edilen üst sınır (adım 7'de sayıya bağlanacak).
5. **Diğer yapay zeka araçlarında "çalışsın":** hangi araçlar (Cursor, Copilot, Gemini CLI, başka) ve "çalışsın" ne kadar demek?
