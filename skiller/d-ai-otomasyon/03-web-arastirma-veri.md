# AI ve Otomasyon › 03-web-arastirma-veri

Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma

[← Skill rehberi](../../README-SKILLER.md) · 3 skill · puana göre sıralı (önce tercih edilen sürümler)

**Kurulum:** `python3 araclar/skill-ekle.py <proje> --skill <id> --kuru` → raporu gör → `--evet`. Çağrı adı projede kurulan klasör adıdır (globalde aynı adlı farklı skill varsa `<ad>--kutuphane`).

| Skill | Ne yapar | Ne zaman kullanılır | Nasıl çağrılır | Puan · not |
|---|---|---|---|---|
| `agent-reach`<br><sub>Panniantong/Agent-Reach</sub> | Çok platformlu salt-okunur içerik erişimi için tek CLI (`agent-reach <kanal> <eylem>`, `read <url>`): GitHub, YouTube, Bilibili, Reddit, X/Twitter, Xiaohongshu, Instagram, Facebook, LinkedIn, V2EX, Xueqiu, podcast ve anonim web arama/okuma. JSON çıktı ve hata… | Çok platformlu web/sosyal medya araştırması, URL'den içerik okuma, YouTube/Bilibili altyazısı, iş ilanı ve hisse verisi okuma, podcast transkripsiyonu. | Otomatik · Claude `/agent-reach` · Codex `$agent-reach` | 98 A |
| `graphify`<br><sub>Graphify-Labs/graphify</sub> | Kod, mimari ve dosya ilişkileri hakkındaki soruları; kod, doküman, makale, görsel ve videolardan kalıcı bilgi grafiği üretip sorgulayarak yanıtlar. | Kod tabanı, proje içeriği veya dosya ilişkileri sorulduğunda; graphify-out/ klasörü varsa soruyu önce graphify sorgusu olarak ele al. | Otomatik · Claude `/graphify` · Codex `$graphify` | 97 A · kısmen ücretli, Codex: uyarlanabilir |
| `notebooklm`<br><sub>teng-lin/notebooklm-py</sub> | Google NotebookLM (Gemini Notebook) için notebooklm-py CLI ve async Python API'si: kurulum, kimlik doğrulama (master token, tarayıcı çerezi), not defteri/kaynak yönetimi, kaynaklara dayalı sohbet ve derin araştırma, sesli özet/podcast gibi artefakt üretimi ve… | Belgeleri NotebookLM'e yükleyip kaynaklı soru-cevap, derin araştırma ya da Audio Overview/podcast üretmek; bunu otomasyona bağlamak. | Otomatik · Claude `/notebooklm` · Codex `$notebooklm` | 85 A · kısmen ücretli |
