# 09 — Proje Taşındı, Skiller Görünmüyor ya da Bir Şey Bozuldu

```kopyala
Bu projedeki kütüphane skillerinde sorun var: [ör. "klasörü taşıdım" / "Codex skilleri görmüyor" / "bir agent dosyası bozuldu"].
Kütüphane: ~/Documents/SkillKutuphanesi. Önce teşhis koy, sonra onayımla düzelt:
1. python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py "$PWD" --dogrula   → sorunları listele ve açıkla
2. Duruma göre öner:
   - proje taşındı / Codex yolları geçersiz / AGENTS.md bloğu bozuk → --yenile
   - eksik/bozuk symlink ya da kopya → --guncelle --kuru, onaylarsam --guncelle --evet
   - yanlış işlem yapıldı → --yedekler, sonra onayla --geri-al <yedek>
3. Düzelttikten sonra --dogrula'yı tekrar çalıştır ve "oturumu yeniden aç" diye hatırlat.
Skill dosyalarını elle düzenleme ya da kopyalama; global klasörlere dokunma.
```

**Codex skilleri hâlâ görmüyorsa:** oturumu kapatıp projeyi yeniden aç; proje klasörünün kendisinde `.agents/skills/` olduğundan emin ol
(Codex, açılan klasörden repo köküne kadar `.agents/skills` arar).
