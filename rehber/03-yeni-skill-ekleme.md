# 03 — Sonradan Yeni Skill / Repo Ekleme

## A) GitHub'da yeni bir repo yıldızladın

```bash
cd ~/Documents/SkillKutuphanesi
python3 araclar/dogrula.py --github     # "UYARI: yıldızlı ama kaynaklar.json'da yok: owner/repo"
```

1. **Repoyu tanı** (skill var mı, nerede, kaç tane?):
   ```bash
   gh api "repos/OWNER/REPO/git/trees/HEAD?recursive=1" --jq '.tree[].path | select(test("(^|/)SKILL\\.md$";"i"))'
   ```
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
   - `dahil` / `dahil_degil`: sadece şu yollardaki SKILL.md'ler (regex). Bir repoyu iki kayda bölüyorsan
     (ör. T1 + T4) her SKILL.md'yi **tam olarak bir** kayıt almalı; kapsam denetimi bunu kontrol eder.
   - `haric`: repo özelinde bilinçli hariç (tam yola uygulanır, ör. `^template/`).
   - `kok_dosyalari`: SKILL.md repo kökündeyse sadece bu dosyaları al (ör. `["SKILL.md"]`). Repodaki diğer kodu indirmez.
   - `bagimlilik`: skill çalışmak için başka bir kurulum istiyorsa açıklaması (ön kontrolde UYARI olur).
3. **Kategori kuralı gerekiyorsa** `kategori-kurallari.json` → `ad_kurallari` başına ekle (ilk eşleşen kazanır).
   Yeni bir konu alanı gerekiyorsa `kategoriler.json`'a alan/kategori ekle.
4. **Çalıştır:**
   ```bash
   python3 araclar/gelistirici-bilgisi.py         # geliştirici bilgisi (yıldız, lisans, bakım)
   python3 araclar/kaynak-cek.py --repo owner/ad   # sadece bu repo
   python3 araclar/arsiv-yerlestir.py
   python3 araclar/kapsam-denetimi.py              # 0 sorun olmalı
   python3 araclar/katalog-uret.py
   python3 araclar/dogrula.py --github             # 0 hata olmalı
   git add -A && git commit -m "Yeni kaynak: owner/ad"
   ```
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

## Kontrol: "hiçbir skill atlanmadı" kanıtı
`notlar/kapsam-denetimi.md` her çalıştırmada yeniden üretilir: her repodaki her SKILL.md için karar
(arşivde / birebir kopya / başka AI aracı kopyası / gerekçeli hariç). **Açıklanamayan sayısı 0 değilse iş bitmemiştir.**
