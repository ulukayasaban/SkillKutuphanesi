# nlm — sürüm ve yer kaydı (kaynak kopyası YOK)

| Alan | Değer |
|---|---|
| Repo | https://github.com/jacob-bd/gemini-notebook-mcp-cli |
| Paket | PyPI `notebooklm-mcp-cli` (komutlar `nlm`, `notebooklm-mcp`) |
| Kayıtlı sürüm | 0.16.5 (2026-11-15 güncellendi, önceki 0.15.8; `site-packages/notebooklm_mcp_cli-0.16.5.dist-info/METADATA` içindeki `Version:` satırından okunur) |
| Lisans | MIT |
| Kayıt tarihi | 2026-11-12 (son güncelleme 2026-11-15) |
| Kurulu yer | `~/.local/share/uv/tools/notebooklm-mcp-cli` (uv tool, Python 3.12; komutlar `~/.local/bin/nlm` ve `~/.local/bin/notebooklm-mcp`) |
| Veri yeri | `~/.notebooklm-mcp-cli` (oturum ve kimlik içerir; okunmaz, yedeğe konmaz) |
| Yedek klasörü | `~/Documents/Claude/yedek/nlm-<YYYY-AA-GG>/` (güncellemeden önce; içinde `KAYIT.json`) |
| Giriş yolu | `programlar.json` → `nlm` → `giris_yolu` |
| Skil | `nlm-skill`, klasörü `…/site-packages/notebooklm_tools/data` (kartta `skill_klasorleri`); projeye bağ olarak verilir |
| Doğrulama | PyPI wheel sha256 `3c33cac11a47f59179ab170e6e06135b3aaf44c5153b5a469b6bd11157aee94f` (notebooklm_mcp_cli-0.16.5-py3-none-any.whl, PyPI JSON, 2026-11-15) |

Kaynak kopyası alınmadı: program PyPI'dan kurulan hazır pakettir ve kendi sürümünü kendi izler; kopya hemen eskirdi.
Paket kalkarsa: kayıtlı sürüm yedekteki `paket` klasöründen yeniden konur (kullanıcı onayıyla).
Yeniden edinmek için: `uv tool install --python 3.12 notebooklm-mcp-cli==<sürüm>` (yalnız kütüphane oturumu, kullanıcı onayından sonra; ayrıntı: kart `kurulum`).
Kart ve güncelleme adımları: `programlar.json` → `nlm`, rehber: `rehber/11-program-yonetimi.md`.
