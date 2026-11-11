# P5 Project tracking: design spec

Package key: `p5-proje-takibi`. Owner of: `araclar/proje-kullanimi.py` (edit), `projeler.json` (edit), `rehber/10-proje-kullanimi.md` (edit), `promptlar/12-proje-kullanimi-ve-etki.md` (edit; real file name), `araclar/testler/test_p5-proje-takibi.py` (new). Generated output (not hand-edited): `notlar/proje-durumu.md` (new, written by the tool).
Closes: B3; critic scenarios 2 (new project, tracking half), 3 (project copied to another Mac/Windows), 9 (second tool adds its own skills to the same project: detection part only). Defers: see section 8 (after review: `--yetim`, `--program`, `--elle-taslak`, `--bilinenleri-yaz`, `--yoksay-kaldir`, `program_kullanimi`; the project side of B7 is therefore deferred).

**Önkoşul (implementation order, binding for all packages):** (0) the uncommitted `programlar/` work is committed first (user approval; the smoke test needs a clean tree); (1) P3 (`.gitignore`, `git-durum`, `yedek-denetim`); (2) P1 (fixes `yapay-zeka-araclari.json` keys, `skill-ekle.py`); (3) P2, P5 and P6 (mutually independent; P5 depends only on the function signatures of `skill-ekle.py` listed in section 6 item 6, which P1 must keep); (4) P7; (5) P4 (needs P3 `.gitignore`, P7 `--atla`, and the `--ozet-json` of P2/P3/P5/P6/P7/P1); (6) P8 last (shared files, parity check, known-warning list); (7) CLAUDE/AGENTS patch B (rule 1 exception) as a separate commit and approval; (8) only then emptying the machine-wide skill folders (rehber/12). P5 itself needs nothing from P2/P3/P4/P6/P7/P8 to run or to pass its own tests.

Conventions: identifiers and user-facing strings are Turkish exactly as they will appear. Paths in `projeler.json` are written in `~/...` form (portable); the tool compares them after `Path.expanduser().resolve()` and Unicode NFC normalisation (macOS may hand back NFD names such as `Danışman`).

---------------------------------------------------------------------------------------------------

## 1 Purpose

