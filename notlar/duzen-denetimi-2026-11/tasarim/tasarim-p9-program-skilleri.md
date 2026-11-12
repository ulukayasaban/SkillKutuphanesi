# P9 design: program skills as links (K-28) and frozen project skills

Status: design only. Two implementers work one after the other: PART A (skill-ekle.py core) first, PART B (tracking, audit, docs on the program side) second.
Language: English prose; every identifier, flag, lock field, code and user-facing string is Turkish exactly as it must appear.
Line numbers refer to the repository state at commit 2956d5701 (before P9). All paths are relative to `/Users/sabanulukaya/Documents/SkillKutuphanesi`.

---------------------------------------------------------------------------------------------------

## 1. Purpose

K-28 (notlar/kararlar.md:39): skills that ship with a program (OpenMontage `.agents/skills/*`, HyperFrames `dist/skills/*`) must not be copied into projects and must always be the installed program's version.

P9 adds two ways for a project to hold a skill that is NOT a library copy:

1. LINK (`tur: "program-bag"`): the project gets a symlink to the program's own skill folder. Single source = the installed program. The library records which project links which program skill, shows broken links, and warns BEFORE a program update which links would break.
2. FROZEN (`tur: "donmus"`): a skill that today exists only in a machine-wide folder (e.g. an older generation skill no program or library source provides any more) is copied once by the tool into the project as the project's own skill and recorded as frozen. The library never updates, repairs or re-reads its source afterwards.

Nothing in P9 installs into a real project or touches machine-wide folders (D9). Real use is a later, separate step.

Decisions D1..D9 from the task are binding. Decisions added here (not in D1..D9) are collected in section 6.1 and again in the structured answer.

---------------------------------------------------------------------------------------------------

## 2. Existing behaviour relied on (with file:line)

skill-ekle.py
- Constants: `META`, `KILIT_SURUM = 3`, `ARACLAR`, `DUZEN_KLASORLERI`, `DUZEN_TALIMAT` (60-66); `ZORLANAMAZ` set (72-73); `ROL_ADI` regex lowercase-only (69) — NOT usable for program skill names (OpenMontage has `video_toolkit`, with underscore), so a new regex is needed.
- `kilit_oku` (200-214) adds defaults and returns the whole dict; unknown top-level keys survive because `kilit_yaz` (217-224) writes the dict as read. This is the backward-compat hook: a NEW top-level key is invisible to old code, while a new entry inside `kilit["skiller"]` would NOT be (every iteration over `kilit["skiller"].values()` assumes repo/commit/klasor_hash fields: 204-205, 1267-1280, 1372, 1390, `proje-kullanimi.py:rapor_metni` 143-156).
- `codex_var` / `duzen_adi` (227-234): layout decided by `kilit["araclar"]`.
- `yedekle(proje, adlar, neden)` (355-380): backs up `.agents/skills/<a>` and `.claude/skills/<a>` for every given name; symlinks are copied as symlinks (`is_symlink` checked FIRST, 361-364), directories with `copytree(symlinks=True)`; keeps last `YEDEK_SAYISI = 10` (70, 378-380). `geri_yukle` (390-404) deletes then restores; `sil_yol` (383-387) unlinks a symlink without following it. These make links safe to back up and restore; they never write through a link.
- `kur` (689-706): ortak layout = real folder `.agents/skills/<ad>` + relative link `.claude/skills/<ad>` made with `os.path.relpath(codex_hedef, claude_hedef.parent)` (703-705); yalniz-claude = real folder in `.claude/skills`, `.agents/skills/<ad>` removed.
- `agent_dosyalari` (717-761): role files; Codex disables every project skill not in the role (`tum = sorted(kilit["skiller"])`, 723, 748-752).
- `blok_yaz` / `blok_sil` (764-781): marked block in CLAUDE.md / AGENTS.md; `talimat_bloklari` (784-819) returns early and DELETES the block when `not kilit["skiller"]` (785-788). Two block variants: `kisa` (790-803) and tam (804-818).
- `hesap_gizleme_hedefi` (825-828) iterates `kilit["skiller"]`.
- `tumunu_yaz` (883-890) = hesap_gizle + kilit_yaz + agent_dosyalari + talimat_bloklari.
- `proje_yapisi_kontrol` (970-993) inspects only the skill directories themselves (`.agents/skills`, `.claude/skills`...), not their children; a child symlink into `~/.openmontage` does not trigger `global-baglanti`.
- `on_kontrol` (1042-1179): existing `projede-kendi-skillin` HATA when a slot exists and is not in the lock (1065-1070); `isim-cakismasi` (1054-1057).
- `onay` (1228-1244): HATA blocks; ZORLANAMAZ codes cannot be forced; `--kuru` returns False (exit 2); UYARI needs `--evet`; BİLGİ never blocks.
- `ekle` (1292-1345), `kaldir` (1348-1376), `guncelle` (1379-1471), `arac_degistir` (1474-1482), `dogrula` (1485-1550), `durum` (1553-1574), `geri_al` (1582-1599), `guvenli_islem` (1283-1289: rollback from backup on exception).
- `kapsam_raporu` (1181-1199) prints a library candidate list even for an empty plan if the project has detectable technologies -> noise for link-only runs.
- `main` (1775-1874): gating expression `(a.profil or a.rol or a.skill or a.planlayici)` appears at: the `gk` update-in-progress check (1798), the `--oner` branch (1792), the `--kuru` branch (1812), the `--yenile/--blok` branch (1819), `--arac` branch (1832), the final `ap.error` (1838). Windows exit message (1787-1789). `--yenile` branch backs up `list(kilit["skiller"])` (1827).
- `proje_raporunu_yenile` (1877-1902) runs only from `__main__`, skips read-only flags, so tests calling `se.main()` never commit anything.

proje-kullanimi.py
- `oku` (99-107), `projeleri_bul` (75-79), `projeleri_bul_ham` (82-96; takes `ayar` as argument, uses module `KOK` only to exclude the library itself).
- `rapor_metni` (117-162): output has no date; `dogrula.py:704-708` and `test.py:1715-1716` require the committed `notlar/proje-kullanimi.md` to equal what the tool would generate NOW. Therefore every addition must produce ZERO new bytes when no project has links/frozen skills.
- `disk_skilleri` (262-280) lists child dirs with `SKILL.md`; `is_dir()` follows symlinks, so linked skills appear as disk skills; `_siniflandir` (443-466) would label any disk skill not in the lock as `KAYITSIZ SKILL` -> must learn the new kinds.
- `proje_denetle` (469-557), `DOGRULA_TEKRAR` (48), `saglik_hesapla` (706-778), `_karar_bekleyenler` (781-799), `ozet_nesnesi` (802-830; max 15 lines), `durum_raporu_metni` (833-888; fixed table columns), `_eski_kipler` (1187-1211), `main` (1141-1184).
- Tests isolate it by assigning module variables `pk.KOK/AYAR/RAPOR/DURUM_RAPORU/REGISTRY` and `pk._SE_ONBELLEK[0] = None` (test_p5-proje-takibi.py:48-58).

program-denetim.py
- `yol_ac(yol, ev)` (66-72) resolves `~`; `git_okuma` (120-127) read-only git wrapper returning stdout or None (note `git cat-file -e` prints nothing and exits 0 -> stdout `""`, so test `is not None`); `_ctx` (795-801) carries `kok`, `ev`, `hedef`, `cevrimdisi`.
- `_kart_sema` (481-): `liste_ok("skilleri", ...)` is at the line after `enum_ok("ucret"...)`; optional fields are silent when absent.
- `oncesi_denetle` (1095-1266): sections S1 sema, S2 kurulu (early return `KURULU DEĞİL` 1155-1157), S3 kart, S4 son (early returns `GÜNCELLENECEK BİR ŞEY YOK` 1166-1168, 1176-1178), then the 8 checks, then `kırıcı`. `hedef_g = hedef or son` (1142).
- `rapor` (1323-1462): per-card loop, tables, `## Kart şeması`, `## Ortam anahtarları`, `## Dikkat`; returns `(out, B, bulgu)` with `B["sorun"|"dikkat"|"satirlar"|"karar"]`.
- `main` (1469-1552): `--oncesi` JSON object built from `S` (1539-1545).
- test_p6-programlar.py mocks `git_okuma`, `gh_api`, urlopen and calls `pd.oncesi_denetle("gp", kart, ctx)` with a temp `ctx.kok` that has NO `projeler.json` (lines 400-406, 539). Hence: absent/empty project data must add NO lines (see B3).

Other
- `ortak.py`: `json_oku` (44), `json_yaz` atomic (51), `klasor_hash` (197), `GLOBAL_KLASORLER` (37).
- `programlar.json`: three cards: etsyotomasyon (`kopya` absent = kaynak, `skilleri: []`), hyperframes (`yerinde.tur npm-global`, `yol /usr/local/lib/node_modules/hyperframes`, `kutuphane_surumu 0.9.35`), openmontage (`yerinde.tur git-checkout`, `yol ~/.openmontage`, `kutuphane_commit fecb9a1e...`). Card `skilleri` is a free text list (hyperframes lists `hyperframes-registry`, which is NOT in `dist/skills`): it is NOT authoritative and P9 never reads it; the real folder is.
- CLAUDE.md == AGENTS.md byte-identical (dogrula enforces).

---------------------------------------------------------------------------------------------------

## 3. Changes per file

### Common contract (both parts)

#### 3.0 Lock format (backward compatible)

New OPTIONAL top-level key `dis_skiller` in `.skill-kutuphanesi/kilit.json`. `KILIT_SURUM` stays 3 (additive). Old code ignores the key (verified by reading: all old paths touch only `kilit["skiller"]`). `kilit["skiller"]` is NOT changed in meaning: it keeps only library skills.

