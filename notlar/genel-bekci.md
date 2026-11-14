# Genel Klasör Bekçisi Raporu

> `araclar/genel-bekci.py` üretir · 2026-11-14 · salt okuma; kural: `rehber/12-genel-klasor-bosaltma.md`

```
Genel klasör bekçisi: SORUN (sorun: 3, dikkat: 2)
YENİ      ~/.agents/.skill-lock.json (dosya, sahip: skills aracı)
YENİ      ~/.agents/skills/microsoft-foundry (klasör, sahip: skills aracı)
HYPERFRAMES_SKIP_SKILLS satırı: 3 dosyanın 2'sinde var. EKSİK: ~/.zshrc (satır yok)
KAYIP     ~/.claude/agents/colab-izleme.md (kalacak girdi yok)
KAYIP     ~/.claude/agents/kopru-izleme.md (kalacak girdi yok)
Karar bekleyen:
  - Yeni girdi ~/.agents/.skill-lock.json (sahip: skills aracı): kalacak mı, boşaltılacak mı? Karar sonrası: --taban-yaz --yenile --evet (onay gerekir).
  - Yeni girdi ~/.agents/skills/microsoft-foundry (sahip: skills aracı): kalacak mı, boşaltılacak mı? Karar sonrası: --taban-yaz --yenile --evet (onay gerekir).
  - HYPERFRAMES_SKIP_SKILLS satırı ~/.zshrc içine eklensin mi? (ayar dosyası: onay gerekir; ajan kendi eklemez)
```
