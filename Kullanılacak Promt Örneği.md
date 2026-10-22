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
