# 03 — Sonradan Yeni Skill / Repo Ekleme

## A) "Yapay Zeka Skillleri" listesine yeni repo ekledin ("kontrol et")

Tüm skill repoları GitHub'da tek listede durur: **"Yapay Zeka Skillleri"** (`kaynaklar.json` → `github_skill_listesi`).
Hazır prompt: `promptlar/07-yeni-skill-reposu-ekle.md`.

```bash
cd ~/Documents/SkillKutuphanesi
python3 araclar/github-skill-listesi.py   # YENİ: listede olup kütüphanede olmayan repolar; ayrıca kopya/eksik liste üyeliği
python3 araclar/dogrula.py --github       # "YENİ SKILL REPOSU" uyarısı da aynı listeyi kullanır
```

1. **Repoyu tanı** (skill var mı, nerede, kaç tane, lisans, ücret):
   ```bash
   gh api "repos/OWNER/REPO/git/trees/HEAD?recursive=1" --jq '.tree[].path | select(test("(^|/)SKILL\\.md$";"i"))'
   ```
   **Çakışma kontrolü (zorunlu, eklemeden önce):**
   - Aynı **ad**: `registry.json`'da aynı `ad` var mı? İçerik aynıysa kopya sayılır; farklıysa `oncelik` küçük olan "tercih" olur.
   - Aynı **iş**: aynı örtüşme grubunda (`ortusme_grubu`) birincil var mı? Yeni skill birincil / tamamlayıcı / alternatif mi?
   - Repo içinde **aynı adlı birden fazla SKILL.md** (araç sürümleri ya da farklı sürümler) var mı? Araç bunları otomatik ayırır.
   - **Global'de** aynı adlı farklı skill var mı? Projeye `<ad>--kutuphane` adıyla kurulur.
   **Ücret kontrolü (zorunlu):** ücretli API/abonelik/lisans gerektiriyor mu? `ucret-siniflandirma.json`'a gerekçesiyle ekle
   (`ucretsiz` / `kismen` / `ucretli`); eklemezsen ücretli servis izi olan skill `belirsiz` olur ve dogrula uyarır.
   **Ölçüt:** `ucretli` = skill ücret ödemeden HİÇ kullanılamıyor (ör. tek işi fal.ai'yi çağırmak). Ücretli servis skill'in
   seçeneklerinden biriyse, ücretsiz katman/kota varsa ya da sadece üretilen kodun çalışması ücretliyse → `kismen`.
2. **Tipini seç** ve `kaynaklar.json` → `repolar` listesine bir kayıt ekle:

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
   - `bagimlilik`: skill çalışmak için başka bir kurulum istiyorsa açıklaması (ön kontrolde UYARI olur).
3. **Kategori kuralı gerekiyorsa** `kategori-kurallari.json` → `ad_kurallari` başına ekle (ilk eşleşen kazanır).
   Yeni repoya ait kurala `"repo": "owner/ad"` yaz; başka repodaki aynı adlı skill etkilenmez. Repo geneli için `repo_varsayilan`.
   Ekledikten sonra eski kayıtların kategorisi/durumu değişmiş mi bak (git HEAD'deki registry ile karşılaştır).
   Yeni bir konu alanı gerekiyorsa `kategoriler.json`'a alan/kategori ekle.
4. **Çalıştır:** (Bulut/kısıtlı oturumda GitHub repo API'si kapalıysa araçlar kendiliğinden git'e düşer: ağaç blob'suz sığ
   fetch ile, dosyalar tek pack isteğiyle, lisans arama API'sinden; `gelistirici-bilgisi.py --repo owner/ad` sadece o repoları
   yeniler. `github-skill-listesi.py` ise GraphQL gerektirir, yerelde çalıştırılır.)
   ```bash
   python3 araclar/gelistirici-bilgisi.py         # geliştirici bilgisi (yıldız, lisans, bakım)
   # (kısmi indirme güvenli: indirilmeyen kaynaklar korunur; bir skill kaybolursa güvenlik kilidi işlemi durdurur)
   python3 araclar/kaynak-cek.py --repo owner/ad   # sadece bu repo
   python3 araclar/arsiv-yerlestir.py
   python3 araclar/kapsam-denetimi.py              # 0 sorun olmalı
   python3 araclar/katalog-uret.py
   python3 araclar/dogrula.py --github             # 0 hata olmalı
   git add -A && git add -f arsiv && git commit -m "Yeni kaynak: owner/ad"
   ```
**Prompt 11 uyumu (zorunlu, her eklemede):** Başka projelerdeki agent'lar `promptlar/11` ile bu kütüphaneden seçim yapar; prompt
sabit bilgi içermez, şu yapılardan okur: `registry.json` (puan, ücret, uyum, yol), `gelistiriciler.json` (`guven`),
`notlar/guven-siralamasi.md` (bölüm 0–4), referans kartları. Bu yüzden:
   - Sıra: `gelistirici-bilgisi.py` → `kaynak-cek.py` → `arsiv-yerlestir.py` → `katalog-uret.py` (rehberi yeniden üretir).
   - T5/T6 referans kütüphanesi eklerken kart (`tasarim-teknolojileri.md`, `### Ad — \`owner/repo\` · sürüm` + `**Skill:**` satırı)
     ya da satır (`kutuphaneler.md`, son sütunda ilgili skiller) ZORUNLU; isteğe bağlı `katalog-uret.py` → `REF_DESEN`'e desen.
   - `dogrula.py`'de "prompt uyumu" HATA/UYARI'sı 0 olmalı. Prompt 11'i değiştirmek gerekmez.
5. **Sonuçları kontrol et:**
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
projelere de uygular. Kaynakta git symlink'i olan `../<kardeş>` dosyaları (arşive düz metin olarak gelir) kurulumda
kendiliğinden kardeş skill bağlantısına çevrilir.

## Kontrol: "hiçbir skill atlanmadı" kanıtı
`notlar/kapsam-denetimi.md` her çalıştırmada yeniden üretilir: her repodaki her SKILL.md için karar
(arşivde / birebir kopya / başka AI aracı kopyası / gerekçeli hariç). **Açıklanamayan sayısı 0 değilse iş bitmemiştir.**

## D) Kaynak / skill KALDIRMAK (azaltma)
Ölçüt (hepsi birlikte): GitHub güveni düşük (D) **ve** yıldız az **ve** işlevi kütüphanede daha iyi bir kaynaktan karşılanıyor **ve**
hiçbir role/profile bağlı değil. Benzersiz işi olan düşük güvenli kaynak tutulur. Adımlar:
0. **Önce içerik (zorunlu):** her alt klasörden örnek SKILL.md OKU ve gerekçeyi içerikle doğrula; klasör adından konu çıkarma
   (bkz. rehber/05 #97: `sealeap-amazon-skills` olayı). "Daha iyi alternatif var" diyorsan alternatifin SKILL.md'sini de oku:
   aynı işi mi yapıyor (geliştirici dokümanı ≠ işletme akışı)? Benzerlik puanları yalnızca aday üretir; Çince metinde çalışmaz.
   Projelerde kurulu mu bak (`find ~ -path '*/.skill-kutuphanesi/kilit.json'`). Varsayılan sonuç **örtüşme grubu** (birincil/alternatif);
   silme listesini kanıtıyla kullanıcıya sun ve **onay** al.
1. `kaynaklar.json`: repo kaydını `repolar`dan sil; `arsivden_cikarilan_repolar`a `{repo, skill_sayisi, neden, tarih, geri_alma}` ekle
   (tek tek skill için `arsivden_cikarilanlar`: `{repo, kaynak_yol, ad, neden, tarih}`).
2. Çalışma sırası: `kaynak-cek.py --repo <repo>` (yalnız tek skill çıkarıyorsan) → `arsiv-yerlestir.py` → `kapsam-denetimi.py` →
   `katalog-uret.py` → `dogrula.py` (0 hata) → `test.py`. Rolde/profilde kullanılan skill varsa önce yerine geçeni koy.
3. GitHub: repoyu listeden çıkar ve yıldızı kaldır (`gh api -X DELETE user/starred/<repo>`); `konu-takip.json` → `degerlendirilen`'e
   "reddedildi: kütüphaneden kaldırıldı" yaz ki aday olarak geri gelmesin. T5/T6 ise kartı/satırı da sil.
4. Geri alma: arşiv dosyaları git geçmişinde; repoyu `kaynaklar.json`'a geri yaz, `kaynak-cek` + `arsiv-yerlestir`, yeniden yıldızla.
