# 03-web-arastirma-veri — AI ve Otomasyon

_Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **1/3**

### agent-reach  ·  Panniantong/Agent-Reach @ 7a38047  ·  puan 98 (A)

- **Ne yapar:** İnternet erişimi için yönlendirici: 16 platformda (web arama/Exa, Twitter/X, Reddit, YouTube, Bilibili, Xiaohongshu, V2EX, LinkedIn, GitHub kod arama, RSS, podcast, hisse verisi) çoklu arka uçla (OpenCLI, platform CLI'ları, API'ler) içerik okur. `agent-reach doctor --json` ile hangi kanalın çalıştığını denetler; kategori başına references/ dosyaları var. SKILL.md Çince, SKILL_en.md İngilizce.
- **Ne zaman:** Çok platformlu web/sosyal medya araştırması, 'internette ne konuşuluyor' taraması, URL'den içerik okuma. · **Ne zaman değil:** Yazma işlemleri (gönderi, yorum, beğeni) için değil; agent-reach CLI kurulmamışsa. Açıklamadaki 'MUST USE' tetikleme dili her URL'de devreye girer — yalnızca araştırma rolüne ver. Giriş gerektiren platformlar tarayıcı çerezi okuyabilir; gizlilik açısından dikkat.
- **Teknoloji:** python, cli, web-arama · **Paketler:** agent-reach CLI (pip/uv), platforma göre: OpenCLI, yt-dlp, gh, Exa API
- **Claude / Codex:** tam / tam
- **Geliştirici:** Panniantong (kisi, ★107638, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-arastirma → birincil · **Roller:** ai-entegrasyon, icerik-pazarlama
- **Boyut:** 23 KB (SKILL.md 7.0 KB, yük kucuk)
- **İnceleme:** yeniden-incelenecek · kalite 4/5 — Karar: TUT (birincil). Çok kanallı, doctor ile kendini denetleyen, hata durumunda yeniden deneme zinciri tanımlı; MIT. Eksi: varsayılan SKILL.md Çince (İngilizce sürüm SKILL_en.md içinde) ve Çin platformlarına ağırlık veriyor.

### graphify  ·  Graphify-Labs/graphify @ 32e5efe  ·  puan 97 (A)

- **Ne yapar:** Use for any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the question should be treated as a graphify query first. Turns any input (code, docs, papers, images, videos) into a persistent knowledge graph with god nodes, community detection, and query/path/explain tools.
- **Teknoloji:** api-anahtari, git, html, node, obsidian, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Graphify-Labs (kurum, ★140568, son güncelleme 2026-11-01, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 5655 KB (SKILL.md 47.3 KB, yük buyuk) · **Bağımlılık:** graphify Python paketi (pip install graphifyy) kurulu olmalı.
- **İnceleme:** otomatik

### notebooklm  ·  teng-lin/notebooklm-py @ 7db1000  ·  puan 85 (A)

- **Ne yapar:** Google NotebookLM (Gemini Notebook) için notebooklm-py CLI ve async Python API'si: kurulum, kimlik doğrulama (master token, tarayıcı çerezi), not defteri/kaynak yönetimi, kaynaklara dayalı sohbet ve derin araştırma, sesli özet/podcast gibi artefakt üretimi ve indirme; yetki sınırları ve hata giderme kuralları.
- **Ne zaman:** Belgeleri NotebookLM'e yükleyip kaynaklı soru-cevap, derin araştırma ya da Audio Overview/podcast üretmek; bunu otomasyona bağlamak. · **Ne zaman değil:** Genel Gemini API işleri için değil; resmi olmayan bir istemci (Google hesap çerezleri/master token kullanır) — kurumsal hesapta politikaya aykırı olabilir.
- **Teknoloji:** python, notebooklm, cli · **Paketler:** notebooklm-py[browser] (pip, Python 3.10+), Google hesabı oturumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** teng-lin (kisi, ★20059, son güncelleme 2026-11-01, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-arastirma → tamamlayıcı · **Roller:** icerik-pazarlama
- **Boyut:** 16 KB (SKILL.md 16.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kimlik doğrulama ve yetki sınırları özenle yazılmış, --json ve açık ID kullanımı ile güvenli otomasyon; MIT. Resmi olmayan API riski taşıyor.