```json
{
  "surum": 3,
  "skiller": { "...": "unchanged library entries" },
  "dis_skiller": {
    "ffmpeg": {
      "ad": "ffmpeg",
      "tur": "program-bag",
      "program": "openmontage",
      "hedef": "/Users/<ev>/.openmontage/.agents/skills/ffmpeg",
      "tarih": "2026-11-12",
      "program_surum": "fecb9a1e3cc23ef84de30b272059457a427f16f8",
      "program_surum_turu": "commit"
    },
    "hyperframes": {
      "ad": "hyperframes",
      "tur": "program-bag",
      "program": "hyperframes",
      "hedef": "/usr/local/lib/node_modules/hyperframes/dist/skills/hyperframes",
      "tarih": "2026-11-12",
      "program_surum": "0.9.35",
      "program_surum_turu": "surum"
    },
    "eski-hf-animasyon": {
      "ad": "eski-hf-animasyon",
      "tur": "donmus",
      "hedef": "/Users/<ev>/.claude/skills/eski-hf-animasyon",
      "tarih": "2026-11-12",
      "icerik_hash": "<ortak.klasor_hash of the copy at freeze time>",
      "dosya_sayisi": 14
    }
  }
}
```
Field rules:
- Key = skill folder name in the project = `ad`.
- `tur` in `{"program-bag", "donmus"}`. Any other value read from disk is ignored by new code with a `dogrula` sorun line `bilinmeyen dış skill türü`.
- `hedef` for a link = ABSOLUTE source path (card `skill_koku` with `~` expanded via `os.path.expanduser`, joined with `ad`, `os.path.abspath` — NOT `realpath`, so that a program update that replaces the folder keeps the link valid). For frozen = absolute original source path as the user gave it (informational only; never read again).
- `program_surum`: for links, the card's recorded version at link time: `kutuphane_commit` when `yerinde.tur == "git-checkout"`, else `kutuphane_surumu`; `null` when the card has neither. `program_surum_turu`: `"commit"`, `"surum"` or `null`. The program is NEVER executed to learn it.
- `kilit_yaz` change: if `kilit.get("dis_skiller")` is empty or missing, the key is removed/not written, so locks of projects without such skills stay byte-identical to today (except the existing `guncelleme` date).
- Helper (new, skill-ekle.py): `dis_kayitlari(kilit) -> dict` = `kilit.get("dis_skiller") or {}` filtered to dict values; used everywhere instead of `kilit["dis_skiller"]`. `kilit_oku` does NOT `setdefault` the key.

#### 3.0b Layout of the two kinds

| | `ortak` | `yalniz-claude` |
|---|---|---|
| link | `.agents/skills/<ad>` = symlink to ABSOLUTE `hedef`; `.claude/skills/<ad>` = relative symlink `../../.agents/skills/<ad>` (same `os.path.relpath` rule as kur, 703-705) | `.claude/skills/<ad>` = symlink to ABSOLUTE `hedef`; `.agents/skills/<ad>` must not exist |
| frozen | real folder `.agents/skills/<ad>` + relative symlink in `.claude/skills/<ad>` | real folder `.claude/skills/<ad>`; `.agents/skills/<ad>` must not exist |

Windows: both options refuse with a plain message (links to a program on this Mac make no sense there).

---------------------------------------------------------------------------------------------------

## PART A — araclar/skill-ekle.py, the test file, rehber/01, rehber/14

### A1. New constants and helpers (near the constants block, skill-ekle.py:56-85)

```python
PROGRAMLAR = KOK / "programlar.json"          # tests may reassign
DIS_TURLER = ("program-bag", "donmus")
DIS_AD = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")   # program skill folder names (video_toolkit has '_')
DONDUR_GIZLI_ADLAR = (".env", "auth.json", "token.json", "credentials.json")   # case-insensitive; also names starting with ".env."
DONDUR_BUYUK_MB = 50
```
Add to `ZORLANAMAZ` (72-73): `"program-skill-bicim", "program-bilinmiyor", "program-skillsiz", "program-kurulu-degil", "program-skill-yok", "program-skill-ad", "dis-ad-cakismasi", "bag-farkli", "bag-degismis", "windows-bag", "dondur-yol", "dondur-kaynak-yok", "dondur-program-skili", "dondur-kutuphane-adi", "dondur-gizli", "dondur-dis-baglanti", "dondur-kendisi", "dondur-ad"`.
(`projede-kendi-skillin` stays forceable as today.)

New functions (all in skill-ekle.py; names Turkish like the rest):

