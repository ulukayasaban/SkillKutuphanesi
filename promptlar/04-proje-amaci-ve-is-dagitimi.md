# 04 — Proje Amacı ve İşleri Agent'lara Dağıtma

**Ne zaman:** Skiller ve agent'lar kuruldu, oturum yeniden açıldı; şimdi projenin amacını kalıcı olarak yazdırıp işleri dağıtmak istiyorsun.

## 4a — Amacı proje talimat dosyasına yazdır (bir kez)

```kopyala
Projenin amacını ve kurallarını araç düzenine göre yaz: ortak düzende AGENTS.md ve CLAUDE.md dosyalarının ikisine aynı metni (Claude CLAUDE.md'yi okur, Codex ve Antigravity AGENTS.md'yi okur); yalniz-claude düzende CLAUDE.md dosyasına. Her zaman "skill-kutuphanesi" işaretli bloğun DIŞINA yaz (o bloğa dokunma):

Amaç: [ör. "Kahve dükkanı için tanıtım sitesi; ana sayfa, menü, hakkımızda, iletişim"]
Hedef kitle: [ör. "şehirdeki 20-40 yaş kahve severler"]
Teknoloji: [ör. "Next.js 16 + Tailwind v4 + GSAP"]
Başarı ölçütü: [ör. "mobilde Lighthouse performans ≥ 90, erişilebilirlik ≥ 95"]
Kısıtlar: [ör. "ücretli servis kullanılmayacak; görseller ücretsiz kaynaklardan"]
```

## 4b — Planı çıkar ve agent'lara dağıt

```kopyala
proje talimat dosyasındaki amaca göre işi adımlara böl ve PLAN.md'ye yaz. Her adım için: ne yapılacak, hangi agent yapacak
(.codex/agents ya da .claude/agents altındaki rollerden), hangi skilleri kullanacak, bitti sayılma ölçütü.
Planı bana göster; onaylarsam 1. adımdan başla. Her adım bitince sonucu doğrula (test/önizleme) ve PLAN.md'de işaretle.
```

## 4c — Tek bir işi belirli agent'a ver

```kopyala
[agent-adi] agent'ıyla şunu yap: [iş]. İlgili skilleri (SKILL.md) işe başlamadan oku ve kurallarına uy.
Bitince ne yaptığını, hangi dosyaları değiştirdiğini ve nasıl doğruladığını kısaca yaz.
```

**Not:** Rol dosyaları (`.claude/agents`, `.codex/agents`) yalnız Claude ve Codex için vardır; Antigravity, Cursor ve Copilot'ta her agent projedeki tüm skilleri görür.

**Örnek:** `ui-tasarimci agent'ıyla ana sayfanın renk paletini ve tipografisini belirle; sonucu DESIGN.md'ye yaz.`
Belirli bir skili açıkça kullandırmak: mesajına `$skill-adi` ekle (ör. `$gsap-react`).
