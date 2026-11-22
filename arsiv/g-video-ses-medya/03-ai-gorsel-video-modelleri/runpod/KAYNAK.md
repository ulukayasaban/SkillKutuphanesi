# runpod

> Bu dosya SkillKutuphanesi tarafından eklendi; skill'in kendi dosyaları değiştirilmedi.

- **Kaynak repo:** https://github.com/digitalsamba/claude-code-video-toolkit
- **Repo içindeki yol:** `.claude/skills/runpod`
- **Commit:** `ad8b4ecb912a9073be11e3d8aff7c158a883e1a2`
- **Lisans:** MIT
- **Geliştirici:** digitalsamba (kurum)
- **Arşive alınma:** 2026-11-22
- **Durum:** tercih
- **Bağımlılık:** claude-code-video-toolkit kökü gerekir: repo klonlanır ve `uv sync` çalıştırılır; skiller `tools/*.py` betiklerini toolkit kökünden `uv run` ile çalıştırır (`VIDEO_TOOLKIT_ROOT`, yoksa `~/claude-code-video-toolkit`). Bulut GPU araçları (seslendirme, görsel, video klip, konuşan kafa) kullanıcının Modal ya da RunPod hesabına kurulan uç noktalarını ve toolkit kökündeki `.env` anahtarlarını ister; Remotion şablonları için Node, `blender` skili için Blender gerekir.