- `dis_kayitlari(kilit)` as in 3.0.
- `yol_goster(p)`: absolute path with the home prefix replaced by `~` (used in blocks and messages; blocks are committed to project repos and must not carry the user's home name).
- `program_karti(program)` -> card dict or None; reads `PROGRAMLAR` with `json_oku`, returns `json["programlar"].get(program)`; tolerant of read errors (returns None).
- `program_skill_koku(kart)` -> `Path | None`: `Path(kart["skill_koku"]).expanduser()` when it is a non-empty string, else None. Relative result (not absolute after expanduser) -> treated as None (error `program-skillsiz` text says "yol mutlak olmalı").
- `program_surumu(kart)` -> `(deger, tur)` as in 3.0.
- `dis_istek_coz(a)` -> `(liste, hatalar)`; `liste` = `[{"tur","ad","program","kaynak": Path,"kart": dict}]`. Parsing `--program-skill X` : split at first `:`; both parts non-empty else HATA `program-skill-bicim` ("`X`: PROGRAM:AD biçiminde yaz, örn. openmontage:ffmpeg"). `--dondur YOL`: `Path(YOL).expanduser()`; must be absolute else HATA `dondur-yol` ("`YOL`: mutlak yol ver (~ kullanılabilir)"). Duplicate names inside one run -> HATA `dis-ad-cakismasi`.
- `dis_on_kontrol(proje, kilit, liste, lib_adlar, rapor)` -> adds the pre-check lines of A3 (below). `lib_adlar` = names that the same run will install as library skills (`adlar.values()`).
- `dis_kur_bag(proje, kilit, ad, hedef)` / `dis_kur_donmus(proje, kilit, ad, kaynak)` / `dis_yerlestir(proje, kilit, rapor_satirlari)` / `dis_sil(proje, kilit, ad)` / `dis_durumu(proje, kilit, ad, k)` / `dis_sorunlari(proje, kilit)` — described in A4-A9.
- `dis_slotlar(proje, kilit, ad)` -> list of `(Path, beklenen)` to inspect.

### A2. Flags (main(), skill-ekle.py:1779-1818)

```
--program-skill PROGRAM:AD [PROGRAM:AD ...]   nargs="+", dest="program_skill"
   help: "programla gelen skili projeye BAĞ ile ver (kopya değil; programın kendi klasörü). Her skil adıyla yazılır; PROGRAM:* yok.
          --profil/--rol/--skill ile aynı çalışmada kullanılabilir. Örn: --program-skill openmontage:ffmpeg hyperframes:hyperframes"
--dondur YOL [YOL ...]                        nargs="+", dest="dondur"
   help: "genel klasördeki (ya da herhangi bir mutlak klasördeki) skili projenin KENDİ skili olarak dondur: araç gerçek içeriği
          bir kez kopyalar, kilide 'donmuş' yazar; kütüphane bir daha güncellemez"
```
Usage rule (documented in `--help` text and rehber/01): put the project path first (both options are `nargs="+"`, like `--skill`).

Gating: add one helper and use it at every place listed in section 2 (`main` gating):
```python
def kurulum_istegi(a, planlayici=True):
    return bool(a.profil or a.rol or a.skill or a.program_skill or a.dondur or (planlayici and a.planlayici))
```
- `gk` check (1798): add `a.program_skill or a.dondur`.
- `--oner` branch (1792): `not (a.profil or a.rol or a.skill or a.program_skill or a.dondur)`.
- 1812 / 1819 / 1832 / 1838: replace `(a.profil or a.rol or a.skill or a.planlayici)` with `kurulum_istegi(a)`. The `ap.error` text becomes `"--profil, --rol, --skill, --program-skill veya --dondur ver"`.
- `a.arac` together with `--program-skill/--dondur` while other skills are installed: existing `arac-karisik` rule (1306-1310) must also count external names in `eskiler` (see A3).

Windows (1787-1789): keep the exit; when `a.program_skill or a.dondur` use instead the message
`"Programla gelen skiller Windows'a bağlanamaz: bağ bu Mac'teki program klasörünü gösterir. Windows'ta açılacak projeler için skill kütüphanenin olduğu Mac'te kurulur (rehber/14 bölüm 5)."`
Defense in depth: `dis_on_kontrol` also emits HATA `windows-bag` with the same text when `windows_mu()` is true (testable by monkeypatching `se.windows_mu`).

No new flag for `--kaldir`, `--yenile`, `--dogrula`, `--durum`, `--guncelle`: they gain behaviour (A5-A9).

### A3. `ekle()` and pre-check (skill-ekle.py:1292-1345)

Order inside `ekle`:
1. existing: kilit_oku, arac handling, `istek_coz` (library part unchanged).
2. NEW: `dis_liste, dis_hatalar = dis_istek_coz(a)`; HATA lines added to `rapor`.
3. existing `on_kontrol(...)` runs with the library plan (an empty plan is fine).
4. NEW `dis_on_kontrol(proje, kilit, dis_liste, set(adlar.values()), rapor)`.
5. `arac_satirlari` unchanged. `eskiler` (arac-karisik) = library names not in this run PLUS `dis_kayitlari(kilit)` names not in this run.
6. `kapsam_raporu` is called ONLY when `plan` is non-empty (link/freeze-only runs must not print library candidates).
7. Print block (exact format):
```
Proje: <yol>
Kurulacak: <n> skill · Roller: <...>                  # unchanged line
  <library lines unchanged>
Programla gelen (bağ): <n>                            # only when n > 0
  openmontage:ffmpeg  -> .agents/skills/ffmpeg -> ~/.openmontage/.agents/skills/ffmpeg  (openmontage fecb9a1e)
Dondurulacak (projenin kendi kopyası): <n>            # only when n > 0
  ~/.claude/skills/eski-hf-animasyon -> .agents/skills/eski-hf-animasyon  (14 dosya, 48 KB)
```
(for `yalniz-claude` the middle column is `.claude/skills/<ad>`). Version in parentheses is `program_surum` shortened to 8 chars for commits, or `sürüm kayıtsız`.
8. `yedekle(proje, list(adlar.values()) + [dis names], "ekle")`.
9. In `islem()` after the library loop and before `tumunu_yaz`: for each item call `dis_kur_bag` or `dis_kur_donmus`, then set `kilit["dis_skiller"][ad] = giris` (3.0). Existing `tumunu_yaz` then writes lock, role files, blocks (A10).
10. Final line: `Tamam: <n> skill, <r> rol · <b> program bağı, <d> donmuş skill · doğrulama: ...` — the extra part `· <b> program bağı, <d> donmuş skill` is printed only when `b + d > 0` (existing runs print exactly what they print today).

Pre-check lines emitted by `dis_on_kontrol` (level, code, message):

HATA (all in ZORLANAMAZ unless noted)
- `program-skill-bicim`, `dondur-yol`: see A1.
- `program-bilinmiyor`: `"{program}: programlar.json'da böyle bir program yok (kartlar: {liste})"`.
- `program-skillsiz`: `"{program}: bu programın skili yok (kartta skill_koku boş ya da yok)"`.
- `program-kurulu-degil`: `"{program}: skill klasörü bu bilgisayarda yok ({yol_goster(skill_koku)}); program kurulu değil ya da taşınmış"`.
- `program-skill-ad`: `"{ad}: geçersiz skill adı (harf, rakam, . _ - içerebilir; / ve .. olamaz)"`.
- `program-skill-yok`: `"{program}:{ad}: {yol_goster(kaynak)} klasörü ya da içinde SKILL.md yok. Programdaki skiller: {ilk 8 ad, sonra '…+N'}"` (listing = names of subfolders that contain SKILL.md; reading names only).
- `dis-ad-cakismasi`: for a name used twice in the run, or equal to a library skill name in `kilit["skiller"]` or `lib_adlar`, or to an existing `dis_skiller` entry of a different kind or different target: `"{ad}: projede başka bir skill bu adı kullanıyor ({neden}); iki tür aynı adı taşıyamaz"`.
- `bag-farkli`: entry exists with `tur=program-bag` but different `hedef`: `"{ad}: zaten {eski_hedef} yoluna bağlı; önce --kaldir {ad}"`.
- `bag-degismis` (on `--kaldir` only, A7): slot exists but is not the symlink the tool made.
- `windows-bag`: see A2.
- `dondur-kaynak-yok`: `"{yol}: klasör ya da içinde SKILL.md yok"`.
- `dondur-program-skili`: `"{ad}: bu skill {program} programıyla geliyor ({yol_goster(gercek_yol)}); dondurma, --program-skill {program}:{ad} kullan (kopya olmasın, program güncellenince kendiliğinden güncel kalsın)"`. Check: `Path(YOL).resolve()` equals or lies under `resolve()` of any card's `skill_koku` (all cards with non-empty `skill_koku`).
- `dondur-kutuphane-adi`: name equals an installed library skill (`kilit["skiller"]` key) or one being installed in this run.
- `dondur-gizli`: `"{ad}: gizli değer taşıyabilecek dosya adı var: {en çok 5 göreli yol}; dondurulmaz (dosya açılmadı)"`. Names compared case-insensitively to `DONDUR_GIZLI_ADLAR` and prefix `.env.`; walk with `os.walk(followlinks=False)`; file CONTENTS are never opened for this check.
- `dondur-dis-baglanti`: a symlink inside the source whose `realpath` is outside the source folder or dangling: `"{ad}: kaynağın içinde klasör dışına giden bağlantı var: {en çok 5}; dondurulmaz"`. Links that resolve inside the source are materialized by the copy.
- `dondur-kendisi`: source resolves inside the target project's own `.agents/skills` or `.claude/skills`.
- `dondur-ad`: folder basename (NOT resolved; the name as given) fails `DIS_AD`.
- `projede-kendi-skillin` (existing code, forceable): a slot `.agents/skills/<ad>` or `.claude/skills/<ad>` exists, is not in the lock, for either kind (message identical to 1066-1069).

UYARI
- `dondur-ad-farkli`: frontmatter `name` of SKILL.md differs from the folder name (use `frontmatter_adi`, 576-579): `"{ad}: SKILL.md içindeki ad ({x}) klasör adından farklı; kopya olduğu gibi alınır, değiştirilmez"`.
- `dondur-buyuk`: total size over `DONDUR_BUYUK_MB`: `"{ad}: {mb} MB; proje deposunu şişirir, gerçekten gerekli mi?"`.

BİLGİ (exactly these, D5)
- `bag-makineye-ozel` (once per run when any link): `"Bağlar bu bilgisayardaki program klasörünü gösterir (mutlak yol). Başka bilgisayarda ve Windows'ta çalışmaz. Bağları ve .claude/skills ile .agents/skills altındaki bağlı klasörleri paylaşılan bir git deposuna koyma (git'e girmesin: .gitignore'a ekle) ya da yalnız bu Mac'te kullan."`
- `bag-programla-guncel` (per link): `"{ad}: {program} programının kendi klasörüne bağlanıyor; program güncellenince kendiliğinden güncel kalır, kütüphane kopyalamaz. Program bu skili kaldırırsa bağ kırılır (program-denetim.py --oncesi {program} önceden söyler)."`
- `bag-surum` (per link): `"{ad}: bağlandığı sürüm {program} {surum_ya_da_'kayıtsız'} (karttaki kayıt; program çalıştırılmadı)"`.
- `bag-var` (idempotent re-run: entry exists, same `hedef`, slots healthy): `"{ad}: zaten bağlı; değişiklik yok"`.
- `dondurma-guncellenmez` (per frozen): `"{ad}: donmuş kopya projenin kendi skilidir; kütüphane onu güncellemez, düzeltmez, kaynağı değişse de izlemez."`
- `dondurma-kopya` (per frozen): `"{ad}: {yol_goster(kaynak)} içeriği gerçek klasör olarak kopyalanacak ({n} dosya, {kb} KB); içindeki göreli bağlantılar gerçek dosyaya çevrilir."`

Exit codes of `ekle`: unchanged (0 ok, 1 doğrulama sorunu, 2 not applied). Note `onay`: none of the new BİLGİ lines require `--evet`; the two UYARI lines above do.

### A4. Creating (functions called from `islem()`)

`dis_kur_bag(proje, kilit, ad, hedef)`:
- `codex = codex_var(kilit)`; `c = proje/.claude/skills/<ad>`, `h = proje/.agents/skills/<ad>`.
- ortak: `sil_yol(h)` (symlink or file only if it is our slot or `--zorla`: `sil_yol` never follows links), `h.parent.mkdir(parents=True, exist_ok=True)`, `os.symlink(str(hedef), h)`; `sil_yol(c)`, `os.symlink(os.path.relpath(h, c.parent), c)`.
- yalniz-claude: `sil_yol(h)`; `c.parent.mkdir(...)`; `sil_yol(c)`; `os.symlink(str(hedef), c)`.
- Never creates anything under the program folder. After creation `assert (c / "SKILL.md").exists()` else raise (guvenli_islem rolls back).

`dis_kur_donmus(proje, kilit, ad, kaynak)`:
- `gercek = kaynak.resolve()`; temp = `<parent>/.{ad}.kurulum-tmp` (same naming as `hazirla`, so the existing `.kurulum-tmp` leftover check in `dogrula` (1537-1541) covers it); `sil_yol(temp)`; `shutil.copytree(gercek, temp, symlinks=False, ignore=shutil.ignore_patterns(".DS_Store"))`; then `sil_yol(final)` and `temp.rename(final)`.
- ortak: final = `.agents/skills/<ad>` then relative link `.claude/skills/<ad>`; yalniz-claude: final = `.claude/skills/<ad>`.
- No content rewriting at all (no `yollari_yerellestir`, no `aciklama_onar`): frozen means as-is.
- Entry: `icerik_hash = klasor_hash(final)`, `dosya_sayisi = len(onemli_dosyalar(final))`.

### A5. `dogrula()` (skill-ekle.py:1485-1550)

After the library loop add (messages are final; they flow into `proje-kullanimi.py --saglik` as "sorun" lines automatically because P5 loops over `dogrula` output, 520-528 there):
- link, target missing or no SKILL.md at `hedef`: `"{ad}: program bağı kırık ({program}: {yol_goster(hedef)} yok ya da içinde SKILL.md yok); program kuruluysa --yenile, program bu skili kaldırdıysa --kaldir {ad}"`.
- link slot missing / not a symlink / wrong target: ortak: `.agents/skills/<ad>` must be a symlink whose `os.readlink` equals `hedef`, and `.claude/skills/<ad>` a symlink resolving to the same real path; yalniz-claude: `.claude/skills/<ad>` symlink with readlink `== hedef`, `.agents/skills/<ad>` absent. Messages: `"{ad}: bağ eksik ya da başka yere gidiyor ({slot göreli yol}); --yenile onarır"`; slot is a real folder: `"{ad}: bağ yerine gerçek klasör var ({slot}); elle değiştirilmiş, --kaldir {ad} ile temizle"`.
- frozen folder missing or no SKILL.md in the real slot: `"{ad}: donmuş skill klasörü yok ya da içinde SKILL.md yok; --geri-al <yedek> ile geri getir ya da --kaldir {ad}"`; frozen layout wrong (ortak but `.claude/skills/<ad>` not a relative symlink to `.agents`, or yalniz-claude with leftover `.agents/skills/<ad>`): `"{ad}: donmuş skill yerleşimi araç düzenine uymuyor; --yenile onarır"`.
- unknown `tur`: `"{ad}: bilinmeyen dış skill türü ({tur})"`.
- Frozen content is NEVER compared with `icerik_hash` (editing a frozen skill is allowed; no 'elle değiştirilmiş' for frozen).
- The block check at 1523-1530 becomes: required when `kilit["skiller"] or dis_kayitlari(kilit)`.
- `tum = set(kilit["skiller"])` (1511) unchanged: role files only ever name library skills.
- `dogrula` exit semantic unchanged (`1 if sorun else 0`, 1858-1859).

### A6. `durum()` (skill-ekle.py:1553-1574)

After the library lines, one line per external skill sorted by name, same column layout `f"  {ad:42s} {kolon2:34s} {isaret}"`:
- link OK: kolon2 = `bağ: {program}`, isaret = `programla güncel (bağ)`. If the lock `program_surum` differs from the card's current recorded version (card read via `program_karti`), append ` · bağlandığında {eski}, kart şimdi {yeni}` (informational; stays "güncel").
- link broken: `BAĞ KIRIK (hedef yok: {yol_goster(hedef)}; --yenile ya da --kaldir {ad})`.
- slot missing: `KURULUM EKSİK/BOZUK (--yenile onarır)`.
- frozen OK: kolon2 = `donmuş`, isaret = `donmuş (kütüphane güncellemez)`; frozen missing: `DONMUŞ KLASÖR YOK (--geri-al <yedek> ya da --kaldir {ad})`.
`durum` prints nothing extra when there are no external skills.

### A7. `kaldir()` (skill-ekle.py:1348-1376)

- `a.kaldir == ["hepsi"]` keeps its meaning: LIBRARY skills only (documented in rehber/01). External skills are removed only by name.
- For each named `ad`: if in `kilit["skiller"]` -> existing path. Elif in `dis_kayitlari(kilit)`:
  - link: check both slots are symlinks created by us (readlink equals `hedef` for the absolute one; relative one resolves to it). If a slot is a real folder or points elsewhere -> HATA `bag-degismis` `"{ad}: {slot} bağ değil ya da başka yere gidiyor; elle değiştirilmiş (--zorla: yedekle ve sil)"` (forceable? NO — it is in ZORLANAMAZ because the slot might hold user data; user removes it by hand). Else BİLGİ `silinecek`: `"{ad} (program bağı; programın kendi klasörüne DOKUNULMAZ)"`.
  - frozen: BİLGİ `silinecek`: `"{ad} (donmuş skill; silmeden önce yedeğe kopyalanır: --geri-al ile dönülür)"` and BİLGİ `dondurma-yedek`: `"Yedekler en son {YEDEK_SAYISI} işlemle sınırlıdır; donmuş kopyayı kalıcı saklamak istiyorsan yedek klasörünü başka yere kopyala."`.
  - Else HATA `kutuphaneden-degil` message extended: `"{ad} bu projeye kütüphaneden, programdan ya da dondurma ile eklenmemiş; dokunulmaz"` (the existing code name and prefix stay).
- `yedekle(proje, hedefler, "kaldir")` receives all names (library + external) -> frozen folder is copied into the usual backup (symlink-preserving).
- In `islem()`: external: `sil_yol` of both slots (never follows links), `del kilit["dis_skiller"][ad]`; ends with `tumunu_yaz`.
- After removal the managed block is rewritten or deleted by `talimat_bloklari` (A10).
- A program folder is NEVER deleted: guard in `dis_sil`: refuse (raise) if the path to delete is not under `proje`.

### A8. `--yenile` (main 1819-1830) and layout switch (`guncelle` with `yapi_degisti`, 1379-1471)

New `dis_yerlestir(proje, kilit)` -> list of message strings; makes the slots of EVERY external skill match the current layout:
- link: if target (`hedef`) has SKILL.md: re-create missing or wrong symlinks per A4 (own symlinks only; if a slot is a real folder -> do not touch, add message `"{ad}: {slot} gerçek klasör; dokunulmadı"`). If `hedef` does not exist: no link is made, message `"{ad}: hedef yok ({yol}); bağ yeniden kurulmadı (program kurulu mu?)"`.
- frozen: layout fix by MOVING the real folder with `os.replace`/`shutil.move` (never copy, never read content): ortak <- yalniz-claude moves `.claude/skills/<ad>` real folder to `.agents/skills/<ad>` and creates the relative link; reverse moves back and removes the `.agents` copy-slot. If the real folder is missing in both places: message `"{ad}: donmuş klasör yok; --geri-al <yedek> ile geri getir ya da --kaldir {ad}"` (cannot be recreated: the library never re-reads the source).
- `--yenile` branch: `yedekle(proje, list(kilit["skiller"]) + list(dis_kayitlari(kilit)), "yenile")`; the lambda becomes `lambda: (tumunu_yaz(proje, kilit, skiller), [print("  ! " + m) for m in dis_yerlestir(proje, kilit)])`. (Order: `dis_yerlestir` first, then `tumunu_yaz`, so the block reflects reality; implementer's choice as long as the final state is identical.)
- `guncelle(..., yapi_degisti=True)` (also reached by `arac_degistir`, 1474-1482): in `islem()` call `dis_yerlestir` before `tumunu_yaz`; the backup list at 1445 uses `list(kilit["skiller"]) + list(dis_kayitlari(kilit))` when `yapi_degisti`. The empty-`.agents` cleanup (1452-1456) then works because moved folders leave `.agents/skills` empty.
- `--kuru` with `--yenile` keeps its one-line behaviour (1812-1815).

### A9. `guncelle()` (non-layout part) and `geri_al()`

- `guncelle` library loop unchanged. After it add ONE info line when external skills exist: BİLGİ `dis-skiller`: `"{b} skill programla güncel (bağ), {d} donmuş (kütüphane güncellemez): bunlar güncellenmez"`, and one UYARI `bag-kirik` per broken link (`"{ad}: program bağı kırık ({yol}); --yenile ya da --kaldir {ad}"`). External skills never enter `degisen` and are never printed as `guncellenecek`. The return code logic (`1383`-style `1 if HATA`) is unchanged.
- `geri_al` (1582-1599): `adlar = set(kilit["skiller"]) | set(dis_kayitlari(kilit)) | {names from backup targets}` so the pre-restore backup covers them.

### A10. Managed block (D6), `talimat_bloklari` (skill-ekle.py:784-819), `agent_dosyalari`, `hesap_gizle`

- `talimat_bloklari`: early-return condition becomes `if not kilit["skiller"] and not dis_kayitlari(kilit)` (block deleted only when NOTHING remains).
- Block text additions (both `kisa` and tam variants), appended after the existing text, each only when non-empty. Linked line:
  `Programla gelen skiller (bağ; kopya değil, programın kendi klasörü; program güncellenince kendiliğinden güncel kalır): \`ad\` (program, ~/.openmontage/.agents/skills/ad), ...`
  Frozen line:
  `Donmuş skiller (projenin kendi kopyası, kütüphane güncellemez; kaynak: ~/.claude/skills/ad, 2026-11-12): \`ad\`, ...`
  plus one fixed sentence when links exist: `Bağlı skillerin dosyalarını düzenleme (programın dosyaları); donmuş skiller projenindir.`
  Paths go through `yol_goster`.
- When there are NO library skills the profile line and the table header are omitted: the block is the heading `## Proje skilleri (SkillKutuphanesi)` plus the lines above plus the existing last paragraph (layout sentence + `skill-ekle.py --guncelle` hint). In `kisa` mode the count sentence is omitted in that case.
- When there are no external skills the block text is byte-identical to today (regression criterion).
- `agent_dosyalari` unchanged: external skills are not role-bound (section 6). `tum` (723) stays library-only; Codex role `.toml` files do not disable external skills.
- `hesap_gizleme_hedefi` (825-828): iterate `set(kilit["skiller"]) | set(dis_kayitlari(kilit))` so an account skill with the same name as a linked/frozen skill is hidden in the project like library ones (`hesap_cakismasi` info line for them is NOT added; the settings.json mechanism is reused as is).
- `yedekle` (355-380) needs no code change: it already takes names. `kilit_yaz` change per 3.0.

### A11. Test file `araclar/testler/test_p9-program-skilleri.py` (PART A part)

Pattern: copy the header of `test_p1-arac-destegi.py` (1-90): temp dir, `HOME` -> temp, `se` loaded with `spec_from_file_location`, `se.canli_global = lambda s: {}`, `se.hesap_skilleri = lambda: {}`, `se.guncelleme_suruyor = lambda: None`, `se.registry = lambda: SAHTE_KAYIT`, `calistir(*args)` wrapper around `se.main()` with `sys.argv`, `yeni_proje()`, `agac()` tree snapshot. Add:
- `se.PROGRAMLAR = TMP / "programlar.json"` (fake card file with two cards: `fakeprog` git-checkout-like with `skill_koku` = absolute `TMP/"program"/"skills"`, `kutuphane_commit` "abc1234def", and `hfaketest` with `skill_koku` = `~/prog2/skills` under the fake HOME and `kutuphane_surumu` "1.0.0"; plus `bossprog` with `skill_koku: ""`).
- Fake program folder `TMP/program/skills/{ffmpeg,video_toolkit,hyperframes-x}/SKILL.md` (+ a subfile) and a fake machine-wide folder `TMP/home/.claude/skills/{eski-skill (real folder with SKILL.md), takma (symlink into the fake program folder), gizli-skill (has `.env`), ...}`.
- Helper `agac_hash(dir)` for before/after comparisons of the fake program folder and the fake machine-wide folder (they must be byte-identical after every operation).
- `se.windows_mu` monkeypatch for the Windows test.
- Last two lines exactly as in P1: `print(f"{gecen}/{len(SONUC)} test geçti")`, `sys.exit(0 if gecen == len(SONUC) else 1)`. The file ends with a marker comment `# === PART B tests are appended below this line, above the final summary ===` so the second implementer inserts there (the summary block must stay last).

The A test cases are listed in section 5 (A-series).

### A12. rehber/01-skill-ekleme-sureci.md and rehber/14-yapay-zeka-araclari.md (PART A docs)

rehber/01: insert two sections AFTER "Araç düzeni: hangi araç neyi görür" and BEFORE "Kaldırma / geri alma":

`## Programla gelen skiller: bağ` — contents: why (K-28); command `python3 araclar/skill-ekle.py <proje> --program-skill openmontage:ffmpeg hyperframes:hyperframes --kuru` then `--evet`; project path FIRST; every skill named explicitly (`PROGRAM:*` yok); source = `<skill_koku>/<ad>` from the program card; layout table (3.0b); lock key `dis_skiller` (example); what `--durum/--dogrula/--guncelle/--kaldir/--yenile` do for links (A5-A9); "bağ makineye özeldir, git'e koyma, Windows'ta çalışmaz"; "program güncellenince önce `python3 araclar/program-denetim.py --oncesi <program>` bağları gösterir" (cross-ref rehber/11); `--kaldir hepsi` kütüphane skillerini kaldırır, bağlara ve donmuşlara adla bakılır; roles do not apply to links.
`## Dondurma` — `--dondur <yol>`; when to use (yalnız bir genel klasörde kalmış ve hiçbir program ya da kütüphane kaynağının vermediği skill); refused cases (list of codes `dondur-*` with one-line meaning); frozen is never updated; `--kaldir` backs up first, backups keep only the last 10 operations; example.
Also fix the sentence at the top "Genel klasörlerdeki (...) skiller bu araçla yönetilmez" -> add: "Programla gelen skiller bağ ile, yalnız genel klasörde kalmış eski skiller dondurma ile projeye alınır (aşağıda)."
Also update the example "Örnek 3 — AI medya projesi" sentence: "Raporda `bagimlilik` uyarısı çıkar..." stays; add one line pointing at `--program-skill` for OpenMontage/HyperFrames skills.
Also the project tree in Örnek 1 gets one comment line: `└─ (bağlı program skilleri .claude/skills/<ad> -> ../../.agents/skills/<ad> -> program klasörü)`.

rehber/14: section 4 diagram gains two lines under both layouts (`<program-skill>  (bağ -> program klasörü)` and `<donmuş-skill>/  (gerçek, projenin kendi skili)`); section 5 (Windows/kopyalama) gets: "Bağlı program skilleri başka bilgisayarda ya da Windows'ta çalışmaz (mutlak yol); git'e konursa Windows'ta düz metin dosyasına döner. Donmuş skiller gerçek klasördür, kopyalanabilir."; section 10 (Bilinen sınırlar) gets one bullet "Program skilleri bağdır: araç düzeni seçimi (ortak/yalniz-claude) bağın yerini değiştirir ama içeriği hiç kopyalamaz".

---------------------------------------------------------------------------------------------------

## PART B — programlar.json field, program-denetim.py, proje-kullanimi.py, rehber/10, rehber/11, promptlar/13, BASLA.md, CLAUDE.md + AGENTS.md

PART B depends on the lock contract in 3.0 only (reads `kilit["dis_skiller"]` as plain JSON); it must not import anything new from skill-ekle.py except what proje-kullanimi already loads lazily.

### B1. programlar.json (D1)

Add `skill_koku` (string) to the three cards, as the first key after `skilleri`:
- `openmontage`: `"skill_koku": "~/.openmontage/.agents/skills"`
- `hyperframes`: `"skill_koku": "/usr/local/lib/node_modules/hyperframes/dist/skills"`
- `etsyotomasyon`: `"skill_koku": ""`
Also (text only, no project names): hyperframes card `giris_yolu.hepsi.nasil` (line ~156) currently says skills are installed with `--skill <kimlik>`: change to `"Skiller projeye KOPYA olarak değil, BAĞ ile verilir: python3 araclar/skill-ekle.py <proje> --program-skill hyperframes:<ad> (skill klasörü kartta skill_koku). CLI her araçta aynı komuttur."`. Add one step to `guncelleme_adimlari` of hyperframes and openmontage, inserted right after the `--oncesi` step: `"bağlar: program-denetim.py --oncesi çıktısındaki 'bağlar' satırlarını oku; 'bağ kırılacak' ya da HATA varsa kullanıcıya söyle (güncellemeden sonra aynı rapor kırık bağı HATA gösterir)"`. Keep existing steps untouched (the schema requires a step containing `program-denetim.py --oncesi`).

### B2. program-denetim.py schema (D1)

In `_kart_sema` (481-), directly after `liste_ok("skilleri", ...)`:
- absent -> silent (optional).
- present and not `str` -> `H("skill_koku", "metin olmalı (boş metin = programın skili yok)")`.
- non-empty and neither absolute nor starting with `~/` -> `H("skill_koku", "mutlak yol ya da ~/ ile başlamalı")`.
- non-empty, valid, and `yol_ac(v, ev).is_dir()` false for a `yerinde` card -> `U("skill_koku", "bu bilgisayarda yok (program kurulu mu?)")` (UYARI, not HATA: other machines). For `ev` the function `sema_denetle(..., ev=...)` already receives `ev`; thread it to `_kart_sema` through a closure/argument only if the existing signature allows, else use `yol_ac(v)` (which honours `_EV`).
- `'<DOLDUR>'` handling stays as is (`_dolu`).
- `iskelet()` (764-792) is NOT changed (test_p6 compares skeleton shapes; implementer verifies); the field is documented in rehber/11 "Kart şeması (v2)".

### B3. program-denetim.py link checks (D7)

New helpers (module level):
- `proje_baglari(ctx)` -> `list[dict]` each `{"proje": ad, "yol": Path, "skill": ad, "program": p, "hedef": str, "surum": str|None, "tur_surum": str|None}` for every `dis_skiller` entry with `tur == "program-bag"` in registered projects. Projects found as: load `ctx.kok / "projeler.json"` with `json_oku` (missing file -> `[]`, any exception -> `[]`); load `proje-kullanimi.py` lazily with `importlib` (same pattern as skill-ekle.py:1882-1885) and call `pk.projeleri_bul(ayar)` (it takes `ayar` as an argument, so no module patching; `~` in `tarama_kokleri` follows the real/test `HOME`); read each `kilit.json` with `json_oku` inside try/except (bozuk kilit -> skipped). Result is cached per call of `rapor`/`oncesi_denetle` (compute once; pass through `ctx` attribute `baglar` set lazily: `getattr(ctx, "_baglar", None)`).
- `bag_hedef_var(b)` -> `os.path.isfile(os.path.join(b["hedef"], "SKILL.md"))` (reads nothing).
- `repo_goreli_skill_yolu(p, ctx, ad)` for a git-checkout card: `os.path.relpath(yol_ac(p["skill_koku"], ctx.ev), yol_ac(y["yol"], ctx.ev))` + `/ad/SKILL.md`; if it starts with `..` -> None.

`oncesi_denetle` (1095): add two blocks. Both emit NOTHING when `proje_baglari` returns no link for this program (keeps test_p6 line sets unchanged; also nothing when `ctx.kok/projeler.json` is missing).
1. "bağlar şimdi": placed right AFTER the `şema` lines and BEFORE `if not kurulu:` (so it appears in every result including `KURULU DEĞİL` and `GÜNCELLENECEK BİR ŞEY YOK`):
   - all targets exist: `("TAMAM", "bağlar", "{n} bağ, hepsi çözülüyor (projeler: {adlar}; skiller: {ilk 8})")`
   - each broken: `("HATA", "bağlar", "{proje}: {skill} bağı kırık (hedef yok: {yol_goster(hedef)})")` (one line per broken link, max 10 then a summary `…+N kırık bağ daha`). HATA counts as `engel` -> `HAZIR DEĞİL` in the main path. Rationale: broken links must be visible in BOTH before and after states ("After an update the same report shows broken links as HATA", D7) and are cheap to fix (`skill-ekle.py <proje> --yenile` or `--kaldir`).
2. "bağ kırılacak": placed after `S += giris_kontrol(p, ctx)` / `S += gizli_kontrol(p, ctx)` (before the `# 8. kırıcı` block), only in the main path (so only when there IS something to update) and only when `hedef_g` is known and not equal to `kurulu`:
   - `git` card: if `git_okuma(yol, "cat-file", "-e", f"{hedef_g}^{{commit}}") is None` -> one line `("BİLGİ", "bağlar", "hedef commit yerel depoda yok (git fetch yapılmaz); bağların kırılıp kırılmayacağı bilinmiyor")`. Else for each link whose program is this card: `git_okuma(yol, "cat-file", "-e", f"{hedef_g}:{goreli}")` is None -> `("UYARI", "bağlar", "bağ kırılacak: {proje}: {skill} ({hedef_g[:8]} sürümünde {goreli_klasor} yok)")`; all present -> `("TAMAM", "bağlar", "{n} bağın hedefi {hedef_g[:8]} sürümünde de var")`. `goreli` None -> `("BİLGİ", "bağlar", "skill_koku depo dışında; bağ kırılacak mı bilinmiyor")`.
   - `npm-global` / other: `("BİLGİ", "bağlar", "paket indirilmeden hedef sürümdeki skill klasörleri bilinemez; güncellemeden sonra bu raporu yeniden çalıştır: kırık bağ HATA görünür")`.
   - Never calls `git fetch`, never reads outside `git cat-file -e`/`rev-parse`. Update `git_okuma` docstring to list `cat-file -e` as an allowed read.
`main` `--oncesi` JSON object needs no change (it maps every S line).

`rapor` (1323): after the existing `## Dikkat` block append (only when at least one link exists for any card):
```
## Programla gelen skiller (bağlar)

| Program | Proje | Skill | Hedef var mı | Bağlandığı sürüm |
|---|---|---|---|---|
| openmontage | <proje> | ffmpeg | evet | fecb9a1e |
```
and per program `B["satirlar"].append(f"{ad}: {n} bağ, {k} kırık")`; if `k > 0`: `B["sorun"].append(f"{ad} {k} kırık bağ")`, `dikkat_bloku` gets `- {ad} · bağ kırık: {proje}/{skill}` lines (so they appear in `## Dikkat` — insert the block before `## Dikkat` is built; simplest: compute links before `out` is assembled). `B["karar"]` gets `f"{ad}: {k} kırık bağ -> skill-ekle.py <proje> --yenile ya da --kaldir"`. With no links the report is byte-identical to today (acceptance).

### B4. proje-kullanimi.py (D7)

Rules: no new bytes in `notlar/proje-kullanimi.md` / `notlar/proje-durumu.md` when no project has external skills (the committed reports must still match, test.py:1715 and dogrula.py:704-708).

1. `rapor_metni` (117-162):
   - Summary table: Skill cell stays `len(k.get('skiller', {}))`; when the project has external skills append ` (+{b} bağ, {d} donmuş)` inside the same cell.
   - Per-project section: after the library table and the `elle` line, when external skills exist add `Programla gelen (bağ): \`ad\` (program), ...` and `Donmuş (projenin kendi kopyası): \`ad\`, ...` as two plain lines (same style as the existing "Kütüphane dışı, elle kurulan:" line, 154-155).
   - At the END (just before the final `s.append("")`, 161): when any link exists, add `## Programla gelen skiller → projeler` with table `| Program | Skill | Projeler |`, sorted by program then skill. Nothing otherwise. The returned `kullanan` dict (library only) is unchanged.
2. `_siniflandir` (443): callers pass `kilitteki = set(kskill) | set(dis_adlari)`; so external disk skills are never `KAYITSIZ SKILL` / `KİLİTSİZ KÜTÜPHANE KOPYASI`. Helper `dis_kayitlari(kilit)` duplicated locally (3 lines; do not import skill-ekle just for it).
3. `proje_denetle` (469-557): `sayac` gets keys `program_bag`, `donmus`, `bag_kirik` (initialised to 0 in the dict at 472-473 — all code uses `.get`, so extra keys are safe). After the library skill loop: count per kind; frozen: one `("bilgi", "donmuş skill (kütüphane güncellemez): ad1, ad2")` line per project; link health is NOT recomputed here: it comes from `se.dogrula` lines (A5), which the existing loop at 520-528 already turns into `("sorun", x)`; increment `bag_kirik` for each such line containing `program bağı kırık`. Add the new dogrula marker strings to nothing in `DOGRULA_TEKRAR` (they must be reported).
4. `durum_raporu_metni` (833): after `## Projeler` table add, only when any project has `program_bag + donmus > 0`, a section `## Programla gelen ve donmuş skiller` with `| Proje | Bağ | Donmuş | Kırık bağ |` table. Columns of the existing table are NOT changed (the `Skill (kilit/klasör)` folder count includes linked and frozen folders — documented).
5. `_karar_bekleyenler` (781): per project with `bag_kirik`: `f"{p['ad']}: {n} kırık program bağı -> skill-ekle.py \"{p['ad']}\" --yenile (program kuruluysa) ya da --kaldir <ad>"`.
6. `ozet_nesnesi` (802): when totals > 0 append one line `f"PROGRAM BAĞI: {b} bağ ({k} kırık), {d} donmuş skill"` (stays within the 15-line cap; existing lines unchanged). `durum` becomes `sorun` automatically through the project `sorun` lines.
7. New option `--program AD` (argparse in `main`, 1141-): prints, for every tracked project (via `oku(ayar)`), each external entry of that program:
   `"{proje}: {skill} — program bağı ({program} {surum_ya_da_'sürüm kayıtsız'}) · hedef {var|YOK}"`; none -> `"Hiçbir projede bu programın bağı yok."`. Read-only; exit 0. It also accepts `--siki`: exit 1 if any target is `YOK` (set `_CIKIS`). Not combinable with writers (`--ekle` etc.): reuse the existing combination error at 1166-1169 by adding `a.program` to the list of read modes.
8. `--skill <ad>` / `--repo` (1187-1211): additionally match external entries by NAME for `--skill`: line `"{proje}: {ad} — programla gelen (bağ: {program})"` / `"{proje}: {ad} — donmuş (projenin kendi kopyası)"`. The no-result text `"Hiçbir projede kullanılmıyor."` stays (test.py:1717-1720).
9. `--saglik` exit codes, `--ozet-json`, `GUVENLIK_SATIRI` unchanged. Module docstring gets the new `--program AD` line.

### B5. rehber/10-proje-kullanimi.md

- Table at the top: `notlar/proje-kullanimi.md` row text adds "programla gelen (bağ) ve donmuş skiller"; `kilit.json` row adds "(`skiller` + `dis_skiller`)".
- "Kullanım" block: add `python3 araclar/proje-kullanimi.py --program <ad>  # bu programın skillerine bağlı projeler (hedef var mı)`.
- Replace the section "Programlar hangi projede (ilk sürümde otomatik değil)" with "Programlar hangi projede": link records live in each project's lock (`dis_skiller`); `--program`, the new report sections, `--saglik` lines (`program bağı kırık`, donmuş skill bilgisi); program-denetim shows the same links before/after updates (rehber/11). The sentence "Program kartlarına proje adı yazılmaz (kural 6)" stays.
- "Projenin kendi yazdığı ve elle kurulan skiller": add one paragraph: frozen skills are recorded in the lock, therefore never `KAYITSIZ`.

### B6. rehber/11-program-yonetimi.md

- "Nerede ne var" (8-18): add row for `skill_koku`.
- New section after "Takip ve güncelleme": `## Programla gelen skiller ve projelerdeki bağlar`: K-28 rule; card field `skill_koku`; how projects get links (`skill-ekle.py --program-skill`, rehber/01); the two audit points (before: `--oncesi` lines `bağlar`, `bağ kırılacak`; after: same report, HATA); what to do on a broken link (`skill-ekle.py <proje> --yenile` if the program is installed; `--kaldir <ad>` if the program dropped the skill; ask the user); program removed => all its links break: list them first with `proje-kullanimi.py --program <ad>` (replaces the "(`--program` bayrağı ... eklenirse)" remark in "Programı çıkarma (A) step 1: change to use `--program <ad>` directly).
- "Güncellemeden önce: ön kontrol (--oncesi)" (176-192): add control 9 `bağlar` (see B3) and the sentence "Hiç bağ yoksa satır görünmez".
- "Taze ajan: istek → adımlar" (255-): in each program's UPDATE steps: before approval, "`proje-kullanimi.py --program <ad>` ve `--oncesi` 'bağlar' satırları kullanıcıya söylenir"; after the update, "`program-denetim.py --oncesi <ad> --cevrimdisi` ve `program-denetim.py`: 'bağlar' satırlarında HATA olmamalı; olursa projeye göre `--yenile`/`--kaldir` için kullanıcıya sor". (Implementer reads the existing step lists first and adds one line per program; no other step text changes.)
- "Kart şeması (v2)" (81-104): document `skill_koku` (optional string; boş = skill yok; `~/` ya da mutlak; sema UYARI when folder missing).
- "Kurallar" first bullet: "Program kopyası proje deposuna konmaz" + add "programın skilleri projeye kopyalanmaz, bağ verilir".

### B7. promptlar/13-program-kur-guncelle.md

Add after step 3: `3b. python3 araclar/proje-kullanimi.py --program [PROGRAM]  → bağlı projeler; --oncesi çıktısındaki 'bağlar' satırları ('bağ kırılacak' varsa bana söyle).` After step 8: `8b. Güncellemeden sonra program-denetim.py yeniden: 'bağlar' satırlarında HATA kalmamalı; kırık bağ için bana sor (--yenile ya da --kaldir).` Keep the rest verbatim.

### B8. BASLA.md (section 3 table, 66 lines)

- Row "Şu projeye skill kur": append in the last column: ` Programla gelen skiller (OpenMontage/HyperFrames) kopyalanmaz: \`--program-skill PROGRAM:AD\` (bağ); yalnız genel klasörde kalmış eski skiller \`--dondur <yol>\` (donmuş).`
- Row "HyperFrames / OpenMontage / başka program": append ` Güncellemeden önce ve sonra projelerdeki bağlar: \`python3 araclar/proje-kullanimi.py --program <ad>\`.`
- Row "Projeleri kontrol et": append `; bağ ve donmuş skiller \`--saglik\`te görünür`.

### B9. CLAUDE.md + AGENTS.md

Add ONE bullet in "Bakım isteklerinde", directly after the "Programlar (skill olmayan yapılar ...)" bullet:
`- Programla gelen skiller (K-28): OpenMontage ve HyperFrames skilleri projeye KOPYALANMAZ; \`python3 araclar/skill-ekle.py <proje> --program-skill PROGRAM:AD --kuru\` ile programın kendi klasörüne BAĞ verilir (kart: \`skill_koku\`), kilit: \`dis_skiller\`. Yalnız genel klasörde kalmış eski skill \`--dondur <yol>\` ile projenin kendi skili olarak dondurulur (kütüphane güncellemez). Program güncellemesinden önce ve sonra \`python3 araclar/proje-kullanimi.py --program <ad>\` ve \`program-denetim.py --oncesi <ad>\` ('bağlar' satırları); ayrıntı: \`rehber/01\`, \`rehber/11\`.`
Then `cp CLAUDE.md AGENTS.md` and `cmp CLAUDE.md AGENTS.md` (must print nothing). The user approved pointer lines for these two files; no other edit to them. Do not touch Kesin kurallar 1-6.

### B10. Test file (PART B part)

Append inside `test_p9-program-skilleri.py` above the final summary (marker from A11). Cases in section 5 (B-series). Use the `test_p6-programlar.py` mocking style for `git_okuma`/`gh_api` when needed, but for the git case create a REAL temp git repo (`git init`, two commits with `-c user.name=t -c user.email=t@t`, in the temp dir only) so `cat-file -e` is exercised for real; record every git argument vector through a wrapper and assert none contains `fetch`, `pull`, `clone`, `checkout`, `switch`.

---------------------------------------------------------------------------------------------------

## 4. User-facing texts (index)

All final strings are in section 3 (codes and messages). Fixed terms used everywhere: `bağ` (link), `programla güncel (bağ)`, `donmuş (kütüphane güncellemez)`, `program bağı kırık`, `bağ kırılacak`, `bağlar` (the check name in `--oncesi`), `Programla gelen skiller (bağlar)` (report heading), `Programla gelen ve donmuş skiller` (durum heading), `Dondurulacak (projenin kendi kopyası)`, `Programla gelen (bağ)`.
`--help` strings: A2. Windows message: A2. Block lines: A10.
Messages never contain the user's home directory name: use `yol_goster`.

---------------------------------------------------------------------------------------------------

## 5. Tests (araclar/testler/test_p9-program-skilleri.py)

A-series (PART A implementer; temp dirs only; `se.PROGRAMLAR`, `se.registry`, `HOME` faked; fake program folder and fake machine-wide folder hashed before and after EVERY test):
- A1 `--program-skill` with `--kuru`: exit 2, `[kuru]` printed, project tree unchanged, output has `bag-makineye-ozel`, `bag-programla-guncel`, `bag-surum`.
- A2 ortak apply: `.agents/skills/x` is a symlink with ABSOLUTE target equal to fake program folder; `.claude/skills/x` relative link `../../.agents/skills/x`; `(link/SKILL.md).exists()`; lock `dis_skiller` has exactly the 3.0 fields with correct `program_surum`/`program_surum_turu` (commit for the git-like card, surum for the other); `kilit["skiller"] == {}`; CLAUDE.md and AGENTS.md block contain the `Programla gelen skiller` line with `~`-shortened path and no `/Users` text; `--dogrula` exit 0; exit code 0.
- A3 yalniz-claude (`--arac yalniz-claude` in the same run as the first install): only `.claude/skills/x` absolute link, no `.agents`, only CLAUDE.md block.
- A4 error codes, nothing written (tree unchanged, exit 2): unknown program (`program-bilinmiyor`), empty `skill_koku` (`program-skillsiz`), card folder missing (`program-kurulu-degil`), skill missing / without SKILL.md (`program-skill-yok`, message lists existing names), bad format `foo` (`program-skill-bicim`), names `../x`, `a/b`, `.x`, 70-char name (`program-skill-ad`); underscore name `video_toolkit` accepted. Also `--zorla` does NOT override any of them.
- A5 one run mixing `--skill alfa` (library) and `--program-skill fakeprog:ffmpeg`: both present, lock has both kinds in separate keys, `--durum` shows `alfa ... güncel` and the link line `programla güncel (bağ)`; Codex role files (with `--rol-adi r --skill alfa`) do not mention the link; block lists both.
- A6 name clash: library skill and link with the same name in one run -> `dis-ad-cakismasi`; link named like an installed library skill; frozen named like a link; duplicate names in one run.
- A7 idempotence: second identical run -> `bag-var`, exit 0, tree and lock `dis_skiller` identical except dates; changed target (edit card path) -> `bag-farkli`.
- A8 Windows: monkeypatch `se.windows_mu = lambda: True`: `main` exits with the Windows text for `--program-skill` and `--dondur`; no writes.
- A9 `--dondur` real folder: copied as real folder (not symlink), content equal, `.DS_Store` ignored, lock `tur=donmus` with `icerik_hash` and `dosya_sayisi`; `--durum` line `donmuş (kütüphane güncellemez)`; editing the frozen file then `--guncelle`/`--dogrula`: no 'elle değiştirilmiş', not in `degisen`; fake source folder unchanged.
- A10 `--dondur` through a symlink in the fake machine-wide folder that points INTO the fake program folder -> `dondur-program-skili` naming `--program-skill`; source without SKILL.md; name equal to installed library skill; folder with `.env` / `Auth.JSON` / `.env.local` -> `dondur-gizli` and the file content was never opened (use a file whose content is a unique marker and assert the marker is not in the output); inner symlink to outside / dangling -> `dondur-dis-baglanti`; inner symlink to inside is materialized; relative YOL -> `dondur-yol`; source inside the target project -> `dondur-kendisi`; frontmatter name differs -> UYARI `dondur-ad-farkli` (needs `--evet`).
- A11 `--dogrula`: program folder removed -> sorun `program bağı kırık`, exit 1; slot replaced by real folder -> `bağ yerine gerçek klasör`; frozen folder deleted -> `donmuş skill klasörü yok`; healthy -> exit 0; `--durum` shows `BAĞ KIRIK` / `DONMUŞ KLASÖR YOK`.
- A12 `--kaldir <link>`: both slots gone, lock entry gone, block updated/removed, fake program folder byte-identical; slot replaced by a real folder -> `bag-degismis`, nothing deleted (also with `--zorla`). `--kaldir <frozen>`: backup holds the folder copy, folder gone; `--geri-al` restores folder, links and lock. `--kaldir hepsi` leaves external skills in place. Unknown name -> `kutuphaneden-degil`.
- A13 `--yenile`: deleted link slots are re-created; missing program target -> message `hedef yok`, no dangling link created; frozen folder missing -> message `donmuş klasör yok`; `--yenile --kuru` writes nothing.
- A14 layout switch with `--arac yalniz-claude` and back (`arac_degistir` path): links re-laid, frozen real folder MOVED (inode/content preserved, byte-equal), `--dogrula` clean after each, no empty `.agents` left in yalniz-claude.
- A15 `--guncelle`: external skills never printed as `guncellenecek`; info line `dis-skiller`; broken link gives UYARI `bag-kirik` and does not change `degisen`.
- A16 block rules: project with only external skills has a block; removing the last one deletes the block while user text outside the block is preserved; no external -> block text byte-identical to the pre-P9 output (compare against a reference produced by calling `talimat_bloklari` on a lock without `dis_skiller`).
- A17 backward compat: a lock file without `dis_skiller` is read and rewritten WITHOUT the key; `kilit_oku` of a lock with the key leaves `kilit["skiller"]` semantics untouched; a hand-written old-format lock still passes `--durum`/`--dogrula`.
- A18 safety: `proje_yapisi_kontrol` still HATA `global-baglanti` when `.claude/skills` itself is a symlink into the (faked) `~/.openmontage`; a link CHILD into the program folder does not trigger it; `--geri-al` of an install removes links and restores the previous lock; `sil_yol` never writes into the program folder (hash check).
- A19 `hesap_skilleri` mocked to `{"ffmpeg": ...}`: `.claude/settings.json` skillOverrides gets the hide entry for the linked name.
- A20 existing real folder in the slot not recorded in the lock -> `projede-kendi-skillin`; with `--zorla` replaced after backup.

B-series (PART B implementer):
- B1 `--sema`: `skill_koku` absent silent; non-string HATA; relative path HATA; valid but folder missing UYARI; empty string valid; `<DOLDUR>` handling unchanged; real `programlar.json` still `--sema --siki` exit 0 after the three fields are added.
- B2 `oncesi_denetle` with fake projects (fake `projeler.json` in `ctx.kok`, `tarama_kokleri` absolute temp dir, projects created by running `se.main` from the A fixtures or by hand-writing locks): no links -> output identical to baseline (assert equality of the S list with and without `projeler.json`); links healthy -> `TAMAM bağlar`; target removed -> `HATA bağlar` and sonuç `HAZIR DEĞİL`; also in the up-to-date case (`GÜNCELLENECEK BİR ŞEY YOK` path) the HATA line is present.
- B3 git program: real temp repo; commit 1 has `skills/a/SKILL.md` and `skills/b/SKILL.md`, commit 2 removes `skills/b`; clone path = the repo as `yerinde.yol`, `skill_koku` inside it; `--hedef <commit2>` with links to `a` and `b` -> `UYARI bağ kırılacak` for `b` only, `TAMAM` for `a`; target commit not in object store (fake sha) -> `BİLGİ hedef commit yerel depoda yok`; assert no network and no mutating git command was issued (argument recorder).
- B4 npm-global card: `BİLGİ bağlar ... indirilmeden` line appears only when a link exists and a target is known.
- B5 `rapor()` normal run: no links -> report text byte-identical to baseline; with links -> new section, `B["satirlar"]`, `B["sorun"]` for broken, `B["karar"]`; `--ozet-json` shape unchanged (keys) and `durum` `sorun` when broken; `--siki` exit 1.
- B6 `proje-kullanimi`: `rapor_metni` with locks without external -> output byte-identical to a baseline string produced by the pre-change function copy embedded in the test (golden string for a tiny fixture); with external -> summary cell suffix, per-project lines, end section; `kullanan` dict unchanged.
- B7 `_siniflandir`/`proje_denetle`: linked and frozen disk skills not `KAYITSIZ`; frozen -> one `bilgi` line, project stays `temiz`; broken link -> `sorun` line from `dogrula`, `sayac["bag_kirik"] == 1`; `durum_raporu_metni` section only when present; `ozet_nesnesi` extra line only when present and within 15 lines; `_karar_bekleyenler` entry.
- B8 `--program AD`: lists links with `hedef var/YOK`; unknown program -> `Hiçbir projede bu programın bağı yok.`; `--siki` exit 1 when a target is `YOK`; combined with `--ekle` -> exit 2 error; `--skill <ad>` finds external by name; `--skill yok-boyle` still prints `Hiçbir projede kullanılmıyor.`
- B9 docs/consistency: `cmp CLAUDE.md AGENTS.md`; BASLA.md and CLAUDE.md mention `--program-skill`, `--dondur`, `--program`; no project name (read `projeler.json` names) appears in `programlar.json`.

The file's last line is `N/N test geçti`; exit 0 only if all pass.

---------------------------------------------------------------------------------------------------

## 6. What stays out and why

- `PROGRAM:*` (all skills of a program): rejected by D2; every skill is named so the project state is explicit and reviewable.
- Role binding of linked/frozen skills (`--rol-adi`, role `.md`/`.toml`): not in D1..D9; roles are a library concept built on library metadata (`onyuklenebilir`, `skill_md_kb`, `kaynak_bul`). Linked skills are visible to all agents of the project; Codex role files do not disable them. A later step can add it.
- Refreshing, repairing or diffing frozen skills; re-freeze from the source: against the decision ("never updated by the library"). Re-freezing = `--kaldir` then `--dondur`.
- Auto-fix of broken links by pointing at another skill, renaming, or fetching: out; the tool reports and asks.
- Fetching, cloning, `git fetch`, npm calls to predict skill folders of the target version: forbidden for the audit (it only uses the clone's existing object store; npm packages cannot be inspected before install).
- Real cards for new programs, `iskelet()` changes, a `program_kullanimi` section in `projeler.json`: not needed (the lock is the single source, rule 6 stays).
- Any install into the real projects, any change to machine-wide folders, emptying `~/.claude/skills`: D9 (separate step, rehber/12 and K-24/K-25).
- Windows support for links: impossible by nature (absolute Mac path, symlinks).
- Making `--kaldir hepsi` remove external skills: could delete user-owned frozen data by surprise; names are explicit.

### 6.1 Decisions taken beyond D1-D9
1. New top-level lock key `dis_skiller` (NOT entries inside `skiller`), because every existing loop over `kilit["skiller"]` assumes library fields.
2. Link `hedef` is `abspath`, not `realpath`.
3. `DIS_AD` regex allows `_`, `.` and uppercase (program skill names), unlike `ROL_ADI`.
4. Broken-now links are HATA in `--oncesi` and the report (also before an update), per D7's "after an update ... HATA" and to keep one rule.
5. When no project links the program, NO extra lines at all (keeps test_p6 and the committed reports stable).
6. `--kaldir hepsi` = library skills only.
7. External skills are not role-bound and are not disabled in Codex role files.
8. `kapsam_raporu` skipped for link/freeze-only runs.
9. Frozen copy ignores only `.DS_Store`, refuses outside-pointing links and secret-like file names, never rewrites content.
10. Backups hold the frozen copy but rotate at 10 operations; user is told.
11. PART B reuses `pk.projeleri_bul(ayar)` instead of duplicating project discovery.
12. Hyperframes card text and two `guncelleme_adimlari` steps are edited (text only).

---------------------------------------------------------------------------------------------------

## 7. Risks and how the implementer proves nothing existing broke

| Risk | Proof |
|---|---|
| Old lock readers choke on the new key | A17; plus read the grep list: every access is `kilit["skiller"]`; run `python3 araclar/testler/test_p1-arac-destegi.py` (uses real lock read/write) |
| Reports drift (committed `proje-kullanimi.md` / `proje-durumu.md` / `program-denetimi.md` stop matching) | B5/B6 byte-identity tests; at the end the orchestrator runs `python3 araclar/proje-kullanimi.py --kontrol --siki` and `python3 araclar/dogrula.py`; `git diff --stat notlar/` must show no change from the tools |
| `talimat_bloklari` change alters existing blocks | A16 reference comparison; test.py block tests |
| Symlink children followed by backup/restore/removal and writes land in the program folder | `yedekle` checks `is_symlink` first, `sil_yol` unlinks links; A12/A18 hash-compare the fake program folder after every operation |
| `argparse` prefix matching / nargs swallowing the project path | project path first in all docs; `--help` text; test calls pass the project first |
| main() gating forgotten in one of six places | A1-A3 exercise `--kuru`, apply, `--arac` combination, update-in-progress (`se.guncelleme_suruyor` mocked to return a dict -> BEKLE exit) |
| test_p6 expectations on `oncesi_denetle` line sets | B2 no-link equality; run test_p6 unchanged |
| test_p5 expectations on `proje_denetle`/`ozet_nesnesi`/`durum_raporu_metni` | extra keys/lines only when present; run test_p5 unchanged |
| `test.py` / `dogrula.py` / `kapsam-denetimi.py` check docs and card hygiene (project names in cards, AGENTS.md identical) | run them in section 8 |
| Frozen content backup lost by rotation | documented; `dondurma-yedek` info line |
| Real HOME or real program folder touched by tests | tests set `HOME` to temp, never import the real `programlar.json` (override `se.PROGRAMLAR`; pass `--kart/--kok/--ev` to program-denetim), assert nothing created under real `~` |

Implementers must read, before editing, the existing tests that cover the touched functions: `araclar/testler/test_p1-arac-destegi.py`, `test_p5-proje-takibi.py`, `test_p6-programlar.py`, and the skill-ekle and proje-kullanimi sections of `araclar/test.py` (1255-1720), and must not edit them (only add the new test file).

---------------------------------------------------------------------------------------------------

## 8. Acceptance commands

Run from `/Users/sabanulukaya/Documents/SkillKutuphanesi` after each part.

After PART A:
```
python3 -m py_compile araclar/skill-ekle.py
python3 araclar/skill-ekle.py --help | grep -E "program-skill|dondur"
python3 araclar/testler/test_p9-program-skilleri.py          # last line: N/N test geçti, exit 0 (A-series)
python3 araclar/testler/test_p1-arac-destegi.py              # unchanged result
python3 araclar/testler/test_p3-yedek-git.py
python3 araclar/testler/test_p5-proje-takibi.py
python3 araclar/testler/test_p8-butunluk.py
python3 araclar/test.py                                      # full end-to-end (allowed for the implementer; uses temp projects)
python3 araclar/kapsam-denetimi.py                           # 0 sorun
python3 araclar/dogrula.py                                   # 0 hata
```
After PART B:
```
python3 -m py_compile araclar/program-denetim.py araclar/proje-kullanimi.py
python3 araclar/program-denetim.py --sema --siki             # exit 0
python3 araclar/program-denetim.py --oncesi openmontage --cevrimdisi   # no new lines (no real links exist)
python3 araclar/program-denetim.py --oncesi hyperframes --cevrimdisi
python3 araclar/proje-kullanimi.py --kontrol --siki          # report still current
python3 araclar/proje-kullanimi.py --program openmontage     # "Hiçbir projede bu programın bağı yok."
python3 araclar/proje-kullanimi.py --saglik --ozet-json      # shape unchanged
python3 araclar/testler/test_p9-program-skilleri.py          # all A and B cases, last line N/N test geçti
for t in p1-arac-destegi p2-genel-bekci p3-yedek-git p4-aylik p5-proje-takibi p6-programlar p7-kaynak-yasam p8-butunluk; do python3 araclar/testler/test_$t.py | tail -1; done
python3 araclar/test.py | tail -3
python3 araclar/kapsam-denetimi.py ; python3 araclar/dogrula.py
cmp CLAUDE.md AGENTS.md && echo ayni
git status --short                                           # only the files named in PART A/B (orchestrator commits)
```
The orchestrator (not the implementers) commits, and applying links/freezes to real projects is a later, separate step (D9, K-28, K-29: user is notified and tests OpenMontage/HyperFrames updates in his own project).

---------------------------------------------------------------------------------------------------

## Uygulama notları (PART A, 2026-11-12)

PART A uygulandı (skill-ekle.py, araclar/testler/test_p9-program-skilleri.py A serisi, rehber/01, rehber/14). Tasarımdan sapmalar ve eklemeler (tasarım eleştirmeninin zorunlu düzeltmeleri dahil):

1. Kilit anahtarı doğrulaması: `dis_kayitlari` yalnız geçerli kayıtları verir (anahtar `DIS_AD.fullmatch`, `ad == anahtar`, tür bilinen, `hedef` mutlak metin, bağda `program` metin). Geçersizler hiçbir yol bileşeninde kullanılmaz; `dogrula` "geçersiz dış skill kaydı" / "bilinmeyen dış skill türü" yazar.
2. Bağ hedefi kilitten değil karttan türetilir (`dis_bag_hedefi`: `skill_koku/ad`, abspath). `dogrula`, `durum`, `--yenile`, `--guncelle` bunu kullanır. Kilitteki hedef karttakinden farklıysa `dogrula` söyler, `--yenile` yeni hedefe bağlayıp kilidi günceller. Kart yoksa bağ kurulmaz ve mesaj verilir; `--kaldir` yine de çalışır (slot, kilitteki ya da karttaki hedefe giden bağsa silinir). `--kaldir` argümanı `dis_ad_gecerli` değilse `kutuphaneden-degil`.
3. `DIS_AD` `fullmatch` ile kullanılır; `.kurulum-tmp` ile biten ad geçersiz; çakışma denetimi büyük/küçük harf duyarsız (`casefold`). `--program-skill` adı kırpılmaz (satır sonlu ad reddedilir). Mesajdaki ".. olamaz" yerine "ilk karakter harf ya da rakam olmalı" yazıldı.
4. Dondurma kopyası: kaynak içindeki her klasör bağı reddedilir; dosya bağları yalnız hedefi kaynak içinde bir normal dosyaysa (ve gizli/atlanan klasörde değilse) kabul edilir ve gerçek dosyaya çevrilir; FIFO/soket HATA (`dondur-ozel-dosya`); sert tavan 200 MB ya da 5000 dosya (`dondur-cok-buyuk`, ZORLANAMAZ), 50 MB üstü UYARI. Boyut ve dosya sayısı kopyadan ÖNCE `os.walk`/`lstat` ile hesaplanır (dosya içeriği açılmaz). `node_modules`, `__pycache__`, `.venv`, `.DS_Store` kopyalanmaz (son üçü dışında BİLGİ `dondurma-atlanan`). `.git`, `.aws`, `.ssh`, `.gnupg` klasörleri gizli sayılır (`dondur-gizli`, kopyalanmaz; tasarımdaki "ya HATA ya say" seçeneğinden HATA seçildi).
5. Gizli dosya adı listesi genişletildi (büyük/küçük harfsiz): `.env`, `.env.*`, `.envrc`, `.npmrc`, `.netrc`, `.pypirc`, `.git-credentials`, `auth.json`, `token.json`, `credentials.json`, `credentials`, `id_rsa*`, `id_ed25519*`, `secrets.*`, `service-account*`, `client_secret*`, `*.pem`, `*.key`, `*.p12`, `*.pfx`, `*.keystore`. `dondurma-kopya` BİLGİ metni "içerik taranmadı; proje deposuna koymadan önce dosyaları gözden geçir" der.
6. Kütüphane skili sonradan aynı adla istenirse (dış bayrak olmadan) `on_kontrol` `dis-ad-cakismasi` verir (ZORLANAMAZ; `projede-kendi-skillin` o slotlar için çıkmaz). `dis_on_kontrol` liste boş olsa da çalışmaz ama `on_kontrol` koşulsuz bu denetimi yapar.
7. `kapsam_raporu` yalnız `plan` boşken VE dış istek (`--program-skill`/`--dondur`) varken atlanır; diğer her çalışmada çıktı eskisiyle aynıdır (test 36, P9 öncesi `2956d5701` sürümüyle karşılaştırır).
8. Git: proje bir git deposuysa bağ yolları `git check-ignore -q` (salt okur) ile sınanır; ignore edilmiyorsa UYARI `bag-git-izlenir` (`--evet` ister). Araç proje `.gitignore`'una yazmaz.
9. Gürültü azaltıldı: program başına tek `bag-programla-guncel` satırı (bağ sayısı, ilk 6 ad, sürüm, kırılma uyarısı); `bag-surum` ayrı kod olarak yok (sürüm aynı satırda). `bag-var` da tek satır.
10. `windows-bag` ön kontrol kodu ve `dis_on_kontrol` dalı yapılmadı (ulaşılamaz); `main`'deki çıkış iletisi `--program-skill`/`--dondur` varken Windows'a özel metni verir.
11. Donmuş `--kaldir`: kopya klasörün `klasor_hash`'i kilitteki `icerik_hash`'ten farklıysa UYARI `dondurma-degismis` (`--evet` ister); aynıysa yalnız BİLGİ. Aynı donmuş ad tekrar istenirse BİLGİ `dondurma-var` (kopyalanmaz). Donmuşta `dogrula` içeriği karşılaştırmaz.
12. `kilit_yaz` anahtarı yalnız önceden varsa ve boşaldıysa siler (hiç olmamışsa yazmaz). Test 26 dolu anahtarın kilit_oku/kilit_yaz döngüsünde korunduğunu sınar.
13. Eklenen kodlar: `dondur-ozel-dosya`, `dondur-cok-buyuk`, `dondur-gizli` (genişledi), `bag-git-izlenir`, `dondurma-var`, `dondurma-atlanan`, `dondurma-degismis`, `dis-skiller`, `bag-kirik`. ZORLANAMAZ: tasarımdaki liste eksi `windows-bag`, artı `dondur-ozel-dosya`, `dondur-cok-buyuk`.
14. Kilit giriş `tarih` bağda ilk kurulumda yazılır; tekrar çalışmada (`bag-var`) kayıt değişmez.
15. Test dosyası: A serisi 47 test; PART B testleri `try` bloğunun sonundaki işaret yorumunun altına eklenir (özet bloğu en sonda kalır). Test 36 P9 öncesi `skill-ekle.py`'yi `git show 2956d5701:...` ile geçici dosyaya okuyup aynı sahte projelerde çıktı/kilit/ağaç karşılaştırır.
16. PART B için not: bağın hedefi kilitte `hedef` alanında mutlak yoldur ama doğruluk kaynağı kartın `skill_koku`'dur; program-denetim.py kilitten `hedef` okurken aynı kuralı (kart + ad) uygulamalıdır. Eleştirmenin PART B'ye ait zorunlu maddeleri (1: `bağlar` satırı HAZIR DEĞİL sebebi olmamalı, KURULU DEĞİL/güncelleme bekleyen durumda UYARI) ve opsiyonel `--hedef -x` düzeltmesi burada uygulanmadı.
