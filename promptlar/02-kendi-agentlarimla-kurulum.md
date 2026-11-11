# 02 — Kendi Agent'larımla Kurulum (sadece skiller)

**Ne zaman:** Agent'larını Codex'te/Claude'da kendin tanımladın (kendi `.codex/agents/*.toml` ya da `.claude/agents/*.md` dosyaların var);
kütüphaneden sadece **skilleri** almak istiyorsun.
**Dikkat:** Kütüphane rolleriyle aynı adda kendi agent dosyan varsa araç onun üzerine yazmaz (`kendi-agent-dosyan` HATA). Bu yüzden burada
rol kurulmaz; skiller "genel" kurulur ve projedeki her agent görür.

```kopyala
Bu projeye skill kütüphanemden SADECE skill kuracağız; agent'larımı ben tanımladım, onlara dokunma.
Kütüphane: ~/Documents/SkillKutuphanesi — önce ~/Documents/SkillKutuphanesi/AGENTS.md dosyasını oku.

Benim agent'larım ve görevleri: [ör. "tasarimci: arayüz; kodcu: Next.js; testci: Playwright"]
Proje: [amaç + teknoloji]

Projede araç düzeni kayıtlıysa (--durum satırı "düzen: ..."), ona uy; "arac-secimi-yok" çıkıyorsa bana hangi araçlarla açılacağını sor ve --arac ile kaydet.

1. Her agent'ım için uygun skilleri bul:
   python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --oner "[agent'ın işi + teknoloji]"
   (her agent için ayrı çalıştır; ücretsiz ve 'tercih' olan skilleri seç, emekli/alternatif olanları seçme)
2. Seçtiğin skillerin listesini agent bazında bana tablo olarak göster (skill · neden · ücret durumu · çakışma riski).
3. Ön kontrol (rol vermeden, sadece skill):
   python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --skill [skill1 skill2 ...] --kuru
4. Raporu göster; ÇAKIŞMA (ortusme, ayni-skill-iki-surum, projede-kendi-skillin, ekli-ad) ve ÜCRETLİ uyarılarını ayrıca açıkla.
5. Onayımı bekle; onaylarsam --evet ile kur, --dogrula sonucunu göster.
6. Kurulumdan sonra benim agent dosyalarımın talimatına hangi agent'ın hangi skili kullanacağını yazmayı ÖNER (ben onaylarsam yaz).

Kurallar: global skill klasörlerine dokunma, skill kopyalama, benim agent dosyalarımın üzerine yazma.
```

**Not:** Codex'te bir agent'ın bazı skilleri görmemesini istersen, kendi `.toml` dosyana
`[[skills.config]] path = "<proje>/.agents/skills/<skill>/SKILL.md"` ve `enabled = false` ekleyebilirsin.
