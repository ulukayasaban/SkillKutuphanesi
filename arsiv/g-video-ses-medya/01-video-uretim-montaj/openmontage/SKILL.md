---
name: openmontage
description: Route ANY video production request to the locally installed OpenMontage studio — make/create/produce/generate a video, explainer, montage, documentary, trailer, clip, animation, stok görüntülü video, seslendirmeli video, altyazı, YouTube indirme/transkript, arka plan silme, upscale. Also triggers on Turkish phrasing ("video yap", "video üret", "montaj", "explainer hazırla", "seslendir", "altyazı bas"). Works from ANY working directory; OpenMontage lives at a fixed path and its keys are stored globally.
argument-hint: [what you want made, e.g. "60 s documentary montage about a rainy city, Turkish narration"]
---

# OpenMontage — entry point

OpenMontage is installed once, here:

```
OPENMONTAGE_HOME = /Users/sabanulukaya/.openmontage
Python           = /Users/sabanulukaya/.openmontage/.venv/bin/python
API keys         = /Users/sabanulukaya/.config/openmontage/.env   (repo .env is a symlink to it)
Default output   = /Users/sabanulukaya/Movies/OpenMontage/<project-id>/
```

## Mandatory first steps (every time, in this order)

1. `Read /Users/sabanulukaya/.openmontage/AGENT_GUIDE.md` — it is the operating contract (Rule Zero: all production goes through a pipeline in `pipeline_defs/`; read the stage director skill before each stage; never write ad-hoc Python around the tools).
2. Run preflight from the repo root (see command pattern below) and present the provider menu.
3. Then proceed exactly as AGENT_GUIDE.md instructs. The Layer-3 skills live in `$OPENMONTAGE_HOME/.agents/skills/` and are no longer linked into the machine-wide skills folder. A project gets only the ones it needs, as links made through the SkillKutuphanesi library: `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py <project> --program-skill openmontage:<name>` (for example `ffmpeg`, `video-edit`, `manim-composer`, `visual-style`). If a Layer-3 skill is not in this project's skill list, Read its `SKILL.md` straight from `$OPENMONTAGE_HOME/.agents/skills/<name>/` when AGENT_GUIDE points to it, and tell the user it can be linked into the project. Do not link OpenMontage's own `hyperframes`, `hyperframes-*` or `motion-graphics` copies: they are an older generation; HyperFrames skills come from the HyperFrames package through the library. Pipeline director skills (`$OPENMONTAGE_HOME/skills/pipelines/<pipeline>/*-director.md`) and meta skills (`$OPENMONTAGE_HOME/skills/meta/*.md`) are NOT skills in the Claude sense — Read them by path when AGENT_GUIDE points to them.

## Command pattern — ALWAYS run from the repo root with the venv python

Everything in the repo (skills, commands, `python tools/...`, `python -m backlot`) assumes cwd = repo root. Never call system `python`. **Two things fail silently-looking if you skip the `cd`: `.venv/bin/python` is "no such file" and `import lib`/`import tools` raise ModuleNotFoundError** (verified). So EVERY Bash call starts with the cd — put it on its own line, do not rely on a previous call's cwd (the tool resets it):

```bash
cd /Users/sabanulukaya/.openmontage
PATH="/Users/sabanulukaya/.openmontage/.venv/bin:/usr/local/opt/ffmpeg-full/bin:$PATH" OPENMONTAGE_PROJECTS_DIR="${OPENMONTAGE_PROJECTS_DIR:-/Users/sabanulukaya/Movies/OpenMontage}" .venv/bin/python <...>
```

- `PATH` prefix is required so `piper`, `manim`, `faster-whisper` binaries in the venv are found (piper_tts shows "unavailable" without it).
- Preflight: `... .venv/bin/python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.provider_menu(), indent=2))"`
- Backlot board: `... .venv/bin/python -m backlot open`

## Slash-style requests (the old `/openmontage`, `/backlot`, `/ink-art`, `/animated-drawing`, `/reel` commands)

