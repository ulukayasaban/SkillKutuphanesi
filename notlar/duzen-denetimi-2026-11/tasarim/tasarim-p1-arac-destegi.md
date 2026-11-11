# P1 Multi-tool install support: design spec

Package key: `p1-arac-destegi`. Status: FINAL DESIGN after review (nothing in the library was edited). Language: English text, Turkish identifiers and user-facing strings exactly as they must appear.

**Önkoşul (implementation order of the whole plan; P1 is step 2):** (0) the uncommitted `programlar/` work is committed first (user approval; the duman test needs a clean tree); (1) P3 landed (library `.gitignore`, `git-durum.py`, `yedek-denetim.py`); then **P1**; then P2, P5, P6 in any order (P6 depends on the tool keys fixed here: `claude-code`, `codex`, `antigravity`, `cursor`, `vscode-copilot`, optional `gemini-cli`, `copilot-cli`); then P7, P4, P8 last. Nothing in P1 reads a P2-P8 file or output; P4 and P8 read P1's `--araclar --ozet-json` and `yapay-zeka-araclari.json`, so P1 must land before them.

**Two phases (review decision).** **Phase 1** = everything in this spec not marked `[AŞAMA 2]`; it is implemented now. **Phase 2** = items marked `[AŞAMA 2]` (`GEMINI.md` block and `--gemini-md`, `--haric`, `kaldir()` sibling warning and empty-role cleanup, project lock `.islem-kilidi`, M2 `ortak-kopya`). Phase 2 is fully designed below so a later session can build it, but it is NOT implemented, NOT documented in rehber/prompts, NOT mentioned in `--help`, and NOT tested until the user has a real need and approves (reason in section 8 and 11). Every sentence below that mentions a Phase 2 flag or code is for that later build only. In particular `promptlar/11` and `rehber/04` must NOT mention a Phase 2 flag or code (`dogrula.py:185-196` would fail).

Implementer rules that apply everywhere in this spec:
- Code first, documents second. `araclar/dogrula.py:185-196` fails (HATA) if prompt 11 mentions a `--flag` or a rehber/04 table code that does not occur literally in the source of `skill-ekle.py`. So every new flag and report code must exist in `skill-ekle.py` before it is written into `promptlar/11` or `rehber/04`. Only P8 may edit `dogrula.py`.
- Every new report line is BİLGİ unless this spec says UYARI or HATA. `onay()` (`skill-ekle.py:1111-1128`) stops a non-interactive run on any UYARI unless `--evet`; the duman test expects "0 uyarı".
- No existing function signature changes. New parameters are keyword-only with a default. Reason: `skill-calistir.py:40` imports `skill-ekle.py` as a module and `test.py:589` calls `se.kur(s, proje, ad, kardes, codex, liste)` positionally.
- Report messages must not start with a single word followed by `": "`. `Rapor.gruplu` (`skill-ekle.py:112-123`) treats `ad: açıklama` with no space in `ad` as a grouped skill name and would mangle the text. All messages below start with a multi-word phrase.
- New argparse attributes are read with `getattr(a, "x", None)`, because `test.py:1057` builds `argparse.Namespace(...)` by hand for `ekle()`.

Milestones: **M1** (Phase 1, everything unmarked) is implemented in full. **M2** (section 3.12, the `ortak-kopya` layout) is Phase 2: fully specified but implemented ONLY after the user answers approval question Q1 (section 7). Tests for M2 and for the other Phase 2 items are in separate groups that the implementer adds only if those items are built.

---

## 1 Purpose

The library already writes one layout that serves five tools (see section 2): real `.agents/skills/<ad>`, `.claude/skills/<ad>` symlink, role files for Claude and Codex, and marked blocks in `CLAUDE.md` and `AGENTS.md`. What is missing is not code for Antigravity, Cursor or Copilot (the files they read already exist), but:

1. Names that say what the choice means. Today `--arac ikisi` / `--arac claude` hide that `ikisi` really serves Codex, Antigravity, Cursor and Copilot, and that `claude` blinds Codex and Antigravity (but not Cursor and VS Code Copilot).
2. A recorded choice. The tool never asks, and a lock without `araclar` silently means `ikisi` (`skill-ekle.py:214-216`).
3. A visible report: which installed tools will and will not see the skills with this choice.
4. A data file about the AI tools (`yapay-zeka-araclari.json`) that the installer, the protection check and the machine-wide watchdog (P2) all read, plus a monthly "did the tool documentation or version change" check.
5. Written flows: choosing the layout, a project copied to Windows or another Mac, adding a new AI tool.
6. Small safety gaps in the installer closed in Phase 1: no `.gitignore` for the backup folder (B6), `--kuru` ignored by `--yenile`/`--geri-al`/`--blok`. Deferred to Phase 2 (reviewer: small gain, big test load, tool not installed): project lock against two concurrent runs (replaced for now by a written warning), `kaldir()` sibling dependency and empty roles, `guncelle()` `--haric`, optional `GEMINI.md`.
7. The project instruction block never says where the library is or what to do when the agent was opened from the project folder (Codex/Antigravity sessions in a project do not know the library path). Closed in Phase 1 (3.1.15): both block variants carry the library path and the "ask for a library session" sentence.

Gaps closed: A1, B9, the `skill-ekle.py` part of B6, critic scenarios 1, 2, 3, 9 (first half), and the unowned gap "block does not name the library path". Taken from the unowned list: that one, plus the "monthly check runs only in full mode" sentence (rehber/14 section 8). Decisions respected: D1 (installed tools only; `GEMINI.md` off by default and now not built), D2 (smallest change, backward compatible), D3 (stdlib only), D4 (`--araclar` follows the report-tool contract), D5, D6, D7, D8, D9, D11.

---

## 2 Existing behaviour relied on (file:line, `araclar/skill-ekle.py` unless stated)

- `:59` `ARACLAR = {"ikisi": ["claude","codex"], "claude": ["claude"]}`. `:1566` `--arac` uses `choices=sorted(ARACLAR)`. `:1178` (`ekle`) and `:1355` (`arac_degistir`) are the only writers of `kilit["araclar"]`.
- `:191-204` `kilit_oku` fills `roller`, `skiller`, `profil`, `surum` but NOT `araclar`. `:214-216` `codex_var(kilit)` = `"codex" in kilit.get("araclar", ARACLAR["ikisi"])`. Real locks: Etsy-Arif and IstatistikYoutube `["claude"]`; Etsy-Yeni and AntigravityTest2 have no field (checked read-only).
- `:207-211` `kilit_yaz` stamps `guncelleme` and `proje_yolu`, creates `.skill-kutuphanesi`, writes via `ortak.json_yaz` (atomic).
- `:572-590` `kur()`: with `codex=False` the real copy goes to `.claude/skills` and `.agents/skills/<ad>` is removed; otherwise real copy in `.agents/skills`, then `os.symlink(relpath)` into `.claude/skills` (`:587`, unconditional, no platform branch; no Windows handling anywhere: grep for `windows`, `os.name`, `platform` finds only the sentence at `:683`).
- `:219-237` `kurulu_hash` / `elle_degismis`: a Claude symlink that turned into an identical real copy is NOT counted as hand-edited (`:233-235`).
- `:239-263` `yedekle()`: targets `.claude/agents`, `.codex/agents`, `AGENTS.md`, `CLAUDE.md`, `.claude/settings.json`, lock, plus per-skill folders; keeps the last 10 (`YEDEK_SAYISI`, `:61`); writes no `.gitignore`. `:273-288` `geri_yukle()` DELETES every target in `hedefler` before restoring `var_olan`. (Consequence for GEMINI.md: a file may only be a target if it is safe to delete, see 3.4.)
- `:600-645` `agent_dosyalari`: Claude `.md` always; Codex `.toml` only when `codex_var`; `.toml` holds absolute paths of this Mac (`:635`).
- `:647-664` `blok_yaz` / `blok_sil`: marked block; `blok_sil` touches a file only if it contains `BLOK_BAS`, deletes the file if nothing else remains. `:667-706` `talimat_bloklari`: `kisa` block carries the "Kütüphanesiz bilgisayarda (ör. Windows) skill ekleme/silme yapma" sentence (`:683`); the `tam` block (`:693-700`) does not. AGENTS.md block only when `codex`; `blok_sil(AGENTS.md)` otherwise.
- `:766-773` `tumunu_yaz`: `hesap_gizle` -> `kilit_yaz` -> `agent_dosyalari` -> `talimat_bloklari`.
- `:853-876` `proje_yapisi_kontrol`: `korunan` = the three `GLOBAL_KLASORLER` + library + `~/.openmontage` (`:855`). `ortak.py:37-41` `GLOBAL_KLASORLER` = `~/.claude/skills`, `~/.codex/skills`, `~/.agents/skills`. `~/.gemini`, `~/.cursor`, `~/.copilot` are not protected.
- `:1111-1128` `onay()`: HATA stops (also with `--zorla` for the `ZORLANAMAZ` set, `:63`); `--kuru` stops after the report; UYARI needs `--evet` or a TTY answer.
- `:1175-1220` `ekle()`; `:1223-1251` `kaldir()` (no sibling check; `kilit["roller"]=[]` only for `hepsi`, `:1246`); `:1254-1345` `guncelle()` (`elle-degistirilmis` is a HATA at `:1283-1310` area, so one edited skill blocks all); `:1348-1356` `arac_degistir()`; `:1359-1425` `dogrula()` (symlink expectation at `:1371-1376`, `proje taşınmış` at `:1413-1414`); `:1427-1447` `durum()` prints `Araçlar: Claude + Codex | sadece Claude`.
- `:1523-1535` `guncelleme_suruyor()`: library-level pid + `baslangic` file, liveness by `kill -0`, stale after 6 h. Template for the project lock.
- `:1568-1613` `main()`: `--help` exits at `:1568`, before `registry()` (`:1569`). The `gk` library-lock check (`:1587`) does not cover `--kaldir`/`--geri-al`. `:1602-1613` the `--yenile`/`--blok` branch ignores `--kuru`; `--geri-al` (`:1599-1600` area) ignores `--kuru`. `:1628` `salt_okur` flag set in `proje_raporunu_yenile` (a read-only flag there prevents the notlar report rewrite and git commit).
- `araclar/proje-kullanimi.py:79` prints `k.get('araclar', []) or '—'` into `notlar/proje-kullanimi.md`.
- `araclar/dogrula.py:185-196` prompt 11 / rehber/04 literal-presence check (see rules above).
- `araclar/test.py:1195-1237` existing `--arac claude` / `--arac ikisi` tests (must keep passing); `test.py:558-600` synthetic-skill helpers (`kayit`, `yeni_proje`, `kur_dongusu`) are the model for the new test file; `test.py:533` loads `skill-ekle.py` with `importlib`.
- Research (read-only audit, 2026-11-11, scratchpad `plan/`): `arac-*.md`, `araclar.json`, `bosluklar.md` table. Key facts used: Antigravity reads `.agents/skills` and, at project level, both `AGENTS.md` and `GEMINI.md` cumulatively; it does not document `.claude/skills` or `CLAUDE.md`. Cursor reads `.agents/skills`, `.cursor/skills`, `.claude/skills`, `.codex/skills`, `AGENTS.md`, and `.claude/agents` / `.codex/agents` role files. VS Code Copilot reads `.github/skills`, `.claude/skills`, `.agents/skills`; `AGENTS.md` and `CLAUDE.md` only when its settings are on. Gemini CLI reads `.gemini/skills` and `.agents/skills`, and `GEMINI.md` only. Symlink support is documented only for Claude (and, for Codex, "symlinked skill folders are followed"); undocumented for Antigravity, Cursor, Copilot, Gemini CLI. Only Claude documents de-duplication of one symlink target.

---

## 3 Changes per file

### 3.1 `araclar/skill-ekle.py` (edit; about +260 lines)

All line numbers are of the current file.

