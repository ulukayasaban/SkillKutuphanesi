# nlm — sürüm ve yer kaydı (kaynak kopyası YOK)

| Alan | Değer |
|---|---|
| Repo | https://github.com/jacob-bd/gemini-notebook-mcp-cli |
| Paket | PyPI `notebooklm-mcp-cli` (komutlar `nlm`, `notebooklm-mcp`) |
| Kayıtlı sürüm | 0.16.6 (2026-11-25 güncellendi, önceki 0.16.5; `site-packages/notebooklm_mcp_cli-0.16.6.dist-info/METADATA` içindeki `Version:` satırından okunur) |
| Lisans | MIT |
| Kayıt tarihi | 2026-11-12 (son güncelleme 2026-11-25) |
| Kurulu yer | `~/.local/share/uv/tools/notebooklm-mcp-cli` (uv tool, Python 3.12; komutlar `~/.local/bin/nlm` ve `~/.local/bin/notebooklm-mcp`) |
| Veri yeri | `~/.notebooklm-mcp-cli` (oturum ve kimlik içerir; okunmaz, yedeğe konmaz) |
| Yedek klasörü | `~/Documents/Claude/yedek/nlm-<YYYY-AA-GG>/` (güncellemeden önce; içinde `KAYIT.json`) |
| Giriş yolu | `programlar.json` → `nlm` → `giris_yolu` |
| Skil | `nlm-skill`, klasörü `…/site-packages/notebooklm_tools/data` (kartta `skill_klasorleri`); projeye bağ olarak verilir |
| Doğrulama | PyPI wheel sha256 `db4aab31816c371f1b69b6ed6a967102f7838c56f2a9676cd9f68dc844bdcf27` (notebooklm_mcp_cli-0.16.6-py3-none-any.whl, PyPI JSON, 2026-11-25) |

Kaynak kopyası alınmadı: program PyPI'dan kurulan hazır pakettir ve kendi sürümünü kendi izler; kopya hemen eskirdi.
Paket kalkarsa: kayıtlı sürüm yedekteki `paket` klasöründen yeniden konur (kullanıcı onayıyla).
Yeniden edinmek için: `uv tool install --python 3.12 notebooklm-mcp-cli==<sürüm>` (yalnız kütüphane oturumu, kullanıcı onayından sonra; ayrıntı: kart `kurulum`).
Kart ve güncelleme adımları: `programlar.json` → `nlm`, rehber: `rehber/11-program-yonetimi.md`.
