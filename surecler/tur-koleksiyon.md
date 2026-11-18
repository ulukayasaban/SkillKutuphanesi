# Tür: skil koleksiyonu

## Ne
İçinde birden çok bağımsız skil olan repo (2-199 SKILL.md). Örnek: `anthropics/skills`, `greensock/gsap-skills`. Bölüm: **arşiv**.
Eklenti paketi (içinde `.claude-plugin` olan repo) ayrı bir tür değildir; skilleri bu dosyaya, `tur-tek-skil.md` ya da `tur-dev-koleksiyon.md` dosyasına göre
işlenir. Paketin ek kuralları bu dosyanın sonundadır.

## Kütüphanede ne durur
Skillerin metin ve kod dosyaları `arsiv/` altında; her skil `registry.json` içinde; `kaynaklar.json` içinde tek kayıt. Medya ve model dosyaları alınmaz (aşağıda).

## Ekleme adımları
1. `yeni-repo.md` adım 1-6 (tür, boyut, çakışma, ücret, tek mesaj, kullanıcı "evet").
2. `rehber/03-yeni-skill-ekleme.md` A4: kaynak kaydı (aşağıdaki alanlar) ve onay kaydı; ücret için `ucret-siniflandirma.json`, gerekirse `kategori-kurallari.json`.
3. `rehber/03` A5-A7: `python3 araclar/gelistirici-bilgisi.py --repo owner/ad`, `python3 araclar/kaynak-cek.py --repo owner/ad`, `python3 araclar/yol-tara.py --repo owner/ad --siki`,
   `python3 araclar/arsiv-yerlestir.py`, `python3 araclar/katalog-uret.py`, `python3 araclar/skill-readme.py`, `python3 araclar/skill-calistir.py --skill <yeni kimlikler>`.
4. Skilleri inceleyen taraf `rehber/07-kategori-inceleme.md` adımlarıyla her yeni skili inceler (kategori, ücret, lisans, örtüşme, Türkçe özet, güvenlik).
5. Kontroller ve commit: `yeni-repo.md` adım 8, `rehber/03` A8.

Koleksiyona özgü kararlar:
- **Köke bağlı skil.** Skilin SKILL.md'si reponun kökündeki bir dosyaya bağlıysa (`tur-belirle.py` "köke bağlı skil" sayar): kök dosyası küçük ve belirliyse kayda `kok_dosyalari` ile
  skille birlikte alınır; skil reponun bütününe bağlıysa kayıtta `tek_basina: false` yazılır ve skil tek başına önerilmez (öneri tarafı HENÜZ YOK, plan adım 4; yine de işaret yazılır).
- **Aynı işi yapan skiller.** Eklerken benzerleri bulunur (`ortusme_grubu`); hangisinin tercih edileceği kayda (`oncelik`, `durum_elle`) ve `notlar` alanına yazılır.
- **Medya.** Bugünkü koruma `kaynaklar.json` içindeki `skill_ici_haric` ve `max_dosya_mb` sınırıdır (video, `node_modules`, büyük dosya). `tur-belirle.py` çıktısındaki medya dosya sayısı ve MB'ı kullanıcıya
  söylenir; skil bir medya dosyasına gerçekten ihtiyaç duyuyorsa `ne_indirir` alanına "kurulumda kaynaktan gelir: <dosya>, <MB>" yazılır. Her medya ve ikili dosyayı arşive girmeden engelleyen otomatik kural HENÜZ YOK
  (plan adım 3); arşive giren medya varsa raporda belirtilir.
- **Kopya skil.** Başka kaynağın birebir kopyası olan skil arşive ayrı girmez; araç ayna/kopyayı ayırır, kayda not düşülür (`rehber/09`).

## Kayda yazılacak alanlar
```json
{"repo": "owner/ad", "tip": "T1", "oncelik": 4, "tur": "koleksiyon", "bolum": "arsiv",
 "tur_gerekce": "12 bağımsız SKILL.md, her biri kendi klasöründe",
 "ne_ister": "Node 20", "ne_indirir": "yok", "tek_basina": true, "kurulmayan_parcalar": [],
 "son_kontrol": {"tarih": "2026-11-18", "commit": "<40 haneli sha>"},
 "arac_uyumu": {"claude": true, "codex": true, "antigravity": true, "windows": true},
 "boyut": {"kutuphane_kb": 120, "kurulum_mb": 4.2, "hesaplanamayan": [], "tarih": "2026-11-18"},
 "eklendi": "2026-11-18", "onay": {"kim": "kullanıcı", "tarih": "2026-11-18", "oturum": "<kısa not>", "commit": "<40 haneli sha>"}}
```
Alan açıklamaları `rehber/03` "Tür ve boyut alanları" maddesindedir. Kayıtta proje adı yazılmaz.

## Aylık güncelleme
Bugünkü zincir: `python3 -u araclar/arsiv-guncelle.py --aylik` (dal, özet, onaylı birleştirme; `rehber/02-guncelleme-yonergesi.md` bölüm 1b). 12 aydır değişmeyen repo "bakımsız" notu alır (raporda görünür; HENÜZ YOK, plan adım 5).

## Projeye kurulum
Arşivden: `python3 araclar/skill-ekle.py <proje> --oner "<ihtiyaç>"`, `--kuru`, kullanıcı onayı, `--evet`, `--dogrula` (`rehber/01-skill-ekleme-sureci.md`, `rehber/04-kontrol-listesi.md`).

## Çıkarma
`python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` (yalnız okur: etki ve sıralı adımlar); kullanıcı onayıyla `rehber/03` bölüm D adımları (`promptlar/14-kaynak-cikar.md`).

## Bilinen sorunlar ve önlem
| Sorun | Önlem |
|---|---|
| Köke bağlı skil | Yukarıda: `kok_dosyalari` ya da `tek_basina: false` |
| Aynı işi yapan skiller çoğalır | Tercih kayda yazılır; projede tercih edilen önerilir |
| Talimatı çok uzun skil | `baglam_yuku` proje raporunda toplanır (HENÜZ YOK, plan adım 4) |
| Repo bakımsız | Aylık raporda "bakımsız" notu (HENÜZ YOK, plan adım 5) |
| Repo silinir, taşınır, lisansı değişir | Silinirse `rehber/03` E (kayıp kaynak, K-49); taşınırsa `repo` güncellenir, eski ad `eski_adlar`a yazılır (`rehber/09`); lisans değişimi aylık raporda görünür, güncelleme kullanıcı kararına kadar bekler |

## Eklenti paketi ek kuralları (`.claude-plugin` olan repo)
- Paket bütün olarak kurulmaz: genel klasöre (`~/.claude`) yazar ve yalnız Claude'da çalışır. Skilleri bu dosyaya (ya da tek skil / dev koleksiyon dosyasına) göre işlenir; paket kurma adımı atılmaz.
- Skil paket kökündeki bir dosyaya bağlıysa eklerken tespit edilir (`notlar/yol-denetimi.md`); gereken kök dosyaları skille birlikte alınır (`kok_dosyalari`).
- Paketin kancaları, ayarları ve MCP sunucuları skille gelmez: alınmaz; kayda `kurulmayan_parcalar` listesine yazılır ve proje raporunda gösterilir.
- Paketin ajan ve komutları bugünkü gibi `registry.json` `bilesenler` kaydında izlenir.
