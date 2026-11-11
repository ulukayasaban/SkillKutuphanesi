# 10 — Proje Kullanımı (hangi proje hangi skili kullanıyor)

**Kural:** Skill ve kaynak kayıtları (`registry.json` inceleme alanları, `kaynaklar.json` notları, kategori ve referans kartları,
ücret notları, öncelik gerekçeleri) projeden bağımsız yazılır. Proje adı ve "şu projeye uyar/uymaz" bilgisi oralara girmez.
Projeye uygunluk kurulum sırasında (`--oner`, `--kuru`) incelenir. Proje ↔ skill bilgisi **tek yerde** tutulur:

| Dosya | İçerik | Kim yazar |
|---|---|---|
| `notlar/proje-kullanimi.md` | Proje özeti, proje → skiller (kaynak, commit, rol), birden fazla projede kullanılan skiller | `araclar/proje-kullanimi.py` |
| `notlar/proje-durumu.md` | Her projenin sağlığı: güncelleme, elle değişiklik, kaynağı kalmamış ve kayıtsız skiller, kayıp projeler, kayıtsız klasörler | `araclar/proje-kullanimi.py --saglik` |
| `projeler.json` | `tarama_kokleri`, `ek_projeler`, projeye özel elle notlar (`notlar` → proje → skill kimliği) + `bilinen_projeler`, `yoksay`, `kayitsiz_tarama`, `kendi_skilleri` | Elle ya da `--ekle/--cikar/--tasindi/--yoksay` (onayla) |
| `<proje>/.skill-kutuphanesi/kilit.json` | Asıl kaynak: projede ne kurulu | `skill-ekle.py` |

## Kullanım
```bash
python3 araclar/proje-kullanimi.py                  # raporu yeniden üret (projelere dokunmaz)
python3 araclar/proje-kullanimi.py --skill <kimlik> # bu skili kullanan projeler
python3 araclar/proje-kullanimi.py --repo owner/ad  # bu kaynaktan skill kullanan projeler
python3 araclar/proje-kullanimi.py --kontrol        # rapor güncel mi (yazmaz; kabukta çıkış kodu hep 0, sıkı denetim için --siki)
python3 araclar/proje-kullanimi.py --saglik         # proje sağlığı -> notlar/proje-durumu.md (projelere salt okuma, yazılan tek dosya bu; --siki: sorun varsa çıkış 1)
python3 araclar/proje-kullanimi.py --saglik --ozet-json [--yaz]   # tek satır JSON özet (dosya yazmaz; --yaz raporu da yeniler)
python3 araclar/proje-kullanimi.py --tara-kayitsiz  # kilidi olmayan ama skill klasörü olan klasörler (yazmaz)
python3 araclar/proje-kullanimi.py --ekle <yol> [--neden "..."]          # projeyi takibe al (önce plan; --evet ile yazar)
python3 araclar/proje-kullanimi.py --cikar <ad> --neden "..."            # takipten çıkar
python3 araclar/proje-kullanimi.py --tasindi <ad> <yeni-yol>             # proje taşındı
python3 araclar/proje-kullanimi.py --yoksay <yol> --neden "..." [--altini-da]   # bilerek takipsiz
```
Dört değişiklik komutu da `--evet` olmadan yalnız planı gösterir; `--evet` ile yalnız `projeler.json` değişir.

## Yapıya bağlandığı yerler
- **`skill-ekle.py`**: projede değişiklik yapan her işlemden (kurulum, `--guncelle`, `--kaldir`, `--geri-al`, `--yenile`,
  `--arac`) sonra raporu kendisi yeniler. `--kuru`, `--durum`, `--dogrula`, `--oner` raporu değiştirmez. Rapor değiştiyse ve
  kütüphane `master` dalındaysa **yalnızca bu dosya** kendiliğinden commit edilir (kütüphane çalışma ağacı temiz kalsın diye;
  aylık güncelleme ve `--birlestir` temiz ağaç ister). Push hiçbir zaman kendiliğinden yapılmaz.
