# 06 — Ücretsiz Yol Önceliği

**Ne zaman:** Projede ücretli servis (ElevenLabs, HeyGen, Kling, Seedance, Gemini/OpenAI API, Azure…) kullanılmasını istemiyorsun ya da
sadece onayınla kullanılsın istiyorsun. Ücretli/kısmen ücretli skiller listesi: `~/Documents/SkillKutuphanesi/notlar/ucretli-skiller.md`.

## 6a — Proje kuralı olarak yaz (bir kez)

```kopyala
AGENTS.md'ye "skill-kutuphanesi" bloğunun DIŞINA şu kuralı ekle:

## Ücret kuralı
- Önce ücretsiz/yerel yol: seslendirme, müzik, ses efekti, transkript, görsel ve video için media-use'un ücretsiz yollarını
  (Kokoro TTS, yerel MusicGen, Openverse SFX, Whisper/Parakeet, yerel FLUX/LTX, yerel ComfyUI — Partner Nodes hariç) kullan.
- Ücretli bir API/servis çağırmadan ÖNCE dur, hangi servis, neden gerekli ve tahmini maliyeti söyle, onayımı bekle.
- API anahtarlarını asla koda, commit'e ya da sohbete yazma; .env kullan ve .env'i git'e ekleme.
- Lisans koşulu olan araçlarda (Remotion şirket lisansı, LTX topluluk lisansı, Adobe Substance) önce beni uyar.
```

## 6b — Kurulumda ücretli skillerden kaçın

```kopyala
Skill kurarken ÜCRETLİ olanları seçme. --kuru raporundaki 'ucretli' uyarısı alan her skill için ücretsiz alternatifini bul
(notlar/ucretli-skiller.md ve --oner), listeden çıkar ve ön kontrolü tekrar çalıştır. Ücretli bir skill gerçekten gerekiyorsa
nedenini ve ücretsiz alternatifin neden yetmediğini yaz, onayımı bekle.
```
