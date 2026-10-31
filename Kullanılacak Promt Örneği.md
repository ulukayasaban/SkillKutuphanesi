Bu projeye skill kütüphanemden skill kuracağız. Kütüphane: ~/Documents/SkillKutuphanesi
Önce ~/Documents/SkillKutuphanesi/AGENTS.md dosyasını oku ve oradaki akışı ATLAMADAN uygula:

1. Öneri al:
   python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --oner "[proje amacı ve teknoloji]"
2. Ön kontrol (hiçbir şey kurmaz):
   python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --profil [profil] [--rol ...] --kuru
3. Raporu bana olduğu gibi göster: kurulacak skiller, roller, HATA/UYARI satırları, ek adaylar.
4. Ben onay verene kadar BEKLE. Onaylarsam aynı komutu --evet ile çalıştır, sonra --dogrula sonucunu göster.

Kurallar: global skill klasörlerine (~/.claude/skills, ~/.agents/skills, ~/.codex/skills) dokunma,
skill dosyalarını elle kopyalama; sadece bu aracı kullan.

---

Tek tek, agent’ı adıyla:

“ui-tasarimci agent’ıyla ana sayfanın renk paletini ve tipografisini belirle.”
“frontend-muhendis agent’ıyla ana sayfayı Next.js’te kodla.”
“qa-erisilebilirlik agent’ıyla sayfayı mobilde test et.”

# 11 — Mevcut Projeye SkillKutuphanesi'nden Güvenilir Skill Seçimi

**Senaryo:** Başka bir Claude Code (ya da Codex) projen var. Oradaki agent projeyi zaten tanıyor: teknolojiyi, sürümleri,
kendi agent'larını, kuralları biliyor. Ondan istediğin şey proje analizi değil, **SkillKutuphanesi'nden** projeye ve
agent'larına en uygun, GitHub'da kendini kanıtlamış skilleri **çakışmasız** seçip **o projeye** kurması; sonraki seferlerde
de aynı düzende devam edebilmesi.

**Kapsam:** Sadece `~/Documents/SkillKutuphanesi`. Agent internetten, başka skill listelerinden ya da `npx skills add` gibi
yollardan skill aramaz/kurmaz. Kütüphanede uygun skill yoksa bunu söyler; kütüphaneye ekleme ayrı bir iştir
(`promptlar/07`, SkillKutuphanesi oturumunda).

**Nasıl kullanılır:** Projeyi Claude Code'da **o projenin klasöründe** aç, aşağıdaki bloğu olduğu gibi yapıştır.
Elle doldurman gereken alan yok; istersen son satıra odaklanmak istediğin işleri yaz.