- **`dogrula.py`**: rapor güncel değilse ve kayıt dosyalarında proje adı geçiyorsa UYARI verir.
- **`arsiv-guncelle.py`**: aylık raporda değişen kaynakları kullanan projeleri listeler.
- **Silme, tercih değiştirme, ad devri öncesi**: `--skill` / `--repo` sorgusuyla etkilenen projelere bakılır.

## Yeni proje nasıl rapora girer
`~/Documents` altında bir seviyedeki projeler kendiliğinden bulunur. Başka yerdeki proje için `projeler.json` → `ek_projeler`
listesine tam yol yazılır. Projeye özel bir not (ör. "şu tarihten beri bu sürüm kullanılıyor") `projeler.json` → `notlar` →
`<proje klasör adı>` → `<skill kimliği>` altına yazılır; raporda o skilin "Not" sütununda görünür.
Başka yerdeki ya da kilitsiz (elle kurulu) bir projeyi takibe almak için `--ekle <yol>` kullanılır (aşağıda).

## Claude Code, Codex ve diğer araçlar
Araçlar yalnızca Python standart kütüphanesini kullanır; hangi yapay zekâ aracından çağrıldığı fark etmez. Claude Code
`CLAUDE.md`'yi, Codex ve `AGENTS.md` okuyan diğer araçlar `AGENTS.md`'yi okur; iki dosyada aynı kural (kural 6) ve aynı komutlar
yazılıdır. Rapor yalnızca bu bilgisayardaki projeleri görür: başka bilgisayarda ya da bulut oturumunda proje bulunamazsa rapora
dokunulmaz ve güncellik denetimi atlanır.

## Aylık proje turu
Her ay (ya da "projeleri kontrol et" denince) kütüphane oturumu şunu çalıştırır: `python3 araclar/proje-kullanimi.py --saglik`.
Çıktı `notlar/proje-durumu.md`: her projenin durumu, güncellemesi gelen / elle değişmiş / kaynağı kütüphanede kalmamış skiller,
kayıp ya da taşınmış projeler ve kayıtsız klasörler. Araç projeleri yalnızca okur (yazdığı tek dosya `notlar/proje-durumu.md`); çıkış kodu 0'dır (sonuç "sorun" olsa da; `--siki` ile 1).
Kullanıcıya sade özet verilir; her gerçek değişiklik (güncelleme, kaldırma, kayıt) ayrı ayrı onay ister.
Tur bitince, kullanıcıya sorularak, değişen `notlar/proje-durumu.md` dosyası tek başına commit edilir (`git commit -m "Proje durumu yenilendi" -- notlar/proje-durumu.md`);
kirli ağaç aylık güncellemeyi (`arsiv-guncelle.py --uygula`) engeller. Push yalnız kullanıcı isteyince.

## Yeni proje izlemeye alma
1. Kütüphaneden ilk kurulum: `skill-ekle.py <proje> --profil … --kuru` -> onay -> `--evet` (rehber/01).
2. Proje `~/Documents` altında bir seviyedeyse rapora kendiliğinden girer. Başka yerdeyse: `proje-kullanimi.py --ekle <yol>` (önce plan gösterir, `--evet` ile yazar).
`--ekle` aynı zamanda projeyi hafızaya (`bilinen_projeler`) yazar: silinirse ya da taşınırsa araç fark eder.
Skiller elle kopyalanmış, kilidi olmayan proje: `proje-kullanimi.py --ekle <yol> --neden "elle kurulu"`. Bu proje yalnızca izlenir
(sağlık ve envanter); güncellenmez. Kütüphaneyle yönetmek istersen önce `skill-ekle.py <yol> --kuru` ile ön kontrol yapılır.

## Kayıtsız proje bulma ve karar
`proje-kullanimi.py --tara-kayitsiz` kilidi olmayan ama skill klasörü olan klasörleri listeler (derinlik ve kökler `projeler.json` → `kayitsiz_tarama`;
bağlantıları izlemez, `.env` gibi dosyalara bakmaz). Her klasör için üç karardan biri verilir ve kullanıcıya sorulur:
(a) kütüphaneyle yönet: `skill-ekle.py` ile kur; (b) yalnız izle: `--ekle <yol> --neden …`; (c) bilerek takipsiz: `--yoksay <yol> --neden …`.
Karar verilmeyen klasör her ay raporda "karar bekleyen" olarak kalır. "Yalnız talimat dosyası olan" klasörler sayılır, işlem gerektirmez.
Bir skill klasörü genel klasöre (`~/.claude/skills` gibi) bağlıysa tarama "GENEL KLASÖRE BAĞLI" der: genel klasörleri boşaltmadan önce bunlara bakılır.

