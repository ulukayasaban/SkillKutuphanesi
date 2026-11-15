# video-use

> Bu dosya SkillKutuphanesi tarafından eklendi; skill'in kendi dosyaları değiştirilmedi.

- **Kaynak repo:** https://github.com/browser-use/video-use
- **Repo içindeki yol:** `(kök)`
- **Commit:** `43cfc566833548093455c9d4a46bd69913b7e552`
- **Lisans:** MIT
- **Geliştirici:** browser-use (kurum)
- **Arşive alınma:** 2026-11-15
- **Durum:** tercih
- **Bağımlılık:** video-use skili ElevenLabs Scribe API'si ister (ELEVENLABS_API_KEY; ücretsiz kota var, yoğun kullanım ücretli) + ffmpeg/ffprobe + Python (requests, librosa, matplotlib, pillow, numpy). Animasyon için isteğe bağlı HyperFrames/Remotion/Manim/yt-dlp (ilk kullanımda npx --yes ile kurulur). Paralel animasyon alt-ajanları Claude Code'un Agent/alt-ajan aracına dayanır (Codex'te bu kısım çalışmaz; temel transkript/kesim/render çalışır). Kurulum kontrolleri SKILL.md 'Setup' bölümünde, bağımlılıklar pyproject.toml'da. install.md arşive alınmaz: global skill klasörüne (~/.claude/skills, ~/.codex/skills) symlink kurma talimatı verir (kural 1), oysa skill projeye skill-ekle.py ile kurulur.
- **Arşive alınmayan dosyalar (7):** `install.md`, `poster.html`, `static/timeline-view.svg`, `static/video-use-banner.png`, `tests/test_render_captions.py`, `tests/test_render_fps.py`, `tests/test_render_orientation.py`