These used to be separate machine-wide command files; they are no longer needed, because this skill is the entry point (invoke it as `/openmontage <request>`). When the user asks for one of them, run the matching instructions from the OpenMontage home (cwd = repo root, command pattern above):

| User asks for | What it actually does | Read and follow |
|---|---|---|
| `/openmontage <request>`, any video request | Full production through a pipeline, free tier only (stock footage + local tools; no paid AI video generation), output under the default output location | this skill, then `AGENT_GUIDE.md` |
| `/backlot [project-id]` | Opens the Backlot living storyboard in the browser (no id = library of all projects). Idempotent; it only observes, so if it fails report it and continue | `.claude/commands/backlot.md`; run `... .venv/bin/python -m backlot open [project-id]` with the command pattern above |
| `/ink-art <what to animate>` | Hand-drawn ink-on-white doodle: a character that draws itself then walks/dances/waves, or a contraption explainer; rendered through HyperFrames to MP4 | `.claude/commands/ink-art.md`, `skills/creative/ink-theater.md`, `ink-theater/README.md` |
| `/animated-drawing <drawing path> <dance\|walk\|jump\|wave>` | Animates a SUPPLIED drawing or photo of a character with real motion capture (Meta AnimatedDrawings). To CREATE a doodle from scratch use ink-art. Resolve the drawing path against the CURRENT working directory before handing it to the tools | `.claude/commands/animated-drawing.md`, `skills/creative/animated-drawing.md` |
| `/reel <request>` | The program's own generic command: treat the request as a full OpenMontage production | `.claude/commands/reel.md` |

All paths in the last column are relative to `$OPENMONTAGE_HOME`. Outputs go under `${OPENMONTAGE_PROJECTS_DIR:-/Users/sabanulukaya/Movies/OpenMontage}/<project-id>/`.

## Output location

- Default: `/Users/sabanulukaya/Movies/OpenMontage/<project-id>/` (set via `OPENMONTAGE_PROJECTS_DIR`, also in the global .env).
- If the user is working inside another project and wants the video next to that project, set `OPENMONTAGE_PROJECTS_DIR=<that project>/openmontage-projects` for the run and tell them where it landed.
- Always pass explicit `output_path` under the project dir, per AGENT_GUIDE "Project Directory Convention".

## What is actually available on THIS machine (free tier only — do not assume more)

