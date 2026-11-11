# P6 Programlar: kurma, güncelleme, geri alma, çıkarma (tasarım)

Paket anahtarı: `p6-programlar`. Kapatılan boşluklar: A4, B7 (proje eşlemesi hariç), eleştirmen senaryosu 5 (kırıcı sürüm).
Dil: açıklamalar İngilizce; kullanıcıya görünen metinler ve kimlikler Türkçe, çıktıda görüneceği gibi.
Bağlayıcı kararlar: D1-D12 (görev metni). Bu belge yalnız tasarımdır, kütüphanede hiçbir dosya değiştirilmedi.
**Önkoşul (uygulama sırası):** (0) kullanıcı onayıyla, commit edilmemiş `programlar/` işinin commit'i; (1) P3 uygulanmış olsun (`yedekler.json` ve `.gitignore`, yalnız §6 P3 isteği için); (2) P1 `yapay-zeka-araclari.json` anahtarlarını kesinleştirmiş olsun (`claude-code, codex, antigravity, cursor, vscode-copilot`; farklıysa §6 P1 kuralı); (3) P6, P2 ve P5 ile birbirinden bağımsız çalışır; `proje-kullanimi.py --program` (P5) yoksa 'Programı çıkarma' 1. adımı `--skill <kimlik>` yedeğiyle yürür. P4 ve P8, P6'dan SONRA gelir (`--ozet-json`, `--sema`).

---------------------------------------------------------------------------------------------------

## 1. Purpose

Today (`programlar.json`, 3 cards; `rehber/11`, 78 lines; `araclar/program-denetim.py`, 346 lines) a program is only *described and reported*. Nothing checks that an update is safe, nothing says how a fresh AI session reaches a program after the machine-wide skill folders are emptied, nothing records OpenMontage's local patches in a durable place, nothing says how to roll back or remove a program, and "KART ESKİ" / HTTP 404 are silent (exit code is always 0, 404 is swallowed as "öğrenilemedi").

P6 delivers, with the smallest change and full backward compatibility:

1. **Card schema v2, two layers** (review). Required CORE: `giris_yolu`, `kurulum`, `geri_alma`, `cikarma`, `yedek`, `ortam_anahtarlari`. OPTIONAL (absence is never reported by `--sema`; validated only when present, findings are UYARI): `disariya_yazar`, `tedarik_dogrulama`, `kirici_surum`, `gizli_dosyalar`, `yerel_yamalar`. The three cards are filled with all of them, but long procedure texts live in `rehber/11`, not in the cards.
2. **`program-denetim.py` new modes** (all read-only): `--sema`, `--oncesi <ad>` (+`--hedef`; 8 main checks), `--iskelet <tür>`, `--pin-listesi <ad>`, plus `--ozet-json`, `--siki`, `--cevrimdisi`, `--ev`, `--yedek-koku`. 404 vs network error vs "repo moved" classification.
3. **`rehber/11`** new sections: entry paths after emptying, new-machine install, pre-update check, breaking release, local patches, rollback, removal, "fresh agent: request → steps", schema table.
4. **`promptlar/13-program-kur-guncelle.md`** (new): one copy-paste prompt for the four requests (install / update / roll back / remove).
5. **`programlar/*/KAYNAK.md`** small additions + a card-vs-KAYNAK.md consistency check.
6. **`araclar/testler/test_p6-programlar.py`** (new).

The update itself is NOT automated (D7). It stays a documented, numbered step list that a library session runs, each step needing the user's approval where stated. The tool only answers "is everything ready?" and "is the card valid?".

---------------------------------------------------------------------------------------------------

## 2. Existing behaviour relied on (file:line)

`araclar/program-denetim.py`
- :15-26 imports; `from ortak import KOK, gh_api, json_oku`. New code adds `GhBulunamadi, api_kapali, repo_takma_adlari, repo_guncel, KAYNAKLAR` (all exist in ortak.py: `KAYNAKLAR` :14, `json_oku` :44-48, `json_yaz` :51-57, `GhBulunamadi` :58-60, `gh_api` :63-78, `api_kapali` :81-83, `repo_takma_adlari` :433-441, `repo_guncel` :444-449).
- :29-44 `surum_ayikla`, `durum` (kaynak kartı, "güncel"/"YENİ SÜRÜM VAR"/"öğrenilemedi").
- :48-53 `YERINDE_TURLER`, `yol_ac` (`~` expansion).
- :56-62 `npm_kurulu_surum` reads `<yol>/package.json` only. :65-72 `npm_son_surum(paket, zaman_asimi=8)` swallows every exception and returns None (this is the "404 swallowed" gap). Tests monkeypatch it (`araclar/test.py:1620-1621`), so **its name, signature and None-on-failure return must not change**.
- :75-82 `git_okuma` (read-only git, `--no-optional-locks`, 60 s, stdin closed). :85-95 `porcelain_say`. :98-111 `git_kurulu` (returns `(sha, değişen, izlenmeyen)`; None counts when status fails).
- :114-129 `git_son(repo, dal, kurulu)` returns `(sha, geride)`; every failure collapses to `(None, None)`; uses `gh_api(..., deneme=2)`.
- :132-135 `sha_esit` (>=7 hex prefix). :143-161 `yerinde_durum` (state words `bu bilgisayarda kurulu değil`, `KART ESKİ`, `öğrenilemedi`, `güncel`, `YENİ SÜRÜM VAR`). Tests at `araclar/test.py:1521-1544` pin these exactly: **unchanged**.
- :175-198 `dist_info_oku(venv)` {normal ad: sürüm} from dist-info METADATA, no pip. :232-247 `pin_karsilastir`.
- :250-269 `yerinde_denetle(ad, p)` builds the dict `r`; :293-342 `main(argv)`: args `--kart`, `--cikti` (:294-296); per-card try/except keeps exit 0 (:301-309; tests :1615-1636 feed malformed cards: `sabit_surumler` as a list, a card with no `repo`); kaynak branch :316-325 calls `gh_api(f"repos/{p['repo']}/releases/latest")`; report written only when the date-stripped text changed (:338-341); always `return 0` (:342).
- Docstring :1-14 promises: never installs, never runs program commands, never opens key/session files, exit 0 always.

`araclar/ortak.py`: `gh_api` raises `GhBulunamadi` on HTTP 404/422 (:58-72), `RuntimeError("gh api kapalı…")` when the endpoint is disabled (:73-74), sleeps 60 s*n on rate limit (:75-77) — so every new call uses `deneme=2`.

`araclar/arsiv-guncelle.py:205-206` runs `program-denetim.py` (no arguments) only inside `--uygula` and only reads the return code. **No-argument behaviour must stay valid** (P4 will additionally call `--ozet-json`).

`araclar/test.py:1492-1513` checks per card: `KAYNAK.md` exists, `kaynaklar.json` record has `"program": <ad>`, and for yerinde cards `yerinde.tur/yol/paket|dal`, `kutuphane_surumu|kutuphane_commit`, no `kaynak_kopyasi`. P6 keeps all of that true; the new schema check is additional.

`programlar.json` today: etsyotomasyon :4-35 (own `kurulum` object :15-19 with keys windows/macos/kaynaktan; `veri_yeri` :20; `guncelleme_adimlari` :25-30; `asla` :31-34), hyperframes :36-86 (`kendini_guncelleme` :54-58; `skill_yazimi` :59-65; steps :72-79; `asla` :80-85), openmontage :87-142 (`sabit_surumler` :102-114; `repo_notu` :116; `veri_yeri` :117; `anahtarlar` :118; `skill_yazimi` :121; `yerel_degisiklik` :122 prose only, no machine-readable patch list; steps :124-132; `asla` :133-141).

`rehber/11-program-yonetimi.md`: yedek rule :57-62 ("yalnız `~/Documents/Claude/yedek/<program>-<YYYY-AA-GG>/`"; HF: `config.json` not copied; `~/.config/openmontage` never copied; kept until the user approves deletion); :62 "Ortam değişkenini kullanıcı kendisi tanımlar; agent tanımlamaz" (contradicted in practice on 2026-11-11, DURUM.md:34); :69-70 yerinde update flow; :74-76 the single exception to `CLAUDE.md` rule 1; no rollback/removal text (the only "sil" is :61).

`~/.openmontage` facts measured read-only on 2026-11-12: `git status --porcelain` shows 9 modified tracked files (`.agents/skills/gsap-plugins/SKILL.md`, `lib/clip_embedder.py`, `remotion-composer/package-lock.json`, `remotion-composer/package.json`, `remotion-composer/src/Explainer.tsx`, `remotion-composer/src/components/StatReveal.tsx`, `tools/analysis/video_understand.py`, `tools/capture/screen_recorder.py`, `tools/enhancement/face_restore.py`) and 6 untracked paths (`.agents/skills/gsap-plugins/SKILL.md.2026-10-15-oncesi`, `clips_cache/`, `gfpgan/`, `remotion-composer/remotion.config.ts`, `remotion-composer/src/Explainer.tsx.bak-2026-09-20`, `…bak-2026-09-30`); `origin` = `https://github.com/calesthio/OpenMontage.git`; the repo ships `AGENTS.md`, `AGENT_GUIDE.md`, `CLAUDE.md`, `CODEX.md`; Makefile has `preflight`/`hyperframes-doctor` targets and `setup` default; `.venv/bin/python` → uv python 3.10. `~/.config/openmontage/` holds `global-skill-links.txt` (79 lines). `~/.claude/commands/openmontage.md` and `~/.claude/skills/openmontage/SKILL.md` exist (entry point today). Existing backups: `~/Documents/Claude/yedek/ayar-2026-11-11/`, `global-skills-2026-11-08/` (no program backup yet). Installed HyperFrames `0.9.23` at `/usr/local/lib/node_modules/hyperframes`, binary `/usr/local/bin/hyperframes`.

Audit notes: `akis-07` (gaps 1-10 + second-reader additions a-f), `akis-08` (gaps 3-4), `ozet-bolum2-4.md` A4/B7, `elestiri-donus.md` scenario 5.

---------------------------------------------------------------------------------------------------

## 3. Changes per file

### 3.1 `programlar.json` (edit; owner P6)

Rules: old keys stay; no existing field is renamed or removed; only additions. Version-of-card marker: new top-level key `"sema": 2` next to `_aciklama` (the tool ignores it if missing; `--sema` expects 2 once the cards are migrated). No project names anywhere (D8). No secret values (D9).

**New/extended fields (schema v2).** Required = HATA in `--sema` when missing. "Y" = yerinde, "K" = kaynak-kopyalı, "G" = git-checkout, "N" = npm-global.

| Field | Layer | Shape | Required for |
|---|---|---|---|
| `giris_yolu` | CORE | object, see 3.1.1 | all |
| `kurulum` | CORE | object: `adimlar` (list[str], non-empty), `dogrulama` (list[str], non-empty), optional `on_kosullar` (list), `yapma` (list); legacy keys `windows`,`macos`,`kaynaktan` (etsyotomasyon) stay allowed | all |
| `geri_alma` | CORE | object: `ne_zaman` (list), `adimlar` (list, non-empty), `dogrulama` (list), `sinir` (str) | all |
| `cikarma` | CORE | object: `makineden` (list[str], non-empty), `dokunulmaz` (list[str]) | all |
| `yedek` | CORE | object: `kok` (str, `~/Documents/Claude/yedek`), `tazelik_gun` (int 1-30), `zorunlu` (list[str], must contain `"KAYIT.json"`), `yasak_adlar` (list[str]) | Y (K: optional, validated if present) |
| `ortam_anahtarlari` | CORE | list of `{ad, beklenen, gerekli(bool), nerede(list[str]), not}`; may be `[]` | all |
| `gizli_dosyalar` | optional | list[str] paths (existence only, never opened); may be `[]` | none |
| `disariya_yazar` | optional | list of `{yol, tur, ne, yedeklenir(bool), dogrulandi(bool)}`; `tur` ∈ `veri, program, skill, bag, ayar, cikti, onbellek, anahtar` | none |
| `yerel_yamalar` | optional (G: recommended) | object, see 3.1.2. Absent on a git card = `bilinen` is empty, so every local change is "unrecorded" and `--oncesi` stops (safe default) | none |
| `kirici_surum` | optional | object, see 3.1.3. Absent = `--oncesi` prints `BİLGİ: kayıtsız` for the breaking-candidate check | none |
| `tedarik_dogrulama` | optional | object, see 3.1.4 | none |

**Severity rule (review).** In `--sema` and `--oncesi`: a missing/invalid CORE field or a core-consistency failure (key != `ad`, `KAYNAK.md` text mismatch, no `kaynaklar.json` record, `<DOLDUR>`, secret-shaped string) = `HATA`; an optional field absent = silent; an optional field present but invalid = `UYARI`. **Library-wide gates never fail on card findings** (they are reported as UYARI by `dogrula.py` and `test.py`, §6 P8); the only library-wide HATA is an unreadable or invalid-JSON `programlar.json`. So a forgotten card field can never roll back the monthly `--birlestir`. `--sema --siki` exits 1 on any HATA (used by the update steps, not by library gates).

Existing fields that the schema now also requires (all three cards already have them except where noted): `ad` (= key), `repo`, `tur`, `lisans`, `ucret` ∈ `ucretsiz|kismen|ucretli`, `ne_yapar`, `veri_yeri`, `ag`, `kendini_gunceller` (bool), `skilleri` (list), `guncelleme_adimlari` (non-empty, must contain a step with the text `program-denetim.py --oncesi`), `asla` (non-empty). Version fields: K → `kutuphane_surumu` + `kutuphane_commit` (40 hex) + `kaynak_kopyasi` (existing non-empty dir); Y/N → `kutuphane_surumu`; Y/G → `kutuphane_commit` (40 hex). `yerinde.tur/yol/paket|dal` as `test.py:1492-1513` already requires. `venv` ⇔ `sabit_surumler` (both present or both absent; `sabit_surumler` must be a dict).

#### 3.1.1 `giris_yolu` (closes A4 "how an agent reaches the program after the folders are emptied")