## Projeyi takipten çıkarma
`proje-kullanimi.py --cikar <ad> --neden "…"` (onayla). Proje klasörüne ve kilidine dokunulmaz; yalnız rapordan, aylık listeden ve
"KAYIP" uyarısından çıkar. Silinmiş projenin "KAYIP" uyarısını susturmanın yolu budur. Geri almak: `--ekle <yol>`.

## Proje taşındı, silindi ya da başka bilgisayara kopyalandı
- Taşındı: `--saglik` "TAŞINMIŞ görünüyor" der -> `proje-kullanimi.py --tasindi "<ad>" "<yeni-yol>"` (onayla) -> `skill-ekle.py "<yeni-yol>" --yenile --kuru` -> onay -> `--yenile`.
- Silindi: "KAYIP" -> kullanıcıya sor -> `--cikar`.
- Başka Mac'e ya da Windows'a kopyalandı: kopya salt okunur sayılır. `skill-ekle.py` yalnızca kütüphanenin olduğu bilgisayarda çalışır; kopyada
  `.skill-kutuphanesi/kilit.json` içindeki yollar eski bilgisayara aittir, bu normaldir ("BAŞKA YERDEN KOPYALANMIŞ olabilir"). Skill ekleme/güncelleme kütüphane
  bilgisayarında yapılır, kopya oraya geri getirilince `--yenile` gerekir. (Windows'ta skill-ekle.py çalıştırılması test edilmedi.)

## Projenin kendi yazdığı ve elle kurulan skiller
Kilitte olmayan her skill klasörü `--saglik`te şu üçünden biri olarak görünür: `elle` (projenin `.skill-kutuphanesi/elle-kurulan.json` dosyasında),
`kendi` (`projeler.json` → `kendi_skilleri` desenlerinden biri), ya da "KAYITSIZ SKILL" (karar bekleyen). İçeriği kütüphanedeki bir skille birebir aynıysa
"KİLİTSİZ KÜTÜPHANE KOPYASI" denir (elle kopyalanmış olabilir). Kayıtsızı sınıflamak için kütüphane oturumu kullanıcıya sorar ve onayıyla projenin
`.skill-kutuphanesi/elle-kurulan.json` dosyasına elle ekler (araç projeye yazmaz). Projenin kendi yazdığı skiller için
`projeler.json` → `kendi_skilleri` → `<proje>` listesine ad ya da `akil-disi-*` gibi desen yazılır.

## Programlar hangi projede (ilk sürümde otomatik değil)
HyperFrames / OpenMontage'ı hangi projenin kullandığı bu sürümde araçla izlenmez (ertelendi). Programı güncellemeden önce etkilenecek projeler
`notlar/hf-om-gecisi/DURUM.md` "Proje taraması" bölümünden ve `--saglik` çıktısındaki genel klasöre bağlantı satırlarından okunur.
Program kartlarına proje adı yazılmaz (kural 6).

## Bilerek takipsiz klasörler (yoksay)
`yoksay` listesinde klasör yolu, neden ve tarih bulunur. Şu an: Psikolojik Danışman Sosyal Medya ve İstatistik KIT paketi (kullanıcı kararı 2026-11-11: işlem yapılmaz).
Yeni giriş: `--yoksay <yol> --neden "…" [--altini-da]`; kaldırmak: `projeler.json` elle düzenlenir ve commit edilir.
Yoksayılan klasör taramada hiç açılmaz (içine bakılmaz).

## Araç ne yapmaz
Hiçbir proje klasörüne, `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage` altına yazmaz; push yapmaz; yalnız `projeler.json`
(onayla) ve kendi raporlarını (`notlar/proje-kullanimi.md`, `notlar/proje-durumu.md`) yazar.
