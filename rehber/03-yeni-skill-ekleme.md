# 03 — Sonradan Yeni Skill / Repo Ekleme, Çıkarma, Kayıp Kaynak

> Karar kutusu (ilk iş): repoda SKILL.md yok ve kendi sürümü/kurulumu olan çalışan bir program ise -> rehber/11 (programlar.json).
> SKILL.md var -> bu rehber. İkisi birden (ör. HyperFrames, OpenMontage) -> ikisi de: burada kaynak kaydı (alan "program": "<ad>"), rehber/11'de program kartı; kartlar birbirine bağlanır.
> Tek ekleme sırası aşağıdaki A1..A9'dur; promptlar/07 aynı sırayı kullanır. Onaysız hiçbir kaynak eklenmez, çıkarılmaz; GitHub'a hiçbir şey kendiliğinden yazılmaz.

## A) "Yapay Zeka Skillleri" listesine yeni repo ekledin ("kontrol et") — tek ekleme sırası A1..A9

Tüm skill repoları GitHub'da tek listede durur: **"Yapay Zeka Skillleri"** (`kaynaklar.json` → `github_skill_listesi`).
Hazır prompt: `promptlar/07-yeni-skill-reposu-ekle.md`. Her adımda durma koşuluna uy.

```
A1  Başlangıç ve bul. `git status --short` BOŞ olmalı; değilse DUR ve kullanıcıya söyle (başka işin değişiklikleri yeni kaynak commitine karışır).
    `python3 araclar/dogrula.py --github | tail -3` -> "N skill · H hata · U uyarı" satırını not et (A7 ile karşılaştırılacak).
    `python3 araclar/github-skill-listesi.py` (YENİ / AD DEĞİŞMİŞ) ve `python3 araclar/github-trend.py --aday`. AD DEĞİŞMİŞ yeni kaynak DEĞİLDİR (rehber/09 'Repo adı değişirse').
    Karar kutusu (yukarıda): skill mi, program mı, ikisi mi. Aday kararı: bölüm F.
A2  İncele, tablo yap (kullanıcıya gösterilecek): ne yapıyor, kaç SKILL.md ve nerede (gh api ... git/trees), LİSANS (riskli sayılanlar:
    belirtilmemiş / NOASSERTION / AGPL / ticari-olmayan; tabloya kırmızı yaz, dogrula.py de uyarı verir), son güncelleme, ücret, trend, çakışma kontrolü (aynı ad / aynı iş / repo içi çoklu sürüm /
    aynı adlı kendi skill; genel klasörler 2026-11-12'de boşaltıldı: "global'de aynı ad" maddesi yalnız orada bir şey yeniden belirirse önemlidir), GÜVENLİK OKUMASI (en az bir SKILL.md ve her betik
    klasörünün örneği: ağdan kod indirip çalıştırma, proje dışına yazma, gizli bilgi okuma, `curl | sh`), UYUM (Claude'a özgü araç ister mi: TodoWrite, Task aracı...;
    Codex/Antigravity'de çalışmayacaksa tabloya yaz). Repo sabit commit'i: `gh api repos/OWNER/REPO/commits/HEAD --jq .sha` (A4'te onay.commit olacak).
    Çakışma/ücret/projeden bağımsız değerlendirme kuralları aşağıda "A2 ek" bölümünde.
A3  Kullanıcıya göster, ONAY bekle. Soru (aynen): "Bu kaynağı kütüphaneye ekleyeyim mi? Repo: <owner/ad>, <N> skill, lisans <L>, ücret <u>, tip <T>, commit <sha7>. Lisans/yol/güvenlik notları: <özet>."
    Cevap "evet" olmadan A4'e geçme. Lisans riskliyse ayrıca sor: "Lisans <L>; yine de ekleyeyim mi?" ve cevabı onay.lisans_onay'a yaz.
A4  Kayıt (yalnız onaydan sonra). kaynaklar.json -> repolar: tip, oncelik, gerekirse dahil/haric/bagimlilik/kimlik + ONAY KAYDI:
      "eklendi": "YYYY-AA-GG",
      "onay": {"kim": "kullanıcı", "tarih": "YYYY-AA-GG", "oturum": "<kısa not>", "commit": "<A2'deki 40 haneli sha>",
               "lisans_onay": "<yalnız riskli lisansta: kullanıcının gerekçesi>", "yol_onay": "<yalnız A5 yol kapısı takılırsa>",
               "guvenlik_notu": "<A2 güvenlik okumasının 1 cümlelik sonucu>"}
    + gerekirse ucret-siniflandirma.json, kategori-kurallari.json, T5/T6 kart/satır (aşağıdaki "A4 ek" kuralları). Onay kaydında PROJE ADI yazma (kural 6).
A5  Ön kontrol (hepsi okuma/indirme; arşive henüz yazmaz): `python3 araclar/gelistirici-bilgisi.py --repo owner/ad`;
    `python3 araclar/kaynak-cek.py --repo owner/ad` -> çıktıda `owner/ad ... skill=N` satırı ve `Toplam kayıt: N` olmalı (0 ise repo adı ya da tip yanlıştır, DUR);
    `python3 araclar/yol-tara.py --repo owner/ad --siki` -> "YOL KAPISI: GEÇTİ" olmalı. TAKILDI ise satırları kullanıcıya göster; yol-istisnalari.json yalnız öğretici
    metin için, "kabul" ancak kullanıcı raporu gördükten sonra; ya da kullanıcının gerekçesini onay.yol_onay'a yaz.
A6  Arşive yerleştir ve denetle: `python3 araclar/arsiv-yerlestir.py` (güvenlik kilidi: başka skill kaybolursa durur; KİMLİK/KİMLİK DEVRİ satırlarını kullanıcıya göster);
    `python3 araclar/kapsam-denetimi.py` (0 sorun); `python3 araclar/katalog-uret.py`; `python3 araclar/skill-readme.py` (aşağıdaki "Prompt 11 uyumu" geçerli).
A7  Skill testi ve doğrulama: yeni kimlikler: `python3 -c "import json;print(' '.join(s['id'] for s in json.load(open('registry.json'))['skiller'] if s['repo'].lower()=='owner/ad'))"`
    sonra `python3 araclar/skill-calistir.py --skill <o kimlikler>` (HATA varsa: yama, bölüm 'Çalışmayan skill'; TEST_RAPORU.md bu çağrıda yeniden yazılmaz);
    `python3 araclar/dogrula.py --github` (0 hata; uyarı sayısı A1'dekinden fazla olmamalı; fazlasını kullanıcıya göster).
A8  İncele, test, commit: sonuçları incele (aşağıdaki "A8 ek"); `python3 araclar/test.py`; `python3 araclar/duman-testi.py`;
    aday kararını deftere yaz (commit'e girsin): `python3 araclar/konu-takip.py --karar owner/ad eklendi "neden"` (repo hiçbir tarama kaydında yoksa araç UYARI verir ama yine de yazar);
    kullanıcıya özet + `git status --short` göster; sonra TEK commit: `git add -A && git add -f arsiv && git commit -m "Yeni kaynak: owner/ad"`.
A9  GitHub (git commitinden SONRA; kullanıcı zaten listeye koyduysa HİÇBİR ŞEY yapma): repo "Yapay Zeka Skillleri" listesinde değilse önce kullanıcıdan "evet" al, sonra
    `printf 'e\n' | python3 araclar/listeye-ekle.py owner/ad` (araç hedef listeyi ve korunan listeleri gösterir, kendi onay sorusunu sorar). `github-skill-listesi.py --ekle/--duzenle` KULLANMA
    (onay sormadan GitHub'a yazar; `--duzenle` GitHub'a hemen yazar ve repoyu korunmayan listelerden sessizce düşürür: yalnız kullanıcı sohbette açıkça isterse, okuma raporunu gösterdikten sonra).
    Aday kararı A8'de yazıldı. Push yalnız kullanıcı isterse.
```

