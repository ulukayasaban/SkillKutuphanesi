# P8 Giriş belgesi, kurallar, kararlar ve kontrol bütünlüğü (entegratör) — tasarım

Package key: `p8-butunluk`. Spec language English; identifiers and user-facing strings in Turkish as they will appear.

**Önkoşul (uygulama sırası, tüm paketler için bağlayıcı):** (0) commit edilmemiş `programlar/` işinin commit'i (kullanıcı onayıyla; duman temiz ağaç ister); (1) P3; (2) P1; (3) P2, P5, P6; (4) P7; (5) P4; (6) **P8 = bu paket, en son** (paylaşılan dosyalar, eşitlik denetimi, bayrak denetimi); (7) CLAUDE/AGENTS Yama B ayrı commit ve onay; (8) ancak sonra genel klasör boşaltması (rehber/12). P8'in gerçek doğrulaması P1-P7'nin hepsi indikten sonra yapılır: `ortak.OZET_ARACLARI`, `BASLA.md` bayrakları ve `dogrula.py` kontrolleri onların dosyalarına ve bayraklarına bakar. Bir paket henüz inmemişse ilgili kontrol UYARI verir, çökmez.

**Birleştirme kuralı (tek cümle, tüm paketlere uygulanır):** `dogrula.py`'de P8'in eklediği ve diğer paketlerin istediği her yeni denetim yalnız UYARI'dır; HATA yalnız (a) var olan bir JSON kayıt dosyasının ayrıştırılamaması ve (b) `CLAUDE.md` ile `AGENTS.md`'nin eşit olmamasıdır; "eksik dosya HATA", "`--sema` HATA", "G-* HATA" gibi tüm istekler bu kurala göre UYARI'ya çevrilmiştir (neden: `arsiv-guncelle.py --birlestir` dogrula HATA'sında master'ı geri alır, yeni bir belge denetimi aylık birleştirmeyi geri sarmamalı).

Design date 2026-11-11. Read-only design: nothing in the library was edited. One slip is recorded in section 9 (an accidental `arsiv-guncelle.py --help`, stopped, verified to have written nothing).

---------------------------------------------------------------------------------------------------

## 1 Purpose

P8 is the last package. It owns the shared files that every other package needs touched (D5, D6) and turns the audit's "documents and checks" gaps into something a hafızasız session can follow in any AI tool.