Snapshot of 2026-09-08 (run preflight for the current state; the program was updated since, see the `openmontage` card in the library's `programlar.json`). Verified then by running every tool once: **60/117 available, 54 pass, 6 blocked by provider accounts** (see below). All local models are now downloaded (u2net, Real-ESRGAN, GFPGAN+facexlib, CLIP, faster-whisper, Piper Turkish) — first-run downloads are done. The user wants to stay **free**; the remaining 57 tools need paid providers (fal.ai, Kling, Runway, HeyGen, Suno, Sora, MiniMax, Replicate) that are NOT configured — do not propose them as if they were.

| Works | Notes |
|---|---|
| Pexels, Pixabay, Unsplash | Primary footage/image source. Prefer stock-footage pipelines. |
| ElevenLabs TTS | **BLOCKED — 402 Payment Required** on this account even though the quota shows 14/10000 used. `music_gen` (same account) too. Do not plan around them. |
| Google AI Studio | Text (`gemini-3.6-flash`) fine. **Image generation: only a few requests/day, then 429.** **Veo video: closed on free tier (429).** The registry marks `google_imagen` / `gemini_omni_video` "available" because a key exists — it does NOT check quota. Warn the user before relying on them. |
| HuggingFace | Speaker diarization. |
| **Turkish narration** | Use `piper_tts` with `model="/Users/sabanulukaya/.piper/models/tr_TR-dfki-medium.onnx"` (absolute path required; it is the only Turkish Piper voice). `google_tts` returns 401 — the Google key is an AI Studio key, not enabled for Cloud Text-to-Speech. |
| **Music** | `pixabay_music` works but is flaky (scrapes the site; occasional 403). `google_music` 429, `music_gen` 402. If music matters, ask the user to drop an mp3 into `music_library/`. |
| Local (no key) | ffmpeg suite, Remotion, HyperFrames, Manim (`math_animate`), Piper TTS, faster-whisper, yt-dlp, rembg (`bg_remove`), realesrgan/gfpgan (`upscale`, `face_restore`), mediapipe (`face_tracker`), torch CPU-only (slow: Intel Mac, no GPU). |

### Session hygiene learned 2026-09-08 (apply without re-discovering)

- **`transcriber` crashes** with `OMP Error #15` (duplicate libiomp5) unless you set `KMP_DUPLICATE_LIB_OK=TRUE`. Its Turkish word accuracy at `base` is poor — use its word *timings* but the script *text* for captions.
- **ffmpeg**: the PATH prefix above puts the keg-only `ffmpeg-full` first. The plain `/usr/local/bin/ffmpeg` (Homebrew 9.x) has **no `drawtext` / `subtitles` / `ass`** filters, which breaks `showcase_card` and SRT burn-in. Keep the prefix.
- **Remotion**: `backgroundVideo` / `backgroundImage` props are NOT auto-staged by `video_compose` (only `source`/`src`/`backgroundSrc`). Copy such files into `remotion-composer/public/<project>/` and reference the relative path, or the render dies on a `file://` URL.
- **`edit_decisions` cut schema rejects Remotion scene props** (`type`, `text`, `steps`, `chartData`…). Keep the schema-valid EDL in the checkpoint and the rich composition in `artifacts/composition.json`, then merge the two when calling `video_compose` render.
- **Local repo patches**: the authoritative list is `yerel_yamalar` in the `openmontage` card of the library's `programlar.json` (installed commit `fecb9a1e`, updated 2026-11-12). Today `video_understand`, `lib/clip_embedder`, `screen_recorder`, `remotion-composer/src/components/StatReveal.tsx` and `.agents/skills/gsap-plugins/SKILL.md` carry local changes. `face_restore` and `Explainer.tsx` were left in the new upstream version on purpose; `remotion_caption_burn` has no local patch now. A `git pull` may revert the patched files: updates go through the library (`program-denetim.py --oncesi openmontage`), never by hand.
- **Per-tool input quirks**: `video_compose` overlay wants `overlays` (not the documented `overlay_assets`); `direct_clip_search` wants `queries` as objects; `character_spec_generator` wants `style` as a dict; `threejs_world` uses `world` + `camera_path` with `time` keys.
- A full Remotion render of a ~100 s 1080p explainer takes **~20 minutes** on this Intel Mac. Budget for it and run it in the background.

## Do NOT break the venv

Intel Mac: PyTorch tops out at 2.2.2 and is built against NumPy 1.x. The venv is pinned: `numpy==1.26.4`, `opencv-python==4.11.0.86`, `torch==2.2.2`, `torchvision==0.17.2`, `transformers<5`, `numba==0.62.1`, `llvmlite==0.45.1`, `jax/jaxlib==0.4.38`, `mediapipe==0.10.21`, `manim==0.19.1`. Never run `pip install -U` on these (manim's own "upgrade me" banner included). If something pulls numpy 2.x, restore with `pip install "numpy==1.26.4"` and verify `python -c "import torch,numpy;torch.from_numpy(numpy.zeros(3))"`. `basicsr/data/degradations.py` carries a one-line import patch (`functional_tensor` → `functional`); the current repo fixes the same problem itself (`tools/enhancement/_basicsr_compat.py`), so the old patch is harmless and need not be re-applied.

## Keys

Never ask the user for API keys again — they are in `/Users/sabanulukaya/.config/openmontage/.env` (backup alongside as `.env.backup-YYYYMMDD`). If a provider errors with 401, tell the user which key to refresh; do not request it be pasted into chat.