```
"giris_yolu": {
  "kural": "<str: one sentence>",
  "kilavuz": "<path of the file an agent reads first, or ''>",
  "calistirma": "<str: command pattern or ''>",
  "karar": "<str: open user decision or ''>",
  "araclar": { "<arac-anahtari>": {"durum": <enum>, "yol": "<path or ''>", "nasil": "<str>"}, ... },
  "hepsi":   {"durum": <enum>, "yol": "<path or ''>", "nasil": "<str>"}
}
```
- Tool keys: the five installed tools of D1: `claude-code`, `codex`, `antigravity`, `cursor`, `vscode-copilot`; optional `gemini-cli`, `copilot-cli` (D1: off by default). Rule: either `hepsi` is present, or `araclar` has all five D1 keys. Unknown keys = HATA. (Constants `ARAC_ANAHTARLARI`, `ARAC_ISTEGE_BAGLI` in the tool; P1 must use the same key strings, see §6.)
- `durum` enum (5 values): `yerinde` (path exists today and stays after emptying), `program-klasoru` (reached through the program's own guide files; session opened in the program folder or prompt points at `kilavuz`), `proje-skili` (reached through skills installed into each project by `skill-ekle.py`, or a command-line binary), `karar-bekliyor` (user decision pending; Bölüm 4 soru 1), `yok` (not supported; reason in `nasil`).
- `--oncesi` check: if `yol` is non-empty and `durum` ∈ {`yerinde`, `program-klasoru`, `proje-skili`} the path must exist (`UYARI: giriş yolu kırık: <arac>: <yol>`); `kilavuz` must exist if non-empty.

Exact values to write:

hyperframes:
```
"giris_yolu": {
  "kural": "HyperFrames bir komut satırı programıdır: her araç onu kabuktan çalıştırır; skilleri genel klasörden değil, projeye skill-ekle.py ile kurulan kopyalardan okunur.",
  "kilavuz": "",
  "calistirma": "/usr/local/bin/hyperframes <komut>   (ortamda HYPERFRAMES_SKIP_SKILLS=1 tanımlı olmalı; init, skills, skills update, update çalıştırılmaz)",
  "karar": "",
  "hepsi": {"durum": "proje-skili", "yol": "/usr/local/bin/hyperframes",
            "nasil": "Skiller (karttaki 'skilleri' listesi) projeye `python3 araclar/skill-ekle.py <proje> --skill <kimlik>` ile kurulur; her aracın proje skill klasörü yapay-zeka-araclari.json'da yazılıdır. CLI her araçta aynı komuttur."}
}
```
openmontage (values proven today; the Claude entry is `karar-bekliyor` because the new place of the `openmontage` entry skill after emptying is an open user decision, DURUM.md:74,106; Bölüm 4 soru 1):
```
"giris_yolu": {
  "kural": "OpenMontage skill değil, git klonudur: araç oturumu ~/.openmontage klasöründe açılır ya da istem kılavuz dosyasını okutur; program kendi AGENTS.md / CODEX.md / CLAUDE.md / AGENT_GUIDE.md dosyalarını taşır.",
  "kilavuz": "~/.openmontage/AGENT_GUIDE.md",
  "calistirma": "cd ~/.openmontage && .venv/bin/python <komut>   (her çağrıda önce cd; sistem python'u kullanılmaz)",
  "karar": "Boşaltma sonrası Claude Code girişinin yeri (komut + openmontage giriş skili) kullanıcı kararı bekliyor.",
  "araclar": {
    "claude-code": {"durum": "karar-bekliyor", "yol": "~/.claude/commands/openmontage.md", "nasil": "Bugün: ~/.claude/CLAUDE.md satırı + /openmontage komutu + ~/.claude/skills/openmontage. Skill klasörü boşaltılınca skilin yeni yeri kararlaştırılmadı; komut ve CLAUDE.md satırı kalır."},
    "codex":       {"durum": "program-klasoru", "yol": "~/.openmontage/AGENTS.md", "nasil": "Oturumu ~/.openmontage klasöründe aç (AGENTS.md ve CODEX.md orada). Başka klasörden: istemde 'önce ~/.openmontage/AGENT_GUIDE.md oku' yaz."},
    "antigravity": {"durum": "program-klasoru", "yol": "~/.openmontage/AGENTS.md", "nasil": "Aynı: çalışma alanı ~/.openmontage ya da istemde kılavuz yolu."},
    "cursor":      {"durum": "program-klasoru", "yol": "~/.openmontage/AGENTS.md", "nasil": "Aynı: klasörü Cursor'da aç ya da istemde kılavuz yolu."},
    "vscode-copilot": {"durum": "program-klasoru", "yol": "~/.openmontage/AGENTS.md", "nasil": "Aynı: klasörü VS Code'da aç ya da istemde kılavuz yolu."}
  }
}
```
etsyotomasyon:
```
"giris_yolu": {
  "kural": "Etsyotomasyon araca bağlı değildir: komut satırı ve localhost paneli; skili yok.",
  "kilavuz": "", "calistirma": "~/.etsyotomasyon-uygulama/bin/etsyotomasyon <komut>   (kaynaktan kurulumda)", "karar": "",
  "hepsi": {"durum": "yok", "yol": "", "nasil": "Araç-özel giriş yok; kullanım notu projeye yazılır (kütüphane kuralı: kopya projeye konmaz)."}
}
```

#### 3.1.2 `yerel_yamalar` (git-checkout only; closes "patches recorded", scenario 5c)

Purpose: the card is the durable *manifest* of which paths in the clone are local patches (paths and purposes only, never code, never secrets). The patch *content* is saved by the backup step into the backup folder (`yerel-yamalar.patch`, `izlenmeyen-yollar.txt`), not into the library or git.
```
"yerel_yamalar": {
  "kural": "Klonda repoda olmayan her değişiklik bu listede kayıtlı olmalı; kayıtsız değişiklik varsa güncelleme ön kontrolü durur.",
  "bilinen": [ {"yol": "<path; trailing '/' = folder prefix>", "tur": "izlenen|izlenmeyen|venv",
                "amac": "<str or 'ölçülmedi'>", "yedek": "kopya|liste", "yeniden_uygula": true|false} ],
  "yedekleme": {"izlenen": "git diff --binary > yerel-yamalar.patch",
                "izlenmeyen": "git ls-files --others --exclude-standard (boyutlarıyla) > izlenmeyen-yollar.txt; 'kopya' olanlar izlenmeyen/ altına kopyalanır"},
  "rehber": "rehber/11-program-yonetimi.md → Yerel yamalar"
}
```
`bilinen` for openmontage (exact; `amac` is honest: nothing measured about purpose except where the card already says so):
- tur `izlenen`, yedek `kopya`, yeniden_uygula true, amac `"yerel değişiklik; amacı kayıtlı değil (kullanıcıya sorulur)"`: `.agents/skills/gsap-plugins/SKILL.md`, `lib/clip_embedder.py`, `remotion-composer/package-lock.json`, `remotion-composer/package.json`, `remotion-composer/src/Explainer.tsx`, `remotion-composer/src/components/StatReveal.tsx`, `tools/analysis/video_understand.py`, `tools/capture/screen_recorder.py`, `tools/enhancement/face_restore.py`.
- tur `izlenmeyen`: `remotion-composer/remotion.config.ts` (kopya, yeniden_uygula true); `.agents/skills/gsap-plugins/SKILL.md.2026-10-15-oncesi`, `remotion-composer/src/Explainer.tsx.bak-2026-09-20`, `remotion-composer/src/Explainer.tsx.bak-2026-09-30` (kopya, yeniden_uygula false, amac "elle yedek dosyası"); `clips_cache/`, `gfpgan/` (yedek `liste`, yeniden_uygula false, amac "ölçülmedi (önbellek ya da model dosyası olabilir; içeriği bilinmeden kopyalanmaz)").
- tur `venv`: yol `.venv/lib/python3.10/site-packages/basicsr/`, amac `"skill notunda geçen içe aktarma yaması; ölçülmedi"`, yedek `liste`, yeniden_uygula true. (`dogrulandi` is not a field here: this entry is type `venv` and is skipped by the git-status comparison; it is documentation of an unverified patch.)

**Review change:** the ordered `uygulama` list is NOT a card field any more; the five steps below are written once into `rehber/11` → 'Yerel yamalar (git klonu)' (cards stay short; the card keeps `kural`, `bilinen`, `yedekleme`, `rehber`). Texts (implementer copies them into the guide):
1. "Güncellemeden önce: yedek klasörüne `git diff --binary > yerel-yamalar.patch`, `izlenmeyen-yollar.txt` ve 'kopya' olan izlenmeyen yollar alınır; `KAYIT.json` yazılır."
2. "Güncelleme `git pull --ff-only` ile yapılır (merge ve rebase yok). Yerel değişikliklerle çakışan dosya varsa git hiçbir şeyi değiştirmeden durur; o zaman çakışan dosyaların yeni sürümdeki farkı kullanıcıya gösterilir."
3. "Çakışan dosya için kullanıcı onaylarsa: yalnız o dosya `git checkout -- <yol>` ile eski haline getirilir (yaması yedekte), pull yapılır, sonra `git apply --3way --include=<yol> yerel-yamalar.patch` ile geri uygulanır. Çakışma işareti kalırsa durulur, kullanıcıya sorulur."
4. "Çakışmayan yamalar pull sonrası yerinde kalır. Her `yeniden_uygula: true` yolun hâlâ değişik olduğu `program-denetim.py --oncesi openmontage` çıktısındaki 'kayıtlı ama değişmemiş' satırından anlaşılır; yama upstream'e girdiyse ya da kaybolduysa kullanıcıya söylenir."
5. "Venv yaması (`tur: venv`) dosya okunarak denetlenir; `pip install` ile venv'e dokunulmaz."

For hyperframes and etsyotomasyon: `yerel_yamalar` absent (not required for N/K).

#### 3.1.3 `kirici_surum` (closes scenario 5a/5b)

```
"kirici_surum": {
  "kural": "<str>",
  "surum_hatti": "major|minor",         # npm: which component change is breaking (0.x => minor)
  "esik_commit": <int>,                  # git: ahead_by above this is a breaking candidate (omit for npm)
  "izle_dosyalar": [ "<path>", ... ],    # git: if the new commits change one of these => breaking candidate
  "deneme_klasoru": "~/Documents/Claude/deneme/<program>-<hedef>",
  "deneme_disk_gb": <number>,
  "rehber": "rehber/11-program-yonetimi.md → Kırıcı sürüm"
}
```
**Review change:** `deneme_adimlari` and `gecme_olcutu` are NOT card fields (cards stay short); the per-program lists below are written once into `rehber/11` → 'Kırıcı sürüm (önce ayrı klasörde dene)' as three sub-headings (HyperFrames, OpenMontage, etsyotomasyon). The card keeps `kural`, `surum_hatti`/`esik_commit`, `izle_dosyalar`, `deneme_klasoru`, `deneme_disk_gb`, `rehber`. The JSON blocks below are the texts to copy there; drop the two list keys when writing the card.

Tool rule (`kirici_adayi`, §3.2): candidate when (npm) the `surum_hatti` component of target > installed, or the release notes the agent reads contain a breaking marker (agent step; the tool only does the number rule), or (git) `geride > esik_commit`, or an `izle_dosyalar` path appears in the compare file list, or a `yerel_yamalar.bilinen` path (izlenen) appears in the compare file list (conflict likely). A candidate must be tried first in `deneme_klasoru` (a separate folder outside the library, outside git, never touching `/usr/local` or `~/.openmontage`), and only after the trial passes `gecme_olcutu` may the real update ask for approval.

hyperframes:
```
"kirici_surum": {
  "kural": "0.x sürümde minor değişimi (0.9 -> 0.10) ve major değişimi kırıcı sayılır; patch (0.9.23 -> 0.9.33) sayılmaz, ama release notunda 'breaking' geçerse kırıcı sayılır (ajan okur).",
  "surum_hatti": "minor",
  "deneme_klasoru": "~/Documents/Claude/deneme/hyperframes-<hedef>",
  "deneme_disk_gb": 1,
  "deneme_adimlari": [
    "Deneme klasörünü aç: mkdir -p ~/Documents/Claude/deneme/hyperframes-<hedef> (kütüphane klasörü ve git dışında)",
    "Ortamda HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_AUTO_INSTALL=1 HYPERFRAMES_NO_UPDATE_CHECK=1 tanımlıyken: npm install --prefix <deneme klasörü> hyperframes@<hedef> (genel kuruluma dokunmaz)",
    "<deneme klasörü>/node_modules/.bin/hyperframes --version komutu hedef sürümü yazmalı",
    "Kullanıcının seçtiği bir kompozisyon üzerinde lint, sonra çıktısı deneme klasörüne giden bir render dene. 'init', 'skills', 'update' ÇALIŞTIRILMAZ (skill yazar).",
    "Sonuç kullanıcıya raporlanır; deneme klasörü silinmez, silmek için kullanıcıya sorulur"
  ],
  "gecme_olcutu": ["--version hedefi yazdı", "lint hatasız", "render çıktısı açılıyor", "genel skill klasörlerinde yeni girdi yok (genel-bekci varsa)"]
}
```
openmontage:
```
"kirici_surum": {
  "kural": "Aday sayılır: main dalı kurulu commit'ten 50'den fazla commit ileride (bugün 244), ya da yeni commit'ler izle_dosyalar'dan birini değiştiriyorsa, ya da yeni commit'ler karttaki bir yerel yama dosyasına dokunuyorsa.",
  "esik_commit": 50,
  "izle_dosyalar": ["requirements.txt", "Makefile", "remotion-composer/package.json", "pyproject.toml"],
  "deneme_klasoru": "~/Documents/Claude/deneme/openmontage-<hedef-ilk-8-hane>",
  "deneme_disk_gb": 8,
  "deneme_adimlari": [
    "Disk: en az 8 GB boş olmalı (ön kontrol söyler). Klasörü aç: mkdir -p ~/Documents/Claude/deneme",
    "git clone --local ~/.openmontage ~/Documents/Claude/deneme/openmontage-<hedef-ilk-8-hane> (yerel klon, ağ yok; ~/.openmontage'e dokunmaz, çalışma ağacı yamaları taşınmaz)",
    "Yalnız deneme klonunda: git remote set-url origin https://github.com/OpenMontageInc/OpenMontage.git ; git fetch origin main ; git checkout --detach <hedef>",
    "Deneme klonunda yeni venv: uv venv --python 3.10 .venv ; requirements.txt kurulur, sonra karttaki sabit_surumler yeniden uygulanır (pip install paket==sürüm). 'make setup' ÇALIŞTIRILMAZ, ~/.openmontage/.venv'e dokunulmaz.",
    "Anahtar dosyası deneme klonuna kopyalanmaz ve bağlanmaz; ücretsiz yerel araçlarla preflight çalıştırılır (openmontage skilindeki 'Command pattern' bölümü; make preflight karşılığı).",
    "Karttaki her yeniden_uygula yama yolu için yeni sürümdeki dosya kullanıcıya gösterilir: yama hâlâ gerekli mi, çakışıyor mu",
    "Sonuç kullanıcıya raporlanır; deneme klasörü silinmez, silmek için kullanıcıya sorulur"
  ],
  "gecme_olcutu": ["preflight hatasız", "sabit paketler pip-freeze karşılaştırmasında aynı", "yama dosyalarının her biri için karar verildi (uygula / yeni sürümde gereksiz / çakışıyor)"]
}
```
etsyotomasyon: optional; write `surum_hatti: "major"`, `deneme_klasoru: "~/Documents/Claude/deneme/etsyotomasyon-<hedef>"`, `deneme_disk_gb: 1`, deneme adımları (rehber): 3 lines (yeni kaynağı ayrı klasöre aç; ayrı venv: `python3 -m venv <klasor>/.venv && <klasor>/.venv/bin/pip install <klasör>/kaynak`; `etsyotomasyon --help` çalıştır, anahtar dosyası bağlanmaz), `gecme_olcutu` 2 lines.

#### 3.1.4 `tedarik_dogrulama` (third-party binaries; closes akis-07 "kaçırılan (e)")

```
"tedarik_dogrulama": {
  "yayinci": {"hesap": "<owner>", "ucuncu_taraf": true|false, "imza": "yok|var|npm-kayit|git-commit", "not": "<str>"},
  "ozet": {"tur": "sha256|npm-integrity|git-commit|yok", "deger": "<value or ''>", "ne_icin": "<what the value was taken from>", "kayit_tarihi": "YYYY-AA-GG or ''"},
  "kural": "<str>"
}
```
- etsyotomasyon: `yayinci.hesap` `wj-sidiss`, `ucuncu_taraf` true, `imza` `yok` (exe/zip imzasız, mevcut `kurulum.windows/macos` metni), `ozet.tur` `git-commit`, `ozet.deger` `950dc9498e46e2fdcd8a369512c26698de54e293` (kaynak kopyasının commit'i, KAYNAK.md ile aynı), `kural`: "Kaynaktan kurulum (kütüphanedeki kaynak kopyası, sabit commit) ikili release dosyasına tercih edilir. Release exe/zip yalnız indirilen dosyanın sha256'sı `ozet`'e kaydedilip kullanıcı onayladıktan sonra kullanılır; kayıtsız ikili kurulmaz." (No sha256 value is invented; recording it needs a download = approval, §7/§8.)
- hyperframes: `yayinci.hesap` `heygen-com`, `ucuncu_taraf` false, `imza` `npm-kayit`, `ozet.tur` `npm-integrity`, `ozet.deger` `''` and `kayit_tarihi` `''` until filled; implementer fills `deger` from `https://registry.npmjs.org/hyperframes/0.9.23` → `dist.integrity` via the new helper `npm_integrity(paket, surum)` (read-only network; if offline leave `''` and say so). `kural`: "Kurulacak sürümün registry integrity değeri kayda geçirilir; ön kontrol kayıtlı değer registry'dekiyle farklıysa durur (sürüm sessizce yeniden yayımlanmış olabilir)."
- openmontage: `yayinci.hesap` `OpenMontageInc`, `ucuncu_taraf` false, `imza` `git-commit`, `ozet.tur` `git-commit`, `ozet.deger` = `kutuphane_commit`, `kural`: "Onay commit'in tam sha'sıyla verilir; dal adıyla ('main') verilmez."

#### 3.1.5 Other per-card values (exact)

`yedek`:
- hyperframes: `{"kok": "~/Documents/Claude/yedek", "tazelik_gun": 3, "zorunlu": ["KAYIT.json", "hyperframes-veri", "paket"], "yasak_adlar": ["config.json"]}` (matches the existing step: `~/.hyperframes` without `config.json` + the package folder; `rehber/11:59-61`).
- openmontage: `{"kok": "~/Documents/Claude/yedek", "tazelik_gun": 3, "zorunlu": ["KAYIT.json", "yerel-yamalar.patch", "izlenmeyen-yollar.txt", "pip-freeze.txt", "bag-listesi.txt"], "yasak_adlar": [".env"]}`.
- etsyotomasyon: `{"kok": "~/Documents/Claude/yedek", "tazelik_gun": 3, "zorunlu": ["KAYIT.json"], "yasak_adlar": [".env", "token.json"]}` (data folder `~/.etsyotomasyon` is not copied: it is keys + session; only `KAYIT.json` with the previous version is required).
Tool-wide always-forbidden names inside any backup folder (constant `YASAK_ADLAR`): `.env`, `token.json`, `credentials.json`, `auth.json`.

`ortam_anahtarlari`:
- hyperframes: `[{"ad": "HYPERFRAMES_SKIP_SKILLS", "beklenen": "1", "gerekli": true, "nerede": ["~/.zshenv", "~/.zshrc", "~/.claude/settings.json"], "not": "Genel skill klasörlerine geri yazmayı durdurur."}, {"ad": "HYPERFRAMES_NO_AUTO_INSTALL", "beklenen": "1", "gerekli": false, "nerede": ["~/.zshenv", "~/.zshrc", "~/.claude/settings.json"], "not": "Sürüm onaydan önce değişmesin; kullanıcı kararı (bugün tanımlı değil)."}, {"ad": "HYPERFRAMES_NO_UPDATE_CHECK", "beklenen": "1", "gerekli": false, "nerede": [...same], "not": "Güncelleme kontrolünü kapatır; kullanıcı kararı."}]`
- openmontage: only `HYPERFRAMES_SKIP_SKILLS` (gerekli true; OM'nin hyperframes hedefleri çağrıldığında skill yazmasın).
- etsyotomasyon: `[{"ad": "ETSYOTOMASYON_NO_UPDATE_CHECK", "beklenen": "1", "gerekli": false, "nerede": [], "not": "Sürüm kontrolünü kapatır (kartta ag alanı)."}]`.
How a file counts: `~/.zshenv` / `~/.zshrc`: a line `export NAME=value` or `NAME=value` not starting with `#`; `~/.claude/settings.json`: `env.NAME`. `nerede: []` means "check only the process environment".

`gizli_dosyalar` (existence via `os.path.lexists` only; never opened, never printed beyond "var/yok"): hyperframes `["~/.hyperframes/config.json"]`; openmontage `["~/.config/openmontage/.env"]`; etsyotomasyon `["~/.etsyotomasyon/.env", "~/.etsyotomasyon/token.json"]`.

`disariya_yazar` (all `dogrulandi` values: true only where an existing card/KAYNAK.md sentence or today's ls proves it):
- hyperframes: `~/.hyperframes` (veri, yedeklenir true, dogrulandi true); `/usr/local/lib/node_modules/hyperframes` (program, true, true); `/usr/local/bin/hyperframes` (program, false, true); `~/.claude/skills` (skill, false, true; "yalnız SKIP anahtarı yokken"); `~/.agents/skills` (skill, false, true); `~/.agents/.skill-lock.json` (ayar, false, true); `~/.gemini/skills`, `~/.gemini/antigravity/skills`, `~/.gemini/antigravity-cli/skills`, `~/.cursor/skills`, `~/.copilot/skills` (bag, false, true: card `skill_yazimi.klasorler`); `~/.npm` (onbellek, false, **false**: not measured).
- openmontage: `~/.openmontage` (program, true, true); `~/Movies/OpenMontage` (cikti, false, true); `~/.config/openmontage` (anahtar, false, true; "açılmaz, kopyalanmaz"); `~/.claude/skills` (bag, true, true; ~74 bağ, kullanıcının manifestiyle, program yazmaz); `~/.claude/commands/openmontage.md` (ayar, true, true); `~/.npm` (onbellek, false, false: `make setup` npm install/npx çağırır, ölçülmedi).
- etsyotomasyon: `~/.etsyotomasyon` (anahtar, false, true); `~/Desktop/Etsy Studio` (cikti, false, true; card says Masaüstü/'Etsy Studio'); `~/.etsyotomasyon-uygulama` (program, false, true; kaynaktan kurulum venv'i).

`geri_alma` (exact texts):
- hyperframes: `ne_zaman`: ["Yeni sürümde render/lint bozuk", "Güncelleme sonrası genel klasörlerde beklenmeyen skill girdisi çıktı", "Kullanıcı eski sürümü istedi"]; `adimlar`: ["Önceki sürüm yedekteki KAYIT.json → onceki.surum alanındadır", "Kullanıcıdan geri alma için ayrı onay al", "HYPERFRAMES_SKIP_SKILLS=1 tanımlıyken: npm install -g hyperframes@<onceki.surum> (tek sürüm; 'latest' yazılmaz)", "Registry sürümü kaldırdıysa yedekteki 'paket' klasörü /usr/local/lib/node_modules/hyperframes yerine konur (kullanıcı onayıyla)", "Veri bozulduysa yedekteki 'hyperframes-veri' dosyaları ~/.hyperframes içine geri kopyalanır (config.json hiç kopyalanmadığı için ezilmez)", "Kart sürümü (kutuphane_surumu), KAYNAK.md ve tedarik_dogrulama.ozet önceki değere çevrilir; commit"]; `dogrulama`: ["program-denetim.py: kurulu = karttaki, durum güncel ya da YENİ SÜRÜM VAR (KART ESKİ değil)", "program-denetim.py --oncesi hyperframes: ortam anahtarı satırı TAMAM"]; `sinir`: "Yedek yoksa geri alma yalnız registry'deki sürümle yapılabilir; yedeği olmayan güncelleme yapılmaz."
- openmontage: `ne_zaman`: ["Güncelleme sonrası preflight ya da bir pipeline bozuk", "Sabit paket sürümlerinden biri değişti", "Yama geri uygulanamadı"]; `adimlar`: ["Önceki commit yedekteki KAYIT.json → onceki.commit alanındadır", "Kullanıcıdan geri alma için ayrı onay al; yerel yamalar önce yedekteki yerel-yamalar.patch ile güvence altındadır", "Önceki commit'e dönmek için: git -C ~/.openmontage switch --detach <onceki.commit>. git reset --hard, git checkout -B ve git clean KULLANILMAZ (yerel yamaları ezer). Yerel değişikliklerle çakışan dosya varsa git hiçbir şeyi değiştirmeden durur; o zaman sonraki adım", "Çakışırsa: yalnız o dosyada git checkout -- <yol> (yaması yedekte), switch, sonra git apply --3way --include=<yol> yerel-yamalar.patch", "Venv bozulduysa: yedekteki pip-freeze.txt ile pip install --no-deps -r pip-freeze.txt (kullanıcı onayıyla; ağ ve torch için yer gerekir); sabit_surumler kartla karşılaştırılır", "Çalışma ağacı geri dönünce dal main'e dönülür: git switch main yalnız kullanıcı isterse (main ileride kalır; commit'i kayda göre sabit tutan 'detached' durum ön kontrolde UYARI verir)", "Kart kutuphane_commit, KAYNAK.md ve tedarik_dogrulama.ozet.deger önceki commit'e çevrilir; commit"]; `dogrulama`: ["program-denetim.py: kurulu commit = karttaki; sabit sürümler N/N tutuyor", "~/.claude/skills içindeki openmontage bağları kırık değil (bag-listesi.txt ile karşılaştır)"]; `sinir`: "Yedekte yerel-yamalar.patch yoksa geri alma ve güncelleme yapılmaz."
- etsyotomasyon: `ne_zaman`: ["Yeni sürüm bozuk"]; `adimlar`: ["Önceki sürüm KAYIT.json → onceki.surum", "Kaynak kopyası git geçmişinden geri alınır: git checkout <önceki commit> -- programlar/etsyotomasyon (kütüphane git'inde; kullanıcı onayıyla)", "Programı kullanan makinede önceki release dosyası ya da kaynaktan pip install yeniden kurulur", "Kart ve KAYNAK.md önceki değere döner; commit"]; `dogrulama`: ["program-denetim.py: kaynak kopyası var, kütüphane sürümü = karttaki"]; `sinir`: "Veri klasörü (~/.etsyotomasyon) hiç kopyalanmaz ve geri alınmaz."

`cikarma` (machine-specific; the library-side removal steps are generic and live in `rehber/11`):
- hyperframes: `makineden`: ["Kullanıcıdan ayrı onay; önce yedek (KAYIT.json + hyperframes-veri + paket)", "npm uninstall -g hyperframes (HYPERFRAMES_SKIP_SKILLS=1 tanımlıyken)", "Genel skill klasörlerinde HyperFrames'in kendi yazdığı skiller varsa bunları kaldırmak genel klasör boşaltma prosedürünün işidir (rehber/12), burada yapılmaz"]; `dokunulmaz`: ["~/.hyperframes (kullanıcı silmek isterse kendisi yapar: kimlik ve tohum değerleri içerir)", "projelerdeki kompozisyonlar"].
- openmontage: `makineden`: ["Kullanıcıdan ayrı onay; önce yedek (yerel yamalar + pip-freeze + bağ listesi)", "Önce ~/.claude/skills içindeki ~74 openmontage bağı kullanıcının manifestiyle (~/.config/openmontage/global-skill-links.txt) kaldırılır; bu genel klasör işlemi rehber/12 kapsamındadır", "Sonra ~/.openmontage klasörü kullanıcı kararıyla taşınır/silinir (4,6 GB; kalıcı silme için ayrıca onay)", "~/.claude/commands/openmontage.md ve global CLAUDE.md satırı kullanıcının dosyalarıdır; kaldırmayı kullanıcı yapar"]; `dokunulmaz`: ["~/.config/openmontage (anahtarlar)", "~/Movies/OpenMontage (üretilen videolar)"].
- etsyotomasyon: `makineden`: ["Kullanıcıdan ayrı onay", "Kaynaktan kurulumda ~/.etsyotomasyon-uygulama silinir; release dosyasıyla kurulumda uygulama kullanıcı tarafından kaldırılır"]; `dokunulmaz`: ["~/.etsyotomasyon (anahtarlar ve oturum)", "~/Desktop/Etsy Studio"].

`kurulum` (new-machine steps; `dogrulama` = read-only checks; `yapma` = forbidden):
- hyperframes: `on_kosullar`: ["Node ve npm kurulu", "~/.zshenv, ~/.zshrc ve ~/.claude/settings.json içinde HYPERFRAMES_SKIP_SKILLS=1 tanımlı (kullanıcı tanımlar ya da açıkça ajana yaptırır) — program kurulmadan ÖNCE"]; `adimlar`: ["Kullanıcıdan ayrı onay", "HYPERFRAMES_SKIP_SKILLS=1 tanımlıyken: npm install -g hyperframes@<kutuphane_surumu> (kartta yazan sürüm; 'latest' yazılmaz)", "tedarik_dogrulama.ozet.deger doluysa kurulu paketin registry integrity'si karşılaştırılır", "Skiller genel klasöre değil, projeye skill-ekle.py ile kurulur"]; `dogrulama`: ["python3 araclar/program-denetim.py: hyperframes satırı 'güncel' ya da 'YENİ SÜRÜM VAR', 'KART ESKİ' değil", "python3 araclar/program-denetim.py --oncesi hyperframes: ortam anahtarı TAMAM"]; `yapma`: ["hyperframes init / skills / skills update / update çalıştırma", "npx skills çalıştırma"].
- openmontage: `on_kosullar`: ["git, Python 3.10 (ya da uv), Node/npm; yaklaşık 8 GB boş disk", "HYPERFRAMES_SKIP_SKILLS=1 tanımlı", "API anahtarları kullanıcı tarafından ~/.config/openmontage/.env içine konur (ajan açmaz, sormaz)"]; `adimlar`: ["Kullanıcıdan ayrı onay", "git clone https://github.com/OpenMontageInc/OpenMontage ~/.openmontage ; git -C ~/.openmontage checkout --detach <kutuphane_commit>", "Venv: uv venv --python 3.10 ~/.openmontage/.venv ; requirements.txt kurulur; sonra karttaki sabit_surumler tek tek paket==sürüm olarak yeniden uygulanır. 'make setup' olduğu gibi çalıştırılmaz (npx ve npm install çağırır).", "remotion-composer içinde yalnız gereken npm adımı, kullanıcıya gösterilerek", "Yerel yamalar: karttaki yerel_yamalar.bilinen listesi bu makinede YOKTUR; yedeğin yerel-yamalar.patch dosyası varsa git apply --3way ile uygulanır, yoksa kullanıcıya söylenir", "Giriş: giris_yolu alanındaki araç satırları (kullanıcı kararlarıyla) uygulanır"]; `dogrulama`: ["python3 araclar/program-denetim.py: openmontage kurulu commit = karttaki, sabit sürümler N/N", "openmontage skilindeki preflight komutu (ağ kullanmayan sağlayıcı menüsü) hatasız"]; `yapma`: ["pip install -U / --upgrade", "make setup ortam anahtarsız ve onaysız", "npx ile hyperframes çağırma", ".env açma"].
- etsyotomasyon: keep legacy keys `windows`, `macos`, `kaynaktan`; add `adimlar`: ["Kullanıcıdan ayrı onay", "Önce kaynaktan kurulum (kaynak_kopyasi, sabit commit) tercih edilir; release exe/zip yalnız tedarik_dogrulama kuralıyla", "Etsy Keystring/Shared secret ve OAuth bağlama adımlarını kullanıcı yapar"], `dogrulama`: ["python3 araclar/program-denetim.py: kaynak kopyası var, sürüm güncel"].

`guncelleme_adimlari` rewrite (the only existing key whose text changes; keep every existing step's content, add the new steps at the marked places). Exact final lists:

hyperframes:
1. "program-denetim.py yeni sürümü ('YENİ SÜRÜM VAR') ya da kartın eskidiğini ('KART ESKİ') gösterir; 'KART ESKİ' ise önce sebebi bulunur, güncelleme yapılmaz"
2. "python3 araclar/program-denetim.py --oncesi hyperframes çalıştırılır; 'KIRICI ADAYI' çıkarsa önce rehber/11 → 'Kırıcı sürüm' deneme adımları ayrı klasörde uygulanır, geçmeden onay istenmez"
3. "kullanıcıya sürüm farkı + release notu özeti sunulur ve bu güncelleme için ayrıca onay istenir (her seferinde)"
4. "yedek: ~/Documents/Claude/yedek/hyperframes-<YYYY-AA-GG>/ altına hyperframes-veri (config.json hariç), paket klasörü ve KAYIT.json (rehber/11 → 'Yedek kaydı'); kütüphane klasörüne ve git'e asla"
5. "program-denetim.py --oncesi hyperframes tekrar çalıştırılır; 'HAZIR' demeden devam edilmez"
6. "onaydan sonra YALNIZ kütüphane oturumu, HYPERFRAMES_SKIP_SKILLS=1 tanımlıyken: npm install -g hyperframes@<sürüm> (tek sürüm sabitlenir, 'latest' yazılmaz)"
7. "sonra yeniden denetim: program-denetim.py kurulu sürümü gösterir; genel skill klasörlerinde yeni girdi olmadığı kontrol edilir (genel-bekci.py varsa); kart sürümü onaylı sürüme çekilir, KAYNAK.md ve tedarik_dogrulama.ozet güncellenir, python3 araclar/program-denetim.py --sema --siki 0 hata, commit"
8. "skill güncellemesi ayrı onay ister; `hyperframes skills update` ancak genel klasörlerin son durumu bilinerek ve onayla çalıştırılır"
9. "yedek klasörü saklanır; silmek için kullanıcıya hatırlatılır ve sorulur"

openmontage: existing 7 steps kept in order, with these insertions: after step 1 → "python3 araclar/program-denetim.py --oncesi openmontage çalıştırılır; 'KIRICI ADAYI' ya da 'kayıtsız yerel değişiklik' çıkarsa durulur: önce rehber/11 → 'Kırıcı sürüm' deneme adımları ayrı klasörde uygulanır, kayıtsız değişiklik yerel_yamalar.bilinen'e kullanıcıyla birlikte yazılır"; step 3 (yedek) becomes "yedek: ~/Documents/Claude/yedek/openmontage-<YYYY-AA-GG>/ altına yerel-yamalar.patch (git diff --binary), izlenmeyen-yollar.txt (+ 'kopya' olan izlenmeyen yollar), pip-freeze.txt (`python3 araclar/program-denetim.py --pin-listesi openmontage` çıktısı), bag-listesi.txt (~/.claude/skills içindeki openmontage bağları, readlink) ve KAYIT.json; ~/.config/openmontage anahtar klasörüne dokunulmaz"; then "ön kontrol HAZIR demeden devam edilmez"; the `git pull` step becomes "`git pull --ff-only` (merge/rebase yok; çakışma halinde yerel_yamalar.uygulama 2-3. adımlar)". The last step adds "`python3 araclar/program-denetim.py --sema --siki` 0 hata" and "yedek klasörü saklanır; silmek için kullanıcıya hatırlatılır ve sorulur".

etsyotomasyon: existing 4 steps + "ön kontrol: python3 araclar/program-denetim.py --oncesi etsyotomasyon" inserted as step 2 and "yedek: KAYIT.json (önceki sürüm); ~/.etsyotomasyon kopyalanmaz" as step 3.

`asla` additions: hyperframes + "ortam anahtarı olmadan kurulum/güncelleme yapılmaz; kullanıcı istemeden anahtar tanımlanmaz"; openmontage + "kayıtsız yerel değişiklik varken güncellenmez; git reset --hard / git clean / git stash -u onaysız çalıştırılmaz"; etsyotomasyon + "imzasız ikili, sha256 kayda geçmeden kurulmaz".

Card size budget (review): total growth of `programlar.json` is checked with `wc -l` at implementation (today 142 lines); target under about 330 lines, long prose goes to `rehber/11`. Remove nothing. The prose fields `yerel_degisiklik` (:122), `skill_yazimi`, `kendini_guncelleme`, `repo_notu`, `anahtarlar` stay.

### 3.2 `araclar/program-denetim.py` (edit; owner P6). Old behaviour → new

Python compatibility: write for Python 3.9+ (no `match`, no `X | Y` annotations). Stdlib only. Keep the module importable by `importlib` (hyphenated name) — `araclar/test.py:1514-1517` does exactly that.

#### 3.2.1 CLI (final)
```
python3 araclar/program-denetim.py                         # as today (report to notlar/program-denetimi.md), exit 0
python3 araclar/program-denetim.py --ozet-json [--siki]    # same run, stdout = one JSON object
python3 araclar/program-denetim.py --sema [--ozet-json] [--siki]
python3 araclar/program-denetim.py --oncesi AD [--hedef SÜRÜM_YA_DA_SHA] [--cevrimdisi] [--ozet-json] [--siki]
python3 araclar/program-denetim.py --iskelet {kaynak|npm-global|git-checkout}
python3 araclar/program-denetim.py --pin-listesi AD
ortak:  --kart PATH  --cikti PATH  --ev DIZIN  --yedek-koku DIZIN  --kok DIZIN
```
`--sema`, `--oncesi`, `--iskelet`, `--pin-listesi` are mutually exclusive (argparse group). `--ev` (default `Path.home()`) replaces `~` in every card path and in env/rc-file lookups; `--yedek-koku` (default `<ev>/Documents/Claude/yedek`; overrides `yedek.kok`); `--kok` (default `KOK`) is the library root used for `kaynak_kopyasi`, `KAYNAK.md`, `kaynaklar.json`, `projeler.json` lookups (tests pass a temp tree). `--cevrimdisi`: no network at all (checks that need it print `atlandı: çevrimdışı`). In normal mode the old networked behaviour stays as is.

Exit codes: `0` ran correctly (whatever was found); `1` only with `--siki` and overall result `sorun` (for `--oncesi`: not ready); `2` usage error (unknown program name for `--oncesi`/`--pin-listesi`, argparse errors). An unreadable/invalid `programlar.json` is a finding, not a crash: prints `HATA: programlar.json okunamadı (<kısa neden>)`, result `sorun`, exit 0 (1 with `--siki`).

**`--ozet-json` writes NOTHING (decision, review):** unlike the plain run, it does not write `notlar/program-denetimi.md` (stdout only; the report file is refreshed only by the plain no-flag run, e.g. the one in `arsiv-guncelle.py:205-206`). P4's contract: 'diske yazmaz' holds for this tool. Test 26b asserts no file appears/changes.

`--ozet-json` rule (D4): the whole run executes with `contextlib.redirect_stdout(sys.stderr)` so existing `print` calls (UYARI lines, per-program lines) go to stderr, then exactly one `print(json.dumps(obj, ensure_ascii=False))` goes to real stdout:
```
{"arac": "program-denetim", "durum": "dikkat", "satirlar": ["hyperframes: YENİ SÜRÜM VAR (kurulu 0.9.23, son 0.9.33)", "openmontage: YENİ SÜRÜM VAR (244 geride) · kırıcı adayı", "kart şeması: 0 hata"], "karar_bekleyen": ["hyperframes 0.9.23 -> 0.9.33 güncellemesi: kullanıcı onayı bekliyor", "openmontage 244 commit güncellemesi: kullanıcı onayı bekliyor"]}
```
(`arac` is `"program-denetim"` or `"program-denetim --oncesi <ad>"` or `"program-denetim --sema"`.) `durum` mapping, normal mode: `sorun` if any of: `--sema` HATA; a yerinde card `KART ESKİ`; pin farkı; required env switch missing everywhere; repo `KAYIP`; kaynak kopyası `YOK`; unreadable card file. `dikkat` if any of: `YENİ SÜRÜM VAR`; `kırıcı adayı` (computed without extra network only when `son`/`geride` known: npm `surum_hatti` rule and git `geride > esik_commit`); `öğrenilemedi`; repo `TAŞINMIŞ`; kart eski repo adını taşıyor; required env switch present in some but not all places; `--sema` UYARI. else `temiz`. `karar_bekleyen` lists one string per `YENİ SÜRÜM VAR`/`KART ESKİ` program (the user must decide).

#### 3.2.2 New functions (names fixed so tests can import them)

Classification of network outcomes (closes B7 "404 vs network"):
- `_SON_HATA = {}` module-level dict. `npm_son_surum` (:65-72) keeps signature/return (str or None) and now records, as a side effect, `_SON_HATA[("npm", paket)] = "404" | "ag"` (HTTPError code 404 → "404"; everything else → "ag"); on success it removes the key. `git_son` (:114-129) likewise records `_SON_HATA[("git", repo)]` = `"404"` when the exception is `GhBulunamadi`, `"kapali"` when `api_kapali(e)`, else `"ag"`. Return values unchanged. (Reason: the existing tests replace `npm_son_surum` with a lambda; a signature change would send them to the real network.)
- `repo_durumu(repo, gh=None)` → one of `("var", None)`, `("taşınmış", yeni_ad)`, `("kayıp", None)`, `("kapalı", None)`, `("ağ", None)`. Calls `gh_api(f"repos/{repo}", deneme=2)`; `full_name` differing case-insensitively from `repo` → `taşınmış` (GitHub redirects renamed repos, `gh api` follows); `GhBulunamadi` → try each name in the matching `kaynaklar.json` record's `eski_adlar` (record found by `program == ad` or by `repo_guncel`): if one answers 200 → `("taşınmış", full_name)`, else `("kayıp", None)`; `api_kapali` → `kapalı`; other exception → `ağ`. Only called when a first call failed with 404, never in the success path (so tests with no network never reach it).
- Kaynak-kopyalı card (:318-325): on `GhBulunamadi` from `releases/latest`, call `repo_durumu`: repo exists → keep `öğrenilemedi` and print `UYARI: <ad>: repo'da yayımlanmış release yok`; `kayıp` → status `KAYIP (404)` (table cell and print line) ; `taşınmış` → `TAŞINMIŞ -> <yeni ad>`. Other exceptions keep today's behaviour (`öğrenilemedi`).
- Yerinde git card: when `git_son` returns `(None, None)` and `_SON_HATA` says `404`, `yerinde_denetle` adds `r["repo_durum"]` from `repo_durumu`; report line gets ` · repo: KAYIP`/`TAŞINMIŞ`. Adds new keys to `r` only (existing consumers read named keys).
- `kart_eski_ad(p)` → new name if `p["repo"].lower()` is a key of `repo_takma_adlari()` else None.
- `origin_durumu(yol, p)` → reads `git remote get-url origin` through `git_okuma`; returns `"güncel"`, `"eski-ad"` (matches an `eski_adlar` entry; existing behaviour of `repo_notu`: GitHub redirects, changing it needs approval) or `"farklı"`.
- `npm_integrity(paket, surum, zaman_asimi=8)` → `dist.integrity` string from `https://registry.npmjs.org/<paket>/<surum>` or None (records `_SON_HATA`).
- `git_karsilastir(repo, kurulu, dal)` → `(ahead_by, [dosya yolları], kesik_mi)` from `gh_api(f"repos/{repo}/compare/{kurulu}...{dal}", deneme=2)["files"]`; `kesik_mi` true when `len(files) >= 300` (GitHub caps the list) → treated as "liste eksik olabilir".

Schema:
- `ARAC_ANAHTARLARI = ("claude-code","codex","antigravity","cursor","vscode-copilot")`, `ARAC_ISTEGE_BAGLI = ("gemini-cli","copilot-cli")`, `GIRIS_DURUMLARI = ("yerinde","program-klasoru","proje-skili","karar-bekliyor","yok")`, `YASAK_ADLAR = (".env","token.json","credentials.json","auth.json")`, `YER_TUTUCU = "<DOLDUR>"`.
- `sema_denetle(kart, kok=KOK, kaynaklar=None, ev=None)` → list of `(seviye, kart_adı, alan_yolu, mesaj)` with `seviye` ∈ `HATA|UYARI`. Rules (all in §3.1 table plus): key == `ad`; any string containing `<DOLDUR>` → HATA `doldurulmamış`; secret-shaped strings (`sk-`+20 chars, `ghp_`+20, `AKIA`+16 caps, `-----BEGIN`) → HATA `gizli değer gibi bir metin (değer yazdırılmıyor)`; text contains a project name from `projeler.json` (`notlar` keys and basenames of `ek_projeler`; words ≥ 4 chars, exact case) → UYARI `kütüphane kuralı 6: kartta proje adı olmamalı`; `KAYNAK.md` missing or not containing the registered `kutuphane_surumu`/`kutuphane_commit` text → HATA (`KAYNAK.md kartla uyuşmuyor`); `kaynaklar.json` has no record with `program == ad` for that repo (via `repo_guncel`) → HATA; `guncelleme_adimlari` without a step containing `program-denetim.py --oncesi` → HATA; `giris_yolu` rules (§3.1.1); `kirici_surum.surum_hatti` ∈ {major, minor} (npm/K) / `esik_commit` int (git); `yedek.zorunlu` contains `KAYIT.json`; `yerel_yamalar.bilinen[*].tur` ∈ {izlenen, izlenmeyen, venv}, `yedek` ∈ {kopya, liste}; `disariya_yazar[*].tur` enum; `tedarik_dogrulama.ozet.tur` ∈ {sha256, npm-integrity, git-commit, yok}; `ozet.deger` for `git-commit` must be 40 hex and equal to `kutuphane_commit` when both exist; `sema` top-level key equals 2 (UYARI if missing).
  Message format printed by `--sema`: `HATA: hyperframes: giris_yolu.hepsi.durum: geçersiz değer 'x'; beklenen: yerinde, program-klasoru, proje-skili, karar-bekliyor, yok`. Totals line: `Kart şeması: 3 kart, 0 hata, 1 uyarı`.
- `iskelet(tur)` → dict: a complete card for `tur` ∈ `kaynak|npm-global|git-checkout` with every required field present, strings `"<DOLDUR>"`, lists/objects with one `"<DOLDUR>"` element, `ad` `"<DOLDUR>"`. Printed as indented JSON (`ensure_ascii=False`). `--sema` on it reports only `doldurulmamış` errors (a test asserts this), so adding a new program = print skeleton → fill → `--sema` clean.

Pre-update check (`--oncesi`):
- `oncesi_denetle(ad, p, ctx)` → `(satirlar, sonuc)` where each satır is `(seviye, kontrol, metin)`, `seviye` ∈ `TAMAM|BİLGİ|UYARI|HATA|ATLANDI`, and `sonuc` ∈ `HAZIR | HAZIR DEĞİL | GÜNCELLENECEK BİR ŞEY YOK | KURULU DEĞİL`. `ctx` = small object `{ev, kok, yedek_koku, cevrimdisi, bugun, environ, hedef}` so tests inject everything.
- State lines (preamble; they are NOT counted among the 8 checks, they decide the result word): `şema`, `kurulu`, `kart`, `son` (items S1-S4 below).
  S1. `şema`: `sema_denetle` for this card only; only a HATA in a CORE field (or an unreadable card) → `HATA`; findings about optional fields collapse into one line `UYARI  şema  isteğe bağlı alanlarda <n> uyarı (program-denetim.py --sema)`.
  S2. `kurulu`: installed value via `npm_kurulu_surum`/`git_kurulu`; none → result `KURULU DEĞİL` (BİLGİ, stop; nothing to update; the pointer to `kurulum` is printed).
  S3. `kart`: `yerinde_durum(...)`; `KART ESKİ` → HATA `kurulu <x> karttan farklı: sebebi bulunmadan güncelleme yapılmaz`.
  S4. `son`: network (skipped with `--cevrimdisi`): `öğrenilemedi` → HATA `son sürüm bilinmiyor (<404|ağ|kapalı>)`; `güncel` and no `--hedef` → result `GÜNCELLENECEK BİR ŞEY YOK`; with `--hedef` equal to installed → same.
- The 8 main checks, in this order (each pure function takes data, returns satır list; names fixed). Review change: cut from 15 to 8; the dropped ones moved as noted:
  1. `yedek`: `yedek_kontrol(ad, p, ctx, kurulu)`: newest folder `<yedek_koku>/<ad>-YYYY-AA-GG[-N]`; missing → HATA `yedek yok: <klasör kalıbı>`; folder date older than `tazelik_gun` → HATA `yedek eski (<n> gün)`; `KAYIT.json` missing/invalid → HATA; `KAYIT.json.tarih` ≠ folder date → HATA; `KAYIT.json.onceki` (`surum` for npm, `commit` for git, compared with `ham_surum`/`sha_esit`) ≠ installed → HATA `yedek başka sürümün (kurulu değil)`; each `yedek.zorunlu` entry missing (file must exist, size may be 0; folder must be non-empty) → HATA `yedekte yok: <ad>`; any file/dir name in `YASAK_ADLAR + yedek.yasak_adlar` under the folder (os.walk, cap 50 000 entries) → HATA `yedekte gizli dosya var: <göreli yol>` (path only). All HATA → `HAZIR DEĞİL`.
  2. `sabit sürümler` (cards with `venv`): `dist_info_oku` + `pin_karsilastir`; `<n>/<m>` and each fark; any fark → HATA `sabit sürüm farkı: düzeltmeden devam edilmez` (existing OM rule, openmontage step 5); `venv` absent on a git card with `sabit_surumler` → HATA `venv yok`.
  3. `ortam`: `ortam_kontrol(p, ctx)` per `ortam_anahtarlari`: for each entry count places defined (`nerede` files + settings.json) and process env; line `HYPERFRAMES_SKIP_SKILLS: 3/3 yerde tanımlı` / `2/3 yerde tanımlı (eksik: ~/.zshenv)` / `hiçbir yerde tanımlı değil`; when `beklenen` is set and a found value differs → `değer beklenenden farklı` (the value itself is never printed). `gerekli` & 0 places & not in `environ` → HATA; `gerekli` & partial → UYARI; not `gerekli` & 0 → BİLGİ `tanımlı değil (isteğe bağlı)`. An unreadable file → `UYARI: <yol>: okunamadı`.
  4. `yama` (git cards): `yama_kontrol(p, porcelain_metin)` using `git status --porcelain` via `git_okuma`: path extraction handles `R  a -> b` (take the new path), double-quoted paths, `??` entries; a path matches a `bilinen` entry exactly or by trailing-`/` prefix. Unrecorded change → `HATA: kayıtsız yerel değişiklik: <yol>` (one line per path, max 20 then `… ve N tane daha`); `bilinen` path with `tur` izlenen/izlenmeyen that is not changed → `BİLGİ: kayıtlı ama değişmemiş: <yol> (yama upstream'e girmiş ya da kaybolmuş olabilir)`; status unreadable → HATA; also `degisen`/`izlenmeyen` counts line. HEAD not on card `dal` (detached) → UYARI.
  5. `repo`: `repo_durumu` (+ `kart_eski_ad`, `origin_durumu`): `kayıp` HATA; `taşınmış` UYARI `kart repo adı eski: yeni ad <x> (kaynaklar.json eski_adlar'a bakın)`; origin `eski-ad` BİLGİ (existing note, change needs approval).
  6. `giriş yolu`: §3.1.1 path checks; `karar-bekliyor` → `BİLGİ: <arac>: kullanıcı kararı bekliyor`.
  7. `gizli`: `gizli_dosyalar` (optional; absent → `BİLGİ: kayıtsız`) → `BİLGİ: anahtar/kimlik dosyası var (açılmaz)` / `UYARI: yok: <yol>`.
  8. `kırıcı`: `kirici_adayi(p, kurulu, hedef, geride, dosyalar)` → list of reasons; non-empty → `UYARI: KIRICI ADAYI: <neden>; önce rehber/11 → 'Kırıcı sürüm' deneme adımları ayrı klasörde (<deneme_klasoru>) uygulanır`; `deneme_disk_gb` vs `shutil.disk_usage(ev)` free → `UYARI` if lower. `--hedef` may be a version (npm) or sha (git, ≥7 hex); default target = latest. Includes the old `çakışma` check (git, online): `git_karsilastir`: files ∩ (`yerel_yamalar.bilinen` izlenen) → `UYARI: yeni commit'ler yamalı dosyaya da dokunuyor: <yol>`; `kesik_mi` → `UYARI: dosya listesi 300'de kesildi; çakışma tam bilinmiyor`. Optional `kirici_surum` absent → `BİLGİ: kayıtsız, kırıcı adayı denetlenmedi`.
- Dropped from `--oncesi` (review): `dışarıya yazar` (existence list; `--sema` validates its shape, `rehber/11` and `genel-bekci` use it, no per-update value); `tedarik` → only with the extra flag `--tedarik`: `ozet.tur == npm-integrity` and `deger` set and online → compare with `npm_integrity(paket, kurulacak/kurulu sürüm)`: equal TAMAM, different HATA `registry integrity kayıttan farklı`, unreachable UYARI; `deger` empty → `BİLGİ: integrity kayıtsız`; `ucuncu_taraf` and `imza == yok` → `UYARI: üçüncü taraf, imzasız: kaynaktan kurulum tercih edilir`. (`ctx.tedarik` False by default; `npm_integrity` helper stays).
- `sonuc`: any HATA → `HAZIR DEĞİL`; else `HAZIR` (UYARI do not block but are printed); `KURULU DEĞİL`/`GÜNCELLENECEK BİR ŞEY YOK` as above. Last printed lines: `SONUÇ: HAZIR` etc., then the fixed footer (§4). `durum` for `--ozet-json`: `HAZIR DEĞİL` → `sorun`, `HAZIR` with any UYARI → `dikkat`, else `temiz`; `karar_bekleyen`: `["<ad> güncellemesi için kullanıcı onayı gerekir"]` when `HAZIR`.
- Writes nothing (no file, no report). It is read-only: only `git_okuma`, file reads, `os.path.lexists`, `shutil.disk_usage`, and (online) `gh_api`/`urllib` GETs. It never runs npm, pip, the venv python, the program, or `git fetch`.

`--pin-listesi AD`: prints `paket==sürüm` lines (sorted) for the card's venv via `dist_info_oku` (all installed packages, not only pinned ones); exit 2 if the card has no `venv`; nothing written. Used by the backup step (`> pip-freeze.txt` redirect is done by the agent into the backup folder).

Normal report (`main`, :293-342): all existing output lines and the existing two tables are kept byte-identical for unchanged data. Added after them: `## Kart şeması` (`tüm kartlar geçerli` or the HATA/UYARI lines), `## Ortam anahtarları` (one line per yerinde card per key: `hyperframes · HYPERFRAMES_SKIP_SKILLS · 3/3`), `## Dikkat` (kırıcı adayı, repo KAYIP/TAŞINMIŞ lines, only when present). These blocks use `--ev` for lookups. The date-stripped comparison (:339-341) is unchanged. `programlar.json` cards that fail the new schema do **not** change the exit code (D4) and do not stop the report.

`main` structure change: wrap the existing body as `rapor(a)` returning `(out_satirlari, bulgular)`; `main` parses args, dispatches to the mode, handles `--ozet-json`/`--siki`. The existing early `UYARI` prints stay.

Docstring :1-14 updated: lists the new modes, repeats "hiçbir şey kurmaz/indirmez/güncellemez, program komutlarını çalıştırmaz, anahtar/oturum dosyalarını açmaz (yalnız var/yok bakar)", and the new exit code rule (`--siki`).

### 3.3 `rehber/11-program-yonetimi.md` (edit; owner P6)

Keep sections "Nerede ne var", "Yeni program eklemek", "Yerinde program (kopyasız)" (with small fixes below). Old → new:

- :12 `KAYNAK.md` description adds: "ve kartla tutarlı sürüm/commit metni (`program-denetim.py --sema` denetler)".
- :34-41 "Kart ne taşır" gets a pointer: "Şema v2 alanları aşağıdaki 'Kart şeması' tablosundadır."
- :57-62 yedek paragraph: keep; add "Yedek klasöründe `KAYIT.json` bulunur (aşağıda 'Yedek kaydı')". Replace :62 last sentence "Ortam değişkenini kullanıcı kendisi tanımlar; agent tanımlamaz, yalnız hangisinin gerektiğini söyler." with: "Ortam değişkenini ajan kendiliğinden tanımlamaz: gerekeni söyler; kullanıcı ya kendisi tanımlar ya da ajana açıkça 'tanımla' der (kabuk dosyalarının yedeği önce alınır)."
- :69-70 yerinde update flow: replace with "Güncelleme adımları: bu belgede 'Taze ajan: istek → adımlar'."
- :74-76 (kural 1 istisnası): keep text; append "Giriş yolları ve boşaltma: genel klasör işlemleri `rehber/12`'dedir."

New sections (append in this order; Turkish, plain words; each with exact commands):
1. `## Kart şeması (v2)`: the §3.1 table in Turkish (field, shape, kimde zorunlu), `python3 araclar/program-denetim.py --sema` and `--iskelet <tür>`.
2. `## Boşaltma sonrası program erişimi (giriş yolları)`: why programs are no longer reached through machine-wide skill folders; `giris_yolu` meaning; the 5 `durum` words; per-tool table for HyperFrames/OpenMontage/etsyotomasyon (copy of §3.1.1 values); open decision pointer (OM Claude entry); "boşaltmadan sonra `--oncesi <ad>` giriş yolu satırlarını yeniden denetler; yol değişirse kart güncellenir (kullanıcı onayıyla)".
3. `## Yeni makineye kurulum`: card `kurulum` fields; order: env switches first → install → `--oncesi`/denetim; "kütüphane oturumu kurar, kullanıcı onayıyla; anahtar/hesap adımlarını kullanıcı yapar".
4. `## Yedek kaydı (KAYIT.json)`: folder `~/Documents/Claude/yedek/<program>-<YYYY-AA-GG>[-N]/`; format:
```
{"program": "openmontage", "tarih": "2026-11-12",
 "onceki": {"surum": "", "commit": "c8066452325cb57c8fc1ba8c2a71b6e8842e6b65"},
 "hedef": "<yeni sürüm ya da sha, bilinmiyorsa boş>", "icerik": ["yerel-yamalar.patch", "izlenmeyen-yollar.txt", "pip-freeze.txt", "bag-listesi.txt"], "not": ""}
```
(`onceki.surum` for npm cards, `onceki.commit` for git cards, the other empty.) Written by the agent with one `python3 -c`/heredoc command; the ready-made command per program is in the section; zero secrets; forbidden names list.
5. `## Güncellemeden önce: ön kontrol (--oncesi)`: what each line means (the 8 main checks plus 4 state lines in plain words), result words, `--hedef`, `--cevrimdisi`, exit codes; "HAZIR demeden güncelleme başlamaz".
6. `## Kırıcı sürüm (önce ayrı klasörde dene)`: rule per card (`kirici_surum`), the trial folder `~/Documents/Claude/deneme/<program>-<hedef>`, never touches `/usr/local`, `~/.openmontage`, library or git; trial passes → then the normal approval/update; trial folder deletion asks the user.
7. `## Yerel yamalar (git klonu)`: manifest in the card (`yerel_yamalar.bilinen`), unrecorded change = stop; backup of patch; `git pull --ff-only`; conflict path steps (copy of §3.1.2 `uygulama`); "yeni yama eklemek: kullanıcıyla amacı yazılır, karta eklenir".
8. `## Geri alma`: when, how (copy of the three `geri_alma` blocks in plain words), what needs approval, where the previous version is (`KAYIT.json.onceki`), "yedeksiz güncelleme yapılmadığı için geri alma her zaman mümkündür".
9. `## Programı çıkarma`: two separate things, each needs its own approval: (A) from the library: steps in order — (1) `python3 araclar/proje-kullanimi.py --program <ad>` (P5 query; fallback `--skill <kimlik>` for each id in card `skilleri`): who uses it; tell the user; (2) approval; (3) remove card from `programlar.json`; (4) delete `programlar/<ad>/` (the `kaynak/` copy is a permanent deletion: git history keeps it; name what will be deleted and ask); (5) remove `"program": "<ad>"` from the `kaynaklar.json` record (if the record exists only for the program: remove the record through the source-removal procedure of `rehber/03`/`kaynak-cikar.py` instead) and the `notlar/referans/kutuphaneler.md` row; (6) un-star/remove from the GitHub list is the user's own action; (7) `kapsam-denetimi.py` 0 sorun, `dogrula.py` 0 hata, `program-denetim.py --sema --siki`, commit (the commit is the rollback: `git revert`). (B) from the machine: card `cikarma.makineden` steps, backup first, keys/data never touched, global-folder parts belong to `rehber/12`.
10. `## Taze ajan: istek → adımlar`: four requests with exact numbered steps (the library session has no memory; it reads `CLAUDE.md`/`AGENTS.md`, `BASLA.md` if present, this file and the card):
   - "HyperFrames'i güncelle" (npm-global) — 12 steps (see §4.2 text).
   - "OpenMontage'i güncelle" (git-checkout) — 14 steps (§4.3).
   - "Yeni program ekle" — `--iskelet`, fill, `--sema`, register steps (the existing 4 steps of :18-28 plus skeleton/sema/KAYIT/`--oncesi` dry check), commit.
   - "Programı kaldır" / "geri al" — pointers to the sections above.
11. `## Aylık takip`: `program-denetim.py --ozet-json` is run by the monthly summary; `YENİ SÜRÜM VAR`/`KART ESKİ`/`kırıcı adayı` become a question to the user, never an automatic update.

### 3.4 `programlar/*/KAYNAK.md` (edit; owner P6)
Each file gets these extra rows in its table (all values derivable from the card; no new facts): `Yedek klasörü` (`~/Documents/Claude/yedek/<ad>-<YYYY-AA-GG>/`), `Giriş yolu` (pointer to card `giris_yolu`), `Doğrulama` (hyperframes: npm integrity `<card deger or "kayıtsız">`; openmontage: commit sha; etsyotomasyon: commit sha + "ikili imzasız"), and openmontage additionally `Yerel yama kaydı` → `programlar.json → openmontage → yerel_yamalar.bilinen`. The registered version/commit text already present in each file stays exactly (the new consistency check relies on it). hyperframes/openmontage KAYNAK.md: the sentence "Yeniden edinmek için…" gets "(ayrıntı: kart `kurulum`)".

### 3.5 `promptlar/13-program-kur-guncelle.md` (new; owner P6)
Same layout as `promptlar/12-proje-kullanimi-ve-etki.md` (title `# 13 — Program Kur, Güncelle, Geri Al, Kaldır`, `**Ne zaman:**`, `**Nerede:**`, one ```` ```kopya ```` block). Full text in §4.4. Header number 13 is fixed by D11; `promptlar/README.md` row is a P8 hand-off (§6).

### 3.6 `araclar/testler/test_p6-programlar.py` (new; owner P6)
See §5. Skeleton: `#!/usr/bin/env python3`, `sys.path.insert(0, parent.parent)`, load `program-denetim.py` through `importlib.util.spec_from_file_location("progden", KOK/"araclar"/"program-denetim.py")`, helper `test(ad, kosul, detay="")` that counts and prints `OK`/`HATA: <ad> <detay>`, `tempfile.TemporaryDirectory()` for every filesystem fixture, final `print(f"{gecen}/{toplam} test geçti")`, `sys.exit(0 if gecen == toplam else 1)`. Never touches `Path.home()`: every call passes `--ev`/`ctx.ev`/`--yedek-koku`/`--kok` pointing into the temp dir; network functions are replaced by fakes on the module (`progden.gh_api`, `progden.npm_son_surum`, `progden.urllib.request.urlopen`, `progden.git_okuma`, `progden.shutil.disk_usage`).

---------------------------------------------------------------------------------------------------

## 4. User-facing texts

### 4.1 `--oncesi` output (exact format; one line per check, `SEVİYE  kontrol  metin`)
```
Program ön kontrolü: hyperframes (npm-global) · karttaki 0.9.23 · kurulu 0.9.23 · son 0.9.33
TAMAM   şema            çekirdek alanlar geçerli
TAMAM   kart            kurulu sürüm karttakiyle aynı
BİLGİ   son             0.9.23 -> 0.9.33 (YENİ SÜRÜM VAR)
HATA    yedek           yedek yok: ~/Documents/Claude/yedek/hyperframes-<YYYY-AA-GG>/
ATLANDI sabit sürümler  kartta venv yok
TAMAM   ortam           HYPERFRAMES_SKIP_SKILLS: 3/3 yerde tanımlı
BİLGİ   ortam           HYPERFRAMES_NO_AUTO_INSTALL: tanımlı değil (isteğe bağlı)
ATLANDI yerel değişiklik npm kartı: git klonu değil
TAMAM   repo            heygen-com/hyperframes erişilebilir
BİLGİ   giriş yolu      hepsi: proje-skili (/usr/local/bin/hyperframes var)
BİLGİ   gizli           anahtar/kimlik dosyası var (açılmaz): ~/.hyperframes/config.json
BİLGİ   kırıcı          kırıcı adayı değil (patch sürüm: 0.9.23 -> 0.9.33)
SONUÇ: HAZIR DEĞİL (1 engel)
Bu araç yalnız okur. Güncelleme için kullanıcıdan bu güncellemeye özel AYRI onay alınır; 'HAZIR' demeden güncelleme başlamaz.
```
Result lines: `SONUÇ: HAZIR`, `SONUÇ: HAZIR DEĞİL (<n> engel)`, `SONUÇ: GÜNCELLENECEK BİR ŞEY YOK (kurulu sürüm son sürüm)`, `SONUÇ: KURULU DEĞİL (bu bilgisayarda yok; kurulum için kartın 'kurulum' alanına bakın)`. Other fixed strings: `KIRICI ADAYI: <neden>`, `kayıtsız yerel değişiklik: <yol>`, `yedekte gizli dosya var: <göreli yol>`, `yedek başka sürümün (kurulu değil)`, `yedek eski (<n> gün; en çok <tazelik_gun>)`, `atlandı: çevrimdışı`.

### 4.2 Fresh agent: "HyperFrames'i güncelle" (goes into `rehber/11` and prompt 13; exact steps)
0. `cd ~/Documents/SkillKutuphanesi`; read `CLAUDE.md`/`AGENTS.md` and this section; `git status` (a dirty tree means: report to the user, do not mix the card change with other work).
1. `python3 araclar/program-denetim.py --sema --siki` → 0 hata, yoksa dur.
2. `python3 araclar/program-denetim.py` → hyperframes satırı. `KART ESKİ` → dur, sebebi bul (program kendini güncellemiş olabilir), kullanıcıya söyle.
3. `python3 araclar/program-denetim.py --oncesi hyperframes` → engelleri oku. `KIRICI ADAYI` varsa kartın `rehber/11 → 'Kırıcı sürüm' deneme adımları`'ni ayrı klasörde uygula, sonucu raporla.
4. Kullanıcıya sun: kurulu → hedef sürüm, release notu özeti, kırıcı adayı mı, yedek yeri. Şu cümleyi sor: "HyperFrames'i <kurulu> sürümünden <hedef> sürümüne güncelleyeyim mi? Önce yedek alırım. Bu onay yalnız bu güncelleme için geçerli."
5. Onaydan sonra yedek klasörünü aç (`~/Documents/Claude/yedek/hyperframes-<bugün>/`), `~/.hyperframes` (config.json hariç) → `hyperframes-veri/`, `/usr/local/lib/node_modules/hyperframes` → `paket/`, `KAYIT.json` yaz.
6. `--oncesi hyperframes` tekrar → `SONUÇ: HAZIR`.
7. `HYPERFRAMES_SKIP_SKILLS=1 npm install -g hyperframes@<hedef>` (izin hatası olursa dur, kullanıcıya sor).
8. `python3 araclar/program-denetim.py` → kurulu = hedef. Genel klasörlerde yeni girdi yok mu (genel-bekci varsa onu çalıştır).
9. Kartı güncelle: `kutuphane_surumu`, `programlar/hyperframes/KAYNAK.md`, `tedarik_dogrulama.ozet` (integrity için `npm_integrity`); `--sema --siki`, `kapsam-denetimi.py`, `dogrula.py`; commit.
10. Kullanıcıya özetle ve hatırlat: "Yedek `~/Documents/Claude/yedek/hyperframes-<tarih>/` klasöründe duruyor; güncellemeyi doğruladığında silmek istersen söyle."

### 4.3 Fresh agent: "OpenMontage'i güncelle" (exact steps)
0-2 as above with `openmontage`. 3. `--oncesi openmontage`: engeller şunlar olabilir: yedek, `kayıtsız yerel değişiklik` (kullanıcıyla `yerel_yamalar.bilinen`'e yaz), sabit sürüm farkı, `KIRICI ADAYI` (bugün 244 commit geride: deneme klasörü şart). 4. Kırıcı adayıysa `rehber/11 → 'Kırıcı sürüm' deneme adımları`; gecme_olcutu geçmeden devam yok. 5. Kullanıcıya sun: kurulu → hedef commit (tam sha), kaç geride, `requirements.txt` farkı (`git -C ~/.openmontage diff <kurulu>..<hedef> -- requirements.txt` yalnız fetch sonrası; fetch için ayrı onay istenir ya da GitHub compare çıktısı gösterilir), yamalı dosyalarla çakışma listesi. Sor: "OpenMontage'i <kurulu 8 hane> -> <hedef 8 hane> güncelleyeyim mi? Önce yerel yamaları ve sabit paket listesini yedeklerim; paket sürümlerini yükseltmem. Bu onay yalnız bu güncelleme için geçerli." 6. Yedek: `git -C ~/.openmontage diff --binary > .../yerel-yamalar.patch`; `git ls-files --others --exclude-standard` + boyutlar → `izlenmeyen-yollar.txt`; 'kopya' olanları `izlenmeyen/`; `python3 araclar/program-denetim.py --pin-listesi openmontage > .../pip-freeze.txt`; bağ listesi → `bag-listesi.txt`; `KAYIT.json`. 7. `--oncesi openmontage` → HAZIR. 8. `git -C ~/.openmontage fetch origin main` ve `git pull --ff-only` (kullanıcı onayı yukarıdaki cümleyle verildi; `origin` adresi değiştirilmez); çakışma olursa `yerel_yamalar.uygulama` 2-3. 9. Bağımlılıklar: `requirements.txt` farkı varsa kullanıcıya göster; `make setup` olduğu gibi çalıştırılmaz; gereken adımlar tek tek, `HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_AUTO_INSTALL=1 HYPERFRAMES_NO_UPDATE_CHECK=1` tanımlıyken; `pip install -U` yok. 10. `--oncesi`/denetim: sabit sürümler N/N, kurulu = hedef; yamalar yerinde ('kayıtlı ama değişmemiş' yok olmalı); `~/.claude/skills` bağları kırık mı. 11. preflight (openmontage skilindeki komut). 12. Kart: `kutuphane_commit`, KAYNAK.md, `tedarik_dogrulama.ozet.deger`, `yerel_yamalar.bilinen` (kaybolan/yeni yama); `--sema --siki`, testler, commit. 13. Yedek silme hatırlatması.

### 4.4 `promptlar/13-program-kur-guncelle.md` (full text)
```
# 13 — Program Kur, Güncelle, Geri Al, Kaldır

**Ne zaman:** HyperFrames, OpenMontage, etsyotomasyon gibi programları (skill olmayan yapılar) bu bilgisayara kurarken, güncellerken,
eski sürüme döndürürken ya da kütüphaneden/bilgisayardan çıkarırken; ya da yeni bir programı kütüphaneye dahil ederken.
**Nerede:** Claude Code ya da Codex, `~/Documents/SkillKutuphanesi` klasöründe. Ayrıntı: `rehber/11-program-yonetimi.md`.

```kopyala
[PROGRAM ADI: hyperframes / openmontage / etsyotomasyon / yeni] için [KUR / GÜNCELLE / GERİ AL / KALDIR / DAHİL ET] işlemi yap.
~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/11-program-yonetimi.md dosyalarını oku (aklında önceki konuşma yok; her şeyi dosyadan öğren).

1. python3 araclar/program-denetim.py --sema --siki   → kartlar geçerli mi (0 hata değilse dur, bana söyle).
2. python3 araclar/program-denetim.py                 → durum (KART ESKİ ise dur, sebebini bul).
3. GÜNCELLE için: python3 araclar/program-denetim.py --oncesi [PROGRAM]   → engelleri ve 'KIRICI ADAYI' satırını oku.
   KIRICI ADAYI ise kartın rehber/11 → 'Kırıcı sürüm' deneme adımları'ni AYRI klasörde uygula, sonucu raporla.
4. Bana sun: sürüm farkı, değişiklik özeti, kırıcı adayı mı, yedeğin yeri. Bu işlem için AYRI onayımı sor (önceki onay geçerli değil).
5. Onayımdan sonra rehber/11 → "Taze ajan: istek → adımlar" altındaki o programın adımlarını sırayla yürüt; önce yedek (KAYIT.json dahil),
   sonra --oncesi 'HAZIR' demeden değişiklik yapma.
6. GERİ AL için kartın geri_alma adımları; KALDIR için rehber/11 → "Programı çıkarma" (kütüphaneden ve bilgisayardan ayrı ayrı onay).
7. DAHİL ET için: python3 araclar/program-denetim.py --iskelet [kaynak|npm-global|git-checkout] > geçici dosya, doldur, --sema temiz olsun,
   sonra rehber/11 → "Yeni program eklemek".
8. Bitince: program-denetim.py yeniden, --sema --siki, kapsam-denetimi.py, dogrula.py; commit. Yedek klasörünü silme, silmek için bana hatırlat ve sor.

Kurallar: anahtar/.env/oturum dosyalarını açma. pip install -U, make setup (onaysız), npx, hyperframes init/skills/update çalıştırma.
Ortam değişkeni (HYPERFRAMES_SKIP_SKILLS vb.) ben istemeden tanımlama. Genel skill klasörlerine ve kabuk dosyalarına dokunma
(yalnız onayla ve rehber/11'deki adımla). Push yapma; kartlara proje adı yazma.
```
```

### 4.5 `--sema` / `--iskelet` / errors
`Kart şeması: 3 kart, 0 hata, 0 uyarı` · `HATA: <kart>: <alan>: <sorun>` · `UYARI: <kart>: <alan>: <sorun>` · `HATA: programlar.json okunamadı (<neden>)` · usage: `HATA: program yok: <ad>; kartlar: etsyotomasyon, hyperframes, openmontage` (exit 2).

---------------------------------------------------------------------------------------------------

## 5. Tests (`araclar/testler/test_p6-programlar.py`; temp dirs, fake data; last line `N/N test geçti`)

Fixtures: `gecerli_kart(tur, kok)` builds a valid card of each tur from `iskelet(tur)` by replacing every `<DOLDUR>` with real values, creates under `kok` the `KAYNAK.md` (with version/commit text), `kaynaklar.json` (record with `program`), and for `kaynak` a non-empty `kaynak/`. `ev` temp home with fake `.zshenv`, `.zshrc`, `.claude/settings.json`.

Schema (S):
1. `iskelet` for each of 3 turs is valid JSON and `sema_denetle` returns only `doldurulmamış`-type errors (no other kind).
2. `gecerli_kart` for each tur → 0 HATA.
3. Remove each CORE top-level field one by one (loop over the §3.1 CORE rows) → exactly one HATA naming that field path. Remove each OPTIONAL field one by one → zero findings. Put an invalid value into each present optional field → UYARI only, never HATA.
3b. Library-gate contract: `--sema --ozet-json` on a card with an optional-field error → `durum` `dikkat`, satırlar start with `UYARI:`; core error → `sorun`, `HATA:`; unreadable JSON → one satır starting `HATA: programlar.json okunamadı`.
4. Enum errors: bad `ucret`, bad `giris_yolu` durum, unknown arac key, missing one of five tool keys without `hepsi`, bad `disariya_yazar.tur`, bad `yerel_yamalar.bilinen.tur`, bad `kirici_surum.surum_hatti`.
5. `venv` without `sabit_surumler` (and reverse) → HATA; `sabit_surumler` as a list → HATA (matches existing bozuk-kart tests).
6. Secret-shaped string → HATA and the message does not contain the string; project name from `projeler.json` → UYARI; `KAYNAK.md` without the commit text → HATA; no `kaynaklar.json` record → HATA; `guncelleme_adimlari` without `--oncesi` → HATA.
7. `--sema --siki` exit 1 on a bad card file, 0 on valid; without `--siki` always 0; `--sema --ozet-json` stdout is one JSON object.

Network classification (N):
8. `npm_son_surum` with fake `urlopen` raising `HTTPError(404)` → None and `_SON_HATA[("npm", p)] == "404"`; raising `URLError`/timeout → `"ag"`; success clears the key; signature unchanged (positional + `zaman_asimi`).
9. `git_son` with fake `gh_api`: `GhBulunamadi` → `(None, None)` and `"404"`; `RuntimeError("gh api kapalı")` → `"kapali"`; other → `"ag"`; success path return values identical to before.
10. `repo_durumu`: `full_name` differs → `taşınmış`; 404 + `eski_adlar` answers → `taşınmış`; 404 everywhere → `kayıp`; kapalı; ağ.
11. Kaynak-kopyalı card in `main` with fake `gh_api`: releases 404 + repo exists → `UYARI … release yok`, status `öğrenilemedi`; repo 404 → `KAYIP (404)`; exit 0 both.
12. `kart_eski_ad` returns the new name for a card using an `eski_adlar` entry; `origin_durumu` for fake `git_okuma` returning old/new/other URL.
13. `npm_integrity` equal/different/unreachable → with `--tedarik` TAMAM/HATA/UYARI; without the flag no `tedarik` line and no call.

Pre-update (O):
14. Backup (`--oncesi` check 1): no folder; folder too old (inject `bugun`); `KAYIT.json` missing/invalid/date mismatch/`onceki` mismatch; missing `zorunlu` file; empty required dir; forbidden `config.json`/`.env` inside nested dir → each its own HATA; fully valid → TAMAM; two same-day folders (`-2`) → newest used.
15. Env: 3/3, 2/3 (UYARI), 0/3 with `gerekli` (HATA), 0/3 with process env set (not HATA), value differs (`beklenenden farklı`, value never printed), unreadable/invalid `settings.json` (UYARI), non-required missing (BİLGİ). A fake `.zshrc` line `export OTHER_API_KEY=SECRETVALUE123` → string `SECRETVALUE123` appears in no output line.
16. Patches: all changes recorded → TAMAM; unrecorded path → HATA with the path; dir-prefix entry matches; `R  a -> b`; quoted path with space; recorded-but-unchanged BİLGİ; unreadable status → HATA; truncation line for >20 paths.
17. Breaking rule: npm 0.9.23→0.9.33 not candidate; →0.10.0 candidate (`minor`); →1.0.0 candidate; git geride 244>50 candidate, 10 not; `izle_dosyalar` in file list; patched file in file list; `kesik_mi` UYARI.
18. `giris_yolu`: existing path TAMAM/BİLGİ; missing path for `program-klasoru` → UYARI; `karar-bekliyor` → BİLGİ; `gizli_dosyalar` with a file `chmod 000` containing text → reported `var` and the text never read (proves existence-only).
19. Pins: fake venv dist-info equal → `N/N`; one differs → HATA; `venv` missing → HATA.
20. Disk: fake `shutil.disk_usage` below `deneme_disk_gb` → UYARI (inside the `kırıcı` check).
21. End-to-end npm card in temp (fake `package.json`, `ev`, `yedek-koku`, fake `npm_son_surum`): ready → `SONUÇ: HAZIR`, exit 0; delete the backup → `HAZIR DEĞİL`, exit 0; with `--siki` exit 1; `--ozet-json` (no file written) stdout parses to an object with exactly keys `arac, durum, satirlar, karar_bekleyen` and nothing else printed to stdout; `güncel` → `GÜNCELLENECEK BİR ŞEY YOK`; no package dir → `KURULU DEĞİL`.
22. End-to-end git card with a real `git init` temp repo (`-c user.name=t -c user.email=t@t`), `kutuphane_commit` = HEAD, one modified tracked file listed in `bilinen`, one unlisted → HATA names only the unlisted; HEAD moved → `KART ESKİ` HATA. Skipped (counted as passed with note) when `git` is missing.
23. `--oncesi nope` exit 2 and message lists card names; `--oncesi X --cevrimdisi` makes no call (fake `gh_api`/`urlopen` raise AssertionError).
24. `--pin-listesi`: sorted `ad==sürüm` lines from fake dist-info, exit 2 when no `venv`.

Report / compat (R):
25. Old-shape card (no v2 fields; copies the cards of `araclar/test.py:1615-1636`) through `main`: exit 0, report written, contains `## Kart şeması` with errors, no exception.
26. Normal run `--ozet-json` mapping: `KART ESKİ` → `sorun`; `YENİ SÜRÜM VAR` → `dikkat` and `karar_bekleyen` has the program; all current → `temiz`; existing `UYARI` prints go to stderr (stdout parses as one JSON).
27. Unreadable `--kart` file → `durum: sorun`, exit 0; with `--siki` exit 1.
26b. `--ozet-json` (plain and `--sema`) leaves the `--cikti` path absent when it was absent and unchanged (mtime) when present: writes nothing.
28. Report idempotence: running `main` twice with unchanged fake data does not rewrite `--cikti` (mtime equal), as today (:338-341).
29. `yerinde_durum`, `durum`, `git_kurulu`, `pin_karsilastir` outputs for the cases in `araclar/test.py:1521-1544` unchanged (spot copies of 6 cases) — protects D2.

Total expected ≈ 60-70 `test()` calls (loops count each iteration).

---------------------------------------------------------------------------------------------------

## 6. Hand-off requests to other packages

**To P8 (shared files):**
1. `araclar/test.py`: add one section that runs every `araclar/testler/test_*.py` as a subprocess (`sys.executable`, cwd KOK), requires exit 0 and parses the last line `N/N test geçti`. Keep the existing program block `araclar/test.py:1492-1513` as is (it still holds). Add one check (review: NOT a failing gate on card findings): `subprocess.run([sys.executable, "araclar/program-denetim.py", "--sema", "--ozet-json"], capture_output=True)`; parse stdout JSON; the check passes unless some satır starts with `HATA: programlar.json okunamadı`; any other `HATA:`/`UYARI:` satır is printed as a note (UYARI), never a failure.
2. `araclar/dogrula.py`: same single check, **as UYARI not HATA**: `programlar.json kart şeması: <n> bulgu (python3 araclar/program-denetim.py --sema)`; only an unreadable/invalid-JSON `programlar.json` is `HATA` (P8's own builtin JSON check E1 already covers that; P8 must change its draft 'exit ≠ 0 → HATA' to this rule, so `arsiv-guncelle.py --birlestir` is never blocked by a card field). Also one check: every key under any card's `giris_yolu.araclar` appears in P1's `yapay-zeka-araclari.json` (skip when the file is missing); this one stays UYARI too.
3. `CLAUDE.md` and `AGENTS.md` line 51 (programs): replace the old "sabit sürüm kopyası" wording with this text (needs the user's approval, §7): "Programlar (skill olmayan yapılar: HyperFrames, OpenMontage, etsyotomasyon): `programlar.json` kartları; HyperFrames ve OpenMontage `kopya: yerinde` (bu bilgisayarda kurulu haliyle izlenir). Her güncelleme, geri alma ve kaldırma kullanıcının AYRI onayıyla ve önce yedekle yapılır: `rehber/11-program-yonetimi.md` → 'Taze ajan: istek → adımlar', hazır istem `promptlar/13-program-kur-guncelle.md`. Önce `python3 araclar/program-denetim.py --oncesi <ad>` 'HAZIR' demelidir."
4. `promptlar/README.md`: add the row for `13-program-kur-guncelle.md` (when: program install/update/rollback/remove/add).
5. `ortak.py`: **no change required** (everything used already exists). `duman-testi.py`: nothing.

**To P4 (monthly summary):** call `python3 araclar/program-denetim.py --ozet-json` (no other flag; online) as a subprocess; it prints one JSON object to stdout and exits 0 even when it finds problems. Do not call `--oncesi` monthly. `--ozet-json` writes no file (decision in 3.2.1), so the summary never dirties the tree; the plain run (which writes `notlar/program-denetimi.md`) is only needed when the summary text is wanted as a file. Keep the exact `karar_bekleyen` strings for your 'kabul edildi' matching. `arsiv-guncelle.py:205-206` may keep the plain call (output unchanged in kind) or be replaced by the summary tool's subprocess; either works. The tool writes only `notlar/program-denetimi.md`, and only in the plain no-flag run; `--ozet-json` writes nothing. The `karar_bekleyen` strings are stable and contain the versions (`hyperframes 0.9.23 -> 0.9.33 güncellemesi: kullanıcı onayı bekliyor`), so P4 can match them exactly against its 'kabul edildi' list (a closed decision for that version does not reappear; a newer target version makes a new string).

**To P3 (backups):** register in `yedekler.json` a backup type "program-yedegi": path pattern `~/Documents/Claude/yedek/<program>-<YYYY-AA-GG>[-N]/`, created by program updates, contains `KAYIT.json` (format in `rehber/11` → 'Yedek kaydı'), never contains `.env`/`config.json`/tokens, deletion trigger "güncelleme doğrulanıp kullanıcı onaylayınca; silmeden önce kullanıcıya sorulur". Also register the trial-folder pattern `~/Documents/Claude/deneme/<program>-<hedef>/` (created by breaking-release trials, same deletion rule). `yedek-denetim.py` may read `KAYIT.json.tarih`.

**To P2 (global-folder watchdog and emptying guide):** (a) `genel-bekci.py` may read each card's `disariya_yazar` entries with `tur` ∈ {`skill`, `bag`} as "known writers" for its report text; (b) `rehber/12` emptying procedure: after each emptying step run `python3 araclar/program-denetim.py --oncesi hyperframes` and `--oncesi openmontage` — the `giriş yolu` and `ortam` lines must stay TAMAM/BİLGİ; (c) when the user decides where the OpenMontage entry skill lives after emptying, the card `giris_yolu.araclar.claude-code` (`durum`, `yol`, `nasil`) is updated by P6's owner in the same commit.

**To P1 (tool support):** the tool keys in `yapay-zeka-araclari.json` must be exactly `claude-code`, `codex`, `antigravity`, `cursor`, `vscode-copilot` (and `gemini-cli`, `copilot-cli` for the optional ones). If P1 picks other strings, change the constants `ARAC_ANAHTARLARI`/`ARAC_ISTEGE_BAGLI` in `program-denetim.py` and the card keys together.

**To P5 (project tracking):** program ↔ project mapping is NOT stored in `programlar.json` (rule 6, D8). P6 relies on P5's query: `python3 araclar/proje-kullanimi.py --program <ad>` (projects that use the program, from lock files and `projeler.json → program_kullanimi`). `rehber/11` → 'Programı çıkarma' step 1 and 'Güncellemeden önce' tell the agent to run it. If P5 ships without `--program`, the guide step falls back to `proje-kullanimi.py --skill <kimlik>` for each id in the card's `skilleri`. (The earlier `projeler.json → notlar → <proje> → program:<ad>` proposal is withdrawn.)

**To P7 (source lifecycle):** `kaynak-cikar.py` must refuse (with a pointer to `rehber/11` → 'Programı çıkarma') to remove a `kaynaklar.json` record that has `"program"`; and when a program is removed it clears that field through P6's documented step (manual edit) or P7's tool.

---------------------------------------------------------------------------------------------------

## 7. Needs the user's approval (at that time, never implied by this design)

- Any real **update** of HyperFrames (0.9.23 → 0.9.33, `npm install -g`) or OpenMontage (244 commits, `git pull --ff-only`, dependency steps): each one separately, per update, after the backup and `--oncesi` result are shown.
- Any **rollback**, **machine removal** (`npm uninstall -g`, deleting `~/.openmontage`), and **library removal** (deleting `programlar/<ad>/`, especially `kaynak/`): each separately; deletions of backup and trial folders are asked, never automatic.
- Defining `HYPERFRAMES_NO_AUTO_INSTALL` / `HYPERFRAMES_NO_UPDATE_CHECK` (currently undefined; the card marks them `gerekli: false` so nothing forces it) — writes shell/settings files.
- Changing the OpenMontage `origin` URL (card already says it needs approval).
- The exact `CLAUDE.md`/`AGENTS.md` line 51 text (§6 P8-3) and the rule-1 exception (P8).
- Entering the **user's decision** for `giris_yolu.araclar.claude-code` (OpenMontage entry after emptying; Bölüm 4 soru 1) — the card stores `karar-bekliyor` until decided.
- Recording `tedarik_dogrulama` values: `npm_integrity` is a read-only registry GET (no approval beyond the normal session); a sha256 for the etsyotomasyon release binaries needs a download, so it needs approval at that time.
- Filling `yerel_yamalar.bilinen[*].amac` for the nine patched files and the two untracked folders: ask the user what each patch is for (the design writes `ölçülmedi`, not a guess).
- Creating a backup folder `~/Documents/Claude/yedek/<program>-<tarih>/` and the trial folder `~/Documents/Claude/deneme/...` happens inside the approved update/trial; both are outside the library and git.
- Committing the still-uncommitted program work (`programlar/hyperframes/`, `programlar/openmontage/`, edited cards/guide): per library rules a commit follows each change; push only on the user's request (D12).

---------------------------------------------------------------------------------------------------

## 8. Deferred and why

- **Update executor / auto-apply** (a tool that backs up, installs, rolls back by itself): D7 and D2 forbid writing machine-wide folders from a tool; the user wants every real change approved. Kept as documented steps + read-only pre-check.
- **Post-update helper `--kayit-oneri`** (prints the card/KAYNAK.md values to copy): small gain; `--sema` (KAYNAK.md consistency) + plain denetim already catch a forgotten card update.
- **Program ↔ project mapping** (B7 explicit exception): belongs to P5 (`proje-kullanimi.py`, `projeler.json`); hand-off in §6.
- **etsyotomasyon release sha256 value and HyperFrames integrity value**: field and rule are in the schema; the etsyotomasyon value needs a download (approval); the HF value is filled at implementation by a read-only registry GET if the network is up.
- **Purpose of the nine OpenMontage patches and the basicsr venv patch**: unmeasured in the existing card (`rehber`/card say so); writing guesses would be false data.
- **Detecting a running render before update** (process check): needs `ps`/lsof, out of the read-only scope the tools use today; the approval sentence tells the user to stop renders; revisit if a failed update ever corrupts a render.
- **Scheduled reminder for backup deletion**: owned by P3/P4 (inventory and monthly summary), only the folder naming/format is P6's.
- **Dropped `--oncesi` checks (review):** `dışarıya yazar` (per-update value low; shape validated by `--sema`) and `tedarik` (only behind `--tedarik`); `çakışma` merged into `kırıcı`. Reason: 15 checks was more than a fresh agent can read; the 8 main ones are the ones that stop a real update.
- **Windows machines / Gemini CLI & Copilot CLI entries**: D1; schema allows the optional keys, no values written.
- **Checking `HYPERFRAMES_*` in Dock/GUI-launched apps**: not detectable by reading rc files (card already states the limit).
- **Signature verification of git commits / npm provenance attestation**: no key store and no tooling in D3 (stdlib only); commit sha / integrity pinning is the chosen minimum.

---------------------------------------------------------------------------------------------------

## 9. Risks and how the implementer verifies nothing existing broke

| Risk | Mitigation / check |
|---|---|
| Changing `npm_son_surum`/`git_son` breaks `araclar/test.py:1615-1636` (monkeypatched, "ağa gidilmez") | Signatures and returns unchanged; only a side-effect dict is added; the new network calls happen only after a 404 and never when the program is not installed. Run `python3 araclar/test.py` before and after; compare the pass/fail summary. |
| New schema makes old/bozuk test cards crash `main` | `sema_denetle` is wrapped in try/except inside `main`; failures become report lines; `main` still returns 0. Test 25 copies the old bozuk cards. |
| `--ozet-json` leaks other stdout | whole run under `redirect_stdout(sys.stderr)`; test 26 parses stdout as exactly one JSON object. |
| Report text changes churn `notlar/program-denetimi.md` | Existing tables byte-identical; new blocks appended; date-stripped compare kept (:338-341); test 28. Verify with `git diff notlar/program-denetimi.md` after a no-op run. |
| `git status` path parsing (renames, quotes, untracked dirs) misreports patches | Dedicated cases in test 16; real temp git repo test 22. |
| Reading `~/.zshrc` could expose secrets | Only the presence/equality of named switches is derived; no line is printed; test 15 asserts a fake secret never appears. |
| `gizli_dosyalar` check opens a key file | `os.path.lexists` only; test 18 uses an unreadable file. |
| `--oncesi` accidentally writes or fetches | Only `git_okuma` (read-only, `--no-optional-locks`), file reads, `gh_api`/`urllib` GETs; tests use `AssertionError`-raising fakes for `--cevrimdisi`; grep the new code for `write_text`, `subprocess.run(["npm"`, `pip`, `git fetch` (must find none outside strings). |
| Strict schema blocks a legitimately incomplete card the user is adding | `--iskelet` + `<DOLDUR>` flow; only `--siki` turns findings into exit 1; the monthly chain reports, never blocks. |
| Card text now very large (readability) | Fields are lists of short sentences; long prose stays in `rehber/11`; `rehber/11` is the single place for narrative (no duplication of steps beyond the card's own lists). |
| Card values drift from reality (paths) | `--oncesi` checks `giris_yolu` and `disariya_yazar` existence each run; `dogrulandi: false` marks unmeasured entries honestly. |
| `KAYNAK.md` consistency check fails on first run | KAYNAK.md files already contain `0.9.23`, the full OM sha, and the etsy full commit (verified by reading); keep those strings. |

Verification the implementer runs (all allowed in the implementation stage): `python3 araclar/testler/test_p6-programlar.py`; `python3 araclar/test.py` (existing suite green; compare count with the pre-change run); `python3 araclar/program-denetim.py --sema --siki` (0 hata on the real cards); `git diff --stat` shows only the owned files.

---------------------------------------------------------------------------------------------------

## 10. Acceptance (commands that prove it is done)

1. `python3 araclar/testler/test_p6-programlar.py` → last line `N/N test geçti`, exit 0.
2. `python3 araclar/program-denetim.py --sema --siki; echo $?` → `Kart şeması: 3 kart, 0 hata, …` and `0`.
3. `python3 araclar/program-denetim.py --iskelet git-checkout | python3 -c "import json,sys; json.load(sys.stdin)"` → exit 0; `… --iskelet npm-global` and `kaynak` likewise.
4. `python3 araclar/program-denetim.py --oncesi hyperframes --cevrimdisi; echo $?` → check table with `HATA yedek yok` (no backup exists today), `SONUÇ: HAZIR DEĞİL (…)`, exit `0`; with `--siki` exit `1`.
5. `python3 araclar/program-denetim.py --oncesi openmontage --cevrimdisi` → `kayıtsız yerel değişiklik` absent (all 9+6 paths recorded), `ortam` line for `HYPERFRAMES_SKIP_SKILLS` `3/3`, `giriş yolu` lines, `sabit sürümler` result, `yedek yok` HATA.
6. `python3 araclar/program-denetim.py --oncesi openmontage` (online) → shows `KIRICI ADAYI: 244 commit ileride (eşik 50)` and the repo state (`origin` `eski-ad` BİLGİ).
7. `python3 araclar/program-denetim.py --ozet-json | python3 -c "import json,sys; o=json.load(sys.stdin); assert set(o)=={'arac','durum','satirlar','karar_bekleyen'}"` → exit 0.
8. `python3 araclar/program-denetim.py` (no flags) → exit 0, report regenerated, per-program first lines identical in format to today's.
9. `python3 araclar/test.py` → no new failures versus the pre-change run; `python3 araclar/kapsam-denetimi.py` 0 sorun; `python3 araclar/dogrula.py` 0 hata (P8 may have added the `--sema` line).
10. `grep -n "oncesi" programlar.json | wc -l` ≥ 3 (one per card); `grep -c "^## " rehber/11-program-yonetimi.md` shows the 10 new section headings of §3.3; `ls promptlar/13-program-kur-guncelle.md`.
11. `git status --short` lists changes only in: `araclar/program-denetim.py`, `programlar.json`, `rehber/11-program-yonetimi.md`, `programlar/*/KAYNAK.md`, `promptlar/13-program-kur-guncelle.md`, `araclar/testler/test_p6-programlar.py` (plus the already-pending files of other packages).

---------------------------------------------------------------------------------------------------

## 11. Review changes

Applied (mandatory):
1. **`--sema` is not a library gate.** `dogrula.py` and `test.py` treat card findings as UYARI; only an unreadable/invalid `programlar.json` is HATA (§3.1 severity rule, §6 P8 items 1-2, test 3b). `--sema --siki` still exits 1 on HATA, but only the update steps use it. A card field can no longer roll back `--birlestir`.
2. **Two-layer card schema.** CORE (`giris_yolu, kurulum, geri_alma, cikarma, yedek, ortam_anahtarlari`) vs OPTIONAL (`disariya_yazar, tedarik_dogrulama, kirici_surum`, plus `gizli_dosyalar` and `yerel_yamalar` which I also made optional so the same silent-absence rule holds; a git card without `yerel_yamalar` is treated as "no recorded patches" = safe stop). `--sema` does not report missing optionals. To answer the readability complaint, `deneme_adimlari`, `gecme_olcutu` and the patch `uygulama` list moved out of the cards into `rehber/11`; a card size budget (target under about 330 lines, measured with `wc -l`) is set in 3.1.5. Patch `amac` values stay honest (`ölçülmedi`), no guesses.
3. **`--oncesi` cut from 15 to 8 main checks** (yedek, sabit sürümler, ortam, yama, repo, giriş yolu, gizli, kırıcı) plus 4 state lines (şema, kurulu, kart, son) that only decide the result word. `çakışma` merged into `kırıcı`; `dışarıya yazar` dropped; `tedarik` only with `--tedarik`. Example output 4.1, tests 13/20 and the guide text updated.

Applied (optional): P5 naming. 'Programı çıkarma' step 1 and §6 To P5 now use `proje-kullanimi.py --program <ad>`; `program:<ad>` withdrawn. Caveat found while re-checking P5's spec: its header lists `--program` among items deferred 'after review' but its mode list (line 215), tests and tool table still define it. So I kept the `--skill <kimlik>` fallback until P5's final text is confirmed.
Applied: `Önkoşul` line at the top (order 0-8 from the cross-package correction).

Gaps taken from the open list: (a) `--ozet-json` writes nothing, decision recorded in 3.2.1, §6 P4, test 26b; (b) stable, version-bearing `karar_bekleyen` strings so P4's 'kabul edildi' list can suppress closed decisions for P6 items.
Not taken (not P6 files or not P6's work): B2 triage, `--kayip-isaretle`, the `promptlar/10` '44 test' line, `rehber/08`, `kayip_tarihi`, `--hizli`, Windows/GEMINI.md, 'damga yok', library path in project blocks. None needs a P6 change.

Rejected: none of the corrections. Not changed on purpose: `npm_son_surum`/`git_son` signatures (existing tests monkeypatch them; code re-checked: `araclar/test.py:1620-1621`).
