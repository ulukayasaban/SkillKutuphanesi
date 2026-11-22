# Entegrasyon Kataloğu (varsayılan listede gizli) › 01-uygulama-entegrasyonlari

Composio üzerinden 800+ uygulama (Gmail, Slack, Notion…); Composio API anahtarı gerekir

[← Skill rehberi](../../README-SKILLER.md) · 1 skill · puana göre sıralı (önce tercih edilen sürümler)

**Kurulum:** `python3 araclar/skill-ekle.py <proje> --skill <id> --kuru` → raporu gör → `--evet`. Çağrı adı projede kurulan klasör adıdır (globalde aynı adlı farklı skill varsa `<ad>--kutuphane`).

| Skill | Ne yapar | Ne zaman kullanılır | Nasıl çağrılır | Puan · not |
|---|---|---|---|---|
| `caption-qa`<br><sub>github/awesome-copilot</sub> | SRT/WebVTT altyazılarını Netflix, BBC ve DCMP standartlarına göre okuma hızı, satır uzunluğu, süre ve boşluk/çakışma açısından denetler; hataları önce süre ayarıyla düzeltir. | Altyazıları doğrulamak, okuma hızını kontrol etmek, yayın standardına uyumlu hazırlamak veya CI'a kontrol eklemek istendiğinde. | Otomatik · Claude `/caption-qa` · Codex `$caption-qa` | 95 A · kısmen ücretli |