**3.1.1 Names (`:59`, `:1566`).**
Old: `ARACLAR = {"ikisi": [...], "claude": [...]}`.
New:
```python
ARACLAR = {"ikisi": ["claude", "codex"], "claude": ["claude"],
           "ortak": ["claude", "codex"], "yalniz-claude": ["claude"]}      # M2 adds "ortak-kopya"
ARAC_TAKMA = {"ikisi": "ortak", "claude": "yalniz-claude"}                  # eski ad -> ad
DUZEN_KLASORLERI = {"ortak": [".agents/skills", ".claude/skills"], "yalniz-claude": [".claude/skills"]}
DUZEN_TALIMAT = {"ortak": ["CLAUDE.md", "AGENTS.md"], "yalniz-claude": ["CLAUDE.md"]}   # [AŞAMA 2] + GEMINI.md when kilit gemini_md
ARAC_JSON = KOK / "yapay-zeka-araclari.json"
ARAC_BELGE_GUN = 45
# [AŞAMA 2] ISLEM_KILIDI = ".islem-kilidi"; KILIT_BAYAT_SN = 6 * 3600
```
Review note: the aliases (`ARAC_TAKMA`) stay in Phase 1 although the reviewer listed them for Phase 2. Reason: about 8 lines, a pure name mapping with no new lock value (`araclar` still holds `["claude","codex"]` / `["claude"]`), existing `--arac ikisi|claude` keeps working, and gap A1 is exactly "the names hide what the choice means"; every document, prompt and the `arac-duzeni` line use the new names. Deferring would force docs to be renamed later and keep the misleading names meanwhile.
`--arac` help text (new): `"proje hangi araçlarla açılacak: ortak (Claude + Codex + Antigravity + Cursor + VS Code Copilot; varsayılan) | yalniz-claude (yalnız Claude; Cursor ve VS Code Copilot da .claude/skills'i okur) ; eski adlar: ikisi = ortak, claude = yalniz-claude. Kurulu skiller yeni düzene göre yeniden kurulur"`.
`duzen_adi(kilit)` -> `"ortak"` if `"codex" in kilit["araclar"]` else `"yalniz-claude"` (M2: `"ortak-kopya"` when `kilit.get("baglanti") == "kopya"`).
`duzen_uygula(kilit, secim)`: `d = ARAC_TAKMA.get(secim, secim)`; `kilit["araclar"] = list(ARACLAR[d])`; `kilit["arac_secimi"] = "secildi"`; M2 also sets/removes `kilit["baglanti"]`.
Both `ekle()` (`:1178`) and `arac_degistir()` (`:1355`) call `duzen_uygula` instead of assigning `ARACLAR[a.arac]` directly. Lock content for `--arac ikisi|ortak` is the same list as today: `["claude","codex"]`; `claude|yalniz-claude`: `["claude"]`. No new list values are ever written.

**3.1.2 Lock fields (`kilit_oku :191`, `kilit_yaz :207`).**
`kilit_oku`, before the existing `setdefault`s: `k.setdefault("arac_secimi", "secildi" if "araclar" in k else "varsayilan")`. Not written to disk by read-only commands.
`kilit_yaz`: before `json_yaz`: `kilit.setdefault("araclar", list(ARACLAR["ikisi"]))`. So a lock written for the first time (or the first write on an old lock without the field) records `["claude","codex"]` and `arac_secimi: "varsayilan"`. A lock that already has `araclar` keeps it untouched; if it had no `arac_secimi` (written by the old tool after `--arac`) it becomes `"secildi"` via `kilit_oku`.
`[AŞAMA 2]` New optional field `gemini_md` (bool), persisted exactly like `blok` (`:1177`). Absent means false. `KILIT_SURUM` stays 3: all additions are optional fields (in Phase 1 the only new field is `arac_secimi`).
Lock after the first default install:
```json
{"surum": 3, "araclar": ["claude", "codex"], "arac_secimi": "varsayilan", "profil": "landing-page", "roller": ["ui-tasarimci"], "skiller": {"...": {}}, "guncelleme": "2026-11-12", "proje_yolu": "/Users/x/Documents/P"}
```
Side effect to expect and accept: the first write on a project whose lock had no `araclar` flips the "Araçlar" cell of `notlar/proje-kullanimi.md` from `—` to `claude, codex` (reader `proje-kullanimi.py:79`); that report is regenerated and auto-committed by `proje_raporunu_yenile` (`:1625-1648`).

**3.1.3 Loading the tool data (new, after `kilit_yaz`).**
```python
def arac_kayitlari(yol=None):
    """yapay-zeka-araclari.json -> kayıt listesi; yok/bozuksa None (çağıran satırları atlar, çökmez)."""
def arac_korunan_yollar(kayitlar=None) -> list[Path]:
    """Her kaydın kullanici_koku'nu (ör. ~/.gemini) genişletip çözer; kayıtlar yoksa []."""
```
Both read lazily (not at import), never raise on missing/invalid JSON. They use `ARAC_JSON` looked up at call time so tests can monkeypatch it.

**3.1.4 Report lines (new `arac_satirlari`).**
```python
def arac_satirlari(proje, kilit, rapor, secim=None, kayitlar=None):
```
`secim` = the `--arac` value of this run or None. `kayitlar=None` loads `arac_kayitlari()`. If the data cannot be read: one BİLGİ `arac-belge-yok` and return (never UYARI). Otherwise (`duzen = duzen_adi(kilit)`, `klasorler = DUZEN_KLASORLERI[duzen]`, `kurulu` = records with `kurulu` true):
`gorur(k) = set(k["proje_skill_okur"]) & set(klasorler)`; `gorenler`/`gormeyenler` over installed tools. Lines (exact Turkish in section 4):
1. `arac-duzeni` BİLGİ, always.
2. `arac-gormez` BİLGİ, only when `gormeyenler` is non-empty.
3. `arac-secimi-yok` BİLGİ, only when `kilit["arac_secimi"] == "varsayilan"` and `secim is None`.
4. `arac-cift-okuma` BİLGİ, only for `ortak` and only when some installed tool reads both folders (`set(klasorler) <= set(k["proje_skill_okur"])`, expected Cursor and VS Code Copilot).
5. `arac-symlink` BİLGİ, only for `ortak` and only when `(proje / ".git").exists()`.
6. `arac-rolsuz` BİLGİ, only when `kilit["roller"]` is non-empty: installed tools whose `rol_dosyasi.uretilir` is false are named.
7. `arac-mutlak-yol` BİLGİ, only when `codex_var(kilit)` and `kilit["roller"]` non-empty.
8. `[AŞAMA 2]` `gemini-md` BİLGİ, only when `kilit.get("gemini_md")` is true (not built in Phase 1).
Call sites: `ekle()` right after `on_kontrol(...)` (`:1186`, before the `print` of the plan so the lines are in `rapor`); `guncelle()` right after `proje_yapisi_kontrol(...)` (`:1257`), `secim=None` there, except via `arac_degistir` which passes the lock it already changed (the `arac-secimi-yok` line then disappears because `duzen_uygula` set `secildi`). `--yenile` prints nothing new.
`durum()` (`:1427-1432`): keep the existing `Araçlar: Claude + Codex | sadece Claude` text and append ` · düzen: ortak (varsayılan: seçim yapılmadı)` or ` · düzen: yalniz-claude (seçildi)`.
`arac_degistir()` (`:1351-1352`): keep the two existing label strings and append the layout names, e.g. `Araçlar: Claude + Codex (ortak) -> sadece Claude (yalniz-claude)`.

**3.1.5 Mixed layout guard in `ekle()`.**
Before applying `--arac` capture `onceki = list(kilit["araclar"])`. After `on_kontrol` returns `adlar`: if `a.arac` and `ARACLAR[a.arac] != onceki` and `set(kilit["skiller"]) - set(adlar.values())` is non-empty, add HATA `arac-karisik` (not in `ZORLANAMAZ`, so `--zorla` can pass, which is the existing behaviour): message in section 4. Existing test `test.py:926` (fresh project, `--skill ... --arac claude`) is unaffected; `--arac X` alone still routes to `arac_degistir` (`:1604`).

**3.1.6 `[AŞAMA 2 — NOT BUILT NOW]` GEMINI.md (optional block).** Kept as a ready design; D1: Gemini CLI is not installed and Antigravity already reads `AGENTS.md`. Build only when Gemini CLI is installed or the user asks. While not built, `--araclar` still reports the Gemini CLI record as `kurulu: false` and prints the decision line if it appears installed.
- New flag: `ap.add_argument("--gemini-md", choices=("ac", "kapat"), help="GEMINI.md'ye aynı skill bloğunu yaz/kaldır (varsayılan kapalı; yalnız Gemini CLI için gerekir, Antigravity AGENTS.md'yi zaten okur). Kilide yazılır")`.
- `gemini_md_ayarla(kilit, deger) -> str|None`: `deger == "ac"` while `not codex_var(kilit)` returns the HATA text `gemini-md-duzen` (section 4); otherwise sets `kilit["gemini_md"] = (deger == "ac")` and returns None.
- `main()` branch (`:1602`): condition becomes `a.yenile or ((a.blok or a.gemini_md) and not (a.profil or a.rol or a.skill or a.planlayici or a.guncelle))`; inside it, after `kilit["blok"]`: apply `gemini_md_ayarla`; on error print `[HATA] gemini-md-duzen: ...` and `return 2`. `ekle()` and `guncelle()` also accept `--gemini-md` together with other operations: in `ekle()` right after `a.blok` handling (`:1179`); `guncelle()` receives the lock from `main` unchanged, so for `--guncelle --gemini-md ac` the value is applied in `main` before the call (pass via `kilit=` as `arac_degistir` does).
- `talimat_bloklari` (`:667`): (a) empty-skills branch: add `"GEMINI.md"` to the `blok_sil` loop. (b) After the AGENTS.md write in both the `kisa` branch (before its `return`, `:690`) and the `tam` branch: `blok_yaz(proje / "GEMINI.md", "\n".join(s)) if (kilit.get("gemini_md") and codex) else blok_sil(proje / "GEMINI.md")`. Same text as the other files; `blok_sil` only touches a file that holds our marker, so a user's own GEMINI.md is never harmed.
- `yedekle()` (`:239`): new keyword-only parameter `gemini=False`. `"GEMINI.md"` is added to `hedefler` only if `gemini` is true or the existing file contains `BLOK_BAS`. Callers pass `gemini=bool(kilit.get("gemini_md"))` (`ekle`, `kaldir`, `guncelle`, `--yenile`); `geri_al` passes nothing (marker check only). Reason: `geri_yukle` deletes every target before restoring (`:273-288`); a user's own GEMINI.md that we never touched must never become a target.
- `dogrula()` (`:1359`): if `kilit["skiller"]` and `kilit.get("gemini_md")`: `GEMINI.md` must exist and contain both markers, else sorun `GEMINI.md: skill-kutuphanesi bloğu eksik/bozuk (--yenile)`. If not `gemini_md` and `GEMINI.md` contains `BLOK_BAS`: sorun `GEMINI.md: gemini_md kapalı ama skill-kutuphanesi bloğu duruyor (--yenile)`.

**3.1.7 `[AŞAMA 2 — NOT BUILT NOW]` Project lock (new `proje_islem_kilidi`).** Phase 1 replacement: a written warning only (rehber/01 and promptlar/09, sections 3.4 and 3.6): "Aynı projede iki oturumdan aynı anda skill-ekle çalıştırma; ikinci oturum açmadan önce ilkinin bittiğine bak." No lock file, no `main()` refactor into `_calistir`, no `.islem-kilidi` in the `.gitignore`. Reason: new code path in the largest working tool, new file in the project, new test load; the realistic risk (two sessions in one project at once) is low and the warning covers it. Ready design for later:
```python
@contextlib.contextmanager
def proje_islem_kilidi(proje, islem="islem"):
```
- File: `<proje>/.skill-kutuphanesi/.islem-kilidi`, JSON `{"pid": int, "baslangic": ISO, "makine": socket.gethostname(), "islem": str}`.
- Create atomically: `os.open(path, O_CREAT | O_EXCL | O_WRONLY)`. If the meta folder does not exist, create it and remember `meta_yeni = True`.
- On `FileExistsError`: read the file; it is "live" if `time since baslangic < KILIT_BAYAT_SN` AND (the pid exists on this host: `os.kill(pid, 0)` succeeds or raises `PermissionError`; if `makine` differs from this host, the process cannot be probed, so live = younger than the limit). Live: `print(BEKLE message)` then `sys.exit(2)`. Stale (dead pid, unreadable file, or older than 6 h): unlink and retry once.
- `finally`: unlink the file; if `meta_yeni` and the meta folder is now empty, `rmdir` it (so a refused or failed run on a fresh project leaves no trace).
- Exit code 2 = "nothing was done", same as `DURDU` in `onay()`. The message is section 4 `BEKLE`.
- Where taken: `main()`, after the `guncelleme_suruyor` check and after the read-only dispatches (`--durum`, `--dogrula`, `--yedekler`). Rule for the implementer: **no lock for `--durum`, `--dogrula`, `--yedekler`, `--oner`, `--listele`, `--araclar` and for any `--kuru` run; lock for everything else, including `--kaldir` and `--geri-al`.** Implementation: move the dispatch from `:1599` onward into `def _calistir(a, proje, skiller, ap)` and call it inside `with proje_islem_kilidi(proje, ...)` when a lock is needed.