Closes:
- **A5** rule contradictions and stale documents: rule 1 exception (single text, separate patch, approval), programs line corrected, stale top-level documents shelved or refreshed, `CLAUDE.md == AGENTS.md` check (HATA), old-wording check.
- **A6** fresh-agent entry: `BASLA.md`, `notlar/kararlar.md`, one-line pointers in `CLAUDE.md`/`AGENTS.md`, session-start routine (`aylik-ozet.py --hizli`).
- **A7** duman test and dirty-tree mismatch: duman fingerprint wording, one shared skip list, the one known emekli-role warning accepted by a small local filter inside duman only (no shared accept list), `--kirli-ok`.
- **B2 (dogrula part)** report staleness: NOT in `dogrula.py` (review). The table and a pure function live in `ortak.py` for the monthly summary (P4) to show; `dogrula.py` never warns about report age.
- **B8 (dogrula part)** `kaynaklar.json` basic schema and P7's new-record gates, all UYARI. (`--siki` is not delivered, review.)
- **B9 (dogrula part)** `yapay-zeka-araclari.json` basic schema (P1's real shape: a list), UYARI.
- **Critic scenario 7** (library session lost its memory): decisions from the Claude-only memory move into the repo.
- **B2 triage question** ("ayda en çok kaç aday karara bağlansın, N"): written into `notlar/kararlar.md` "Henüz sonuçlanmamış sorular" (P7/P4 both deferred it to P8).
- **Shared "kabul edilen bekleyenler" list**: `notlar/kararlar.md` gets the two sections P4's `aylik-ozet.py` reads (`## Karar bekleyenler`, `## Kabul edilen bekleyenler (aylık özette susturulur)`), so a closed decision of any report tool does not come back every month.
- **Unowned documents taken** (file list extended, see 3.11 and section 11): `promptlar/10-kutuphane-saglik-kontrolu.md` line 8 (old "44 güvenlik testi" count) and a paragraph in `rehber/08-test-sureci.md` about `araclar/testler/`.
- **Windows note** in `BASLA.md` (`skill-ekle.py` does not run on Windows) and "the monthly tool-document check runs in full mode only".
- **GEMINI.md**: deferred by D1; optional stub text and an optional check that runs only if the file exists.

Also delivers: the shared loader for `araclar/testler/` (D5), the hand-off intake format (D6), and a single place for the "report tool" list (`OZET_ARACLARI`) that duman and P4 share.

Non-goals: no new report tool, no edit of any file P8 does not own, no real change outside the library (D7). Everything that changes `CLAUDE.md`, `AGENTS.md`, moves a document, or changes a rule is listed in section 7 and needs the user's yes at that time.

---------------------------------------------------------------------------------------------------

## 2 Existing behaviour relied on (file:line)

Checked on 2026-11-11 (`git status` clean, 10 commits ahead of origin, `programlar/*` tracked now).

| Fact | Where |
|---|---|
| `CLAUDE.md` and `AGENTS.md` are byte-identical (57 lines each, `diff` empty). No tool checks it. | `CLAUDE.md`, `AGENTS.md`; `grep AGENTS.md araclar/*.py` empty (akis-09) |
| Rule 1 forbids writing `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage` without exception | `CLAUDE.md:7-8` |
| Programs line says "sabit sürüm kopyası", but HyperFrames/OpenMontage cards are `kopya: yerinde` | `CLAUDE.md:51`; `programlar.json` keys (`kopya`, `yerinde`); `araclar/test.py:1495-1506` |
| `README.md` says global folders "değişmez" and old agents keep using them; names only Claude Code + Codex | `README.md:3-4, 6-7`; same stale sentence `rehber/01-skill-ekleme-sureci.md:12` (P1's file) |
| README lists rehber 1-10 only (rehber/11 exists), says "11 prompt" (there are 12) | `README.md:73-82, 71` |
| README "Gönderilmeyenler" and restore block | `README.md:52, 53-57` |
| `promptlar/README.md` rows are ordered 10, 12, 11 | `promptlar/README.md` table (row 12 before row 11) |
| Rule text in prompts "dokunulmaz" for global folders | `promptlar/README.md:24` (mine), 01:28, 02:25, 03:22, 07:46, 09:12, 11:26, 12:21 (others') |
| `dogrula.py` output contract: warnings first, errors next, last line `N skill · N hata · N uyarı`; exit 1 only on `hatalar` | `araclar/dogrula.py:281-286` |
| `dogrula.py` has no argparse, flags read with `"--github" in sys.argv` | `araclar/dogrula.py:231` |
| Emekli-rol warning that makes duman red | `araclar/dogrula.py:119-120` |
| dogrula already does flag/code checks for prompt 11 by reading `skill-ekle.py` source (string match, never executes) | `araclar/dogrula.py:186-198` |
| Project block: `adlar_p` and the file tuple for rule-6 leakage | `araclar/dogrula.py:268-278` |
| `programlar.json` is not mentioned in `dogrula.py` | grep (akis-11 #5) |
| `dogrula.py` is run by the monthly chain at two places and `--birlestir` reverts master on its failure | `araclar/arsiv-guncelle.py:80, 214, 254-256`; rehber/02 |
| duman: clean tree, `dogrula --github`, "0 hata" and "0 uyarı" parsed from the summary line | `araclar/duman-testi.py:61-63, 70-72` |
| duman fingerprint skips `synced`, `.system`, covers `GLOBAL_KLASORLER` only; test.py fingerprint additionally covers `~/.openmontage/.agents/skills` | `duman-testi.py:44-53`; `araclar/test.py:32-41` |
| duman compares git status to the baseline `kirli` in later steps (so a dirty tree only matters at step 1) | `duman-testi.py:81, 90, 144` |
| duman step 10 text: "global skill klasörleri değişmedi" | `duman-testi.py:143` |
| `GLOBAL_KLASORLER` (claude, codex, agents) is also used by skill-ekle security refusal and `global_durum`; must stay as is (D2) | `araclar/ortak.py:37-41`; `araclar/test.py:1652` |
| `test.py` ends: `test("global klasörler test boyunca DEĞİŞMEDİ", parmak_izi() == once)`, cleanup, `N/N test geçti`, exit | `araclar/test.py:1689-1693` |
| `test.py` `once = parmak_izi()` at start of `main()` | `araclar/test.py:1072-1073` |
| Many tools have no argparse: dogrula, duman-testi, arsiv-guncelle, github-skill-listesi, konu-takip, github-trend, katalog-uret, kapsam-denetimi, gelistirici-bilgisi, arsiv-yerlestir, listeye-ekle, skill-ekle's siblings; `--help` on them RUNS the tool (observed: `arsiv-guncelle.py --help` started the report and hung) | `grep -L argparse araclar/*.py`; `arsiv-guncelle.py:272-281` uses `sys.argv` |
| `TEST_RAPORU.md` is a generated file at the root: written by `skill-calistir.py`, linked from README and `skill-readme.py` | `araclar/skill-calistir.py:44`, `araclar/skill-readme.py:121`, `README.md:30`, `arsiv-guncelle.py:211-213` |
| `PLAN.md`, `Kullanılacak Promt Örneği.md`, `notlar/yerel-yapilacaklar-2026-11.md` have no inbound links (grep over md/py/json outside `arsiv/` and `registry.json`: only a self-reference `PLAN.md:159`) | grep 2026-11-11 |
| Existing shelf precedent: `notlar/hf-om-gecisi/rafta/` | directory listing |
| Report notes carry their date in the first lines: `github-trend.md` "son tarama 2026-11-09", `populer-skiller.md` "2026-11-04", `program-denetimi.md` "2026-11-11", `kapsam-denetimi.md` "2026-11-11", `TEST_RAPORU.md:3` "Tarih: 2026-11-05"; `konu-takip.md` has no date in the first lines | `sed -n` of each |
| `kaynaklar.json`: `repolar` list of 181, every record has `repo` and `tip` (T1-T6, KAYIP); `not`, `oncelik` optional | read-only python |
| `projeler.json` keys: `_aciklama`, `tarama_kokleri` (list), `ek_projeler` (list), `notlar` (dict) | read-only python |
| `programlar.json` keys: `_aciklama`, `programlar` (dict); card schema is P6's (`program-denetim.py --sema`) | read-only python |
| `notlar/hf-om-gecisi/DURUM.md` starts "Son güncelleme: 2026-11-11"; not referenced from `CLAUDE.md`/`AGENTS.md`/`README.md` | `DURUM.md:3` |
| Library rule: other packages' tests live in `araclar/testler/` (D5); that folder does not exist yet | `ls araclar/testler` |

---------------------------------------------------------------------------------------------------

## 3 Changes per file

General rules for every new check (apply everywhere below):
- **R-0** The merge rule at the top of this spec: new checks are UYARI; HATA only for (a) an existing JSON record file that does not parse and (b) `CLAUDE.md` != `AGENTS.md`.
- **R-A** A check on a file that a not-yet-landed package will create is **UYARI** while the file is missing, never HATA. This includes P8's own `BASLA.md` and `notlar/kararlar.md` (a missing document is a UYARI; the library session sees it at once, the monthly merge is not reverted).
- **R-B** The existing output contract of `dogrula.py` is untouched: the print block, the summary line `N skill · N hata · N uyarı` and the exit rule (`1` only on `hatalar`) are not edited (`dogrula.py:281-286`). The only insertion is the call of the new aggregator before the print block. No `--siki`, no accept list, no staleness check in `dogrula.py` (section 11).
- **R-C** No new check executes any tool except the two read-only calls named in E1 (`program-denetim.py --sema --ozet-json`) and the importlib loads in K; tool flags are read from source text (never `--help`; see 3.7 F).
- **R-D** "New" means new against `git show HEAD:...` only where stated (K); the 181 existing source records never count as new.

### 3.1 `BASLA.md` (new, repository root)

Purpose: the single entry document for a fresh agent in any tool. Written in plain Turkish, at most ~110 lines. Full text in section 4.1. Outline:
1. Kim olduğun (hafızasız oturum; her şey bu klasörde yazılı).
2. Okuma sırası (BASLA → `CLAUDE.md`/`AGENTS.md` → `notlar/kararlar.md` → `DURUM.md` only if a step is not "bitti" → the guide for the request).
3. Oturum başı rutini: `python3 araclar/aylik-ozet.py --hizli`, how to read `temiz/dikkat/sorun`, what to say to the user (max 5 lines), what never to do on your own.
4. "Hangi istek → hangi rehber → hangi komut" table (14 rows; section 4.1).
5. Her zaman geçerli beş kural (konu konu, onaysız değişiklik yok, push yalnız isteyince, proje adı kayıtlara yazılmaz, bilmiyorsan dur ve sor).
6. Hangi araç hangi talimat dosyasını okur (Claude Code → `CLAUDE.md`; Codex, Antigravity, Cursor, VS Code Copilot → `AGENTS.md`; Gemini CLI kurulu değil, `GEMINI.md` yok; Windows'ta `skill-ekle.py` çalışmaz).
7. İş bitince: `kapsam-denetimi.py`, `dogrula.py`, `test.py`, sonra commit (kullanıcıya sorarak).

Command/flag rule for BASLA: every `python3 araclar/<tool>.py ... --flag` in `BASLA.md` is checked by the flag check (3.7 check F). Only these flags may appear in BASLA (all taken from the already-written specs or the existing code): `aylik-ozet.py --hizli` (P4; `--oturum` is only P4's alias and is never written), `git-durum.py --kisa`, `--ozet-json`, `yedek-denetim.py --ozet-json`, `genel-bekci.py --ozet-json`, `--taban-yaz`, `program-denetim.py --oncesi <ad>`, `--sema`, `--ozet-json`, `proje-kullanimi.py --saglik --tara-kayitsiz --yetim --ekle --cikar --tasindi --yoksay --skill --repo`, `skill-ekle.py --oner --kuru --evet --dogrula --durum --guncelle --kaldir --geri-al --arac`, `arsiv-guncelle.py --aylik --kuru --uygula --dal --birlestir`, `github-skill-listesi.py`, `kaynak-cikar.py --repo --kuru` (P7), `duman-testi.py --araclar --kirli-ok`, `dogrula.py --github`. If a package ships a different flag name, the implementer edits BASLA to the real name (check F reports a UYARI until they match).

### 3.2 `notlar/kararlar.md` (new)

Purpose: standing decisions with dates, taken from the user's Claude memory files and `DURUM.md`, so Codex/Antigravity/Cursor sessions see them and `DURUM.md` can be archived without losing them (scenario 7). Project names are allowed here (notes file; the user's instruction). No secrets, no values.
Structure (full text in 4.2): "Nasıl okunur ve nasıl eklenir", "Geçerli kararlar" (K-01..K-24, each: tarih · karar · kaynak), "Değişen kararlar (artık geçerli DEĞİL)" (each with what replaced it), "Henüz sonuçlanmamış sorular" (incl. the monthly-triage question N), "Karar bekleyenler" and "Kabul edilen bekleyenler (aylık özette susturulur)" (the two sections `aylik-ozet.py` reads).
Edit rule written inside: only the library session adds a decision, only after the user said it; never delete, replaced items move to "Değişen kararlar" with the new date; keep each entry ≤ 3 lines.
dogrula checks (3.7 check B): file exists and the four headings exist (all UYARI, merge rule).

### 3.3 `CLAUDE.md` and `AGENTS.md`

**Equality rule.** The two files are kept **byte-identical**. There are no allowed differences (simplest and true today; the heading "Agent Talimatı" is already tool-neutral). Procedure: edit `CLAUDE.md`, then **one command** `cp CLAUDE.md AGENTS.md`, then `cmp CLAUDE.md AGENTS.md`; the commit message says "AGENTS.md eşitlendi". Why both exist: Claude Code reads `CLAUDE.md` and reads `AGENTS.md` only when `CLAUDE.md` is absent; the other four supported tools read `AGENTS.md` (bosluklar.md table). `dogrula.py` check A makes a difference a HATA (rule (b)).
Optional `GEMINI.md` (D1: off by default): if the file ever exists, check A2 warns when it does not mention `BASLA.md`. Stub text in 4.7.

Two **separate patches**. Both are proposals; neither is applied by the design.

**Patch A (pointers and flows; changes no rule).** Needs the user's yes, safe to apply any time after P8's files exist. Exact diff in 4.3. Summary:
1. New first line: pointer to `BASLA.md`, then a blank line, then the existing H1.
2. "Skill ekleme akışı" step 1 replaced by P1's text (which AI tools; `--arac`; `rehber/14-yapay-zeka-araclari.md`).
3. Line 51 (Programlar) replaced: in-place cards for HyperFrames and OpenMontage (merges P6's text).
4. "Bakım isteklerinde": the session-start bullet (P4's sentence, `aylik-ozet.py --hizli`), the monthly bullet replaced by P4's text (`arsiv-guncelle.py --aylik`), the "Yeni skill ekledim" bullet corrected (P7: A1..A9, no "global'de farklı sürüm"), and one new line per flow: proje takibi (P5), git ve yedek (P3), genel klasörler (P2), kaynak/skill çıkar (P7), aday kararları (P7), yapay zeka araçları (P1), eşitlik kuralı.
The overlapping proposals (P2 session-start wording, P3 first-step line, P6 programs line) are merged here, not stacked: one session-start command (`aylik-ozet.py --hizli`, which itself runs `git-durum`, `genel-bekci`, `yedek-denetim`); the individual commands are named only as fallback in `BASLA.md`.
Size: about +14 lines (57 -> ~71), long lines but one line per flow; details live in `BASLA.md` and the rehber files.

**Patch B (rule 1 exception) — ONE text, kept only here (4.4); P2's `rehber/12` and P6's `rehber/11` only cite "CLAUDE.md kural 1 istisnası" and never write their own variant.** APPLY ONLY AFTER THE USER APPROVES, as its own commit, before the first emptying step or the first approved HyperFrames/OpenMontage update, whichever comes first (OpenMontage lives in `~/.openmontage`, which rule 1 names). Until applied, rule 1 is unchanged, the library session must not write those folders, and `BASLA.md` says so. The exception is per operation and never general permission. The Claude-side memory note that also says "global klasörlere dokunma" (`skill-kutuphanesi.md`) is outside the library; after Patch B the library session asks the user whether to update that memory note too (approval item, section 7).

### 3.4 `README.md`

Edits (exact text in 4.5):
1. Lines 3-4: tools sentence names the five supported tools; line 1 of the file gets a pointer "Yeni oturum mu? Önce BASLA.md".
2. Lines 6-7: replace the stale "değişmez / eski agent'lar devam eder" bullet with the current stance (library tools never write the global folders; emptying planned, procedure in rehber/12).
3. "Klasörler" table: rows for `BASLA.md`, `notlar/kararlar.md`, `notlar/rafta/`, `yapay-zeka-araclari.json`, `yedekler.json`, `programlar.json`/`programlar/` (check each row against what exists when implementing; add only rows whose file exists).
4. Line 52 "Gönderilmeyenler": new patterns **only after P3's `.gitignore` change is approved and applied**; text from P3 hand-off 5(a).
5. Lines 53-57 restore block: P3 hand-off 5(b) sentences plus P8's one extra line (run `dogrula.py` and `git-durum.py` after cloning; unpushed commits are not in a clone).
6. Line 71: "11 prompt" → count derived from `promptlar/README.md` (16).
7. "Rehberler" list: add 11 (program yönetimi), 12 (genel klasör boşaltma), 13 (yedek ve geri alma), 14 (yapay zeka araçları).
8. "Araçlar" table: add one row per new tool (genel-bekci, git-durum, yedek-denetim, aylik-ozet, kaynak-cikar, program-denetim, yol-tara if missing) and the extended `proje-kullanimi.py` flags (P5 hand-off 5). Each row uses only flags that exist (check F).
Not changed: "GitHub deposu (private)" section other than line 52-57; "Değişiklik süreci (PR)".

### 3.5 `promptlar/README.md`

1. Reorder: row 11 before row 12 (fixes the 10, 12, 11 order).
2. Row 12 description replaced (P5 hand-off 5): `Bir skili/kaynağı hangi projeler kullanıyor (silmeden önce etki); aylık proje sağlık turu; proje ekle/çıkar/taşındı/yoksay`.
3. New rows 13, 14, 15, 16 (texts in 4.6): 13 program kur/güncelle/geri al/çıkar (P6), 14 kaynak/skill çıkar (P7), 15 yeni yapay zeka aracı (P1), 16 genel klasör boşaltma (P2).
4. Intro line "Claude Code ve Codex'te aynen çalışır" → five tools.
5. First bullet under "Değişmeyen kurallar" gets the exception clause (only after Patch B is applied; until then the bullet stays as is, and a note in the commit says why).
Everything in the file stays one table + one rules list.

### 3.6 Stale top-level documents: what is shelved, what is refreshed

New folder `notlar/rafta/` with a 5-line `notlar/rafta/OKU.md` ("Burada eski belgeler durur; hiçbiri uygulanmaz; güncel bilgi BASLA.md, CLAUDE.md, notlar/kararlar.md"). Moves use `git mv` (history kept, reversible). Needs the user's approval (critic list: "arşive taşıma = silme sayılır").

| Document | Decision | Reason |
|---|---|---|
| `PLAN.md` | **shelve** → `notlar/rafta/PLAN.md`; first line already says UYGULANDI; no inbound links | decision history; body has old counts (139/55/28) and "Global kurulum yok" |
| `Kullanılacak Promt Örneği.md` | **shelve** → `notlar/rafta/Kullanılacak Promt Örneği.md` | older copy of `promptlar/11` (no `~/.openmontage` in rule line); before moving the implementer runs `diff` against `promptlar/11-guvenilir-skill-secimi-mevcut-proje.md` and notes the result in the commit message |
| `notlar/yerel-yapilacaklar-2026-11.md` | **shelve** → `notlar/rafta/yerel-yapilacaklar-2026-11.md` | finished work (PR #3, 5250 skills, `find ~ ... kilit.json` loop that conflicts with the project gate) |
| `TEST_RAPORU.md` | **stays at root, refreshed by the normal process, not by P8** | generated by `skill-calistir.py:44`, linked from README and `skill-readme.py:121`; shelving would break links and the generator. `ortak.RAPOR_YASI` lists it for the monthly summary when older than 45 days (not a dogrula warning); the monthly chain already regenerates it (`arsiv-guncelle.py:211`). P8 does NOT run `skill-calistir.py` (it installs every skill into temp projects: long, and a real run is a library change). The implementer only reports the age. |
| `README-SKILLER.md`, `KATALOG*.md` | not touched | generated |
| `notlar/hf-om-gecisi/DURUM.md` | not P8's file; section 6 asks the library session to update it with approval | owner rule |

No inbound link needs fixing (grep: none). After shelving, the implementer re-runs the quoted grep `grep -rn "PLAN.md\|Promt\|yerel-yapilacaklar" --include='*.md' --include='*.py' --include='*.json' .` (excluding `arsiv/`, `registry.json`, `KATALOG.md`, `aciklama-tr.json`) and expects only hits inside `notlar/rafta/`.

### 3.7 `araclar/dogrula.py`

Structure: add module-level functions (no behaviour change when called by nothing), each takes `kok: Path` (and `bugun: date` where time matters) and returns `(hatalar, uyarilar)` lists so tests can feed fake trees. One aggregator `belge_ve_kayit_denetimleri(kok=KOK)` calls them in the order below. In `main()`: after the project block (`dogrula.py:280`) and before the print loop (`:281`) insert exactly:

```python
h2, u2 = belge_ve_kayit_denetimleri()
hatalar += h2
uyarilar += u2
```
**Nothing else in the output path changes**: the print loop, the summary line and `sys.exit(1 if hatalar else 0)` (`:281-286`) stay byte for byte. There is no `--siki`, no accept list and no report-age check in `dogrula.py` (the review removed all three, section 11). Docstring (`:1-10`) gets the new check bullets.

Existing lines edited (P5 hand-off, exact):
- after `:267` add `for u in pk.hizli_kontrol(ayar_p): uyarilar.append(u)` guarded by `hasattr(pk, "hizli_kontrol")` (P5 not landed -> nothing).
- `:269` extend `adlar_p` with `set(ayar_p.get("bilinen_projeler", {})) | set(ayar_p.get("program_kullanimi", {})) | set(ayar_p.get("kendi_skilleri", {})) | {Path(y["yol"]).name for y in ayar_p.get("yoksay", []) if isinstance(y, dict) and y.get("yol")}`; the existing `len(a) >= 5` and skill-name filters stay.
- `:274` add `"programlar.json"` to the leakage tuple (D8). Expected result today: no hit (P5 checked by grep). If it hits, that is a real rule-6 leak: fix the card, never the check.

#### New checks (severity table)

| Id | Function | Behaviour | Severity |
|---|---|---|---|
| A | `esitlik_denetimi` | `CLAUDE.md` and `AGENTS.md` read as bytes; either missing -> `CLAUDE.md/AGENTS.md eksik`; different -> `CLAUDE.md ile AGENTS.md aynı değil (cp CLAUDE.md AGENTS.md)` | **HATA** (rule b) |
| A2 | same | `GEMINI.md` exists and does not contain `BASLA.md` -> `GEMINI.md BASLA.md'ye işaret etmiyor`. Missing file = nothing (D1) | UYARI |
| B | `giris_belgeleri_denetimi` | `BASLA.md` missing; `notlar/kararlar.md` missing; `kararlar.md` lacks a heading whose line starts with `## Geçerli kararlar`, `## Değişen kararlar`, `## Karar bekleyenler`, `## Kabul edilen bekleyenler` (P4 reads the last two); first line of `CLAUDE.md` does not contain `BASLA.md` | UYARI (all) |
| B2 | same | every backticked repo path in `BASLA.md` matching `` `((?:araclar|rehber|promptlar|notlar)/[\w./-]+\.(?:py|md|json|txt))` `` must exist -> `BASLA.md olmayan dosyayı anıyor: <path>`. `BASLA.md` must name `notlar/kararlar.md` and `DURUM.md` | UYARI |
| C | `paket_dosyalari_denetimi` | each file of the table below missing -> `<paket> dosyası yok: <path>` (R-A). `.gitignore` missing any pattern of P3's block, **including P4's two lines `notlar/son-aylik-calisma.json` and `notlar/aylik-ozet.md`** -> UYARI (skipped if `notlar/kararlar.md` records `.gitignore değişikliği reddedildi`). `rehber/13-yedek-ve-geri-alma.md` lacks any of `git revert -m 1`, `gh auth login`, `git bundle create`, `yedekler.json`, `rehber/12` -> UYARI | UYARI |
| E1..E6 | `kayit_semalari_denetimi` | basic schemas, see below | HATA only for an unparsable existing file; every schema finding UYARI |
| F | `bayrak_denetimi` | docs mention flags/tools that do not exist, see below | UYARI |
| H | `eski_anlatim_denetimi` | stale wording, see below | UYARI |
| K | `kaynak_kapilari_denetimi` | P7's gates on `kaynaklar.json`, see below | UYARI (all) |

Package-file table for check C (path -> package): `rehber/12-genel-klasor-bosaltma.md` P2, `rehber/13-yedek-ve-geri-alma.md` P3, `rehber/14-yapay-zeka-araclari.md` P1, `promptlar/13-program-kur-guncelle.md` P6, `promptlar/14-kaynak-cikar.md` P7, `promptlar/15-yeni-yapay-zeka-araci.md` P1, `promptlar/16-genel-klasor-bosaltma.md` P2, `yapay-zeka-araclari.json` P1, `yedekler.json` P3, `notlar/genel-klasor-tabani.json` P2 (written only on emptying day), `araclar/genel-bekci.py` P2, `araclar/git-durum.py` P3, `araclar/yedek-denetim.py` P3, `araclar/aylik-ozet.py` P4, `araclar/kaynak-cikar.py` P7.
Deviations from the requests (merge rule): P2 "HATA if rehber/12, promptlar/16, genel-bekci.py or the three files are missing" -> UYARI; P1 "HATA if `yapay-zeka-araclari.json`, `rehber/14` or `promptlar/15` missing" -> UYARI.

**Report staleness (B2) is not a `dogrula.py` check.** The table `RAPOR_YASI` and the pure function `rapor_yasi_satirlari()` are in `ortak.py` (3.8) for `aylik-ozet.py` full mode (P4 request); `dogrula.py` never imports them. Reason: the "0 uyarı" rule of duman and the monthly `dogrula` runs must not depend on the calendar. P1's `skill-ekle.py --araclar` already reports tool-document age (45 days); P8 does not repeat it. P2's baseline age and DURUM.md age are in the same table.

**Check E — basic schemas (E1..E6).** Each is skipped when the file is missing (check C reports absence). In every item: JSON that does not parse -> HATA `<dosya> okunamadı: <neden>` (rule a); every other finding -> UYARI.
- E1 `programlar.json`: no `programlar` dict -> UYARI. If `araclar/program-denetim.py` source contains `"--sema"`: run `sys.executable araclar/program-denetim.py --sema --ozet-json` with `cwd=kok`, timeout 60 s (no network: schema mode reads the card file only); parse the single JSON object; each `satirlar` item starting `HATA:` or `UYARI:` -> UYARI `programlar.json kart şeması: <satır>`; exit != 0, timeout or invalid JSON -> UYARI `program şema denetimi çalışmadı`. No built-in card-field check (P6's `sema_denetle` is the authority). Cross-check (P6): every key of any `card["giris_yolu"]["araclar"]` must be in the key set of E4 (`arac_anahtarlari`, skipped if that file is missing or unreadable) -> UYARI `program <ad>: giris_yolu araç anahtarı yok: <k>`.
- E2 `projeler.json`: top level not dict, `tarama_kokleri`/`ek_projeler` not lists of strings, `notlar` not dict -> UYARI. P5 fields, only if present: `bilinen_projeler`, `program_kullanimi`, `kendi_skilleri` dict, `yoksay` list of dicts each with `yol` and `neden` -> UYARI when the type is wrong. A `tarama_kokleri` path that does not exist on this machine -> UYARI.
- E3 `yedekler.json` (P3): `surum != 1`, a record missing `kimlik, yol, tur, ne, tarih, geri_yukleme, gizli_icerir`, `gizli_icerir` not in `("evet","hayir")`, duplicate `kimlik`, or `tur` not in `TURLER` -> UYARI. `TURLER` is read with `importlib` from `araclar/yedek-denetim.py` inside try/except; when the module or constant is unavailable the `tur` check is skipped.
- E4 `yapay-zeka-araclari.json` (P1's real shape, answers P1 hand-off 7): `d["araclar"]` is a LIST of records, each with a string `anahtar`; `arac_anahtarlari(kok)` returns `{r["anahtar"] for r in d["araclar"]}` (a dict-shaped `araclar` is tolerated: its keys). Must contain at least `claude-code`, `codex`, `antigravity`, `cursor`, `vscode-copilot` (D1; same keys P6 relies on); a missing one -> UYARI `araç kaydı yok: <anahtar>`. A record lacking any of `anahtar, ad, kurulu, proje_skill_okur, dogrulama_tarihi, surumler` -> UYARI; `dogrulama_tarihi` not `YYYY-AA-GG` -> UYARI. **No staleness UYARI here** (the former 120-day rule and the field names `son_dogrulama`, `proje_skill_klasoru`, `talimat_dosyasi` are withdrawn; P1's `--araclar`, P4's full monthly summary and `dogrulama_siniri_gun` (45) own freshness).
- E5 `notlar/genel-klasor-tabani.json` (P2): `surum != 1` -> UYARI. No age check (P2's `genel-bekci.py` and `RAPOR_YASI` cover it).
- E6 `kaynaklar.json` basic schema (merged with P7's G-TIP): `repolar` not a list, a record not a dict -> UYARI; `repo` not matching `^[\w.-]+/[\w.-]+$` -> UYARI; duplicate `repo` (case-insensitive) -> UYARI; `tip` not in `KAYNAK_TIPLERI = ("T1","T2","T3","T4","T5","T6","KAYIP","EMEKLI")` (one constant at module level; P6/P7 add values here) -> UYARI; `oncelik` present and not an int -> UYARI; a key outside `KAYNAK_ANAHTARLARI = ("repo","tip","oncelik","not","haric","dahil","dahil_degil","bagimlilik","kimlik","dosya_haric","program","kok_dosyalari","eski_adlar","ad_devral","eklendi","onay","kayip_tarihi")` -> UYARI. First real run: if a legacy record trips a rule, relax the rule (never edit the 181 records); the hits go in the commit message.

**Check K — P7's gates (UYARI only; fires only on records that are new against `HEAD`).**
- *New record* = a `repolar` entry for which neither its `repo` nor any of its `eski_adlar` matches (case-insensitively) the `repo` or any `eski_adlar` of any record in `git show HEAD:kaynaklar.json` (`subprocess`, `cwd=kok`, timeout 10 s). If git cannot read `HEAD` (no repo, no file, other machine) the gates are skipped silently. A rename (new `repo`, old name in `eski_adlar`) is not new. Consequence, stated on purpose: the gates are visible between the edit and the commit (rehber/03 A9 runs `dogrula.py` before the commit); after the commit the record is no longer new.
- **G-ONAY:** new record without `eklendi` (`YYYY-AA-GG`) or without an `onay` dict having `kim`, `tarih`, `commit` (40 hex) -> `kaynak kaydında onay yok: <repo> (rehber/03 A4)`.
- **G-LISANS:** new record whose registry skills (dogrula's loaded `skiller`, field `repo` and `lisans`) have a `lisans` for which `lisans_riskli()` (loaded from `araclar/kaynak-cek.py` by importlib, side-effect free; skipped if absent) is true and `onay.lisans_onay` is empty -> `lisans <L> için onay.lisans_onay yok: <repo>`.
- **G-YOL:** new record, `kapi_kontrol(repo, None, skiller)` from `araclar/yol-tara.py` (importlib; returns `(sorunlar, taranan, hata)`) gives problems and `onay.yol_onay` is empty -> `yol kapısı takıldı: <repo>: <ilk sorun>`; `hata` not None or any exception -> `yol kapısı çalışmadı: <repo>`; module absent -> skipped.
- **G-ONAY-CIKAR:** an entry of `arsivden_cikarilan_repolar` or `arsivden_cikarilanlar` that is not present in HEAD's list (compared as JSON text) and lacks `onay{kim,tarih}`, or whose `neden` contains `<NEDEN`, or (`arsivden_cikarilan_repolar` only) lacks `geri_alma` -> UYARI.
- **G-KAYIP:** any record with `tip == "KAYIP"` and no `kayip_tarihi` -> UYARI. P7's implementation adds the date to the one existing KAYIP record (J-DTurner/etsy-api-skill) in its own change (needs the user's approval, P7 section 7), so the first run after P7 is clean; if P7 has not landed, this UYARI is real and is fixed by that data edit, not by a list.
- Raising any of these to HATA is a separate later decision with the user's own approval (P7 section 7).

**Check F — documents mention tools or flags that do not exist (replaces "derive flags from `--help`").**
`--help` is not usable: twelve tools have no argparse and `--help` runs them (observed). Flags are derived statically.
- Tool flag set: `bayraklar(tool_py_text) = set(re.findall(r"""["'](--[a-z][a-z0-9-]*)(?=[=\s"'])""", text))`. This covers `add_argument("--x")`, `"--x" in sys.argv`, `sys.argv.index("--x")`. Add `{"--help", "-h"}`.
- Documents scanned: `CLAUDE.md`, `AGENTS.md`, `BASLA.md`, `README.md`, `rehber/*.md`, `promptlar/*.md` (not `notlar/`, not `arsiv/`).
- Preprocessing: join backslash-continued lines (`text.replace("\\\n", " ")`).
- Match: `re.finditer(r"araclar/([a-z][\w-]*)\.py([^`\n]*)", text)`. If `araclar/<tool>.py` does not exist -> UYARI `<doc>:<satır>: olmayan araç araclar/<tool>.py`. Else every `(?<![\w-])(--[a-z][a-z0-9-]*)` in group 2 must be in the tool's flag set, otherwise UYARI `<doc>:<satır>: araclar/<tool>.py '<flag>' bayrağını tanımıyor`.
- The match stops at a backtick or end of line, so flags in a different backtick span than the tool are not attributed (no false positives from git/gh/codex options).
- `--hizli` of `aylik-ozet.py` is found in P4's source (`"--hizli"`); `--oturum` is only P4's alias and appears in no document.
- Existing prompt-11 checks (`dogrula.py:186-198`, HATA) are untouched.
- First real run: the implementer runs dogrula once and triages each hit: fix the document, or (document right, tool builds the flag dynamically) leave it and write the hit in the commit message. There is no accept list.

**Check H — stale wording (A5).** Patterns (over `README.md`, `BASLA.md`, `CLAUDE.md`, `AGENTS.md`, `rehber/*.md`, `promptlar/*.md`, line by line):
- `H1 = (?i)global skill klasörlerin[^\n]*değişmez` (hits README:6 today)
- `H2 = (?i)eski agent'ların[^\n]*devam eder` (hits README:7 and `rehber/01:12`)
Hit -> UYARI `<doc>:<satır>: eski anlatım (genel klasörler boşaltılacak, notlar/kararlar.md K-04): <ilk 60 karakter>`. P8 fixes README itself; the `rehber/01:12` hit is P1's (hand-off P1-B).

**The one known warning today** (the emekli-role line `dogrula.py:119-120`) is not suppressed in `dogrula.py`; duman filters exactly that line locally (3.9 item 4), with an end date. Every other UYARI must be fixed at acceptance.

### 3.8 `araclar/ortak.py` (append-only, at the end of the file; no existing line changes, D2)

```python
# --- P8: genel klasör izi, rapor araçları, rapor yaşı ---------------------------------------
GENEL_ATLA = ("synced", ".system", "skills-cursor")  # Claude hesap senkronu / Codex ve Cursor'ın kendi yerleşikleri
GENEL_IZLEME_KLASORLERI = list(GLOBAL_KLASORLER.values()) + [
    Path.home() / ".openmontage" / ".agents" / "skills",
    Path.home() / ".cursor" / "skills",
    Path.home() / ".gemini" / "skills",
    Path.home() / ".gemini" / "antigravity" / "skills",
    Path.home() / ".copilot" / "skills",
]


def genel_izleri(klasorler=None) -> dict:
    """{'<klasör>/<ad>': mtime_ns}: kütüphane araçları bu klasörlere yazmamalı. Yalnız okur."""
    iz = {}
    for g in (GENEL_IZLEME_KLASORLERI if klasorler is None else klasorler):
        g = Path(g)
        if g.is_dir():
            for p in sorted(g.iterdir()):
                if p.name not in GENEL_ATLA:
                    iz[f"{g}/{p.name}"] = p.lstat().st_mtime_ns
    return iz


def genel_parmak_izi(klasorler=None) -> str:
    return hashlib.sha256(json.dumps(genel_izleri(klasorler), sort_keys=True).encode()).hexdigest()


def genel_fark(once: dict, sonra: dict) -> list:
    return sorted(set(once) ^ set(sonra) | {k for k in set(once) & set(sonra) if once[k] != sonra[k]})


OZET_DURUMLAR = ("temiz", "dikkat", "sorun")
OZET_ARACLARI = [  # (araç dosyası adı, ekstra bayraklar); her biri --ozet-json destekler (D4); duman ve aylik-ozet (P4) aynı listeyi kullanır
    ("git-durum", []), ("yedek-denetim", []), ("genel-bekci", []),
    ("program-denetim", []), ("proje-kullanimi", ["--saglik"]),
    ("skill-ekle", ["--araclar"]),                                                            # P1
    ("konu-takip", ["--bekleyenler"]), ("github-trend", ["--bekleyenler"]), ("populer-tarama", ["--bekleyenler"]),  # P7
]


def ozet_json_gecerli(metin: str):
    """stdout tam olarak tek JSON nesnesi mi? -> (nesne ya da None, hata metni)."""
    try:
        o = json.loads(metin)
    except ValueError as e:
        return None, f"JSON değil: {str(e)[:80]}"
    if not isinstance(o, dict) or not {"arac", "durum", "satirlar", "karar_bekleyen"} <= set(o):
        return None, "arac/durum/satirlar/karar_bekleyen anahtarları eksik"
    if o["durum"] not in OZET_DURUMLAR or not isinstance(o["arac"], str):
        return None, f"durum geçersiz: {o['durum']!r}"
    if not all(isinstance(o[k], list) and all(isinstance(x, str) for x in o[k]) for k in ("satirlar", "karar_bekleyen")):
        return None, "satirlar/karar_bekleyen metin listesi değil"
    return o, ""


RAPOR_YASI = [  # (yol, eşik gün, yenileme komutu): aylik-ozet tam modda gösterir; dogrula.py KULLANMAZ
    ("notlar/github-trend.md", 45, "python3 araclar/github-trend.py --aday"),
    ("notlar/populer-skiller.md", 45, "python3 araclar/populer-tarama.py"),
    ("notlar/konu-takip.md", 45, "python3 araclar/konu-takip.py"),
    ("notlar/program-denetimi.md", 45, "python3 araclar/program-denetim.py"),
    ("notlar/kapsam-denetimi.md", 45, "python3 araclar/kapsam-denetimi.py"),
    ("TEST_RAPORU.md", 45, "aylık güncelleme yeniler (python3 araclar/skill-calistir.py)"),
    ("notlar/proje-durumu.md", 45, "python3 araclar/proje-kullanimi.py --saglik --yaz"),
    ("notlar/genel-bekci.md", 45, "python3 araclar/genel-bekci.py"),
    ("notlar/hf-om-gecisi/DURUM.md", 45, "kütüphane oturumu 'Son güncelleme' satırını yeniler"),
]


def rapor_yasi_satirlari(kok=None, bugun=None, tablo=None) -> list:
    """Bayat raporların düz cümleleri (yoksa []). Yalnız okur. Tarih: dosyanın ilk 8 satırındaki ilk YYYY-AA-GG;
    yoksa 'git log -1 --format=%cs -- <dosya>' (klonda mtime sıfırlanır, kullanılmaz); ikisi de yoksa atlanır."""
    import subprocess
    from datetime import date
    kok = Path(kok or KOK)
    bugun = bugun or date.today()
    cikti = []
    for yol, esik, komut in (RAPOR_YASI if tablo is None else tablo):
        f = kok / yol
        if not f.is_file():
            continue
        m = re.search(r"\d{4}-\d{2}-\d{2}", "\n".join(f.read_text(encoding="utf-8", errors="replace").splitlines()[:8]))
        gun = m.group(0) if m else ""
        if not gun:
            try:
                gun = subprocess.run(["git", "log", "-1", "--format=%cs", "--", yol], cwd=kok, capture_output=True,
                                     text=True, timeout=10).stdout.strip()
            except (OSError, subprocess.SubprocessError):
                gun = ""
        try:
            yas = (bugun - date.fromisoformat(gun)).days
        except ValueError:
            continue
        if yas > esik:
            cikti.append(f"{yol} {yas} gün önce üretilmiş (eşik {esik}); yenile: {komut}")
    return cikti
```
`GLOBAL_KLASORLER` (`ortak.py:37-41`) is unchanged: skill-ekle's refusal and `global_durum` behave as before. The extra folders only widen the *fingerprint* (read-only). Superset note: both old fingerprints (duman: 3 folders; test.py: 3 + OpenMontage agents folder) are contained. `subprocess` and `datetime` are imported inside the function so the module import list is unchanged. There is **no** `BILINEN_UYARILAR`/`bilinen_uyari` (removed in review). `OZET_ARACLARI` now also holds P1's `skill-ekle --araclar` and P7's three `--bekleyenler` tools (review); P4 merges it with its own list without duplicates.

### 3.9 `araclar/duman-testi.py`

Exact edits (old -> new):
1. Header docstring (`:1-18`): step 2 text becomes "dogrula.py --github (0 hata; bilinmeyen uyarı yok, emekli-rol uyarısı kabul)"; step 10 becomes "10. Kütüphane araçları genel skill klasörlerine yazmadı mı"; new step 11 "Rapor araçları (salt okuma)".
2. Remove local `parmak_izi()` (`:44-53`); `from ortak import GLOBAL_KLASORLER, KOK` -> `from ortak import KOK, OZET_ARACLARI, genel_fark, genel_izleri, ozet_json_gecerli`. `main()` start (`:58`) `once_iz = genel_izleri()`.
3. `:61-63` tree check: if `"--kirli-ok"` in `sys.argv` the check is informational (`print("     bilgi: ...")`, not counted) else as before. The failure detail prints the first 8 changed paths and the hint `önce commit (kullanıcı onayıyla), sonra duman testi`. Later steps keep comparing against the baseline `kirli` (`:81, 90, 144`), so `--kirli-ok` is safe.
4. `:70-72` (no shared accept list; one local filter):
   ```python
   # dogrula.py'nin bugün bilinen tek uyarısı (rol emekli skil kullanıyor); sona erince yeniden sorulur
   KABUL_UYARI = re.compile(r"^UYARI: rol [\w-]+: '[^']+' emekli/kaynakta kaldırılmış; arşiv kopyası kullanılıyor")
   KABUL_SON = "2027-02-11"
   k, o = kos(PY, "araclar/dogrula.py", "--github")
   adim("dogrula.py --github: 0 hata", k == 0 and " 0 hata" in o, o)
   uyarilar = [s for s in o.splitlines() if s.startswith("UYARI:")]
   bilinmeyen = [s for s in uyarilar if not (KABUL_UYARI.match(s) and date.today().isoformat() <= KABUL_SON)]
   if len(bilinmeyen) != len(uyarilar):
       print(f"     bilgi: kabul edilen emekli-rol uyarısı: {len(uyarilar) - len(bilinmeyen)} (son {KABUL_SON})")
   adim("dogrula.py: bilinmeyen uyarı yok", not bilinmeyen, "\n".join(bilinmeyen))
   ```
   Network-origin warnings (`YENİ SKILL REPOSU`, `yıldızlı ama kaynaklar.json'da yok`, `GitHub ... okunamadı`) never match the pattern: they are decisions or outages. `dogrula.py`'s own output is unchanged.
5. `:143` step 10:
   ```python
   print("10) Genel skill klasörleri")
   fark = genel_fark(once_iz, genel_izleri())
   adim("kütüphane araçları ve bu test genel skill klasörlerine yazmadı", not fark,
        "değişen girdiler: " + ", ".join(fark[:6]) + " (testten mi dışarıdan mı? HyperFrames, skills aracı ya da Codex aynı anda yazmış olabilir: python3 araclar/genel-bekci.py)")
   adim("kütüphane değişmedi", kos("git", "status", "--porcelain")[1].strip() == kirli)
   ```
   Effect after the planned emptying: the folders hold only vendor items (skipped) so the before/after hashes are trivially equal.
6. New step 11 (after step 10), read-only; every tool file must exist (duman runs only at acceptance, after all packages landed):
   ```python
   print("11) Rapor araçları (salt okuma, --ozet-json)")
   AG_YOK = {"program-denetim": ["--oncesi", "hyperframes", "--cevrimdisi"]}   # ağa çıkmasın (P6 bayrağı); çıkış 0 ve geçerli JSON ister
   for ad, ek in OZET_ARACLARI + [("aylik-ozet", ["--hizli"])]:
       arg = AG_YOK.get(ad, ek)
       k, o = kos(PY, f"araclar/{ad}.py", *arg, "--ozet-json")
       obj, neden = ozet_json_gecerli(o) if k == 0 else (None, f"çıkış kodu {k}")
       adim(f"{ad} --ozet-json: tek JSON nesnesi, çıkış 0", obj is not None, neden + " " + o[-200:])
   adim("rapor araçları kütüphane dosyalarına hiçbir şey yazmadı", kos("git", "status", "--porcelain")[1].strip() == kirli)
   ```
   `durum` is not judged: "dikkat" and "sorun" are findings, not failures (D4). The `proje-kullanimi --saglik` call has no `--yaz` and the `aylik-ozet` call is the fast mode (`--hizli`, P4: no network, no file). Only `program-denetim` can reach the network, hence `--oncesi hyperframes --cevrimdisi`. `skill-ekle --araclar` runs local `--version` probes only (P1). The old exemption for `notlar/` files is dropped: every `--ozet-json` run writes nothing (P4 contract), so the tree must be exactly as before.
7. `--araclar` step 9 stays Claude + Codex only. Deferred for the other three tools (section 8).
8. Final line unchanged (`Duman testi: N/N adım geçti`). `import re` and `from datetime import date` are added if missing.

### 3.10 `araclar/test.py`

1. `:16` import: `from ortak import GLOBAL_KLASORLER, KOK, json_oku` → add `genel_parmak_izi`. Replace the body of `parmak_izi()` (`:32-41`) with `return genel_parmak_izi()` (name and call sites `:1073`, `:1689` unchanged; the extra OpenMontage path of the old body is now part of `GENEL_IZLEME_KLASORLERI`). `GLOBAL_KLASORLER` stays imported (`:1652`).
2. New function (place before `main()`, i.e. before `:1072`) and one call inserted **before** `:1689` (so the global fingerprint also covers the child tests):
   ```python
ALT_TEST_ZAMAN_ASIMI = 600  # sn, dosya başına


def alt_testler():
    """araclar/testler/test_*.py dosyalarını sırayla ayrı süreçte çalıştırır (D5): çıkış 0 ve son satır 'N/N test geçti'."""
    import re
    klasor = KOK / "araclar" / "testler"
    dosyalar = sorted(klasor.glob("test_*.py")) if klasor.is_dir() else []
    if not dosyalar:
        print("  BİLGİ: araclar/testler/ yok ya da boş; alt test dosyası çalıştırılmadı")
        return
    for f in dosyalar:
        try:
            r = subprocess.run([sys.executable, str(f)], cwd=KOK, capture_output=True, text=True,
                               stdin=subprocess.DEVNULL, timeout=ALT_TEST_ZAMAN_ASIMI)
        except subprocess.TimeoutExpired:
            test(f"alt test {f.name}: {ALT_TEST_ZAMAN_ASIMI} sn içinde bitmedi", False)
            continue
        son = (r.stdout.strip().splitlines() or [""])[-1]
        m = re.fullmatch(r"(\d+)/(\d+) test geçti", son)
        test(f"alt test {f.name}: {son or 'çıktı yok'}", r.returncode == 0 and bool(m) and m.group(1) == m.group(2),
             (r.stdout + r.stderr)[-600:])
```
   Call: `alt_testler()` right before line `:1689`. Zero files = pass with a BİLGİ line (nothing counted). One `test()` entry per file. Sorted order is stable. The loader never runs `test.py` recursively and `test_p8-butunluk.py` must not call `test.py`.
3. P6 hand-off 1 (one check, after the program block `:1513-1530`): if `araclar/program-denetim.py` source contains `"--sema"`: run it with `--sema --ozet-json` (`subprocess`, `cwd=KOK`, timeout 60), parse the one JSON object. The only failure is "no parsable JSON" or a `satirlar` item containing `programlar.json okunamadı`: `test("programlar.json: kart şeması okunabilir (program-denetim --sema)", ...)`. Every other `HATA:`/`UYARI:` line is printed as `  not: ...` and is not a failure (P6's request; schema findings are UYARI everywhere). Skipped (no entry) while the flag is not in the source.
4. The existing program block `:1492-1531` stays as is (P6 hand-off 1).

### 3.11 Other owned files

- `PLAN.md`, `Kullanılacak Promt Örneği.md`, `notlar/yerel-yapilacaklar-2026-11.md`: moved (3.6). `TEST_RAPORU.md`: unchanged by P8 (3.6).
- `notlar/rafta/OKU.md` (new, 5 lines, text in 4.8).
- `araclar/testler/test_p8-butunluk.py` (new, section 5). `araclar/testler/` itself is created by whichever package lands first; P8's implementer creates it if absent (no `__init__.py`; tests are scripts).
- `promptlar/10-kutuphane-saglik-kontrolu.md` line 8 (unowned gap taken): `... katalog, 44 güvenlik testi, güncelleme raporu ...` -> `... katalog, güvenlik testleri, güncelleme raporu ...` (delete the stale number only).
- `rehber/08-test-sureci.md` (unowned gap taken): one paragraph appended as the last section: "## Alt test dosyaları (`araclar/testler/`): her paket testlerini `araclar/testler/test_<paket-anahtarı>.py` dosyasında tutar. Dosya tek başına çalışır (`python3 araclar/testler/test_<anahtar>.py`), yalnız geçici klasör ve sahte veri kullanır, son satırı `N/N test geçti` olur, çıkış kodu 0 ya da 1'dir. `python3 araclar/test.py` bu dosyaların hepsini ayrı süreçte çalıştırır ve her biri için bir satır gösterir."

### 3.12 Hand-off intake format (D6) — fixed list format

Every request from another package is recorded and answered in this exact shape. The implementer keeps the filled register in the commit message of the P8 change and in `notlar/kararlar.md` only when a decision results.

```
DEVIR <PAKET>-<n>  →  P8
Dosya:     <tam yol; yalnız P8'in sahip olduğu dosyalardan biri>
Tür:       ekle-satır | değiştir-metin | kontrol-ekle | sabit-ekle | karar-ekle | belge-güncelle
İçerik:    <tam metin ya da tam davranış; kontrolse HATA ya da UYARI>
Önkoşul:   <hangi paket dosyası var olmalı>
Onay:      yok | kullanıcı onayı gerekir (neden)
Sınama:    <komut ya da test numarası>
Karar:     kabul | değiştirildi (neden) | reddedildi (neden) | ertelendi (neden)   ← P8 doldurur
Yer:       <bu spec'te bölüm / dosya:satır>                                          ← P8 doldurur
```
Rules: a request that names a file P8 does not own is returned to its sender; a request for HATA on a not-yet-existing file is changed to UYARI (R-A); a request that changes an existing output format is rejected (D2). Section 6.2 is the register already filled for the specs that exist.

---------------------------------------------------------------------------------------------------

## 4 User-facing texts

### 4.1 `BASLA.md` (full text)

```markdown
# BASLA — kütüphane oturumuna giriş (her yapay zeka aracı için)

Sen bu kütüphanenin hafızasız oturumusun: önceki konuşmaları görmezsin. Bilmen gereken her şey bu klasörde yazılı.
Kütüphane: skill arşivi + araçlar. Skiller yalnız projenin içine, yalnız `skill-ekle.py` ile kurulur. HyperFrames,
OpenMontage gibi programların takibi ve güncellemesi de burada yapılır. Kullanıcı bunları kendisi izlemez; sen izlersin,
her gerçek değişiklikte onayını alırsın.

## 1. Okuma sırası
1. Bu dosya.
2. `CLAUDE.md` (Claude Code okur) ya da `AGENTS.md` (Codex, Antigravity, Cursor, VS Code Copilot okur). İkisi birebir aynıdır; kesin kurallar orada.
3. `notlar/kararlar.md`: kullanıcının verdiği kalıcı kararlar. Birini değiştirmeden önce kullanıcıya sor.
4. `notlar/hf-om-gecisi/DURUM.md`: yalnız çizelgesinde durumu "bitti" olmayan adım varsa oku. Hepsi bitti ise atla.
5. İsteğe uyan rehber (aşağıdaki tablo).

## 2. Oturum başı rutini
Kütüphane oturumunun ilk işi:
```
python3 araclar/aylik-ozet.py --hizli
```
Çıktıyı kullanıcıya iki cümleyle söyle. Aylık çalışma 35 günü aştıysa "Aylık çalışmayı şimdi yapayım mı?" diye sor; evet derse `python3 -u araclar/arsiv-guncelle.py --aylik`.
Hızlıdır (yaklaşık 5 sn), ağ kullanmaz, hiçbir şey yazmaz, en çok 15 satır basar. Git durumunu, genel klasörlerde beklenmeyen girdi olup olmadığını,
yedek yaşını, son aylık çalışmayı ve karar bekleyenleri toplar.
- Sonuç `temiz`: kısa bir cümleyle söyle, başka bir şey yapma.
- Sonuç `dikkat` ya da `sorun`: en fazla 5 satırla, sade Türkçe ile söyle. Kendiliğinden düzeltme, silme, taşıma, push yapma.
- Tam özet (ayda bir ya da kullanıcı isterse): `python3 araclar/aylik-ozet.py`. Yapay zeka aracı belgelerinin bayatlığı (`python3 araclar/skill-ekle.py --araclar`) ve rapor bayatlığı yalnız tam modda görünür.
- Komut yok ya da hata verirse kullanıcıya söyle; yerine tek tek çalıştır: `python3 araclar/git-durum.py --kisa`,
  `python3 araclar/genel-bekci.py --ozet-json`, `python3 araclar/yedek-denetim.py --ozet-json`.

## 3. Hangi istek, hangi rehber, hangi komut
| Kullanıcı ne diyor | Rehber / istem | İlk komut (hepsi önce rapor, değişiklik onayla) |
|---|---|---|
| "Şu projeye skill kur" | `rehber/01`, `promptlar/01-03` | `python3 araclar/skill-ekle.py <proje> --oner "<ihtiyaç>"`, sonra `--kuru`, onay, `--evet`, `--dogrula` |
| Hangi AI araçlarını kullanıyor / yeni araç ekle | `rehber/14-yapay-zeka-araclari.md`, `promptlar/15` | `yapay-zeka-araclari.json` oku; kurulumda `--arac` seçimini sor |
| "Yeni skill ekledim, kontrol et" (yeni kaynak) | `rehber/03` A1..A9, `promptlar/07` | `python3 araclar/github-skill-listesi.py`, çakışma ve ücret kontrolü, onaysız ekleme yok |
| Bir kaynağı ya da skili çıkar | `rehber/03` "kaynak/skill çıkar", `promptlar/14` | `python3 araclar/proje-kullanimi.py --skill <kimlik>` (etki), sonra `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` |
| "Skilleri güncelle" (aylık) | `rehber/02`, `promptlar/08` | `python3 -u araclar/arsiv-guncelle.py --aylik`, dal özeti, onay, `--birlestir <dal>` |
| Projeleri kontrol et, proje ekle/çıkar/taşındı | `rehber/10`, `promptlar/12` | `python3 araclar/proje-kullanimi.py --saglik` (kayıtsız klasörleri de tarar) |
| Git durumu, push gecikmesi, geri alma | `rehber/02`, `rehber/13` | `python3 araclar/git-durum.py --kisa` (push yalnız kullanıcı isteyince) |
| HyperFrames / OpenMontage / başka program: kur, güncelle, geri al, çıkar | `rehber/11`, `promptlar/13` | `python3 araclar/program-denetim.py --oncesi <ad>` "HAZIR" demeden dokunma |
| Genel skill klasörlerini boşalt / orada beklenmeyen girdi var | `rehber/12`, `promptlar/16` | `python3 araclar/genel-bekci.py` (yalnız okur); her adım ayrı onay |
| Yedek, geri alma, yedek silme hatırlatması | `rehber/13` | `python3 araclar/yedek-denetim.py` (silmez; silmeyi kullanıcı onaylar) |
| Kütüphane sağlık kontrolü | `promptlar/10` | `python3 araclar/dogrula.py`, `python3 araclar/duman-testi.py` |
| Yeni bilgisayar / klon | `README.md` "Başka bilgisayarda kurmak", `rehber/13` | `python3 araclar/dogrula.py`, `python3 araclar/git-durum.py` |
| Ad çakışması, aynı ad farklı skill | `rehber/09` | `python3 araclar/proje-kullanimi.py --skill <kimlik>` |
| Proje taşındı ya da bozuldu | `promptlar/09` | `python3 araclar/skill-ekle.py <proje> --dogrula` |

## 4. Her zaman geçerli kurallar
1. Kullanıcıyla konu konu, sade Türkçe ile konuş; plan belgesi yığma; en fazla bir soru sor.
2. Gerçek değişiklik (kurulum, kaldırma, taşıma, güncelleme, ayar dosyası, genel klasör, taşıma/silme) önce rapor, sonra kullanıcının ayrı onayı. Önceki onay sonrakini kapsamaz.
3. GitHub'da yalnız `ulukayasaban/SkillKutuphanesi`; push ve PR yalnız kullanıcı isteyince; depo private kalır.
4. Kayıt dosyalarına (`registry.json`, `kaynaklar.json`, `programlar.json` kartları, öncelik) proje adı ya da "şu projeye uyar" gerekçesi yazılmaz. Proje bilgisi `projeler.json` ve `notlar/proje-kullanimi.md`'de.
5. Bilmediğin ya da çelişen bir durumda dur, kullanıcıya sade sor. Gizli anahtar, parola, token değerini asla okuyup yazma; yalnız var mı yok mu söyle.

## 5. Hangi araç hangi dosyayı okur
Claude Code: `CLAUDE.md`. Codex, Antigravity, Cursor, VS Code Copilot: `AGENTS.md`. Gemini CLI ve Copilot CLI bu bilgisayarda kurulu değil,
`GEMINI.md` yok. Windows'ta `skill-ekle.py` çalışmaz; Windows'ta açılan projeler için karar bekliyor (`notlar/kararlar.md` sorular, `rehber/14`). Kurulurlarsa `rehber/14-yapay-zeka-araclari.md` "Yeni AI aracı" yolu izlenir.

## 6. İş bitince
`python3 araclar/kapsam-denetimi.py` (0 sorun), `python3 araclar/dogrula.py` (0 hata), gerekirse `python3 araclar/test.py`;
sonra commit önerisini kullanıcıya söyle. `CLAUDE.md` değiştirdiysen `cp CLAUDE.md AGENTS.md` yap.
```
(Flag claims: `--oner --kuru --evet --dogrula` exist in skill-ekle; `--arac`, `--araclar` are P1's; `--oncesi` P6's; `--hizli`, `--aylik` P4's; `--repo`, `--kuru` of `kaynak-cikar.py` P7's; check F reports any mismatch as UYARI. `--oturum` is not used anywhere.)

### 4.2 `notlar/kararlar.md` (full text; dates from memory files and DURUM.md)

```markdown
# Kalıcı kararlar (kullanıcının verdikleri)

Bu dosyayı her yapay zeka aracının oturumu okur. Kullanıcının kararı burada yazılıdır; konuşmalardaki hafıza kaybolur, bu dosya kalır.
Ekleme: yalnız kullanıcı söyleyince, tarihle, en fazla 3 satır. Silme yok: yerine yenisi gelen karar "Değişen kararlar"a taşınır.
Proje adları bu dosyada serbesttir (kayıt dosyalarında yasaktır, kural 6).

## Geçerli kararlar
- K-01 (2026-10-31) GitHub'da yalnız `ulukayasaban/SkillKutuphanesi` ile işlem yapılır. Başka hiçbir repoda push, PR, birleştirme, dal, issue, yorum yok; proje repolarının (Etsy-Arif, Etsy-Yeni, Akil Disi...) git işlemini kullanıcı yapar. Kütüphanede de push ve PR yalnız kullanıcı isteyince. Depo private kalır (arşivde lisanssız üçüncü taraf kopyalar var).
- K-02 (2026-11-09) Skill ve kaynak yalnız kendi niteliğiyle değerlendirilir (üretici, kapsam, bağımlılık, lisans, ücret, kalite, çakışma). Proje adı ya da "projeye uyar/uymaz" gerekçesi kayıtlara, nota, önceliğe yazılmaz.
- K-03 Skiller projeye yalnız `skill-ekle.py` ile kurulur: önce `--kuru` raporu, kullanıcı onayı, sonra `--evet`. Elle kopyalama yok. `--zorla` yalnız kullanıcı açıkça isterse.
- K-04 (2026-11-10) Bilgisayarın genelindeki skill klasörleri boşaltılacak; skiller yalnız kütüphaneden, yalnız proje klasörüne kurulur. HyperFrames ve OpenMontage programları yerinde kalır, yalnız skilleri taşınır. Her kaldırmadan önce yedek.
- K-05 (2026-11-10) Skill, HyperFrames, OpenMontage ve benzeri yapıların takibi, kontrolü, güncellemesi kütüphane oturumunda yapılır; kullanıcı kendisi yapmaz. Her güncelleme önce yedek, sonra programdan skillere, bir projede deneme, rapor; her biri ayrı onayla. Yeni bir yapı (program) eklenince kullanıcı söyler, burada kayda alınır.
- K-06 (2026-11-10) Diğer araçların genel talimat dosyalarına (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`) kural yazılmaz, hazır metin verilmez. Yeni araç ya da proje açılınca kullanıcı araca bu kütüphane klasörünü verir; yönergeler buradan okunur.
- K-07 (2026-11-10) Genelden kaldırılan skillerin yedeği kullanıcı "sil" diyene kadar durur. Silme zamanı gelince kullanıcıya hatırlatmak ŞARTTIR. Hatırlatma, genel klasörler gerçekten boşaltıldığı gün kurulur. Yedek yeri: `~/Documents/Claude/yedek/` (27 eski genel skill: `global-skills-2026-11-08`; ayar dosyaları: `ayar-2026-11-11`, düz metin anahtar içerebilir).
- K-08 (2026-11-11) İki kapı da AÇIK (kullanıcı "işim bitti" ve "başla" dedi): HyperFrames, OpenMontage, genel klasörler, ayar dosyaları ve proje klasörleri. Bu toplu onay DEĞİL: her güncelleme, kaldırma, taşıma, ayar değişikliği önce yedek, sonra ayrı onay.
- K-09 (2026-11-10) Akıl Dışı projesi Codex'ten Claude'a geçer; geçişi proje içinde kütüphane oturumu yapar. Etsy-Arif, IstatistikYoutube, Akıl Dışı proje düzenlemesi kütüphane oturumunda.
- K-10 (2026-11-07) Etsy-Arif: Arif Windows'ta çalışır, skilleri yalnız kullanır; skiller "sadece Claude" gerçek klasör (`--arac claude`, symlink yok), `CLAUDE.md` kısa blok, `etsy-listings/` ortak kayıt (skili çalıştıran hemen commit/push eder). Arif'in elle kurduğu skiller ve ajan dosyaları Arif'in alanıdır; öneri yazılır, değiştirilmez. Bu iş "bende" kararıyla çelişebilir: sıra gelince kullanıcıya açıkça sor.
- K-11 (2026-11-11) "Psikolojik Danışman Sosyal Medya" ve İstatistik "KIT" paketi önemli değil: işlem yapılmaz, boşaltma bunlar için beklemez, tekrar sorulmaz. Kayıtsız proje taramasında yoksay listesindedir.
- K-12 (2026-11-11) `HYPERFRAMES_SKIP_SKILLS=1` üç yerde tanımlı: `~/.zshrc`, `~/.zshenv`, `~/.claude/settings.json` (env). HyperFrames'in genel klasöre skill yazmasını durdurur. Yedek `ayar-2026-11-11`. `launchctl setenv` ancak ayrı onayla.
- K-13 (2026-11-10) Çalışma tarzı: kullanıcı isteğini söyler; tek konu, sade Türkçe, adım adım; plan belgesi ya da büyük tablo sunulmaz. Bağlam dolmasın diye durum dosyada tutulur, ağır iş alt ajanlara verilir, yanıtlar kısa.
- K-14 Tek oturum sırayla çalışır; paralel oturumlar master'a yazmaz (çakışma yaşandı). Çalışma ağacı (worktree) yalnız kullanıcı isterse.
- K-15 (2026-11-11) Desteklenen yapay zeka araçları bu bilgisayarda kurulu olanlardır: Claude Code, Codex, Antigravity, Cursor, VS Code Copilot. Gemini CLI ve Copilot CLI kurulu değil; `GEMINI.md` desteği isteğe bağlı, kapalı.
- K-16 (2026-11-11) Düzen kararları: en küçük değişiklik, çalışan kod yeniden yazılmaz, mevcut bayraklar ve çıktılar geriye uyumlu; yeni araçlar yalnız Python standart kütüphanesi; rapor araçları salt okur ve `--ozet-json` verir; gizli değer yazdırılmaz (yalnız var/yok); makine geneli klasörlere, kabuk ayar dosyalarına, ayar dosyalarına, zamanlanmış göreve ve proje klasörlerine yazan her işlem ayrı onayla.
- K-17 Ücret: ücretsiz yol önce; `ucretli` = ücret ödemeden hiç kullanılamayan skill; ücretli servis yalnız bir seçenekse `kismen`. Ücretli skill rol çekirdeğine ancak gerekçeyle.
- K-18 Kaynaklar: GitHub "Yapay Zeka Skillleri" listesi tek kaynak listesidir (`yapay-zeka-skillleri`). Yeni kaynak eklemeden önce çakışma ve ücret kontrolü zorunlu, kullanıcı onayı şart. Trend'de olan ve konuya uyan skiller önce önerilir; trend tek başına sebep değildir.
- K-19 Aylık güncelleme `guncelleme/YYYY-AA` dalında yapılır, master değişmez; kullanıcı onaylarsa yerelde `--birlestir`, sonra `git push origin master`. GitHub'daki Merge düğmesi kullanılmaz. Zamanlanmış görev hiçbir şey push etmez.
- K-20 Kütüphane işi gerçek proje üretiminden ayrıdır; istenmedikçe uygulama iskeleti kurulmaz.
- K-21 Kullanıcı Claude'u ne zaman yeniden başlatacağını ajanın söylemesini ister (ayarlar yeni oturumda geçerli olur). Doğru an: arka plan işleri bitip kütüphane commit edildikten sonra.
- K-22 Kütüphane sürümleme: her değişiklikten sonra `kapsam-denetimi.py` (0 sorun) ve `dogrula.py` (0 hata), sonra commit. Commit önerisini kullanıcıya söyle; onaysız commit ve push yok.
- K-23 Yedek ve git eşikleri (rehber/13 ve `git-durum.py`'de yazılı): 5 commit ya da 7 gün push gecikmesi hatırlatılır, `.git` 300 MB, yeni dosya 5 MB, rapor yaşı 45 gün; gizli içerikli yedek en çok 30 gün; yedek silme her zaman kullanıcı onayıyla, araç silmez. (Değerler ilgili araç gelince oraya göre güncellenir.)

## Değişen kararlar (artık geçerli DEĞİL; yeniden uygulama)
- "Global skill klasörleri değişmez; eski agent'lar onlarla çalışmaya devam eder" (README, rehber/01, eski notlar) → 2026-11-10 K-04 ile değişti.
- "Skiller yerinden oynamaz" (2026-11-10 öncesi) → K-04.
- "HyperFrames ve OpenMontage sabit sürüm kopyası olarak kütüphanede" (`CLAUDE.md` eski satır) → 2026-11-11: `kopya: yerinde` kartları (programlar.json).
- "Akıl Dışı Codex'te çalışır" → K-09.
- "Kullanıcı HyperFrames'i Terminal'den kendisi günceller" → K-05 (2026-11-10).
- "Araç düzeni yalnız Claude + Codex (`ikisi` / `claude`)" → K-15 (beş araç; uygulama P1'de).
- "Skill kurulumunda araç sorulmaz" → `--arac` seçimi sorulur (rehber/14).

## Henüz sonuçlanmamış sorular
- HyperFrames ve OpenMontage'ın Claude dışındaki araçlarda girişi (proje `AGENTS.md` notu mu, tek giriş skili mi): boşaltma gününde kullanıcıya sorulacak.
- Windows'ta açılan projelerde varsayılan düzen (kopya mı, symlink mi).
- Aylık görev yalnız Claude zamanlamasıyla mı, her oturum açılışında 35 gün kontrolüyle mi (oturum başı rutini ikincisini kısmen karşılar).
- GitHub'a bekleyen commit'lerin push edilmesi ve ayrıca `git bundle` yedeği.
- Aylık özet/triyaj: ayda en çok kaç aday repo karara bağlansın (N)? Cevaplanana kadar özet yalnız ilk 5 adı gösterir, sınır koymaz (öneri: 5).

## Karar bekleyenler
Aylık özet (`aylik-ozet.py`) bu kutuları toplar. Kutu biçimi: tire, `[ ]`, düz cümle. Karar verilince `[x]` yapılır, silinmez. Başlangıçta boş.

## Kabul edilen bekleyenler (aylık özette susturulur)
Satır biçimi: tire ve bir ifade, istenirse sonuna ` | AAAA-AA-GG` (tarihten sonra susturma biter). İfade en az 8 karakter olmalı. Aylık özet, bu ifadeyi içeren karar cümlelerini göstermez. Kullanıcı "bunu kabul ettim, bir daha sorma" deyince eklenir. Başlangıçta boş.
```

### 4.3 Patch A for `CLAUDE.md` and `AGENTS.md` (apply to `CLAUDE.md`, then `cp CLAUDE.md AGENTS.md`)

```diff
--- CLAUDE.md
+++ CLAUDE.md
@@ -1,3 +1,5 @@
+> Yeni oturumsan önce `BASLA.md` dosyasını oku: okuma sırası, "hangi isteğe hangi komut" tablosu, oturum başı rutini. Kalıcı kararlar: `notlar/kararlar.md`.
+
 # SkillKutuphanesi — Agent Talimatı
@@ skill ekleme akışı adım 1 (P1 metni, aynen)
-1. İhtiyacı netleştir: proje yolu, proje tipi, teknoloji, agent rolleri (bilinmiyorsa sor).
+1. İhtiyacı netleştir: proje yolu, proje tipi, teknoloji, agent rolleri ve hangi AI araçlarıyla açılacağı (Claude Code / Codex / Antigravity / Cursor / VS Code Copilot; Windows'ta açılacak mı). Cevaba göre --arac ortak ya da --arac yalniz-claude ver; rapordaki arac-duzeni, arac-gormez, arac-secimi-yok satırlarını kullanıcıya göster (rehber/14-yapay-zeka-araclari.md). Bilinmiyorsa sor.
@@ ## Bakım isteklerinde (başa)
+- Oturum başı: kütüphane oturumunun ilk işi `python3 araclar/aylik-ozet.py --hizli` (salt okuma, ağsız); çıktıyı kullanıcıya iki cümleyle söyle. Aylık çalışma 35 günü aştıysa "Aylık çalışmayı şimdi yapayım mı?" diye sor; evet derse `python3 -u araclar/arsiv-guncelle.py --aylik`. `dikkat`/`sorun` varsa kendiliğinden düzeltme, silme, push yok. Ayrıntı: `BASLA.md`.
@@ "Skilleri güncelle" maddesi (P4 metni; eski üç adım yerine)
+- "Skilleri güncelle" (aylık) → `python3 -u araclar/arsiv-guncelle.py --aylik` (ön kontrol, rapor, güncelleme/takip dalı, özet, damga) → kullanıcıya dal özeti ve `notlar/aylik-ozet.md` → onay gelirse `--birlestir <dal>` (iki dal türü için aynı).
@@ "Yeni skill ekledim" maddesi (P7 düzeltmesi)
-   … çakışma kontrolü (aynı ad, aynı iş, aynı repoda birden fazla sürüm, global'de farklı sürüm) …
+   … çakışma kontrolü (aynı ad, aynı iş, aynı repoda birden fazla sürüm, aynı adlı kendi skill; genel klasörler boşaltıldıktan sonra global madde geçersiz) … tek ekleme sırası `rehber/03` A1..A9; onay kaydı zorunlu.
@@ (satır 51 değişir; P6 metni)
-- Programlar (skill olmayan yapılar, ör. etsyotomasyon): kullanıcı "dahil et" deyince `programlar.json` kartı + `programlar/<ad>/kaynak/` sabit sürüm kopyası; takip `python3 araclar/program-denetim.py` → `notlar/program-denetimi.md`; güncelleme onayla. Projeye `skill-ekle.py` ile kurulmaz. Ayrıntı: `rehber/11-program-yonetimi.md`.
+- Programlar (skill olmayan yapılar: HyperFrames, OpenMontage, etsyotomasyon): `programlar.json` kartları; HyperFrames ve OpenMontage `kopya: yerinde` (bu bilgisayarda kurulu haliyle izlenir). Her güncelleme, geri alma ve kaldırma kullanıcının AYRI onayıyla ve önce yedekle yapılır: `rehber/11-program-yonetimi.md` → "Taze ajan: istek → adımlar", hazır istem `promptlar/13-program-kur-guncelle.md`. Önce `python3 araclar/program-denetim.py --oncesi <ad>` "HAZIR" demelidir. Projeye `skill-ekle.py` ile kurulmaz.
@@ yeni maddeler (Bakım isteklerinde sonu)
+- Proje takibi: aylık ya da "projeleri kontrol et" denince `python3 araclar/proje-kullanimi.py --saglik` (`notlar/proje-durumu.md`; salt okuma, kayıtsız klasörleri de tarar). Yeni proje / çıkar / taşındı / yoksay: `--ekle`, `--cikar`, `--tasindi`, `--yoksay` (yalnız `projeler.json` değişir, önce plan, onayla `--evet`). Ayrıntı: `rehber/10-proje-kullanimi.md`, `promptlar/12`.
+- Git ve yedek: `araclar/git-durum.py`, `araclar/yedek-denetim.py` (salt okuma); yedek ve geri alma kuralı `rehber/13-yedek-ve-geri-alma.md`. Her yedek `yedekler.json`'a kaydedilir. Push yalnız kullanıcı isteyince.
+- Genel klasörler: beklenmeyen girdi ya da boşaltma için `python3 araclar/genel-bekci.py` (yalnız okur, hiçbir şeyi silme). Boşaltma yalnız `rehber/12-genel-klasor-bosaltma.md` ile, her adım ayrı onayla; hazır istem `promptlar/16`.
+- Kaynak/skill çıkarma, emekli, kayıp kaynak: `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` (yalnız okur: etki + sıralı adımlar + geri alma); onayla uygula. Ayrıntı: `rehber/03` D-G, `promptlar/14`.
+- Aday kararları: `konu-takip.py --karar owner/ad eklendi|reddedildi|izle "neden"` (`populer-tarama.py --karar` kullanma); bekleyenler: `konu-takip.py --bekleyenler` (üç kaynağı özetler).
+- Yeni AI aracı: `rehber/14` bölüm 7 ve `promptlar/15`; aylık araç belgesi kontrolü: `python3 araclar/skill-ekle.py --araclar`.
+- `CLAUDE.md` ve `AGENTS.md` birebir aynı tutulur: birini değiştirince `cp CLAUDE.md AGENTS.md`; `dogrula.py` farkı HATA sayar.
```
Line-number hints refer to the current files; the implementer applies by text match, not by number (the "Yeni skill ekledim" and "Skilleri güncelle" bullets are matched by their first words). Net: about +14 lines. The "Hazır promptlar", "Her değişiklikten sonra", "GitHub" bullets stay as they are. Resulting heading and rules 1-6 are untouched. Every flag written here (`--hizli`, `--aylik`, `--birlestir`, `--karar`, `--bekleyenler`, `--araclar`, `--oncesi`, `--saglik`, `--kuru`) must exist in the tool source when Patch A is applied (check F); the implementer fixes the text to the real name if a package shipped another.

### 4.4 Patch B for rule 1 — APPLY ONLY AFTER THE USER APPROVES (separate commit)

```diff
-1. Global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) **asla** yazma,
-   kopyalama, symlink koyma ya da silme. Skiller sadece kullanıcının verdiği proje klasörüne, sadece `skill-ekle.py` ile kurulur.
+1. Global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) **asla** yazma,
+   kopyalama, symlink koyma ya da silme. Tek istisna: kullanıcının o işlem için AYRI ve açık onay verdiği, önce yedeği alınmış iki iş:
+   (a) `rehber/11-program-yonetimi.md` adımlarıyla program güncelleme, geri alma, kaldırma; (b) `rehber/12-genel-klasor-bosaltma.md`
+   adımlarıyla boşaltma. Onay yalnız o işlem içindir, genel izin sayılmaz. Skiller sadece kullanıcının verdiği proje klasörüne,
+   sadece `skill-ekle.py` ile kurulur.
```
This is the ONLY rule-1 text: P2's `rehber/12` and P6's `rehber/11` cite it and never restate it. Merges P2's proposed clause ("tek istisna: rehber/12 ... ile yapılan, yedekli ve her adımı ayrıca onaylı boşaltma ile onaylı program güncellemesi") and P6's program wording; backup location stays `~/Documents/Claude/yedek/` as in rehber/13. After applying: `cp CLAUDE.md AGENTS.md`, add a "Geçerli kararlar" line in `kararlar.md` with the approval date (K-24), and in the same commit change the first bullet of `promptlar/README.md` "Değişmeyen kurallar" to end with `(tek istisna: onaylı program güncellemesi ve onaylı boşaltma, promptlar/13 ve 16)`.

### 4.5 `README.md` replacement texts

- New line 1 (above the title): `> Yeni oturum mu? Önce [BASLA.md](BASLA.md) · kalıcı kararlar: [notlar/kararlar.md](notlar/kararlar.md)`
- Lines 3-4: `GitHub'da yıldızladığın repolardaki agent skillerinin **yerel, tekrarsız, sürüm takipli arşivi** ve onları **sadece seçtiğin projeye, seçtiğin agent'a** kuran araç seti. Desteklenen araçlar: Claude Code, Codex, Antigravity, Cursor, VS Code Copilot (`yapay-zeka-araclari.json`, `rehber/14-yapay-zeka-araclari.md`).`
- Lines 6-7:
  `- Kütüphane araçları global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) hiçbir zaman yazmaz.` / `  Bu klasörler boşaltılacak (karar: `notlar/kararlar.md` K-04); yöntem ve yedek `rehber/12-genel-klasor-bosaltma.md`, `rehber/13-yedek-ve-geri-alma.md`. Skiller yalnız projenin içine kurulur.`
- Line 71: `Yeni projelerde ve bakımda kopyala-yapıştır kullanılacak 16 prompt: [promptlar/README.md](promptlar/README.md)` (number = row count of `promptlar/README.md` at implementation time).
- Rehberler list, appended:
  `11. [Program yönetimi](rehber/11-program-yonetimi.md): HyperFrames, OpenMontage ve benzeri programların kurulumu, güncellemesi, geri alınması`
  `12. [Genel klasör boşaltma](rehber/12-genel-klasor-bosaltma.md): bilgisayarın genelindeki skill klasörlerini yedekleyip boşaltma`
  `13. [Yedek ve geri alma](rehber/13-yedek-ve-geri-alma.md): yedek envanteri, git geri alma, yeni bilgisayara geri kurma`
  `14. [Yapay zeka araçları](rehber/14-yapay-zeka-araclari.md): hangi araç hangi klasörü ve talimat dosyasını okur, yeni araç ekleme`
- Line 52 (after P3's `.gitignore` is applied): the list from P3 hand-off 5(a): `.gecici/`, `.arsiv-yeni/`, `.arsiv-eski/`, `.guncelleme-kilidi`, `__pycache__/`, `.DS_Store`, `/.env*`, `/*.pem`, `/*.key`, `/*.p12`, `/*.pfx`, `/programlar/**/.env`, `/yedek/`, `/.skill-kutuphanesi/`, `/*.bundle`, `/*.yedek`.
- Restore block (after line 57), P3 hand-off 5(b) plus P8 line:
  `Tam geri kurma listesi, geri gelmeyenler ve makine durumu: [rehber/13-yedek-ve-geri-alma.md](rehber/13-yedek-ve-geri-alma.md). **GitHub'a gönderilmemiş commit'ler klonda yoktur; önce `python3 araclar/git-durum.py` çalıştır.** Klondan sonra `python3 araclar/dogrula.py` ve `python3 araclar/git-durum.py`; skill'lerin kendi `.gitignore` dosyaları yüzünden eksik gelen arşiv dosyası `dogrula.py` tarafından HATA olarak gösterilir.`
- Araçlar table, new rows (flags only from existing specs): `aylik-ozet.py [--hizli]`, `git-durum.py [--kisa] [--ozet-json]`, `yedek-denetim.py [--ozet-json]`, `genel-bekci.py [--ozet-json] [--taban-yaz]`, `program-denetim.py [--oncesi ad] [--sema]`, `kaynak-cikar.py [--kuru]`, and the `proje-kullanimi.py` row appended with ` · --saglik / --tara-kayitsiz / --yetim / --program / --ekle / --cikar / --tasindi / --yoksay`. `duman-testi.py` row gets ` [--kirli-ok]`.

### 4.6 `promptlar/README.md` rows

```
| 13 | [13-program-kur-guncelle.md](13-program-kur-guncelle.md) | HyperFrames, OpenMontage ya da başka bir programı kurmak, güncellemek, geri almak, çıkarmak ya da yeni program kaydetmek |
| 14 | [14-kaynak-cikar.md](14-kaynak-cikar.md) | Kütüphaneden bir kaynak repoyu ya da skili çıkarmak (etki, yedek, geri alma ile) |
| 15 | [15-yeni-yapay-zeka-araci.md](15-yeni-yapay-zeka-araci.md) | Yeni bir yapay zeka aracı kullanmaya başlayınca kütüphaneye tanıtmak, ya da aracın okuma düzeni değişince kontrol etmek |
| 16 | [16-genel-klasor-bosaltma.md](16-genel-klasor-bosaltma.md) | Genel skill klasörlerini yedekleyip boşaltmak ya da orada beklenmeyen bir girdi belirince bakmak |
```
Order after the edit: 01..11, 12, 13, 14, 15, 16. Row 12: `Bir skili/kaynağı hangi projeler kullanıyor (silmeden önce etki); aylık proje sağlık turu; proje ekle/çıkar/taşındı/yoksay`. Intro: `Claude Code, Codex, Antigravity, Cursor ve VS Code Copilot'ta aynen çalışır.` Row texts for 13/16 are P6's/P2's; 14/15 are P8's wording and must be reconciled with the final prompt titles when P7/P1 land.

### 4.7 Optional `GEMINI.md` stub (only if Gemini CLI is ever installed; D1 says off now)
```
Bu klasör bir skill kütüphanesidir. Önce `BASLA.md` dosyasını, sonra `AGENTS.md` dosyasını oku; kurallar orada.
```
Created only after the user decides (needs approval); `dogrula.py` check A2 then verifies it names `BASLA.md`.

### 4.8 `notlar/rafta/OKU.md`
```
# Rafta
Burada eski belgeler durur. Hiçbiri uygulanmaz; yalnız karar geçmişidir.
Güncel bilgi: BASLA.md, CLAUDE.md / AGENTS.md, notlar/kararlar.md.
Raftaki dosyalar bilerek taşındı (git mv); geri almak için: git mv notlar/rafta/<dosya> <eski yer>.
```

### 4.9 dogrula/duman messages (Turkish, as printed)
`CLAUDE.md ile AGENTS.md aynı değil (cp CLAUDE.md AGENTS.md)` · `BASLA.md yok` · `notlar/kararlar.md yok` · `CLAUDE.md ilk satırı BASLA.md'ye işaret etmiyor` · `BASLA.md olmayan dosyayı anıyor: <yol>` · `<paket> dosyası yok: <yol>` · `<belge>:<satır>: araclar/<araç>.py '<bayrak>' bayrağını tanımıyor` · `<belge>:<satır>: olmayan araç araclar/<araç>.py` · `<belge>:<satır>: eski anlatım (...)` · `kaynak kaydında onay yok: <repo> (rehber/03 A4)` · duman `kütüphane araçları ve bu test genel skill klasörlerine yazmadı`, `dogrula.py: bilinmeyen uyarı yok`. (Report-age lines `<yol> <N> gün önce üretilmiş (eşik 45); yenile: <komut>` are printed by `aylik-ozet.py`, not by `dogrula.py`.)

### 4.10 DURUM.md lines (library session, with approval; not P8's file)
After emptying day or when this package lands: `Son güncelleme: <tarih>`; one line under "Hedef": `Tek giriş belgesi: BASLA.md; kalıcı kararlar: notlar/kararlar.md. Bu dosya yalnız geçiş durumunu tutar; iş bitince rafta/'ya taşınır, kararlar kararlar.md'de kalır.` Step 3 row and the "Boşaltma sırası (taslak)" line get `→ rehber/12-genel-klasor-bosaltma.md` (P2 hand-off).

---------------------------------------------------------------------------------------------------

## 5 Tests: `araclar/testler/test_p8-butunluk.py`

Rules (D5): stdlib only; imports `dogrula` and `ortak` via `importlib` from `araclar/`; every case works on a **temp directory** built from fake data (never the real library files, never the real home folders, no network, no subprocess to other tools; the only subprocesses are `git` inside a temp repo for the K cases and tiny fake tool scripts written into the temp tree); prints one line per case; last line `N/N test geçti`; exit 0 only if all pass. Does not call `test.py` (loader recursion). The former "gerçek depo" cases (old 26, 33-36) and P1's real-file case 44 are **not here**: they are acceptance commands in section 10.

Helper: `sahte_kok(**dosyalar)` writes `{relpath: text}` under `tempfile.mkdtemp(prefix="p8-")`; `sahte_git(kok)` runs `git init`, sets a local user and commits (cases are skipped with a printed BİLGİ if `git` is missing).

Cases:
1. `esitlik`: identical `CLAUDE.md`/`AGENTS.md` -> no message; one byte differs -> HATA containing `aynı değil`; `AGENTS.md` missing -> HATA `eksik`.
2. `esitlik`: `GEMINI.md` absent -> no message; present without `BASLA.md` -> UYARI; with it -> none.
3. `giris`: `BASLA.md` and `notlar/kararlar.md` missing -> two **UYARI and no HATA** (R-A); present with all four headings -> none; missing `## Karar bekleyenler` or `## Kabul edilen bekleyenler` -> UYARI.
4. `giris`: `CLAUDE.md` first line without `BASLA.md` -> UYARI; with -> none.
5. `giris` B2: `BASLA.md` mentions `` `araclar/yok.py` `` -> UYARI `olmayan dosyayı anıyor`; existing path -> none.
6. `paket_dosyalari`: missing `rehber/12-genel-klasor-bosaltma.md` -> UYARI (never HATA); `rehber/13` lacking `git revert -m 1` -> UYARI, containing all five strings -> none; `.gitignore` lacking `notlar/son-aylik-calisma.json` or `notlar/aylik-ozet.md` -> UYARI; skipped when `kararlar.md` says `.gitignore değişikliği reddedildi`.
7. E1: `programlar.json` invalid JSON -> HATA; valid but no `programlar` dict -> UYARI; a fake `araclar/program-denetim.py` containing `"--sema"` that prints a JSON object with a `HATA:` line -> UYARI; printing garbage / exit 3 -> UYARI `çalışmadı`; fake tree without `program-denetim.py` -> no subprocess; `giris_yolu.araclar` key not in the E4 key set -> UYARI; the E4 file missing -> cross-check skipped.
8. E2: `projeler.json` with `tarama_kokleri` as a string -> UYARI (not HATA); `yoksay` item without `yol` -> UYARI; nonexistent root -> UYARI; invalid JSON -> HATA.
9. E3: valid `yedekler.json` -> none; duplicate `kimlik`, `gizli_icerir: "belki"`, `surum: 2`, missing field -> UYARI each (no HATA); invalid JSON -> HATA.
10. E4: P1's real shape `{"surum":1,"araclar":[{"anahtar":...}, ...]}` with the five keys and all required fields -> none; missing `vscode-copilot` -> UYARI; record without `dogrulama_tarihi` -> UYARI; `dogrulama_tarihi: "dün"` -> UYARI; `dogrulama_tarihi` 200 days old -> **no message** (staleness is not dogrula's); dict-shaped `araclar` tolerated; invalid JSON -> HATA.
11. E5: `surum: 2` -> UYARI; baseline 60 days old -> no message.
12. E6: record `tip: "EMEKLI"` -> none; `tip: "X9"` -> UYARI; unknown key -> UYARI; string `oncelik` -> UYARI; duplicate repo differing in case -> UYARI; `repo` without slash -> UYARI; **the whole fake file yields no HATA** (P7's mandatory case: the monthly path would not roll back).
13. K (fake git repo, HEAD = legacy `kaynaklar.json`): a genuinely new record without `onay` -> exactly one G-ONAY UYARI and no HATA; a renamed record (`repo` changed, old name in `eski_adlar`) -> not new, no message; the legacy records -> no message; no git / no HEAD -> silent; new `arsivden_cikarilanlar` entry without `onay` or with `<NEDEN` -> UYARI; `tip: "KAYIP"` without `kayip_tarihi` -> G-KAYIP UYARI, with it -> none; fake `araclar/kaynak-cek.py` with `lisans_riskli = lambda l: True` and a new record with a skill whose `lisans` is `AGPL-3.0` and empty `lisans_onay` -> UYARI; with `lisans_onay` -> none; fake `araclar/yol-tara.py` whose `kapi_kontrol` raises -> UYARI `çalışmadı`, returns problems and empty `yol_onay` -> UYARI, with `yol_onay` -> none; modules absent -> gates skipped.
14. F: fake `araclar/a.py` with `add_argument("--var")` and `"--eski" in sys.argv`; fake doc `` `python3 araclar/a.py --var --yok` `` -> exactly one UYARI naming `--yok`; `--var`, `--eski` accepted.
15. F: backslash-continued command joined; flag on the continuation line checked.
16. F: git/gh options after other commands (`` `git status --porcelain` ``) not flagged; a flag in a different backtick span than the tool is not flagged.
17. F: doc mentions `araclar/yok.py` -> UYARI `olmayan araç`; a fake `aylik-ozet.py` containing `"--hizli"` makes `--hizli` valid and `--oturum` in a doc is reported (unknown to the fake tool).
18. F: static extraction handles `sys.argv.index("--uygula")` and single-quoted strings; never executes the tool (a tool whose body is `raise SystemExit("çalıştırıldı")` causes no exception).
19. H: README-like text with the two old sentences -> two UYARI; the corrected sentence -> none; a `rehber/01:5-8` style sentence ("hiçbir zaman değişmez ... reddeder", no "global skill klasörlerin") -> none (false-positive guard).
20. **Merge rule as a test:** run `belge_ve_kayit_denetimleri` on a fake tree where everything is broken at once (missing documents, bad schemas, unknown tip, stale-looking dates, new record without `onay`, bad flags); `hatalar` is empty. Then add (i) one unparsable JSON record file -> exactly one HATA, (ii) `AGENTS.md` != `CLAUDE.md` -> exactly one HATA. No other HATA path exists.
21. `rapor_yasi_satirlari` (ortak): date 50 days before `bugun` in the first lines -> one line with the refresh command; 10 days -> none; file missing -> none; no date in the text and a temp git repo with an old commit date -> uses `%cs`; no date and no git -> skipped, no crash; a date on line 9 only is ignored.
22. `ozet_json_gecerli`: valid object -> ok; extra key tolerated; missing `karar_bekleyen` -> error; `durum: "iyi"` -> error; two JSON objects concatenated -> error; non-string in `satirlar` -> error.
23. `OZET_ARACLARI`: every entry is `(str, list)`; contains `git-durum`, `yedek-denetim`, `genel-bekci`, `program-denetim`, `proje-kullanimi`, `skill-ekle` (`--araclar`), `konu-takip`, `github-trend`, `populer-tarama` (`--bekleyenler`); no duplicate names.
24. `genel_izleri`/`genel_fark` with fake folders: vendor names (`synced`, `.system`, `skills-cursor`) skipped; a new entry -> in `genel_fark`; touch (mtime change) -> in `genel_fark`; identical -> empty; missing folder -> no crash. `genel_parmak_izi` equal for equal trees, different after adding an entry.
25. Loader as a unit: a temp `araclar/testler/` containing `test_ok.py` (prints `2/2 test geçti`, exit 0), `test_kotu.py` (prints `1/2 test geçti`, exit 1), `test_bos.py` (exit 0, no last line); `alt_testler` is loaded from `test.py` source by `ast` (the function text is extracted and executed against a fake `KOK`, so `test.py`'s own `main()` is never run) -> ok passes, kotu fails, bos fails. Empty folder -> BİLGİ and no entries.
26. `cikis` summary compatibility: none needed (the print block is untouched); instead a source-text case on a temp copy of the aggregator call is not added. The real-source assertion that the print block is unchanged is an acceptance command (section 10).

---------------------------------------------------------------------------------------------------

## 6 Hand-off requests

### 6.1 Intake format
See 3.12.

### 6.2 Intake register: requests received and decisions (all seven specs exist; final hand-offs)

Decision classes: **kabul** (applied as asked), **değiştirildi** (applied differently, reason), **reddedildi**, **ertelendi**. Rule applied to every dogrula request: UYARI unless the merge rule (HATA) says otherwise.

| Id | From | Request | Decision |
|---|---|---|---|
| P1-1 | P1 | CLAUDE/AGENTS "Skill ekleme akışı" step 1 text and "Yeni AI aracı" line | kabul: 4.3 (text aynen) |
| P1-2 | P1 | `promptlar/README.md` row 15; `README.md` one line | kabul: 4.5, 4.6 |
| P1-3 | P1 | dogrula: HATA for missing/invalid `yapay-zeka-araclari.json`, missing record fields; HATA for missing `rehber/14`, `promptlar/15`; UYARI for 45-day staleness | değiştirildi: invalid JSON HATA; missing file, record fields, missing documents UYARI (merge rule); the 45-day UYARI **reddedildi** (P1's `--araclar` and the monthly summary report it; `dogrula` stays calendar-free) |
| P1-4 | P1 | schema: `anahtar` list, `dogrulama_tarihi`, `proje_skill_okur`, `proje_talimat_okur` | kabul: E4 rewritten (P8's own field names withdrawn) |
| P1-5 | P1 | duman optional step `skill-ekle.py --araclar --ozet-json` | kabul: in `OZET_ARACLARI`, duman step 11 |
| P1-6 | P1 | BASLA: Windows `skill-ekle.py` note; monthly tool-document check in full mode only | kabul: 4.1 section 5 and section 2 |
| P1-7 | P1 | P1 does not ask P8 for `ortak.py`/`GLOBAL_KLASORLER` changes; P1's real-file test 44 | kabul; test 44 must move to acceptance (D5): section 10 carries the check, P1 is asked to drop case 44 from its test file (6.3) |
| P2-1 | P2 | test.py loader section | kabul: 3.10 |
| P2-2 | P2 | dogrula: baseline UYARI when missing, HATA when invalid, HATA when rehber/12, promptlar/16, genel-bekci.py missing, 45-day baseline UYARI | değiştirildi: missing baseline/files UYARI (C); invalid JSON HATA, `surum != 1` UYARI (E5); the 45-day rule **reddedildi** (`RAPOR_YASI` for the monthly summary) |
| P2-3 | P2 | rule-1 exception wording; session-start line | kabul, merged: Patch B is the single text (4.4), session-start line is P4's `--hizli` sentence (4.3) |
| P2-4 | P2 | `promptlar/README.md` row 16, README rehber row, `notlar/genel-bekci.md` as known generated note | kabul: 4.5, 4.6; no list of generated notes exists in `kapsam-denetimi.py`/`dogrula.py` (grep), nothing to add; the note is in `RAPOR_YASI` |
| P2-5 | P2 | `parmak_izi` unchanged | değiştirildi: P8 moves the skip list to `ortak.py` (A7 is P8's); same semantics |
| P2-6 | P2 | P2 `genel-bekci --ozet-json` in every `aylik-ozet` branch; P3 backup name patterns; P1 `ek_klasorler` step in rehber/14 | not P8's files; no P8 action. P2's decisions enter `kararlar.md` as K-24+ when the user decides |
| P3-1 | P3 | test.py loader | kabul |
| P3-2 | P3 | dogrula: `yedekler.json` HATA schema; `.gitignore` block UYARI (incl. two P4 lines); `rehber/13` strings UYARI | değiştirildi: schema findings UYARI, invalid JSON HATA (E3); `.gitignore` block and `rehber/13` strings kabul (C) |
| P3-3 | P3 | duman: two `--ozet-json` steps | kabul: step 11 via `OZET_ARACLARI` |
| P3-4 | P3 | CLAUDE/AGENTS first step and maintenance line | kabul: merged into the session-start bullet and the "Git ve yedek" bullet (4.3) |
| P3-5 | P3 | README Gönderilmeyenler list, `rehber/13` link, clone warning | kabul: 4.5; the list waits for P3's `.gitignore` decision |
| P3-6 | P3 | BASLA and `kararlar.md` entries (thresholds, 30-day rule, deletion always with approval) | kabul: 4.1 rows, K-23 |
| P4-1 | P4 | `--hizli` instead of `--oturum` everywhere | kabul (mandatory correction): BASLA 2, CLAUDE/AGENTS bullet, duman step 11 `["--hizli"]`, check F finds the flag; `--oturum` appears nowhere in P8's texts |
| P4-2 | P4 | session-start sentence and monthly line (P4 section 6 P8 item 1 and 2) | kabul, verbatim: 4.1 section 2 and 4.3 |
| P4-3 | P4 | `kararlar.md`: `## Karar bekleyenler` with `- [ ]` boxes, `## Kabul edilen bekleyenler (aylık özette susturulur)`, question N | kabul: 4.2 |
| P4-4 | P4 | test.py loader; no dogrula check for P4; rehber/14 note "monthly check in full mode"; BASLA Windows note; promptlar/10 line 8; rehber/08 | kabul: 3.10; dogrula adds only C-table existence + `.gitignore` lines; BASLA 4.1; 3.11 takes promptlar/10 and rehber/08 |
| P4-5 | P4 | `OZET_ARACLARI` use; optionally the four P4 additions | kabul: the list now holds the P1 and P7 tools too (3.8) |
| P4-6 | P4 | stamp file name | `son-aylik-calisma.json` (not `.txt`) everywhere in this spec (C `.gitignore` check) |
| P4-7 | P4 | (P8 asks, 6.3) show report age in the full summary | kabul as an optional request: `ortak.rapor_yasi_satirlari` |
| P5-1 | P5 | test.py loader | kabul |
| P5-2 | P5 | dogrula: `hizli_kontrol`, `adlar_p` extension, `programlar.json` in leakage tuple | kabul: 3.7 existing-line edits |
| P5-3 | P5 | CLAUDE/AGENTS "Proje takibi", promptlar/README row 12 text, README row, BASLA line | kabul: 4.3, 4.5, 4.6, 4.1 |
| P6-1 | P6 | test.py loader + parse `--sema --ozet-json`, only the `programlar.json okunamadı` line fails | kabul (3.10 item 3, changed from the earlier `--siki` check) |
| P6-2 | P6 | dogrula: schema finding UYARI, only unreadable file HATA; `giris_yolu.araclar` keys UYARI | kabul: E1 uses P1's key set built from the `anahtar` list |
| P6-3 | P6 | CLAUDE/AGENTS line 51 | kabul: 4.3 |
| P6-4 | P6 | promptlar/README row 13 | kabul: 4.6 |
| P6-5 | P6 | duman: `program-denetim` must not reach the network | kabul: step 11 runs `--oncesi hyperframes --cevrimdisi --ozet-json` |
| P7-1 | P7 | test.py includes `test_p7-kaynak-yasam.py` | kabul via the loader |
| P7-2 | P7 | dogrula gates G-TIP, G-ONAY, G-LISANS, G-YOL, G-ONAY-CIKAR, G-KAYIP | kabul, UYARI only, new against HEAD, rename test and EMEKLI/unknown-key/string-`oncelik` test included (check K, E6, cases 12-13) |
| P7-3 | P7 | CLAUDE/AGENTS two bullets and the "Yeni skill ekledim" correction | kabul: 4.3 |
| P7-4 | P7 | README rows (`kaynak-cikar`, `--atla`, `--siki`, `--bekleyenler`), promptlar/README rows 14 and 07 | kabul: 4.5, 4.6 |
| P7-5 | P7 | `kararlar.md` question N | kabul: 4.2 |
| P7-6 | P7 | `promptlar/10` line 8 and `rehber/08` paragraph (taken as unowned) | kabul: 3.11 |
| P7-7 | P7 | staleness UYARI (optional) | reddedildi for dogrula; in `RAPOR_YASI` (konu-takip, github-trend, populer-skiller) |
| P7-8 | P7 | optional duman lines for `konu-takip --bekleyenler`, `kaynak-cikar` | kabul for the `--bekleyenler` tools (via `OZET_ARACLARI`); `kaynak-cikar --json` duman line ertelendi (its tests are P7's; duman stays about report tools) |

### 6.3 What P8 asks of other packages

- **P4-A (`aylik-ozet.py`) — required:** the flag is `--hizli` (alias `--oturum` is P4's business; no P8 text uses it): offline, no `gh`, no network, about 5 s (P4: at most about 10 s), writes **nothing** (no `notlar/aylik-ozet.md`), prints at most 15 lines (P4 4.2: one line when all is well, otherwise 3 decisions + 3 attention items + headings), and supports `--ozet-json` (D4 object, exit 0). It runs `git-durum`, `genel-bekci`, `yedek-denetim`, reads the stamp and the last full summary. BASLA.md, CLAUDE/AGENTS and duman step 11 rely on exactly this flag name. P8's earlier condition "15 lines, 20 s" is replaced by P4's 4.2 output. P4's 35-day question sentence is copied verbatim.
- **P4-B:** import `OZET_ARACLARI` from `ortak.py` (3.8) with a built-in fallback (as P4 already designed); the list holds only tools whose spec says `--ozet-json`.
- **P4-C (optional):** in full mode append `ortak.rapor_yasi_satirlari()` lines as `dikkat` (report age). If P4 declines, staleness is simply not shown (the monthly chain regenerates the reports); `dogrula.py` never shows it. `notlar/son-aylik-calisma.json` and `notlar/aylik-ozet.md` are P4's files (the `.gitignore` lines are P3's, checked by C). On a fresh clone the stamp does not exist: P4 should treat "no stamp" as "ilk kurulum, soru yok" (P4's decision; P8's BASLA says only what P4 prints).
- **P1:** (1) `yapay-zeka-araclari.json` shape `{surum, araclar:[...]}` accepted (E4). (2) Drop real-file test case 44 from `test_p1-arac-destegi.py` (D5: real library file); the same checks are in section 10. (3) P1-B: fix `rehber/01-skill-ekleme-sureci.md:12` ("Eski projelerin ve eski agent'ların, global klasörlerdeki skilleri kullanmaya devam eder"; check H reports it until then) and make the rule line consistent with `notlar/kararlar.md` K-04. (4) The project instruction block sentence (library path, "kütüphane oturumuna yönlendir") is P1's (unowned gap taken by P1, Q3).
- **P6:** confirm that `program-denetim.py --oncesi <ad> --cevrimdisi --ozet-json` is valid together (duman step 11 and E1 rely on `--sema --ozet-json` printing one JSON object, exit 0).
- **P7:** (1) `kaynak-cikar.py` flags `--repo`, `--skill`, `--kuru`, `--json` (BASLA uses `--repo ... --kuru`); (2) `tip` values beyond the constant `KAYNAK_TIPLERI` are told to P8 (one constant in `dogrula.py`); (3) P7's implementation adds `kayip_tarihi` to the existing KAYIP record, otherwise G-KAYIP fires at the first run.
- **P2/P3/P5/P6:** nothing new beyond their registers; each keeps its `N/N test geçti` last line and its tests runnable alone with temp directories (D5).
- **Unowned gaps taken by P8** (the orchestrator must add `promptlar/10-kutuphane-saglik-kontrolu.md` and `rehber/08-test-sureci.md` to P8's file list; the edits are tiny, 3.11): `promptlar/10` line 8 and the `rehber/08` paragraph. Not taken (other owners): the `--kayip-isaretle` flag (P4 and P7 both document it as ertelendi: marking a source lost stays the manual step in `rehber/03` E3, user decision); "no stamp on a fresh clone" and "same lost source reported every month" (P4); project-block library path (P1); P6's `--ozet-json` file-writing decision (P6 decided: writes nothing; P4's contract matches).
- **Library session (after approval):** update `notlar/hf-om-gecisi/DURUM.md` with 4.10; first commit of everything (section 9, order).

---------------------------------------------------------------------------------------------------

## 7 Needs the user's approval (at that time; this design approves nothing)

1. **Edit `CLAUDE.md` and `AGENTS.md`, Patch A (4.3).** Includes the new first line, step 1, the programs line and the new bullets (P1, P2, P3, P4, P5, P6, P7 texts merged; no rule changes).
2. **Patch B (4.4): rule 1 exception.** One text, separate patch and commit, only after an explicit yes; needed before the first approved program update or emptying step. After it: `cp CLAUDE.md AGENTS.md`, K-24 in `kararlar.md`, the `promptlar/README.md` bullet, and a question whether to update the Claude memory note `skill-kutuphanesi.md` (outside the library) that still says "global klasörlere dokunma".
3. **Shelve `PLAN.md`, `Kullanılacak Promt Örneği.md`, `notlar/yerel-yapilacaklar-2026-11.md`** into `notlar/rafta/` (`git mv`, 3.6).
4. **`.gitignore` change** is P3's, but README line 52 follows it (README text waits for that decision).
5. **Commit(s).** `git status` was clean today but P8 changes about 14 files; commits only on the user's word. `duman-testi.py` needs a clean tree (or `--kirli-ok` for a pre-commit trial). Ten commits are unpushed: **push only when the user asks** (D12); P8 never pushes.
6. **Optional `GEMINI.md` stub (4.7)** and **`git bundle` second backup** stay user decisions.
7. **Edits to `promptlar/10-kutuphane-saglik-kontrolu.md` line 8 and `rehber/08-test-sureci.md`** (3.11): small documentation edits; the user's yes with the commit.
8. **Any run of `skill-calistir.py` to refresh `TEST_RAPORU.md`** is a long run and a library change: only on request (the monthly chain refreshes it).
9. **DURUM.md edit (4.10)** by the library session.
10. **Raising any new `dogrula.py` UYARI to HATA** (P7 gates, schemas) is a separate later decision.
Not needed: reading files, running `dogrula.py`/`test.py`/`kapsam-denetimi.py` (they do not change the library), running the report tools.

---------------------------------------------------------------------------------------------------

## 8 Deferred and why

- **Real-tool duman steps for Antigravity, Cursor, VS Code Copilot:** no verified headless command exists for them on this Mac; `duman-testi.py --araclar` stays Claude + Codex. Substitute: P1's `--araclar` freshness report in the monthly full summary.
- **`dogrula.py --siki` and a known-warning accept list (`BILINEN_UYARILAR`):** designed first, **removed in review** (extra maintenance, stricter "0 uyarı" rule, calendar dependence). The one known warning (emekli-role line) is filtered locally in duman with an end date. If the need returns it is a ten-line change.
- **Report-age and DURUM.md-age UYARI in `dogrula.py`:** removed; shown only in the monthly full summary via `ortak.rapor_yasi_satirlari` (P4 optional).
- **`GEMINI.md` creation:** D1 (off). Only the optional pointer check A2 and the stub text exist.
- **`dogrula.py --ozet-json`:** not in D4's list of report tools; the monthly summary can read the summary line. Adding it later is a 10-line change.
- **Extending `GLOBAL_KLASORLER` / skill-ekle's security refusal to `~/.cursor/skills`, `~/.gemini/skills`, `~/.copilot/skills`:** would change P1's file behaviour (D2). P8 widened only the read-only fingerprint (`GENEL_IZLEME_KLASORLERI`). Offered to P1 as an option.
- **Checking prose-attributed flags (`` `python3 araclar/x.py` -> `--y` ``):** only same-span flags are attributed (3.7 F) to avoid false positives.
- **Windows (Q1/M2) and `.gitattributes`/CRLF checks:** user decision pending; BASLA states that `skill-ekle.py` does not run on Windows.
- **Scheduled-task SKILL.md copy diff check (B1):** P4 closed it as an information line in `aylik-ozet.py`; dogrula would break duman's "0 uyarı" (P4 asked for no dogrula check).
- **`kapsam-denetimi.py` listing of generated notes:** none exists; nothing to extend.
- **Refreshing `TEST_RAPORU.md`:** 3.6; P8 does not run `skill-calistir.py`.
- **Tests for `duman-testi.py` itself:** integration script that needs the full library; covered by running it at acceptance (section 10), source-text assertions only there.
- **`kaynak-cikar --json` duman smoke line and `--kayip-isaretle`:** P7/P4 (see 6.2, 6.3).

---------------------------------------------------------------------------------------------------

## 9 Risks and how the implementer verifies nothing existing broke

**Order (P8 is last).** All of P1-P7 landed and approved first (Önkoşul at the top). Then in this order, one commit per bullet when the user allows commits: (1) `ortak.py` additions + `dogrula.py` + `duman-testi.py` + `test.py` + `test_p8-butunluk.py`; (2) `BASLA.md`, `notlar/kararlar.md`, `README.md`, `promptlar/README.md`, `promptlar/10` line 8, `rehber/08` paragraph; (3) shelving (approved); (4) Patch A (approved; `cp CLAUDE.md AGENTS.md`, message "AGENTS.md eşitlendi"); (5) later and separately Patch B (approved). Acceptance runs after (4).

**Baseline before editing anything** (record in scratch, not in the library): `python3 araclar/dogrula.py > dogrula-once.txt` (exit code and the list of UYARI lines), `python3 araclar/test.py | tail -1` (N/N), `git status --short`, `wc -l` of the files to be edited. Never run these in the design stage (rule); the implementer runs them.

**Risks**
1. *New HATA breaks the monthly merge.* Mitigation: the merge rule (HATA only for an unparsable existing JSON file and for the CLAUDE/AGENTS difference); test case 20 asserts that any other breakage yields no HATA.
2. *Check F false positives* (docs with `--flag` after a tool that builds the flag dynamically). Mitigation: static string match, same-span attribution, first-run triage with a hit list in the commit message. If more than 10 hits appear, fix documents first (real drift).
3. *Check F false negatives* (flag written in prose). Accepted, section 8.
4. *Summary-line format.* The print block of `dogrula.py` is not edited at all; verify with `git diff -U0 araclar/dogrula.py` (section 10).
5. *duman stricter about report tools.* Step 11 requires every listed tool to exist; run it only at acceptance. It does not judge `durum` (D4). `program-denetim` runs with `--cevrimdisi`.
6. *Fingerprint widened to more folders.* A false failure could come from another program writing during the run (HyperFrames, `skills` tool): the message lists the entries and points to `genel-bekci.py`; rerun when idle.
7. *`CLAUDE.md` grows* by about 14 lines; details stay in `BASLA.md` (user dislikes long instruction files).
8. *Rule-1 exception too broad.* Patch B is per operation, needs the user's AYRI yes, stays a separate commit; `kararlar.md` K-08 repeats that the gate opening is not blanket approval.
9. *`BASLA.md` rots.* Checks B2 (paths) and F (flags) make drift visible in `dogrula.py`; the library session reads UYARI lines at every change.
10. *Shelving breaks a link.* None exists (grep, section 2); re-grep after the move (3.6).
11. *`test.py` loader slows the suite.* Each alt test has a 600 s timeout; unit tests use temp dirs and are fast.
12. *New-record gates invisible after commit* (K): intended; they guard the add procedure (rehber/03 A9 runs dogrula before the commit).
13. *CLAUDE.md/AGENTS.md edited on one side only.* HATA at once; the one-command copy is in `BASLA.md` and in the bullet.
14. *Design-stage slip.* While looking for tool flags, `python3 araclar/arsiv-guncelle.py --help` was started: that tool has no argparse and ran its report. It was stopped after about 2 minutes. Verified afterwards: `git status --short` empty, `.guncelleme-kilidi` absent, `.gecici/` last modified Nov 9, `notlar/` newest file unchanged (Nov 11 18:25). Nothing was written. This is why check F derives flags statically and why the spec forbids `--help` on those twelve tools.

**Verifying nothing existing broke (commands)**
- `python3 araclar/dogrula.py` : same HATA set as the baseline, same UYARI lines plus any new UYARI listed one by one in the commit message.
- `python3 araclar/test.py | tail -1` : `N/N test geçti` with N >= baseline N + number of alt test files; exit 0.
- `python3 araclar/testler/test_p8-butunluk.py` alone : exit 0.
- `python3 araclar/skill-ekle.py --help` unchanged (no edits to skill-ekle).
- `git diff --stat` shows only the owned files (`CLAUDE.md`, `AGENTS.md`, `BASLA.md`, `notlar/kararlar.md`, `README.md`, `promptlar/README.md`, `promptlar/10-kutuphane-saglik-kontrolu.md`, `rehber/08-test-sureci.md`, `araclar/{dogrula,duman-testi,ortak,test}.py`, `araclar/testler/test_p8-butunluk.py`, `notlar/rafta/*`).
- `git diff araclar/ortak.py` shows additions only at the end of the file.
- `cmp CLAUDE.md AGENTS.md` silent.

---------------------------------------------------------------------------------------------------

## 10 Acceptance (commands that prove it is done)

Run from `/Users/sabanulukaya/Documents/SkillKutuphanesi` after P1-P7 landed and after the commit(s) the user approved:
```
python3 araclar/testler/test_p8-butunluk.py            # last line N/N test geçti, exit 0
python3 araclar/test.py | tail -1                       # N/N test geçti (includes the alt test loader), exit 0
python3 araclar/dogrula.py; echo "çıkış: $?"            # 0 hata, çıkış 0; UYARI yalnız emekli-rol satırları (duman'ın kabul ettiği)
python3 araclar/kapsam-denetimi.py                       # sorun: 0
cmp CLAUDE.md AGENTS.md && echo "aynı"
head -3 CLAUDE.md | grep -q BASLA.md && echo "işaret var"
ls BASLA.md notlar/kararlar.md notlar/rafta/
grep -rn "global skill klasörlerin[^$]*değişmez\|eski agent'ların[^$]*devam eder" README.md rehber promptlar BASLA.md CLAUDE.md AGENTS.md   # boş
python3 araclar/aylik-ozet.py --hizli                    # <= 15 satır, hiçbir dosya yazmaz (git status değişmez)
python3 araclar/duman-testi.py                           # tüm adımlar geçer (temiz ağaç gerekir; commit sonrası)
git status --short                                       # boş
```
Read-only checks of the real library (moved here from the test file, D5; each prints nothing on success):
```
grep -q "K-04" notlar/kararlar.md && grep -q "notlar/kararlar.md" BASLA.md && grep -q "aylik-ozet.py --hizli" BASLA.md && ! grep -rq -- "--oturum" BASLA.md CLAUDE.md AGENTS.md
grep -q "^## Karar bekleyenler" notlar/kararlar.md && grep -q "^## Kabul edilen bekleyenler (aylık özette susturulur)" notlar/kararlar.md
ls notlar/rafta/PLAN.md "notlar/rafta/Kullanılacak Promt Örneği.md" notlar/rafta/yerel-yapilacaklar-2026-11.md && test ! -e PLAN.md   # yalnız taşıma onaylandıysa
git diff -U0 <taban-commit> -- araclar/dogrula.py | grep -c 'skill · {len(hatalar)} hata'   # 0: özet satırı basan kod değişmedi
python3 - <<'EOF'   # P1 gerçek dosya denetimi (P1 test 44'ün yeri); salt okuma
import json
d = json.load(open("yapay-zeka-araclari.json"))
a = d["araclar"]; assert isinstance(a, list) and len(a) == 7
assert {r["anahtar"] for r in a} == {"claude-code","codex","antigravity","cursor","vscode-copilot","gemini-cli","copilot-cli"}
assert all("dogrulama_tarihi" in r and "makine_geneli_yazar" not in r for r in a)
print("yapay-zeka-araclari.json tamam")
EOF
```
Pass criteria: `dogrula.py` exit 0 with 0 hata; `duman-testi.py` prints `Duman testi: N/N adım geçti` with no `BAŞARISIZ`; each check of 3.7 shows at least one passing and one failing case in `test_p8-butunluk.py`; Patch B is **not** part of acceptance (applied only on the user's yes, then `cmp CLAUDE.md AGENTS.md` is repeated).

---------------------------------------------------------------------------------------------------

## 11 Review changes

**Applied (mandatory corrections)**
1. `--oturum` -> `--hizli` everywhere: BASLA section 2 and the command table, CLAUDE/AGENTS session-start bullet (4.3), duman step 11 (`["--hizli"]`), P4-A text (6.3, now matching P4's 4.2: at most 15 lines, about 5 s, no network, no file), acceptance, the flag check (F finds `--hizli` in P4's source). P4's session-start sentence (35 days, "Aylık çalışmayı şimdi yapayım mı?", `arsiv-guncelle.py --aylik`) is copied verbatim into BASLA and Patch A.
2. E4 rewritten for P1's real file: `d["araclar"]` is a list, keys from `anahtar`; at least `claude-code, codex, antigravity, cursor, vscode-copilot`; date field `dogrulama_tarihi`; no 120-day staleness (P1's `dogrulama_siniri_gun` 45 and `--araclar` own freshness); P8's requests for `son_dogrulama`, `proje_skill_klasoru`, `talimat_dosyasi` withdrawn. E1's `giris_yolu.araclar` cross-check uses the same key extraction.
3. Register 6.2 extended with P1-1..7, P4-1..7, P7-1..8 and decisions; P7's gates accepted as UYARI only (never HATA, new against HEAD, rename and EMEKLI tests in test cases 12-13); P1's file/rehber existence checks lowered to UYARI; `notlar/kararlar.md` template gained `## Karar bekleyenler` (`- [ ]` boxes) and `## Kabul edilen bekleyenler (aylık özette susturulur)`; Patch A carries P1's step 1, P7's two bullets and the "Yeni skill ekledim" correction (CLAUDE/AGENTS equality kept with `cp`); stamp file named `son-aylik-calisma.json`; P8's "real library" tests (old 26, 33-36) and P1's test 44 moved to acceptance (section 10); the test file uses temp directories and fake data only.
4. `OZET_ARACLARI` (optional correction, applied): now holds `skill-ekle --araclar` and the three `--bekleyenler` tools; duman runs `program-denetim --oncesi hyperframes --cevrimdisi --ozet-json` so it cannot reach the network (`proje-kullanimi --saglik` is local per P5).
5. Implementation order added at the top (Önkoşul 0-8).
6. **Merge rule** (one sentence at the top and R-0): new dogrula checks are UYARI; HATA only for an unparsable existing JSON record file and for CLAUDE/AGENTS inequality. Applied to P1, P2, P3, P6, P7 requests (missing files, schemas, gates all UYARI; BASLA.md and kararlar.md missing also UYARI). Removed: the known-warning accept list (`BILINEN_UYARILAR`, `bilinen_uyari`), `dogrula.py --siki` and the replaced print block, check D report staleness and D2 DURUM age in dogrula. The staleness table moved to `ortak.rapor_yasi_satirlari` for `aylik-ozet.py` (optional P4 request). duman keeps "no unknown warning" with one local, dated filter for the existing emekli-role line instead of the shared list.
7. Patch B pinned as one text (4.4, 3.3); P2/P6 only cite it; the two files are equalised with one `cp` and the commit message says so; applied before the first emptying step with its own approval, rule 1 unchanged until then; the Claude memory note is named as an approval item (section 7).

**Gaps taken:** B2 triage question N (kararlar.md sorular); `promptlar/10` line 8 (the two duplicate "unowned" entries are one item); `rehber/08` paragraph; Windows note in BASLA; the shared "kabul edilen bekleyenler" list (kararlar.md); `--hizli` not showing tool-document age: stated in BASLA section 2 (full mode only). **Not taken (owners named in 6.3):** `--kayip-isaretle` (P4/P7 both ertelendi), KAYIP record `kayip_tarihi` (P7's data edit; G-KAYIP stays clean after it), fresh-clone "no stamp" and repeated lost-source report (P4), project-block library path (P1), P6 `--ozet-json` file writing (P6 decided: none).

**Rejected, with reason:** P1's and P2's 45-day staleness UYARI in dogrula (calendar-dependent warnings in a check that duman and the monthly merge read; shown by the monthly summary instead); P2/P3/P6 HATA for schema or missing files (merge rule); the earlier `--siki` and accept-list design (maintenance weight, stricter duman); P7's duman line for `kaynak-cikar --json` (P7's tests cover it).
