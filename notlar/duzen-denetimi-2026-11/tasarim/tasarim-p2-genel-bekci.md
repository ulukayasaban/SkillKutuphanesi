# P2 design: machine-wide folder watchdog and the emptying procedure

Package P2. Files owned: `araclar/genel-bekci.py`, `notlar/genel-klasor-tabani.json`, `rehber/12-genel-klasor-bosaltma.md`,
`promptlar/16-genel-klasor-bosaltma.md`, `araclar/testler/test_p2-genel-bekci.py` (all new). Nothing else is edited.
Written 2026-11-11 from read-only inspection; revised after review (section 11).

Önkoşul: (1) uncommitted `programlar/` work committed (user approval; smoke test needs a clean tree); (2) P3 done (`.gitignore`, `yedek-denetim.py` name patterns); (3) P1 keys final (this package reads none of them; it only needs P1's `rehber/14` to carry the `ek_klasorler` step). P2 is independent of P5 and P6 and is built in the same wave as them. P4 (monthly chain) and P8 (shared files) come after P2. The real emptying (`rehber/12`) comes last, after P8 and the CLAUDE/AGENTS rule-1 exception are approved and committed. Counts below are measured values (ls, wc) and are expected to drift.

Gaps: A2 (watchdog and baseline) CLOSED; A3 (procedure, backup, rollback) CLOSED as written procedure plus dry-run tool
(the real emptying stays a user-approved act, D7); critic scenario 10 (tool writes machine-wide again) CLOSED for detection
and for the "what to do" procedure; the environment part of scenario 8 CLOSED for `HYPERFRAMES_SKIP_SKILLS` only (rest of the
environment inventory is deferred, section 8).

---------------------------------------------------------------------------------------------------------------------------

## 1 Purpose

1. A read-only watchdog, `araclar/genel-bekci.py`, that lists what lives in every machine-wide skill folder of the five
   supported tools (D1) plus the neighbouring machine-wide files (lock file, slash commands, subagents, global instruction
   files), compares it with a committed baseline `notlar/genel-klasor-tabani.json`, and reports NEW / MISSING / CHANGED
   entries, with an owner for each entry. It also checks that the `HYPERFRAMES_SKIP_SKILLS` line is present in the three
   places that stop HyperFrames from re-writing skills. It runs at session start and in the monthly chain (hand-offs, section 6).
2. A written, ordered emptying procedure `rehber/12-genel-klasor-bosaltma.md` with a dependency reason, backup, check and
   rollback for each step, plus the "what to do when something reappears" procedure and the backup-deletion reminder.
3. A dry-run mode in the same tool (`--plan`, `--yedek-dogrula`) that prints the exact commands and runs the pre-checks, so a
   fresh agent with no memory does not hand-write shell commands. The tool never executes them (D7).
4. A ready prompt `promptlar/16-genel-klasor-bosaltma.md` that starts either the emptying or the "something reappeared" run.

The tool is a smoke detector, not a cleaner. Every removal, every write to a user file and every baseline write is a
separate user approval (D7, DURUM.md:15-16 "Bu söz toplu onay değildir").

---------------------------------------------------------------------------------------------------------------------------

## 2 Existing behaviour relied on (file:line)

Library code and rules
- `araclar/ortak.py:11` `KOK` is the library root (`Path(__file__).resolve().parent.parent`). New tool uses it to find
  `notlar/` and `programlar.json`.
- `araclar/ortak.py:37-41` `GLOBAL_KLASORLER` = claude, codex, agents only, read-only use; hard-wired to `Path.home()`.
  The watchdog does NOT use it (it needs a fakeable home and more folders); it defines its own table. Not edited (D5).
- `araclar/ortak.py:23` `HESAP_SKILLERI = ~/.claude/skills/synced`: the Claude account sync, read-only, owned by the app.
  Confirms `synced` is a permanent vendor entry.
- `araclar/ortak.py:44-56` `json_oku`, `json_yaz` (atomic: temp file then `os.replace`). Reused for the baseline read/write.
- `araclar/ortak.py:188` `GURULTU` regex (`.DS_Store`, `__pycache__`, `.git`, `Thumbs.db`, `.ipynb_checkpoints`, `*.pyc`). Reused as
  the noise filter, so the watchdog ignores the same noise the rest of the library ignores.
- `araclar/test.py:33-42` and `araclar/duman-testi.py:44-53` `parmak_izi()`: the only existing watching of global folders. It
  hashes names and mtimes of the three folders (+ `~/.openmontage/.agents/skills` in test.py), skips `synced` and `.system`,
  and compares the start and end of ONE run. It cannot see writes between runs (akis-08 gap 1). The watchdog adds the
  between-runs view and does not change `parmak_izi` (P8 owns that, A7).
- `araclar/test.py:1691-1693` prints `N/M test geçti` and exits 1 on any failure. The new test file copies this last-line format.
- `araclar/program-denetim.py:15-30,293-346` is the style reference for a report tool: docstring with purpose and
  "Çıkış kodu her zaman 0", `argparse`, `sys.path.insert(0, ...)` then `from ortak import ...`, `main(argv=None)`, report file
  rewritten only when the content (date stripped) changed (`:337-340`). The watchdog copies this style (including the
  date-stripped write-only-if-changed rule so the report does not create git noise).
- `programlar.json` card `hyperframes`: `skill_yazimi.yazar` (which commands write skills), `.klasorler` (writes
  `~/.claude/skills`, `~/.agents/skills`, lock `~/.agents/.skill-lock.json`, mirrors to `~/.gemini/antigravity/skills`,
  `~/.gemini/antigravity-cli/skills`, `~/.gemini/skills`, `~/.cursor/skills`, `~/.copilot/skills` when the parent exists,
  creates the `skills` folder if only the parent exists, never writes `~/.codex/skills` and deletes old HF mirror links there),
  `.durduran` (only the exact value `1` is valid; stops `skills`, `skills update`, `update`'s skill part, init's skill install
  and the background skill check; does not stop the CLI self-update), `.simdi` (key written on 2026-11-11 to `~/.zshenv`,
  `~/.zshrc`, `~/.claude/settings.json` → `env`; Dock apps that start without a shell are not covered). `.skilleri` =
  [hyperframes, hyperframes-cli, media-use, hyperframes-registry] (used only as an owner hint).
- `programlar.json` card `openmontage`: `skill_yazimi` says the OM update does not recreate the ~74 links in
  `~/.claude/skills`; they were placed by the user's manifest `~/.config/openmontage/global-skill-links.txt`.
- `rehber/11-program-yonetimi.md:57-62` backup rule: `~/Documents/Claude/yedek/<program>-<YYYY-AA-GG>/`, never in the library or git,
  "ortam değişkenini kullanıcı kendisi tanımlar". The emptying backup uses the same parent folder and naming.
- `rehber/02-guncelleme-yonergesi.md:142-144` states the key rule; its "genel klasörler boşaltılmadı" sentence is a P8/doc
  follow-up on emptying day (DURUM.md "Sonraya kalan düzeltmeler").
- `CLAUDE.md:7` hard rule 1 (never write to the global folders) conflicts with an approved emptying; the exception wording is P8's (A5), proposed in section 6.
- `notlar/hf-om-gecisi/DURUM.md`: "Boşaltma sırası (taslak)" (anahtar → giriş skili ve komut yolları → Codex bağları → `~/.claude` bağları →
  `~/.claude` gerçek klasörler → `~/.agents` kilit dosyasıyla), "İki kapı", decision of 2026-11-10 "Yedek silme hatırlatması boşaltıldığı gün kurulur",
  user decision that "Psikolojik Danışman Sosyal Medya" and the "Istatistik template/.../KIT" package need no action (D10), the open
  "küçük açık" list (5 scheduled tasks, `~/.claude/bin`, `plugin-sources`, `marketplaces`, `~/Library`).
- Existing manual backups (read-only listing): `~/Documents/Claude/yedek/global-skills-2026-11-08/` (LISTE.md, `geri-al.sh` using `mv` and fixed
  paths, `tasi.sh`, `kilit-temizle.py`, `agents-skills/`, `claude-skills-linkler/`) and `~/Documents/Claude/yedek/ayar-2026-11-11/`
  (`zshrc.yedek`, `zshenv.yedek`, `claude-settings.json.yedek`, mode 600; the zshrc backup holds a plain-text key line per DURUM.md "Yan gözlem").
  The new procedure does not reuse `geri-al.sh` (outside the library, fixed paths, `mv`-only, no link list).
- `promptlar/10-kutuphane-saglik-kontrolu.md`: prompt style (title, "Ne zaman", "Nerede", one ```kopyala block). Prompt 16 copies it.

Measured machine state (read-only `ls`, 2026-11-11, used to write realistic examples; not assumed by the tool)
- `~/.claude/skills`: 105 entries incl. `.trash` (dir) and `.DS_Store`; 81 links (74 → `~/.openmontage/.agents/skills/<ad>`, 1 → `~/.openmontage/.claude/skills/...`,
  6 → `../../.agents/skills/<ad>`); real folders: `captions-overlay changelog-video design-dna embedded-captions figma hyperframes hyperframes-animation
  hyperframes-cli hyperframes-core hyperframes-creative hyperframes-registry media-use motion-graphics music-to-video nlm-skill openmontage
  oversized-cursor remotion-to-hyperframes slideshow talking-head-recut youtube-arama synced`.
- `~/.agents/skills`: 28 folders + `.DS_Store`; `~/.agents/.skill-lock.json` (28 skills, key `skills`, entries carry `source`, `sourceType`, `sourceUrl`) and a manual `.skill-lock.json.yedek-2026-11-10`.
- `~/.codex/skills`: 11 links (8 → `../../.claude/skills/<ad>`... 3 → `../../.agents/skills/<ad>`; relative targets), real folder `playwright`, vendor `.system` (5 entries).
- `~/.gemini/skills`, `~/.cursor/skills`, `~/.copilot/skills`: exist, empty. `~/.gemini/antigravity/skills` does NOT exist (parent exists; earlier note that it has 1 entry was an `ls` error text). `~/.gemini/antigravity-cli/skills`: not checked as existing (parent exists).
- `~/.cursor/skills-cursor` vendor, ~26-29 entries. `~/.claude/commands`: 4 files (animated-drawing, backlot, ink-art, openmontage; the brief says "three", the real count is four). `~/.claude/agents`: 2 files.
- Global instruction files present: `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md` (0 bytes), `~/.gemini/GEMINI.md` (376 bytes). `~/.copilot/copilot-instructions.md`: not checked.
- NEW FINDING not in the audit: `~/.palmier/skills` (10 entries) and `~/.openmontage/skills` (5 entries) are other `~/.<x>/skills` folders. `.openmontage` is the program's own tree (ignored by design); `.palmier` is an unknown tool. The watchdog's discovery pass (3.1) reports it.

---------------------------------------------------------------------------------------------------------------------------

## 3 Changes per file (all new files; no existing file is edited)

### 3.1 `araclar/genel-bekci.py` (new, about 450-550 lines, stdlib only)

Docstring (Turkish, program-denetim style): purpose; "Salt okuma: makinedeki genel skill klasörlerine, ayar dosyalarına, kabuk dosyalarına
YAZMAZ ve hiçbir şeyi silmez, taşımaz. Yazdığı tek yerler: kütüphane içinde `notlar/genel-bekci.md` (rapor) ve yalnız `--taban-yaz --evet` ile
`notlar/genel-klasor-tabani.json`. Anahtar ve ayar dosyalarının değerlerini ASLA yazdırmaz."

Imports: `argparse, json, os, re, sys, shlex` and `from datetime import date`, `from pathlib import Path`;
`sys.path.insert(0, str(Path(__file__).parent))`; `from ortak import KOK, GURULTU, json_oku, json_yaz`.

#### 3.1.1 Fake home (`--ev`)
`ev = Path(args.ev or os.environ.get("SKILL_BEKCI_EV") or Path.home())`. EVERY machine path is `ev / <relative>`. Tests pass `--ev <tmpdir>`
and never touch the real home (D5). The baseline stores paths with a leading `~/` (never the absolute home), so the committed file is portable.
Helper `kisalt(p)` -> `"~/" + relative` when `p` is under `ev`, else `str(p)`; `ac(s)` is the inverse.

#### 3.1.2 What is watched (constants)
```python
BOLGELER = [  # (anahtar, ev'e göre yol, tür)  tür: "skill" = skill klasörü, "liste" = dosya listesi
 ("claude",   ".claude/skills",   "skill"), ("agents", ".agents/skills", "skill"), ("codex", ".codex/skills", "skill"),
 ("gemini",   ".gemini/skills",   "skill"), ("cursor", ".cursor/skills", "skill"), ("copilot", ".copilot/skills", "skill"),
 ("komutlar", ".claude/commands", "liste"), ("ajanlar", ".claude/agents", "liste"),
]
# elle sabit eklenenlere ek olarak çalışma anında bulunanlar (anahtar "gemini-<ad>"): ev/.gemini/*/skills  (antigravity, antigravity-cli, gelecekte yenileri)
# kesif (anahtar "kesif-<ad>"): ev/.*/skills klasörü olup yukarıdakilerden ve KESIF_YOKSAY'dan biri olmayan her şey (tek seviye)
KESIF_YOKSAY = {".openmontage", ".Trash", ".trash", ".npm", ".cache", ".local", ".config"}
DOSYALAR = [  # tek dosyalar
 ("kilit",   ".agents/.skill-lock.json",           "kilit"),     # 'skills' aracı ve HyperFrames kayıt dosyası
 ("talimat", ".claude/CLAUDE.md",                  "talimat"),
 ("talimat", ".codex/AGENTS.md",                   "talimat"),
 ("talimat", ".gemini/GEMINI.md",                  "talimat"),   # Gemini CLI ve Antigravity aynı dosyayı okur
 ("talimat", ".copilot/copilot-instructions.md",   "talimat"),
]
IZINLI_VARSAYILAN = [  # kalıcı izinli satıcı girdileri: taban 'girdiler'ine YAZILMAZ, YENİ/KAYIP/DEĞİŞTİ raporlanmaz
 {"yol": "~/.claude/skills/synced",   "sahip": "uygulama", "neden": "Claude uygulamasının hesap skili senkronu (ortak.py:23)"},
 {"yol": "~/.codex/skills/.system",   "sahip": "uygulama", "neden": "Codex'in kendi yerleşik skilleri"},
 {"yol": "~/.cursor/skills-cursor",   "sahip": "uygulama", "neden": "Cursor'un kendi yerleşik skilleri (skills klasörünün kardeşi; zaten izlenmez, kayıt için yazılır)"},
]
TOHUM_KALACAK = {"~/.codex/skills/playwright": ("uygulama", "Codex'in playwright kopyası (DURUM.md ölçümü); kullanıcı onayıyla kalıcı")}
SAHIPLER = ("uygulama", "kullanıcı", "hyperframes", "openmontage", "skills aracı", "bilinmiyor")
KULLANICI_ADLARI = {"openmontage", "youtube-arama", "nlm-skill", "design-dna"}   # DURUM.md "4 kişisel/başka"; tabana girince tabandaki sahip geçerlidir
```
Notes: `~/.cursor/skills-cursor` and `~/.copilot/skills` entries of the permanent list are only recorded; `izinli` list in the baseline = defaults ∪ extras the user adds by hand-editing the JSON (the user adds a vendor entry there, no code change).
Noise (`.DS_Store`, `Thumbs.db`, etc.) is skipped with `GURULTU.search(name)`. Names are never read from file contents.

`ek_klasorler` (optional list in the baseline, `[{"ad": "<kısa>", "yol": "~/.<x>/skills", "tur": "skill"}]`) adds more watched
folders without a code change; a new AI tool (P1, rehber/14) is added there with the user's approval. Preserved by `--taban-yaz --yenile`.

Discovery pass: one `os.scandir(ev)`; for each directory whose name starts with `.` and has a `skills` subdirectory that is not already
a known region and not in `KESIF_YOKSAY`, add region `kesif-<ad>` (e.g. `kesif-.palmier`). At first baseline its entries are recorded with
`sahip: "bilinmiyor"`, `durum: "kalacak"` (out of scope of the emptying; recorded so changes show) and `karar_bekleyen` gets
"`~/.palmier/skills` hangi araca ait? Genel boşaltma kapsamında mı?" once. After the baseline exists, a discovered region that is not in the
baseline is reported `YENİ KLASÖR` (non-empty -> sorun, empty -> dikkat).

#### 3.1.3 Entry measurement `olc(path)` (read-only, never follows links)
- symlink (`os.path.islink`): `{"tur": "bag", "hedef": <readlink collapsed with kisalt>, "kirik": not os.path.exists(path)}`. `kirik` is a live
  attribute only, NOT stored in the baseline and NOT part of the fingerprint.
- directory: `{"tur": "klasor", "dosya": N, "bayt": B}` via `os.walk(followlinks=False)`; counts files and links, sums `lstat().st_size`
  of files, skips noise by `GURULTU.search(relative path)`, stops at 50000 files and then sets `"kesik": true` (fingerprint still compares).
- file in regions `komutlar`, `ajanlar` and of kind `talimat`: `{"tur": "dosya"}` ONLY (existence). No size, no mtime, no hash is stored or compared: the user edits `~/.claude/CLAUDE.md` often and an edit is not an event. The content is never opened (D9).
- file of kind `kilit` (the skill lock file, written by tools, not by the user): `{"tur": "dosya", "bayt": size, "mtime": int(st_mtime)}`; a change means a writer touched it, so it stays compared.
Fingerprint = every key except `kirik`. For instruction, command and agent files the fingerprint is just `tur` (plus `hedef` if the entry is a link), so the only events for them are YENİ (appeared), KAYIP (disappeared) and a link-target or type change.

#### 3.1.4 Owner rules `sahip_bul(yol, tur, hedef, ad)` (first match wins; used only when the entry is not already in the baseline)
1. path in `izinli` -> that entry's `sahip`; in `TOHUM_KALACAK` -> its owner.
2. `ad` in `KULLANICI_ADLARI` -> `kullanıcı`.
3. `hedef` starts with `~/.openmontage/` -> `openmontage`.
4. Lock lookup: read `~/.agents/.skill-lock.json` (only keys `skills.<ad>.source`; nothing else is read or kept). If `ad` is there:
   `source` contains `heygen-com/hyperframes`, OR `sourceType == "local"` and the `source` path has a path segment equal to `hf-skills` (a local HyperFrames checkout; measured 2026-11-11 on the lock: 16 github/heygen-com + 11 local/`hf-skills` + 1 other github of 28) -> `hyperframes`; else `skills aracı`. A name starting with `hyperframes` is also `hyperframes`. The `source` text is only tested, never stored or printed (local paths contain project folder names, D8). If `ad` is in `programlar.json` → `hyperframes.skilleri` -> `hyperframes`.
   For a link whose target ends in `/.agents/skills/<x>` or `../.agents/skills/<x>`, `<x>` is looked up instead of `ad`.
5. regions `komutlar`, `ajanlar`, files of kind `talimat` -> `kullanıcı`; file of kind `kilit` -> lock `source` majority is not computed: `skills aracı`.
6. name starts with `.` (e.g. `.trash`) -> `bilinmiyor`.
7. else -> `bilinmiyor`.
Unreadable or malformed lock file never raises: owners fall back to rule 7 and a BİLGİ line says "kilit okunamadı".

#### 3.1.5 First-baseline state rules `durum_ver(bolge, tur, ad, yol)` (`kalacak` | `boşaltılacak`)
- region `komutlar`, `ajanlar`, files of kind `talimat`: `kalacak`.
- name starts with `.` (dot entries cannot be loaded as skills; `.trash`): `kalacak` (listed among decisions, section 7).
- path in `TOHUM_KALACAK`: `kalacak`.
- `kesif-*` regions: `kalacak`.
- everything else in skill regions and the lock file: `boşaltılacak`.
So the first baseline "reflects today's un-emptied state": today's 28+ in `~/.agents`, ~80 links and ~21 real folders in `~/.claude`, 11 codex links, the lock file are all `boşaltılacak`.

#### 3.1.6 Baseline file `notlar/genel-klasor-tabani.json` (format; schema version 1)
```json
{
  "surum": 1,
  "yazildi": "2026-11-12",
  "izinli": [
    {"yol": "~/.claude/skills/synced", "sahip": "uygulama", "neden": "Claude uygulamasının hesap skili senkronu"},
    {"yol": "~/.codex/skills/.system", "sahip": "uygulama", "neden": "Codex'in kendi yerleşik skilleri"},
    {"yol": "~/.cursor/skills-cursor", "sahip": "uygulama", "neden": "Cursor'un kendi yerleşik skilleri"}
  ],
  "ek_klasorler": [],
  "klasorler": {
    "claude":  {"yol": "~/.claude/skills", "var": true},
    "gemini":  {"yol": "~/.gemini/skills", "var": true},
    "gemini-antigravity": {"yol": "~/.gemini/antigravity/skills", "var": false}
  },
  "girdiler": [
    {"yol": "~/.claude/skills/ffmpeg", "bolge": "claude", "tur": "bag",
     "hedef": "~/.openmontage/.agents/skills/ffmpeg", "sahip": "openmontage", "durum": "boşaltılacak"},
    {"yol": "~/.claude/skills/design-dna", "bolge": "claude", "tur": "klasor", "dosya": 142, "bayt": 912345,
     "sahip": "kullanıcı", "durum": "boşaltılacak"},
    {"yol": "~/.claude/skills/openmontage", "bolge": "claude", "tur": "klasor", "dosya": 1, "bayt": 2210,
     "sahip": "kullanıcı", "durum": "boşaltılacak"},
    {"yol": "~/.agents/skills/microsoft-foundry", "bolge": "agents", "tur": "klasor", "dosya": 12, "bayt": 40210,
     "sahip": "skills aracı", "durum": "boşaltılacak"},
    {"yol": "~/.agents/.skill-lock.json", "bolge": "kilit", "tur": "dosya", "bayt": 13404, "mtime": 1794372420,
     "sahip": "skills aracı", "durum": "boşaltılacak"},
    {"yol": "~/.claude/commands/openmontage.md", "bolge": "komutlar", "tur": "dosya",
     "sahip": "kullanıcı", "durum": "kalacak"},
    {"yol": "~/.gemini/GEMINI.md", "bolge": "talimat", "tur": "dosya",
     "sahip": "kullanıcı", "durum": "kalacak"}
  ],
  "gecmis": [{"tarih": "2026-11-12", "islem": "ilk-taban", "girdi": 190}]
}
```
Rules: `girdiler` sorted by `yol` (deterministic file, minimal git diff); written with `ortak.json_yaz` (atomic, `ensure_ascii=False`);
no project names (D8), no secrets (D9), no content hashes, sizes or dates of instruction, command and agent files (only `kilit` carries `bayt`/`mtime`). Entry key is `yol`. `gecmis` keeps the last 20 writes. The example
entry `~/.claude/skills/openmontage` is `boşaltılacak` in the first baseline; the user's decision in section 7 (Q1) flips it to `kalacak` with `--taban-yaz --yenile --kalacak '~/.claude/skills/openmontage' --evet` (or by editing `durum` by hand; the tool validates values on read).
Read-time validation: unknown `surum` -> durum `sorun` with "taban sürümü desteklenmiyor"; `sahip` outside `SAHIPLER` or `durum` outside {kalacak, boşaltılacak} -> sorun with the entry's path (the whole file is not discarded).

#### 3.1.7 Comparison and severity
Live scan vs baseline, keyed by `yol`. Entries in `izinli` (default ∪ baseline) are skipped on both sides. Lines (exact Turkish, `kisalt` paths):
| Case | Line | Severity |
|---|---|---|
| live, not in baseline, region skill/kilit | `YENİ      <yol> (<tür>, sahip: <sahip>)` | sorun |
| live, not in baseline, region komutlar/ajanlar/talimat | same | dikkat |
| in baseline `kalacak`, not live | `KAYIP     <yol> (kalacak girdi yok)` | dikkat |
| in baseline `boşaltılacak`, not live | counted only: `boşaltılan: N` | bilgi |
| fingerprint differs | `DEĞİŞTİ   <yol> (<ne>)` with `<ne>` one of `hedef: <eski> -> <yeni>`, `tür: <eski> -> <yeni>`, `dosya sayısı: a -> b`, `boyut: a -> b`, `tarih değişti`. Instruction, command and agent files can only produce `hedef`/`tür` (never size/date); `boyut`/`tarih` only for the lock file and real skill folders | dikkat |
| live link, `kirik` and baseline `kalacak` (or not in baseline) | `KIRIK BAĞ <yol> -> <hedef>` | dikkat |
| live link, `kirik`, baseline `boşaltılacak` | counted: `kırık bağ (boşaltılacak): N` | bilgi |
| region exists live, baseline says `var: false` or region absent from baseline | `YENİ KLASÖR <yol> (<N> girdi)` | sorun if N>0 else dikkat |
| baseline `var: true`, folder gone | `KLASÖR YOK <yol>` | bilgi |
| baseline missing | `TABAN YOK` | dikkat |
| baseline unreadable / invalid | `TABAN OKUNAMADI: <kısa neden>` (never file content) | sorun |
| environment line missing or invalid in any of 3 places | see 3.1.8 | sorun |
`durum` of the run = worst severity: any sorun -> `sorun`; else any dikkat -> `dikkat`; else `temiz`. A run that only finds
`boşaltılacak` entries still present (the planned state) is `temiz`; its summary says `boşaltılacak girdi duruyor: N`.
`YENİ` of an `izinli` path never appears. A `YENİ` child of a `kalacak` real folder is not a separate line: the parent shows `DEĞİŞTİ (dosya sayısı)`.

#### 3.1.8 Environment check (presence only)
Targets (relative to `ev`): `.zshenv`, `.zshrc`, `.claude/settings.json` (JSON, `env` object). Rules:
- text files: open and iterate LINE BY LINE (never `read()` the whole file into memory), stop after 1 MB or 20000 lines, apply only
  `^\s*(?:export\s+)?HYPERFRAMES_SKIP_SKILLS=(?P<q>["']?)(?P<v>[^"'\s#]*)(?P=q)\s*(?:#.*)?$`. Commented-out lines never match. `v == "1"` -> present and valid;
  other `v` -> `geçersiz değer` (the value itself is not printed; `programlar.json` says only `1` is valid). Matched text and every other line are discarded immediately (the loop variable is overwritten each line; nothing is accumulated). `except` clauses never use `str(e)`/`repr(e)`/traceback in any output: they map to the fixed phrases `dosya yok`, `okunamadı`, `geçersiz değer` only; no output ever contains a line or fragment of a read file. This helper is private to `genel-bekci.py`; P6 keeps its own copy and its own test (no shared helper, no `ortak.py` change).
- `settings.json`: `json.loads`, then only `data.get("env")`; if it is a dict, test only the key `HYPERFRAMES_SKIP_SKILLS` (`str(value) == "1"`). Other keys and the
  whole `env` dict are never iterated into any output, log, exception text or report (the file may contain keys).
- file missing -> `dosya yok`; unreadable or invalid JSON -> `okunamadı` (exception text is replaced by a fixed phrase).
Output (all outputs, report and JSON): `HYPERFRAMES_SKIP_SKILLS satırı: 3 dosyanın 3'ünde var.` (D9 form) and for failures
`HYPERFRAMES_SKIP_SKILLS satırı: 3 dosyanın 2'sinde var. EKSİK: ~/.zshenv (dosya yok)`, plus `karar_bekleyen`
"HYPERFRAMES_SKIP_SKILLS satırı <dosya> içine eklensin mi? (ayar dosyası: onay gerekir; ajan kendi eklemez)". Missing or invalid anywhere = `sorun`.
Not checked (deferred): `launchctl getenv`, running processes' environment, Dock apps.

#### 3.1.9 CLI
```
python3 araclar/genel-bekci.py [--ev DIR] [--taban YOL] [--kart YOL] [--rapor YOL | --rapor-yok] [--siki] [--ozet-json] [--ayrinti]
python3 araclar/genel-bekci.py --taban-yaz [--yenile] [--kalacak YOL ...] [--evet] [--tarih YYYY-AA-GG] [--ev DIR] [--taban YOL] [--kart YOL]
python3 araclar/genel-bekci.py --plan {3,4,5a,5b,6,7} [--tarih YYYY-AA-GG] [--siki]
python3 araclar/genel-bekci.py --yedek-dogrula YEDEK_KLASORU [--ev DIR] [--taban YOL]
python3 araclar/genel-bekci.py --help
```
- `--kart YOL` = `programlar.json` path for the HyperFrames owner hint (default `KOK/programlar.json`; same option as `program-denetim.py:295`); a missing or malformed card never raises, the hint is just skipped.
- default baseline `KOK/notlar/genel-klasor-tabani.json` (`--taban` overrides, for tests); default report `KOK/notlar/genel-bekci.md` (`--rapor` overrides,
  `--rapor-yok` writes none). `--ayrinti` also prints per-region counts and every `boşaltılacak` entry that is still present (default prints counts only).
- Report mode (default) prints the lines of 3.1.7 grouped (1: durum line, 2: sorunlar/dikkat lines, 3: environment line, 4: counts), then the
  `karar_bekleyen` lines. Exit code ALWAYS 0 when it ran correctly; with `--siki` exit 1 only when `durum == "sorun"` (D4). Argparse errors exit 2.
- `--ozet-json`: stdout is exactly ONE line of JSON and nothing else:
  `{"arac": "genel-bekci", "durum": "dikkat", "satirlar": ["..."], "karar_bekleyen": ["..."]}` (D4). At most 12 `satirlar` (worst first, then
  `... ve N satır daha`), at most 10 `karar_bekleyen`. No report file, no baseline write, no stderr noise on success. Errors become a `sorun` JSON, still exit 0
  (or 1 with `--siki`). `--ozet-json` cannot be combined with `--taban-yaz`, `--plan`, `--yedek-dogrula` (argparse error, exit 2).
- Report file `notlar/genel-bekci.md`: header with date (`YYYY-AA-GG` only, no time), same lines, rewritten only if the content without the date differs (program-denetim.py:337-340 pattern).
- `--plan` follows the D4 exit rule (0, or 1 with `--siki` when it refuses). `--taban-yaz` refusals and `--yedek-dogrula` failures exit 1 unconditionally (they are write/verify actions, not reports; details below).
- Write guard: the tool refuses any write whose target path is inside any watched folder or inside `ev/.claude`, `ev/.agents`, `ev/.codex`, `ev/.gemini`, `ev/.cursor`, `ev/.copilot` (test 31).

#### 3.1.10 `--taban-yaz`
- Without `--evet`: dry run. Prints `Kuru çalışma: <N> girdi yazılacak (boşaltılacak: X, kalacak: Y, bilinmeyen sahip: Z). Hedef: <yol>. Yazmak için --evet ekle (kullanıcı onayı gerekir).`
  plus the list of owners=`bilinmiyor` entries and the discovered regions. Writes nothing. Exit 0.
- `--evet`, baseline file does not exist: writes it using rules 3.1.4/3.1.5, appends `gecmis` `{"islem": "ilk-taban"}`. Exit 0.
- `--evet`, baseline exists, no `--yenile`: refuses: `Taban zaten var (<yol>). Üzerine yazmak için --yenile kullan; önce raporu kullanıcıya göster.` Exit 1, file untouched.
- `--evet --yenile`: rebuilds from the live scan: entries already in the baseline keep `sahip` and `durum` and get new fingerprints; `boşaltılacak` entries that are no longer live are
  dropped (that is how emptying is recorded); `kalacak` entries no longer live are dropped and printed as `düşürüldü (kalacak idi): <yol>`; live entries that were not in the
  baseline are added as `durum: kalacak`, `sahip` by rule 3.1.4, and printed as `kabul edildi: <yol>` (the refresh is the user's explicit "accept current state" act, so it must
  only run after the report was shown). `izinli`, `ek_klasorler` are preserved; `gecmis` gets `{"islem": "yenile"}`.
  Flipping a state: `--kalacak YOL` (repeatable, only with `--taban-yaz --yenile --evet`; YOL in `~/...` form) sets `durum: kalacak` on that baseline entry (it must exist in the baseline, else exit 1 `Tabanda yok: <yol>`) and prints `kalacak yapıldı: <yol>`. It is the only code route to flip an existing `boşaltılacak` to `kalacak` (hand-editing `durum` in the JSON also works and is validated on read). Each use needs its own approval (Q1/Q7).
  After a refresh the report must be `temiz`; the tool prints the new report status at the end.

#### 3.1.11 `--plan <adım>` (dry run; PRINTS commands, never executes)
Reads the baseline. Step sets are the baseline entries with `durum == "boşaltılacak"`, still live:
| Step | Set |
|---|---|
| 3 | region `codex` |
| 4 | region `claude`, `tur == "bag"` |
| 5a | region `claude`, `tur != "bag"`, `sahip == "hyperframes"` |
| 5b | region `claude`, `tur != "bag"`, `sahip != "hyperframes"` |
| 6 | region `agents` and region `kilit` |
| 7 | no set: prints the closing checks (see below) |
Pre-checks, in this order; any failure prints `DURDUR: <neden>` lines and no commands; exit code is 0, or 1 when `--siki` is given (same rule as report mode, so a refused plan never breaks a chain unless asked):
1. baseline exists and is valid;
2. the plain report has no `sorun` (a `YENİ` entry or a missing key must be classified first);
3. earlier steps (3 < 4 < 5a < 5b < 6) have no live `boşaltılacak` entries left: `ÖNCEKİ ADIM BİTMEMİŞ: adım <n> (<k> girdi)`;
4. dependency scan: every live link anywhere in the watched regions that is NOT in this step's set but whose target (lexically resolved: `normpath(join(dirname(link), target))`, no following)
   lies at or under a path in this step's set is listed as `BAĞIMLI: <link> -> <hedef> bu adımla kırılır`;
5. `--tarih` default today; backup folder name `genel-klasorler-<YYYY-AA-GG>`.
Printed output (shell text, each step starts with a `# ONAY GEREKİR` banner):
```
# ADIM 4 - ~/.claude/skills bağlarını kaldır (81 bağ). ONAY GEREKİR: bu listeyi kullanıcıya göster, "evet" gelmeden çalıştırma.
YEDEK="$HOME/Documents/Claude/yedek/genel-klasorler-2026-11-12"; mkdir -p "$YEDEK"
# 1) yedek: yol ve hedef listesi (readlink), ls -la dökümü
printf '%s\t%s\n' '/Users/.../.claude/skills/ffmpeg' "$(readlink '/Users/.../.claude/skills/ffmpeg')" >  "$YEDEK/bag-listesi-claude.tsv"   # one explicit line per entry (no glob)
printf '%s\t%s\n' '/Users/.../.claude/skills/<sonraki>' "$(readlink '/Users/.../.claude/skills/<sonraki>')" >> "$YEDEK/bag-listesi-claude.tsv"
ls -la '/Users/.../.claude/skills' > "$YEDEK/ls-claude-skills-oncesi.txt"
# 2) kaldır (yalnız bağın kendisi: rm, -r YOK)
rm -- '/Users/.../.claude/skills/ffmpeg'
...
# 3) kontrol
python3 araclar/genel-bekci.py --yedek-dogrula "$YEDEK" ; python3 araclar/genel-bekci.py
# 4) geri alma (bu adımı geri al)
while IFS=$'\t' read -r p t; do if [ -e "$p" ] || [ -L "$p" ]; then echo "ÇAKIŞMA: $p"; else ln -s -- "$t" "$p"; fi; done < "$YEDEK/bag-listesi-claude.tsv"
```
Interpreter: the first line of every plan is `# zsh/bash uyumlu; glob yok` and the text contains NO unquoted glob (zsh errors on an unmatched glob): the backup lists are emitted as one explicit `printf` line per path (the tool knows every entry from its own scan; first line `>`, the rest `>>`), and the rollback loop reads the tsv with `while IFS=$'\t' read -r p t` (no glob). Every `ls` dump targets one named folder, no wildcard. Steps 5a, 5b and 6 start with the same-device check `[ "$(stat -f %d "$HOME/.claude/skills")" = "$(stat -f %d "$HOME/Documents/Claude")" ] || { echo 'FARKLI DİSK: mv kopyalar, durdur'; exit 1; }` (adapted to the source folder), as the first printed command.
Rules for generated lines: paths quoted with `shlex.quote`; links -> `rm --`; real folders and files -> `mv -- <yol> "$YEDEK/<bolge>-skills/"` (kept as `"$YEDEK/agents-skills/"`, `"$YEDEK/claude-skills/"`, `"$YEDEK/codex-skills/"`; the lock file goes to `"$YEDEK/agents-kilit/"`);
step 6 additionally `cp -p ~/.agents/.skill-lock.json "$YEDEK/agents-kilit/skill-lock.json.kopya"` BEFORE the `mv` (a copy and the moved original: two copies of the 13 KB file, protects against a half-done `mv` across volumes);
no `rm -rf`, no globs over real folders, never anything under `synced`, `.system`, `skills-cursor`, `kalacak` entries or `izinli` entries; only the entries listed by name.
Backup choice: real folders are MOVED (`mv`, atomic on the same volume, no extra disk) instead of copied, and the backup is verified by `--yedek-dogrula` against the baseline numbers
(file count and bytes). The brief said "copied"; `mv` is the same approach as the user's earlier `tasi.sh` and keeps exactly one authoritative copy; a copy is still taken for the lock file. If the user prefers copy-then-delete, only the generator line changes (`cp -Rp` then a separate approved `rm`).
Step 7 prints: the closing checks (`genel-bekci.py` plain; `~/.gemini/skills`, `~/.cursor/skills`, `~/.copilot/skills`, antigravity folders are empty or absent, with `--ayrinti`), the baseline refresh command
(`python3 araclar/genel-bekci.py --taban-yaz --yenile --evet`, "ONAY GEREKİR"), the same-day backup record text (section 4) and the scheduled reminder text (section 4).
Steps 1 and 2 are not generated (key check = plain report; step 2 is user-file edits): `--plan 1|2` prints `Bu adım elle: rehber/12 bölüm <n>` and exits 0.

#### 3.1.12 `--yedek-dogrula <klasör>`
For every baseline entry with `durum == "boşaltılacak"` that is no longer live: `tur == "bag"` must appear in some `bag-listesi-*.tsv` in the backup folder with the same target; `tur == "klasor"` must exist at
`<klasör>/<bolge>-skills/<ad>` with the same `dosya` and `bayt` as the baseline; `dosya` of region `kilit` must exist in `<klasör>/agents-kilit/`. Prints `yedekte tamam: N`, and `YEDEKTE YOK: <yol>` /
`FARKLI: <yol> (<ne>)` lines. Exit 1 if any problem (also if the folder does not exist), else 0. Read-only.

### 3.2 `notlar/genel-klasor-tabani.json` (new, generated; NOT hand-written by the implementer)
The implementer creates NO baseline. The baseline is written once by `python3 araclar/genel-bekci.py --taban-yaz --evet`, only after the user approves (section 7 item 1) and after the
dry run was shown. The implementer ships the tool without this file; tests use temp baselines. Until then the tool reports `TABAN YOK` (dikkat) and prints the exact command.
Format: 3.1.6.

### 3.3 `rehber/12-genel-klasor-bosaltma.md` (new, about 220-280 lines Turkish)
Outline (headings exactly):
1. `# 12 — Genel skill klasörlerini bekleme ve boşaltma` (what, who may do it: library session only, each step separate approval, link to `rehber/13-yedek-ve-geri-alma.md`, `notlar/hf-om-gecisi/DURUM.md`).
2. `## Neyi izliyoruz` : table region -> path -> who normally writes -> state after emptying (kalacak/boşaltılacak). Rows: `~/.claude/skills`, `~/.agents/skills`, `~/.agents/.skill-lock.json`,
   `~/.codex/skills`, `~/.gemini/skills`, `~/.gemini/antigravity*/skills`, `~/.cursor/skills`, `~/.copilot/skills`, `~/.claude/commands`, `~/.claude/agents`, the global instruction files, discovered `~/.<x>/skills`.
   Permanent vendor list with the reason (`synced`, `.system`, `skills-cursor`) and how to add one (edit `izinli` in the baseline with approval, then `--taban-yaz --yenile --evet`).
3. `## Her gün kullanım` : `python3 araclar/genel-bekci.py` (session start, monthly via `aylik-ozet.py`), how to read YENİ/KAYIP/DEĞİŞTİ, what `temiz/dikkat/sorun` mean, `--ozet-json`, `--siki`.
4. `## Boşaltmadan önce kararlanacaklar` : the list of section 7 (Q1-Q9) with the recommended answer for each and the place the answer is recorded (`notlar/kararlar.md` by P8, `DURUM.md` until then).
5. `## Hazırlık (adım 0)` : conditions, each checked by a command: library tree clean and committed (`git status`), baseline written and committed, `genel-bekci.py` = temiz, project-gate decisions made,
   last read-only scan of the open gaps (5 scheduled tasks, `~/.claude/bin`, `plugin-sources`, `marketplaces`, `~/Library`, DURUM.md "Hâlâ okunmadı"), no other session running, a fixed backup folder named for the day, `df -h ~` has more than 1 GB free.
6. `## Adımlar` : for each step the same sub-bullets: Amaç / Sıra nedeni / Yedek / Komut (`--plan <n>`) / Kontrol / Geri alma / Onay. Steps:
   - **Adım 1 Anahtar** (no removal). Reason: first, because any HyperFrames `init/skills/update` after emptying re-creates the skills (programlar.json `skill_yazimi`). Check: report line `3 dosyanın 3'ünde var`. If missing: user decides; the agent states which file; the agent does not edit shell/settings files on its own (rehber/11:63-64). Optional, separate approval: `launchctl setenv HYPERFRAMES_SKIP_SKILLS 1` for Dock apps (does not survive reboot unless a LaunchAgent is added; not recommended unless a Dock-started app is observed writing).
   - **Adım 2 Giriş yerleri** (user files; each its own approval): 2a the `openmontage` entry skill, 2b the four slash commands, 2c the global `CLAUDE.md` lines (and the `global-skill-links.txt` manifest note). Reason: these are what tells Claude, in every folder, to load `openmontage` and ~80 skills from `~/.claude/skills`; if step 4 ran first, every video request in any folder would fail silently. Backup: copy of each file to `$YEDEK/giris/`. Check: a test request "openmontage skilini oku" works in a new session started from a temp folder; `genel-bekci.py` shows `DEĞİŞTİ` for the edited files (expected) and baseline is refreshed ONLY at step 7. Rollback: copy the file back from `$YEDEK/giris/`.
   - **Adım 3 Codex bağları** (11 links; `playwright` and `.system` stay). Reason: they point into `~/.claude/skills` and `~/.agents/skills`; removing the targets first leaves dangling links in Codex's folder. Rollback: `ln -s` from the tsv.
   - **Adım 4 `~/.claude/skills` bağları** (about 81). Reason: links are lossless to restore from the list (readlink), so they go before real folders; removes the 6 links into `~/.agents/skills` before step 6; OM program tree `~/.openmontage` is untouched (only the links to it go). Restore from the tsv, not from `global-skill-links.txt` (79 lines vs 75 links, DURUM.md).
   - **Adım 5a HyperFrames kopyaları** (real folders with owner `hyperframes`). Reason: reproducible from the HF release and from the library; nothing in the library reads them. 5b: other real folders (`youtube-arama`, `nlm-skill`, `design-dna`, `openmontage` unless kept, old HF skills): ONLY after the project-gate decisions (Q4-Q6) because IstatistikYoutube and Akıl Dışı read some of them (DURUM.md project scan). Backup = move to `$YEDEK/claude-skills/`. Rollback: `mv` back one by one (collision check).
   - **Adım 6 `~/.agents/skills` and `.skill-lock.json`**. Reason last: the `skills` tool and HF treat the lock as "installed"; removing folders but leaving the lock makes the next `npx skills` run reinstall from stale records, and removing the lock first would hide what was installed. Links that pointed here were removed in steps 3-4. The empty `skills` folders are LEFT in place (the watchdog watches them; a missing folder gets re-created by HF mirror logic anyway). Lock: `cp -p` then `mv`.
   - **Adım 7 Kapanış**: mirrors empty check; `--taban-yaz --yenile --evet` (approval; plus `--kalacak` for Q1/Q7 exceptions); `genel-bekci.py` must be `temiz`; library commit (approval); backup record and reminder (section "Yedek silme hatırlatması"); update DURUM.md "Adım çizelgesi" row 3 and `rehber/02`, `README.md` 6-7, `rehber/01` 12 lines noted in DURUM "Sonraya kalan düzeltmeler" (P8/library session, own approvals); restart open Claude/Codex sessions (open sessions keep the old skill list).
   - Whole-procedure rollback order: 6, 5b, 5a, 4, 3 (folders before links, so restored links are not dangling), then 2 files; then `genel-bekci.py` must equal the baseline again (`temiz`).
7. `## Geri yazma: kim yazabilir, nasıl yakalanır` : table writer -> folder -> how it is stopped -> how the watchdog sees it:
   HyperFrames `init/skills/skills update/update` (stopped by the key; Dock apps not covered) -> `~/.claude/skills`, `~/.agents/skills`, lock, mirrors -> YENİ;
   `npx skills add -g` (not stopped by the key; also named inside some skills' texts, `ortak.py:480` `_YAZAR`) -> `~/.agents/skills`, lock -> YENİ;
   Claude app (synced) / Codex app (`.system`, playwright) / Cursor (`skills-cursor`) -> allowed;
   a user or agent doing `cp`/`ln` by hand -> YENİ; plugins (`~/.claude/plugins`, not a skills folder; not watched, deferred); Antigravity creating `~/.gemini/antigravity*/skills` -> YENİ KLASÖR (glob);
   a newly installed AI tool -> discovery `kesif-*` / `YENİ KLASÖR`; Time Machine/other-Mac restore -> YENİ/KAYIP everywhere (run the full report before anything).
8. `## Bir şey yeniden belirirse` : ordered: (1) do not delete; run `genel-bekci.py --ayrinti`; (2) read `sahip` and mtime of the entry; check the key (report line); check the lock `source` through the tool's owner column (no history files are read); (3) ask the user which: (a) unwanted writer -> stop the cause first (key, instruction text), then quarantine the entry with approval: `mv` to `~/Documents/Claude/yedek/geri-yazilan-<YYYY-AA-GG>/` with the link list; (b) wanted skill -> it belongs to a project: install by `skill-ekle.py`, not globally; (c) legitimately permanent (vendor) -> add to `izinli` in the baseline (approval) and `--taban-yaz --yenile --evet`; (4) re-run the report: `temiz`; (5) if the same thing returns twice, treat the writer as an open problem and tell the user (do not loop).
9. `## Yedek silme hatırlatması` : the same-day record and reminder (section 4 texts); retention 30 days AND explicit user "sil"; the earlier two backups; plain-text key warning for `ayar-2026-11-11`.
10. `## Yeni bir yapay zeka aracı eklenince` : one line pointing to `rehber/14-yapay-zeka-araclari.md` (P1) and the `ek_klasorler` step (user approval).

### 3.4 `promptlar/16-genel-klasor-bosaltma.md` (new, about 50 lines)
Same style as prompt 10. Two copy blocks: A) emptying run, B) "something reappeared / report is not temiz". Texts in section 4.

### 3.5 `araclar/testler/test_p2-genel-bekci.py` (new): see section 5.
Creates `araclar/testler/` if absent (it does not exist today; P8's runner iterates it). File name with a hyphen: tests import the tool with `importlib.util.spec_from_file_location("genel_bekci", ...)` and run the CLI by `subprocess` with `--ev`.

---------------------------------------------------------------------------------------------------------------------------

## 4 User-facing texts (Turkish, exact)

Tool messages
- `Genel klasör bekçisi: <durum.upper()> (sorun: N, dikkat: N)` first line of the report.
- `TABAN YOK: notlar/genel-klasor-tabani.json yazılmamış. İlk taban için: python3 araclar/genel-bekci.py --taban-yaz  (kuru çalışma); onaydan sonra --evet ekle.`
- `boşaltılacak girdi duruyor: N (bekleniyor, taban: <tarih>)` / `boşaltılan: N`.
- `HYPERFRAMES_SKIP_SKILLS satırı: N dosyanın K'sinde var.` and `EKSİK: <liste>`.
- `YENİ      ~/.agents/skills/microsoft-foundry (klasör, sahip: skills aracı)`; `KAYIP     ...`; `DEĞİŞTİ   ... (dosya sayısı: 12 -> 14)`; `KIRIK BAĞ ...`; `YENİ KLASÖR ...`.
- `karar_bekleyen` for `YENİ KLASÖR` / `kesif-*`: `Yeni bir yapay zeka aracı klasörü göründü (rehber/14): <yol> — araç ise ek_klasorler'e eklensin mi, değilse izinli/yoksay mı?` (the monthly summary shows it as is).
- `karar_bekleyen`: `Yeni girdi <yol> (sahip: <sahip>): kalacak mı, boşaltılacak mı? Karar sonrası: --taban-yaz --yenile --evet (onay gerekir).`
- Refusals: `Taban zaten var (...)...`, `DURDUR: ...`, `ÖNCEKİ ADIM BİTMEMİŞ: adım 3 (2 girdi)`, `BAĞIMLI: ...`, `Yazma reddedildi: hedef izlenen bir klasörün içinde`.
- `Bu araç yalnız okur ve yazdırır; hiçbir komutu kendisi çalıştırmaz.` printed at the top of every `--plan` output.

Backup record text (given to P3 as the content for `yedekler.json`, written by the library session with approval on emptying day; field names follow akis-12's proposal: yol, tür, tarih, neden, silme tetiği, gizli içerir)
```
yol: ~/Documents/Claude/yedek/genel-klasorler-<YYYY-AA-GG>/   tür: genel-klasor   tarih: <son boşaltma günü>
neden: Genel skill klasörleri boşaltıldı (rehber/12). İçerik: bağ listeleri (tsv), taşınan skill klasörleri, skill kilit dosyası, giriş dosyaları kopyaları.
silme_tetigi: 30 gün geçince VE kullanıcı "sil" deyince (kendi kendine silinmez)   gizli_icerir: hayır (kilit dosyası yalnız kaynak adresleri içerir)
```
Scheduled reminder proposal (needs approval, D7; created on the SAME day as the last emptying step, DURUM.md 2026-11-10 decision)
- one-time reminder 30 days later, title `Genel skill klasörü yedeğini silme zamanı`, text:
  `~/Documents/Claude/yedek/genel-klasorler-<tarih>/ 30 gündür duruyor. Önce python3 araclar/genel-bekci.py çalıştır: temiz ise kullanıcıya sor: "Yedeği silelim mi?" Kullanıcı açıkça evet demeden hiçbir şeyi silme. Ayrıca ayar-2026-11-11 yedeğinde düz metin anahtar satırı olabilir; onu da hatırlat (içeriği yazdırma).`
- Recurring check is NOT created here; P3's `yedek-denetim.py` lists backup ages monthly (hand-off).

Prompt 16 block A (emptying)
```
~/Documents/SkillKutuphanesi'de çalış. Önce notlar/hf-om-gecisi/DURUM.md ve rehber/12-genel-klasor-bosaltma.md dosyalarını oku.
Genel skill klasörlerini boşaltma işini adım adım yürüt. Kurallar: her adımdan önce python3 araclar/genel-bekci.py ile durumu göster,
python3 araclar/genel-bekci.py --plan <adım> çıktısını (yedek, komutlar, kontrol, geri alma) bana göster ve ben "evet" demeden hiçbir komutu çalıştırma.
Bir adım bitince kontrolü çalıştır, sonucu söyle, sonra bir sonraki adımı sor. Taban dosyasını yazmak, bir ayar ya da giriş dosyasına dokunmak,
commit ve hatırlatma kurmak ayrı onay ister. Kararlanacaklar listesindeki sorulara cevap vermeden 2. adımdan öteye geçme.
Bittiğinde yedek kaydını ve silme hatırlatmasını aynı gün öner.
```
Block B (reappeared)
```
~/Documents/SkillKutuphanesi'de python3 araclar/genel-bekci.py --ayrinti çalıştır. YENİ, KAYIP, DEĞİŞTİ ya da ortam anahtarı sorunu varsa
rehber/12-genel-klasor-bosaltma.md "Bir şey yeniden belirirse" bölümünü uygula: önce kim yazdı bul, hiçbir şeyi silme, bana seçenekleri sun.
```

---------------------------------------------------------------------------------------------------------------------------

## 5 Tests: `araclar/testler/test_p2-genel-bekci.py`

Harness: `test(ad, kosul, ayrinti="")` like `test.py:27-30`; every test builds a fake home in `tempfile.mkdtemp()`; baseline and report paths
also in temp. CLI cases use `subprocess.run([sys.executable, TOOL, "--ev", ev, "--taban", taban, "--rapor-yok", ...])`. No test touches the real home (a guard asserts
`ev` is under the temp root before every run), and no test creates `notlar/genel-klasor-tabani.json` (assert at the end that the real file's existence/hash is unchanged). Last line `N/N test geçti`; exit 1 on any failure.
Fake home builder `ev_kur()`: `.claude/skills` (links to a fake `.openmontage/.agents/skills/x`, a `../../.agents/skills/y` link, real folder `hyperframes` with 3 files, `design-dna`, `synced/a/b/SKILL.md`, `.trash/`, `.DS_Store`),
`.agents/skills/{y,microsoft-foundry}`, `.agents/.skill-lock.json` (fake `skills` with `heygen-com/hyperframes` and another source), `.codex/skills` (link, `playwright`, `.system/x`), `.gemini/skills` (empty),
`.gemini/antigravity-cli/skills` (empty), `.cursor/skills` (empty), `.cursor/skills-cursor/v`, `.copilot/skills` (empty), `.claude/commands/{a.md}`, `.claude/agents/b.md`, `.claude/CLAUDE.md` (fake text with `FAKE_SECRET_AAA`), `.gemini/GEMINI.md`,
`.zshenv`, `.zshrc` (contains `export FAKE_API_KEY=SECRETVALUE123` and the key line), `.claude/settings.json` (`{"env": {"HYPERFRAMES_SKIP_SKILLS": "1", "TOKEN": "SECRETVALUE456"}}`).

Cases:
1. `--help` exits 0 and mentions `--taban-yaz`, `--plan`, `--ozet-json`, `--ev`, `--kart`, `--kalacak`.
2. No baseline: report durum `dikkat`, line `TABAN YOK`, exit 0; with `--siki` exit 0 (dikkat is not sorun).
3. `--taban-yaz` without `--evet`: baseline file not created; stdout has `Kuru çalışma`; exit 0.
4. `--taban-yaz --evet`: file created; valid JSON; `surum == 1`; entries sorted by `yol`; paths start with `~/` and contain no absolute fake-home path; no `kirik` key; no secret strings.
5. Baseline owners: link into `.openmontage` -> `openmontage`; lock entry with HF source -> `hyperframes`; other lock entry -> `skills aracı`; `design-dna` -> `kullanıcı`; unknown folder -> `bilinmiyor`.
6. Baseline states: skill-region entries and lock file `boşaltılacak`; `.trash`, `playwright`, commands, agents, instruction files `kalacak`.
7. Vendor entries (`synced`, `.system`, `skills-cursor`) are in `izinli` and in no `girdiler` row; creating files inside `synced` and `.system` produces no report line.
8. Second `--taban-yaz --evet` without `--yenile` exits 1, file bytes unchanged.
9. Right after baseline with env present: durum `temiz`, exit 0, `--siki` exit 0, line `boşaltılacak girdi duruyor`.
10. New folder in `.agents/skills`: line `YENİ`, durum `sorun`, exit 0; with `--siki` exit 1.
11. Removing a `boşaltılacak` entry: durum stays `temiz`, `boşaltılan: 1`; removing a `kalacak` command file: `KAYIP`, durum `dikkat`.
12. Link retargeted: `DEĞİŞTİ ... hedef:`; file added inside a real folder: `DEĞİŞTİ ... dosya sayısı`; durum `dikkat`.
13. Dangling link in a `kalacak` slot: `KIRIK BAĞ` dikkat; dangling link in a `boşaltılacak` slot: counted only.
14. New `~/.gemini/antigravity/skills` folder (empty): `YENİ KLASÖR` dikkat; with one child: sorun. New `.gemini/antigravity-2/skills` is found by the glob. With a `YENİ KLASÖR` present, `--ozet-json` `karar_bekleyen` contains the exact sentence `Yeni bir yapay zeka aracı klasörü göründü (rehber/14): <yol> — araç ise ek_klasorler'e eklensin mi, değilse izinli/yoksay mı?`.
15. Discovery: `~/.foo/skills/x` created after baseline: `YENİ KLASÖR`; `~/.openmontage/skills/x` ignored.
16. `ek_klasorler` in the baseline (`~/.windsurf/skills`) is watched; a child appearing there is `YENİ`; `--yenile` preserves the list.
17. Environment: all three present -> `3 dosyanın 3'ünde var`; remove from `.zshenv` -> sorun, names `~/.zshenv`; commented-out line does not count; value `0` -> `geçersiz değer`, sorun; settings.json without the key -> sorun; invalid JSON -> `okunamadı` sorun; missing file -> `dosya yok`; `.zshrc` made a directory -> `okunamadı` with no path text from the OS exception; a 3 MB `.zshrc` with the key line only after 1 MB -> `EKSİK` (cap holds); every non-matching line (including `export FAKE_API_KEY=SECRETVALUE123`) never appears in stdout, stderr or any file.
18. Secrets never printed: run plain, `--ayrinti`, `--ozet-json`, `--plan 3|4|5a|5b|6|7`, `--taban-yaz` dry-run and `--yedek-dogrula`, plus the written report and baseline; none contains `SECRETVALUE123`, `SECRETVALUE456`, `FAKE_SECRET_AAA`, `FAKE_API_KEY`.
19. `--ozet-json`: stdout parses as exactly one JSON object with keys `arac`, `durum`, `satirlar`, `karar_bekleyen` only; `arac == "genel-bekci"`; `durum` in the three values; no second line; stderr empty; no report file and no baseline created; `satirlar` ≤ 12; combined with `--plan` exits 2.
20. Instruction, command and agent files: rewriting content and changing size/mtime -> NO line, durum stays `temiz`; deleting one -> `KAYIP` dikkat; a new one -> `YENİ` dikkat; the baseline row has only `yol, bolge, tur, sahip, durum` (no `bayt`, `mtime`, hash, content). Lock file: size change -> `DEĞİŞTİ ... boyut` dikkat. A command file replaced by a link to another target -> `DEĞİŞTİ ... tür`.
21. Corrupt baseline (`{`): durum `sorun`, line `TABAN OKUNAMADI`, exit 0; unknown `surum`: sorun; bad `sahip` value: sorun naming the path.
22. `--taban-yaz --evet --yenile`: keeps `sahip/durum` of existing entries; drops emptied `boşaltılacak` entries; adds new live entry as `kalacak` and prints `kabul edildi`; prints `düşürüldü (kalacak idi)` for a vanished `kalacak` entry; after refresh the report is `temiz`; `izinli` preserved.
23. Write guard: `--taban <fake-home>/.claude/skills/x.json --taban-yaz --evet` exits 1 and writes nothing.
24. `--plan 3` on the fake home: exits 0; output contains `ONAY GEREKİR`, `readlink`, `rm --` lines only for the codex links, `ln -s` rollback loop, backup name `genel-klasorler-<tarih>` with `--tarih`; does NOT contain `playwright` or `.system`; fake home tree is byte-identical before and after (names, sizes, mtimes, link targets).
25. `--plan 4` before step 3 is done: prints `ÖNCEKİ ADIM BİTMEMİŞ` and no `rm` lines; exit 0 without `--siki`, 1 with `--siki`.
26. Dependency scan: a codex link pointing into `.claude/skills/hyperframes` blocks `--plan 5a` with `BAĞIMLI`.
27. After manually removing the codex links in the fake home (simulating step 3), `--plan 4` prints `rm --` for each claude link and none for `synced`, real folders, or `kalacak` entries; `--plan 5a` lists only owner `hyperframes` folders and uses `mv --`; `--plan 6` includes the `cp -p` of the lock file before `mv`, no `rm -rf` anywhere in any plan (assert the string is absent).
28. `--plan` without baseline: `DURDUR`, no commands. `--plan 1` / `--plan 2` print `Bu adım elle` and exit 0.
29. `--yedek-dogrula`: build a backup folder from a simulated step 4+5a (tsv from readlink, folders moved) -> `yedekte tamam`, exit 0; delete one tsv line / change one file -> `YEDEKTE YOK` or `FARKLI`, exit 1; nonexistent folder -> exit 1.
30. Nothing written outside: snapshot of the whole fake home (every path, size, mtime, link target) is identical after running every mode except the ones that write only to the temp baseline/report; the library's `notlar/` has no new file after the run; no file named `*.tmp` is left next to the baseline.
31. `SKILL_BEKCI_EV` environment variable is used when `--ev` is absent; `--ev` wins when both are given.
32. Determinism: two `--taban-yaz` writes on an unchanged fake home (first removed between) produce identical files except `yazildi`/`gecmis`; report file is not rewritten when only the date differs.
33a. Owner rule: lock entry `sourceType: local` with a source path containing an `hf-skills` segment -> `hyperframes`; local source without it -> `skills aracı`; the source text appears nowhere in outputs or baseline. Tests pass a fake `--kart` (card with `hyperframes.skilleri`), never the library's `programlar.json`.
33b. `--kalacak '~/.claude/skills/hyperframes'` with `--taban-yaz --yenile --evet` flips `durum` and prints `kalacak yapıldı`; unknown path exits 1 `Tabanda yok`; the entry then disappears from `--plan 5a/5b` sets and from the `boşaltılacak girdi duruyor` count; without `--evet` nothing changes.
33c. Plans contain no unquoted glob: no line of any `--plan` output matches `[*?]` outside quotes (regex check) and every `printf` backup line names one explicit path.
33. `.DS_Store` and `__pycache__` inside a watched folder never appear in any line.
34. `ozet-json` run with a missing `--ev` directory: still exactly one JSON object, durum `sorun`, exit 0.

---------------------------------------------------------------------------------------------------------------------------

## 6 Hand-off requests to other packages

To P8 (integrator; the only owner of the shared files):
- `araclar/test.py`: one section that runs every `araclar/testler/test_*.py` as a subprocess (D5), including `test_p2-genel-bekci.py`; success = exit 0 and last line matches `^\d+/\d+ test geçti$`.
- `araclar/dogrula.py`: (a) UYARI (not HATA) if `notlar/genel-klasor-tabani.json` is missing; HATA if it exists but is not valid JSON or `surum != 1`; (b) HATA if `rehber/12-genel-klasor-bosaltma.md`, `promptlar/16-genel-klasor-bosaltma.md`, `araclar/genel-bekci.py` are missing; (c) after emptying day, optional UYARI if the baseline `yazildi` date is older than 45 days.
- `CLAUDE.md` and `AGENTS.md` (keep identical, `diff -q`): (1) hard rule 1 exception wording, proposed exactly: "…**asla** yazma, kopyalama, symlink koyma ya da silme (tek istisna: `rehber/12-genel-klasor-bosaltma.md` adımlarıyla yapılan, yedekli ve her adımı kullanıcının ayrıca onayladığı boşaltma ile onaylı program güncellemesi)."; (2) one line under "Bakım isteklerinde": "- Genel klasörler: oturum başında `python3 araclar/genel-bekci.py --ozet-json` (YENİ ya da sorun varsa kullanıcıya söyle, hiçbir şeyi silme). Boşaltma ve geri yazma durumları yalnız `rehber/12-genel-klasor-bosaltma.md` ile, her adım ayrı onayla. Hazır komut: `promptlar/16-genel-klasor-bosaltma.md`." This text needs the user's approval (A5, approval list).
- `promptlar/README.md`: add row `| 16 | [16-genel-klasor-bosaltma.md](16-genel-klasor-bosaltma.md) | Genel skill klasörlerini yedekleyip boşaltmak ya da orada beklenmeyen bir girdi belirince bakmak |` and `README.md` rehber list: row for `rehber/12-genel-klasor-bosaltma.md`.
- `araclar/duman-testi.py:44-53` and `test.py:33-42` `parmak_izi`: unchanged by P2; keep as is (A7 is P8's). If P8 moves the skip list to `ortak.py`, `genel-bekci.py` may later import the same constant; not required now.
- `notlar/hf-om-gecisi/DURUM.md` (P8 or the library session, with approval): after emptying day, step 3 row and the "Boşaltma sırası (taslak)" line get a pointer to `rehber/12`; "Genel klasör bekçisi" gets a one-line mention. `notlar/kararlar.md`: the decisions of section 7 once taken.
- The generated report `notlar/genel-bekci.md` (tool output, written by `genel-bekci.py` unless `--rapor-yok`) must be accepted by `kapsam-denetimi.py`/`dogrula.py` as a known generated note (like `notlar/program-denetimi.md`); P8 adds it to whatever list of generated notes those checks keep. Whether it is committed is the user's usual rule for `notlar/*.md` reports.
To P4 (monthly chain):
- `aylik-ozet.py` runs `python3 araclar/genel-bekci.py --ozet-json` as a subprocess and merges `satirlar`/`karar_bekleyen`; `sorun` puts a UYARI at the top of the monthly report. The scheduled task SKILL.md proposal (outside the library, needs the user's approval): add the step "python3 araclar/genel-bekci.py çalıştır; YENİ ya da sorun varsa raporun başına yaz; hiçbir şeyi silme, taşıma". It must also run in the "nothing changed" branch (C2), unlike `program-denetim` today (arsiv-guncelle.py:202-206 per akis-08).
To P3 (backup and git):
- `yedekler.json` row for `~/Documents/Claude/yedek/genel-klasorler-<tarih>/` written on emptying day with the text of section 4; the backup name stays `genel-klasorler-<tarih>` (P3's own correction was checked: the two specs use the same name); `yedek-denetim.py` must recognise the `genel-klasorler-*` and `geri-yazilan-*` name patterns and show their age; `rehber/13-yedek-ve-geri-alma.md` should link to `rehber/12` for the folder-level rollback and note that the backup parent is `~/Documents/Claude/yedek/` for emptying too. Mark `ayar-2026-11-11` as "anahtar içerir" in the inventory.
To P6 (programs):
- After emptying, `programlar.json` openmontage `guncelleme_adimlari` step "~/.claude/skills içindeki bağlarda kırık olan var mı denetlenir" and the `skill_yazimi`/`simdi` texts become stale: on emptying day P6's card fields (`giris_yolu`) should state the new entry path chosen in Q1-Q3; `program-denetim.py --oncesi` may call `genel-bekci.py --ozet-json` as an extra pre-check ("genel klasör temiz mi") before any program update (optional).
To P1 (AI tools):
- `rehber/14-yapay-zeka-araclari.md` new-tool procedure: "Aracın genel skill klasörünü `notlar/genel-klasor-tabani.json` → `ek_klasorler` listesine ekle (kullanıcı onayıyla); sonra `python3 araclar/genel-bekci.py` temiz olmalı." The watchdog does not read `yapay-zeka-araclari.json` today (deferred, section 8). ACCEPTANCE RECORD: P1's reviewed spec accepts this request (rehber/14 new-tool step adds `ek_klasorler`); because the step is easy to forget, the watchdog also catches it: any unknown `~/.<x>/skills` shows as `YENİ KLASÖR` with the `rehber/14` sentence (section 4) in the monthly summary, so a forgotten step surfaces within a month.
To nobody else: P2 needs no change in `skill-ekle.py`, `arsiv-guncelle.py`, `proje-kullanimi.py`.

---------------------------------------------------------------------------------------------------------------------------

## 7 Needs the user's approval

At implementation time (library files): none beyond the normal commit approval; the five new files are inside the library and read-only toward the machine.

At the time of use (each separate, shown before it happens):
1. First baseline: `genel-bekci.py --taban-yaz --evet` (writes `notlar/genel-klasor-tabani.json`) after the dry run is shown, then the commit. Recorded in `gecmis`.
2. Every baseline refresh (`--yenile --evet`), especially the `kabul edildi` list.
3. Each emptying step 3, 4, 5a, 5b, 6 (the `--plan` text shown first); the choice "move to backup" vs "copy then delete".
4. Step 2: editing the entry skill, the four slash commands (animated-drawing, backlot, ink-art, openmontage), the global `~/.claude/CLAUDE.md` lines (these are the user's files; one approval each).
5. Adding the key line anywhere it is missing; `launchctl setenv` (optional).
6. The scheduled one-time reminder (scheduled task creation) and the `yedekler.json` row.
7. The `CLAUDE.md`/`AGENTS.md` rule-1 exception and the new line (P8).
8. Deleting any backup (30 days AND an explicit "sil"), deleting `.trash` content, quarantining something that reappeared.
9. Restarting open Claude/Codex sessions after emptying.

Decisions needed BEFORE emptying (user-only; each with a recommendation; the tool supports every outcome by the `durum` field):
- Q1 Where does the `openmontage` entry skill live? Today a real folder `~/.claude/skills/openmontage/SKILL.md` and `CLAUDE.md:4,6` (global) command it. Options: (A) keep this ONE folder in `~/.claude/skills` as the only named exception (`durum` -> `kalacak`; smallest change, programs stay in place, D2); its text then reads Layer-3 skills from `~/.openmontage/.agents/skills/<ad>/SKILL.md` by path; (B) move it into the library and install per project; (C) turn it into a slash command only. Recommended A.
- Q2 The four slash commands (the brief says three; `animated-drawing`, `backlot`, `ink-art`, `openmontage`) stay in `~/.claude/commands` (`kalacak`); their text that points to `~/.claude/skills/...` must be re-pointed to `~/.openmontage/...` (per-file approval).
- Q3 The global `CLAUDE.md` lines about the entry skill and "~80 symlinked Layer-3 skills load in every session": rewrite so they say "read the skill file from `~/.openmontage/.agents/skills/<ad>/SKILL.md`"; and decide the fate of `~/.config/openmontage/global-skill-links.txt` (79 lines vs 75 links; stays as a record, marked old).
- Q4 HyperFrames' retired skills (`hyperframes-core`, `-animation`, `-creative`, `-keyframes`, `-audio`, `motion-graphics`): into the library or frozen copy in the project (DURUM.md project scan). Blocks step 5b for the 8 skills IstatistikYoutube reads.
- Q5 Homes of `youtube-arama`, `nlm-skill`, and the 142-file `design-dna`.
- Q6 Will Codex be used by the project that is migrating to Claude; does the project keep a project-level copy.
- Q7 `playwright` in `~/.codex/skills`: confirm it stays (`kalacak`, seeded as Codex's own); `~/.claude/skills/.trash` (about 9 folders from 2026-10-22): leave (default) or clear.
- Q8 `~/.palmier/skills` (10 entries, unknown tool): in scope or ignored (add to `KESIF_YOKSAY`/`izinli` by baseline).
- Q9 Accepted breakage (already decided, D10, DURUM.md): "Psikolojik Danışman Sosyal Medya" and `Istatistik template/.../KIT` get no action and do not block; their global skill calls stop working after emptying; the watchdog never lists them.

---------------------------------------------------------------------------------------------------------------------------

## 8 Deferred and why

- Environment inventory beyond the one key (LaunchAgents, scheduled-task contents, `~/.config/openmontage/.env` presence, `~/.openmontage` venv pins, gh session; scenario 8 rest): different owner/package (P3/P6) and it touches secret-bearing files; this tool only proves the one key line.
- `launchctl getenv` / running-process environment: not reproducible in tests, platform-specific; Dock apps stay an open, documented gap.
- Watching `~/.claude/plugins` and plugin caches, `~/.config/openmontage`, the program tree `~/.openmontage/.agents/skills`: they change legitimately on approved updates; covered by `program-denetim.py` (P6). Recorded as "KALIR, izlenmiyor" in rehber/12.
- Reading `yapay-zeka-araclari.json` (P1) to build the watched list automatically: schema not final; `ek_klasorler` covers the need today.
- GEMINI.md rules / writing any instruction file: D1 and DURUM decision "genel talimat dosyalarına kural yazılmaz"; the tool only reads size/date.
- Shared `parmak_izi`/skip-list refactor into `ortak.py` (akis-08 D): P8's file; no behaviour needed from it here.
- Automatic remediation (a `--temizle` mode): deliberately not built (D7; every removal is an approval).
- Windows paths: the tool targets macOS paths; Windows copies of projects are not machine-wide folders of this Mac.
- Exact lock-file semantics of the `skills` tool beyond reading `skills.<ad>.source`: the file format is the tool's, not ours; unknown shapes fall back to owner `bilinmiyor`.

---------------------------------------------------------------------------------------------------------------------------

## 9 Risks and how the implementer verifies nothing existing broke

Risks
1. Reading shell files that contain a plain-text key (`~/.zshrc`): mitigated by single-regex line matching, discarding everything else, fixed error phrases; test 18 proves no leakage in any output or file.
2. False alarms: Claude/Codex/Cursor apps refreshing vendor folders (handled by `izinli`), `.DS_Store` (noise filter), instruction files edited by the user (not watched for content at all, so no noise), `~/.<x>/skills` discovery of legitimate tools (reported once, accepted by `--yenile`).
3. Baseline drift while emptying is in progress: baseline is refreshed only at step 7; interim runs show `boşaltılan: N` (bilgi). If a session is abandoned mid-way the summary stays `temiz` but shows the numbers; rehber/12 says to finish or roll back within the day.
4. The plan generator emits shell text: it never executes, quotes every path, never emits `rm -rf`, never globs real folders, refuses on unmet pre-checks. The agent still runs it only after approval. Test 27 asserts the absence of `rm -rf`.
5. Moving real folders with `mv` leaves the backup as the single copy until step 7: mitigated by `--yedek-dogrula` (counts and bytes vs baseline) before the next step; the lock file is copied AND moved; `df` check in step 0. Cross-volume `mv` is not atomic: the home folder and `~/Documents/Claude` are on the same volume today; the plan prints a `stat -f %d` same-device check as the first command of steps 5a, 5b, 6 and stops if different.
6. Open Claude sessions hold the old skill list; skills vanish for them only after restart (documented).
7. Exit-code exception: action modes exit 1 on refusal while D4 says report tools exit 1 only with `--siki`. Report mode obeys D4 exactly; action modes are not report mode. If the reviewer disagrees, the alternative is "exit 0 and print DURDUR" for `--plan` unless `--siki` (a one-line change); the tests in 24-25 encode the chosen behaviour for `--plan` (exit 1 only with `--siki`), and only `--taban-yaz` refusals and `--yedek-dogrula` failures exit 1 unconditionally.
8. First `--taban-yaz` on a machine with a stray partial emptying records the remaining entries as `boşaltılacak`; harmless.
9. `gecmis` and the `yazildi` field change the committed file on every refresh: intended audit trail.

Verification that nothing existing broke (the implementer runs; all read-only toward the machine)
- `git status --short` shows only the five new files (plus `araclar/testler/` directory) and the pre-existing modified files listed at session start; no existing tracked file differs because of P2 (`git diff --stat` for those paths empty).
- `python3 araclar/test.py` (existing suite) still passes, run after P8 wires the section; before P8, `python3 araclar/testler/test_p2-genel-bekci.py` alone.
- `python3 araclar/dogrula.py` 0 errors; `python3 araclar/kapsam-denetimi.py` 0 problems (new `rehber/`/`promptlar/` files are expected by P8's index rows; if kapsam-denetimi reports unlisted files, P8's hand-off rows are the fix).
- `python3 araclar/duman-testi.py` unchanged result: the tool is not called by it and does not write to the global folders (`parmak_izi` equal before and after a `genel-bekci.py` run: check by saving `ls -lA` of the three folders before and after and comparing with `diff`).
- Real-machine smoke (read-only): `python3 araclar/genel-bekci.py --rapor-yok` (expect `TABAN YOK`, env line `3 dosyanın 3'ünde var`, discovered `~/.palmier/skills`), `--taban-yaz` dry run, `--plan 3` (prints only; compare `ls ~/.codex/skills` before and after: identical).

---------------------------------------------------------------------------------------------------------------------------

## 10 Acceptance: commands that prove it is done

```
cd /Users/sabanulukaya/Documents/SkillKutuphanesi
python3 araclar/testler/test_p2-genel-bekci.py                  # last line "N/N test geçti", exit 0 (N >= 34)
python3 araclar/genel-bekci.py --help                           # lists --ev --taban --taban-yaz --yenile --evet --plan --yedek-dogrula --ozet-json --siki --ayrinti --rapor --rapor-yok --tarih
python3 araclar/genel-bekci.py --rapor-yok; echo $?             # prints TABAN YOK and the environment line; exit 0
python3 araclar/genel-bekci.py --ozet-json --rapor-yok | python3 -c 'import sys,json; d=json.loads(sys.stdin.read()); assert set(d)=={"arac","durum","satirlar","karar_bekleyen"}; print(d["durum"])'
python3 araclar/genel-bekci.py --taban-yaz                      # dry run only; file must not exist afterwards: test ! -e notlar/genel-klasor-tabani.json
python3 araclar/genel-bekci.py --plan 3 | head -20              # real machine, no baseline yet: prints DURDUR, executes nothing; ls -A ~/.codex/skills identical before/after
python3 araclar/genel-bekci.py --siki --rapor-yok; echo $?      # 0 while TABAN YOK (dikkat), 1 only if a sorun exists
grep -c "^## " rehber/12-genel-klasor-bosaltma.md               # 10 sections as outlined in 3.3
grep -n "ONAY GEREKİR" rehber/12-genel-klasor-bosaltma.md promptlar/16-genel-klasor-bosaltma.md
git status --short | grep -E "genel-bekci|genel-klasor|test_p2|12-genel|16-genel"   # exactly the five new paths
git diff --stat -- araclar/test.py araclar/dogrula.py araclar/ortak.py araclar/duman-testi.py CLAUDE.md AGENTS.md README.md promptlar/README.md   # P2 adds nothing here
```
Notes: all real-machine smoke runs above use `--rapor-yok` so the check writes nothing. On the real machine `--plan 3` prints `DURDUR: taban yok` until the baseline is written with approval (section 7 item 1); plan generation itself is proven only by tests 24-27 and 33c on the fake home.

Done = tests pass, the tool runs on the real home without any write outside the library, the real baseline is NOT yet written (waits for the user's approval), `rehber/12` and `promptlar/16` exist, and the hand-off list in section 6 has been delivered to P8/P3/P4/P6/P1.

---------------------------------------------------------------------------------------------------------------------------

## 11 Review changes

Applied (mandatory)
- Order and prerequisites: `Önkoşul:` line added at the top (commit of the `programlar/` work, P3, P1 `rehber/14`; P2 independent of P5/P6; then P4, P8; emptying last).
- Instruction, command and agent files: only existence is watched (YENİ / KAYIP, plus link target/type). Bytes, mtime and hashes are no longer compared or stored; `DEĞİŞTİ` remains only for link-target change, skill-folder content change (file count / bytes) and the lock file. Sections 3.1.3, 3.1.6 example rows, 3.1.7 table, test 20 and risk 2 updated.

Applied (optional)
- Shell-file reading: made explicit that files are read line by line with a size/line cap, non-matching lines are dropped at once, exceptions are mapped to fixed phrases only (no `str(e)`); new test cases for a directory-as-file, the cap, and non-leakage. The helper is private to this tool; P6 keeps its own copy and test (no shared code, no `ortak.py` change).
- Backup name `genel-klasorler-<tarih>` kept; the P3 hand-off now states that the name was cross-checked.
- P1 hand-off: acceptance record added; plus a safety net: `YENİ KLASÖR` produces the `karar_bekleyen` sentence "Yeni bir yapay zeka aracı klasörü göründü (rehber/14)" so a forgotten `ek_klasorler` step appears in the monthly summary.

Unowned gaps: none taken. B2 triage, `--kayip-isaretle`, the `10-kutuphane-saglik-kontrolu.md` count, `rehber/08`, the `kayip_tarihi` entry, fresh-clone stamp, repeated karar_bekleyen/accepted list, library path in project blocks and kayıp-kaynak monthly reporting do not touch P2's files. The `--hizli`/`--araclar` note is P1/P4 scope. The `--ozet-json` contract here is explicit: it writes no report file (section 3.1.9), which P4 can rely on.

Rejected: none of the corrections was rejected. A baseline hash for instruction files was never added (it would have reintroduced the noise).
