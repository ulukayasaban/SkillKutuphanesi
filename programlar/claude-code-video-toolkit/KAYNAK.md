# claude-code-video-toolkit — sürüm ve yer kaydı (kaynak kopyası YOK, bu bilgisayarda kurulu değil)

| Alan | Değer |
|---|---|
| Repo | https://github.com/digitalsamba/claude-code-video-toolkit |
| Kayıtlı commit | `01e85f4bbf5b3edffc7f8138406f3acc1dc43c66` (dal `main`; v0.29.1 etiketinin 4 commit ilerisi; kurulacak onaylı commit) |
| Lisans | MIT |
| Kayıt tarihi | 2026-11-15 |
| Kurulu yer | yok (2026-11-15 ölçümü). Kurulursa `~/claude-code-video-toolkit` (skillerin varsayılan kökü; başka yer için `VIDEO_TOOLKIT_ROOT`) |
| Anahtarlar | toolkit kökündeki `.env`, `_internal/.youtube`, `~/.modal.toml` (açılmaz, yazdırılmaz) |
| Yedek klasörü | `~/Documents/Claude/yedek/claude-code-video-toolkit-<YYYY-AA-GG>/` (güncellemeden önce; içinde `KAYIT.json`) |
| Giriş yolu | `programlar.json` → `claude-code-video-toolkit` → `giris_yolu` (karar bekliyor) |
| Doğrulama | commit `01e85f4bbf5b3edffc7f8138406f3acc1dc43c66` (tam sha; dal adıyla onay verilmez) |
| Skiller | 16 skill kütüphane arşivinde (`kaynaklar.json` T2 kaydı); projeye `skill-ekle.py` ile kopya olarak kurulur, program bağı yok |

Kaynak kopyası alınmadı: toolkit bir çalışma alanıdır (kendi uv ortamı, şablon `node_modules`, kullanıcının `projects/`, `jobs/`, `kits/`
klasörleri ve kökte `.env`); skiller araçları bu kökten çalıştırır, kütüphanedeki bir kopya kullanılamazdı. Skill dosyaları zaten
arşivdedir. Yeniden edinmek için: `git clone https://github.com/digitalsamba/claude-code-video-toolkit` ve kayıtlı commit'e geçmek,
sonra `uv sync --frozen` (yalnız kütüphane oturumu, kullanıcı onayıyla; ayrıntı: kart `kurulum`).
`scripts/migrate_to_codex.py` ve `scripts/migrate_to_kiro.py` genel skill klasörlerine yazar; çalıştırılmaz (kart `asla`).
Kart ve güncelleme adımları: `programlar.json` → `claude-code-video-toolkit`, rehber: `rehber/11-program-yonetimi.md`.