Today the project side of the library is blind in five ways (akis-05, akis-01 #3/#4, DURUM.md "Proje taraması" / "Boşluk taraması"):
1. Nobody reports, per registered project, how stale / broken / hand-changed it is. The monthly chain only lists projects touched by changed sources (`arsiv-guncelle.py:84-100`).
2. Projects that have skills but no lock (`Yetisio`, `IsBasvuruClaude`, `Tekfen…`, `CrmProject2`, …) are invisible (`proje-kullanimi.py:36-38` needs `kilit.json`).
3. A registered project that is deleted or moved silently drops out of the report (`proje-kullanimi.py:38` `continue`; ek_projeler path that does not exist is skipped without a word).
4. There is no way to take a project out of tracking, to register a hand-installed project, or to remember that a project was ever tracked.
5. Skills a project wrote itself (`akil-disi-*`), skills installed by hand (`elle-kurulan.json`, written by nobody) and skills whose library source is gone are not told apart.
(Which project uses which program, B7 project side, is deferred in the first version: see section 8.)

P5 (first version, reduced after review) adds read-only reporting modes (`--saglik`, `--tara-kayitsiz`, `--ozet-json`), four dry-run-by-default writers that edit ONLY `projeler.json` (`--ekle`, `--cikar`, `--tasindi`, `--yoksay`), three new `projeler.json` fields (`yoksay`, `bilinen_projeler`, plus the small `kendi_skilleri` and the scan setting `kayitsiz_tarama`), a generated `notlar/proje-durumu.md`, the guide/prompt text for the procedures, and its own test file. Nothing in a project folder or in a machine-wide folder is ever written. The existing report `notlar/proje-kullanimi.md`, the existing flags (`--skill`, `--repo`, `--kontrol`, no flag), the module functions used by other tools (`projeleri_bul`, `oku`, `rapor_metni`, `hesapla`, `guncel_mi`, `rapor_guncelle`, `kullanan_projeler`, `kisa_yol`, constants `AYAR`, `RAPOR`) keep their signatures and their output format.

---------------------------------------------------------------------------------------------------

## 2 Existing behaviour relied on (file:line)

`araclar/proje-kullanimi.py` (all line numbers = current file, 184 lines):
- L21-22: `sys.path.insert(0, araclar)`, imports `KOK, REGISTRY, json_oku, repo_guncel` from `ortak`.
- L24-25: `AYAR = KOK/"projeler.json"`, `RAPOR = KOK/"notlar"/"proje-kullanimi.md"`.
- L28-42 `projeleri_bul(ayar)`: for each `tarama_kokleri` root that is a dir, `kok.glob("*/.skill-kutuphanesi/kilit.json")` (ONE level only, L30-33); plus `ek_projeler` (L34); resolves, dedupes, skips `KOK` itself and any path without `kilit.json` (L38 `continue`: this is the silent drop).
- L45-53 `oku(ayar)`: reads `kilit.json` with `json_oku` (L48; a corrupt JSON raises: P5 does not change this, `--saglik` uses its own tolerant reader) and `elle-kurulan.json` (L49-52; accepts `{"skiller": {...}}` or the bare dict; only the NAMES are kept).
- L56-60 `kisa_yol`: `~/…` form.
- L63-108 `rapor_metni`, 111-117 `hesapla`, 120-125 `guncel_mi`, 128-134 `rapor_guncelle`, 137-145 `kullanan_projeler`: imported dynamically by `skill-ekle.py:1633`, `dogrula.py:262`, `arsiv-guncelle.py:88`. `guncel_mi()` returns `(True, 0)` when no project is found (L123), `rapor_guncelle()` never touches an existing report when no project is found (L131). Report text carries no date (L65-66): same convention for the new report.
- L148-180 `main()`: no-flag run writes `RAPOR` (L174) and prints the count; L178-180 prints the "notes for unknown project" warning (only `notlar` keys).
- `projeler.json` today (12 lines): `_aciklama`, `tarama_kokleri: ["~/Documents"]`, `ek_projeler: []`, `notlar: {IstatistikYoutube: {motion-design: ...}}`.

`araclar/skill-ekle.py` (imported lazily as a module by P5; it has `if __name__ == "__main__"` at L1654, no side effects at import):
- `META=".skill-kutuphanesi"` L57; `kilit_oku(proje)` L191-204 (fills `roller/skiller/profil`, returns default skeleton when no lock; reads old `.agents/skills/SKILLS.lock.json` fallback); `kilit_yaz` L207-211 writes `proje_yolu` and `guncelleme` (so a lock normally holds `proje_yolu`, `kutuphane`, `guncelleme`, `araclar`(optional), `blok`(optional)); `codex_var(kilit)` L214; `kurulu_hash` L219-223; `elle_degismis` L226-236 (includes the "Claude symlink became an identical real copy" tolerance, important for Windows/other-Mac copies: scenario 3).
- `kaynak_bul(skiller, k)` L155-162: source lookup by repo+kaynak_yol (uses `repo_guncel`); None = source gone from library ("yetim").
- `durum()` L1427-1447: the per-skill status order: kaynak yok -> EMEKLİ (`kaynak_durumu` in `kaynakta-kaldirildi`/`kayip`) -> ELLE DEĞİŞTİRİLMİŞ -> GÜNCELLEME VAR (`s["klasor_hash"] != k["klasor_hash"]`) -> KURULUM EKSİK/BOZUK (`kurulum_eksik`, L1155-1163) -> güncel. P5 mirrors this exact order in a pure function `skill_durumu` (a test cross-checks it against `durum()` output).
- `dogrula(proje, skiller, sessiz=True)` L1359-1425 returns the list of problem strings (also: `proje taşınmış (… -> …)` L1411, `kaynağı kütüphanede artık yok` L1407, `kurulumdan sonra elle değiştirilmiş` L1405, `skillOverrides` L1409-1410 via `hesap_gizleme_eksik` L755 which reads `~/.claude/skills/synced` read-only).
- `guncelleme_suruyor()` L1523-1534 (library update lock `.guncelleme-kilidi`).
- `registry()` L139-143 returns `registry.json["skiller"]`; each entry has `id, ad, repo, kaynak_yol, klasor_hash, commit, kaynak_durumu, durum`.
- `proje_raporunu_yenile()` L1625-1651 calls `pk.rapor_guncelle()` and auto-commits ONLY `notlar/proje-kullanimi.md` (L1644-1646). P5 must not make `rapor_guncelle()` write anything else (it would dirty the tree that monthly update/`--birlestir` need clean).

`araclar/ortak.py`: `KOK` L11, `REGISTRY` L13, `GLOBAL_KLASORLER` L37 (dict of machine-wide skill folders; used to flag symlinks to them), `json_oku` L44-48, `json_yaz` L51-60 (atomic write), `klasor_hash` L197-203, `repo_guncel` L444-454.
`araclar/dogrula.py:259-283`: loads `proje-kullanimi.py`, calls `guncel_mi()`, builds `adlar_p` from `projeleri_bul` + `ayar_p["notlar"]` and checks 4 registry-like files for project-name leakage (rule 6 / D8).
`araclar/test.py:1681-1686`: runs `proje-kullanimi.py --kontrol` (must exit 0) and `--skill boyle-bir-skill-yok` (stdout must contain `kullanılmıyor`, no report write). Both stay valid.
`rehber/10-proje-kullanimi.md` (39 lines), `promptlar/12-proje-kullanimi-ve-etki.md` (one `kopyala` prompt, 26 lines). `promptlar/README.md:20` lists prompt 12.
`programlar.json` cards: `programlar.<ad>.skilleri` (HyperFrames: `['hyperframes','hyperframes-cli','media-use','hyperframes-registry']`; OpenMontage and etsyotomasyon: `[]`). Read only by P5.
Real data seen (read only): 5 registered projects under `~/Documents` (AntigravityTest2, Akil Disi Youtube Kanali, Etsy-Arif, Etsy-Yeni, IstatistikYoutube); locks carry `proje_yolu`, `kutuphane`, `guncelleme`; `Etsy-Arif/.skill-kutuphanesi/elle-kurulan.json` has `{ad: {repo, kaynak_yol, commit, lisans}}`; `Akil Disi Youtube Kanali/.agents/skills` has 33 dirs for a 24-skill lock (8 `akil-disi-*` self-written + others); `~/Documents/Istatistik template/Arkadasa-Gonderilecek/KIT` and `~/Documents/Psikolojik Danışman Sosyal Medya` exist.

---------------------------------------------------------------------------------------------------

## 3 Changes per file

### 3.1 `projeler.json` (edit, hand-owned data; shipped literal below)

Old: `_aciklama`, `tarama_kokleri`, `ek_projeler`, `notlar`. New: all old keys unchanged in meaning, plus 4 new top-level keys (`kayitsiz_tarama`, `yoksay`, `bilinen_projeler`, `kendi_skilleri`; `program_kullanimi` was dropped in review). Unknown keys are tolerated by every reader.

```json
{
  "_aciklama": "Proje ↔ skill bilgisinin tek yeri. Skill ve kaynak kayıtlarına proje adı yazılmaz. tarama_kokleri altında bir seviye aranır (.skill-kutuphanesi/kilit.json olan klasörler); başka yerdeki projeler ek_projeler'e tam yolla yazılır. bilinen_projeler: bir kez izlenen projelerin hafızası (silinen/taşınan proje fark edilsin diye). yoksay: bilerek takipsiz klasörler (neden + tarih zorunlu). kayitsiz_tarama: kilitsiz skill'li klasör taraması ayarı. kendi_skilleri: projenin kendi yazdığı skiller (ad ya da * desenleri; kayıtsız skill uyarısı çıkmasın diye). notlar: <proje klasör adı> -> <skill kimliği> -> elle not. Değişiklik komutları: python3 araclar/proje-kullanimi.py --help. Rapor: python3 araclar/proje-kullanimi.py -> notlar/proje-kullanimi.md; sağlık: --saglik -> notlar/proje-durumu.md",
  "tarama_kokleri": ["~/Documents"],
  "ek_projeler": [],
  "kayitsiz_tarama": {
    "kokler": [],
    "derinlik": 4,
    "en_cok_klasor": 30000
  },
  "yoksay": [
    {
      "yol": "~/Documents/Psikolojik Danışman Sosyal Medya",
      "altini_da": true,
      "neden": "Kullanıcı kararı: güncel kullanılmıyor, işlem yapılmaz.",
      "tarih": "2026-11-11"
    },
    {
      "yol": "~/Documents/Istatistik template/Arkadasa-Gonderilecek/KIT",
      "altini_da": true,
      "neden": "Kullanıcı kararı: başkasına gönderilecek dağıtım paketi, önemli değil, işlem yapılmaz.",
      "tarih": "2026-11-11"
    }
  ],
  "bilinen_projeler": {
    "AntigravityTest2":         {"yol": "~/Documents/AntigravityTest2",         "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"},
    "Akil Disi Youtube Kanali": {"yol": "~/Documents/Akil Disi Youtube Kanali", "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"},
    "Etsy-Arif":                {"yol": "~/Documents/Etsy-Arif",                "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"},
    "Etsy-Yeni":                {"yol": "~/Documents/Etsy-Yeni",                "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"},
    "IstatistikYoutube":        {"yol": "~/Documents/IstatistikYoutube",        "tur": "kilitli", "durum": "takipte", "eklendi": "2026-11-11"}
  },
  "kendi_skilleri": {
    "Akil Disi Youtube Kanali": ["akil-disi-*"]
  },
  "notlar": {
    "IstatistikYoutube": {
      "motion-design": "2026-10-15'ten beri bu sürüm kullanılıyor (edit-026); 2026-11-07'de kütüphaneden kurulup güncellemesi izlenmeye başlandı."
    }
  }
}
```

Field rules (validated by `ayar_kontrol`, section 3.2 F):
- `kayitsiz_tarama.kokler`: list of paths; `[]` means "use `tarama_kokleri`". `derinlik`: int 1-6 (1 = direct children of a root), default 4 (KIT is depth 3). `en_cok_klasor`: int, safety cap on directories visited per run, default 30000.
- `yoksay[]`: objects `{yol, altini_da (bool, default false), neden (non-empty str), tarih (YYYY-MM-DD)}`. `altini_da: true` = the folder and everything below it; false = only that exact folder.
- `bilinen_projeler.<klasör adı>`: `{yol, tur: "kilitli"|"elle", durum: "takipte"|"takipten-cikti", eklendi: YYYY-MM-DD}` plus optional `onceki_yollar: [str]` (written by `--tasindi`), `cikis_tarihi`, `cikis_nedeni` (written by `--cikar`), `neden` (written by `--ekle` for `tur: elle`). Key = project folder name (same key convention as `notlar`; two projects with the same folder name are reported as `AYNI AD İKİ YOL` UYARI and are not supported).
- `kendi_skilleri.<proje>`: list of exact names or `fnmatch` patterns (e.g. `akil-disi-*`).
- Project names live only in `projeler.json` and `notlar/proje-*.md` (D8).
- A "known project name" = key of `bilinen_projeler` ∪ names of found projects ∪ basename of any `yoksay` path. Keys of `notlar`, `kendi_skilleri` not in that set give UYARI `projeler.json: <alan> içinde bilinmeyen proje: <ad>`.

### 3.2 `araclar/proje-kullanimi.py` (edit; 184 -> roughly 480 lines after the review reduction)

Policy: all existing functions stay; only two existing places are touched (A, B). Everything else is added after `kullanan_projeler` and in `main()`.

**A. `projeleri_bul(ayar)` (L28-42): one additive filter.** Old: returns every project with a lock. New: build `cikanlar = {_norm(Path(rec["yol"]).expanduser().resolve()) for rec in ayar.get("bilinen_projeler", {}).values() if rec.get("durum") == "takipten-cikti"}` and `continue` when `_norm(y)` is in it (line goes right before `gorulen.add(y)`, after the L38 check). Effect: a project taken out of tracking disappears from `notlar/proje-kullanimi.md`, from `kullanan_projeler()` (so `arsiv-guncelle.py` stops listing it) and from `dogrula.py`'s name list. With the shipped `projeler.json` nobody is `takipten-cikti`, so today's output is byte-identical (acceptance check 10.3). The format of `proje-kullanimi.md` does not change.
Also add `projeleri_bul_ham(ayar)`: same as the old body WITHOUT the `cikanlar` filter (used by `--saglik` to still show opted-out projects in their own section). `projeleri_bul` = `ham` minus `cikanlar`. Implement by extracting, not duplicating.

**B. `main()`** becomes `main(argv=None)` (`ap.parse_args(argv)`, so tests call it in-process) and gets the new flags (3.2 K). `--skill/--repo/--kontrol/no-flag` code paths are untouched; the new flags are checked first with early `return`.
**Exit-code policy (review correction, mandatory):** the entry point is NOT changed globally. Today `main()` (L183-184) discards its return value, so the legacy modes (no flag, `--skill`, `--repo`, `--kontrol`) always exit 0 in the shell, and `test.py:1681` (which runs `--kontrol` against the real library and real projects and expects 0) depends on that. Changing it to `sys.exit(main() or 0)` would turn a merely stale report into a red test (D2 violation). Implementation: a module variable `_CIKIS = 0`; the entry point is `main(); sys.exit(_CIKIS)`. `_CIKIS` is set ONLY by (a) the new modes (`--saglik --siki` with `durum == sorun` -> 1; `--tara-kayitsiz --siki` with a `sorun` scan -> 1; writer/validation errors -> 2 via `sys.exit(2)` directly), and (b) `--kontrol` ONLY when the new flag `--siki` is given with it (`--kontrol --siki` -> 1 on a stale report). `main()`'s own return value for `--kontrol` stays `0/1` as today (in-process tests). Plain `--kontrol` and no-flag keep exit 0 in the shell exactly as before.

**C. New constants** (after `RAPOR`):
```
DURUM_RAPORU = KOK / "notlar" / "proje-durumu.md"
SKILL_KLASORLERI = (".claude/skills", ".agents/skills", ".cursor/skills", ".codex/skills", ".github/skills", ".gemini/skills")
TALIMAT_ISARETLERI = ("AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md", ".cursor/rules",
                      ".agents/rules", ".claude/agents", ".codex/agents", ".agents/agents", ".github/agents")
ATLANAN_KLASORLER = {"node_modules", "__pycache__", "site-packages", "venv", "env", "dist", "build", "target", "vendor",
                     "Pods", "DerivedData", "Library", "Trash"}        # plus EVERY name that starts with "."
ESKI_GUN = 60                                                           # last kilit "guncelleme" older than this -> BİLGİ line
DIKKAT_DOGRULA = ("skillOverrides güncel değil",)                       # dogrula lines that are 'dikkat' not 'sorun'
DOGRULA_TEKRAR = ("elle değiştirilmiş", "kaynağı kütüphanede artık yok", "proje taşınmış (")  # reported by P5 itself; dropped from dogrula's list
AYAR_ANAHTARLARI = ("tarama_kokleri", "ek_projeler", "kayitsiz_tarama", "yoksay", "bilinen_projeler", "kendi_skilleri", "notlar")
```
Tool names are NOT hard-coded: `kilit["araclar"]` values are printed as found (P1 may add `antigravity`, `cursor`, `copilot`); unknown values are never an error.

**D. Helpers (pure, no I/O beyond reading):**
- `_norm(p) -> str`: `unicodedata.normalize("NFC", str(Path(p).expanduser().resolve()))`.
- `_skill_ekle()`: lazy module cache; loads `araclar/skill-ekle.py` with `importlib.util.spec_from_file_location("skillekle", ...)`; returns the module or `None` on any exception. Tests replace `pk._SE_ONBELLEK[0]`. All callers handle `None` (falls back to "denetlenemedi: skill-ekle.py yüklenemedi" -> sorun line, never a crash).
- `kilit_guvenli_oku(yol) -> (kilit|None, hata|None)`: reads `<yol>/.skill-kutuphanesi/kilit.json` with `json.loads`; JSON error / not a dict -> `(None, "kilit.json okunamıyor: <kısa hata>")`; on success returns `se.kilit_oku(yol)` (normalised) when `se` available, else the raw dict.
- `skill_durumu(proje, ad, k, kilit, skiller, se) -> str` mirroring `skill-ekle.durum()` order; returns one of `kaynak-yok`, `emekli-kaynakta-kaldirildi`, `emekli-kayip`, `elle-degismis`, `guncelleme-var`, `kurulum-eksik`, `guncel`.
- `disk_skilleri(proje) -> {ad: [göreli klasörler]}`: for each dir in `SKILL_KLASORLERI` that exists as a real directory (not a symlink to a directory outside the project: if the skills dir itself is a symlink it is skipped here and reported by the scan as `baglanti`), each child that is a directory (or a symlink to one) containing `SKILL.md` counts, keyed by child name (so `.claude/skills/x` symlink and `.agents/skills/x` are one skill). Never reads other files.
- `elle_kayitlari(proje) -> (dict, hata|None)`: parsed `elle-kurulan.json` (`skiller` wrapper tolerated); `({}, None)` if missing; `({}, "<hata>")` if corrupt (the caller turns it into a sorun line).
- `kendi_mi(proje_adi, skill_adi, ayar) -> bool`: `fnmatch.fnmatchcase` against `ayar["kendi_skilleri"].get(proje_adi, [])`.
- `kutuphane_hash_haritasi(skiller) -> {klasor_hash: id}` (built once from registry entries; used only for the HINT below).
- `ayar_kontrol(ayar) -> [str]`: schema validation (types, enum values, date format `YYYY-MM-DD`, non-empty `neden`, unknown project names in `notlar/kendi_skilleri`, `yoksay` path that no longer exists = BİLGİ, same folder name with two different `yol` = `AYNI AD İKİ YOL`). Returns UYARI strings.
- `izleme_kapsaminda_mi(yol, ayar=None) -> (bool, str)` (used by `--saglik`'s out-of-scope listing and by `--ekle`; NOT offered to `skill-ekle.py` after review, see section 6 item 6): True when the folder is exactly one level under a `tarama_kokleri` root or equals an `ek_projeler` entry (compared with `_norm`); the str is the reason (`tarama kökü altında` / `ek_projeler'de` / `kapsam dışı: --ekle gerekir`). Pure, no I/O except `expanduser/resolve`.
- `hizli_kontrol(ayar=None) -> [str]`: **cheap** (no registry, no hashing, no scan, no subprocess; < 50 ms) set of UYARI lines meant for `dogrula.py` (hand-off 6): `ayar_kontrol` lines + for each `bilinen_projeler` entry with `durum: "takipte"`: `yol` missing -> `proje takibi: KAYIP: <ad> (<yol>) klasörü yok -> --saglik; taşındıysa --tasindi, silindiyse --cikar`; `tur: "kilitli"` and folder exists but no `kilit.json` -> `KİLİT YOK`; `ek_projeler` path missing -> `ek_projeler yolu yok`. Returns `[]` (silent) when `projeler.json` is absent or when `projeleri_bul_ham(ayar)` finds NO project on this machine, whatever `bilinen_projeler` holds (cloud session / other clone / Windows copy: same philosophy as `guncel_mi` L123). The `bilinen_projeler`-based KAYIP/KİLİT YOK lines are only produced when at least one tracked project IS found (i.e. this is the library machine).

**E. Health model (`saglik_hesapla(ayar, skiller, programlar, bugun=None) -> dict`)**
Returns `{"projeler": [P...], "kaybolanlar": [...], "takipte_olmayan": [...], "kayitsiz": {...}, "ayar_uyarilari": [...], "durum": "temiz|dikkat|sorun", "karar_bekleyen": [...]}`. Never raises: each project is wrapped in `try/except Exception as e` -> a `sorun` line `denetlenemedi: <hata>`. Never writes. Never opens any file other than: `kilit.json`, `elle-kurulan.json`, `.claude/settings.json` (only via `se.dogrula`), skill folder contents for hashing, and instruction/marker NAMES via directory listing. `.env*`, keys and tokens are never opened or listed (the scan only checks for the marker names in `SKILL_KLASORLERI`/`TALIMAT_ISARETLERI`).

Per tracked project P (from `projeleri_bul_ham` ∩ not `takipten-cikti`), fields and rules (each rule yields a line `[düzey] metin`, düzey ∈ `sorun`, `dikkat`, `bilgi`; project durum = worst):
1. Lock readable: `KİLİT OKUNAMIYOR: <hata>` -> sorun; stop further checks for this project.
2. Path: lock `proje_yolu` != actual path: if the recorded parent folder does not exist on this machine (copied from elsewhere: different user home, `C:\`, another Mac) -> `dikkat: BAŞKA YERDEN KOPYALANMIŞ olabilir (kilit yolu: <eski>) -> kütüphanenin olduğu Mac'te: skill-ekle.py "<proje>" --yenile; skill-ekle bu kopyada çalıştırılmaz`; else -> `dikkat: TAŞINMIŞ (kilit yolu: <eski>) -> skill-ekle.py "<proje>" --yenile`.
3. Library path: lock `kutuphane` != `str(KOK)` -> `dikkat: kilit başka bir kütüphane yoluna ait (<yol>) -> promptlar/09`.
4. Counts: lock skills N; on disk M (from `disk_skilleri`).
5. Per lock skill: `skill_durumu` -> counters `guncelleme_var`, `elle_degismis`, `kaynak_yok` (= "yetim"), `emekli`, `kurulum_eksik`. Lines: `guncelleme-var` -> dikkat `GÜNCELLEME VAR: <ad> (<eski7> -> <yeni7>)`; `elle-degismis` -> dikkat; `kaynak-yok` -> dikkat `KAYNAK KÜTÜPHANEDE YOK: <ad> (<repo>:<yol>) -> yerine geçeni KATALOG.md'den bul ya da kaldır`; `emekli-*` -> dikkat; `kurulum-eksik` -> sorun.
6. Structure: `se.dogrula(proje, skiller, sessiz=True)` lines, after dropping those matching `DOGRULA_TEKRAR`; each remaining line -> sorun, except lines containing a `DIKKAT_DOGRULA` marker -> dikkat. (`se.dogrula` reads the same lock again; double work is acceptable.)
7. Disk-vs-lock classification of every name in `disk_skilleri` that is NOT a key of `kilit["skiller"]`, in this order: in `elle_kayitlari` -> `elle` (counter, no line); matches `kendi_skilleri` -> `kendi` (counter, no line); folder hash equals a registry `klasor_hash` -> `dikkat: KİLİTSİZ KÜTÜPHANE KOPYASI: <ad> (kütüphanedeki <id> ile aynı içerik; elle kopyalanmış olabilir; --elle-taslak <proje>)`; else `dikkat: KAYITSIZ SKILL: <ad> (kilitte, elle-kurulan.json'da ve kendi_skilleri'nde yok)`. The registry-hash hint is best-effort: a copy that went through path localisation or repair differs and falls into `KAYITSIZ SKILL`; that is fine.
8. Reverse: names in `elle_kayitlari` with no folder on disk -> `dikkat: elle-kurulan.json'da olup klasörü yok: <ad>`.
9. Age: lock `guncelleme` older than `ESKI_GUN` days (relative to `bugun`) -> `bilgi: son işlem <tarih> (60 günden eski)`. The report prints the date only, never an age (so the file does not change daily).
10. Tool selection (accepted P1 request): printed as `araçlar: <lock araclar or "claude, codex (kilitte yok: varsayılan)">`; layout correctness comes from step 6. When the lock has no `araclar` field (older locks) or P1's tool-choice field says `varsayılan` (read tolerantly: `kilit.get("arac_secimi")`, absent is fine, never an error), the project gets `bilgi: araç seçimi kilitte yok (varsayılan: claude, codex)` (no flag name is hard-coded: P1 owns the tool-choice flag). `bilgi` never raises the level.
11. Hand-installed (`tur: "elle"`, no lock expected): checks = folder exists; skills on disk listed; each classified as in 7 (all are `elle`/`kendi`/`KİLİTSİZ KÜTÜPHANE KOPYASI`/`KAYITSIZ`); no update/health claims.

`kaybolanlar` (from `bilinen_projeler` with `durum: "takipte"` and not found among tracked):
- `yol` exists, no `kilit.json`, `tur: kilitli` -> sorun `KİLİT YOK: <ad> klasör duruyor, .skill-kutuphanesi/kilit.json yok (silinmiş ya da kurulum yarım kaldı) -> kurulumu yeniden yap (promptlar/09) ya da --cikar`.
- `yol` missing and a found project has the same folder name at another path -> sorun `TAŞINMIŞ görünüyor: <ad> şimdi <yeni> -> --tasindi "<ad>" "<yeni>"`.
- `yol` missing, no such project -> sorun `KAYIP: <ad> klasörü yok (<yol>) -> taşındıysa --tasindi "<ad>" "<yeni yol>", silindiyse --cikar "<ad>" --neden "..."`.
- Found tracked projects not in `bilinen_projeler` -> dikkat `KAYITLI DEĞİL: <ad> hafızada yok -> --ekle "<yol>" (kilitli proje için bilinen_projeler'e yazar)` (decision item).
- `ek_projeler` path that does not exist and not in `bilinen_projeler` -> dikkat `ek_projeler yolu yok: <yol>`.
`takipte_olmayan`: `bilinen_projeler` with `durum: "takipten-cikti"`: `<ad>: takipten çıktı <cikis_tarihi> — <cikis_nedeni>`; if its lock still exists add `bilgi: kilit duruyor (silinmedi)`. If its folder is gone: nothing (intended).
`ayar_uyarilari` = `ayar_kontrol(...)`; any `ayar_kontrol` line is dikkat (never sorun), except the stale-`yoksay` line which is `bilgi` and does not raise the level.

Overall `durum`: `sorun` if any project line level is sorun or any `kaybolanlar` sorun line; else `dikkat` if any dikkat line, any unregistered skilled folder (scan, below), any `KAYITLI DEĞİL` or `ayar_uyarilari`; else `temiz`. `bilgi` never raises the level.

**F. Unregistered scan (`tara_kayitsiz(ayar, bulunan_projeler, skiller) -> dict`)** (read only, no network, no subprocess):
- Roots: `kayitsiz_tarama.kokler` or, when empty, `tarama_kokleri`. A root that is not a directory is skipped with a `bilgi` line (not an error).
- **Ignore list is applied BEFORE any directory is opened (review correction):** for every directory the walk is about to enter, `_norm(d)` is compared with the `yoksay` entries first; on a match (exact, or `altini_da` subtree) the directory is counted in `yoksayilan` and is NEVER passed to `os.scandir`, `lstat` of its children, or any marker check. The only thing seen of an ignored folder is its name, which came from the PARENT's listing. Same for the library root and tracked/`takipten-cikti` projects. Test 15 patches `os.scandir`, `os.lstat` and `os.stat` with a recorder and asserts that no recorded path equals or lies under an ignored folder.
- Walk (own iterative `os.scandir` stack, NOT `glob`/`os.walk` with link-following): depth limit `derinlik` counted from the root (children of the root are depth 1). A directory entry is descended into only when `entry.is_dir(follow_symlinks=False)`; symlinked directories are never followed and are counted (`atlanan_baglanti`). Names starting with `.` and names in `ATLANAN_KLASORLER` are not descended into. `KOK` (the library) is never descended into; neither is any found tracked project or a directory that is `takipten-cikti` (they are known). Stop with `sinira_ulasildi: true` after `en_cok_klasor` directories (reported as dikkat line `tarama sınıra ulaştı (<n> klasör) -> kayitsiz_tarama.derinlik/en_cok_klasor`; results found so far are still reported).
- For each visited directory `d` (including depth 1.. `derinlik`): one `os.scandir(d)` giving child names; marker check by `os.path.lstat`/`is_dir(follow_symlinks=False)` on `d/<marker>`; never opens file contents.
  - `skilli`: at least one of `SKILL_KLASORLERI` is a real directory with >= 1 child dir containing `SKILL.md` (count distinct names), OR a skills dir is a symlink (`baglanti`: record `os.readlink` target text; flag `genel_klasore_bagli: true` when the target text expands to a path under any `ortak.GLOBAL_KLASORLER` value, because emptying those folders (P2) would break it).
  - `talimat`: not `skilli`, but one of `TALIMAT_ISARETLERI` exists.
  - A candidate directory (`skilli` or `talimat`) is not descended into further (it is the project root). A directory that has `.skill-kutuphanesi/kilit.json` is a tracked project (skipped, not a candidate).
  - Matching `yoksay`: `_norm(d) == _norm(entry.yol)` or (`altini_da` and `_norm(d)` starts with `_norm(entry.yol) + os.sep`) -> not reported as candidate; counted in `yoksayilan` with `neden` and `tarih`; the walk does not descend under an ignored folder with `altini_da`.
- Per candidate: `{"yol": kisa_yol, "sinif": "skilli"|"talimat", "skill_sayisi": int, "araclar": sorted tool labels, "baglanti": [{"klasor","hedef","genel":bool}]}` where tool labels come from the markers found: `claude` (`.claude/skills|agents`, `CLAUDE.md`), `agents/codex` (`.agents/*`, `.codex/*`, `AGENTS.md`), `cursor` (`.cursor/*`), `copilot` (`.github/skills|agents|copilot-instructions.md`), `gemini` (`.gemini/*`, `GEMINI.md`).
- Output ordering: sorted by `yol`. Only `skilli` candidates feed `karar_bekleyen` (one line each, capped at 8 plus `…ve N tane daha`); `talimat` ones are only counted in the report (`N klasörde yalnız talimat dosyası var, skill yok: işlem gerekmez`).
- Stale ignore entry (path no longer exists) -> `bilgi: yoksay girdisi artık yok: <yol> (temizlenebilir)`.

**G. (deferred in review) Program usage per project.** `program_kullanimi`, `programi_kullanan_projeler`, `--program` are NOT in the first version (see section 8, 11). Program cards stay untouched; `rehber/10` states that the project side of program tracking is not yet automated.

**H. Report writer `durum_raporu_metni(sonuc, ayar) -> str`** produces `notlar/proje-durumu.md`, deterministic, no date, no time, no ages (format in 4.3). `--saglik` writes it with `Path.write_text` only when content differs from the existing file (same idempotence as `rapor_guncelle`, L131); when `projeleri_bul_ham(ayar)` finds no project on this machine (other machine/cloud, same philosophy as L123/L171) it prints `Hiç proje bulunamadı (başka bilgisayar/bulut olabilir); notlar/proje-durumu.md değiştirilmedi.`, leaves the file untouched, and `--ozet-json` returns `{"durum": "temiz", "satirlar": ["Bu bilgisayarda proje bulunamadı: denetim atlandı"], ...}`, exit 0, even though `bilinen_projeler` lists projects. The KAYIP logic therefore only runs on the library machine.

**I. Writers (edit ONLY `projeler.json`; dry-run by default).** D4 clarification: these are configuration edits to a file inside the library, separate from the report modes. The report modes `--saglik`, `--tara-kayitsiz`, `--yetim`, `--program`, `--elle-taslak`, `--ozet-json` write at most `notlar/proje-durumu.md` (and only `--saglik`, or `--ozet-json --yaz`, do that) and never `projeler.json`. All go through pure `ayar_degistir(ayar, islem, **kw) -> (yeni_ayar, [aciklama satırları])`, the printed plan is the full change; `--evet` writes with `ortak.json_yaz(AYAR, yeni)` (atomic) and prints `projeler.json güncellendi (geri almak: git checkout -- projeler.json)`. Refused while `se.guncelleme_suruyor()` returns a lock (message `BEKLE: kütüphane aylık güncelleniyor`). They never touch a project folder, `kilit.json`, `elle-kurulan.json`, `registry.json`, any other library file. After a write they do NOT refresh `proje-kullanimi.md` automatically (the monthly flow keeps a clean tree; the user is told to run the no-flag report if he wants it refreshed). Each writer validates inputs and exits 2 with a Turkish message on error.
- (deferred in review) `--bilinenleri-yaz`: the five currently tracked projects are shipped in `bilinen_projeler` in section 3.1; later projects enter memory through `--ekle`. A tracked project that is missing from memory is shown as `KAYITLI DEĞİL` with the `--ekle` command.
- `--ekle <yol> [--neden <metin>]`: "put this project under tracking". Rules: folder must exist and be a directory; refuse if it is the library, home, a machine-wide skill folder or inside `.skill-kutuphanesi` (same guard idea as `skill-ekle.py:1562-1569`). With `kilit.json`: add to `bilinen_projeler` as `tur: "kilitli"`, and add to `ek_projeler` when the folder is not exactly one level under a `tarama_kokleri` root (so `projeleri_bul` can see it). Without `kilit.json` (hand-installed): requires `--neden`, adds `tur: "elle"`; message says "kilit yok: güncellenmez, sadece sağlık/envanter; kütüphaneyle yönetmek için önce skill-ekle.py <yol> --kuru". If the entry exists with `takipten-cikti`: set `durum: "takipte"`, drop `cikis_tarihi`/`cikis_nedeni` (history is in git).
- `--cikar <ad> --neden <metin>`: sets `durum: "takipten-cikti"`, `cikis_tarihi` today, `cikis_nedeni`. If the project is tracked (found by `projeleri_bul_ham`) but not yet in `bilinen_projeler`, the entry is created in the same change with `durum: takipten-cikti`; an unknown name is `HATA: <ad> izlenen projelerde yok`. Removing a project from tracking never deletes its folder or lock; it only stops the report/monthly listing. If the folder is already deleted this is the way to silence `KAYIP`.
- `--tasindi <ad> <yeni-yol>`: new folder must exist; if it has no lock and `tur: kilitli` refuse; updates `yol`, appends old `yol` to `onceki_yollar`; replaces a matching `ek_projeler` entry; when the new folder name differs from `<ad>` also renames the key in `bilinen_projeler`, `notlar`, `kendi_skilleri` and prints that a rename was applied. Prints the next step: `python3 araclar/skill-ekle.py "<yeni-yol>" --yenile --kuru` then user approval for the real `--yenile` (this P5 tool does NOT run it).
- `--yoksay <yol> --neden <metin> [--altini-da]`: appends `{yol (~ form), altini_da, neden, tarih: bugün}`; refuses duplicate and empty `neden`.
- (deferred in review) `--yoksay-kaldir`: an ignore entry is removed by editing `projeler.json` by hand and committing (the stale-entry `bilgi` line tells when).
`--evet` without a writer flag is ignored with a message. Two writer flags at once -> exit 2.

**J. Read-only extras**
- (deferred in review) `--yetim`: the same information is already in `--saglik` (E.5, E.7, E.8: `KAYNAK KÜTÜPHANEDE YOK`, `KAYITSIZ SKILL`, `KİLİTSİZ KÜTÜPHANE KOPYASI`).
- (deferred in review) `--program <ad>`.
- (deferred in review) `--elle-taslak`: the `KAYITSIZ SKILL` line already names the folder; the library session writes the `elle-kurulan.json` entry by hand with the user's approval (it is a project file: not written by this tool, D7).
- `--tara-kayitsiz`: stdout only (table of candidates, ignored entries and limit info); no file; this is the cheap preview of the scan section of `--saglik`.

**K. CLI (argparse; existing flags unchanged)**
```
python3 araclar/proje-kullanimi.py                      # unchanged: writes notlar/proje-kullanimi.md
python3 araclar/proje-kullanimi.py --skill <id> | --repo owner/ad | --kontrol [--siki]    # unchanged; --siki is new and only then gives a real exit 1 on a stale report
python3 araclar/proje-kullanimi.py --saglik [--siki] [--ozet-json [--yaz]]
python3 araclar/proje-kullanimi.py --tara-kayitsiz [--siki]
python3 araclar/proje-kullanimi.py --ekle <yol> [--neden ..] | --cikar <ad> --neden .. | --tasindi <ad> <yeni-yol> | --yoksay <yol> --neden .. [--altini-da]   [--evet]
```
- `--ozet-json` (valid with `--saglik`, or alone = implies `--saglik` computation): all human output is suppressed (computation runs under `contextlib.redirect_stdout(io.StringIO())`), and stdout receives exactly one line: the JSON object of D4. No file is written unless `--yaz` is also given (then `notlar/proje-durumu.md` is refreshed). Errors in the computation of one project are lines in `satirlar`, never a traceback on stdout.
- Exit codes (see 3.2 B for the mechanism): 0 whenever the tool ran correctly, whatever it found (including `durum: sorun`); 1 only with `--siki` and the result `durum == "sorun"` (`--saglik --siki`, `--tara-kayitsiz --siki`: unregistered skilled folders are `dikkat`, so they never give 1; only an unreadable scan root is `sorun`) or `--kontrol --siki` on a stale report; 2 for usage/validation errors. The legacy modes (no flag, `--skill`, `--repo`, plain `--kontrol`) keep exiting 0 in the shell exactly as today (the entry point discards `main()`'s value; `test.py:1681` therefore keeps passing even when the report is stale, which is today's behaviour and is not changed). `skill-ekle.py`/`dogrula.py`/`arsiv-guncelle.py` use `guncel_mi()` directly, not the exit code.

**`--ozet-json` object** (exact):
```json
{"arac": "proje-kullanimi", "durum": "dikkat",
 "satirlar": ["5 proje izleniyor: 0 sorun, 3 dikkat", "GÜNCELLEME VAR: 2 skill (AntigravityTest2, Etsy-Arif)", "ELLE DEĞİŞTİRİLMİŞ: 0", "KAYNAK KÜTÜPHANEDE YOK: 1 skill (Etsy-Arif)", "KAYITSIZ SKILL: 1 (Akil Disi Youtube Kanali)", "KAYITSIZ PROJE: 4 skilli klasör, 9 yalnız talimat dosyalı", "KAYIP/TAŞINMIŞ: 0"],
 "karar_bekleyen": ["Kayıtsız proje: ~/Documents/Yetisio (6 skill) -> --ekle <yol> --neden ... ya da --yoksay <yol> --neden ...", "AntigravityTest2: 1 güncelleme -> skill-ekle.py <proje> --guncelle --kuru, sonra onay"]}
```
`satirlar` <= 15 items, each <= 160 chars, Turkish, no secrets (D9: only counts and names; e.g. `skillOverrides` lines are never echoed with values). `karar_bekleyen` <= 12 items (overflow summarised in the last item).

### 3.3 `rehber/10-proje-kullanimi.md` (edit: keep all 39 existing lines; append sections, and extend the table at the top)

- Table: add rows `notlar/proje-durumu.md` (generated, `--saglik`) and extend the `projeler.json` row ("+ `bilinen_projeler`, `yoksay`, `kayitsiz_tarama`, `kendi_skilleri`").
- Under "## Kullanım" add the new commands (section 3.2 K).
- New sections (text in 4.2): `## Aylık proje turu`, `## Yeni proje izlemeye alma (kilitli ya da elle kurulu)`, `## Kayıtsız proje bulma ve karar`, `## Projeyi takipten çıkarma`, `## Proje taşındı, silindi ya da başka bilgisayara kopyalandı`, `## Projenin kendi yazdığı ve elle kurulan skiller`, `## Bilerek takipsiz klasörler (yoksay)`, `## Kuralların dışında kalanlar` (what P5 never does: no writes to projects, no writes to machine-wide folders).
- Existing paragraph "Yeni proje nasıl rapora girer" gets one added sentence pointing to `--ekle` (no deletion).

### 3.4 `promptlar/12-proje-kullanimi-ve-etki.md` (edit)

Keep the existing prompt block verbatim. Change the header lines only: the title becomes `# 12 — Proje Kullanımı, Etki Kontrolü ve Proje Sağlık Turu`; "Ne zaman" gains the sentence in 4.4. Append two new `kopyala` blocks (texts in 4.4): "Proje sağlık turu" and "Proje ekle / çıkar / taşındı / yoksay". P8 updates `promptlar/README.md:20` (hand-off 5).

### 3.5 `araclar/testler/test_p5-proje-takibi.py` (new): see section 5.

`araclar/testler/` does not exist yet: the file creates nothing outside itself, but the implementer creates the folder (`mkdir araclar/testler`, no `__init__.py` needed; run as a script). Other packages create the same folder; creating it twice is harmless.

---------------------------------------------------------------------------------------------------

## 4 User-facing texts

### 4.1 CLI messages (Turkish, exact)
- Health summary on stdout (`--saglik`): first line `Proje sağlığı: <N> proje izleniyor · <s> sorun · <d> dikkat · <k> kayıtsız skilli klasör · rapor: notlar/proje-durumu.md`, then one line per project `  <ad>: <durum> (<n> skill)` and the first 3 problem lines of non-`temiz` projects.
- `Hiç proje bulunamadı (başka bilgisayar/bulut olabilir); notlar/proje-durumu.md değiştirilmedi.`
- Writer dry run: `PLAN (hiçbir şey yazılmadı; onaylıyorsan aynı komuta --evet ekle):` followed by lines `  + bilinen_projeler.<ad>: ...`. Real write: `projeler.json güncellendi (geri almak: git checkout -- projeler.json).`
- Errors: `HATA: <yol> bir klasör değil` · `HATA: --neden zorunlu` · `HATA: <ad> izlenen projelerde yok` · `HATA: bu klasör proje olamaz (kütüphane, ev dizini ya da genel skill klasörü)` · `HATA: yeni yolda kilit.json yok` · `BEKLE: kütüphane aylık güncelleniyor; birkaç dakika sonra tekrar dene.`
- Safety footer on every non-JSON mode: `Bu araç hiçbir proje klasörüne ve genel skill klasörüne yazmaz.`

### 4.2 `rehber/10` new sections (final wording, Turkish, plain)

```
## Aylık proje turu
Her ay (ya da "projeleri kontrol et" denince) kütüphane oturumu şunu çalıştırır: `python3 araclar/proje-kullanimi.py --saglik`.
Çıktı `notlar/proje-durumu.md`: her projenin durumu, güncellemesi gelen / elle değişmiş / kaynağı kütüphanede kalmamış skiller,
kayıtsız klasörler ve programların hangi projede kullanıldığı. Araç yalnızca okur; çıkış kodu 0'dır (sonuç "sorun" olsa da).
Kullanıcıya sade özet verilir; her gerçek değişiklik (güncelleme, kaldırma, kayıt) ayrı ayrı onay ister.
Tur bitince değişen `notlar/proje-durumu.md` dosyası tek başına commit edilir (`git commit -m "Proje durumu yenilendi" -- notlar/proje-durumu.md`); kirli ağaç aylık güncellemeyi (`arsiv-guncelle.py --uygula`) engeller. Push yalnız kullanıcı isteyince.

## Yeni proje izlemeye alma
1. Kütüphaneden ilk kurulum: `skill-ekle.py <proje> --profil … --kuru` -> onay -> `--evet` (rehber/01).
2. Proje `~/Documents` altında bir seviyedeyse rapora kendiliğinden girer. Başka yerdeyse: `proje-kullanimi.py --ekle <yol>` (önce plan gösterir, `--evet` ile yazar).
`--ekle` aynı zamanda projeyi hafızaya (`bilinen_projeler`) yazar: silinirse ya da taşınırsa araç fark eder.
Skiller elle kopyalanmış, kilidi olmayan proje: `proje-kullanimi.py --ekle <yol> --neden "elle kurulu"`. Bu proje yalnızca izlenir
(sağlık ve envanter); güncellenmez. Kütüphaneyle yönetmek istersen önce `skill-ekle.py <yol> --kuru` ile ön kontrol yapılır.

## Kayıtsız proje bulma ve karar
`proje-kullanimi.py --tara-kayitsiz` kilidi olmayan ama skill klasörü olan klasörleri listeler (derinlik ve kökler `projeler.json` -> `kayitsiz_tarama`;
bağlantıları izlemez, `.env` gibi dosyalara bakmaz). Her klasör için üç karardan biri verilir ve kullanıcıya sorulur:
(a) kütüphaneyle yönet: `skill-ekle.py` ile kur; (b) yalnız izle: `--ekle <yol> --neden …`; (c) bilerek takipsiz: `--yoksay <yol> --neden …`.
Karar verilmeyen klasör her ay raporda "karar bekleyen" olarak kalır. "Yalnız talimat dosyası olan" klasörler sayılır, işlem gerektirmez.

## Projeyi takipten çıkarma
`proje-kullanimi.py --cikar <ad> --neden "…"` (onayla). Proje klasörüne ve kilidine dokunulmaz; yalnız rapordan, aylık listeden ve
"KAYIP" uyarısından çıkar. Silinmiş projenin "KAYIP" uyarısını susturmanın yolu budur. Geri almak: `--ekle <yol>`.

## Proje taşındı, silindi ya da başka bilgisayara kopyalandı
- Taşındı: `--saglik` "TAŞINMIŞ görünüyor" der -> `proje-kullanimi.py --tasindi "<ad>" "<yeni-yol>"` (onayla) -> `skill-ekle.py "<yeni-yol>" --yenile --kuru` -> onay -> `--yenile`.
- Silindi: "KAYIP" -> kullanıcıya sor -> `--cikar`.
- Başka Mac'e ya da Windows'a kopyalandı: kopya salt okunur sayılır. `skill-ekle.py` yalnızca kütüphanenin olduğu bilgisayarda çalışır; kopyada
  `.skill-kutuphanesi/kilit.json` içindeki yollar eski bilgisayara aittir, bu normaldir. Skill ekleme/güncelleme kütüphane bilgisayarında yapılır, kopya oraya geri getirilince `--yenile` gerekir.
  (Windows'ta skill-ekle.py çalıştırılması test edilmedi.)

## Projenin kendi yazdığı ve elle kurulan skiller
Kilitte olmayan her skill klasörü `--saglik`te şu üçünden biri olarak görünür: `elle` (projenin `.skill-kutuphanesi/elle-kurulan.json` dosyasında),
`kendi` (`projeler.json` -> `kendi_skilleri` desenlerinden biri), ya da "KAYITSIZ SKILL" (karar bekleyen). Kayıtsızı sınıflamak için
kütüphane oturumu kullanıcıya sorar ve onayıyla projenin `.skill-kutuphanesi/elle-kurulan.json` dosyasına elle ekler (araç projeye yazmaz). Projenin kendi yazdığı skiller
için `projeler.json` -> `kendi_skilleri` -> `<proje>` listesine ad ya da `akil-disi-*` gibi desen yazılır.

## Programlar hangi projede (ilk sürümde otomatik değil)
HyperFrames / OpenMontage'ı hangi projenin kullandığı bu sürümde araçla izlenmez (ertelendi). Programı güncellemeden önce etkilenecek projeler
`notlar/hf-om-gecisi/DURUM.md` "Proje taraması" bölümünden ve `--saglik` çıktısındaki genel klasöre bağlantı satırlarından okunur. Program kartlarına proje adı yazılmaz (kural 6).

## Bilerek takipsiz klasörler (yoksay)
`yoksay` listesinde klasör yolu, neden ve tarih bulunur. Şu an: Psikolojik Danışman Sosyal Medya ve İstatistik KIT paketi (kullanıcı kararı 2026-11-11: işlem yapılmaz).
Yeni giriş: `--yoksay <yol> --neden "…" [--altini-da]`; kaldırmak: `projeler.json` elle düzenlenir ve commit edilir.

## Araç ne yapmaz
Hiçbir proje klasörüne, `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage` altına yazmaz; push yapmaz; yalnız `projeler.json`
(onayla) ve kendi raporlarını (`notlar/proje-kullanimi.md`, `notlar/proje-durumu.md`) yazar.
```

### 4.3 `notlar/proje-durumu.md` format (generated; exact skeleton)

```
# Proje durumu — kayıtlı projelerin sağlığı

> `araclar/proje-kullanimi.py --saglik` üretir; elle düzenleme. Salt okuma: hiçbir projeye ve genel skill klasörüne yazılmaz.
> Tarih yoktur: içerik yalnız durum değişince değişir. Ayrıntı: `rehber/10-proje-kullanimi.md`.

**Genel durum: dikkat**

## Projeler
| Proje | Durum | Skill (kilit/klasör) | Güncelleme var | Elle değişmiş | Kaynak yok | Kayıtsız | Kendi/elle | Araçlar | Son işlem |
|---|---|---|---|---|---|---|---|---|---|
| AntigravityTest2 | dikkat | 9/9 | 1 | 0 | 0 | 0 | 0 | claude, codex | 2026-11-07 |

## Ayrıntı
### AntigravityTest2 — dikkat
- [dikkat] GÜNCELLEME VAR: ui-ux-pro-max (1a2b3c4 -> 5d6e7f8)

## Kayıp, taşınmış ya da hafızada olmayan
- (satır yoksa: `Yok.`)

## Takipte olmayanlar
- (satır yoksa: `Yok.`)

## Kayıtsız proje klasörleri
Tarama: `~/Documents` (derinlik 4, <n> klasör bakıldı, bağlantılar izlenmedi).
| Klasör | Sınıf | Skill | Araçlar | Not |
|---|---|---|---|---|
| `~/Documents/Yetisio` | skilli | 6 | claude | |
Yalnız talimat dosyası olan klasör sayısı: 9 (işlem gerekmez).
### Yoksayılanlar
| Yol | Neden | Tarih |
|---|---|---|

## Karar bekleyenler
- …

## Ayar uyarıları
- (`projeler.json` doğrulaması; yoksa `Yok.`)
```
Ordering: projects by name (case-insensitive), candidates by path, programs by name. No absolute home paths other than the `~/` form.

### 4.4 `promptlar/12` additions (final wording)

"Ne zaman" gets: `Ayrıca: aylık "projeleri kontrol et" turunda; yeni proje, taşınan/silinen proje, kayıtsız klasör ya da elle kurulu skill çıktığında.`

Block 2:
```kopyala
Proje sağlık turu yap. ~/Documents/SkillKutuphanesi/AGENTS.md'yi oku (Claude ise CLAUDE.md).

1. python3 araclar/proje-kullanimi.py --saglik   → notlar/proje-durumu.md'yi üretir (hiçbir projeye yazmaz).
2. Bana sade bir özet ver: kaç proje, kaçında sorun/dikkat var; sorun varsa önce onu yaz.
3. Karar bekleyenleri tek tek, konu konu sor: güncellemesi gelen projeler (skill-ekle.py <proje> --guncelle --kuru ile göster),
   kayıtsız klasörler (kütüphaneyle yönet / yalnız izle / yoksay), KAYIP ya da TAŞINMIŞ projeler, KAYITSIZ SKILL'ler.
4. Tur bitince yalnız notlar/proje-durumu.md'yi tek başına commit et (kirli ağaç aylık güncellemeyi engeller); push yapma.
5. Onayım olmadan hiçbir şey yazma; onaylarsam yalnız söylenen komutu çalıştır. Projelere, genel skill klasörlerine
   (~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.openmontage) dokunma.
```
Block 3:
```kopyala
Projeyi takip listesinde şu işlemi yap: [ekle <yol> | çıkar <ad> | taşındı <ad> → <yeni-yol> | yoksay <yol>]. Gerekçe: [NEDEN].
~/Documents/SkillKutuphanesi/AGENTS.md'yi oku.

1. İlgili komutu --evet OLMADAN çalıştır (proje-kullanimi.py --ekle / --cikar / --tasindi / --yoksay), planı bana göster.
2. Onaylarsam aynı komutu --evet ile çalıştır; sonra python3 araclar/proje-kullanimi.py --saglik ile sonucu doğrula.
3. Sadece projeler.json değişir. Projeye, genel klasörlere dokunma. Kayıtlara proje adı yazma (kural 6). Push yapma.
```

---------------------------------------------------------------------------------------------------

## 5 Tests: `araclar/testler/test_p5-proje-takibi.py`

Runnable alone: `python3 araclar/testler/test_p5-proje-takibi.py`. Standard library only. Builds everything in `tempfile.mkdtemp()`; never reads/writes `~`, `~/Documents`, `registry.json` (22 MB), the real `projeler.json`, `notlar/` or the library git. It loads `araclar/proje-kullanimi.py` via `importlib` and then monkey-patches: `pk.AYAR`, `pk.RAPOR`, `pk.DURUM_RAPORU` to temp paths; `pk._SE_ONBELLEK[0]` to a stub object exposing `kilit_oku, dogrula, kaynak_bul, elle_degismis, kurulum_eksik, guncelleme_suruyor` implemented over fake data (or the real `skill-ekle` module with `hesap_gizleme_eksik = lambda p, k: []` for test 20); a fake `skiller` list is passed explicitly. Fake home: tests pass `kok` temp dirs in `tarama_kokleri` (absolute temp paths), so `~` is never used. Final line: `N/N test geçti`; exit 1 on any failure. Helper `test(ad, kosul, ayrinti="")` prints `✅/❌`.

Cases:
1. `ayar_kontrol`: valid shipped-style config -> no lines; bad date, missing `neden`, unknown program, unknown project key, duplicate folder name -> one UYARI each.
2. `projeleri_bul` unchanged: temp root with 2 lock folders + 1 without -> 2 found; `takipten-cikti` entry removes that project; `projeleri_bul_ham` still returns it.
3. Existing report byte-stability: `rapor_metni` for a fake project set with the new fields present in `ayar` equals the text produced with the old 4-key `ayar` (format unchanged).
4. `kilit_guvenli_oku`: missing / corrupt JSON / list instead of dict -> `(None, "kilit.json okunamıyor: …")`, no exception.
5. `skill_durumu`: one fake skill per branch (`kaynak-yok`, `emekli-kayip`, `emekli-kaynakta-kaldirildi`, `elle-degismis`, `guncelleme-var`, `kurulum-eksik`, `guncel`) returns the expected code and order of precedence.
6. Health: clean fake project -> `temiz`; update available -> `dikkat`; deleted `.agents/skills/<ad>` copy -> `sorun`; hand-edited skill -> `dikkat` listed once (the `DOGRULA_TEKRAR` filter removes dogrula's duplicate).
7. Moved project: lock `proje_yolu` points to another existing parent -> `TAŞINMIŞ`; points to a non-existing parent (`/Users/baska/...`, `C:\x`) -> `BAŞKA YERDEN KOPYALANMIŞ`.
8. `kutuphane` mismatch -> dikkat line.
9. Source gone from library -> `KAYNAK KÜTÜPHANEDE YOK`, counted in `kaynak_yok`.
10. Disk classification: folder in `elle-kurulan.json` -> `elle`; matches `kendi_skilleri` pattern `akil-disi-*` -> `kendi`; folder whose hash equals a fake registry hash -> `KİLİTSİZ KÜTÜPHANE KOPYASI`; other -> `KAYITSIZ SKILL`; `elle-kurulan.json` entry with no folder -> the reverse line. Symlinked `.claude/skills/x` + real `.agents/skills/x` counted once.
11. Kaybolanlar: known project folder deleted -> `KAYIP`; folder exists without lock -> `KİLİT YOK`; same name at another path -> `TAŞINMIŞ görünüyor`; tracked-not-known -> `KAYITLI DEĞİL`; `takipten-cikti` + folder deleted -> no `KAYIP`, listed in `takipte_olmayan`.
12. Scan: temp tree with (a) `a/.claude/skills/s1/SKILL.md`, (b) `b/AGENTS.md` only, (c) nested `c/d/e/.agents/skills/s/SKILL.md` at depth 4, (d) a registered project, (e) `node_modules/x/.claude/skills/s/SKILL.md`, (f) a dot-dir project. Expected: `a` skilli, `b` talimat, `c/d/e` found with depth 4 and NOT found with `derinlik: 3`, `d` and `e`, `f` not reported.
13. Scan never follows links: a symlink `link -> <dir with a skilled project>` is not reported; symlink loop (`x/loop -> x`) does not hang; a symlinked `.claude/skills` is reported as `baglanti`; with `ortak.GLOBAL_KLASORLER` patched to a temp dir, a link into it sets `genel: true`.
14. Scan limits: `en_cok_klasor: 5` on a wide tree stops with `sinira_ulasildi: true` and still returns partial results; run time < 5 s.
15. Ignore list: exact entry and `altini_da` subtree are excluded and listed under `yoksayilan` with reason/date; NFD-spelled path (`unicodedata.normalize("NFD", ...)`) matches an NFC entry; stale entry gives the `bilgi` line. **No-open proof (review correction):** `os.scandir`, `os.lstat` and `os.stat` are patched with recorders; after a scan over a tree that contains an ignored folder `x` with `altini_da: true` (children included, one of them skilled), no recorded path equals or lies under `x`; the folder is still listed under `yoksayilan`. Same for an exact (`altini_da: false`) entry: that folder itself is never opened but its siblings are.
16. `.env` is never opened: a project dir containing a `.env` whose content is the string `GIZLI-DEGER-123` -> the string appears nowhere in any output (`--saglik`, `--tara-kayitsiz`, `--ozet-json`, report file); a spy on `builtins.open`/`Path.read_text` asserts no path ending `.env*` is read.
17. (removed in review: program usage deferred.) Replaced by: `kayitsiz_tarama` and the `KAYITSIZ SKILL` / `kendi_skilleri` / `elle-kurulan.json` classification for a project whose skills dir holds a mix; and the `arac_secimi`/`araclar`-less lock case: a lock without `araclar` field and one with an unknown extra key are read without error and give the `bilgi` line of E.10.
18. Writers (pure `ayar_degistir` and CLI by calling `pk.main([...])` in-process with patched `pk.AYAR`; no env var, no subprocess): dry run changes nothing on disk; `--evet` writes; `--cikar` requires `--neden`, and works on a tracked project that is not yet in `bilinen_projeler` (creates the entry); `--tasindi` updates `yol`, `onceki_yollar`, `ek_projeler`, and a renamed folder renames keys in all three maps (`bilinen_projeler`, `notlar`, `kendi_skilleri`); `--ekle` of a folder with lock outside the scan root adds `ek_projeler` + `bilinen_projeler(tur kilitli)`, of a lock-less folder requires `--neden` and gives `tur: elle`; `--ekle` refuses library/home/global folders; `--yoksay` duplicate/empty neden rejected; two writer flags -> exit 2; writer refused while a fake `guncelleme_suruyor` returns a lock. After every writer test the project temp folders are byte-identical (hash of the tree before/after) and the temp library files other than `projeler.json` are untouched.
19. `--ozet-json`: stdout parses as exactly one JSON object with keys `arac, durum, satirlar, karar_bekleyen` (types checked, `durum` in the three values, `satirlar` <= 15, each <= 160 chars), nothing else on stdout; no file written (temp `notlar/` stays empty) without `--yaz`, report written with `--yaz`.
20. Exit codes, checked through a REAL subprocess (`python3 araclar/proje-kullanimi.py ...` with the temp `projeler.json` selected by running a copy of the script placed in a temp `araclar/` dir next to copies of `ortak.py` and a temp `projeler.json`; `KOK` is derived from the script location so the copy sees only temp data), because in-process `main()` cannot prove the process exit code: `--saglik` on a `sorun` fixture exits 0; with `--siki` exits 1; on a `temiz` fixture with `--siki` exits 0; `--tara-kayitsiz --siki` exits 0 even when skilled unregistered folders exist (level dikkat) and 1 only when the scan itself failed in a way classified sorun (a scanned root that exists but cannot be listed: PermissionError); plain `--kontrol` exits 0 on BOTH a stale and a current report (legacy behaviour kept; the stale case is also checked on a copy of the real report format), `--kontrol --siki` exits 1 on a stale report and 0 on a current one; no-flag report and `--skill` exit 0; unknown writer args exit 2.
21. Report determinism: `--saglik` run twice gives byte-identical `proje-durumu.md`; second run does not rewrite (mtime unchanged); no date/time pattern `\d{4}-\d{2}-\d{2}` appears except in the `Son işlem` column and `yoksay`/`takipten çıktı` dates (assert by regex on the other sections); when no project and no `bilinen_projeler` exists the file is not created.
22. Other-machine guard: config with 5 `bilinen_projeler` and tarama kökü that holds no project -> `hizli_kontrol` returns `[]`, `--saglik` leaves the report file uncreated/untouched and prints the `Hiç proje bulunamadı` line, `--ozet-json` gives `durum: temiz`. (This guards the shipped `projeler.json` on a cloud clone.)
22b. `hizli_kontrol`: empty ayar -> `[]`; known project folder deleted -> one `KAYIP` UYARI; runs < 200 ms and never imports `skill-ekle` (`pk._SE_ONBELLEK[0] is None` afterwards).
23. Cross-check against the real `skill-ekle.durum()` (real `skill-ekle` module with `se.hesap_gizleme_eksik = lambda p, k: []`; fixture files written by the test: `<proj>/.skill-kutuphanesi/kilit.json` = `{"surum":3,"kutuphane":"<tmp>","profil":null,"roller":[],"skiller":{"x":{"id":"x","repo":"o/r","kaynak_yol":"x","commit":"c0ffee1","klasor_hash":"<H>","varyantlar":[],"roller":[],"kurulu_hash":{"codex":"<H>","claude":"symlink"}}},"proje_yolu":"<proj>"}`, `<proj>/.agents/skills/x/SKILL.md` with frontmatter `name: x`, symlink `<proj>/.claude/skills/x -> ../../.agents/skills/x`, `CLAUDE.md` and `AGENTS.md` containing the markers `se.BLOK_BAS`/`se.BLOK_SON`; `<H>` computed with `ortak.klasor_hash`; the fake `skiller` = `[{"id":"x","ad":"x","repo":"o/r","kaynak_yol":"x","klasor_hash":"<H>","commit":"c0ffee1"}]`; variants: change `klasor_hash` in the fake registry -> GÜNCELLEME VAR; edit the SKILL.md -> ELLE DEĞİŞTİRİLMİŞ; drop the fake entry -> KAYNAK KÜTÜPHANEDE YOK): the status label of each skill from `durum()` stdout matches the `skill_durumu` code mapping (güncel / GÜNCELLEME VAR / ELLE DEĞİŞTİRİLMİŞ / KAYNAK KÜTÜPHANEDE YOK).
24. Backward-compat guards, in-process only (D5: no real home, no real `projeler.json`, no 22 MB registry): module still exposes `projeleri_bul, oku, rapor_metni, hesapla, guncel_mi, rapor_guncelle, kullanan_projeler, kisa_yol, AYAR, RAPOR`; with patched `AYAR`/`RAPOR`/`REGISTRY` (a tiny fake `registry.json` in the temp dir) and a temp scan root: `pk.main(["--skill","boyle-bir-skill-yok"])` prints `Hiçbir projede kullanılmıyor.` and writes nothing; `pk.main(["--kontrol"])` returns 0 when the temp report equals `hesapla()` text and 1 after the temp report is altered. The real-CLI equivalents run only in section 10. The entry-point exit behaviour of the legacy modes is proven by test 20 (real subprocess).
25. Safety invariant: a recursive hash of the whole temp "home" (projects, fake global folders) before and after every read-only mode (`--saglik`, `--tara-kayitsiz`, `--ozet-json`) is identical.

---------------------------------------------------------------------------------------------------

## 6 Hand-off requests to other packages

1. **P8 — `araclar/test.py`** (D5): add one section that runs every `araclar/testler/test_*.py` as a subprocess and checks exit 0 and the last line `N/N test geçti`. Nothing else from P5.
2. **P8 — `araclar/dogrula.py`** (after L267 and around L268-274): 
   - add `for u in pk.hizli_kontrol(ayar_p): uyarilar.append(u)` (function is cheap and returns `[]` on machines without these projects; text already starts with `proje takibi:`);
   - extend `adlar_p` (L269) with `set(ayar_p.get("bilinen_projeler", {})) | set(ayar_p.get("kendi_skilleri", {})) | {Path(y["yol"]).name for y in ayar_p.get("yoksay", [])}`; keep the existing length>=5 and skill-name filters;
   - add `"programlar.json"` to the leakage file tuple at L274 (D8 names it explicitly); expected result today: no hit (checked by grep: `programlar.json` contains no project folder names from the new fields);
   - optional: UYARI when `notlar/proje-durumu.md` is missing and projects exist. (P4's monthly summary also makes it fresh.)
3. **P6 — `program-denetim.py`**: no request in the first version (the project-per-program map was deferred, section 8). P6 must not write project names into `programlar.json` (D8).
4. **P4 — `aylik-ozet.py`**: run `python3 araclar/proje-kullanimi.py --saglik --ozet-json --yaz` (one subprocess; `--ozet-json` itself writes nothing unless `--yaz` is given; the JSON is the summary input, `--yaz` refreshes `notlar/proje-durumu.md`); the result also contains the unregistered-folder scan, so P4 needs no second call. Remark for P4: `notlar/proje-durumu.md` is tracked in git and changes only when state changes; P4 decides whether the monthly step commits it (do not let it dirty the tree before `arsiv-guncelle.py --uygula`, which needs a clean tree). `arsiv-guncelle.py:84-100` can stay as is.
5. **P8 — documents**:
   - `promptlar/README.md:20`: replace the description with `Bir skili/kaynağı hangi projeler kullanıyor (silmeden önce etki); aylık proje sağlık turu; proje ekle/çıkar/taşındı/yoksay`.
   - `CLAUDE.md` and `AGENTS.md` ("Bakım isteklerinde"), one bullet, identical in both: `- Proje takibi: aylık ya da "projeleri kontrol et" denince python3 araclar/proje-kullanimi.py --saglik (notlar/proje-durumu.md; salt okuma, kayıtsız klasörleri de tarar). Yeni proje / çıkar / taşındı / yoksay: --ekle, --cikar, --tasindi, --yoksay (yalnız projeler.json değişir, önce plan, onayla --evet). Ayrıntı: rehber/10-proje-kullanimi.md, promptlar/12.`
   - `BASLA.md`: one line pointing to the same command.
   - `README.md:101` (tool table row for `proje-kullanimi.py`): append `· --saglik / --tara-kayitsiz / --ekle / --cikar / --tasindi / --yoksay`.
   - `kapsam-denetimi.py` (if it checks that every tool in `araclar/` is mentioned in README/rehber): nothing new is created by P5 under `araclar/` except the test file; no change expected.
6. **P1 — `skill-ekle.py`** (owner of install flow): (a) keep these names and signatures stable because P5 loads the module: `kilit_oku(proje)`, `dogrula(proje, skiller, sessiz=False)`, `kaynak_bul`, `elle_degismis`, `kurulum_eksik`, `guncelleme_suruyor`, and the status order of `durum()` (cross-checked by test 23; if P1 changes it, update `skill_durumu` and the test together). (b) New tool values in `kilit["araclar"]` are fine: P5 prints them verbatim and judges layout only through `se.dogrula`. (c) If P1 adds a new project skill folder beyond `.claude/skills .agents/skills .cursor/skills .codex/skills .github/skills .gemini/skills`, tell P5 to extend `SKILL_KLASORLERI`. (d) **Accepted from P1 (their request to P5):** (1) `--saglik` reports a `KAYITSIZ SKILL` line for every skill folder in `.agents/skills` / `.claude/skills` (and the other `SKILL_KLASORLERI`) that is not in the lock, in `elle-kurulan.json` or in `kendi_skilleri` (already E.7: accepted, nothing more to build); (2) for a lock whose tool choice is `varsayılan` or that has no `araclar` field a `bilgi` line is printed (accepted, E.10), and a lock without `araclar` is read without error. **Declined / deferred from P5 to P1 (P1's request that `skill-ekle.py` print `BİLGİ: ... --ekle` after an install):** deferred, P1 also declined it; `--saglik` already lists projects outside the scan scope. `proje_raporunu_yenile` must NOT write `projeler.json`. `pk.izleme_kapsaminda_mi` stays available but nobody has to call it. Entry in P1's hand-off section: 'ertelendi: P5 --saglik zaten kapsam dışı projeyi listeler'.
7. **P2 — general-folder emptying**: the scan's `genel_klasore_bagli` flag and `--saglik` can be run before emptying to list projects whose skills dir is a symlink into a machine-wide folder; P2's procedure may cite `proje-kullanimi.py --tara-kayitsiz`. Read-only, no action needed from P2.

---------------------------------------------------------------------------------------------------

## 7 Needs the user's approval

- Approving this package's implementation = approving the shipped `projeler.json` content: two `yoksay` entries (per D10), the five `bilinen_projeler` entries and `kendi_skilleri` for the 8 `akil-disi-*` skills (without it they would show as 8 permanent `KAYITSIZ SKILL` alerts).
- Each real write by the new writers (`--ekle`, `--cikar`, `--tasindi`, `--yoksay`) needs the user's approval at that time (dry-run plan first, `--evet` after a clear yes); P5 itself never decides.
- Deciding what to do with each unregistered skilled folder found by `--tara-kayitsiz` (manage with the library / watch only / ignore): per folder, user decision, at the monthly tour. Initial known set per DURUM.md: IsBasvuruClaude, Yetisio, Tekfen Araştırma Sonuçları, CrmProject2, LinkedinSabanIsBasvurusu, OyleSaniyordukChatGpt, MacBilgisayarTemizleme, Oyak-OrduPazariNew, NewTetraTarim, EtsyEski, Kantin, `Documents/Codex/.../ECommerceProject` (not all will have skill folders). Only the two folders of D10 are pre-ignored; nothing else is pre-decided.
- Any real follow-up (project `--yenile` after a move, `--guncelle` for stale projects, `--kaldir` for orphans, pasting an `elle-kurulan.json` draft into a project) is a separate approval and runs through `skill-ekle.py`/manual paste, not through P5.
- The monthly commit of `notlar/proje-durumu.md` (P4 decides; push only on the user's request, D12).

---------------------------------------------------------------------------------------------------

## 8 Deferred and why

- **Scenario 2 (new project): "CLAUDE.md step 1 does not ask which AI tool the project uses"** is owned elsewhere: P1 (`--arac` selection, `araclar` in the lock, prompts 01/03) and P8 (`CLAUDE.md`/`AGENTS.md` wording). P5 closes the tracking half of scenario 2 only (`--ekle`, `--bilinenleri-yaz`, scope check `izleme_kapsaminda_mi`, `rehber/10` section "Yeni proje izlemeye alma").

- **Writing `elle-kurulan.json` automatically / drafting it (`--elle-taslak`)**: D7 forbids project writes by these tools; the library session adds the entry by hand with the user's approval. A writer would belong in `skill-ekle.py` (P1).
- **Project-level lock against two tools running `skill-ekle` at once (critic scenario 9, first half)**: needs a change in `skill-ekle.py` (P1's file); not designed here. P5 delivers only the detection half: a skill folder added by another tool shows up as `KAYITSIZ SKILL` / `KİLİTSİZ KÜTÜPHANE KOPYASI` on the next `--saglik`.
- **Windows execution of `skill-ekle.py` / running P5 on Windows (scenario 3, third bullet)**: cannot be verified on this Mac; rehber text states "test edilmedi"; copies are treated read-only. The tool itself is pure stdlib and path-handling uses `pathlib`, but no promise is made.
- **Per-tool skill dir semantics (Cursor, Copilot, Antigravity)** beyond "is there a skills dir": layout correctness for those tools belongs to P1 (`--arac`, kilit `araclar`); P5 reports whatever `se.dogrula` says.
- **Tool-correctness of "project really sees the skills in tool X"**: needs launching the tools (no); deferred to P1's duman testi.
- **Moving `tarama_kokleri` discovery deeper than one level for LOCKED projects**: not needed; `ek_projeler` + `--ekle` cover it, and the unregistered scan (depth 4) tells about deeper skilled folders. Changing `projeleri_bul` depth would change the existing report content.
- **Corrupt `kilit.json` crashing the no-flag report** (`oku()` L48): left as is (D2: do not rewrite working code; `skill-ekle.py:1647` and `dogrula.py:281` already catch it). `--saglik` reports it as `KİLİT OKUNAMIYOR` instead. Could be hardened later in a separate small change.
- **Automatic detection of program use inside project files** (grep of `~/.openmontage`, `hyperframes` calls in scripts): would read arbitrary project files (privacy/secrets risk, D9); only kilit-based and elle notes in this package.
- **Deferred in review (reduce the 760-line surface): `--yetim`, `--program`, `--elle-taslak`, `--bilinenleri-yaz`, `--yoksay-kaldir` and the `program_kullanimi` field.** `--yetim` duplicates `--saglik`; the program-to-project map (B7 project side) can be added later without breaking anything (the module and the json ignore unknown keys); until then the facts live in `notlar/hf-om-gecisi/DURUM.md`. Ask again when P6 needs it for `program-denetim.py --oncesi`.
- **P1's request that `skill-ekle.py` print `BİLGİ: ... --ekle` after an install and that `proje_raporunu_yenile` write `projeler.json`**: not done (P1 declined the hand-off and `proje_raporunu_yenile` must never write `projeler.json`, it would dirty the tree). `--saglik` already lists projects outside the scan scope (`KAYITLI DEĞİL`, and the unregistered-folder scan), so nothing is lost; P1 section: 'ertelendi: P5 --saglik zaten kapsam dışı projeyi listeler'.
- **Git status of each project repo** (ahead/behind, dirty): belongs to P3 (`git-durum.py`).
- **Project backups inventory** (`.skill-kutuphanesi/yedek` size/age): belongs to P3 (`yedek-denetim.py`).

---------------------------------------------------------------------------------------------------

## 9 Risks and how the implementer verifies nothing existing broke

| Risk | Mitigation / check |
|---|---|
| `projeleri_bul` filter changes the existing report | Filter is inert without `takipten-cikti` entries. Before editing: `python3 araclar/proje-kullanimi.py --kontrol` (expect `güncel`, exit 0) and `cp notlar/proje-kullanimi.md` hash. After: same `--kontrol` and `sha256` of the file unchanged; run the no-flag report ONLY if the implementer first confirms `git diff --stat notlar/proje-kullanimi.md` is empty afterwards (a rewrite must give the same bytes). |
| Importing `skill-ekle.py` into `proje-kullanimi.py` has side effects | It has none at import (`__main__` guard L1654); lazy import only inside `--saglik`; `dogrula.py`/`arsiv-guncelle.py`/`skill-ekle.py` paths that import `proje-kullanimi.py` never trigger it (`hizli_kontrol` and `rapor_guncelle` do not load it; test 22 asserts). |
| `--saglik` slowness (22 MB registry + hashing + scan of `~/Documents`) | Registry loaded once; scan capped by `en_cok_klasor` and depth; acceptance command 10.5 prints elapsed time; expected well under 2 minutes; if the scan hits the cap the result says so. |
| Scan touches secrets / huge trees / loops | Marker-name checks only, no content reads; dot-dirs, `node_modules`, `Library` etc. never entered; symlinks never followed; tests 13, 14, 16. |
| `se.dogrula` reads `~/.claude/skills/synced` (machine-wide folder) | Read-only; no writes anywhere (D7). Tests patch it. |
| Writers corrupt `projeler.json` | Atomic `json_yaz`; dry-run default; `ayar_kontrol` run on the new object BEFORE writing (refuse to write an invalid file); git revert hint. |
| `projeler.json` new keys break other readers | `dogrula.py:268` reads only `notlar`; `projeleri_bul` reads `tarama_kokleri`/`ek_projeler`; unknown keys ignored. |
| Project-name leakage into registry-like files (rule 6/D8) | P5 writes names only in `projeler.json` and `notlar/proje-*.md`; hand-off 2 extends the leak check; acceptance 10.7 greps. |
| NFC/NFD path mismatch for `Danışman` | `_norm`; test 15. |
| Tracked project in `bilinen_projeler` found under both `~` and absolute forms | Compare via `_norm(resolve)`. |
| Folder-name collisions (two projects, same folder name) | `AYNI AD İKİ YOL` UYARI; not supported (stated in 3.1). |
| Exit codes: the legacy modes always exit 0 (entry point discards `main()`'s value) | NOT changed globally (review): `_CIKIS` module variable set only by the new modes and by `--kontrol --siki`; test 20 proves legacy exits 0 even for a stale report; acceptance 10.3 checks `--kontrol` exit 0 before and after; `test.py:1681` stays green whatever the report state. |
| `dogrula` list parsing relies on message text (`DOGRULA_TEKRAR`, `DIKKAT_DOGRULA`) | Strings are copied from `skill-ekle.py:1405-1411`; test 23 and test 6 guard them; if P1 rewords, those tests fail loudly. |

Implementer's non-regression procedure (all read-only until the last step):
1. Record baseline: `python3 araclar/proje-kullanimi.py --kontrol; echo $?`; `shasum notlar/proje-kullanimi.md projeler.json`; `git status --short`.
2. Implement. Run `python3 araclar/testler/test_p5-proje-takibi.py`.
3. Re-run step 1: `--kontrol` identical output, `proje-kullanimi.md` hash unchanged (the shipped `projeler.json` adds keys, not tracked-project changes).
4. `python3 araclar/proje-kullanimi.py --skill boyle-bir-skill-yok` -> `Hiçbir projede kullanılmıyor.`; `--repo x/y` likewise.
5. `python3 -c "import importlib.util,sys; ..."` check that `skill-ekle.py`, `dogrula.py`, `arsiv-guncelle.py` can still load `proje-kullanimi.py` (the three callers) — `python3 araclar/skill-ekle.py --help` and `python3 araclar/arsiv-guncelle.py --help` print help without error.
6. The full `araclar/test.py` and `dogrula.py` are run by whoever integrates (P8); the P5 implementer is not allowed to edit them but MAY run them once at the end of the integration stage (they write temp dirs only). 

---------------------------------------------------------------------------------------------------

## 10 Acceptance: commands that prove it is done

Run from `/Users/sabanulukaya/Documents/SkillKutuphanesi`.
1. `python3 araclar/testler/test_p5-proje-takibi.py` -> last line `N/N test geçti` (N >= 20), exit 0.
2. `python3 araclar/proje-kullanimi.py --help` lists every new flag; `python3 -c "import json; json.load(open('projeler.json'))"` exits 0; `python3 araclar/proje-kullanimi.py --saglik --ozet-json | python3 -c "import sys,json; d=json.loads(sys.stdin.read()); assert set(d)=={'arac','durum','satirlar','karar_bekleyen'}; print(d['durum'])"` prints one of `temiz|dikkat|sorun`.
3. Backward compatibility: `python3 araclar/proje-kullanimi.py --kontrol` -> `Proje kullanım raporu güncel.` exit 0; `shasum notlar/proje-kullanimi.md` equals the value from before; `python3 araclar/proje-kullanimi.py --skill boyle-bir-skill-yok` -> `Hiçbir projede kullanılmıyor.` `python3 araclar/proje-kullanimi.py --kontrol; echo $?` prints 0 (same as before the change, also when the report is stale); only `--kontrol --siki` can exit 1.
4. `python3 araclar/proje-kullanimi.py --saglik` writes `notlar/proje-durumu.md`; run it again and `shasum` is identical (determinism); the file contains the sections of 4.3; `git status --short` shows only `notlar/proje-durumu.md` (+ the owned files) as new/changed by this step.
5. `python3 araclar/proje-kullanimi.py --tara-kayitsiz` lists the real unregistered skilled folders (at least `IsBasvuruClaude`, `Yetisio`, `Tekfen Araştırma Sonuçları` per DURUM.md), does NOT list `Psikolojik Danışman Sosyal Medya` nor the `KIT` folder (they appear under "Yoksayılanlar" with reason and date 2026-11-11), and does not list the 5 tracked projects. Elapsed time printed by `time` < 2 min. Additionally, with `strace`-free proof: the unit test 15 (recorder on `os.scandir/lstat/stat`) shows the ignored folders are never opened.
6. `python3 araclar/proje-kullanimi.py --saglik` for the real data shows, for `Akil Disi Youtube Kanali`, the 8 `akil-disi-*` as `kendi` (no `KAYITSIZ SKILL` line for them), and the retired `etsy-api-skill` source (if still installed in a project) as `KAYNAK KÜTÜPHANEDE YOK` or `EMEKLİ`.
7. Leak check: `grep -n -E "IstatistikYoutube|Etsy-Arif|Etsy-Yeni|AntigravityTest2|Akil Disi" registry.json kaynaklar.json programlar.json ucret-siniflandirma.json kategori-kurallari.json | head` shows no NEW hit caused by P5 (hits that already existed before are listed in the baseline).
8. Writers, dry run only: `python3 araclar/proje-kullanimi.py --yoksay ~/Documents/Yetisio --neden "deneme"` prints a plan (`PLAN (hiçbir şey yazılmadı…`) and `git status --short projeler.json` shows no change.
9. Read-only proof: `git status --short` before and after the whole acceptance run differs only by `notlar/proje-durumu.md` and the P5-owned files; `ls -la ~/.claude/skills ~/.agents/skills ~/.codex/skills` untouched (the tool never writes there; this is a check by absence).
10. After P8 applied hand-offs 1-2: `python3 araclar/dogrula.py` shows 0 errors and, with a known project folder temporarily absent in a COPY of `projeler.json` (done only in the test, not on the real file), a `proje takibi: KAYIP` UYARI; `python3 araclar/test.py` runs the new section and stays green.

---------------------------------------------------------------------------------------------------

## 11 Review changes

Applied (mandatory):
- **Exit code (mandatory, applied):** the global `sys.exit(main() or 0)` change is REMOVED. Re-checked in the code: `araclar/proje-kullanimi.py:183-184` calls `main()` and discards the value, and `test.py:1681-1682` asserts `returncode == 0` for `--kontrol` on the real library and real projects, so a stale report would have turned that test red (D2). New design (3.2 B and K): module variable `_CIKIS`, set only by the new modes (`--saglik --siki`, `--tara-kayitsiz --siki`) and by `--kontrol` when the new `--siki` flag is also given; legacy no-flag, `--skill`, `--repo`, plain `--kontrol` keep exiting 0. Section 9 risk row, test 20, test 24 and acceptance 10.3 rewritten accordingly.
- **Önkoşul / implementation order** added at the top of the spec (items 0 to 8 of the review text; P5 depends only on P1's `skill-ekle.py` function signatures).

Applied (optional, accepted):
- **Surface reduced:** `--yetim`, `--program`, `--elle-taslak`, `--bilinenleri-yaz`, `--yoksay-kaldir`, the `program_kullanimi` field, `programi_kullanan_projeler`, `program_kullanimi_haritasi` and the "Programlar → projeler" report section are deferred (sections 3.2 G/I/J, 8). Tool size estimate 760 -> about 480 lines; test count N >= 20. Kept: `--saglik`, `--tara-kayitsiz`, `--ozet-json [--yaz]`, `--ekle`, `--cikar`, `--tasindi`, `--yoksay`. The first `bilinen_projeler` memory is shipped literally (5 entries) and `--ekle` / `--cikar` create entries when needed, so `--bilinenleri-yaz` is not needed.
- **Ignored folders are never opened:** the ignore check runs before any `os.scandir`/`lstat`/marker check (3.2 F); test 15 patches `os.scandir`, `os.lstat`, `os.stat` with recorders and asserts no recorded path is the ignored folder or under it.
- **P1 acceptance lines** written into section 6 item 6: `--saglik` unlisted-skill-folder lines accepted (already E.7), `araclar`-less / `varsayılan` lock `bilgi` line accepted (E.10, never an error). P1's `--ekle` BİLGİ request deferred with the sentence 'ertelendi: P5 --saglik zaten kapsam dışı projeyi listeler' (P1 must put it in its own hand-off section).
- Hand-offs adjusted: `dogrula.py` `adlar_p` extension no longer lists `program_kullanimi`; P6 hand-off removed; README row shortened.

Rejected (with reason):
- **Deferring `kendi_skilleri`:** rejected. It is one small `fnmatch` list, and without it the 8 self-written `akil-disi-*` skills of the Akıl Dışı project would appear as 8 permanent `KAYITSIZ SKILL` alerts every month, which the user would have to dismiss each time (noise that hides real findings). Only `program_kullanimi` is deferred.
- **Keeping the scan from reading user folders at all:** a scan of unregistered skilled folders needs to list directory names; that is kept (names only, no file contents, no `.env`), limited by depth and folder cap, with the ignore list applied before any open.

Gaps nobody owned (took none): B2 (candidate triage), `--kayip-isaretle`, the `promptlar/10` '44 tests' line, `rehber/08`, the KAYIP `kayip_tarihi` record, `--hizli` tool staleness, the P6 `--ozet-json` write question, Windows/Gemini note, missing stamp on a fresh clone, the accepted-decisions list in `--ozet-json`, the library path in project blocks: none of these concern the five files P5 owns (they belong to P4, P7, P8, P1, P6 as named in the review). One related remark for P4: P5's `--ozet-json` `karar_bekleyen` lines are stable text, so a shared accepted-decision list can match them verbatim.