**3.1.8 `--kuru` honoured everywhere (fixes the docstring promise "--kuru hiçbir dosya yazmaz").**
In `main()`: if `a.kuru` and (`a.yenile` or `a.geri_al` or (`a.blok` without install flags `--profil/--rol/--skill/--planlayici/--guncelle`)): print `[kuru] Hiçbir şey değiştirilmedi. (yapılacak: <yenile|geri-al|blok>)`, return 0 before any write. Old behaviour (these three ignored `--kuru` and wrote) is a bug, not a contract. (Phase 2 adds `gemini-md` to the list.)

**3.1.9 Backup folder `.gitignore` (B6) in `yedekle()`.**
After `y.mkdir(...)` (`:241`): `meta_gitignore(proje)`:
- file `.skill-kutuphanesi/.gitignore` missing: write `yedek/\n`. (Phase 2 adds `.islem-kilidi`.)
- present: read; append `yedek/` only if missing (never rewrite or reorder, never remove user lines). Match a line after strip, with or without trailing slash (`yedek` / `yedek/`).
- never added to `hedefler`; never created by `--kuru` (since `yedekle` runs only after approval).

**3.1.10 Protection list.**
`proje_yapisi_kontrol` (`:855`) and `main` (`:1578`): `korunan = [...existing...] + arac_korunan_yollar()`. With the data file this adds `~/.gemini`, `~/.cursor`, `~/.copilot` (plus `~/.claude`, `~/.codex` already in `main`'s list). If the file is missing the list equals today's. No other behaviour change.

**3.1.11 Platform guard.**
Top of `main()` after `parse_args` for any operation that has a project: `if os.name == "nt": sys.exit("skill-ekle.py Windows'ta çalıştırılmaz (symlink, kill -0 ve Mac yolları). Skill ekleme/güncelleme kütüphanenin olduğu Mac'te yapılır; Windows'ta açılan projeler için rehber/14 bölüm 5.")`. (The check is a one-liner; the code has no Windows support today, so we say so instead of failing later with `OSError`.)

**3.1.12 `[AŞAMA 2 — NOT BUILT NOW]` `kaldir()` safety (C items).** Ready design; reasons for deferral: new UYARI changes the exit behaviour of `--kaldir` (R5), empty-role cleanup changes what `kilit["roller"]` means (R4), both need `test.py` regression checks owned by P8. Until built the library session checks `python3 araclar/proje-kullanimi.py --skill <kimlik>` (P5, existing) before removing, as rehber/01 already says.
- Sibling dependency: for each name in `hedefler`, for every remaining skill `b` in `kilit["skiller"]` (not itself in `hedefler`): if the removed name is a value of `b["kardes"]` (lock field written by `kayit_guncelle :1145`), add UYARI `kardes-bagimli` (section 4), one line per (removed, dependent) pair. UYARI, not HATA: `--evet` (or interactive yes) proceeds, because the user may intend it. `--kaldir hepsi` produces none (both sides removed).
- Empty roles: after deleting the skills, `kilit["roller"]` keeps only roles that still have at least one skill: `[r for r in kilit["roller"] if any(r in k["roller"] for k in kilit["skiller"].values())]` (`agent_dosyalari` then removes the generated agent files of roles no longer listed, `:640-645`). BİLGİ `bos-rol` is added to the report before approval for each role that will disappear. Only tool-generated agent files (marker `URETILDI`) are removed, as today.
- At the end of `--kaldir hepsi`, print one extra line: `Bu proje artık kütüphaneden skill kullanmıyor. Takipten çıkarmak (projeler.json / .skill-kutuphanesi klasörü) ayrı ve onaylı bir iştir; bkz. rehber/10.` (no deletion; ownership of project tracking is P5).

**3.1.13 `[AŞAMA 2 — NOT BUILT NOW]` `guncelle()` safety: `--haric`.** Phase 1 workaround that needs no code: when one hand-edited skill (`elle-degistirilmis`) blocks the update, the library session shows the report to the user and offers (a) `--zorla` on that skill after the user decides, or (b) updating only after the user restores the skill (`--kaldir <ad>` then `--skill <ad>`), as `rehber/04` already describes. Ready design:
- New flag `--haric` (`nargs="+"`, metavar `skill`): only meaningful with `--guncelle` / `--arac`.
- In the `guncelle()` loop (`:1257-1310`), first statement for each `ad`: if `ad in (getattr(a, "haric", None) or [])`: BİLGİ `haric-atlandi` and `continue`. After the loop: for each name in `haric` not in `kilit["skiller"]`: UYARI `haric-yok`.
- Default behaviour unchanged: without `--haric` a hand-edited skill is still HATA `elle-degistirilmis` and stops the run (existing tests depend on it); with `--haric <ad>` the others update normally.

**3.1.14 Read-only subcommand `--araclar` (monthly tool/document check).**
New flags: `--araclar`, `--ozet-json`, `--siki` (all `store_true`). Handled in `main()` BEFORE `registry()` (so it does not load 22 MB) and without needing a project: `if a.araclar: return araclar_raporu(a)`. `--ozet-json` or `--siki` without `--araclar`: `ap.error`. Add `"--araclar"` to `salt_okur` in `proje_raporunu_yenile` (`:1628`) so the notlar report is not rewritten or committed.
```python
def araclar_raporu(a, kayitlar=None, simdi=None) -> int
```
Reads `ARAC_JSON`. For each record and each entry of `surumler`: `bulunan = surum_oku(okuma)` where
- `{"komut": [...]}`: `subprocess.run(cmd, capture_output=True, text=True, timeout=10)`; the first match of `\d+(?:\.\d+)+` in stdout; any failure (not found, timeout, non-zero, no match) gives `None`;
- `{"plist": "/Applications/X.app/Contents/Info.plist"}`: `plistlib.load`, key `CFBundleShortVersionString`; file missing gives `None`.
Computation of `durum`:
- `sorun`: file missing, invalid JSON, not the expected shape, or a record lacking one of the required keys (`anahtar`, `ad`, `kurulu`, `proje_skill_okur`, `dogrulama_tarihi`, `surumler`).
- `dikkat`, with one `karar_bekleyen` line each: (a) a record whose `dogrulama_tarihi` is older than `ARAC_BELGE_GUN` (45) days; (b) `bulunan` differs from `kayitli` while both are not None; (c) the record says `kurulu: true` but no entry was found; (d) the record says `kurulu: false` but an entry was found.
- `temiz` otherwise. Always add one summary line to `satirlar`.
Output: human mode prints a table (`Araç | kurulu | okuduğu proje skill klasörleri | kayıtlı sürüm | bulunan sürüm | doğrulama (gün önce)`) and the decision lines. `--ozet-json` prints exactly ONE JSON object to stdout and nothing else:
```json
{"arac": "arac-belgeleri", "durum": "dikkat", "satirlar": ["7 araç kayıtlı, 5 kurulu; en eski doğrulama 2026-11-11 (0 gün)", "Codex: kayıtlı sürüm 0.167.0, bulunan 0.171.0"], "karar_bekleyen": ["Codex: sürüm 0.167.0 -> 0.171.0; belgeleri yeniden doğrula (rehber/14 bölüm 8) ve dogrulama_tarihi'ni güncelle"]}
```
Exit code: 0 always when the tool ran correctly; with `--siki` exit 1 only if `durum == "sorun"`. Writes nothing in the library (D4).

**3.1.15 Block sentences (scenario 3 and the "library path" gap).**
New module constant `BLOK_KUTUPHANE = "Kütüphane: `~/Documents/SkillKutuphanesi` (kütüphanenin CLAUDE.md/AGENTS.md dosyası orada). Skill ekleme, silme ve güncelleme yalnız kütüphane klasöründe açılan oturumda yapılır; bu proje klasöründen açılan oturumdaysan kullanıcıdan kütüphane klasöründe oturum açmasını iste ya da ihtiyacı not düş. Kütüphanesiz bilgisayarda (ör. Windows) skill ekleme/silme yapma."`.
- `kisa` branch (`:681-684`): replace its existing sentence `Kütüphanesiz bilgisayarda (ör. Windows) skill ekleme/silme yapma; ihtiyacı not düş, kütüphane sahibi kurar. ` by `BLOK_KUTUPHANE + " "` (the old sentence is contained in the new one in substance; the old command path `~/Documents/SkillKutuphanesi/araclar/skill-ekle.py` in the same block stays).
- `tam` branch (`:693-700`): append ` ` + `BLOK_KUTUPHANE` to the last paragraph, after the `--guncelle` command.
- Same text in `CLAUDE.md` and `AGENTS.md` blocks (both written from the same list `s`). The path `~/Documents/SkillKutuphanesi` is the library location on this Mac and is already hard-coded in both blocks (`:682`, `:700`); `ortak.KOK` is not used so the text stays identical across Macs.
Effect: blocks in existing projects change at their next write (`--yenile`, `--guncelle`, `--skill`, `--kaldir`, `--arac`); no project is touched by installing this package. Needs approval wording in section 7 (Q3). Test 36 checks both blocks contain `Kütüphane: ~/Documents/SkillKutuphanesi` and `Kütüphanesiz bilgisayarda`.

**3.1.16 Docstring (`:1-37`).** Replace the `--arac claude` paragraph and the example line `--arac claude --kuru` with the new names (`--arac yalniz-claude`), add the examples `--arac ortak --kuru`, `--araclar`. (Phase 2 would add `--gemini-md ac --kuru` and `--guncelle --haric <skill>`.)

### 3.2 `yapay-zeka-araclari.json` (new, library root, about 330 lines)

Purpose: single data file about AI tools. Used by (a) `skill-ekle.py` (`arac_satirlari`, `arac_korunan_yollar`, `--araclar`), (b) P4 `aylik-ozet.py` through `--araclar --ozet-json`, (c) P6 `program-denetim.py` and P8 `dogrula.py`, which only check the tool keys, (d) humans (`rehber/14`). P2's watchdog does NOT read it (P2 deferred that; the machine-wide folders a tool writes are owned by exactly one place, P2's `notlar/genel-klasor-tabani.json` -> `ek_klasorler`; this file does not repeat them). It is the only place that records what each tool reads; no other file repeats it (rehber/14 shows a table generated by hand from it and says the JSON wins).

Top level: `{"_aciklama": str, "surum": 1, "dogrulama_siniri_gun": 45, "araclar": [record, ...]}`. `araclar` is a LIST of records, each with the string field `anahtar` (not a dict keyed by tool). Consumers that need a map build `{k["anahtar"]: k for k in d["araclar"]}`.
Record fields (machine fields first; prose fields copy the researched text from scratchpad `plan/araclar.json` and `plan/arac-*.md`, translated into plain Turkish, keeping the "second reading" corrections):

