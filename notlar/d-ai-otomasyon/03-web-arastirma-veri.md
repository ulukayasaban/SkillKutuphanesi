# 03-web-arastirma-veri — AI ve Otomasyon

_Web/sosyal medya okuma, araştırma, NotebookLM, veri çıkarma_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **2/3**

### agent-reach  ·  Panniantong/Agent-Reach @ 7a38047  ·  puan 98 (A)

- **Ne yapar:** Çok platformlu salt-okunur içerik erişimi için tek CLI (`agent-reach <kanal> <eylem>`, `read <url>`): GitHub, YouTube, Bilibili, Reddit, X/Twitter, Xiaohongshu, Instagram, Facebook, LinkedIn, V2EX, Xueqiu, podcast ve anonim web arama/okuma. JSON çıktı ve hata kodlarıyla çalışır; tarayıcı gerektiren kanallar ortak özel tarayıcıyı (CloakBrowser/Chrome + OpenCLI) kullanır. Önce agent'ın kendi araçlarını dener, Reach boşlukları doldurur. SKILL.md Çince (SKILL_en.md İngilizce).
- **Ne zaman:** Çok platformlu web/sosyal medya araştırması, URL'den içerik okuma, YouTube/Bilibili altyazısı, iş ilanı ve hisse verisi okuma, podcast transkripsiyonu. · **Ne zaman değil:** Yazma işlemleri (gönderi, yorum, beğeni) için değil; agent-reach CLI kurulu değilse (kanal tablosu kurulumda doldurulan şablon). Gizlilik: kullanıcının Chrome'una OpenCLI eklentisi bağlıysa o sitenin giriş çerezleri özel tarayıcıya kopyalanır; açık onay olmadan kurma. 2026-11'de eski Exa/RSS/jina/yt-dlp doğrudan komutları kaldırıldı.
- **Teknoloji:** python, cli, web-arama · **Paketler:** agent-reach CLI (pip/uv; browser setup ile Node, OpenCLI, CloakBrowser/Chrome indirilir), platforma göre: yt-dlp, gh, bili CLI, opsiyonel: Groq anahtarı (podcast transkripsiyonu), github-token, proxy
- **Claude / Codex:** tam / tam
- **Geliştirici:** Panniantong (kisi, ★108808, son güncelleme 2026-11-04, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-arastirma → birincil · **Roller:** ai-entegrasyon, icerik-pazarlama
- **Boyut:** 23 KB (SKILL.md 7.0 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. 2026-11 yeniden yazımı: hata kodlarına göre dallanan akış, döngüsel yeniden deneme yasağı, 'yazma/giriş/şifre isteme yok' çizgileri, önce yerleşik araç ilkesi; MIT. Eksiler: SKILL.md varsayılan Çince, CLI kurulumu şart, tarayıcı indirme ve çerez kopyalama ile izin yüzeyi büyüdü; RSS, Exa genel arama ve bazı yorum okuma eylemleri artık yok.

### graphify  ·  Graphify-Labs/graphify @ 32e5efe  ·  puan 98 (A)

- **Ne yapar:** Use for any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the question should be treated as a graphify query first. Turns any input (code, docs, papers, images, videos) into a persistent knowledge graph with god nodes, community detection, and query/path/explain tools.
- **Teknoloji:** api-anahtari, git, html, node, obsidian, python, typescript _(otomatik tespit)_
- **Claude / Codex:** tam / uyarlanabilir — Claude'a özgü araç adları geçiyor (); Codex mantığı uygular, araç adlarını kendi karşılığıyla yorumlar
- **Geliştirici:** Graphify-Labs (kurum, ★142439, son güncelleme 2026-11-03, lisans Apache-2.0)
- **Durum:** tercih
- **Boyut:** 5655 KB (SKILL.md 47.3 KB, yük buyuk) · **Bağımlılık:** graphify Python paketi (pip install graphifyy) kurulu olmalı.
- **İnceleme:** otomatik

### notebooklm  ·  teng-lin/notebooklm-py @ 7db1000  ·  puan 85 (A)

- **Ne yapar:** Google NotebookLM (Gemini Notebook) için notebooklm-py CLI ve async Python API'si: kurulum, kimlik doğrulama (master token, tarayıcı çerezi), not defteri/kaynak yönetimi, kaynaklara dayalı sohbet ve derin araştırma, sesli özet/podcast gibi artefakt üretimi ve indirme; yetki sınırları ve hata giderme kuralları.
- **Ne zaman:** Belgeleri NotebookLM'e yükleyip kaynaklı soru-cevap, derin araştırma ya da Audio Overview/podcast üretmek; bunu otomasyona bağlamak. · **Ne zaman değil:** Genel Gemini API işleri için değil; resmi olmayan bir istemci (Google hesap çerezleri/master token kullanır) — kurumsal hesapta politikaya aykırı olabilir.
- **Teknoloji:** python, notebooklm, cli · **Paketler:** notebooklm-py[browser] (pip, Python 3.10+), Google hesabı oturumu
- **Claude / Codex:** tam / tam
- **Geliştirici:** teng-lin (kisi, ★20096, son güncelleme 2026-11-03, lisans MIT)
- **Durum:** tercih · **Örtüşme:** web-arastirma → tamamlayıcı · **Roller:** icerik-pazarlama
- **Boyut:** 16 KB (SKILL.md 16.0 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Kimlik doğrulama ve yetki sınırları özenle yazılmış, --json ve açık ID kullanımı ile güvenli otomasyon; MIT. Resmi olmayan API riski taşıyor.
