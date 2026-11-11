# P3 Backup inventory and git state: design spec

Önkoşul: uygulama sırası 1. adımdır. Önce (0) commit edilmemiş programlar/ işi kullanıcı onayıyla commit edilir (duman temiz ağaç ister); P3 tamamlanmadan P4 (.gitignore'daki iki satıra bağlı) ve P8 uygulanmaz. Tam sıra: 0 programlar/ commit, 1 P3, 2 P1, 3 P2+P5+P6, 4 P7, 5 P4, 6 P8, 7 CLAUDE/AGENTS Yama B (ayrı onay), 8 genel klasör boşaltması (rehber/12).

Package: P3. Gaps: B5 (git tracking), B6 (backup inventory and reminder, except the skill-ekle.py part), critic scenarios 8, 11, 12 and "push lag".
Owned files (all new except .gitignore): araclar/git-durum.py, araclar/yedek-denetim.py, yedekler.json, rehber/13-yedek-ve-geri-alma.md, .gitignore (edit), araclar/testler/test_p3-yedek-git.py.
Generated on demand only (never by default): notlar/git-durumu.md, notlar/yedek-durumu.md (written only with --rapor).

Note on names: ozet-bolum2-4.md calls the guide rehber/12-yedek-ve-geri-alma.md. Decision D11 wins: it is rehber/13-yedek-ve-geri-alma.md (rehber/12 is P2's boşaltma guide). README.md is not owned by P3 (D5): its changes are hand-off requests (section 6).

---------------------------------------------------------------------------------------------------

## 1 Purpose

1. git-durum.py: one read-only command that tells a library session (an agent without memory) whether the library's git state is healthy: push lag (the 9 unpushed commits nobody tracks), dirty tree, untracked folders (programlar/hyperframes, programlar/openmontage), leftover or pending branches, repo size, new big files, secret-like tracked file names, missing .gitignore protections, files hidden from git inside arsiv/, and (optionally) whether the GitHub repo is still private. It never pushes, never deletes, never fetches unless --uzak.
2. yedek-denetim.py + yedekler.json: the single inventory of backups kept outside the library (today: two folders in ~/Documents/Claude/yedek). Per backup: what it is, date, how to restore, delete trigger, contains secrets. The tool checks existence, age, permissions, wrong location, unregistered folders, and prints a "ready to delete" list. It never deletes.
3. rehber/13: one rule for where backups go and how they are named, restore steps per kind, retention and reminder rule, restoring the library on a new computer from GitHub alone (what returns, what does not), the list of machine state outside the library, and what to do when the GitHub login has expired.
4. .gitignore: root-anchored protections for secret-like files and backup folders that must not break arsiv/ (which legitimately tracks third-party `.env*` examples).

What this closes:
- B5: ahead/behind report, dirty/untracked report, leftover branch report, size threshold, public-repo warning, secret pattern, .gitignore protections, revert -m 1 and after-push rollback written (in rehber/13; the pointer in rehber/02 is a hand-off to P4), new-machine restore list.
- B6: backup inventory, age/existence, ready-to-delete list, secrets flag, retention rule. NOT closed here: `yedekle()` in skill-ekle.py writing `.skill-kutuphanesi/.gitignore` (P1 owns skill-ekle.py; hand-off in section 6).
- Scenario 8 (Mac restored from backup): machine-state inventory (names only) and the plain-text-key backup warning.
- Scenario 11 (GitHub login expired): "local-only mode" list and the `gh auth login` instruction (user does it himself).
- Scenario 12 (fresh clone): what the clone contains, how arsiv/ is tracked, verification commands.
- Push lag: thresholds, session-start one-liner (--kisa), monthly summary feed (--ozet-json).

---------------------------------------------------------------------------------------------------

## 2 Existing behaviour relied on (file:line)

Library code and conventions
- araclar/ortak.py:11 `KOK = Path(__file__).resolve().parent.parent` is the library root. New tools use `from ortak import ...` after `sys.path.insert(0, str(Path(__file__).parent))` exactly like araclar/program-denetim.py:26 (`from ortak import KOK, gh_api, json_oku  # noqa: E402`).
- ortak.py:44-48 `json_oku(yol, varsayilan=None)` returns default when file absent; ortak.py:51-56 `json_yaz` writes atomically (temp file then os.replace). yedekler.json is read with json_oku. The tools never write yedekler.json (agent edits it by hand in a library session, with approval); the report files are written with plain write_text like program-denetim.py:340-342.
- ortak.py:37-41 `GLOBAL_KLASORLER` = ~/.claude/skills, ~/.codex/skills, ~/.agents/skills. yedek-denetim.py imports it to refuse backup locations inside skill-scanned folders (plus ~/.openmontage, added locally as a constant).
- ortak.py:188 `GURULTU` regex (noise names: .DS_Store, __pycache__, .git, ...). Used to filter "ignored arsiv files" the same way as dogrula.py:226-230.
- araclar/program-denetim.py:78 uses `["git", "--no-optional-locks", "-C", path, ...]`: read-only git that does not refresh the index. Same for git-durum.py.
- araclar/program-denetim.py:293-346: report-tool shape (`main(argv=None)` returns int, `if __name__ == "__main__": sys.exit(main())`, report file skipped when only the date changed: lines 339-341). Reused.
- araclar/program-denetim.py:10 docstring ("Çıkış kodu her zaman 0"; lines 2-11 state read-only): convention reused. P3 tools keep exit 0 except with --siki (D4).

Git facts (measured read-only on 2026-11-11)
- `git rev-list --left-right --count origin/master...master` printed `0 9`: behind 0, ahead 9. origin/master tip date 2026-11-09. Remote: origin https://github.com/ulukayasaban/SkillKutuphanesi.git. Local branches: master, skill/lottiefiles-motion-design (merged, dated 2026-11-07). No custom hooks in .git/hooks. .git is 207 MB (pack 128.97 MiB + loose 70.25 MiB, count-objects). 33889 tracked files. registry.json is 22 MB, arsiv/ 367 MB.
- `git ls-files | grep -v '^arsiv/'` against secret-like names: no hit. Inside arsiv/ four tracked hits (third-party examples: n8n `.env.queue.example`, `.env.single.example`, ecommerce-competitor-analyzer `.env.example`, and `foundry-agentic-loop/evals/fixtures/rapid-locked/.env`). So a name scan must exclude arsiv/ or it gives false positives (bosluk-elestiri, akis-06 second reading).
- 32 nested `.gitignore` files exist under arsiv/ (find count). `git ls-files --others --ignored --exclude-standard --directory` currently lists only .DS_Store, .gecici/, araclar/__pycache__/, notlar/.DS_Store: no arsiv file is hidden from git today. `git ls-files -ci --exclude-standard | wc -l` prints 1 (one tracked-but-ignored arsiv file; baseline for the .gitignore check).
- Root .gitignore today (6 lines): `.gecici/`, `.DS_Store`, `__pycache__/`, `.arsiv-yeni/`, `.arsiv-eski/`, `.guncelleme-kilidi`. README.md:52 lists exactly these as "Gönderilmeyenler".
- araclar/dogrula.py:225-230: `git status --ignored --porcelain arsiv`; every `!! ` line that is not GURULTU becomes a HATA ("git'e girmeyen arşiv dosyası ... -> git add -f arsiv"). araclar/arsiv-guncelle.py:219 runs `git add -f arsiv` after an update so nested .gitignore files cannot hide archive files. Conclusion: arsiv/ is fully tracked via `-f`; a fresh clone is complete as long as that holds; the one-line check in git-durum reuses dogrula's command.
- araclar/arsiv-guncelle.py:157-159 and 247-248 stop on a dirty tree; :252 merges with `git merge --no-ff ... -m "Birleştir: <dal> (kullanıcı onayıyla)"`; :253-259 runs dogrula, kapsam-denetimi, test and `git reset --hard <önceki>` on failure ("master eski hâline döndürüldü"). Only for guncelleme/* branches. The takip/* branch merge (`git merge --no-ff`) has no such guard (scheduled task SKILL.md:42).
- Scheduled task SKILL.md (outside the library: ~/.claude/scheduled-tasks/skill-kutuphanesi-aylik-guncelleme/SKILL.md): line 16 stops on a dirty tree except notlar/proje-kullanimi.md; line 18 lists `guncelleme/*` and `takip/*` branches and refuses to open a new one; lines 27-28 delete the takip/* branch on error; line 43 reminds the user about push and PR. git-durum.py mirrors the line-16 exception.
- rehber/02-guncelleme-yonergesi.md:97 says only `git revert HEAD` for rollback. For a `--no-ff` merge commit this needs `-m 1`; there is no after-push rollback text. rehber/13 supplies both (hand-off to P4 for a pointer in rehber/02).
- rehber/02:62-83 (GitHub'a gönderme), README.md:44-57 (private repo, two-command clone), CLAUDE.md:54 ("her değişiklikten sonra ... git commit") and CLAUDE.md rule 5 (only ulukayasaban/SkillKutuphanesi may be touched on GitHub).
- araclar/duman-testi.py:61 and :80 compare `git status --porcelain` (clean tree expected).

Backup facts
- `ls -la ~/Documents/Claude/yedek` (names, sizes, dates only): two folders.
  - `ayar-2026-11-11/` (created 2026-11-11 18:22): `claude-settings.json.yedek` (8261 bytes, mode 600), `zshenv.yedek` (56 bytes, 600), `zshrc.yedek` (1434 bytes, 600). Origin: notlar/hf-om-gecisi/DURUM.md:35-41 (settings env + ~/.zshrc + ~/.zshenv got a HYPERFRAMES_SKIP_SKILLS line; "geri almak = yedeği yerine kopyalamak"). The audit (elestiri-donus.md scenario 8) says zshrc.yedek carries a plain-text key line: so gizli_icerir = evet. I did not open any file.
  - `global-skills-2026-11-08/` (2026-11-08, content moved 2026-11-09 12:50 / 2026-11-10 13:30): `agents-skills/` (28 entries), `claude-skills-linkler/` (28 entries), `LISTE.md` (3290 B), `geri-al.sh` (414 B), `tasi.sh` (9470 B), `kilit-temizle.py` (776 B). Origin: DURUM.md:21 ("27 eski genel skill yedeğe taşındı ... kullanıcı 'sil' diyene kadar durur") and DURUM.md:27 (reminder on the day the folders are really emptied).
- rehber/11-program-yonetimi.md:57-61: program backups go only to `~/Documents/Claude/yedek/<program>-<YYYY-AA-GG>/`; never into the library or git; `~/.hyperframes` backup excludes config.json; `~/.config/openmontage` key folder is never copied; the backup is kept until the update is verified and deleted only after asking the user.
- araclar/skill-ekle.py:57 (`META = ".skill-kutuphanesi"`), :238-263 `yedekle()` keeps the last `YEDEK_SAYISI = 10` (:61) backups in the project under `.skill-kutuphanesi/yedek/<zaman>/`, restored by `--geri-al [ad]` / listed by `--yedekler` (rehber/01:118-119). These project backups are automatic and are NOT recorded in yedekler.json (reason in section 8).
- rehber/04-kontrol-listesi.md:76: `.skill-kutuphanesi/yedek/` should be in the project's .gitignore (recommendation only). rehber/05-risk-ve-onlemler.md:45: backup SKILL.md files must stay outside skill folders (agents would load them).
- CLAUDE.md rule 1 and DURUM.md "İki kapı": machine-wide folders and settings change only with per-action approval, backup first.

---------------------------------------------------------------------------------------------------

## 3 Changes per file

### 3.1 .gitignore (edit, append at the end; nothing existing is removed or reordered)

Old: 6 lines. New: the same 6 lines followed by exactly:

```
# Gizli bilgi ve yedek korumaları. Hepsi kök düzeyine bağlı (başında /): arsiv/ içindeki üçüncü taraf
# dosyalar (ör. .env.example) etkilenmez, dogrula.py'deki "git'e girmeyen arşiv dosyası" denetimi bozulmaz.
/.env
/.env.*
!/.env.example
/araclar/.env
/*.pem
/*.key
/*.p12
/*.pfx
/programlar/**/.env
# Yedekler kütüphanenin dışında tutulur (rehber/13). Yanlışlıkla kök ya da proje klasörüne düşerse git'e girmesin.
/yedek/
/.skill-kutuphanesi/
/*.bundle
/*.yedek
# P4 yerel damga ve özet: makineye özgü, her koşuda değişir, git'e girmez (aylik-ozet 'yoksayılmıyorsa yazma' kontrolü yapar).
/notlar/son-aylik-calisma.json
/notlar/aylik-ozet.md
```

Why each pattern: `/.env` and `/.env.*` (with `!/.env.example` so an example file could still be committed), `/araclar/.env` (tool folder), `/*.pem /*.key /*.p12 /*.pfx` (key material at root), `/programlar/**/.env` (exact name `.env` only: `programlar/etsyotomasyon/kaynak/.env.example` stays trackable), `/yedek/` and `/*.yedek` and `/*.bundle` (backups; bundle = optional git bundle second copy), `/notlar/son-aylik-calisma.json` and `/notlar/aylik-ozet.md` (P4's local stamp and summary; mandatory request from P4: without them aylik-ozet refuses to write and `--aylik` would dirty the tree on every run), `/.skill-kutuphanesi/` (if skill-ekle.py is ever run on the library root itself, its backups must not enter git).
Rejected on purpose: unanchored `.env`, `.env.*`, `*.key`, `token*` (the audit's refuted suggestion): they would hide new arsiv/ files and trip dogrula.py:226-230.
Verification (implementer): `git status --short` identical before and after; `git ls-files -ci --exclude-standard | wc -l` stays 1; `git check-ignore -q .env && git check-ignore -q x.pem && git check-ignore -q yedek/x && git check-ignore -q notlar/son-aylik-calisma.json && git check-ignore -q notlar/aylik-ozet.md && ! git check-ignore -q programlar/etsyotomasyon/kaynak/.env.example` and `git check-ignore -v arsiv/ornek/.env` must not show a `.gitignore` (root) rule (only nested arsiv rules may appear).
Approval: yes, section 7 item 1 (library rule list, `.gitignore` is on the audit's "needs approval" list).

### 3.2 araclar/git-durum.py (new, about 330 lines)

Module docstring (Turkish): purpose, read-only guarantee ("push etmez, dal silmez, dosya değiştirmez; --uzak yalnız `git fetch origin` yapar"), exit codes, usage.

Imports: argparse, json, os, re, subprocess, sys, time, datetime.date; `from ortak import KOK, GURULTU`.

Constants:
```
BEKLENEN_DEPO = "ulukayasaban/SkillKutuphanesi"   # CLAUDE.md kural 5
ANA_DAL = "master"
ESIK_ONDE_COMMIT = 5        # gönderilmemiş commit sayısı: dikkat
ESIK_ONDE_GUN = 7           # en eski gönderilmemiş commit yaşı: dikkat
ESIK_GIT_MB = 300           # .git boyutu: dikkat
ESIK_YENI_DOSYA_MB = 5      # yeni eklenen/izlenmeyen dosya: dikkat
ESIK_BEKLEYEN_DAL_GUN = 45  # guncelleme/* ve takip/* dalı bu kadar gündür bekliyorsa dikkat
ZAMAN_ASIMI = 60            # her git komutu için saniye (fetch 120, gh 20)
BEKLEYEN_DAL_ONEKLERI = ("guncelleme/", "takip/")
GIZLI_AD = re.compile(r"^(?:\.env(?:\..+)?|.*\.(?:pem|key|p12|pfx|keystore|jks)|id_(?:rsa|dsa|ecdsa|ed25519)\b.*|"
                      r"\.npmrc|\.netrc|\.pypirc|\.git-credentials|credentials(?:\..*)?|tokens?(?:\..*)?|secrets?(?:\..*)?|.*\.yedek)$", re.I)
GIZLI_MASKE_SONEKLERI = (".example", ".sample", ".template", ".dist")   # .env.example gizli sayılmaz
KORUMA_PROBLARI = [".env", "ornek.pem", "ornek.key", "yedek/ornek", ".skill-kutuphanesi/yedek/ornek",
                   "notlar/son-aylik-calisma.json", "notlar/aylik-ozet.md"]
```
(GIZLI_AD is the same family as ortak.py:469 `_YOL_GIZLI_AD`; it is duplicated, not imported, because ortak.py is a shared file P3 cannot edit and the name is private.)

Functions (signatures binding):
- `git(depo, *args, zaman=ZAMAN_ASIMI) -> (kod:int, cikti:str)`: runs `["git", "--no-optional-locks", "-C", str(depo), *args]`, `capture_output=True, text=True, stdin=subprocess.DEVNULL`; on TimeoutExpired/OSError returns `(124, "")`.
- `origin_depo_adi(url) -> str|None`: regex `github\.com[:/]+([\w.-]+/[\w.-]+?)(?:\.git)?/?$`; None for non-GitHub URLs.
- `bilgi_topla(depo, uzak=False, gh_kullan=True) -> dict` (keys below).
- `degerlendir(b) -> (durum, bulgular)` where each finding is `{"seviye": "sorun"|"dikkat"|"bilgi", "metin": str, "karar": str|None}`; durum is the worst level (`bilgi` counts as temiz).
- `ozet_json(b, durum, bulgular) -> dict`, `kisa_metin(...) -> str`, `tam_metin(...) -> str`, `rapor_md(...) -> str`.
- `main(argv=None) -> int`.

`bilgi_topla` collects (every git call via `git()`; none writes):
1. `depo_var`: `rev-parse --is-inside-work-tree` == "true". If false: return `{"depo_var": False}` and the evaluation gives one `sorun` finding "Kütüphane git deposu değil: <yol>".
2. `dal`: `branch --show-current` (empty string = detached HEAD).
3. `origin_url`: `config --get remote.origin.url`; `origin_depo` = `origin_depo_adi(url)`.
4. If `uzak` is True: allowed only if `origin_depo is None or origin_depo == BEKLENEN_DEPO`; runs `fetch origin` (zaman 120) once; result stored as `uzak_sonuc` in {"alindi", "hata", "reddedildi"} with the first 160 characters of git's stderr for "hata". "reddedildi" = origin is a GitHub repo other than BEKLENEN_DEPO (library rule 5). Never `--prune`, never `pull`, never `push`.
5. `ahead`/`behind`: `rev-list --left-right --count origin/master...master` -> `behind, ahead` (note the order: left is origin). None when `refs/remotes/origin/master` does not exist.
6. `son_uzak_tarih`: `log -1 --format=%cs origin/master`; `en_eski_gun`: `log origin/master..master --format=%ct`, minimum timestamp, converted to whole days (`(now - ts)//86400`), None when ahead == 0.
7. `degisen` and `izlenmeyen`: `status --porcelain=v1 -z`; split on NUL; entries with status `??` go to `izlenmeyen` (folders end with `/`), others to `degisen`; for status codes R and C the next NUL field is the old path and is skipped. Both lists sorted.
8. `arsiv_gizli`: `status --ignored --porcelain arsiv` lines starting `!! ` whose path (without the prefix and trailing slash) does not match `GURULTU` (same logic as dogrula.py:226-230). Count and first 5 paths.
9. `yerel_dallar`: `for-each-ref --format=%(refname:short)%09%(committerdate:unix) refs/heads`; for each name != ANA_DAL: `birlesmis` = `merge-base --is-ancestor <ad> master` exit 0; `onde` = `rev-list --count master..<ad>`; `gun` = whole days since committer date; `bekleyen` = name starts with a prefix in BEKLENEN_DAL_ONEKLERI.
10. `uzak_bekleyen`: `for-each-ref --format=%(refname:short) refs/remotes/origin/guncelleme refs/remotes/origin/takip` names (as of the last fetch) not present as local branches.
11. Size: `git_mb` = (`count-objects -v`: size + size-pack, both KiB) / 1024 rounded to 1 decimal; `en_buyuk`: top 5 tracked files by size (`ls-files -z`, `os.lstat` each, skip missing and symlinks); `yeni_buyuk`: files in `diff --name-only --diff-filter=A origin/master master` plus untracked files (folders: sum of file sizes with a 20000-entry cap) whose size >= ESIK_YENI_DOSYA_MB. Added files only (not modified): registry.json changes every month and is already 22 MB.
12. `gizli_adlar`: tracked names (from the same `ls-files -z`) outside `arsiv/` whose basename matches `GIZLI_AD` and does not end with a `GIZLI_MASKE_SONEKLERI` suffix; `gizli_arsiv_say`: number of such names inside `arsiv/` (reported as information only, names not listed).
13. `koruma_eksik`: for each path in KORUMA_PROBLARI, `check-ignore -q --no-index -- <yol>`; exit 1 = not ignored -> listed. (exit 0 = ok; any other exit = "bilinmiyor", not listed.)
14. `stash`: number of lines of `stash list`.
15. `gorunurluk`: only when `gh_kullan` and `origin_depo == BEKLENEN_DEPO`: `gh repo view <depo> --json visibility --jq .visibility` (zaman 20); output lowercased: "private" / "public" / "internal"; any non-zero exit or missing `gh` -> None and no finding (skipped quietly; the full text prints one line "depo görünürlüğü: denetlenemedi (gh oturumu yok ya da ağ yok)").

`degerlendir` rules (finding level, exact Turkish text in section 4):
- sorun: not a git repo; origin is a GitHub repo other than BEKLENEN_DEPO; `ahead > 0 and behind > 0` (diverged); `gorunurluk` in ("public", "internal"); `gizli_adlar` non-empty; `arsiv_gizli` count > 0.
- dikkat: detached HEAD or branch != master; `ahead >= ESIK_ONDE_COMMIT` or (`ahead > 0` and `en_eski_gun > ESIK_ONDE_GUN`); `behind > 0` and `ahead == 0`; `degisen` non-empty (info instead when the only changed file is `notlar/proje-kullanimi.md`, mirroring the scheduled task's exception, SKILL.md:16); `izlenmeyen` non-empty; any local non-master branch that is merged (leftover; decision line), a non-merged non-pending branch (decision line), a pending guncelleme/takip branch of ANY age as a decision line (the scheduled task refuses to open a new branch while one exists, SKILL.md:18), plus the 45-day escalation in the text; `git_mb > ESIK_GIT_MB`; `yeni_buyuk` non-empty; `koruma_eksik` non-empty; `uzak_sonuc == "hata"` is NOT dikkat (see the next line).
- bilgi: ahead/behind numbers, last remote commit date, pending branches with age, `stash` > 0, top 5 biggest files, `.git` size, arsiv name-match count, `uzak_sonuc` result, visibility "private" ok line, origin unknown (`origin/master` missing).
- `uzak_sonuc`: "hata" = bilgi (login or network; text points to rehber/13 "GitHub oturumu bitince"); "reddedildi" = sorun.
Overall durum: any sorun -> "sorun"; else any dikkat -> "dikkat"; else "temiz".

CLI (argparse, description "Git durumu (salt okuma)"):
- `--depo PATH` (default `str(KOK)`; used by tests).
- `--uzak` (fetch origin first; only network action).
- `--gh-yok` (skip visibility check).
- `--kisa`: skips the gh visibility check (offline-safe, no 20 s wait at session start; same as --gh-yok) and prints one line "git: temiz" or only dikkat/sorun lines (for the session-start line in CLAUDE.md/AGENTS.md).
- `--ozet-json`: prints exactly one JSON object (D4) and nothing else on stdout; nothing is written. Any unexpected exception inside the tool is caught and printed as `{"arac": "git-durum", "durum": "sorun", "satirlar": ["araç hatası: <ilk 120 karakter>"], "karar_bekleyen": []}`; exit still 0.
- `--rapor` and `--cikti PATH` (default `KOK/notlar/git-durumu.md`): write the Markdown report. Without `--rapor` nothing is ever written (a default-written report would dirty the tree on every run). Skip the write when only the date line changed (same trick as program-denetim.py:339-341).
- `--siki`: exit 1 when durum == "sorun".
- `--ozet-json` combined with `--kisa` or `--rapor` is an argparse error (exit 2).
Exit codes: 0 = ran correctly (whatever it found); 1 = only with --siki and durum "sorun"; 2 = argparse usage error (existing tool convention).

JSON example (`python3 araclar/git-durum.py --ozet-json`, today's real state would print about this):
```json
{"arac": "git-durum", "durum": "dikkat",
 "satirlar": ["GitHub'a gönderilmemiş 9 commit var (en eskisi 2 gün önce; son bilinen uzak commit 2026-11-09)",
              "Kaydedilmemiş değişiklik: 9 dosya",
              "İzlenmeyen klasör: programlar/hyperframes/, programlar/openmontage/",
              "Birleşmiş artık dal: skill/lottiefiles-motion-design (master'a zaten girmiş)"],
 "karar_bekleyen": ["9 commit GitHub'a gönderilsin mi? (push yalnız sen isteyince yapılır)",
                    "programlar/hyperframes/ ve programlar/openmontage/ commit edilsin mi?",
                    "skill/lottiefiles-motion-design dalı silinsin mi? (git branch -d, birleşmiş)"]}
```
`satirlar`: only sorun/dikkat findings, worst first, at most 10 (remaining counted: "... ve N satır daha"); when durum is temiz: `["Git temiz: master GitHub ile aynı, değişiklik yok."]`.
`karar_bekleyen`: the `karar` text of findings that need a user decision, same order, at most 10.

Human output (default, no flags): header line, then one line per finding with prefix `SORUN`, `DİKKAT`, `bilgi`, then the section "Karar bekleyenler". Plain words, no secrets. Example in section 4.

Markdown report (`--rapor`): title "# Git Durumu", a one-line note "`araclar/git-durum.py` üretir · <tarih> · salt okuma", table of findings (Seviye, Bulgu), list of decisions, top-5 biggest files table. Content is generated from the same findings (single source).

Performance: `ls-files` + 33.9k lstat calls and `status --ignored arsiv` (about 1.3 s measured) total under 5 s on this repo.

### 3.3 araclar/yedek-denetim.py (new, about 300 lines)

Module docstring: purpose; "Hiçbir şeyi silmez, taşımaz, kopyalamaz; dosya içeriği açılmaz (yalnız ad, boyut, izin, tarih okunur); gizli değer yazdırılmaz."

Imports: argparse, json, os, sys, datetime.date/datetime, pathlib.Path; `from ortak import KOK, GLOBAL_KLASORLER, json_oku`.

Constants:
```
VARSAYILAN_KAYIT = KOK / "yedekler.json"
TURLER = ("ayar-dosyasi", "genel-skill-klasoru", "program", "proje", "kutuphane-dali", "git-paketi", "diger")
ZORUNLU = ("kimlik", "yol", "tur", "ne", "tarih", "geri_yukleme", "gizli_icerir")
YAS_UYARI_GUN = 90          # kayıtta yas_uyari_gun yoksa
YAS_UYARI_GUN_GIZLI = 30    # gizli_icerir == "evet" ise varsayılan
GIT_PAKETI_GUN = 90         # ikinci_kopya_iste açıkken git-paketi en fazla bu kadar eski olabilir
BOYUT_TARAMA_SINIRI = 20000 # boyut toplarken en çok bu kadar girdi gezilir
TARAMA_KLASORLERI = list(GLOBAL_KLASORLER.values()) + [Path.home() / ".openmontage"]
```

yedekler.json format (version 1). Top-level keys:
- `_aciklama` (str), `surum` (int, 1), `kok` (str, default "~/Documents/Claude/yedek"), `ikinci_kopya_iste` (bool, default false), `yedekler` (list of records).
Record fields:
| field | type | required | meaning |
|---|---|---|---|
| kimlik | str | yes | unique; equals the folder or file name (`ayar-2026-11-11`); form `<ne>-<YYYY-AA-GG>` (+ `-2` for a second one on the same day) |
| yol | str | yes | absolute or `~/...` path of the backup folder/file |
| tur | str | yes | one of TURLER |
| ne | str | yes | plain-language description: what was backed up, why |
| tarih | str | yes | `YYYY-AA-GG` creation date (not file mtime) |
| geri_yukleme | str | yes | how to restore, in plain steps, no secret values; points to rehber/13 section |
| gizli_icerir | str | yes | "evet" or "hayir" |
| beklenen | [str] | no | names that must exist directly inside `yol` (names only) |
| silme_gun | int | no | ready to delete when age >= this many days (and the event, if any, is done) |
| silme_olay | str | no | named event that must happen first; the library session sets `silme_olay_tamam` to true after the user confirms the event |
| silme_olay_tamam | bool | no | default false |
| yas_uyari_gun | int | no | overrides the age warning threshold |
| durum | str | no | "tutuluyor" (default) or "silindi" |
| silindi_tarih | str | no | set together with durum "silindi" |
| not | str | no | free note |
| kayit | str | no | the backup's own restore data file inside `yol` (e.g. `KAYIT.json` written by program updates, P6: version, commit). yedekler.json stays the ONLY inventory; `kayit` just points to that file. If set, `kayit` must be a name that also appears in `beklenen` or exists in `yol` (name check only, never opened) |
A record with durum "silindi" is kept as history and skipped by every check. Deleting a backup is always a hand action approved by the user at that time; after it the session sets durum and silindi_tarih.

Initial yedekler.json (exact proposal; dates and names read from ls):
```json
{
  "_aciklama": "Kütüphane dışındaki yedeklerin envanteri. Tek kural: yedek ~/Documents/Claude/yedek altında durur, <ne>-<YYYY-AA-GG> diye adlanır, burada kayıtlıdır (rehber/13-yedek-ve-geri-alma.md). yedek-denetim.py bu dosyayı okur, hiçbir şeyi silmez. Silme her zaman kullanıcı onayıyla elle yapılır; sonra kayıt durum: silindi olur.",
  "surum": 1,
  "kok": "~/Documents/Claude/yedek",
  "ikinci_kopya_iste": false,
  "yedekler": [
    {
      "kimlik": "ayar-2026-11-11",
      "yol": "~/Documents/Claude/yedek/ayar-2026-11-11",
      "tur": "ayar-dosyasi",
      "ne": "HYPERFRAMES_SKIP_SKILLS satırı eklenmeden önceki ~/.claude/settings.json, ~/.zshrc ve ~/.zshenv (notlar/hf-om-gecisi/DURUM.md, 2026-11-11)",
      "tarih": "2026-11-11",
      "geri_yukleme": "Her dosyayı yerine kopyala: claude-settings.json.yedek -> ~/.claude/settings.json, zshrc.yedek -> ~/.zshrc, zshenv.yedek -> ~/.zshenv. Önce mevcut dosyanın .onceki kopyasını al; settings.json'ın geçerli JSON olduğunu doğrula (içeriği ekrana basma). Her dosya ayrı onayla. Uyarı: yedekler düz metin anahtar satırı içerir; geri yüklemek onu da geri getirir. Ayrıntı: rehber/13, 'Ayar dosyası'.",
      "gizli_icerir": "evet",
      "beklenen": ["claude-settings.json.yedek", "zshrc.yedek", "zshenv.yedek"],
      "silme_gun": 30,
      "not": "Gizli içerikli olduğu için en çok 30 gün tutulur; süre dolunca aylık özet silinsin mi diye sorar."
    },
    {
      "kimlik": "global-skills-2026-11-08",
      "yol": "~/Documents/Claude/yedek/global-skills-2026-11-08",
      "tur": "genel-skill-klasoru",
      "ne": "Genel skill klasörlerinden yedeğe taşınan 27 eski skill (agents-skills), ~/.claude/skills bağ kopyaları (claude-skills-linkler) ve taşıma betikleri (notlar/hf-om-gecisi/DURUM.md, 2026-11-09)",
      "tarih": "2026-11-08",
      "geri_yukleme": "Yedekteki geri-al.sh bağları ve klasörleri ilk yerine koyar; çalıştırmadan önce dosyayı oku ve kullanıcıdan onay al (kütüphane dışında, sabit yollu). Elle yol: agents-skills/* -> ~/.agents/skills/, claude-skills-linkler/* (bağlar; hedeflerine ls -la ile bak) -> ~/.claude/skills/. Ayrıntı: rehber/13, 'Genel skill klasörü', ve rehber/12 (boşaltma).",
      "gizli_icerir": "hayir",
      "beklenen": ["agents-skills", "claude-skills-linkler", "LISTE.md", "geri-al.sh"],
      "silme_olay": "Genel skill klasörleri boşaltıldı (DURUM.md adım 3) ve kullanıcı yedeğin gereksiz olduğunu söyledi",
      "silme_olay_tamam": false,
      "not": "Kullanıcı 'sil' diyene kadar durur (DURUM.md:21). Hatırlatma boşaltma günü başlar (DURUM.md:27): olay tamam olunca bu yedek 'silinebilir' listesine girer."
    }
  ]
}
```
(`gizli_icerir: "hayir"` for global-skills rests on "skill folders and scripts only"; the implementer confirms by reading names only, not contents. The "beklenen" lists are taken from the real `ls` output: agents-skills, claude-skills-linkler, LISTE.md, geri-al.sh exist.)

Functions:
- `yol_ac(s) -> Path` (`Path(s).expanduser()`).
- `kayit_oku(yol) -> (veri|None, hata|None)` (JSON error is returned as a `sorun`, not raised).
- `boyut(yol) -> (bayt, kesildi)`: `os.scandir` walk, summing `st_size` of regular files, no opening, symlinks not followed, stop at BOYUT_TARAMA_SINIRI entries.
- `kayit_denetle(k, kok, bugun, kutuphane) -> list[bulgu]`.
- `kayitsizlar(kok, kayitlar) -> list[(ad, bayt)]`.
- `main(argv=None) -> int`.

Checks per record with durum != "silindi" (finding level in brackets; texts in section 4):
1. Schema: missing required field, unknown `tur`, bad `tarih`, `gizli_icerir` not evet/hayir, duplicate `kimlik` [sorun]. A record with schema errors skips the other checks.
2. Backup root missing (`kok` not a directory): ONE finding [dikkat] "yedek klasörü yok (yeni makine olabilir)" and the per-record existence checks are skipped.
3. `yol` missing [sorun]; any `beklenen` name missing inside `yol` [sorun] (names listed, content never read). `kayit` set but not present inside `yol` [sorun] "kayıt dosyası yok" (name only).
4. Wrong place [sorun]: resolved `yol` is inside `kutuphane` (KOK) (rehber/11:59: never inside the library) or inside any of TARAMA_KLASORLERI (rehber/05:45).
5. Secrets hygiene, only `gizli_icerir == "evet"`: any regular file (recursive, capped) with `st_mode & 0o077` != 0 [dikkat] "izinleri gevşek (chmod 600 önerilir)"; no `silme_gun` and no `silme_olay` [dikkat].
6. Ready to delete [dikkat + decision]: `(silme_gun is not None or silme_olay is not None)` and `(silme_gun is None or yas >= silme_gun)` and `(silme_olay is None or silme_olay_tamam is True)`. Text "SİLİNEBİLİR". In the full output also: "silme komutu (yalnız kullanıcı onaylarsa; kalıcıdır, geri alınamaz): rm -r -- '<mutlak yol>'" and the gentler option "ya da Çöp Sepeti'ne taşı: mv -- '<mutlak yol>' ~/.Trash/". The printed path is always the EXPANDED absolute path (never `~`, which does not expand inside quotes). The tool runs neither.
7. Pending event [bilgi]: `silme_olay` set and not done: "silme olayı bekleniyor: <olay>". Pending day count [bilgi]: "N gün sonra silinebilir".
8. Age [dikkat] when not ready to delete: `yas > (yas_uyari_gun or default)`: "N gündür duruyor; hâlâ gerekli mi?" (decision line).
Age = `(bugun - date(tarih)).days`.
Root level:
9. Unregistered [dikkat + decision]: every direct child of `kok` not starting with "." whose resolved path matches no record `yol` -> "kayıtsız yedek: <ad> (<boyut>)" decision "<ad> kayda alınsın mı?". Known name patterns are recognised and named in the text (still a finding, never ignored): `genel-klasorler-*` and `geri-yazilan-*` (P2: genel skill klasörü boşaltma/geri yazılan), `<ad>-YYYY-AA-GG[-N]` (program or ayar backup); text: "kayıtsız yedek: <ad> ({bilinen tür}; {boyut}) ". Pattern table `BILINEN_AD_KALIPLARI` in the tool; unknown names read "tanınmayan ad".
10. `ikinci_kopya_iste` true and no non-deleted `git-paketi` record, or the newest one older than GIT_PAKETI_GUN [dikkat]; when false: nothing (the decision is the user's, section 7 item 5).
Overall durum: any sorun -> "sorun"; else dikkat -> "dikkat"; else "temiz".

CLI: `--kayit PATH` (default yedekler.json), `--kok PATH` (override of the file's `kok`, for tests), `--kutuphane PATH` (default KOK, for the in-library check), `--bugun YYYY-MM-DD` (test hook), `--kisa`, `--ozet-json`, `--rapor`, `--cikti PATH` (default `KOK/notlar/yedek-durumu.md`), `--siki`. Same exit-code rules and same --ozet-json contract as git-durum.py (D4); the error object on an internal exception uses `"arac": "yedek-denetim"`. Missing yedekler.json file: one `sorun` finding "yedekler.json bulunamadı", exit 0.

JSON example (today's real state, 2026-11-11, after the initial records are added):
```json
{"arac": "yedek-denetim", "durum": "temiz",
 "satirlar": ["2 yedek kayıtlı, hepsi yerinde; silinecek yedek yok.",
              "global-skills-2026-11-08: silme olayı bekleniyor (genel skill klasörleri boşaltılıp onay gelince)",
              "ayar-2026-11-11: 30 gün sonra silinebilir (gizli içerikli)"],
 "karar_bekleyen": []}
```
Note: `bilgi` lines appear in this JSON only when durum is temiz and the pending lines are the useful reminder; with dikkat/sorun they are omitted (same rule as git-durum). Today's expected result is "temiz".

Human/Markdown output: a table with columns Yedek, Tür, Tarih, Yaş (gün), Gizli, Durum, Silme; below it findings and decisions; sizes in MB.

### 3.4 yedekler.json (new): as above (about 40 lines). Edited only by a library session, with the user's approval. Template for a new record is in rehber/13 section "Yeni yedek kaydı".

### 3.5 rehber/13-yedek-ve-geri-alma.md (new, about 220 lines)

Outline (Turkish headings; full text in section 4):
1. Tek kural (where, naming, permissions, records, never in library, never in scanned folders, never secrets in git).
2. Hangi yedek nerede (table: project automatic backup, library branch/git, program, settings file, machine-wide folder, git bundle).
3. Geri yükleme adımları per kind: Proje kurulumu; Kütüphane güncelleme dalı (before merge, after merge not pushed, after push, lost commits via reflog); Program güncellemesi; Ayar dosyası; Genel skill klasörü.
4. Saklama süresi ve hatırlatma kuralı (table; who reminds: aylik-ozet via yedek-denetim --ozet-json; deletion procedure).
5. Yeni bilgisayarda yalnız GitHub'dan geri kurma (commands; what comes back; what does not; checks).
6. Makine dışı durumun envanteri (names only).
7. GitHub oturumu bitince.
8. Yeni yedek kaydı şablonu and the "git bundle" optional second copy.

### 3.6 araclar/testler/test_p3-yedek-git.py (new): see section 5.

---------------------------------------------------------------------------------------------------

## 4 User-facing texts (exact strings)

### 4.1 git-durum.py findings (placeholders in {})
Header (full output): `Git durumu · {tarih} · dal {dal} · durum: {TEMİZ|DİKKAT|SORUN}`
- sorun: `Kütüphane git deposu değil: {yol}`
- sorun: `origin beklenen depo değil ({origin_depo}); bu araç yalnız {BEKLENEN_DEPO} ile çalışır, fetch yapılmadı`
- sorun: `master ile origin/master ayrışmış: {ahead} önde, {behind} geride. Önce sebebi bulunur (GitHub'daki Merge düğmesi kullanılmış olabilir, rehber/02); hiçbir şey kendiliğinden birleştirilmez`
- sorun: `GitHub deposu {gorunurluk} görünüyor; arsiv/ üçüncü taraf kopyalar içerir, depo private olmalı. Kullanıcıya hemen söyle`
- sorun: `Adı gizli bilgi gibi görünen izlenen dosya: {yollar}. İçeriğini açma; kullanıcıya söyle (rehber/13)`
- sorun: `Skill'in kendi .gitignore'u yüzünden git'e girmeyen arşiv dosyası var ({n}; ilk: {ilk}). Düzeltme: git add -f arsiv (klon eksik gelir)`
- dikkat: `Şu an {dal} dalındasın (beklenen: master)` / `HEAD bir dala bağlı değil`
- dikkat: `GitHub'a gönderilmemiş {ahead} commit var (en eskisi {gun} gün önce; son bilinen uzak commit {tarih}).` decision: `{ahead} commit GitHub'a gönderilsin mi? (push yalnız sen isteyince yapılır)`
- dikkat: `GitHub'da {behind} yeni commit var; yerelde yok (git pull gerekir, kullanıcıyla)`
- dikkat: `Kaydedilmemiş değişiklik: {n} dosya` ; bilgi variant: `Kaydedilmemiş tek değişiklik notlar/proje-kullanimi.md (aylık görev bunu kendisi kaydeder)`
- dikkat: `İzlenmeyen klasör/dosya: {liste}` decision: `{liste} commit edilsin mi?`
- dikkat: `Birleşmiş artık dal: {ad} (master'a zaten girmiş)` decision: `{ad} dalı silinsin mi? (git branch -d, birleşmiş)`
- dikkat: `Birleşmemiş yerel dal: {ad} ({onde} commit master'da yok, son commit {gun} gün önce)` decision: `{ad} dalı birleştirilsin mi, silinsin mi?`
- dikkat (any age): `Bekleyen güncelleme dalı: {ad} ({gun} gündür bekliyor); yenisi açılmaz` decision `{ad} dalı birleştirilsin mi, reddedilsin mi? (promptlar/08)`; the text gains `45 günden uzun` when > 45 days: `... 45 günden uzun bekliyor` decision `{ad} dalı birleştirilsin mi, reddedilsin mi? (promptlar/08)`
- bilgi: `GitHub'da bekleyen dal (son alıştan): {liste}`
- dikkat: `.git klasörü {mb} MB (eşik {ESIK_GIT_MB} MB). Büyüme sebebi araştırılır; kullanıcıya sor, kendiliğinden temizleme yapma`
- dikkat: `Yeni büyük dosya (>= {ESIK_YENI_DOSYA_MB} MB): {liste}` decision: `{liste} git'e girsin mi? (büyük medya arsiv'e girecekse önce sor)`
- dikkat: `.gitignore koruması eksik: {liste} (rehber/13)`
- bilgi: `GitHub ile eşit: 0 önde, 0 geride` / `origin/master bilinmiyor (uzak hiç alınmamış)`
- bilgi: `Saklanmış değişiklik (stash): {n}`
- bilgi: `En büyük 5 izlenen dosya: {ad} {mb} MB, ...`; `.git boyutu: {mb} MB`
- bilgi: `arsiv/ içinde adı gizli desenine uyan {n} izlenen üçüncü taraf dosya var (örnek/sabit dosyalar; taranmadı)`
- bilgi: `Uzak güncellendi (git fetch origin)` / `Uzak alınamadı (GitHub oturumu ya da ağ yok): ahead/behind son bilinen duruma göre. Oturum için bkz. rehber/13, 'GitHub oturumu bitince'`
- bilgi: `Depo görünürlüğü: private` / `depo görünürlüğü: denetlenemedi (gh oturumu yok ya da ağ yok)`
`--kisa` all-clear line: `git: temiz`.

### 4.2 yedek-denetim.py findings
Header: `Yedek durumu · {tarih} · {n} kayıt · durum: {TEMİZ|DİKKAT|SORUN}`
- sorun: `yedekler.json bulunamadı ya da bozuk: {ilk 100 karakter}`
- sorun: `{kimlik}: kayıtta eksik ya da hatalı alan: {alanlar}` / `kimlik tekrar ediyor: {kimlik}`
- sorun: `{kimlik}: yedek yok ({yol})`
- sorun: `{kimlik}: beklenen öğe eksik: {adlar}`
- sorun: `{kimlik}: yedek yanlış yerde ({kütüphane içinde | skill taranan klasör içinde}); gizli ya da yanlış yüklenebilir, taşınması için kullanıcıya sor`
- dikkat: `yedek klasörü yok ({kok}); yeni makine olabilir`
- dikkat: `{kimlik}: gizli içerikli ama izinleri gevşek (chmod 600 önerilir; kullanıcıya sor)`
- dikkat: `{kimlik}: gizli içerikli ama silme zamanı tanımsız (kayda silme_gun ekle)`
- dikkat: `{kimlik}: SİLİNEBİLİR ({neden}). Silme komutu (yalnız kullanıcı onaylarsa; kalıcıdır, geri alınamaz): rm -r -- '{mutlak_yol}' ; ya da Çöp Sepeti'ne taşı: mv -- '{mutlak_yol}' ~/.Trash/` decision `{kimlik} yedeği silinsin mi? Kalıcı silinir, geri alınamaz ({ne}); istersen Çöp Sepeti'ne taşırım`
- dikkat: `{kimlik}: {yas} gündür duruyor; hâlâ gerekli mi?` decision `{kimlik} yedeği hâlâ gerekli mi?`
- dikkat: `kayıtsız yedek: {ad} ({mb} MB)` decision `{ad} yedeği kayda alınsın mı?`
- dikkat: `Kütüphanenin GitHub dışında ikinci kopyası (git bundle) yok ya da {n} günden eski`
- bilgi: `{kimlik}: silme olayı bekleniyor: {olay}` / `{kimlik}: {n} gün sonra silinebilir`
- all clear: `{n} yedek kayıtlı, hepsi yerinde; silinecek yedek yok.`

### 4.3 rehber/13-yedek-ve-geri-alma.md body (final text for the implementer; Turkish, plain words)

```markdown
# Yedek ve geri alma

Bu rehber iki şeyi söyler: yedek nereye konur, nasıl geri alınır. Kütüphanenin kendi git geçmişi, projelerin otomatik yedeği ve
kütüphane dışına alınan yedekler (ayar dosyaları, programlar, genel skill klasörleri) ayrı yerlerdedir. Hepsinin özeti burada.
Kayıt: `yedekler.json`. Denetim: `python3 araclar/yedek-denetim.py` (salt okuma, hiçbir şeyi silmez).
Git durumu: `python3 araclar/git-durum.py` (salt okuma, push etmez).

## 1. Tek kural
1. Kütüphane dışına alınan her yedek `~/Documents/Claude/yedek/` altında durur. Kütüphane klasörüne, git'e, skill klasörlerine
   (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`) ve `~/.openmontage` içine konmaz (araçlar yedekteki SKILL.md'yi skill sanar).
2. Ad: `<ne>-<YYYY-AA-GG>` (ör. `ayar-2026-11-11`, `global-skills-2026-11-08`, `hyperframes-2026-12-03`). Aynı gün ikinci yedek: sonuna `-2`.
3. Gizli bilgi olabilecek yedek (ayar dosyaları, `.env`, anahtar içeren her şey): klasör `chmod 700`, dosyalar `chmod 600`; kayıtta
   `gizli_icerir: "evet"`, `silme_gun` en çok 30. Anahtar klasörleri (`~/.config/openmontage`) ve `~/.hyperframes/config.json` hiç yedeğe alınmaz.
4. Yedek alan oturum, aynı adımda `yedekler.json`'a kayıt ekler (şablon 8. bölümde). Kayıtsız yedek, aylık özette "kayıtsız yedek" diye çıkar.
5. Yedek almak ve silmek kullanıcı onayıyla yapılır. `yedek-denetim.py` silmez; "silinebilir" der, kullanıcı onaylarsa oturum siler ve kaydı `durum: "silindi"` yapar.

## 2. Hangi yedek nerede
| Ne | Yedek nerede | Kim alır | Kayıt |
|---|---|---|---|
| Projedeki skill kurulumu | projede `.skill-kutuphanesi/yedek/<zaman>/` (son 10) | `skill-ekle.py` kendiliğinden | yedekler.json'a yazılmaz (otomatik, 10'a kırpılır) |
| Kütüphane içeriği | git geçmişi + GitHub (`ulukayasaban/SkillKutuphanesi`, private) | `git commit`, push yalnız kullanıcı isteyince | yok (git zaten kayıt) |
| Kütüphanenin ikinci kopyası (isteğe bağlı) | `~/Documents/Claude/yedek/kutuphane-<tarih>.bundle` | kullanıcı isteyince oturum | tür `git-paketi` |
| Program güncellemesi | `~/Documents/Claude/yedek/<program>-<tarih>/` | oturum, güncellemeden önce | tür `program` |
| Ayar dosyası değişikliği | `~/Documents/Claude/yedek/ayar-<tarih>/` | oturum, değişiklikten önce | tür `ayar-dosyasi` |
| Genel skill klasörü boşaltma | `~/Documents/Claude/yedek/genel-klasorler-<tarih>/` (rehber/12; eski taşıma: `global-skills-2026-11-08/`; geri yazılanlar: `geri-yazilan-<tarih>/`) | oturum, boşaltmadan önce | tür `genel-skill-klasoru` |

## 3. Geri yükleme (her gerçek geri yükleme için kullanıcıdan o anda onay al)

### Proje kurulumu
`python3 araclar/skill-ekle.py <proje> --yedekler` (liste), `--geri-al` (son yedek) ya da `--geri-al <yedek-adı>`. Geri almayı geri almak da mümkün.
Kütüphaneye ya da yedek klasörüne dokunulmaz.

### Kütüphane güncelleme dalı (guncelleme/AAAA-AA)
- Birleştirmeden önce reddetmek: `git switch master && git branch -D guncelleme/AAAA-AA` (push edildiyse `git push origin --delete <dal>`, kullanıcı isteyince).
- `--birlestir` kontrolleri geçmezse master kendiliğinden eski haline döner (araç yapar); yapılacak şey yoktur.
- Birleştirme geçti, sonradan hata fark edildi, push EDİLMEDİ: `git log --oneline --graph | head` ile birleştirme commit'ini bul, sonra
  `git revert -m 1 <birleştirme-commit>`. (`-m 1` şart: birleştirme commit'inin iki ebeveyni var; 1 = master tarafı.) `git revert HEAD` birleştirme
  commit'inde `-m` olmadan hata verir.
- Birleştirme push EDİLDİ: aynı `git revert -m 1 <birleştirme-commit>`; yeni commit olur. Push yalnız kullanıcı isteyince. `reset --hard` ve
  `push --force` kullanılmaz.
- Commit kayboldu gibi: `git reflog` son hareketleri listeler; bulunan commit için `git branch kurtar <commit>`. Silinen dal da böyle döner.
- takip/AAAA-AA dalı: birleştirmek `git merge --no-ff <dal>` (otomatik geri alma yok: sonra `dogrula.py` ve `kapsam-denetimi.py` çalıştır;
  sorun çıkarsa `git revert -m 1 <birleştirme-commit>`); reddetmek `git branch -D <dal>`.

### Program güncellemesi (HyperFrames, OpenMontage, ...)
Önce programın kartındaki `geri_alma` alanı (rehber/11, P6) izlenir; kartta yoksa:
1. Programın çalışan işi durdurulur. 2. Yedek klasörü `<program>-<tarih>` açılır; içindekiler (yerel değişiklikler, veri klasörü, sabit sürüm listesi)
   neyin nereye döneceğini yedekteki not belirtir. 3. Kullanıcı onayıyla dosyalar yerine kopyalanır. 4. `python3 araclar/program-denetim.py` ile
   kurulu sürüm karttakiyle karşılaştırılır. Yedek, güncelleme doğrulanıp kullanıcı onaylayana kadar silinmez.

### Ayar dosyası
Yedek: `ayar-<tarih>/`. Önce bugünkü dosyanın `.onceki` kopyası alınır; sonra yedek yerine kopyalanır (`claude-settings.json.yedek` -> `~/.claude/settings.json`,
`zshrc.yedek` -> `~/.zshrc`, `zshenv.yedek` -> `~/.zshenv`). `settings.json` için doğrulama içeriği basmadan yapılır:
`python3 -c "import json,sys; json.load(open(sys.argv[1]))" ~/.claude/settings.json && echo geçerli`.
Uyarı: bu yedekler düz metin anahtar satırı içerebilir; geri yüklemek onu geri getirir. Yeni terminal açıp `env` değerini değil, yalnız satırın varlığını kontrol et.

### Genel skill klasörü
Yedek: `global-skills-<tarih>/` (`agents-skills/`, `claude-skills-linkler/`, `LISTE.md`, `geri-al.sh`). `geri-al.sh` kütüphane dışında ve sabit yollu;
çalıştırmadan önce oku, kullanıcıdan onay al. Bağlar elle de döner: önce `ls -la` ile hedeflerini yaz, sonra aynı bağı kur. `~/.agents/.skill-lock.json`
duruyorsa araç eski kayıtla skilli yeniden kurabilir: sıra ve kilit dosyası için rehber/12.

## 4. Saklama süresi ve hatırlatma
| Yedek türü | En çok ne kadar | Silme tetiği |
|---|---|---|
| Gizli içerikli (ayar dosyaları) | 30 gün | doğrulandıktan sonra `silme_gun` dolunca |
| Genel skill klasörü yedeği | kullanıcı "sil" diyene kadar | genel klasörler boşaltıldı ve kullanıcı onayladı (`silme_olay`) |
| Program yedeği | güncelleme doğrulanıp onaylanana kadar, en çok 90 gün | güncelleme onayı |
| Git paketi | 90 günden eskiyse yenisi alınır | kullanıcı isteyince |
Hatırlatma kuralı: kullanıcı yedekleri kendisi izlemez. `aylik-ozet.py` her ay `yedek-denetim.py --ozet-json` çalıştırır; "SİLİNEBİLİR", "gerekli mi?" ve "kayıtsız
yedek" satırları özetteki "karar bekleyenler"e düşer. Oturum açıldığında özet okunur ve bu satırlar kullanıcıya sorulur. Yeni zamanlanmış görev gerekmez.
Silme sırası: (1) kullanıcıya "şu yedek silinsin mi" sor, (2) onay gelirse `rm -r -- '<mutlak yol>'` (kalıcıdır; daha yumuşağı Çöp Sepeti'ne `mv`), (3) `yedekler.json`'da `durum: "silindi"` ve `silindi_tarih`, (4) commit.

## 5. Yeni bilgisayarda yalnız GitHub'dan kurma
Gerekenler: Python 3, git, `gh` (GitHub CLI). `gh auth login` komutunu kullanıcı kendisi çalıştırır (agent giriş yapmaz).
```bash
gh auth login                                                    # kullanıcı yapar
gh repo clone ulukayasaban/SkillKutuphanesi ~/Documents/SkillKutuphanesi
cd ~/Documents/SkillKutuphanesi
python3 araclar/dogrula.py && python3 araclar/kapsam-denetimi.py
python3 araclar/git-durum.py && python3 araclar/yedek-denetim.py && python3 araclar/program-denetim.py
```
Geri GELEN: git'in izlediği her şey: araçlar, rehberler, promptlar, roller, profiller, registry.json, `arsiv/` (3. taraf kopyalar; skillerin kendi
`.gitignore`'u yüzünden dışarıda kalmasın diye `git add -f arsiv` ile izleniyor, arsiv-guncelle.py yapar), kartlar (`programlar.json`, `projeler.json`),
`programlar/<ad>/` altındaki sabit sürüm kopyaları ve `KAYNAK.md` dosyaları, notlar.
Geri GELMEZ:
- GitHub'a gönderilmemiş commit'ler (`git-durum.py` "önde" sayısını söyler: yeni makineye geçmeden önce push iste).
- Commit edilmemiş değişiklikler ve izlenmeyen klasörler (ör. henüz commit edilmemiş `programlar/<ad>/`).
- Yalnız yerelde kalmış dallar, stash, reflog, `.git/config` içindeki ad ve e-posta.
- `.gitignore`'un dışarıda bıraktıkları: `.gecici/`, `.arsiv-yeni/`, `.arsiv-eski/`, `.guncelleme-kilidi`, `__pycache__/`, `.DS_Store`, ve yeni korumalar (`/.env*`, `/*.pem`, `/*.key`, `/yedek/`, `/.skill-kutuphanesi/`, `/*.bundle`, `/*.yedek`, `/notlar/son-aylik-calisma.json`, `/notlar/aylik-ozet.md`).
- `~/Documents/Claude/yedek/` içindekiler (kütüphane dışı) ve 6. bölümdeki bütün makine durumu.
- Programların kendisi (venv, npm paketi, `~/.openmontage` kurulumu): kartlardaki `kurulum` bölümüne (rehber/11) göre yeniden kurulur.
Klon doğrulaması: `dogrula.py` "git'e girmeyen arşiv dosyası" HATA'sı vermemeli; `git-durum.py` "arşiv dosyası git'e girmemiş" demezse klon eksiksizdir.
Kütüphane farklı bir yola klonlanırsa projelerin `kilit.json` yolları için `promptlar/09-proje-tasindi-veya-bozuldu.md`.

## 6. Makine durumu envanteri (kütüphane dışı; yalnız adlar, değer yazılmaz)
Geri yüklemede yeniden kurulacaklar. Her biri için gizli değer kopyalanmaz; yalnız "satır var mı" denetlenir.
| Ne | Yer | Not |
|---|---|---|
| Kabuk ortamı | `~/.zshrc`, `~/.zshenv` | `HYPERFRAMES_SKIP_SKILLS` satırı (DURUM.md); anahtar satırları düz metin |
| Claude ayarları | `~/.claude/settings.json` (env, izin kuralları, hook'lar), `~/.claude/CLAUDE.md` (genel talimat) | ses kaydı ve OpenMontage izinleri burada |
| Claude hafızası | `~/.claude/projects/*/memory/` | kalıcı kararlar `notlar/kararlar.md`'ye (P8) taşınır |
| Aylık zamanlanmış görev | `~/.claude/scheduled-tasks/skill-kutuphanesi-aylik-guncelleme/SKILL.md` | kütüphane dışı, yedeksiz; P4 kopyasını kütüphaneye alır, yoksa tek kopya budur |
| Diğer zamanlanmış görevler | `~/.claude/scheduled-tasks/` (colab, kopru görevleri) | kütüphaneyle ilgisiz, yine de makine durumu |
| Genel skill klasörleri | `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.agents/.skill-lock.json` | boşaltma sonrası içerik: rehber/12 |
| Programlar | `~/.openmontage` (venv ve sürüm sabitleri), `~/Movies/OpenMontage`, `~/.hyperframes`, npm genel `hyperframes` paketi | kartlardaki `kurulum` |
| Anahtar dosyaları | `~/.config/openmontage/.env` | yedeğe ALINMAZ; kullanıcı yeniden girer |
| Ses kaydı | `~/Documents/Claude/Kayitlar/` (betikler ve kayıtlar) | Terminal.app mikrofon izni (macOS) dosyayla geri gelmez, kullanıcı yeniden verir |
| Başlangıç ajanları | `~/Library/LaunchAgents/` (varsa) | adlar yedekte tutulur |
| GitHub oturumu | `gh auth` (`~/.config/gh/`) | kullanıcı `gh auth login` yapar |
| Projelerin kilitleri | her projede `.skill-kutuphanesi/kilit.json`, `.agents/skills`, `.claude/skills`, `CLAUDE.md`/`AGENTS.md` blokları | proje kendi git'inde; `proje_yolu` başka makinede geçersiz olur |
| Diğer araçların ayarları | Codex, Antigravity, Cursor, VS Code Copilot kendi ayar klasörleri | tam liste `yapay-zeka-araclari.json` (P1) |
Mac Time Machine'den geri yüklenirse: `~/Documents/Claude/yedek/` de geri gelir ve `zshrc.yedek` içindeki düz metin anahtar satırı da dönmüş olur;
`yedek-denetim.py` bunu "gizli içerikli" diye gösterir ve 30 günü dolunca silinmesini ister.

## 7. GitHub oturumu bitince
Belirti: `gh auth status` hata verir, `git push` 401/403 ya da "Authentication failed" yazar, `git-durum.py --uzak` "Uzak alınamadı" der.
1. Kullanıcı kendisi çalıştırır: `gh auth login` (GitHub.com, HTTPS, tarayıcıyla). Sonra `gh auth status`. Agent şifre ve token girmez.
2. Bu sırada çalışmaya devam eden yerel araçlar ("yalnız yerel mod"): `git-durum.py` (`--uzak` olmadan), `yedek-denetim.py`, `dogrula.py` (`--github` olmadan),
   `kapsam-denetimi.py`, `test.py`, `skill-ekle.py`. Durmuş olanlar: push, PR, `github-trend.py`, `kaynak-cek.py`, `arsiv-guncelle.py`, `github-skill-listesi.py`.
3. Giriş geri gelene kadar kütüphanenin tek kopyası bu Mac'tir. Kullanıcı isterse ikinci kopya: `git bundle create ~/Documents/Claude/yedek/kutuphane-<tarih>.bundle --all`
   (kütüphaneyi değiştirmez; kayıt: tür `git-paketi`; geri: `git clone <dosya>.bundle <klasör>`).
4. Token sızdığından şüphelenilirse kullanıcı GitHub'da tokenı iptal eder ve `gh auth login` ile yenisini alır.

## 8. Yeni yedek kaydı şablonu
`yedekler.json` → `yedekler` listesine:
{ "kimlik": "<ne>-<YYYY-AA-GG>", "yol": "~/Documents/Claude/yedek/<kimlik>", "tur": "<tür>", "ne": "<ne yedeklendi ve neden>", "tarih": "<YYYY-AA-GG>",
  "geri_yukleme": "<adımlar; rehber/13 bölümü>", "gizli_icerir": "evet|hayir", "beklenen": ["<ad>"], "silme_gun": 30, "kayit": "KAYIT.json (yalnız program yedeğinde)" }
Bu kayıt ZORUNLU adımdır: yedek alan her rehber (11, 12) kendi yedek adımından hemen sonra bu satırı ekletir. yedekler.json tek envanterdir; `KAYIT.json` yalnız programın geri alma verisidir (sürüm, commit), `kayit` alanı ona işaret eder.
Sonra: `python3 araclar/yedek-denetim.py` (sorun olmamalı), commit.
```

(Section 3.5's final file = the block above; the implementer keeps all commands exactly.)

---------------------------------------------------------------------------------------------------

## 5 Tests (araclar/testler/test_p3-yedek-git.py)

Harness: no dependencies; function `test(ad, kosul)` collects results; last line `N/N test geçti`; exit 0 when all pass, else 1 (prints failing names). Module loading: `importlib.util.spec_from_file_location` for the hyphenated file names `git-durum.py` and `yedek-denetim.py`; CLI cases also run the tools with `subprocess` (`sys.executable`). All git repos live in `tempfile.mkdtemp()`; every git call sets env `GIT_CONFIG_GLOBAL=/dev/null`, `GIT_CONFIG_NOSYSTEM=1`, `GIT_AUTHOR_*`/`GIT_COMMITTER_*` names and dates (old dates via `GIT_COMMITTER_DATE`), `git init -b master`. `HOME` is set to a temp folder for every subprocess so `~` never touches the real home. Fake `gh`: a small shell script in a temp bin folder put first on PATH (prints `PRIVATE`, `PUBLIC`, or exits 1). The test never imports `ortak.KOK`-relative real state except the tool modules themselves.

git-durum cases
1. clean repo with a bare origin, in sync -> durum "temiz", `--ozet-json` satirlar == ["Git temiz: master GitHub ile aynı, değişiklik yok."].
2. 6 local commits ahead -> ahead 6, "dikkat", decision line mentions push; ESIK 5 boundary: 4 ahead is temiz, 5 ahead dikkat.
3. 1 commit ahead but committed 10 days ago (GIT_COMMITTER_DATE) -> dikkat by age (en_eski_gun >= 10).
4. behind 1 / ahead 0 (commit added to origin through a second clone, tool run without --uzak): behind stays 0 (no implicit fetch); the same run with `--uzak` -> behind 1 and "dikkat". Check by comparing `refs/remotes/origin/master` before the plain run (unchanged).
5. diverged (ahead 1 and behind 1 after --uzak) -> "sorun"; `--siki` exits 1; without `--siki` exits 0.
6. dirty tracked file + untracked folder -> counts, untracked folder name ends with "/" in the finding; sole change `notlar/proje-kullanimi.md` -> bilgi, durum temiz.
7. renamed file in status (`git mv`) parsed with -z without crashing; old path is not listed as untracked.
8. merged leftover branch -> finding with `git branch -d` decision text; non-merged branch -> "Birleşmemiş yerel dal"; neither is deleted (branch list identical after the run).
9. pending `guncelleme/2026-11` branch: 10 days old -> dikkat with the decision line (any age); 50 days old -> same plus the text "45 günden uzun".
10. `.git` threshold: run with a patched constant `ESIK_GIT_MB = 0` through the imported module (`mod.ESIK_GIT_MB = 0`) -> dikkat; default -> no finding.
11. new tracked file >= 5 MB added after origin (`diff-filter=A`) -> "Yeni büyük dosya"; a modified big file already on origin does not warn; an untracked 6 MB file warns (patched ESIK_YENI_DOSYA_MB to 1 to keep the test small).
12. secret-like tracked names: `.env`, `a/b.pem`, `credentials.json` outside arsiv/ -> "sorun" and names listed, never any content (the file content is a sentinel string `GIZLI-DEGER`; assert it is absent from stdout and stderr); `.env.example` is not flagged; the same names under `arsiv/x/` -> not listed, only the count line.
13. arsiv ignored file: temp repo with `arsiv/s/.gitignore` containing `x.txt` and an untracked `arsiv/s/x.txt` -> "sorun" with the `git add -f arsiv` hint; after `git add -f` -> gone.
14. gitignore protections: repo without the new patterns -> `koruma_eksik` lists them; a repo whose .gitignore holds the exact block from section 3.1 (including the two P4 lines) -> none listed (the test holds the block text in a constant `GITIGNORE_BLOK`; temp repos only, the real library files are NOT read by this test file, per D5).
15. `--uzak` with origin `https://github.com/someone/else.git` -> "sorun", no fetch attempted (assert `FETCH_HEAD` absent); with local-path origin -> fetch works.
16. visibility: fake gh prints PUBLIC with origin `https://github.com/ulukayasaban/SkillKutuphanesi.git` -> "sorun"; PRIVATE -> bilgi; gh missing (empty PATH) -> no finding and exit 0; `--gh-yok` -> gh never called (fake gh writes a marker file; marker absent).
17. detached HEAD -> dikkat "HEAD bir dala bağlı değil"; no crash.
18. not a git repo (`--depo` plain temp folder) -> durum "sorun", exit 0; with `--siki` exit 1; `--ozet-json` still valid JSON.
19. `--ozet-json` purity: `json.loads(stdout)` succeeds, keys exactly {"arac","durum","satirlar","karar_bekleyen"}, `arac == "git-durum"`, stderr empty, no file created in the repo or in `notlar/`; `--ozet-json --rapor` and `--ozet-json --kisa` exit 2.
20. read-only guarantee: snapshot of the work tree files (names + sizes + mtimes) and of `git for-each-ref` and `git status --porcelain` before and after every previous run = identical; `.git/index` mtime unchanged (verifies `--no-optional-locks`).
21. `--kisa` prints `git: temiz` on a clean repo and only dikkat/sorun lines otherwise.
22. `--rapor --cikti <temp>/r.md` writes the file; running again does not rewrite when only the date differs (mtime unchanged after setting an old mtime and patching the date line).
23. stash count line appears after `git stash` (bilgi level, durum unaffected).

yedek-denetim cases (records and folders in a temp root; `--bugun` fixed to 2026-11-11)
24. both initial-style records, folders and `beklenen` names present -> durum "temiz", ozet-json valid, exit 0.
25. missing folder -> "sorun" with `yol yok`; missing `beklenen` name -> "sorun" listing the name only.
26. backup root missing -> one "yedek klasörü yok" dikkat finding, no per-record sorun.
27. record inside the temp "library" (`--kutuphane`) -> "sorun" (yanlış yerde); record under a fake `~/.claude/skills` (HOME temp) -> "sorun".
28. gizli_icerir "evet" with a 644 file -> dikkat "izinleri gevşek"; chmod 600 -> gone; the sentinel content `GIZLI-DEGER` never appears in output; the tool does not change file modes (stat before/after).
29. gizli evet without `silme_gun`/`silme_olay` -> dikkat.
30. ready to delete by days: `silme_gun` 30, tarih 31 days before `--bugun` -> "SİLİNEBİLİR" + decision + the `rm -r --` command text; the folder still exists afterwards (never deleted); age 29 days -> "N gün sonra silinebilir" bilgi.
31. ready to delete by event: `silme_olay` set, `silme_olay_tamam` false -> bilgi "silme olayı bekleniyor", not in the ready list; flip to true in the file -> "SİLİNEBİLİR".
32. `silme_gun` and `silme_olay` both set: only ready when both hold (age ok but event false -> not ready; both true -> ready).
33. age warning: no silme fields, tarih 100 days old (gizli hayir, default 90) -> "gündür duruyor"; gizli evet default threshold 30.
34. unregistered folder in root (`.hidden` child ignored) -> dikkat + decision; size printed in MB, computed without opening files (test makes a file unreadable with mode 000: the tool must not fail).
35. schema errors: missing `geri_yukleme`, bad `tur`, bad date, duplicate kimlik, `gizli_icerir` "belki" -> each "sorun"; broken JSON file -> "sorun", exit 0; missing yedekler.json -> "sorun".
36. `durum: "silindi"` record with missing folder -> no finding.
37. `ikinci_kopya_iste` true, no bundle record -> dikkat; with a `git-paketi` record 10 days old -> none; 100 days old -> dikkat; `ikinci_kopya_iste` false -> never.
38. `--ozet-json` purity and exit codes for yedek-denetim (same assertions as case 19; `--siki` exit 1 only on sorun).
40. name patterns: unregistered `genel-klasorler-2026-12-01` and `geri-yazilan-2026-12-02` folders -> each a dikkat finding naming the recognised type; once a record with that `kimlik` exists the finding disappears; an unknown name reads "tanınmayan ad".
41. `kayit` field: record with `kayit: "KAYIT.json"` and the file present -> no finding; file absent -> sorun "kayıt dosyası yok" (name only; the file is never opened: test makes it mode 000).
42. GITIGNORE_BLOK constant includes `/notlar/son-aylik-calisma.json` and `/notlar/aylik-ozet.md`; test 14 with a repo lacking only those two lines -> `koruma_eksik` lists exactly those two.
39. (reserved, no case. The real-file checks, namely the yedekler.json schema, the .gitignore block and the rehber/13 command strings, live in the P8 dogrula hand-off and in section 10 acceptance, not here, so a rejected .gitignore change can never fail this file.)

All tests use temp directories and fake data only; no real library or home file is read or written.

---------------------------------------------------------------------------------------------------

## 6 Hand-off requests to other packages

To P8 (integrator; shared files)
1. araclar/test.py: add a section that runs every `araclar/testler/test_*.py` as a subprocess (already planned by D5); no P3-specific text.
2. araclar/dogrula.py: add checks. (a) HATA: `yedekler.json` exists, is valid JSON, `surum == 1`, every record has `kimlik, yol, tur, tur in TURLER, ne, tarih, geri_yukleme, gizli_icerir in ("evet","hayir")`, kimlik values unique. (The tool's own tests cover the same; dogrula makes it part of the standard health run.) (b) UYARI: `.gitignore` lacks any line of the section 3.1 block (including `/notlar/son-aylik-calisma.json` and `/notlar/aylik-ozet.md`) (skip when the user rejected that change); (c) UYARI: `rehber/13-yedek-ve-geri-alma.md` missing or lacks the strings `git revert -m 1`, `gh auth login`, `git bundle create`, `yedekler.json`, `rehber/12`. These real-file checks replace former test cases 39-41 (D5).
3. araclar/duman-testi.py: add a read-only step: `python3 araclar/git-durum.py --ozet-json` and `python3 araclar/yedek-denetim.py --ozet-json` each must print valid JSON and exit 0 (no pass/fail on dikkat; duman already demands a clean tree separately at :61).
4. CLAUDE.md and AGENTS.md (identical text in both, `diff -q` check by P8):
   - First-step line: "Oturum başında `python3 araclar/git-durum.py --kisa` çalıştır; sorun ya da dikkat satırı varsa kullanıcıya söyle (push yalnız o isteyince)."
   - Maintenance bullet: "Git ve yedek: `araclar/git-durum.py`, `araclar/yedek-denetim.py` (salt okuma); yedek ve geri alma kuralı `rehber/13-yedek-ve-geri-alma.md`. Her yedek `yedekler.json`'a kaydedilir."
   - Rule 1 exception text (P2/P8) must keep "yedek `~/Documents/Claude/yedek/` altına" consistent with rehber/13.
5. README.md (after P3 finishes, because of the `.gitignore` list and restore text): (a) the "Gönderilmeyenler" line (README.md:52) gets the new patterns: `/.env*`, `/*.pem`, `/*.key`, `/*.p12`, `/*.pfx`, `/programlar/**/.env`, `/yedek/`, `/.skill-kutuphanesi/`, `/*.bundle`, `/*.yedek`, `/notlar/son-aylik-calisma.json`, `/notlar/aylik-ozet.md` (açıklama: P4 yerel damga ve özet); (b) the "Başka bilgisayarda kurmak" block (README.md:53-57) gets one sentence: "Tam geri kurma listesi, geri gelmeyenler ve makine durumu: rehber/13-yedek-ve-geri-alma.md"; plus the warning "GitHub'a gönderilmemiş commit'ler klonda yoktur; önce `git-durum.py`"; (c) add rehber/13 to the "Rehberler" list.
6. BASLA.md (P8): list of "hangi isteğe hangi komut": "git durumu / push gecikmesi -> git-durum.py"; "yedek / geri alma / yedek silme -> yedek-denetim.py, rehber/13".
7. notlar/kararlar.md (P8): record decisions: thresholds (5 commit, 7 gün, 300 MB, 5 MB, 45 gün), "gizli içerikli yedek en çok 30 gün", "yedek silme her zaman onayla ve araç silmez".

To P4 (monthly summary and scheduled task)
1. aylik-ozet.py runs `git-durum.py --ozet-json` and `yedek-denetim.py --ozet-json` as subprocesses (D4), merges `karar_bekleyen` into the single list; do not pass --uzak by default (offline-safe). Optional: P4 may run `git-durum.py --uzak` as an explicit extra step when `gh auth status` is fine.
2. Proposed text for the scheduled task's step 1 (needs approval, section 7): replace "git branch --show-current && git status --short | wc -l" stop rule by "python3 araclar/git-durum.py --kisa; kirli ağaçta durmak yerine raporu yaz ve salt okuma adımlarını yine çalıştır" (P4 already plans this; P3 only supplies the tool).
3. rehber/02, section "Geri alma" (line 95-98): replace `git revert HEAD` by a pointer "Birleştirme commit'i için `git revert -m 1 <commit>`; push sonrası ve reflog: rehber/13, 'Kütüphane güncelleme dalı'". rehber/02 also gets a short "Git sağlığı" line: "`git-durum.py` ahead/behind, artık dal, boyut; eşikler: 5 commit ya da 7 gün".
4. promptlar/08: takip/* merge and reject steps are written in rehber/13 ("takip/AAAA-AA dalı"); P4 may copy them.

To P1 (skill-ekle.py)
1. In `yedekle()` (araclar/skill-ekle.py:239): on the first backup in a project also write `.skill-kutuphanesi/.gitignore` containing exactly `yedek/` (only if the file does not exist; never overwrite) so project backups do not enter the project's git. Close of the skill-ekle.py part of B6. rehber/13 section 2 already says "Projedeki skill kurulumu ... otomatik".

To P2 (genel-bekci and rehber/12)
0. P2's five requests, answered: (i) folder name: ACCEPTED, `genel-klasorler-<tarih>` (and `geri-yazilan-<tarih>`) everywhere in P3; (ii) yedek-denetim recognises both name patterns in `kayitsizlar()` (accepted, check 9, test 40); (iii) rehber/13 links to rehber/12 for folder-level rollback and states that the backup parent for emptying is `~/Documents/Claude/yedek/` (accepted, section 3 'Genel skill klasörü'); (iv) `ayar-2026-11-11` marked as key-bearing: ACCEPTED, the record already has `gizli_icerir: "evet"` and 30-day deletion; (v) the one-time reminder: not P3's (scheduled task), yedek-denetim gives the same reminder through `silme_olay`. CHANGED: P2's record `tür: genel-klasor` must be written as `tur: "genel-skill-klasoru"` (the TURLER value; P2 text to be adjusted), field names are `kimlik/yol/tur/ne/tarih/...` (not `neden`).
1. rehber/12's "backup before emptying" step must create `~/Documents/Claude/yedek/genel-klasorler-<YYYY-AA-GG>/` (list of links via `ls -la`, `.skill-lock.json` copy, folders) and add a yedekler.json record of tur `genel-skill-klasoru` using the template in rehber/13 section 8; `silme_olay` text: "Boşaltma doğrulandı ve kullanıcı yedeğin gereksiz olduğunu söyledi". The reminder on emptying day (DURUM.md:27) is then automatic through yedek-denetim.
2. genel-bekci.py's "tracked secrets" scanning (HYPERFRAMES_SKIP_SKILLS line count) stays separate; no overlap with git-durum.

To P6 (programs)
0. P6's 'program-yedegi' request: mapped to TURLER value `program` (no new value). `KAYIT.json` stays P6's own restore data; the yedekler.json row points to it with `kayit: "KAYIT.json"` (yedekler.json is the single inventory, no second record format to keep in sync). The trial folder `~/Documents/Claude/deneme/<program>-<hedef>/`: its record may use a `yol` outside `kok`; it is not covered by the unregistered-folder check (outside `kok`), the record is the only reminder. P6's rehber/11 backup step must say: 'yedekler.json'a satır ekle' is a mandatory step after taking the backup.
1. rehber/11 and `program-denetim.py --oncesi <ad>`: the program backup folder is `~/Documents/Claude/yedek/<ad>-<tarih>/` (already rehber/11:59); after taking it, add a yedekler.json record of tur `program` (template in rehber/13). `--oncesi` may check existence by looking up a record whose `kimlik` starts with `<ad>-` and `durum != "silindi"` (read yedekler.json with json_oku; do not import yedek-denetim). Program card field `geri_alma` (A4) is the first thing rehber/13 "Program güncellemesi" points to.

To P5 (project tracking): none (project backups are not tracked here, section 8).

---------------------------------------------------------------------------------------------------

## 7 Needs the user's approval

Design/implementation (library files, one approval round before the commit):
1. `.gitignore` additions (section 3.1): on the audit's approval list.
2. New files themselves (tools, yedekler.json, rehber/13) and their commit: normal library work, per-commit approval like any other change (CLAUDE.md:54 then commit). Push: only when the user asks (D12).

At the time of the real action (the design only delivers procedure, pre-check tool and text):
2a. The new policy numbers: push-lag thresholds (5 commits or 7 days), `.git` 300 MB, new file 5 MB, pending branch 45 days, secret-containing backup kept at most 30 days, other backups asked about after 90 days, program backup at most 90 days. They decide when he gets asked; he confirms or changes them before they are written into rehber/13 and the tools.
3. Creating, restoring or deleting any backup folder under ~/Documents/Claude/yedek, and changing `silme_olay_tamam`.
4. Restoring settings files (`~/.claude/settings.json`, `~/.zshrc`, `~/.zshenv`) or machine-wide skill folders from backup: every file separately.
5. Optional second copy: `git bundle create ...` into ~/Documents/Claude/yedek (user question 6 in ozet-bolum2-4). Until he says yes, `ikinci_kopya_iste` stays false and the tool stays silent about it.
6. Deleting the merged local branch `skill/lottiefiles-motion-design` (`git branch -d`): decision line, only on his yes.
7. Committing programlar/hyperframes/ and programlar/openmontage/ (untracked KAYNAK.md cards): decision line, only on his yes.
8. `git push` of the 9 unpushed commits and any later push (rule 5): only on his request.
9. `gh auth login` after expiry: the user types it himself.
10. Changing the scheduled task text (~/.claude/scheduled-tasks/...): not done by P3 (P4's proposal).
11. Adding yedekler.json records for future backups: part of each backup's approval.

---------------------------------------------------------------------------------------------------

## 8 Deferred and why

- Project backups (`.skill-kutuphanesi/yedek` inside each project) are not inventoried by yedek-denetim.py: they are automatic, rotated to 10 (skill-ekle.py:260-262), live in projects the library does not own, and listing them needs the project registry P5 owns (`proje-kullanimi.py`, `projeler.json`). They are covered by rehber/13 section 3 and by P5's `--saglik`. Revisit after P5 ships: a `--projeler` flag can then read the project list.
- `.skill-kutuphanesi/.gitignore` writing in `yedekle()`: skill-ekle.py belongs to P1 (hand-off).
- One-command bootstrap script for a fresh clone (critic scenario 12 "tek komutlu bootstrap"): not written. The five-command block in rehber/13 section 5 is enough and a script that calls `gh auth` or clones would add a second path to maintain (D2). BASLA.md (P8) may link to it.
- A pre-commit hook that enforces "commit after every change" and secret scanning at commit time: hooks live in `.git/hooks` (not tracked, not restored on a clone) and would change how every session commits; the audit only needs detection, which git-durum.py gives at session start and monthly. Deferred, no owner needed.
- git LFS / large-file policy: only a threshold and a decision line now (new files >= 5 MB). A real policy needs the user's opinion on arsiv/ media; not forced.
- `git gc` / repack advice: the tool reports `.git` size and warns above 300 MB; the cleanup itself stays a manual, approved action (D7 spirit).
- Windows behaviour of the tools (Etsy-Arif): paths and `chmod` check (`st_mode & 0o077`) are POSIX; on Windows the permission check is skipped (tool wraps it in try/except and reports nothing). Not tested on Windows because the library session runs on this Mac.
- Remote-branch cleanup (`git push origin --delete ...`): not performed or suggested as a command by the tool beyond the existing rehber/02 text (D12).
- yedek integrity (hash or restore test): only existence, names, permissions, age. A restore rehearsal is manual and approval-bound.
- Gemini/Copilot CLI instruction files: unrelated to P3.

---------------------------------------------------------------------------------------------------

## 9 Risks and how the implementer verifies nothing existing broke

Risks
1. `.gitignore` hides something that should be tracked: patterns are root-anchored and exact. Check: before/after `git status --short` identical; `git ls-files -ci --exclude-standard | wc -l` stays 1; `git status --ignored --porcelain arsiv | grep -c '^!! '` unchanged (dogrula.py:226-230 depends on it); `git check-ignore -v programlar/etsyotomasyon/kaynak/.env.example` must print nothing.
2. A tool writes into the library by accident: no default writes; only `--rapor`. Tests 20 and 19 compare tree snapshots. `--no-optional-locks` prevents index refresh writes.
3. Slow or hanging git/gh: every subprocess has a timeout (60/120/20 s) and timeouts degrade to "bilgi" lines, never an exception.
4. False positives of the secret-name scan: scan skips arsiv/ and example suffixes; the library has no hit today (measured). If a legitimate file is ever flagged the finding is `sorun` only with `--siki` exit 1; default exit stays 0, the monthly chain is not blocked.
5. Counting convention: `rev-list --left-right --count origin/master...master` prints `behind<TAB>ahead` (left = origin). Test 2 and 4 pin the order.
6. `--uzak` fetch could touch a wrong repo: refused unless origin is non-GitHub or equals ulukayasaban/SkillKutuphanesi (test 15).
7. gh output format changes: only the single word from `--jq .visibility` is read; anything else -> None (silent skip).
8. Backup `gizli_icerir: "hayir"` for global-skills rests on assumption: implementer lists names only (`ls`) to confirm, and sets "evet" if any name looks like `.env`/key material.
9. New-file naming: the test file name has a hyphen, so it is loaded by path, not `import`.
10. Shared files untouched: P3 edits only `.gitignore` among existing files. Check with `git diff --stat` after implementation: only `.gitignore` changes among tracked files (others from other packages are not P3's).

Verification of existing behaviour: run (implementation stage only) `python3 araclar/dogrula.py` (0 hata), `python3 araclar/kapsam-denetimi.py` (0 sorun), `python3 araclar/test.py` (all pass), and the new test file. None of the existing tools is modified, so failures would point to the .gitignore edit.

---------------------------------------------------------------------------------------------------

## 10 Acceptance (commands that prove it is done)

```bash
cd ~/Documents/SkillKutuphanesi
python3 araclar/testler/test_p3-yedek-git.py                    # last line "N/N test geçti", exit 0
python3 araclar/git-durum.py --help && python3 araclar/yedek-denetim.py --help
python3 araclar/git-durum.py                                    # human report; today: DİKKAT (9 önde, 9 dosya kirli, 2 izlenmeyen klasör, artık dal) or the then-current truth
python3 araclar/git-durum.py --kisa
python3 araclar/git-durum.py --ozet-json | python3 -c "import json,sys; d=json.load(sys.stdin); assert set(d)=={'arac','durum','satirlar','karar_bekleyen'} and d['arac']=='git-durum'"
python3 araclar/git-durum.py --siki; echo "cikis=$?"            # 0 unless durum is sorun
python3 araclar/yedek-denetim.py                                # 2 kayıt, ikisi yerinde, durum temiz
python3 araclar/yedek-denetim.py --ozet-json | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['arac']=='yedek-denetim' and d['durum'] in ('temiz','dikkat','sorun')"
python3 araclar/yedek-denetim.py --siki; echo "cikis=$?"
ls ~/Documents/Claude/yedek                                     # unchanged: ayar-2026-11-11, global-skills-2026-11-08 (tool never deletes)
git status --short                                              # only the new files and .gitignore beyond what existed
git ls-files -ci --exclude-standard | wc -l                     # still 1
git check-ignore -q .env && git check-ignore -q yedek/x && git check-ignore -q notlar/son-aylik-calisma.json && git check-ignore -q notlar/aylik-ozet.md && ! git check-ignore -q programlar/etsyotomasyon/kaynak/.env.example && echo koruma-tamam
grep -c "git revert -m 1" rehber/13-yedek-ve-geri-alma.md       # >= 2
python3 araclar/dogrula.py && python3 araclar/kapsam-denetimi.py
python3 araclar/test.py                                         # existing tests keep passing
```
Done means: both tools run read-only on the real library with the outputs above; yedekler.json holds the two real records; rehber/13 contains the sections of 3.5 and the commands of 4.3; `.gitignore` has the new block and nothing else changed; the test file passes alone; no file outside the owned list was edited by P3.

---------------------------------------------------------------------------------------------------

## 11 Review changes

Applied (mandatory)
1. P4 blocking request: `/notlar/son-aylik-calisma.json` and `/notlar/aylik-ozet.md` appended to the section 3.1 block (with explanation), to the "why" list, to `KORUMA_PROBLARI` (probe), to the test GITIGNORE_BLOK (test 14 and new test 42), to rehber/13 section 5 list, to the verification and acceptance `check-ignore` commands, and to the README and dogrula hand-offs (P8).
2. Order dependency written at the top ("Önkoşul"): programlar/ commit, then P3, P1, P2+P5+P6, P7, P4, P8, Yama B, then folder emptying. P3 must precede P4 because of the .gitignore lines.
Applied (optional)
3. Backup folder name unified to `genel-klasorler-<YYYY-AA-GG>` (+ `geri-yazilan-<tarih>`) in the table, the P2 hand-off and `kayitsizlar()`; patterns recognised and named (new test 40). P2's five requests answered one by one in section 6 (accepted four; changed: tur value `genel-skill-klasoru`, not `genel-klasor`).
4. P6 'program-yedegi' mapped to `program` and the trial-folder note in section 6.
5. One inventory only: yedekler.json; new optional `kayit` field points to P6's `KAYIT.json`; a name-only existence check was added (test 41); backup template says the yedekler.json row is a MANDATORY step of rehber/11 and rehber/12.
Re-checked against the code: the ignore patterns remain root-anchored; `notlar/` is a tracked folder but the two new files are untracked today (`git ls-files notlar/son-aylik-calisma.json` is empty), so ignoring them hides nothing tracked.
Unowned gaps: none taken. B2 (triage), kayip_tarihi, 44-test line, rehber/08, kabul-edildi list and library-path-in-project-block do not touch P3 files. The repeated `karar_bekleyen` lines of git-durum and yedek-denetim are kept short and stable (same wording each run) so P4's future 'kabul edildi' filter can match them by exact text.
Rejected: none.