Bulut/kısıtlı oturumda GitHub repo API'si kapalıysa araçlar kendiliğinden git'e düşer (ağaç blob'suz sığ fetch, dosyalar tek pack isteğiyle,
lisans arama API'sinden); `github-skill-listesi.py` ve `listeye-ekle.py` GraphQL gerektirir, yerelde çalıştırılır. Kısmi indirme güvenlidir:
indirilmeyen kaynaklar korunur; bir skill kaybolursa güvenlik kilidi işlemi durdurur.

### A2 ek: çakışma, ücret, projeden bağımsız değerlendirme
**Çakışma kontrolü (zorunlu, eklemeden önce):**
- Aynı **ad**: `registry.json`'da aynı `ad` var mı? İçerik aynıysa kopya sayılır; farklıysa `oncelik` küçük olan "tercih" olur.
- Aynı **iş**: aynı örtüşme grubunda (`ortusme_grubu`) birincil var mı? Yeni skill birincil / tamamlayıcı / alternatif mi?
- Repo içinde **aynı adlı birden fazla SKILL.md** (araç sürümleri ya da farklı sürümler) var mı? Araç bunları otomatik ayırır.
- **Global'de** aynı adlı farklı skill var mı? Projeye `<ad>--kutuphane` adıyla kurulur.
**Ücret kontrolü (zorunlu):** ücretli API/abonelik/lisans gerektiriyor mu? `ucret-siniflandirma.json`'a gerekçesiyle ekle
(`ucretsiz` / `kismen` / `ucretli`); eklemezsen ücretli servis izi olan skill `belirsiz` olur ve dogrula uyarır.
**Ölçüt:** `ucretli` = skill ücret ödemeden HİÇ kullanılamıyor (ör. tek işi fal.ai'yi çağırmak). Ücretli servis skill'in
seçeneklerinden biriyse, ücretsiz katman/kota varsa ya da sadece üretilen kodun çalışması ücretliyse → `kismen`.
**Değerlendirme projeden bağımsızdır:** öncelik, not ve inceleme alanları repo/skill'in kendi niteliğine göre yazılır; proje adı
ya da "şu projeye uyar" gerekçesi yazılmaz. Proje ↔ skill bilgisi: `python3 araclar/proje-kullanimi.py` → `notlar/proje-kullanimi.md`.
**Aynı ad, farklı iş:** kimlikler değişmez (eski kayıt çıplak adını korur, yeni gelen `ad@kaynak` olur); yeni kaynağın önceliği
daha yüksek olsa bile eski kayıt `durum_elle` ile "tercih" sabitlenir ve iki kaydın `notlar` alanına fark yazılır.

### A4 ek: tip, alanlar, kategori kuralı
**Tipini seç** ve `kaynaklar.json` → `repolar` listesine bir kayıt ekle:

| Tip | Ne zaman | Örnek kayıt |
|---|---|---|
| T1 | Repo bir skill koleksiyonu | `{"repo": "owner/ad", "tip": "T1", "oncelik": 3}` |
| T2 | Ürün reposu, içinde kullanıcıya yönelik birkaç skill var | `{"repo": "owner/ad", "tip": "T2", "oncelik": 1, "dahil": ["^skills/"]}` |
| T3 | Repoya katkı yapanlar için iç skiller | `{"repo": "owner/ad", "tip": "T3", "oncelik": 8, "dahil": ["^\\.claude/"], "kimlik": "owner__ad__repo-ici"}` |
| T4 | Yüzlerce uygulama-entegrasyon skilli | `{"repo": "owner/ad", "tip": "T4", "oncelik": 9, "dahil": ["^entegrasyonlar/"], "kimlik": "ad-entegrasyon"}` |
| T5 | Kütüphane/araç, skill yok | `{"repo": "owner/ad", "tip": "T5"}` + `notlar/referans/kutuphaneler.md`'ye satır |
| KAYIP | Repo silindi/private oldu; arşivdeki kopya korunsun | `tip`'i `"KAYIP"` yap |
| T6 | Tasarım teknolojisi, skill yok | `{"repo": "owner/ad", "tip": "T6"}` + `notlar/referans/tasarim-teknolojileri.md`'ye kart |

Alanlar:
- `oncelik`: aynı isimli skill başka repoda da varsa küçük sayı kazanır ("tercih"). 1 = resmî üretici, 2 = tek konulu
  uzman repo, 3 = metodoloji, 4–6 = toplama koleksiyon, 8–9 = gizli.
- `dahil` / `dahil_degil`: sadece şu yollardaki SKILL.md'ler (regex). Dışarıda kalanları başka bir kayıt almıyorsa
  `dahil` yerine gerekçeli `haric` kullan (kapsam denetimi "açıklanamayan" der). Bir repoyu iki kayda bölüyorsan
  (ör. T1 + T4) her SKILL.md'yi **tam olarak bir** kayıt almalı; kapsam denetimi bunu kontrol eder.
- `haric`: repo özelinde bilinçli hariç (tam yola uygulanır, ör. `^template/`).
- `kok_dosyalari`: SKILL.md repo kökündeyse sadece bu dosyaları al (ör. `["SKILL.md"]`). Repodaki diğer kodu indirmez.
- `dosya_haric`: skill klasörü içindeki göreli yollar için hariç (regex). Kökte duran skilllerde önizleme/rapor/test
  klasörlerini indirmemek için (ör. `["^\\.previews/", "^reports/"]`). Skill'in kullandığı `scripts/`, `references/` alınır.
- `bagimlilik`: skill çalışmak için başka bir kurulum istiyorsa açıklaması (ön kontrolde UYARI olur). Repodaki bütün skillere yazılır.
- `skill_bagimlilik`: tek bir skilin bağımlılığı repo metninden farklıysa `{"<kaynak_yol>": "metin"}` (ör.
  `{"skills/manim-video": "Manim CE, LaTeX, ffmpeg…"}`; boş metin = bağımlılık yok). `arsiv-yerlestir.py` registry'ye ve KAYNAK.md'ye
  bunu yazar. Bağımlılığı registry'de elle düzeltme: bir sonraki çalışmada repo metniyle ezilir. Anahtar registry'de bir skile
  karşılık gelmiyorsa ya da registry'ye işlenmemişse `dogrula.py` UYARI verir.
- `ad_devral`: bu kaynağın, başka bir kaydın taşıdığı çıplak adı **bilerek** devralacağı adlar (ör. `["motion-design"]`).
  Yazılmazsa çıplak ad eski kayıtta kalır, yeni skill `ad@kaynak` olur. Kullanıcı onayı gerekir (`rehber/09`).
- `eklendi`, `onay`: A4'teki onay kaydı (yeni kayıtta zorunlu; dogrula UYARI verir). Onay metninde proje adı yazılmaz.
- `kayip_tarihi`: `tip` KAYIP iken kaybın doğrulandığı gün (`YYYY-AA-GG`; bölüm E).
- `eski_adlar`: repo GitHub'da taşındıysa önceki adları (ör. `["eski-sahip/ad"]`); kurulu projelerin kilidi bununla eşlenir.
**Kategori kuralı gerekiyorsa** `kategori-kurallari.json` → `ad_kurallari` başına ekle (ilk eşleşen kazanır).
Yeni repoya ait kurala `"repo": "owner/ad"` yaz; başka repodaki aynı adlı skill etkilenmez. Repo geneli için `repo_varsayilan`.
Ekledikten sonra eski kayıtların kategorisi/durumu değişmiş mi bak (git HEAD'deki registry ile karşılaştır).
Yeni bir konu alanı gerekiyorsa `kategoriler.json`'a alan/kategori ekle.

**Prompt 11 uyumu (zorunlu, her eklemede):** Başka projelerdeki agent'lar `promptlar/11` ile bu kütüphaneden seçim yapar; prompt
sabit bilgi içermez, şu yapılardan okur: `registry.json` (puan, ücret, uyum, yol), `gelistiriciler.json` (`guven`),
`notlar/guven-siralamasi.md` (bölüm 0–4), referans kartları. Bu yüzden:
- Sıra: `gelistirici-bilgisi.py` → `kaynak-cek.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (rehberi yeniden üretir).
- T5/T6 referans kütüphanesi eklerken kart (`tasarim-teknolojileri.md`, `### Ad — \`owner/repo\` · sürüm` + `**Skill:**` satırı)
  ya da satır (`kutuphaneler.md`, son sütunda ilgili skiller) ZORUNLU; isteğe bağlı `katalog-uret.py` → `REF_DESEN`'e desen.
- `dogrula.py`'de "prompt uyumu" HATA/UYARI'sı 0 olmalı. Prompt 11'i değiştirmek gerekmez.

### A8 ek: sonuçları kontrol et
- `KATALOG.md`'de yeni skiller doğru kategoride mi?
- Aynı isimli skill varsa hangisi `tercih` oldu? Yanlışsa `oncelik`'i değiştir ya da registry'de `durum_elle`.
- Yeni skill bir role girmeli mi? `roller/*.json` → `cekirdek` / `opsiyonel`.
- Kategoriye `07-kategori-inceleme.md` adımlarıyla inceleme kartı yaz.

## B) Tek bir skill'i (repo olmadan) eklemek
Kütüphane kaynakları **herkese açık GitHub repolarıdır** (sabit commit ve geri izlenebilirlik için).
- Kendi yazdığın bir skill'i birden fazla projede kullanacaksan: kendi **public** GitHub reposuna koy ve A) adımlarıyla ekle.
- Sadece bir projede kullanacaksan: doğrudan o projenin `.claude/skills/<ad>/` (Claude) ve/veya `.agents/skills/<ad>/` (Codex)
  klasörüne koy. Bu senin skill'indir; `skill-ekle.py` ona **hiç dokunmaz** ve aynı adla kütüphaneden kurulum yapmaya
  çalışırsan `projede-kendi-skillin` hatasıyla durur.

## B2) Kendi skillerim (yerel kaynak, `kendi/`)
Kullanıcının kendi yazdığı skiller (ya da bir programın paketinden alınmış anlık kopyalar) GitHub'sız tutulur: kütüphane içindeki
`kendi/<ad>/` klasörü, `kaynaklar.json` → `yerel/kendi` kaydı (tip **T7**, `yerel: "kendi"`). Depo private olduğu için dağıtım yoktur.
Açıklama: `kendi/README.md`. Bu kaynak GitHub'a sorulmaz, ağ gerekmez; kaybolmuş ya da erişilemeyen sayılmaz.
- **Yeni skill eklemek:** klasörü `kendi/<ad>/` altına koy (SKILL.md + yanındaki dosyalar; `node_modules`, `package-lock.json`, `.env`, `*.pem`,
  `*.key` alınmaz). Kategori için `kategori-kurallari.json` → `ad_kurallari`'na `{"repo": "yerel/kendi", "desen": "^<ad>$", "kategori": ...}`,
  ücret için `ucret-siniflandirma.json`'a satır (rehber/03 A2 ek). Proje adı yazma (kural 6). Sonra aşağıdaki iki komut.
- **Düzenlenen skilin projelere ulaşması:** tek yer `kendi/<ad>/`. Düzenledikten sonra
  `python3 araclar/kaynak-cek.py --repo yerel/kendi` (ağ yok) → `python3 araclar/arsiv-yerlestir.py` (klasor_hash değişir, inceleme
  "yeniden-incelenecek" olur; arşiv elle düzenlenmez) → `kapsam-denetimi.py` (0 sorun) → `dogrula.py` (0 hata) → commit.
  Projede `skill-ekle.py <proje> --durum` güncelleme gösterir; `--guncelle --kuru` → onay → `--evet` → `--dogrula`. Aylık zincir
  (`arsiv-guncelle.py`) `kendi/` değişmişse bunu da değişen kaynak sayar. Düzenlenip işlenmemiş skili `kapsam-denetimi.py` yakalar.
- **Ad çakışması:** kendi skilin halka açık bir skille aynı adı taşırsa rehber/09 geçerlidir: çıplak ad kendiliğinden el değiştirmez
  (daha önce kayıtlı olan kimliği korur, yeni gelen `ad@yerel` olur); bilerek devir `ad_devral`.
- **Programla gelen skil** (ör. `nlm-skill`): bir programın kendi paketinde gelen skil kopya olarak buraya girerse kaynak notu ve sürüm
  kayda yazılır; program güncellenince klasör paketten yeniden kopyalanır. Tutarlı yol programın kartında `skill_koku` ile bağ vermektir
  (rehber/11); klasör adı skil adından farklıysa (`nlm-skill` için `data`) kartta `skill_klasorleri` eşlemesi yazılır ve bağ
  `skill-ekle.py <proje> --program-skill nlm:nlm-skill` ile verilir (`nlm` kartı artık vardır; `kendi/nlm-skill` anlık kopyasının yerini bu bağ alır).

- **Yalnız kullanıcının kendi yazdığı skiller** `kendi/` altına girer. Bir web sitesinden alınan (kullanıcının yazmadığı, GitHub'da da
  olmayan) skill buraya konmaz: B3.

## B3) Web sitesinden alınan skiller (yerel kaynak `site/`, K-57)
GitHub'da bulunmayan, kullanıcının sitesini verdiği skiller `site/<ad>/` klasöründe ve kendi yerel kaynağında durur: `kaynaklar.json` →
`yerel/site` (tip **T8**, `yerel: "site"`). `kendi/`'ye konmaz (orası yalnız kullanıcının kendi yazdıkları; `site/README.md`, `kendi/README.md`).
T7 gibi GitHub'a sorulmaz, ağ gerekmez, KAYIP sayılmaz; arşiv, kategori, ücret ve inceleme zinciri aynıdır.
- **Takip kaydı ZORUNLU:** kökteki `site-takip.json` → `skiller` içinde skill başına bir kayıt: `skill`, `kaynak: "yerel/site"`,
  `yerel: "site/<ad>"`, `site`, `sahip` (gerçek sahip; "Kendi (özel)" ya da "kullanıcı" yazılmaz), `sahip_tipi`, `sahip_url`, `lisans`
  (yazmıyorsa `belirtilmemiş`), `resmi_kaynak`, `kayit_tarihi` ve `dosyalar`. Her dosya: `ad`, `url` (https), `tur` (`asil` gerçek dosya,
  `yonlendirme` sitenin yönlendirme sayfası), `bayt`, `sha256` (indirilen baytların özeti), `karsilastirma` (`tam`: yerel dosya = site dosyası;
  `onek`: yerel dosya site dosyasıyla başlar, kütüphanenin eklediği bölüm sonda), `yerel_dosya` (skill klasörüne göreli; kütüphanede
  tutulmayan sayfalarda yok), istenirse `etkiler` (sayfa değişince bakılacak yerel dosyalar) ve `not`. Kaydı olmayan `site/<ad>/`, `kendi/`
  altını gösteren kayıt ya da bozuk yapı `dogrula.py`'de **HATA** verir; yerel kopyanın kayıttaki özetle uyuşmaması UYARI'dır.
  Sahip ve lisans kayda `arsiv-yerlestir.py` tarafından buradan alınır (değerlendirme puanı gerçek lisansla hesaplanır).
- **Yeni site skili eklemek:** dosyaları indir (yalnız GET), `site/<ad>/` altına koy (SKILL.md + yanındakiler), `site/<ad>/KAYNAK.md`'ye
  kaynak notunu yaz (site, yazar, lisans, indirme tarihi, kütüphanenin yaptığı değişiklikler, güvenlik notu), `site-takip.json`'a kaydı ekle
  (`python3 araclar/site-takip.py --kayit-denetle` 0 hata), kategori kuralı `{"repo": "yerel/site", "desen": "^<ad>$", ...}`, ücret satırı (A2 ek).
  Sonra `python3 araclar/kaynak-cek.py --repo yerel/site` (ağ yok) → `python3 araclar/arsiv-yerlestir.py` → `kapsam-denetimi.py` → `dogrula.py`.
  Kullanıcı onayı olmadan eklenmez; lisansı belirtilmemişse onay kaydında `lisans_onay` gerekir (A4).
- **Site değişti mi:** `python3 araclar/site-takip.py` (aylık zincir de çalıştırır) her adres için AYNI / DEĞİŞTİ / YENİ İÇERİK /
  ERİŞİLEMEDİ der; rapor `notlar/site-takip.md` (git'e girmez), aylık özet tarih ve değişen sayısını gösterir, değişikliği "karar bekleyenler"e
  koyar. Yönlendirme adresi gerçek dosyaya dönüşürse YENİ İÇERİK olur. Ağ yoksa ya da site düştüyse yalnız ERİŞİLEMEDİ; kaynak KAYIP sayılmaz.
  Araç `site/`, `kendi/`, `arsiv/` ve `site-takip.json`'a hiç yazmaz.
- **Güncelleme (her seferinde kullanıcı onayıyla, elle):** (1) `python3 araclar/site-takip.py --indir` değişen dosyaları kütüphane dışına,
  `~/Documents/Claude/deneme/site-takip-<tarih>/<ad>/` altına indirir (yalnız oku, çalıştırma); (2) farkı oku, güvenlik taraması yap
  (gizli değer, sistem dosyasına yazan komut, genel klasöre kurulum), kullanıcıya özetle; (3) onay gelirse `site/<ad>/` dosyalarını güncelle
  (önekli dosyada kütüphanenin eklediği son bölümü koru), `KAYNAK.md` tablosunu ve `site-takip.json` özetlerini (`bayt`, `sha256`,
  `kayit_tarihi`) yenile; (4) B2'deki işleme sırası (`kaynak-cek.py --repo yerel/site` → `arsiv-yerlestir.py` → kontroller), sonra
  `site-takip.py` yeniden AYNI demeli; (5) projelerde `skill-ekle.py <proje> --durum`.
- **Sitede GitHub reposu çıkarsa:** skill normal kaynak olarak A1..A9 ile eklenir; `site/<ad>/` kopyası emekli olur (H), takip kaydı kaldırılır.
- **Taşıma (`kendi/` → `site/`):** klasör taşınır, registry kaydının `repo`/`tip` alanı yeni kaynağa çevrilir ve iki yerel kaynak yeniden
  çekilip yerleştirilir; kimlik, kategori, ücret ve inceleme alanları korunur (2026-11-15 `stil`, K-57).

## C) Kategori, rol, profil eklemek
- **Kategori:** `kategoriler.json` → ilgili alan → `"NN-ad": "açıklama"`; kurallara desen ekle; `arsiv-yerlestir.py`.
- **Rol:** `roller/<rol>.json` (`ad`, `aciklama`, `gorev`, `cekirdek`, `opsiyonel`). Çekirdek ≤ 6 skill önerilir.
- **Profil:** `profiller/<profil>.json` (`ad`, `baslik`, `roller`, `ek_skiller`).
- Sonra `python3 araclar/dogrula.py` (var olmayan skill/rol adı HATA verir).

## Description ve tetiklenme (her yeni kaynakta)
Claude Code ve Codex bir skill'i **sadece** dosyanın ilk satırında başlayan YAML frontmatter'daki `description` ile tanır ve
"ne zaman kullanılacağına" onunla karar verir. Arşivdeki orijinallere dokunulmadığı için bozukluk **kurulan kopyada** düzeltilir
(`skill-ekle.py` → `aciklama_onar`, mantık `araclar/ortak.py` → `frontmatter_onar`):

| Sorun | Kurulumda ne olur | Elle iş |
|---|---|---|
| Frontmatter'ın önünde HTML yorumu var | Frontmatter başa alınır, yorum altına iner | — |
| `description` tırnaksız ve `: ` ya da ` #` içeriyor (YAML bozulur / kesilir) | Aynı metin JSON tırnağıyla yazılır | — |
| Frontmatter yok · `description` yok · 40 karakterden kısa · 1024'ten uzun | `aciklama_duzeltme.description` uygulanır | **Yaz** ↓ |

Elle yazılan düzeltme `registry.json` kaydında (inceleme alanı, `arsiv-yerlestir.py` korur):
```json
"aciklama_duzeltme": {"description": "<ne yapar>. Use when <hangi istekte/durumda>.", "neden": "description yok",
                      "skill_md_hash": "<kaydın skill_md_hash'i>", "tarih": "YYYY-AA-GG"}
```
- İngilizce, 40–1024 karakter; önce ne yaptığı, sonra **"Use when …"** ile tetikleyen istekler/anahtar sözcükler.
- `skill_md_hash` o anki SKILL.md'yi gösterir; kaynak değişirse `dogrula.py` "aciklama_duzeltme eskidi" uyarısı verir
  (yeni description yeterliyse düzeltmeyi sil, değilse güncelle).
- `dogrula.py` her skill'in kurulacak halini (onarım uygulanmış) okur; tetiklenemeyen varsa **HATA** verir.
- Projede zaten kurulu skillere `skill-ekle.py <proje> --guncelle` onarımı uygular (`aciklama-onarim`).
- Son toplu denetim: `notlar/tetiklenme-denetimi.md`.

## Çalışmayan skill: kurulum yaması ve çalıştırma testi
`python3 araclar/skill-calistir.py` her skill'i gerçek kurulum yoluyla geçici projeye kurar; yüklemeyi, bağlantıları ve
betiklerin sözdizimini sınar (`.py` derlenir, `.sh` `bash -n`, `.js` `node --check`, `.json`) → `TEST_RAPORU.md`.
`--ajan araclar/ornek-gorevler.json` ek olarak gerçek Claude Code'a örnek görev verir ve skill'in tetiklenip tetiklenmediğine bakar
(sadece okuma araçları; maliyeti raporda yazar).

Betiği bozuk bir skill arşivde düzeltilmez; düzeltilmiş dosya **`yamalar/<skill id>/<yol>`** altına konur ve kayda yazılır:
```json
"yama": {"dosyalar": {"scripts/x.py": "<orijinal dosyanın git blob hash'i>"}, "neden": "…", "tarih": "YYYY-AA-GG"}
```
Kurulumda (`hazirla()`) yama sadece orijinal o hash'teyse uygulanır; kaynak güncellenince yama atlanır ve `dogrula.py`
"yama eskidi" der (yeni sürümü dene; sorun sürüyorsa yamayı yenile, düzeldiyse yamayı sil). `--guncelle` yamayı kurulu
projelere de uygular. Yama yalnızca bozuk betik için değil, projeye uyarlama için de kullanılır: ör. `etsy-seller` kayıtlarını kullanıcının ev dizinine yazıyordu, yamayla proje köküne (`./etsy-listings`) alındı ki iki kişilik projede herkes aynı kaydı görsün; skill klasörü dışında kalan şablonlar da `bootstrap.py` içine gömüldü (`yamalar/etsy-seller/`).
Kaynakta git symlink'i olan `../<kardeş>` dosyaları (arşive düz metin olarak gelir) kurulumda
kendiliğinden kardeş skill bağlantısına çevrilir.

## Kontrol: "hiçbir skill atlanmadı" kanıtı
`notlar/kapsam-denetimi.md` her çalıştırmada yeniden üretilir: her repodaki her SKILL.md için karar
(arşivde / birebir kopya / başka AI aracı kopyası / gerekçeli hariç). **Açıklanamayan sayısı 0 değilse iş bitmemiştir.**


## D) Kaynak / skill KALDIRMAK (azaltma)
Ölçüt (hepsi birlikte): GitHub güveni düşük (D) **ve** yıldız az **ve** işlevi kütüphanede daha iyi bir kaynaktan karşılanıyor **ve**
hiçbir role/profile bağlı değil. Benzersiz işi olan düşük güvenli kaynak tutulur.
```
D0  Önce içerik (zorunlu): her alt klasörden örnek SKILL.md OKU ve gerekçeyi içerikle doğrula; klasör adından konu çıkarma
    (bkz. rehber/05 #97: `sealeap-amazon-skills` olayı). "Daha iyi alternatif var" diyorsan alternatifin SKILL.md'sini de oku:
    aynı işi mi yapıyor (geliştirici dokümanı ≠ işletme akışı)? Benzerlik puanları yalnızca aday üretir; Çince metinde çalışmaz.
    Varsayılan sonuç **örtüşme grubu** (birincil/alternatif); silme listesini kanıtıyla kullanıcıya sun.
D1  Etki raporu: `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` (ya da `--skill <kimlik> --kuru`; `--github` eklenirse repo/yıldız durumunu okur).
    Raporu kullanıcıya göster: engeller (role/profile bağlı), projeler, dikkatler. Onay al. Araç yalnız okur; hiçbir şey değiştirmez.
D2  Aracın yazdığı ADIMLAR'ı sırayla uygula: roller/profiller -> projelerde `skill-ekle.py <proje> --kaldir` (her proje için ayrı onay) -> kaynaklar.json
    (tüm repo: `repolar`dan sil + `arsivden_cikarilan_repolar`a ekle; tek skill: `arsivden_cikarilanlar`a ekle; kayda `onay` ve `geri_alma` yaz)
    -> `arsiv-yerlestir.py` -> `kapsam-denetimi.py` -> `katalog-uret.py` -> `dogrula.py` -> `test.py` -> TEK commit "Kaynak çıkarıldı: owner/ad".
    `--kayba-izin-ver` kullanma. `konu-takip.py --karar ... reddedildi` GEREKMEZ: çıkarılan repolar aday olarak bir daha çıkmaz.
D3  GitHub tarafı (git dışı; kullanıcının kararı): yıldız ve liste üyeliği kalsın mı? Kaldırılacaksa onayla: `gh api -X DELETE user/starred/<owner/ad>` (listeden çıkarma GitHub sayfasından).
D4  Geri alma: bölüm G'deki "çıkarmayı geri al" (git revert + listeye-ekle.py).
```
Program kaydı olan ("program" alanlı) kaynak bu yolla çıkarılmaz: rehber/11 'Programı çıkarma'.

## E) Kayıp kaynak (repo 404 oldu, private oldu, silindi)
```
E1  Teyit: `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru --github` ya da `gh api repos/owner/ad --jq .full_name`. `gh auth status` önce: oturum/ağ sorunu
    404 değildir. Yeni ad dönerse (full_name farklı) bu KAYIP değil taşınmadır: rehber/09 'Repo adı değişirse'.
E2  Etki: aynı raporu oku (projeler, roller). Projelerdeki kopya çalışır ama `--durum` "EMEKLİ: KAYNAK KAYIP" der; yenilenmez.
E3  Karar: hiçbir projede kullanılmıyorsa SORMADAN (a) uygulanır ve rol/profillerden çıkarılır (K-49, kullanıcı 2026-11-12); bir projede kullanılıyorsa kullanıcıya sor.
    (a) arşiv kopyası kalsın: kaynaklar.json'da kaydı SİLME; `"tip": "KAYIP"`, `"kayip_tarihi": "YYYY-AA-GG"` yaz ve `not`a
    "repo GitHub'da yok (404), <tarih>" ekle (bu işaretleme ELLE yapılır; otomatik `--kayip-isaretle` yoktur, kullanıcı kararıdır). Kaydı silmek güvenlik kilidini tetikler.
    (b) yerine geçeni var: rol/profilleri güncelle, sonra (a). (c) bilerek tamamen çıkar: bölüm D.
    Aylık güncelleme KAYIP olmayan ama o an erişilemeyen kaynağı `kaynak-cek.py --atla owner/ad` ile atlar ve raporlar (arşiv kopyası korunur); kalıcıysa bu bölümle KAYIP yap.
E4  `kapsam-denetimi.py`, `dogrula.py`, commit. KAYIP kaynak aylık sorgulanmaz: ara sıra `kaynak-cikar.py --repo <kayıp> --kuru --github` ile geri geldi mi bak;
    geri geldiyse `tip`'i eski değerine döndür, `kayip_tarihi`ni sil, `kaynak-cek.py --repo` + `arsiv-yerlestir.py`.
```

## F) Aday kararları (trend, popüler, konu takibi)
Üç araç aynı defteri okur: `konu-takip.json` (`degerlendirilen`, `izlenen`). Kararı HER ZAMAN şununla yaz: `python3 araclar/konu-takip.py --karar owner/ad <karar> "neden"`
(`populer-tarama.py --karar` KULLANMA: `izle` kararını sonsuza kadar gizler).

| Karar | Anlamı | Raporlarda |
|---|---|---|
| eklendi | kütüphaneye eklendi (A4'ten sonra yaz) | aday olarak bir daha çıkmaz |
| reddedildi | eklenmeyecek | aday olarak bir daha çıkmaz (yeniden açmak kullanıcı kararı) |
| izle | şimdilik değil; durum değişirse bak | konu-takip.py raporunda "İzlenenler" bölümünde; 90 gün sonra "zamanı geldi" |

Karar bekleyen sayısı ve en çok 5 aday adı: `python3 araclar/konu-takip.py --bekleyenler` (tarama yapmaz, ağ kullanmaz, dosya yazmaz; üç kaynağı birden özetler).
Karar verilince HEMEN `--karar` yaz. Kütüphaneden çıkarılan repo ayrıca karar gerektirmez. Kararı kullanıcı verir; ajan tek başına karar yazmaz.
Not: `github-trend.py` kendi aday tablosunda reddedilen repoyu yine listeleyebilir; karar defteri `konu-takip.py --bekleyenler` özetinde tam süzülür.

## G) Eklemeyi geri al / çıkarmayı geri al
- Commit atılmadıysa: `git status --short` göster; kullanıcı onaylarsa `git restore --source=HEAD --staged --worktree .`, sonra `git clean -n -d arsiv` ile izlenmeyen yeni arşiv klasörlerini göster ve silmeden önce sor.
- Commit atıldıysa: `git revert <commit>` (tek commit; merge commit ise `-m 1`). Kaynak kaydı, arşiv, registry, katalog, ücret/kategori kuralı, T5/T6 kartı tek hamlede geri gelir.
- GitHub (git revert kapsamaz): bu akış repoyu yıldızlayıp listeye ekledi ise, kullanıcıya söyle; kaldırmayı kullanıcı kendisi yapar ya da onayıyla `gh api -X DELETE user/starred/<owner/ad>`
  (liste üyeliği GitHub sayfasından). Kullanıcı kendisi koyduysa DOKUNMA. Çıkarmayı geri alırken yıldız/liste: `python3 araclar/listeye-ekle.py owner/ad` (kullanıcı onayıyla).

## H) Emekli etmek (kaldırmadan)
Emekli = skill kütüphanede ve projelerde kalır, yerine geçeni önerilir. Kaynakta silinen skill `kaynak_durumu: kaynakta-kaldirildi`, silinen repo
`kayip` olarak OTOMATİK emekli olur. Elle emekli: registry inceleme alanı `ortusme_rolu: emekli` (rehber/07 inceleme akışı) + rollerde yerine geçeni koy.
Projeler çalışmaya devam eder; `skill-ekle.py <proje> --durum` "EMEKLİ" der.