| field | type | meaning / who reads it |
|---|---|---|
| `anahtar` | str | stable id, exactly these strings (P6 and P8 depend on them): `claude-code`, `codex`, `antigravity`, `cursor`, `vscode-copilot`; optional (not installed, D1) `gemini-cli`, `copilot-cli` |
| `ad` | str | long name |
| `ad_kisa` | str | name used in report lines: `Claude Code`, `Codex`, `Antigravity`, `Cursor`, `VS Code Copilot`, `Gemini CLI`, `Copilot CLI` |
| `kurulu` | bool | installed on this Mac when verified (D1: supported = installed) |
| `destek` | `"tam"`/`"istege-bagli"`/`"yok"` | `tam` installed and served by the layouts; `istege-bagli` not installed, served by `.agents/skills` plus optional `GEMINI.md`; `yok` not served |
| `surumler` | list of `{"ad", "kayitli", "okuma"}` | `okuma` = `{"komut": [...]}` or `{"plist": "<path>"}`; `kayitli` null when not installed; read by `--araclar` |
| `proje_skill_okur` | list of project-relative folders | MACHINE field: what the tool reads in a project; visibility = overlap with the layout |
| `proje_talimat_okur` | list of file names read unconditionally | MACHINE field (report line 1 "talimat bloğu" part) |
| `proje_talimat_kosullu` | list of strings | read only under a condition (text states the condition) |
| `rol_dosyasi` | `{"yol", "bicim", "uretilir": bool, "neden"}` | which role file format; whether the library generates it and why not |
| `kullanici_koku` | str | the tool's user folder, e.g. `~/.gemini`; added to the protected list (`arac_korunan_yollar`) |
| `genel_skill_okur` | list of str | machine-wide skill folders it reads (informational only; the watched-folder list is P2's `ek_klasorler`) |
| `symlink` | str | documented / undocumented, with source |
| `ayni_ad_onceligi` | str | prose |
| `alt_ajan_bicimi` | str | prose |
| `kaynaklar` | list of URL str | official documentation pages read |
| `dogrulama_tarihi` | `YYYY-MM-DD` | date the record was verified against the sources |
| `belirsizler` | list of str | open uncertainties (never deleted without a real test) |
| `denendi` | list of `{"tarih", "sonuc"}` | real-world tests (a tool really listing a skill from a project). Empty for all tools at creation: nothing has been tested by this package. |

Records to create (all `dogrulama_tarihi` `2026-11-11`):

| anahtar | kurulu / destek | surumler (kayitli: okuma) | proje_skill_okur | proje_talimat_okur (+kosullu) | rol_dosyasi | kullanici_koku |
 |
| claude-code | true / tam | `2.1.319`: komut `["claude","--version"]` | `[".claude/skills"]` | `["CLAUDE.md"]` (+`AGENTS.md` only if no CLAUDE.md exists) | `.claude/agents/*.md`, md-yaml, uretilir true | `~/.claude` |
| codex | true / tam | `0.167.0`: komut `["codex","--version"]` | `[".agents/skills"]` | `["AGENTS.md"]` (+`AGENTS.override.md`; `CLAUDE.md` only via `project_doc_fallback_filenames`) | `.codex/agents/*.toml`, toml, uretilir true | `~/.codex` |
| antigravity | true / tam | `2.29.0`: plist `/Applications/Antigravity.app/Contents/Info.plist`; `2.6.0`: plist `/Applications/Antigravity IDE.app/Contents/Info.plist` | `[".agents/skills"]` | `["AGENTS.md","GEMINI.md"]` (read together, cumulative) | `.agents/agents/*.md`, md-yaml, uretilir **false**, neden: "alan adları ve önyükleme anlamı belgede tam değil, IDE'nin gerçek yolu doğrulanmadı; her ajan projedeki tüm skilleri görür" | `~/.gemini` |
| cursor | true / tam | `3.25.6`: plist `/Applications/Cursor.app/Contents/Info.plist` | `[".agents/skills", ".cursor/skills", ".claude/skills", ".codex/skills"]` | `["AGENTS.md"]` (+`.cursor/rules/*.mdc`) | `.cursor/agents/*.md`, md-yaml, uretilir **false**, neden: "Cursor .claude/agents ve .codex/agents dosyalarını da okur (belge); ayrı dosya gerekmez" | `~/.cursor` |
| vscode-copilot | true (yalnız VS Code; Copilot CLI ayrı kayıt, kurulu değil) / tam | `1.146.0`: plist `/Applications/Visual Studio Code.app/Contents/Info.plist` | `[".github/skills", ".claude/skills", ".agents/skills"]` | `[".github/copilot-instructions.md"]` (+`AGENTS.md` if `chat.useAgentsMdFile`, `CLAUDE.md` if `chat.useClaudeMdFile`) | `.github/agents/*.agent.md`, md-yaml, uretilir **false**, neden: "format ayrı; `.claude/agents` okunuyor mu belgede yok" | `~/.copilot` |
| gemini-cli | false / istege-bagli | `null`: komut `["gemini","--version"]` | `[".gemini/skills", ".agents/skills"]` | `["GEMINI.md"]` (+`AGENTS.md` only via `context.fileName`) | `.gemini/agents/*.md`, md-yaml, uretilir false | `~/.gemini` |
| copilot-cli | false / istege-bagli | `null`: komut `["copilot","--version"]` | `[".github/skills", ".claude/skills", ".agents/skills"]` | `[".github/copilot-instructions.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md"]` (hepsi belgede okunuyor; `@` ile göreli import) | `.github/agents/*.agent.md`, md-yaml, uretilir false, neden: "kurulu değil; format ayrı" | `~/.copilot` |

Mandatory `belirsizler` entries (copied from the audit, do not drop): Claude: `.agents/skills` not read (documented absence); Codex: whether `~/.codex/skills` is still read, same-name priority undocumented, relative symlink inside a project untested, `[[skills.config]] name = ` form (portable alternative to absolute `path`) unverified; Antigravity: symlink, `CLAUDE.md` and `.claude/skills` not documented, IDE 2.6.0 real folder (`~/.gemini/antigravity/skills` vs `config/skills`); Cursor: `CLAUDE.md` not documented, same-name priority and symlink undocumented, `cursor-agent` not on PATH; Copilot: same-name priority in VS Code, `.claude/agents` read or not, symlink undocumented, VS Code "Local harness" deprecated (Feb 2027); Copilot CLI (not installed): project skill beats personal skill (documented), personal agent beats project agent (opposite rule), `.claude/settings.json` partly read; Gemini CLI: symlink undocumented, extra-folder setting, doc says free users move to Antigravity CLI (June 2026). Cross-tool: "Cursor ve Copilot ortak düzende hem .agents/skills hem .claude/skills okuyor: aynı skill iki kez listelenebilir; yalnız Claude tek hedefi bir kez yüklediğini belgeliyor; denenmedi."

Example (one record, complete):
```json
{
  "anahtar": "claude-code",
  "ad": "Claude Code (CLI ve masaüstü Code sekmesi)",
  "ad_kisa": "Claude Code",
  "kurulu": true,
  "destek": "tam",
  "surumler": [{"ad": "Claude Code CLI", "kayitli": "2.1.319", "okuma": {"komut": ["claude", "--version"]}}],
  "proje_skill_okur": [".claude/skills"],
  "proje_talimat_okur": ["CLAUDE.md"],
  "proje_talimat_kosullu": ["AGENTS.md (yalnız çalışma klasöründe ve üstünde hiç CLAUDE.md yoksa, v2.1.277+)"],
  "rol_dosyasi": {"yol": ".claude/agents/*.md", "bicim": "md-yaml", "uretilir": true, "neden": ""},
  "kullanici_koku": "~/.claude",
  "genel_skill_okur": ["~/.claude/skills"],
    "symlink": "belgeli: proje/kişisel/kurumsal skill girdisi symlink olabilir, hedef bir kez yüklenir; göreli proje içi bağ için ayrı örnek yok",
  "ayni_ad_onceligi": "kurumsal > kişisel (~/.claude/skills) > proje: genel klasördeki aynı adlı skill proje kopyasını gölgeler",
  "alt_ajan_bicimi": "...(araclar.json metni)...",
  "kaynaklar": ["https://code.claude.com/docs/en/skills", "https://code.claude.com/docs/en/memory", "https://code.claude.com/docs/en/sub-agents"],
  "dogrulama_tarihi": "2026-11-11",
  "belirsizler": [".agents/skills, .codex/skills, .gemini/skills okunduğu belgede yok", "göreli symlink'in proje içinde çalıştığı belgede açık örnekle yok"],
  "denendi": []
}
```
No secrets, tokens or account data in this file (D9); version strings and public paths only.

How the consumers use it:
- Installer: `arac_satirlari` (visibility), `arac_korunan_yollar` (protection), `--araclar` (age, version, installed-state).
- Watchdog (P2): does NOT read this file now (P2 deferred it). Machine-wide folders that tools write (Claude `synced`, Codex `.system`, Cursor `skills-cursor`, `~/.gemini/*/skills`, `~/.copilot/skills`) are tracked only in P2's `ek_klasorler`; see the non-binding candidate list in section 6 "To P2". `kullanici_koku` stays here only for the installer's protected-path list.
- Program audit (P6) and `dogrula.py` (P8): read only the `anahtar` values.
- Monthly (P4): subprocess `python3 araclar/skill-ekle.py --araclar --ozet-json`.

### 3.3 `rehber/14-yapay-zeka-araclari.md` (new, about 170 lines)

Outline (Turkish, plain words; tables in this file are copies of the JSON and state that the JSON wins):
1. Neden bu belge: one folder layout serves many tools; this is where choices are explained.
2. Hangi araç neyi okur: table (7 tools × project skill folders, instruction files, role files, symlink documented?, last verified). Footnote: unverified items live in the JSON `belirsizler`.
3. Düzen seçimi: question to ask the user ("Bu proje hangi araçlarla açılacak?"), decision table:
   - Codex or Antigravity used -> `ortak`.
   - Only Claude Code (Cursor, VS Code Copilot may also open it) -> `yalniz-claude` (they read `.claude/skills`; they miss the `AGENTS.md` block, Codex/Antigravity see nothing).
   - Opened on Windows -> today `yalniz-claude` (Etsy-Arif does this); Codex and Antigravity are blind there; M2 option `ortak-kopya` only if the user approved it.
   - Unknown -> `ortak` (default) and record with `--arac ortak` once the user answers.
   - Gemini CLI used (not installed now) -> `ortak` (Gemini CLI reads `.agents/skills`); it also reads `GEMINI.md`, and the library does not write that file yet (Phase 2, `--gemini-md`). Tell the user and ask whether to build Phase 2.
   How to record: `--arac <düzen> --kuru`, then `--evet`; check the `arac-duzeni` line.
4. Projede ne oluşur: one tree per layout (`ortak`, `yalniz-claude`; M2 `ortak-kopya`).
5. Windows ve başka bilgisayara kopyalama: what travels (`.agents`, `.claude`, `.codex`, `CLAUDE.md`, `AGENTS.md`, `.skill-kutuphanesi/kilit.json`); what breaks: (a) symlinks become text files without `core.symlinks` (so `ortak` is unsafe on Windows), (b) `.codex/agents/*.toml` hold this Mac's absolute paths (Codex cannot disable role-excluded skills elsewhere; fix on the library Mac with `--yenile`), (c) lock `proje_yolu` mismatches (`--dogrula` reports `proje taşınmış`; fix with `--yenile`), (d) line-ending conversion on Windows can change file hashes and show false `elle-degistirilmis` back on the Mac; recommended `.gitattributes` text for the project (documented only, the tool never writes it): `.agents/skills/** -text` and `.claude/skills/** -text`, (e) the library does not exist there: updates only from the library Mac (the instruction block tells agents so and names the library path, see 3.1.15), (f) `skill-ekle.py` refuses to run on Windows (3.1.11). Step list "projeyi başka Mac'e kopyaladım" and "projeyi Windows'ta açacağım".
6. GEMINI.md: not written by the library (Phase 2, built only when Gemini CLI is installed or the user asks). Why: Antigravity reads AGENTS.md and GEMINI.md cumulatively, so a block in both would load twice; Gemini CLI alone needs it. Describe the planned flag `--gemini-md ac|kapat` as a plan, not as a command that works today.
7. Yeni bir yapay zeka aracı eklendiğinde (the written flow; also embedded in `promptlar/15`):
   1. Ask the user the tool name and whether it is installed; run `python3 araclar/skill-ekle.py --araclar` (installed state shows).
   2. Read ONLY official documentation: project skill folders, instruction files, role file format, symlink, same-name priority, machine-wide folders it writes, version command. Write the date and URLs. Unknown or unclear items go to `belirsizler`; never guess.
   3. Add a record to `yapay-zeka-araclari.json` (copy the closest record; fill every field; `denendi: []`); keep the JSON valid.
   4. Fit check: if the tool reads `.agents/skills` or `.claude/skills` it is already served; if it reads neither, set `destek: "yok"`, tell the user, and stop: a new layout is a code change that needs approval (do not improvise).
   5. Machine-wide folders: fill `kullanici_koku` and `genel_skill_okur` (information). Then, with the user's approval at that time, add the tool's machine-wide skill folder to `notlar/genel-klasor-tabani.json` -> `ek_klasorler` (the ONLY place the watchdog reads; this JSON does not duplicate it); `python3 araclar/genel-bekci.py` must then be clean.
   6. Run `python3 araclar/skill-ekle.py --araclar` (record parses, version read) and later `python3 araclar/dogrula.py` (P8's check).
   7. Dry-run one registered project: `skill-ekle.py <proje> --guncelle --kuru`; the `arac-duzeni` line must name the new tool among those that see or do not see skills. If it is blind, ask the user whether to change the layout.
   8. Real test: open a small test project in the new tool, ask it to list its skills, record the date and result in `denendi`, remove the matching `belirsizler` line only after that test.
   9. Show the diff to the user; commit only with approval; push only when the user asks.
8. Aylık kontrol: `--araclar` meaning of `temiz` / `dikkat` / `sorun`; what to do for each decision line (re-read the official pages for that tool, update the record and `dogrulama_tarihi`, run the real test again if a behaviour changed). State explicitly: the monthly summary (P4 `aylik-ozet.py`) runs this check only in its FULL mode; the fast start-of-session mode (`--hizli`) does not show tool-document staleness, so the full monthly run (or `python3 araclar/skill-ekle.py --araclar` by hand) is the only place it appears.
9. Belirsizlikler ve nasıl denenir: per tool, one sentence how to verify that a project skill is visible (Claude: skill list in the session; Codex: `codex exec "list available skills"` as in rehber/04; others: ask the tool to list skills; record in `denendi`).
10. Bilinen sınırlar: roles only for Claude and Codex (and Cursor through `.claude/agents`); duplicates possible in Cursor/Copilot with `ortak`; no machine-wide installs by the library.

### 3.4 `rehber/01-skill-ekleme-sureci.md` (edit)

- Line 11-12 (`- Eski projelerin ve eski agent'ların, global klasörlerdeki skilleri kullanmaya devam eder.`): replace with `- Genel klasörlerdeki (~/.claude/skills, ~/.agents/skills, ~/.codex/skills) skiller bu araçla yönetilmez. Genel klasörler boşaltıldıktan sonra (rehber/12-genel-klasor-bosaltma.md) eski projeler ve agent'lar yalnız kendi proje klasöründeki skilleri görür; skill gerekiyorsa o projeye bu araçla kurulur.` (the old sentence contradicts the target arrangement, already listed in `DURUM.md` "Sonraya kalan düzeltmeler").
- Process list item 1 (`**İhtiyaç:** ...`): append `ve hangi AI araçlarıyla açılacağı (Claude Code, Codex, Antigravity, Cursor, VS Code Copilot; Windows'ta açılacak mı). Cevaba göre --arac ortak ya da --arac yalniz-claude (rehber/14).`
- Section "Projeyi Codex Desktop'ta / Claude'da açtığında" and "Sadece Claude kullanan proje (`--arac claude`)" are replaced by a section "Araç düzeni: hangi araç neyi görür" holding the two-layout table (section 4 of this spec) and: `--arac ortak|yalniz-claude`; `ikisi` and `claude` are old names that still work; the choice is stored in `kilit.json` -> `araclar` (+ `arac_secimi`); updates keep it; switch back and forth with `--arac`; pointer to `rehber/14` (no `--gemini-md`, Phase 2). Keep the sentence about symlink -> identical copy not counting as hand-edited. Remove the claim "Windows'ta açılıyorsa --arac claude" as the only advice and point to rehber/14 section 5.
- "Proje taşındıysa": add `Başka bilgisayara ya da Windows'a kopyalandıysa rehber/14 bölüm 5.`
- Add near the end (Phase 1 wording, no Phase 2 code names): `Silmeden önce başka skillerin ona bağlı (kardeş yol) olup olmadığına bak: python3 araclar/proje-kullanimi.py --skill <kimlik> ve projedeki skiller/ kilit.json -> kardes alanı. Tek elle değişmiş skill yüzünden güncelleme duruyorsa kullanıcıya göster; kararını al (--zorla ya da skili geri yükle).`
- Add: `Aynı projede iki oturumdan aynı anda skill-ekle çalıştırma (proje kilidi yok); ikinci oturumu açmadan önce ilkinin bittiğine bak.`
- Example 4 ("Sohbetten"): add as the first agent step "Hangi araçlarla açılacağını sorar ve --arac ile kaydeder".

### 3.5 `rehber/04-kontrol-listesi.md` (edit)

- Section A: replace the bullet `**Codex'te de kullanacak mısın?** ...` with `**Hangi araçlar?** Claude Code / Codex / Antigravity / Cursor / VS Code Copilot / Windows? Cevaba göre --arac ortak ya da --arac yalniz-claude; raporda arac-duzeni, arac-gormez ve arac-secimi-yok satırlarını oku (rehber/14). codex-uyum / claude-ozel uyarılarını da oku.`
- Section B table: add rows (code, seviye, meaning, action) for the codes of section 4: `arac-duzeni` BİLGİ, `arac-gormez` BİLGİ, `arac-secimi-yok` BİLGİ, `arac-cift-okuma` BİLGİ, `arac-symlink` BİLGİ, `arac-rolsuz` BİLGİ, `arac-mutlak-yol` BİLGİ, `arac-belge-yok` BİLGİ, `arac-karisik` HATA (not `HATA*`). Phase 2 codes (`gemini-md`, `gemini-md-duzen`, `kardes-bagimli`, `bos-rol`, `haric-atlandi`, `haric-yok`) are NOT added to rehber/04 until built. (Rows must be written after the code exists; table format `| \`kod\` | ... |` so `dogrula.py:192` finds them.)
- Section B, rows `ayni-klasor` and `elle-degistirilmis` stay unchanged in Phase 1.
- Section C: replace the last bullet (`.skill-kutuphanesi/yedek/ için .gitignore önerilir`) with `araç ilk yedekte .skill-kutuphanesi/.gitignore dosyasını kendisi yazar (yedek/); .agents/, .claude/, .codex/, .skill-kutuphanesi/kilit.json commit edilebilir`. Add `- [ ] arac-duzeni satırı doğru araçları listeledi mi; arac-secimi-yok çıkıyorsa kullanıcıya soruldu ve --arac ile kaydedildi` and `- [ ] Antigravity / Cursor / Copilot'ta gerçek deneme yapıldıysa yapay-zeka-araclari.json -> denendi'ye yazıldı`.
- Section D: add rule 6 `Hangi araçlarla açılacağını sormadan ilk kurulum yapma (arac-secimi-yok).`

### 3.6 `promptlar/01..05, 09, 11` (edits)

- `01`: in the `kopyala` block insert a new first step `0. ARAÇ SORUSU (bekle): "Bu proje hangi araçlarla açılacak? Claude Code, Codex, Antigravity, Cursor, VS Code Copilot; Windows'ta da açılacak mı?" Cevabıma göre: Codex ya da Antigravity varsa --arac ortak; yalnız Claude (Cursor/Copilot olabilir) --arac yalniz-claude; Windows'ta açılacaksa yalniz-claude (Codex/Antigravity görmez, nedeni rehber/14 bölüm 5); bilmiyorsam ortak. Seçimi 2. ve 3. adımdaki komutlara --arac <düzen> olarak ekle ve raporda arac-duzeni, arac-gormez ve arac-secimi-yok satırlarını bana ayrıca göster.` Update "**Beklenen sonuç**" to say the `.agents/skills` + `.claude/skills` + role files apply to `ortak`; for `yalniz-claude` only `.claude/skills`, `.claude/agents`, `CLAUDE.md`. Step 5 reminder: `Claude/Codex/Antigravity/Cursor oturumunu yeniden aç`.
- `02`, `03`: add one line before the numbered steps: `Projede araç düzeni kayıtlıysa (--durum satırı "düzen: ..."), ona uy; "arac-secimi-yok" çıkıyorsa bana hangi araçlarla açılacağını sor ve --arac ile kaydet.`; in `02` step 3 and `03` step 4 the command is unchanged.
- `04`: section 4a: replace `AGENTS.md dosyasına` with `araç düzenine göre: ortak düzende AGENTS.md ve CLAUDE.md dosyalarının ikisine aynı metni (Claude CLAUDE.md'yi okur, Codex ve Antigravity AGENTS.md'yi okur); yalniz-claude düzende CLAUDE.md dosyasına`, still "skill-kutuphanesi işaretli bloğun DIŞINA". Section 4b first line: `AGENTS.md'deki amaca göre` -> `proje talimat dosyasındaki amaca göre`. Add note: roles (`.claude/agents`, `.codex/agents`) exist only for Claude and Codex; in Antigravity, Cursor, Copilot every agent sees all project skills.
- `05`: step 1 of 5a unchanged; add 5d `Araç düzenini değiştir`: `skill-ekle.py "$PWD" --arac <ortak|yalniz-claude> --kuru` (shows what changes; content unchanged), approval, `--evet`, `--dogrula`. In 5a step 4 add: `silmek istediğin skill'e başka bir skill bağlı mı (kardeş yol) kullanıcıya göster; elle değişmiş tek skill güncellemeyi durduruyorsa kullanıcıya göster ve kararını al.` (no Phase 2 flag names).
- `09`: add branch: `- proje başka bilgisayara / Windows'a kopyalandı -> rehber/14 bölüm 5; kütüphanenin olduğu Mac'te önce --dogrula, sonra --yenile; Windows'ta skill-ekle çalıştırma.` and `Aynı projede başka bir oturum skill-ekle çalıştırıyorsa onun bitmesini bekle (proje kilidi yok, bunu sen kontrol et).`
- `11`: ADIM 1 summary gets a 7th line `hangi araçlarla açılıyor (Claude Code / Codex / Antigravity / Cursor / VS Code Copilot / Windows)`; ADIM 8 command becomes `... [--arac <ortak|yalniz-claude>] --kuru`; ADIM 9 item 1 `Aynı komut --evet ile`. Rule 2 text `...kopyalar, .claude/skills altına bağlar` gets `(düzene göre; yalniz-claude'da yalnız .claude/skills)`. Every flag mentioned must already exist in code (`--arac`); `--haric` is Phase 2 and must not appear.

### 3.7 `promptlar/15-yeni-yapay-zeka-araci.md` (new, about 40 lines)

Format as the other prompts (title, "Ne zaman", `kopyala` block, "Beklenen sonuç"). Context: run in a library session (`~/Documents/SkillKutuphanesi`). Block content: asks `[ARAÇ ADI]`; tells the agent to read `rehber/14-yapay-zeka-araclari.md` bölüm 7 and follow steps 1-9 without skipping; use only official documentation; do not guess; show the new record as a diff before writing; run `skill-ekle.py --araclar`; run `skill-ekle.py <registered project> --guncelle --kuru` for one project; do not change `CLAUDE.md`, `AGENTS.md`, `README.md`, `dogrula.py`, `test.py` (those belong to the integrator); do not write to machine-wide skill folders, shell files or settings; commit only after approval, never push. Expected result: a new record, `--araclar` shows it, a short report with open uncertainties.

### 3.8 `araclar/testler/test_p1-arac-destegi.py` (new, about 450 lines)

See section 5.

### 3.9 `.skill-kutuphanesi/.gitignore` format

Plain text, one pattern per line: `yedek/` (Phase 2 adds `.islem-kilidi`).

### 3.10 `[AŞAMA 2]` Lock file format `.islem-kilidi`

`{"pid": 4242, "baslangic": "2026-11-12T10:15:00", "makine": "MacBook-Pro.local", "islem": "skill-ekle"}`.

### 3.11 CLI summary (new/changed flags of `skill-ekle.py`)

| flag | new/old | behaviour |
|---|---|---|
| `--arac {claude,ikisi,ortak,yalniz-claude}` | old + 2 aliases | records layout in `araclar`, sets `arac_secimi: secildi` |
| `[AŞAMA 2]` `--gemini-md {ac,kapat}` | not built | sets lock `gemini_md`; `ac` refused with `yalniz-claude` (exit 2) |
| `[AŞAMA 2]` `--haric SKILL...` | not built | `--guncelle` skips listed skills (BİLGİ), warns on unknown names |
| `--araclar` | new | read-only table of AI tools from the JSON; exit 0 |
| `--ozet-json` | new | with `--araclar`: one JSON object on stdout |
| `--siki` | new | with `--araclar`: exit 1 only when `durum == "sorun"` |
Exit codes unchanged: 0 ok, 1 doğrulama sorunu, 2 işlem yapılmadı (onay yok, HATA, kuru; Phase 2: BEKLE).

### 3.12 M2: `ortak-kopya` layout (implement ONLY after Q1 is approved)

Why it is optional: it closes "Windows project, Codex and Antigravity blind" but touches `kurulum_eksik`, `dogrula` and `kur`, and the Windows default is the user's decision (user question 3 in `ozet-bolum2-4.md`).
- `ARACLAR["ortak-kopya"] = ["claude","codex"]`, `DUZEN_KLASORLERI["ortak-kopya"]` = same as `ortak`, `DUZEN_TALIMAT` same. New lock field `baglanti: "kopya"` (absent = symlink). `duzen_adi` returns `ortak-kopya` when `baglanti == "kopya"`; `duzen_uygula` sets/removes it.
- `kur()` (`:572`): new keyword-only `kopya=False`. In the non-variant branch of the `codex=True` path, instead of `os.symlink` call `hazirla(KOK / var.get("codex", s["yol"]), claude_hedef, s, ad, kardes, ".claude/skills", skiller)` when `kopya` (`hazirla` removes any existing symlink with `sil_yol`, `:566`). Callers `ekle()` (`:1206`) and `guncelle()` (`:1331`) pass `kopya=(kilit.get("baglanti") == "kopya")`.
- `kurulum_eksik` (`:1155-1163`): in the `codex_var` branch the last expression `(not varyant and not c.is_symlink())` becomes `(not varyant and (c.is_symlink() == (kilit.get("baglanti") == "kopya")))` i.e. expect a real folder in `kopya` mode, a symlink otherwise.
- `dogrula` (`:1371-1376`): in `kopya` mode a symlink in `.claude/skills` is a sorun (`.claude/skills bağlantısı olmamalı, gerçek kopya olmalı`) and the "beklenmeyen gerçek klasör" sorun is skipped. `elle_degismis` needs no change: the lock stores a hash for both copies (`kurulu_hash`, `:219-223`) and the existing tolerance (`:233-235`) covers switching from the symlink layout.
- Switching `ortak` <-> `ortak-kopya` and from `yalniz-claude` uses `arac_degistir` -> `guncelle(yapi_degisti=True)`; every skill is re-installed through `kurulum_eksik`.
- Report: replace line 5 `arac-symlink` by `arac-kopya` BİLGİ: `.claude/skills ve .agents/skills ayrı gerçek kopyalar (symlink yok); Windows ve symlink'siz git için güvenli, disk iki kat. İkisi de aynı anda güncellenir; elle birine dokunma.`
- Cost to record: two copies per skill; hand-edit of either is caught by `kurulu_hash`.

---

## 4 User-facing texts (exact Turkish)

Report lines (`[BİLGİ] kod: mesaj`):
- `arac-duzeni` (ortak): `Araç düzeni: ortak (seçim: {varsayılan|seçildi}). Klasörler: .agents/skills (gerçek kopya) + .claude/skills (bağ). Skilleri görenler: {Claude Code, Codex, Antigravity, Cursor, VS Code Copilot}. Görmeyenler: yok. Talimat bloğu: CLAUDE.md, AGENTS.md.` For every record with `destek == "istege-bagli"` and `kurulu` false, append ` Kurulu olmayan: {ad_kisa listesi} (.agents/skills'i okur; GEMINI.md yazılmıyor).` (e.g. `Kurulu olmayan: Gemini CLI, Copilot CLI (...)`.)
- `arac-duzeni` (yalniz-claude): `Araç düzeni: yalniz-claude (seçim: seçildi). Klasör: .claude/skills (gerçek kopya). Skilleri görenler: Claude Code, Cursor, VS Code Copilot. Görmeyenler: Codex, Antigravity. Talimat bloğu: CLAUDE.md.`
- `arac-gormez`: `Bu düzende {Codex, Antigravity} bu projedeki skilleri GÖRMEZ (okudukları klasör: .agents/skills). Onları da kullanacaksan: --arac ortak.`
- `arac-secimi-yok`: `Bu proje için araç düzeni hiç seçilmedi; varsayılan 'ortak' uygulanıyor. Projenin hangi araçlarla açılacağını (Claude Code, Codex, Antigravity, Cursor, VS Code Copilot, Windows) kullanıcıya sor, sonra --arac ortak ya da --arac yalniz-claude ile kaydet (rehber/14).`
- `arac-cift-okuma`: `{Cursor, VS Code Copilot} hem .agents/skills hem .claude/skills klasörünü okur; aynı skill iki kez listelenebilir (belgede yok, denenmedi). Görürsen kullanıcıya bildir (rehber/14 bölüm 9).`
- `arac-symlink`: `.claude/skills altındaki bağlar symlink'tir; Windows'ta ve core.symlinks kapalı git'te düz metin dosyasına döner, Claude skilleri göremez. Proje Windows'ta açılacaksa --arac yalniz-claude kullan (Codex ve Antigravity görmez; rehber/14 bölüm 5).`
- `arac-rolsuz`: `Rol dosyaları yalnız Claude (.claude/agents) ve Codex (.codex/agents) için üretilir. Cursor .claude/agents dosyalarını da okur (belge). {Antigravity, VS Code Copilot} için rol dosyası üretilmez: orada her ajan projedeki tüm skilleri görür.` (names = installed tools with `rol_dosyasi.uretilir` false that are not read through `.claude/agents` per record `neden`; implementation: list `ad_kisa` of installed records with `uretilir == false` and `anahtar != "cursor"`.)
- `arac-mutlak-yol`: `.codex/agents/*.toml içinde bu bilgisayarın mutlak yolları var; proje başka klasöre ya da bilgisayara taşınırsa Codex rol dışı skilleri kapatamaz. Kütüphanenin olduğu bilgisayarda --yenile çalıştır.`
- `arac-belge-yok`: `yapay-zeka-araclari.json okunamadı; hangi aracın skilleri göreceği satırları atlandı (kurulum etkilenmez).`
- `[AŞAMA 2]` `gemini-md`: `GEMINI.md bloğu açık: Antigravity hem AGENTS.md hem GEMINI.md dosyasını okuduğu için aynı blok iki kez yüklenir. Yalnız Gemini CLI kullanılıyorsa gerekir; kapatmak için --gemini-md kapat.`
- `arac-karisik` (HATA): `--arac {yeni} verildi ama projede {n} skill {eski} düzeninde kurulu ({adlar}). Önce yalnız --arac {yeni} --kuru, sonra --arac {yeni} --evet çalıştır; ardından skill ekle.`
- `[AŞAMA 2]` `gemini-md-duzen` (HATA, printed by `main`, exit 2): `GEMINI.md bloğu yalniz-claude düzeninde yazılmaz (bu düzende .agents/skills yok). Önce --arac ortak.`
- `[AŞAMA 2]` `kardes-bagimli` (UYARI): `{b} skill'i {a} skill'ine bağlı (kardeş yol); {a} kaldırılırsa {b} içindeki bağlantılar kırılır. İkisini birlikte kaldır ya da {a}'yı tut.`
- `[AŞAMA 2]` `bos-rol` (BİLGİ): `rol {r} son skilini kaybediyor; rolün agent dosyaları (üretilmiş olanlar) silinecek.`
- `[AŞAMA 2]` `haric-atlandi` (BİLGİ): `{ad}: --haric ile atlandı; kurulu kopya olduğu gibi kalıyor.`
- `[AŞAMA 2]` `haric-yok` (UYARI): `--haric {ad}: projede böyle bir kütüphane skill'i yok.`
Messages and stdout lines:
- `[AŞAMA 2]` `BEKLE: bu projede başka bir skill-ekle işlemi sürüyor (pid {pid}, başlangıç {baslangic}, {islem}). Bitmesini bekle. Süreç yoksa ve takılı kaldıysa .skill-kutuphanesi/.islem-kilidi dosyasını sil (6 saatten eski kilit zaten yok sayılır).`
- `[kuru] Hiçbir şey değiştirilmedi. (yapılacak: {yenile|geri-al|blok})`
- Windows guard: see 3.1.11.
- `--araclar` human table header: `Araç | Kurulu | Okuduğu proje skill klasörleri | Kayıtlı sürüm | Bulunan sürüm | Doğrulama`.

---

## 5 Tests (`araclar/testler/test_p1-arac-destegi.py`)

Mechanics (D5): runnable alone; temp directories and fake data only; never touches `~/.claude`, `~/.codex`, `~/.agents`, `~/.gemini`, `~/.cursor`, `~/.copilot`, `~/.openmontage`; never runs the library `__main__` (`proje_raporunu_yenile` git-commits inside the library). Load the module with `importlib.util.spec_from_file_location("se_p1", KOK / "araclar" / "skill-ekle.py")` (the file name has a hyphen; same as `test.py:533`). Monkeypatch before use: `se.canli_global = lambda s: {}`, `se.hesap_skilleri = lambda: {}`, `se.guncelleme_suruyor = lambda: None`, `se.registry = lambda: [fake skills]`, `se.ARAC_JSON = <temp file>`. Fake skills are built like `test.py:558-600` (folder under a temp `arsiv/`, record with `id, ad, klasor_adi, kaynak_yol, repo, yol, klasor_hash, commit`). Drive `se.main()` in-process by setting `sys.argv` and catching `SystemExit`. Print each case `✅/❌ name`; last line `N/N test geçti`; exit 0 if all pass else 1. Final cleanup removes temp dirs.

Cases (each is one `test(...)`). Phase 1 file contains groups A, B, C, F (reduced), H, I; groups marked `[AŞAMA 2]` (D, E, G) and the Phase 2 parts named in the cases are NOT written until built. Case numbers are kept stable (gaps are fine). Fake JSON in these tests uses the final keys (`claude-code, codex, antigravity, cursor, vscode-copilot`, plus `gemini-cli`/`copilot-cli` records with `kurulu: false`); `arac_satirlari` assertions look up tools by `anahtar`, so a record keyed `copilot` must fail the test.
A names and lock
1. `ARACLAR["ortak"] == ARACLAR["ikisi"]` and `ARACLAR["yalniz-claude"] == ARACLAR["claude"]`; `duzen_adi` returns `ortak` / `yalniz-claude` for the four spellings.
2. `python3 skill-ekle.py --help` (subprocess) mentions `yalniz-claude`, `--araclar`, `--ozet-json`, `--siki`, and (Phase 1) does NOT yet mention `--gemini-md` or `--haric` (so docs cannot drift ahead of code).
3. `kilit_oku` on a lock without `araclar`: `codex_var` true, `arac_secimi == "varsayilan"`; with `araclar: ["claude"]`: `"secildi"`; reading never writes (file mtime unchanged).
4. First `kilit_yaz` of a default lock writes `araclar == ["claude","codex"]` and `arac_secimi == "varsayilan"`; a lock that already has `["claude"]` keeps it.
5. `duzen_uygula(kilit, "ikisi")` equals `duzen_uygula(kilit, "ortak")` (same lists, `secildi`).
B report lines (`arac_satirlari` with a fake JSON; all assertions on `rapor.satirlar`)
6. `ortak`: `arac-duzeni` present listing all five installed tools as seeing, no `arac-gormez`.
7. `yalniz-claude`: `arac-gormez` names Codex and Antigravity but not Cursor or VS Code Copilot.
8. Default choice and `secim=None`: `arac-secimi-yok` present; after `duzen_uygula`: absent.
9. Every line emitted in cases 6-8 has seviye `BİLGİ` (no UYARI, no HATA).
10. Missing JSON and broken JSON: exactly one line `arac-belge-yok`, no exception.
11. `arac-cift-okuma` only for `ortak`, names Cursor and VS Code Copilot; absent for `yalniz-claude`.
12. `arac-rolsuz` and `arac-mutlak-yol` appear only when `kilit["roller"]` is non-empty (and the latter only for `ortak`).
13. `arac-symlink` appears only for `ortak` when the project has `.git`.
14. For every emitted message `m.partition(": ")[0]` contains a space (so `Rapor.gruplu` cannot mangle it).
15. `durum()` output keeps `Claude + Codex` / `sadece Claude` and shows the layout name.
C layout switching and guard
16. `arac_degistir` ortak -> yalniz-claude -> ortak on a synthetic project: `.agents` removed then restored, `--dogrula` clean (sorun list empty) each time; `araclar` persisted.
17. `ekle()` with `--arac yalniz-claude` on a project with two other skills from `ortak`: HATA `arac-karisik`, nothing written; with `--zorla` passes the HATA stage.
D `[AŞAMA 2]` GEMINI.md
18. `gemini_md_ayarla` refuses `ac` for `yalniz-claude` (returns text containing `gemini-md-duzen`); accepts for `ortak`.
19. With `gemini_md` true and a user GEMINI.md with own text: block appended, user text intact, backup folder contains GEMINI.md; `dogrula` clean.
20. `kapat`: block removed, user text intact; if the file held only the block, it is deleted.
21. `dogrula` reports a missing block when on, and a leftover block when off.
22. A user's own GEMINI.md without our marker, flag off: `yedekle` does not list it in `hedefler`; `geri_al` of an older backup leaves it untouched.
E `[AŞAMA 2]` project lock
23. A lock written by the current pid (live) makes `proje_islem_kilidi` exit with code 2 and the BEKLE text; the lock file content is untouched.
24. A lock with a dead pid (use the pid of a finished child process) is stale: replaced, then removed on exit.
25. A lock older than 6 h with a live pid is stale.
26. Lock released after an exception inside the `with`; if the meta folder was created by the lock and is empty it is removed; if it pre-existed it stays.
27. `main()` with `--yenile --kuru` and `--blok kisa --kuru` and `--geri-al --kuru` on a fresh temp project: exit 0, text `[kuru]`, project tree identical (no `.skill-kutuphanesi`, no `.gitignore`).
28. With the lock held by another process (fake file), `main()` `--skill X --evet` exits 2 and the tree is unchanged; `--durum` and `--dogrula` still run.
F backup `.gitignore`
29. First `yedekle` creates `.skill-kutuphanesi/.gitignore` with exactly `yedek/`; a second backup does not change it.
30. Existing user `.gitignore` without `yedek`: `yedek/` appended, user lines and order kept; already containing `yedek` or `yedek/`: file byte-identical.
31. `.gitignore` is never part of `hedefler`; a `--kuru` run creates none.
G `[AŞAMA 2]` kaldir / guncelle
32. `kaldir` of skill A when B's `kardes` maps to A: UYARI `kardes-bagimli` (and DURDU without `--evet` non-interactively); `--kaldir hepsi`: none.
33. `kaldir` removes a role whose last skill went away (lock `roller`, generated `.claude/agents/<rol>.md` and `.toml` removed) and keeps a role that still has a skill; a user-written agent file of the same name is not deleted.
34. `guncelle` with one hand-edited skill and one outdated skill: without `--haric` HATA `elle-degistirilmis` and nothing updated (old behaviour); with `--haric <edited>` the other updates and `haric-atlandi` is reported; unknown name gives `haric-yok`.
H protection and blocks
35. `arac_korunan_yollar` with a fake JSON returns the expanded roots; `main()` refuses a project located under such a root (fake root inside temp) with the `Güvenlik` text; with no JSON the list is empty and behaviour equals today.
36. Both `tam` and `kisa` blocks contain `Kütüphane: ~/Documents/SkillKutuphanesi` and `Kütüphanesiz bilgisayarda` (and the command path `skill-ekle.py`); blocks keep the user text outside the markers; `CLAUDE.md` and `AGENTS.md` blocks are identical.
37. Platform guard: with `os.name` monkeypatched to `"nt"`, `main()` exits with the Windows text before touching anything.
I `--araclar`
38. Fake JSON with `komut` entries that print fixed versions (`[sys.executable, "-c", "print('1.2.3')"]`) and a `plist` entry written with `plistlib` in a temp file: `durum == "temiz"`, exit 0.
39. Version differs: `durum == "dikkat"`, the `karar_bekleyen` line has both versions.
40. `dogrulama_tarihi` 46 days old (pass `simdi`): `dikkat`; 44 days: `temiz`.
41. Record `kurulu: false` but entry found: `dikkat` with the "artık kurulu" decision line; record `kurulu: true` but not found: `dikkat`.
42. Broken JSON: `sorun`, exit 0 without `--siki`, exit 1 with `--siki`.
43. `--ozet-json`: stdout is exactly one line that parses as JSON with keys `arac`, `durum`, `satirlar`, `karar_bekleyen` and `arac == "arac-belgeleri"`; nothing else on stdout (checked by running `araclar_raporu` with captured stdout).
44. The real library file `yapay-zeka-araclari.json` (read only): parses, 7 records with the keys `anahtar, ad, ad_kisa, kurulu, destek, surumler, proje_skill_okur, proje_talimat_okur, rol_dosyasi, kullanici_koku, dogrulama_tarihi, belirsizler, denendi`; `anahtar` values are exactly `claude-code, codex, antigravity, cursor, vscode-copilot, gemini-cli, copilot-cli`; top level is `{surum, araclar:[...]}` with `araclar` a list; no record has `makine_geneli_yazar`; every `proje_skill_okur` entry is a relative path; no value looks like a key or token (no 20+ character mixed alphanumeric strings without spaces except URLs).
J M2 only (add if implemented): 45 `ortak-kopya` install: `.claude/skills/<ad>` is a real folder, `dogrula` clean, `kurulum_eksik` false; 46 switching to `ortak` makes it a symlink again and `elle_degismis` stays false; 47 a hand-edited copy in `.claude/skills` is caught; 48 `arac-kopya` line present and `arac-symlink` absent.

---

## 6 Hand-off requests to other packages

To P8 (applies them; no other package edits these files):
1. `CLAUDE.md` and `AGENTS.md`, "Skill ekleme akışı" step 1, replace with: `1. İhtiyacı netleştir: proje yolu, proje tipi, teknoloji, agent rolleri ve hangi AI araçlarıyla açılacağı (Claude Code / Codex / Antigravity / Cursor / VS Code Copilot; Windows'ta açılacak mı). Cevaba göre --arac ortak ya da --arac yalniz-claude ver; rapordaki arac-duzeni, arac-gormez, arac-secimi-yok satırlarını kullanıcıya göster (rehber/14-yapay-zeka-araclari.md). Bilinmiyorsa sor.` Add to "Bakım isteklerinde": `- Yeni AI aracı: rehber/14 bölüm 7 ve promptlar/15; aylık araç belgesi kontrolü: python3 araclar/skill-ekle.py --araclar.` Keep the two files byte-identical.
2. `promptlar/README.md`: add the row `| 15 | [15-yeni-yapay-zeka-araci.md](15-yeni-yapay-zeka-araci.md) | Kütüphaneye yeni bir yapay zeka aracı (IDE ya da CLI) eklemek, belgelerini doğrulayıp kaydetmek |`.
3. `README.md`: one line pointing to `rehber/14-yapay-zeka-araclari.md` and `yapay-zeka-araclari.json`.
4. `araclar/dogrula.py`: (a) HATA if `yapay-zeka-araclari.json` is missing, invalid JSON, or a record lacks any of `anahtar, ad, kurulu, proje_skill_okur, dogrulama_tarihi, surumler`; (b) HATA if `rehber/14-yapay-zeka-araclari.md` or `promptlar/15-yeni-yapay-zeka-araci.md` is missing; (c) UYARI (not HATA) when the JSON's oldest `dogrulama_tarihi` is older than 45 days (the monthly tool also reports it; this keeps `dogrula.py` honest). Existing prompt 11 / rehber/04 checks need no change.
5. `araclar/test.py`: the section that runs every file in `araclar/testler/` as a subprocess already covers `test_p1-arac-destegi.py`; no extra line from P1.
6. `araclar/duman-testi.py` (optional): add `python3 araclar/skill-ekle.py --araclar --ozet-json` as a smoke step (must print valid JSON, exit 0).
7. SCHEMA (answers P8's hand-off P1-A and its E4 check; P8 withdraws its own field-name request): `yapay-zeka-araclari.json` is `{"surum": 1, "araclar": [record, ...]}`, `araclar` is a LIST of records, each with the string field `anahtar`. The five required values are exactly `claude-code`, `codex`, `antigravity`, `cursor`, `vscode-copilot` (the Copilot record is `vscode-copilot`, never `copilot`); optional records `gemini-cli` and `copilot-cli` (`kurulu: false`). Field names are P1's schema and stay: `dogrulama_tarihi` (not `son_dogrulama`), `proje_skill_okur` (not `proje_skill_klasoru`), `proje_talimat_okur` (not `talimat_dosyasi`), `kurulu`, `destek`. P8's E4 must therefore read `{k["anahtar"]: k for k in d["araclar"]}` (not `d.get("araclar", d)` as a dict), check the five keys, and use `dogrulama_tarihi` for its staleness UYARI; the `{araclar: {...}}`/flat-dict tolerance can be dropped. P1's own `--araclar` already reports staleness at 45 days; P8's 120-day UYARI may stay as a coarser backstop.
8. `rehber/01` line 12 hit (P8 check G, hand-off P1-B) is fixed by P1 (3.4); P8's `BASLA.md` should state in its tools section that `skill-ekle.py` does not run on Windows (the tool refuses; see rehber/14 section 5) and that the monthly tool-document check is in the full monthly run only.
9. `araclar/ortak.py`: no change requested. (`GLOBAL_KLASORLER` stays; extra protected roots come from the JSON at runtime. If P2 decides to extend `GLOBAL_KLASORLER` for `~/.gemini/skills`, `~/.cursor/skills`, `~/.copilot/skills`, that is P2's request to P8; this package does not depend on it.)

To P2 (watchdog `genel-bekci.py`): P2 does not read `yapay-zeka-araclari.json` now (P2 deferred it) and this file has no `makine_geneli_yazar` field; the machine-wide folders that tools write live ONLY in P2's `notlar/genel-klasor-tabani.json` -> `ek_klasorler`. Non-binding candidates, taken from the tool research, for P2 to judge when it fills `ek_klasorler`: `~/.gemini/config/skills`, `~/.gemini/antigravity/skills`, `~/.gemini/antigravity-cli/skills`, `~/.gemini/skills` (Antigravity/Gemini), `~/.cursor/skills` and `~/.cursor/skills-cursor` (the latter is Cursor's own built-in, vendor-owned), `~/.copilot/skills`. Allowances known from research: Claude app writes `~/.claude/skills/synced`; Codex writes `~/.codex/skills/.system`. rehber/14 section 7 step 5 tells the library session to add a new tool's folder to `ek_klasorler` with the user's approval; P2 needs no change for that.
To P4 (`aylik-ozet.py`): run `python3 araclar/skill-ekle.py --araclar --ozet-json` as a subprocess, expect exit 0, merge `satirlar` and `karar_bekleyen`; `durum` `dikkat` means the tool documentation or version changed (decision lines tell what). Do not call without `--ozet-json`.
To P3 (`yedek-denetim.py`): project backups (`<proje>/.skill-kutuphanesi/yedek/`) are now git-ignored by the tool itself; the backup inventory need not warn about them. (Phase 2 only: `GEMINI.md` would be included in a backup only when it contains our marker or `gemini_md` is on.)
To P5 (project tracking): second half of critic scenario 9, "an AI tool added its own skill to a project folder": `proje-kullanimi.py --saglik` should list directories under `.agents/skills`, `.claude/skills` that are not in `kilit.json` (and not in `.skill-kutuphanesi/elle-kurulan.json`). `skill-ekle.py --dogrula` does not do this. Also: `--dogrula` already reports `proje taşınmış`; the `arac_secimi` lock field lets P5 report projects with `varsayilan` choice ("araç seçimi yapılmadı").

---

## 7 Needs the user's approval

Q1 (Windows, before M2): user question 3 of `ozet-bolum2-4.md` is still open. Question to ask at implementation time: `Windows'ta da açılacak projelerde Codex ve Antigravity'nin skilleri görmesini ister misin? Evet ise ortak-kopya düzeni (her skill iki gerçek kopya, symlink yok) eklenir; hayır ise Windows projeleri yalniz-claude kalır (Codex ve Antigravity göremez).` No default is chosen by this design. M2 is built only on "evet".
Q2 (GEMINI.md, Phase 2): D1 decided: off by default; review decision: not built now. Asked only if Gemini CLI gets installed (then `--araclar` prints a decision line because the record says `kurulu: false` but the version is found) or the user asks for it.
Q3 (block text churn): both block variants get the library-path sentence `BLOK_KUTUPHANE` (3.1.15; the `tam` block also gains the Windows sentence it lacked). Existing projects change at their next write. Ask before implementing: `Projelerin CLAUDE.md / AGENTS.md bloğuna "Kütüphane: ~/Documents/SkillKutuphanesi; skill ekleme/silme yalnız kütüphane oturumunda; kütüphanesiz bilgisayarda (ör. Windows) yapma" cümlesi eklensin mi? (Projelerde sonraki yazımda blok bir iki cümle uzar.)` If refused, drop 3.1.15 and test 36.
Q4: The first write on a project whose lock lacks `araclar` flips `—` to `claude, codex` in `notlar/proje-kullanimi.md`, which is auto-committed by the existing mechanism. Mention in the implementation approval; no separate decision.
Real changes that each need the user's approval at that time (this package only delivers the tool and procedures): switching any registered project's layout (for example Etsy-Arif from `yalniz-claude` to `ortak`), adding a new tool's machine-wide folder to P2's `ek_klasorler`, committing the library changes of this package, and pushing (only when the user asks).
This package itself changes no machine-wide folder, shell file, settings file, scheduled task or project folder (D7). `skill-ekle.py` writes into a project only when run with `--evet` by an approved flow; the new things it may write there are `.skill-kutuphanesi/.gitignore` (one line `yedek/`), the new lock field `arac_secimi` (and `araclar` on first write), and the longer block sentence. (Phase 2 would add `GEMINI.md` and `.islem-kilidi`.)

---

## 8 Deferred and why

- Role files for Antigravity (`.agents/agents/*.md`), Cursor (`.cursor/agents/`), Copilot (`.github/agents/*.agent.md`) and Gemini CLI: NOT produced. Reasons: Cursor already reads `.claude/agents` and `.codex/agents` (documented); Antigravity's frontmatter fields for skill preloading, and the IDE's real folder, are not verified; Copilot's `.claude/agents` handling is undocumented and its format is separate; Gemini CLI is not installed. A wrong guess would put misleading files into every project. Trigger to revisit: the user says they really use roles in that tool; then verify the format with a real test and add a layout option (new approval). Recorded in `rol_dosyasi.neden` and in `arac-rolsuz`.
- Codex `[[skills.config]] name = ...` instead of absolute `path` (would make `.codex/agents/*.toml` portable across machines): the semantics of `name` (global or project scope) are unverified. Recorded in the Codex `belirsizler`; until tested the `arac-mutlak-yol` line and `--yenile` are the answer.
- A dedicated CRLF warning code and automatic `.gitattributes`: only recommended in rehber/14 section 5; the tool does not write into the project's git settings.
- `--kaldir hepsi` "remove from tracking" automation: P5 owns project tracking (`projeler.json`); the tool only prints a pointer (3.1.12).
- Zip warning for projects without git: outside the scope of the installer; no mechanism yet.
- Real tests of Antigravity, Cursor and Copilot actually listing a project skill: cannot be done by a design or by unattended tests; `denendi` stays empty and `belirsizler` stays until the user (or a supervised session) runs them; rehber/14 section 9 describes how.
- A forced "ask the user which tools" prompt inside the tool (UYARI would break non-interactive runs and the duman test): replaced by the BİLGİ line `arac-secimi-yok` plus the written flow (CLAUDE.md step 1 via P8, prompts 01/03/11). Weakness: an agent that ignores the written flow can still install with the default; the lock keeps `arac_secimi: varsayilan` so the omission stays visible (and P5 can list such projects).
- Windows support of `skill-ekle.py` itself (copy instead of link, `kill -0`): not planned; the tool refuses to run on Windows (3.1.11).
- Changing `GLOBAL_KLASORLER` in `ortak.py` (P2/P8 decision).
- Phase 2 items (reviewer: small gain, new code paths, new lock fields, test load; D1 says Gemini CLI is not installed): `GEMINI.md` block and `--gemini-md` (3.1.6), project lock `.islem-kilidi` (3.1.7, replaced by a written warning in rehber/01 and promptlar/09), `kaldir()` sibling warning and empty-role cleanup (3.1.12), `--haric` (3.1.13), M2 `ortak-kopya` (3.12, also awaits Q1). Trigger to build: the user hits the problem for real (two sessions collide, a blocked update, Gemini CLI installed, Windows project needing Codex). Each is fully designed above, so a later session builds it without redesign.
- Library path in project blocks is built (3.1.15) but the `--yenile` rewrite of existing projects' blocks happens only at their next write, never in bulk by this package.

---

## 9 Risks and how the implementer verifies nothing existing broke

Risks:
- R1 `kilit_yaz` now writes `araclar` on first write (same effective value). Visible only in `notlar/proje-kullanimi.md` (see Q4) and lock diffs. Verify with test 3-4 and `python3 araclar/test.py` (`test.py:1195-1237` cover `--arac`).
- R2 `[AŞAMA 2]` `main()` refactor for the project lock: not built, so in Phase 1 `main()` only gains an early `--araclar` branch, the Windows guard and the `--kuru` early return. Verify: every existing branch returns the same codes; `--help` still exits before `registry()`; run the whole `test.py`.
- R3 The `--kuru` fix for `--yenile`/`--blok`/`--geri-al` changes old (buggy) behaviour. Check `grep -n "kuru" araclar/test.py araclar/duman-testi.py` that no test depends on `--yenile --kuru` writing.
- R4 `[AŞAMA 2]` `kaldir` empty-role cleanup: not built now (see 3.1.12). When built: `test.py:1129-1138` and `:1383` use `--kaldir ... --evet`; confirm none asserts a role survives with zero skills.
- R5 `[AŞAMA 2]` New UYARI `kardes-bagimli`: not built now. When built, all existing `--kaldir` calls must pass `--evet` (`test.py:921, 1129, 1134, 1138, 1383`, `duman-testi.py:136`); re-check by grep.
- R6 Block text change (Q3, 3.1.15) vs tests: grep found no test or checker asserting either block's closing sentence (`grep -n "Kütüphanesiz\|değişiklik/güncelleme"` in `test.py`, `duman-testi.py`, `dogrula.py`, `proje-kullanimi.py` returned nothing). Re-run the grep.
- R7 `proje_yapisi_kontrol`/`main` protected list grows: an existing project located under `~/.gemini`, `~/.cursor` or `~/.copilot` would be refused. None of the registered projects is (checked: projects live in `~/Documents`).
- R8 `os.name == "nt"` guard: none on this Mac.
- R9 No concurrency protection in Phase 1 (project lock deferred): two sessions in one project at once can interleave writes; mitigated only by the written warning in rehber/01 and promptlar/09, and by `yedekle()` backups before every change.
- R10 `--araclar` runs external `claude --version`, `codex --version` (read-only, 10 s timeout, output only parsed for a version number). Tests use fakes, never the real commands.
- R11 Doc/flag drift: `dogrula.py:185-196`. Edit documents only after code; run `dogrula.py` at the end (P8's checks included).

Verification steps, in this order:
1. Before any edit: `cd /Users/sabanulukaya/Documents/SkillKutuphanesi && python3 araclar/test.py | tail -3` and `python3 araclar/dogrula.py | tail -5` record baseline.
2. After code (3.1): `python3 araclar/testler/test_p1-arac-destegi.py` (Phase 1 groups A, B, C, F, H, I) and `python3 araclar/test.py` (unchanged result), `python3 -c "import importlib.util,sys; s=importlib.util.spec_from_file_location('x','araclar/skill-ekle.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)"` (module still imports; `skill-calistir.py` depends on it).
3. After docs: `python3 araclar/dogrula.py` (0 hata), `python3 araclar/kapsam-denetimi.py` (0 sorun).
4. `git -C . status --short` shows only the files owned by this package; `git diff --stat` reviewed by the user before commit.
5. Final: `python3 araclar/duman-testi.py` only after the user has committed the dirty tree (it requires a clean tree; see A7).

---

## 10 Acceptance (commands that prove it is done)

From `/Users/sabanulukaya/Documents/SkillKutuphanesi`:
1. `python3 araclar/testler/test_p1-arac-destegi.py` -> last line `N/N test geçti`, exit 0.
2. `python3 araclar/test.py` -> same pass count as the baseline, exit 0.
3. `python3 araclar/skill-ekle.py --help | grep -c -e "yalniz-claude" -e "--araclar" -e "--ozet-json" -e "--siki"` -> 4 or more matching lines, and `... --help | grep -c -e "--gemini-md" -e "--haric"` prints 0 (Phase 2 flags not built).
4. `python3 araclar/skill-ekle.py --araclar` -> table with 7 tools, exit 0; `python3 araclar/skill-ekle.py --araclar --ozet-json | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['arac']=='arac-belgeleri' and d['durum'] in ('temiz','dikkat','sorun'); print(d['durum'])"` prints a status, exit 0; `python3 araclar/skill-ekle.py --araclar --siki; echo $?` prints 0 when the file is valid.
5. Dry run on a throw-away temp project (created with `mktemp -d`, never a real project): `python3 araclar/skill-ekle.py "$T" --skill code-tour --arac ortak --kuru` prints `arac-duzeni`, no `arac-gormez`; `... --arac yalniz-claude --kuru` prints `arac-gormez` naming Codex and Antigravity; both leave `"$T"` empty (`ls -A "$T"` empty).
6. `python3 araclar/skill-ekle.py "$T" --yenile --kuru` prints `[kuru]` and writes nothing; `ls -A "$T"` empty.
7. `python3 araclar/dogrula.py` -> 0 hata (requires P8's JSON check to be present or absent consistently); `python3 araclar/kapsam-denetimi.py` -> 0 sorun.
8. A read-only `python3 -c` one-liner over `yapay-zeka-araclari.json` shows 7 records, each with `dogrulama_tarihi` and non-empty `belirsizler`, and no `denendi` entries (honest: nothing tested yet).
9. `ls rehber/14-yapay-zeka-araclari.md promptlar/15-yeni-yapay-zeka-araci.md araclar/testler/test_p1-arac-destegi.py yapay-zeka-araclari.json` all exist; `grep -n "Eski projelerin ve eski agent" rehber/01-skill-ekleme-sureci.md` returns nothing.
10. `git status --short` lists only P1-owned files (plus whatever was already dirty before); no file under `arsiv/`, no machine-wide folder, no project folder changed.
11. Python one-liner over the JSON: `{k['anahtar'] for k in d['araclar']}` equals `{claude-code, codex, antigravity, cursor, vscode-copilot, gemini-cli, copilot-cli}`; `d['araclar']` is a list; no record has `makine_geneli_yazar`.
12. `grep -c "Kütüphane: ~/Documents/SkillKutuphanesi" araclar/skill-ekle.py` is at least 1 (block sentence present once as a constant); `grep -n "GEMINI.md\|islem-kilidi" araclar/skill-ekle.py` shows nothing that writes either (Phase 2 not built).

---

## 11 Review changes

Mandatory corrections applied:
1. Tool key mismatch. The Copilot record's `anahtar` is now `vscode-copilot` (`ad_kisa` "VS Code Copilot"); optional records `gemini-cli` and `copilot-cli` (both `kurulu: false`, `destek: istege-bagli`; `copilot-cli` record added from `arac-copilot.md`, so 7 records). Schema, examples, report-line lookup (by `anahtar`), tests 6, 7, 44 and acceptance 8 and 11 updated. Section 6 now tells P8: file shape is `{surum, araclar:[record]}` (a list), field names stay `dogrulama_tarihi`, `proje_skill_okur`, `proje_talimat_okur` (plus `kurulu`, `destek`); P8 withdraws its `son_dogrulama`/`proje_skill_klasoru`/`talimat_dosyasi` request and builds its map from `anahtar`.
2. `makine_geneli_yazar` removed from the JSON (field table, record table, example, consumer list, test 44). Machine-wide folder list has one owner: P2's `ek_klasorler`. Conflict between the two mandatory corrections (one said "two places: JSON for info and ek_klasorler", the other said "remove from the JSON") resolved in favour of removal, because two sources of one list is exactly the stated problem; `kullanici_koku` and `genel_skill_okur` stay as information and for the installer's protected-path list. The "To P2" text now says P2 does not read the file and lists non-binding candidate folders. rehber/14 section 7 step 5 now says to add a new tool's machine-wide folder to `notlar/genel-klasor-tabani.json` -> `ek_klasorler` with the user's approval, after which `python3 araclar/genel-bekci.py` must be clean.
3. Implementation order and prerequisite line added at the top (P3 before P1; P6, P8 depend on P1's keys; P4, P8 read P1's `--araclar --ozet-json`).

Optional corrections:
- Split into two phases: ACCEPTED, with one rejection. Phase 1 keeps everything the reviewer listed (arac-* BİLGİ lines, `--araclar` and `arac_secimi`, rehber/14, promptlar/15, `--kuru` honoured by `--yenile`/`--geri-al`/`--blok`, backup `.gitignore` now only `yedek/`, `--araclar` in `salt_okur`). Phase 2 (designed, not built, not documented, not tested): `GEMINI.md`/`--gemini-md`, `--haric`, `kaldir()` sibling UYARI and empty-role cleanup, project lock (replaced by a written warning in rehber/01 and promptlar/09, as the reviewer proposed), M2 `ortak-kopya`. Docs, prompts and `rehber/04` no longer mention Phase 2 flags or codes; test 2 asserts `--help` does not mention them yet. REJECTED for deferral: the `--arac` aliases `ortak`/`yalniz-claude`. They are about eight lines of pure name mapping with no new lock value (the lock still holds `["claude","codex"]` or `["claude"]`), old names keep working, and they are the point of gap A1 (names that say what the choice means); every report line and document depends on them. The `arac-karisik` HATA stays too, because it protects the layout switch which is Phase 1 (`--arac`).
- Kept in Phase 1 unchanged by the review (not named by the reviewer): Windows guard (3.1.11, one line), protected paths from JSON (3.1.10), `--araclar` (3.1.14).

Unowned gaps taken (fit my files):
- Project blocks carry the library path and a "ask for a library session" sentence (3.1.15 `BLOK_KUTUPHANE`, both block variants; Q3 reworded; test 36). Section 1 item 7.
- rehber/14 section 8 states that the tool-document check appears only in the full monthly run, not in the fast start-of-session mode.
- Windows note for BASLA: passed to P8 (section 6 item 8); rehber/14 already has it.
Not taken (not my files or not mine to fix): B2 triage rule (P4/P8), `--kayip-isaretle` (P7/P4), promptlar/10 line 8 (P8), rehber/08 (P8), `kayip_tarihi` for the J-DTurner record (P7), `--ozet-json` writing notlar (P4/P6; P1's `--araclar --ozet-json` writes nothing, stated in 3.1.14), fresh-clone "no stamp" behaviour (P4), shared "accepted" decision list (P4), `kaynaklar.json` KAYIP handling (P7/P4).

Re-checked against code: block text and its path hard-coding (`skill-ekle.py:667-706`, command path `~/Documents/SkillKutuphanesi/araclar/skill-ekle.py` is in both blocks already; the `tam` block really lacks the Windows sentence); `kisa`/`tam` branch structure unchanged by the design. Line numbers in section 3 were taken from the pre-review file and remain valid because no code was edited.
