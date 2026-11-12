# 01 — Yeni Projeye Skill ve Agent Kurulumu

**Ne zaman:** Yeni bir projeye başlıyorsun; skilleri ve hazır agent rollerini kütüphaneden kurmak istiyorsun.
**Nerede:** Codex Desktop ya da Claude Code, **proje klasörü açıkken**.
**Önce:** Proje klasörü var olmalı (`mkdir -p ~/Projeler/proje-adi`). Profil ve rol listesi: `~/Documents/SkillKutuphanesi/notlar/roller-ve-profiller.md`.

```kopyala
Bu projeye skill kütüphanemden skill ve agent rolleri kuracağız. Kütüphane: ~/Documents/SkillKutuphanesi
Önce ~/Documents/SkillKutuphanesi/AGENTS.md dosyasını oku ve oradaki akışı ATLAMADAN uygula.

Proje: [projenin amacı, ör. "kahve dükkanı için tanıtım sitesi"]
Teknoloji: [ör. Next.js + Tailwind + GSAP]
İstediğim agent'lar: [ör. ui-tasarimci, motion-gelistirici, frontend-muhendis, qa-erisilebilirlik — bilmiyorsan "sen öner" yaz]

0. ARAÇ SORUSU (bekle): "Bu proje hangi araçlarla açılacak? Claude Code, Codex, Antigravity, Cursor, VS Code Copilot; Windows'ta da açılacak mı?"
   Cevabıma göre: Codex ya da Antigravity varsa --arac ortak; yalnız Claude (Cursor/Copilot olabilir) --arac yalniz-claude;
   Windows'ta açılacaksa yalniz-claude (Codex/Antigravity görmez, nedeni rehber/14 bölüm 5); bilmiyorsam ortak.
   Seçimi 2. ve 3. adımdaki komutlara --arac <düzen> olarak ekle ve raporda arac-duzeni, arac-gormez ve arac-secimi-yok satırlarını bana ayrıca göster.
1. Öneri al ve bana uygun profil/rolleri öner:
   python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --oner "[proje amacı ve teknoloji]"
2. Ön kontrol (hiçbir şey kurmaz):
   python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --profil [profil] [--rol ...] [--skill ...] --arac [ortak|yalniz-claude] --kuru
3. Raporu bana olduğu gibi göster ve özellikle şunları ayrı ayrı açıkla:
   - kurulacak skiller ve hangi agent'a gittikleri
   - HATA satırları (varsa kurulum YAPMA, nedenini ve seçenekleri söyle)
   - ÇAKIŞMA uyarıları: ortusme, ayni-skill-iki-surum, ekli-ad (globalde farklı sürüm; genel klasörler boş, yalnız orada bir şey yeniden belirirse), projede-kendi-skillin, kendi-agent-dosyan
   - ÜCRETLİ skiller (ucretli uyarısı) ve ücretsiz alternatifleri
   - ek-aday listesi (kütüphanede ilgili olup seçilmeyen skiller)
   - arac-duzeni, arac-gormez, arac-secimi-yok satırları (hangi araç skilleri görür, hangisi görmez)
   - OpenMontage/HyperFrames skilleri kopyalanmaz: --program-skill PROGRAM:AD ile BAĞ verilir; kaynağı artık hiçbir yerde verilmeyen eski skil --dondur <yol> ile dondurulur (rehber/01)
4. Ben onay verene kadar BEKLE. Onaylarsam aynı komutu --evet ile çalıştır, sonra --dogrula sonucunu göster.
5. Bittiğinde bana "Claude/Codex/Antigravity/Cursor oturumunu yeniden aç" diye hatırlat.

Kurallar: global skill klasörlerine (~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage) dokunma,
skill dosyalarını elle kopyalama; sadece bu aracı kullan. --zorla'yı ben istemedikçe kullanma.
```

**Beklenen sonuç:** `ortak` düzende projede `.agents/skills/`, `.claude/skills/`, `.claude/agents/<rol>.md`, `.codex/agents/<rol>.toml`,
`AGENTS.md`/`CLAUDE.md` içinde skill tablosu ve `.skill-kutuphanesi/kilit.json`; `yalniz-claude` düzende yalnız `.claude/skills/`, `.claude/agents/`, `CLAUDE.md` ve kilit. Oturumu yeniden açınca agent'lar ve skiller görünür.

**Örnek doldurulmuş hâller:**
- Tanıtım sitesi: `--profil landing-page`
- 3D ürün sitesi: `--profil 3d-urun-sergisi`
- Video: `--profil urun-tanitim-videosu` (ücretsiz yol önceliklidir; bkz. 06)
- Next.js uygulaması: `--profil nextjs-web-uygulamasi`
- Backend: `--profil backend-api-servisi`