```kopyala
Bu projeye ~/Documents/SkillKutuphanesi kütüphanesinden skill kur. Projeyi sen zaten tanıyorsun; proje analizi yapma,
bildiklerini kullan. Kapsam TAMAMEN SkillKutuphanesi: skill ve referans kütüphanesi bilgisini sadece oradan al.

══ KESİN KURALLAR ══
1. ~/Documents/SkillKutuphanesi SALT OKUNUR. Orada dosya oluşturma/düzenleme/silme, git işlemi YOK (sadece okuma ve
   `araclar/skill-ekle.py` çalıştırma). Kanıt: başta ve sonda `git -C ~/Documents/SkillKutuphanesi status --porcelain`
   çıktısını al; ikisi aynı olmalı. Farklıysa DUR ve bildir.
2. Skill'i SADECE `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py . …` ile kur. Elle kopyalama, symlink,
   `npx skills add`, internetten skill indirme YOK. Bu araç skilleri BU projenin `.agents/skills/` klasörüne kopyalar,
   `.claude/skills/` altına bağlar, `.skill-kutuphanesi/kilit.json`'a kaynağını (repo + commit) yazar, yedek alır.
3. Global klasörlere (~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage) dokunma.
4. `--evet` sadece ben raporu görüp "onaylıyorum" dedikten sonra. `--zorla` sadece ben açıkça istersem.
5. Benim dosyalarıma (mevcut `.claude/agents/*`, kendi `.claude/skills/*`, CLAUDE.md) onayım olmadan dokunma.

══ ADIM 1 — Bildiğini 6 satırda yaz (analiz değil, özet) ══
Teknoloji ve ana sürümler · referans kütüphaneleri (three.js, React, Next.js, GSAP, Tailwind, Playwright, FFmpeg…) ve
sürümleri · mevcut agent'lar ve görevleri · projede zaten kurulu skiller (`.skill-kutuphanesi/kilit.json` varsa oradan) ·
bu turda güçlendirilecek işler · Codex de kullanılıyor mu. Emin olmadığın bir şey varsa SADECE onu kısa bir dosya okumasıyla
doğrula (ör. package.json'da sürüm).

══ ADIM 2 — Kütüphanenin karar rehberini oku ══
`~/Documents/SkillKutuphanesi/notlar/guven-siralamasi.md` (otomatik üretilir, güncel):
- Bölüm 0: karar kuralları (skill puanı + kaynak güveni → al / gerekçeyle al / alma). BU KURALLARI UYGULA.
- Bölüm 1: kategori → en güvenilir kaynaklar ve en yüksek puanlı skiller. İşlerine karşılık gelen kategorileri seç.
- Bölüm 2: kaynakların GitHub güveni (yıldız, yıldız hızı, katkıcı, 90 gün commit, fork, sürüm, lisans, ücret dağılımı).
- Bölüm 3: referans kütüphanesi → onu öğreten skiller + kartın yazıldığı sürüm.
Gerekirse: `~/Documents/SkillKutuphanesi/notlar/roller-ve-profiller.md` (hazır rol/profil), `KATALOG.md` (tüm skiller).

══ ADIM 3 — Referans kütüphanelerinden başla ══
Projendeki her referans kütüphanesi için bölüm 3'teki "ilgili skiller"i aday yap. Kartı oku
(`~/Documents/SkillKutuphanesi/notlar/referans/<Kart sütunu>`: nasıl çalışır, ne zaman seç, performans/a11y, skill eşlemesi).
Sürüm kontrolü: kartın/skill'in anlattığı ana sürüm projendekinden farklıysa (ör. Tailwind v3↔v4, Three.js r1xx, Next.js
Pages↔App Router, GSAP <3.13) skill'in SKILL.md'sindeki API'yi kontrol et; uyumsuzsa ele ya da "sürüm farkı" diye işaretle.

══ ADIM 4 — İşlere göre adayları tara (tüm kütüphane) ══
Her iş için: `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py . --oner "<iş + teknoloji>" --adet 15`
(🔥trend = kaynağı GitHub Trending'e girmiş; eşitlikte öne geçirir, tek başına sebep değildir.)

══ ADIM 5 — Her adayı kanıtla (salt okuma) ══
python3 - <<'PY'
import json
ids = ["ID1", "ID2"]   # adayları yaz (id ya da ad)
K = "/Users/sabanulukaya/Documents/SkillKutuphanesi/"
R = {s["id"]: s for s in json.load(open(K + "registry.json"))["skiller"]}
for i in ids:
    s = R.get(i) or next((x for x in R.values() if x["ad"] == i and x["durum"] == "tercih"), None)
    if not s: print(i, "KÜTÜPHANEDE YOK"); continue
    g, d, t = s.get("gelistirici") or {}, s["degerlendirme"], s.get("trend") or {}
    gv = g.get("guven") or {}
    print(f"{s['id']} | skill {d['puan']}({d['not']}) | kaynak güveni {gv.get('puan','?')}({gv.get('derece','?')}) "
          f"#{gv.get('sira','?')}/{gv.get('toplam','?')} | ★{g.get('yildiz','?')} ★/ay {g.get('yildiz_hizi','?')} "
          f"katkıcı {g.get('katkici','?')} commit90g {g.get('commit_90g','?')} sürüm {g.get('son_surum') or '-'} | "
          f"lisans {g.get('lisans','?')} | ücret {s['ucret']}: {s.get('ucret_notu','')[:60]} | durum {s['durum']} | "
          f"kalite {s.get('kalite','-')} | codex {s['uyum']['codex']} | örtüşme {s.get('ortusme_grubu') or '-'}/{s.get('ortusme_rolu') or '-'} | "
          f"teknoloji {', '.join((s.get('teknoloji') or s['teknoloji_oto'])[:5])} | {s['repo']} | SKILL.md: {K}{s['yol']}/SKILL.md")
PY
Bölüm 0'daki kararları uygula. Ek olarak:
- `durum: tercih` olanı seç; `alternatif`i ancak somut nedenle (ör. teknolojine daha uygun).
- Ücret: önce `ucretsiz`; `kismen` ise ücretsiz yolunu yaz; `ucretli` (ücret ödemeden kullanılamayan) sadece açıkça gerekirse.
- Codex de kullanılıyorsa `codex: tam` tercih; `konu-claude-ozel` olanı Codex agent'ına verme.
- Seçeceğin her skill'in SKILL.md'sini oku: ağdan kod indiriyor mu, proje dışına yazıyor mu, gizli anahtar istiyor mu,
  projendeki teknolojiyle çelişiyor mu? Varsa bana söyle.

══ ADIM 6 — Çakışma kontrolü (zorunlu) ══
- Aynı İŞ: aynı `ortusme_grubu`ndan aynı role birden fazla "birincil" verme. Aynı işi yapan iki adayda bölüm 0 kuralı.
- Projede zaten olan skillerle (ADIM 1) aynı işi yapan adayı ekleme; hangisinin kalacağını bana sor.
- Aynı AD: projede kütüphane dışı aynı adlı skill varsa araç `projede-kendi-skillin` HATASI verir — dokunma, seçenek sun.
- Global'de aynı adlı farklı sürüm varsa araç `<ad>--kutuphane` adıyla kurar; agent dosyalarında o adı kullan.
- Bağlam: rol başına çekirdek 3–6, toplam ≤ 12 skill ve ~150 KB SKILL.md (`baglam-yuku`). `kardes-eksik` çıkarsa kardeşi ekle ya da skili çıkar.

══ ADIM 7 — Agent eşleme planı ══
- Agent'ların varsa onları DEĞİŞTİRME. İki yol sun: (a) skilleri `--skill …` ile kur (gerekirse `--rol-adi <yeni-ad>` ile ayrı
  bir kütüphane rolüne bağla), sonra onayımla kendi agent dosyamın `skills:` alanına ekle; (b) kütüphanedeki hazır rolü
  (`roller-ve-profiller.md`) farklı bir adla ekle. Kütüphane rolü benim agent dosyamla aynı adı taşıyamaz (`kendi-agent-dosyan`).
- Agent'ın yoksa uygun profil/rolleri öner (`--profil`, `--rol`).
Tablo ver: agent/rol → çekirdek → opsiyonel → her skill için: skill puanı · kaynak güveni (derece, #sıra) · ilgili referans
kütüphanesi ve sürüm uyumu · lisans · ücret · trend. Ayrıca: seçmediğin güçlü adaylar ve nedeni; kütüphanede KARŞILIĞI
OLMAYAN ihtiyaçlar (bunları kütüphaneye ekletmek için SkillKutuphanesi oturumunda prompt 07'yi öner).

══ ADIM 8 — Ön kontrol (hiçbir şey değişmez) ══
`python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py . [--profil P] [--rol R …] [--skill S …] [--rol-adi X] --kuru`
Raporu OLDUĞU GİBİ göster (kurulacaklar, roller, tüm HATA/UYARI/BİLGİ, `ek-aday`). HATA varsa kurma, nedenini ve seçenekleri
açıkla. UYARI'ları tek tek yorumla. DUR ve onayımı bekle.

══ ADIM 9 — Kurulum ve kanıt (sadece onayımdan sonra) ══
1. Aynı komut `--evet` ile. 2. `… skill-ekle.py . --dogrula` → ✅. 3. `… skill-ekle.py . --durum` → hepsi güncel.
4. `git -C ~/Documents/SkillKutuphanesi status --porcelain` başlangıçtakiyle aynı (kütüphane değişmedi).
5. Projede oluşanları listele (`.agents/skills/`, `.claude/skills/`, `.claude/agents/`, `.codex/agents/`, `.skill-kutuphanesi/kilit.json`).
   Proje git'teyse `.skill-kutuphanesi/yedek/`'i `.gitignore`'a eklemeyi öner (onayla).
6. Skillerin görünmesi için oturumu yeniden açmam gerektiğini hatırlat.

══ ADIM 10 — Sağlıklı devam (bu ve sonraki oturumlar için) ══
- Onayımla projenin CLAUDE.md'sine kısa bir bölüm ekle (yoksa oluşturma, öner): "Skiller ~/Documents/SkillKutuphanesi'nden
  `skill-ekle.py` ile kurulur; kütüphane salt okunur; kurulu skiller `.skill-kutuphanesi/kilit.json`'da; yeni skill
  gerekince prompt 11 akışı; güncelleme `--durum` → `--guncelle --kuru` → onay → `--guncelle --evet`."
- Kütüphane aylık güncellenir; projedeki kopyalar kendiliğinden değişmez. Her ay ya da ben istediğimde:
  `… skill-ekle.py . --durum` → değişen varsa `--guncelle --kuru` raporunu göster → onayımla `--guncelle --evet` → `--dogrula`.
- `--durum` "kaynak-yok" ya da "emekli" derse: kütüphanede yerine geçen skill'i bölüm 1/3'ten bul, bana öner.
- Yeni bir ihtiyaç çıkarsa ADIM 2'den devam et (projeyi yeniden analiz etme).
- Geri alma: `… skill-ekle.py . --geri-al` (son yedek), `--yedekler`, `--kaldir <ad>`.

Bu turda özellikle odaklanmanı istediğim işler (boşsa ADIM 1'deki işlere göre karar ver): […]
```

## Bu prompt neyi garanti eder?

| Konu                   | Nasıl                                                                                                                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kütüphane bozulmaz     | Salt okunur kural + başta/sonda `git status` kanıtı; kurulum aracı kütüphaneye yazmaz                                                                                                     |
| Skiller projede durur  | `skill-ekle.py` kopyalar; kaynak/commit `kilit.json`'da; yedek ve geri alma var                                                                                                           |
| Kanıtlanmış kaynak     | `notlar/guven-siralamasi.md`: skill puanı + kaynağın GitHub güveni (yıldız, yıldız hızı, katkıcı, commit, fork, sürüm, lisans; resmî sadece küçük bir parça), kaynaklar arası sıra/derece |
| Referans kütüphaneleri | Bölüm 3: three.js, Tailwind, GSAP, FFmpeg… → onları öğreten skiller + sürüm uyumu kontrolü                                                                                                |
| Çakışma yok            | Agent kontrolü (ADIM 6) + aracın ön kontrolü (`--kuru`); HATA varken kurulum olmaz                                                                                                        |
| Agent yapısı korunur   | Mevcut agent dosyalarına dokunulmaz; eşleme planı ve onay                                                                                                                                 |
| Sağlıklı devam         | Proje CLAUDE.md notu, `--durum`/`--guncelle` döngüsü, yeni ihtiyaçta ADIM 2'den devam                                                                                                     |
