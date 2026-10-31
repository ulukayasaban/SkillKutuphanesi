# 11 — Mevcut Projeye Güvenilir Skill Seçimi (kanıtlanmış kaynak + çakışma kontrolü)

**Ne zaman:** Başka bir Claude Code projen var (kodu, belki kendi agent'ları da var) ve ona SkillKutuphanesi'nden
**sadece kendini kanıtlamış, projene ve agent'larına uygun** skilleri almak istiyorsun.
**Nerede:** Claude Code'u **o projenin klasöründe** aç (SkillKutuphanesi'nde değil) ve aşağıdaki metni yapıştır.
`[KÖŞELİ PARANTEZ]` alanlarını doldur; bilmiyorsan boş bırak, agent projeden çıkarır ve sana sorar.

```kopyala
Bu projeye ~/Documents/SkillKutuphanesi kütüphanesinden skill kurmanı istiyorum. Amaç: projeye ve agent'larıma en uygun,
GitHub'da ve güven açısından kendini kanıtlamış skilleri, çakışmasız şekilde BU projenin klasörüne almak.

Proje hakkında (boşsa projeden çıkar ve bana doğrulat):
- Amaç / ne yapıyor: [ör. Next.js e-ticaret sitesi]
- Odaklanmak istediğim işler: [ör. ürün sayfası SEO, ödeme, test]
- Kullanacağım araç: [sadece Claude Code | Claude Code + Codex]

═══ KESİN KURALLAR (ihlal etme) ═══
1. ~/Documents/SkillKutuphanesi SALT OKUNUR. Orada hiçbir dosyayı oluşturma, düzenleme, silme; git komutu çalıştırma
   (status hariç). Sadece okuma ve `araclar/skill-ekle.py` çalıştırma serbest. Başta ve sonda
   `git -C ~/Documents/SkillKutuphanesi status --porcelain` çıktısını al; ikisi aynı olmalı, değilse DUR ve bildir.
2. Skilleri SADECE `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py . …` ile kur. Elle cp/ln/symlink YOK.
   Bu araç skilleri bu projenin `.agents/skills/` klasörüne KOPYALAR, `.claude/skills/` altına bağlar, kilit ve yedek tutar.
3. Global klasörlere (~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage) dokunma.
4. `--evet` sadece ben raporu görüp "onaylıyorum" dedikten sonra. `--zorla` sadece ben açıkça istersem.
5. Benim yazdığım dosyalara (mevcut `.claude/agents/*.md`, `.claude/skills/*`, CLAUDE.md) onayım olmadan dokunma.

═══ ADIM 1 — Projeyi ve mevcut yapıyı anla (sadece oku) ═══
- Teknoloji yığını: package.json / pyproject / go.mod / Gemfile vb., framework ve sürümleri, test aracı, deploy hedefi.
- Mevcut agent'lar: `.claude/agents/*.md` (ad, açıklama, varsa `skills:` listesi, araçları) ve `.codex/agents/*.toml`.
- Mevcut skiller: `.claude/skills/`, `.agents/skills/` (kendi skillerim mi, daha önce kütüphaneden mi kurulmuş?
  `.skill-kutuphanesi/kilit.json` varsa kütüphaneden gelenler orada yazılı).
- CLAUDE.md / AGENTS.md'deki kurallar.
Bana kısa bir özet tablo ver: teknoloji · mevcut agent'lar ve görevleri · mevcut skiller · eksik görünen yetenekler.

═══ ADIM 2 — Adayları bul (tüm kütüphane taranır) ═══
- Her ihtiyaç / her agent görevi için ayrı çalıştır:
  `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py . --oner "<ihtiyaç + teknoloji>" --adet 15`
- Uygun hazır profil/rol var mı bak: `ls ~/Documents/SkillKutuphanesi/profiller ~/Documents/SkillKutuphanesi/roller`
  ve `~/Documents/SkillKutuphanesi/notlar/roller-ve-profiller.md`.
- Kategori kataloğu gerekiyorsa: `~/Documents/SkillKutuphanesi/KATALOG.md`.

═══ ADIM 3 — Güven ve kanıt filtresi (her aday için, salt okuma) ═══
Aday kimliklerini (id) şu komutla incele (değiştirmez, sadece okur):
python3 - <<'PY'
import json, sys
ids = ["ID1", "ID2"]   # adayları buraya yaz
R = {s["id"]: s for s in json.load(open("/Users/sabanulukaya/Documents/SkillKutuphanesi/registry.json"))["skiller"]}
for i in ids:
    s = R.get(i) or next((x for x in R.values() if x["ad"] == i and x["durum"] == "tercih"), None)
    if not s: print(i, "YOK"); continue
    g, d, t = s.get("gelistirici") or {}, s["degerlendirme"], s.get("trend") or {}
    print(f"{s['id']:34s} puan {d['puan']:3d}({d['not']}) ★{g.get('yildiz','?')} lisans {g.get('lisans','?')} "
          f"son {g.get('son_guncelleme','?')} resmî {g.get('resmi_kaynak')} trend {t.get('seviye','-')} "
          f"ücret {s['ucret']} durum {s['durum']} kalite {s.get('kalite','-')} codex {s['uyum']['codex']} "
          f"örtüşme {s.get('ortusme_grubu') or '-'}/{s.get('ortusme_rolu') or '-'} kaynak {s['repo']}")
PY
Kabul ölçütleri (hepsini birlikte değerlendir, gerekçesini yaz):
- Değerlendirme puanı ≥ 65 (A/B). 50–64 (C) sadece daha iyi alternatif yoksa ve gerekçeyle. D ve `kalite: 1` (sadece yönlendirme) ALMA.
- Kaynak güveni: resmî üretici (resmi_kaynak) ya da kurum/topluluk tarafından benimsenmiş (yıldız sayısı yüksek), bakımı
  güncel (son güncelleme ≤ 180 gün tercih). GitHub Trending'e girmiş (`trend`) olanlar eşit durumda öne geçer, ama trend
  tek başına seçim sebebi değildir.
- Lisans açık (MIT, Apache-2.0, BSD…). Lisansı "yok/NOASSERTION" olanı ancak alternatif yoksa al ve bana işaretle.
- Ücret: `ucretsiz` önce. `kismen` olursa ücretsiz yolunu yaz. `ucretli` (ücret ödemeden hiç kullanılamayan) skili sadece
  açıkça gerekiyorsa öner ve ayrıca belirt.
- `durum: tercih` olanı seç. `alternatif` sürümü ancak somut nedenle (ör. projendeki teknolojiye daha uygun) seç.
- Teknoloji uyumu: skill'in teknolojisi projendekiyle aynı olmalı (React mı, vanilla mı; framework sürümü).
- Codex de kullanılacaksa `codex: tam` tercih; `konu-claude-ozel` olanı Codex agent'ına verme.
- SKILL.md'yi oku (`~/Documents/SkillKutuphanesi/` altındaki `yol`): projede beklenmedik iş yapıyor mu (ağdan kod indirme,
  proje dışına yazma, gizli anahtar isteme)? Varsa bana söyle.

═══ ADIM 4 — Çakışma kontrolü (zorunlu) ═══
- Aynı İŞ: aynı `ortusme_grubu`ndan aynı role birden fazla "birincil" verme; birini seç, diğerini gerekçeyle ele.
- Aynı AD: projede aynı adlı kendi skilim varsa (araç `projede-kendi-skillin` HATASI verir) DOKUNMA; bana seçenek sun.
- Global'de aynı adlı farklı sürüm varsa araç `<ad>--kutuphane` adıyla kurar; agent dosyalarında bu adı kullan.
- Mevcut skillerimle (ADIM 1) aynı işi yapan aday varsa ekleme; ya da hangisinin kalacağını bana sor.
- Bağlam yükü: rol başına çekirdek 3–6 skill; toplam 12'yi ve ~150 KB SKILL.md'yi aşma (`baglam-yuku` uyarısı).
- Kardeş bağımlılık (`kardes-eksik`) uyarısı çıkarsa önerilen kardeş skili de ekle ya da o skili çıkar.

═══ ADIM 5 — Agent'lara eşleme planı ═══
- Benim agent'larım varsa: onları DEĞİŞTİRME. Her agent'ın görevine göre skill listesi öner. Kurulum için iki yol sun:
  (a) skilleri sadece kur (`--skill … ` + gerekirse `--rol-adi <kütüphane-rol-adı>` ile ayrı bir rol), sonra benim onayımla
      agent dosyamın `skills:` alanına elle ekle; (b) kütüphanedeki hazır rolü farklı bir adla ekle.
  Kütüphane rolü benim agent dosyamla aynı adı taşıyamaz (araç `kendi-agent-dosyan` hatası verir).
- Agent'ım yoksa: uygun profil/rolleri öner (`--profil`, `--rol`).
Bana tablo ver: agent/rol → çekirdek skiller → opsiyonel skiller → neden (puan, kaynak, lisans, ücret, trend).
Seçmediğin ama ilgili güçlü adayları ve neden seçmediğini de listele.

═══ ADIM 6 — Ön kontrol (hiçbir şey değişmez) ═══
`python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py . [--profil P] [--rol R …] [--skill S …] [--rol-adi X] --kuru`
Raporu OLDUĞU GİBİ göster: kurulacak skiller, roller, tüm HATA/UYARI/BİLGİ satırları, `ek-aday` listesi.
HATA varsa kurma; nedenini ve seçenekleri açıkla. UYARI'ları tek tek yorumla (ücretli, lisans, alternatif, codex-uyum…).
Sonra DUR ve onayımı bekle.

═══ ADIM 7 — Kurulum ve doğrulama (sadece onayımdan sonra) ═══
1. Aynı komutu `--evet` ile çalıştır (`--kuru` yerine).
2. `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py . --dogrula` → ✅ olmalı.
3. `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py . --durum` → hepsi "güncel".
4. Kütüphanenin değişmediğini kanıtla: `git -C ~/Documents/SkillKutuphanesi status --porcelain` başlangıçtakiyle aynı.
5. Projede oluşanları listele: `.agents/skills/`, `.claude/skills/`, `.claude/agents/`, `.codex/agents/`,
   `.skill-kutuphanesi/kilit.json`. Proje git'teyse `.skill-kutuphanesi/yedek/`'i `.gitignore`'a eklemeyi öner (onayla).
6. Özet: kurulan skiller (kaynak repo, puan, lisans, ücret), agent eşlemesi, kalan uyarılar, ücretsiz yol notları.
   Skillerin görünmesi için Claude Code oturumunu yeniden açmam gerektiğini hatırlat.

Geri alma her zaman mümkün: `skill-ekle.py . --geri-al` (son yedek) ya da `--kaldir <ad>`.
```

## Neden böyle?
- **Kütüphane salt okunur:** Başka projedeki agent kütüphaneyi bozamaz; başta ve sonda `git status` karşılaştırması bunun kanıtı.
- **Proje kendi kopyasıyla çalışır:** `skill-ekle.py` skilleri projeye kopyalar ve `kilit.json`'a kaynağını (repo + commit) yazar.
- **Güven filtresi** registry'deki verilere dayanır: değerlendirme puanı (bakım, yıldız, lisans, resmî kaynak, Codex uyumu,
  bağlam yükü, yapı, GitHub trend), ücret sınıfı, inceleme kalitesi, örtüşme grubu.
- **Çakışma kontrolünü** hem agent (ADIM 4) hem araç (`--kuru` ön kontrolü) yapar; HATA varken kurulum olmaz.
