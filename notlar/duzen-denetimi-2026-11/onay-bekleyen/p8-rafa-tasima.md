# Rafa taşıma önerisi (P8, onay bekliyor)

Durum: TAŞINMADI. Kütüphane kökündeki üç eski belge hiçbir yerden bağlanmıyor (arama sonucu aşağıda) ve eski sayılar ile
artık geçerli olmayan kararlar taşıyor. Silinmez, `git mv` ile `notlar/rafta/` altına alınır (geri almak tek komut).
Arşive taşıma silme sayıldığı için kullanıcının onayı gerekir.

| Belge | Taşınacağı yer | Neden |
|---|---|---|
| `PLAN.md` | `notlar/rafta/PLAN.md` | ilk satırı zaten UYGULANDI diyor; gövdede eski sayılar (139/55/28) ve "Global kurulum yok" var |
| `Kullanılacak Promt Örneği.md` | `notlar/rafta/Kullanılacak Promt Örneği.md` | `promptlar/11` dosyasının eski kopyası (kural satırında `~/.openmontage` yok) |
| `notlar/yerel-yapilacaklar-2026-11.md` | `notlar/rafta/yerel-yapilacaklar-2026-11.md` | biten iş (PR #3, 5250 skill); proje kapısıyla çelişen `find ~ ... kilit.json` döngüsü içeriyor |

Taşınmayacaklar: `TEST_RAPORU.md` (üretilen dosya, README ve `skill-calistir.py` ona bağlı; yenilemeyi aylık güncelleme yapar),
`README-SKILLER.md`, `KATALOG*.md` (üretilen), `notlar/hf-om-gecisi/DURUM.md` (kütüphane oturumunun işi).

## Uygulama (onaydan sonra, kütüphane klasöründe)
```
diff "Kullanılacak Promt Örneği.md" promptlar/11-guvenilir-skill-secimi-mevcut-proje.md | head   # sonucu commit iletisine yaz
mkdir -p notlar/rafta
git mv PLAN.md notlar/rafta/PLAN.md
git mv "Kullanılacak Promt Örneği.md" "notlar/rafta/Kullanılacak Promt Örneği.md"
git mv notlar/yerel-yapilacaklar-2026-11.md notlar/rafta/yerel-yapilacaklar-2026-11.md
```
Sonra `notlar/rafta/OKU.md` dosyasını şu içerikle yaz:
```
# Rafta
Burada eski belgeler durur. Hiçbiri uygulanmaz; yalnız karar geçmişidir.
Güncel bilgi: BASLA.md, CLAUDE.md / AGENTS.md, notlar/kararlar.md.
Raftaki dosyalar bilerek taşındı (git mv); geri almak için: git mv notlar/rafta/<dosya> <eski yer>.
```
Taşımadan sonra bağlantı denetimi (bugün tek bağlantı `PLAN.md` içindeki kendi satırıdır; `notlar/hf-om-gecisi/rafta/` içindeki eski not satırı ve `promptlar/04`'teki, bir projenin plan dosyasından söz eden satırlar ilgisizdir; başka bağlantı çıkarsa dur ve sor):
```
git grep -nw "PLAN.md\|Promt Örneği\|yerel-yapilacaklar-2026-11.md" -- '*.md' '*.py' '*.json' ':!arsiv' ':!notlar/duzen-denetimi-2026-11' ':!notlar/rafta' ':!KATALOG.md' ':!skiller'
```
