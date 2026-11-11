# P7 design: source life cycle and candidate follow-up

Package P7. Language: English prose; identifiers, flags, file names and user-facing strings are Turkish exactly as they will appear.
Library root below = `/Users/sabanulukaya/Documents/SkillKutuphanesi` (written `KOK`). Line numbers refer to the state at the start of the audit (git clean, HEAD cf5e4a39d).
Status of this file: DESIGN only. Nothing in the library was changed while writing it.

**Önkoşul (uygulama sırası: 0 commit edilmemiş `programlar/` işi, 1 P3, 2 P1, 3 P2/P5/P6, 4 P7 = bu paket, 5 P4, 6 P8, 7 CLAUDE/AGENTS Yama B, 8 genel klasör boşaltması):** P7 başlamadan `git status --short` boş olmalı (0. sıradaki commit kullanıcı onayıyla atılmış). Gerçek bağımlılıklar: P5'in `proje-kullanimi.py` işlevleri (`projeleri_bul`, `oku`; bugün var) ve `kaynaklar.json` `program` alanı (bugün var). P7, P4'ten ÖNCE biter: P4 `kaynak-cek.py --help` çıktısında `--atla` arar. P7'nin kendi testleri P1/P3'ü gerektirmez.
**Kapsam notu (inceleme sonrası daraltıldı):** Bu paket iki aşamadır. Aşama 1 (şimdi uygulanır): bölüm 3'te "AŞAMA 1" yazanlar. Aşama 2 (ertelendi, bölüm 8): "ERTELENDİ" yazanlar. Ayrıntı ve gerekçe bölüm 11.

--------------------------------------------------------------------------------------------------------------------------

## 1 Purpose

Close, inside the files P7 owns, these gaps from `ozet-bolum2-4.md`. Scope was narrowed after review (section 11): what ships now is the smallest set that closes the gap.

| Gap | What P7 does NOW (Aşama 1) |
|---|---|
| B4 (except `arsiv-guncelle.py`) | New read-only `araclar/kaynak-cikar.py` (impact report + exact ordered manual steps + rollback). `kaynak-cek.py --atla` (an unreachable source no longer stops the whole monthly chain; P4 calls it). Written removal / retire / lost-source flows in `rehber/03` and `rehber/09`. `rehber/09` step 3 file list completed. Prompt `promptlar/14-kaynak-cikar.md`. |
| B8 (all but `dogrula.py`) | One fixed add order shared by `rehber/03` and `promptlar/07`, now 9 steps (A1..A9). Approval record on the source entry (`eklendi`, `onay{...}`). `yol-tara.py --siki` gate. `kaynak-cek.py` pure function `lisans_riskli` (used by P8's dogrula). `listeye-ekle.py` lower-case membership bug fix. Rollback of an add written down. `dogrula.py` parts are hand-offs to P8 (section 6), all warning-level. |
| B2 candidate parts | `konu-takip.py`: one shared elimination (case-insensitive, `izlenen` and removed repos excluded), validated `--karar`, one read-only `--bekleyenler [--ozet-json]` that reports the candidates of all three sources (konu-takip, trend, populer) for P4 (max 5 names per source = triage view). |
| Data | One-field data edit: `kayip_tarihi` on the existing KAYIP record (needs the user's approval, section 7). |

ERTELENDİ (section 8): rewrite of `github-trend.py` and `populer-tarama.py` (they stay byte-identical), `github-skill-listesi.py` consent/snapshot/`--geri-al`, `kaynak-cek.py` early-error (K1) and summary block (K3), `--yeniden-ac`, `--kayip-isaretle`.

Hard constraints honoured: stdlib only, Turkish text, existing flags/outputs/lock formats unchanged except where stated in section 3; no write to machine-wide skill folders, shell rc, settings, scheduled tasks or project folders; rule 6 (no project names in registry/kaynaklar/programlar cards): `kaynak-cikar.py` prints project names to stdout only and writes nothing; secrets never touched.

The user does not follow this personally: a library session (agent without memory) runs it. Every real change (adding a source, removing a source, GitHub star/list change, project skill removal) needs the user's approval at that time; the tools only prepare, check and print.

--------------------------------------------------------------------------------------------------------------------------

## 2 Existing behaviour relied on (file:line)

Shared helpers
- `araclar/ortak.py:11-18` constants `KOK, REGISTRY, KAYNAKLAR, GECICI, TREND`; `:44-56` `json_oku` (returns default when file missing) and `json_yaz` (atomic, `indent=2`, `ensure_ascii=False`).
- `ortak.py:433-454` `repo_takma_adlari` / `repo_guncel`: cached in module global `_TAKMA_ADLAR` (tests must reset it); maps `eski_adlar` to current repo.
- `ortak.py:415-427` `trend_durumu`.
- `ortak.py:989-1000` `yol_degerlendir(s, skiller, kurulacak_idler=None)` returns `{"sutun", "sayim", "satirlar": [(seviye, kod, govde)], "cevrilecek"}`; `ortak.py:887` `skill_yol_taramasi`; `:909` `istisna_anahtari`; `:1189-1222` `yol_istisna_denetimi` (keys already remapped through `eski_adlar`, so a repo rename needs no exception rewrite).
- `ortak.py:154-182` `repo_lisansi` returns SPDX id, `"belirtilmemiş"` or `"NOASSERTION"`.

Registry facts
- `registry.json` top keys: `_aciklama, guncelleme, skiller, bilesenler, denetim`. A skill record has (among others) `id, ad, repo, kaynak_yol, durum` (`tercih|alternatif`), `kaynak_durumu` (`None|kaynakta-kaldirildi|kayip`, 5647/1/1 today), `commit` (40 hex), `lisans`, `ortusme_grubu/ortusme_rolu`, `kopya_kaynaklar`, `ust_skill`, `gizli`, `tip`, `ucret`. Licence distribution today: MIT 3557, belirtilmemiş 1456, Apache-2.0 464, NOASSERTION 100, AGPL-3.0 72.
- `kaynaklar.json` top keys: `github_skill_listesi, ayna_klasorler, max_dosya_mb, repolar, konum_haric, skill_ici_haric, arsivden_cikarilanlar (109), takip_konulari, korunan_listeler, arsivden_cikarilan_repolar (9)`. `repolar[*]` keys seen: `repo, tip, oncelik, not, haric, dahil, dahil_degil, bagimlilik, kimlik, dosya_haric, program, kok_dosyalari, eski_adlar` (+ `ad_devral` per `rehber/03:54`). `tip` counts: T1 105, T6 35, T5 18, T2 15, T3 6, T4 1, KAYIP 1 (J-DTurner/etsy-api-skill, `not` records the 404 on 2026-11-10; no `kayip_tarihi` field exists yet).
- `arsivden_cikarilan_repolar` entries: `{repo, skill_sayisi, neden, tarih, geri_alma}` (9 entries). `arsivden_cikarilanlar`: `{repo, kaynak_yol, ad, neden, tarih, son_commit}` (109).

Removal mechanics (why the ledgers matter)
- `arsiv-yerlestir.py:337-339`: manifest records of repos that are no longer in `repolar` or that appear in `arsivden_cikarilan_repolar` are dropped, so a stale `.gecici/cekilen/manifest.json` cannot resurrect a removed repo.
- `arsiv-yerlestir.py:329-332`: exits with "Önce araclar/kaynak-cek.py çalıştır." when `.gecici/cekilen/manifest.json` is missing (fresh clone) or has no records.
- `arsiv-yerlestir.py:463-466`: registry skills whose `(repo, kaynak_yol)` is in `arsivden_cikarilanlar` or whose repo is in `arsivden_cikarilan_repolar` are skipped (not preserved).
- `arsiv-yerlestir.py:632-637`: safety lock ("güvenlik kilidi"): a previously present source that disappears exits unless it is in those two ledgers or `--kayba-izin-ver` is given. With the ledgers filled `--kayba-izin-ver` is NOT needed and must not be used.
- `kaynak-cek.py:93-96` and `:75`: a skill in `arsivden_cikarilanlar` gets decision `haric:arsivden-cikarildi` (not downloaded again).
- `arsiv-guncelle.py:284-286`: one unreachable source stops the whole `--uygula`; advice is `tip: "KAYIP"`, never delete the record. `arsiv-guncelle.py:158`: dirty tree stops `--uygula`. `arsiv-guncelle.py:189-198`: monthly chain runs `github-trend.py --aday`, `populer-tarama.py`, `konu-takip.py` as subprocesses (non-zero return = a printed UYARI only); `:201-203` runs `yol-tara.py` (return value only checked for non-zero).
- `kapsam-denetimi.py:48,135` KAYIP repos are never queried again (a repo that comes back or moves is never noticed).

Install / project side
- `skill-ekle.py:1223-1252` `kaldir()`: removes a skill from one project (backup first, `--geri-al <yedek>`); flag `--kaldir` at `skill-ekle.py:1546`, `--kuru` at `:1563`, `--evet` at `:1564`. `skill-ekle.py:1018-1022,1435-1437`: `kaynakta-kaldirildi` / `kaynak-kayip` UYARI and `EMEKLİ` marks (projects keep working on a lost source).
- `proje-kullanimi.py:28-42` `projeleri_bul(ayar)`, `:45-53` `oku(ayar)` (returns `[{"ad","yol","kilit","elle"}]`), `:137-145` `kullanan_projeler(repolar=(), idler=())` returns `{proje: [kurulu ad]}` and returns `{}` both when no project is on this machine and when nobody uses the source. P5 promised these signatures stay (tasarim-p5 L20). `AYAR = KOK/"projeler.json"` (`:24`).
- `dogrula.py:112-130` roles: an entry in `cekirdek/opsiyonel` resolves by `id` or by bare `ad` of the `tercih` skill (`:116` HATA `rol <r>: skill yok -> <x>`). `dogrula.py:97-98` ücret UYARI; `:244-255` loads `github-skill-listesi.py` by importlib and warns `YENİ SKILL REPOSU`; `:259-283` rule-6 scan of `kaynaklar.json, registry.json, ucret-siniflandirma.json, kategori-kurallari.json` for project names; `:286` `sys.exit(1 if hatalar else 0)` (warnings never fail). `dogrula.py` has no argparse: NEVER run it with `--help`.
- `skill-calistir.py:322-352`: `--skill id ...` runs only those, returns 1 on HATA, does NOT rewrite `TEST_RAPORU.md` (only without `--skill`, `:350`).
- `gelistirici-bilgisi.py:127`: any argv containing `/` limits the refresh to those repos.

Candidate tools
- `konu-takip.py:28-29` `DURUM = KOK/"konu-takip.json"`, `RAPOR`; `:95-97` `bilinenler`; `:100-134` `rapor` (candidate filter duplicated at `:112` and `:119`, and again in `main()` `:166`, all case-sensitive and ignoring `izlenen`); `:140-148` `--karar` (`izle` writes then pops from `degerlendirilen` and writes `izlenen`, but reports never exclude `izlenen`).
- `populer-tarama.py:83-93` `--karar` (writes `izle` INTO `degerlendirilen`: permanently hidden); `:95-97` lowercases ledger keys (konu-takip does not); `:109-111` `skilli/yeni/eski`.
- `github-trend.py:117-154` `rapor`: only `kaynak` (`:118`) is eliminated; candidate list `:140`; `aday_skill_sayisi` `:143`; `main()` `:157-175`; `--rapor` still calls `registry_guncelle` (`:164`) which writes `registry.json` if a trend field changed.
- `konu-takip.json` today: keys `_aciklama, degerlendirilen (192: 170 reddedildi, 22 eklendi, 0 izle), konular, izlenen (3)`; 67 ledger keys have upper-case letters. Therefore NO migration of `degerlendirilen` is needed (no `izle` entries there).
- `trend.json` keys: `_aciklama, gecmis, son_tarama, son_liste, taramalar, skill_sayisi`.

GitHub list tools
- `github-skill-listesi.py:26-37` `gql`, `:40-55` `listeler()` (paginated), `:58-149` `main`; `:75` `yeni`; `:79-80` `eksik/kopya`; `:83-90` move detection only when both `yeni` and `eksik` non-empty; `:104-124` `--ekle` (no consent, PUT star + `updateUserListsForItem` with target list + protected lists only, `:119`); `:125-149` `--duzenle` (same drop of non-protected lists, `:138`).
- `listeye-ekle.py:23-25` loads gsl by importlib; `:32` `var`; `:58-68` consent via `input()`; `:69-73` `uyelik` keyed by exact-case `nameWithOwner`; `:82,87` lookups with the user's spelling (BUG: a lower-case argument misses and `:87` sends only the target list, dropping protected-list memberships).

Tests that must keep passing
- `araclar/test.py:501-503` `yol-tara.py --skill` (no value) and `--bogus` must exit 0; `:519-520` unknown skill exits 0 and writes nothing. `arsiv-guncelle.py:201-203` relies on `yol-tara.py` exit 0.

--------------------------------------------------------------------------------------------------------------------------

## 3 Changes per file

Naming of modules in code: the tools have hyphens, so they are loaded with `importlib.util.spec_from_file_location` exactly like `listeye-ekle.py:23-25`. Importing must have no side effects (all five candidate/list tools and `kaynak-cek.py` already guard `main()`).

### 3.1 NEW `araclar/kaynak-cikar.py` (impact and step report; `--kuru` only)

#### Purpose
For one source repo or one skill id: list everything that depends on it, say what blocks or needs care, print the exact ordered manual steps (with ready-to-paste ledger JSON) and the rollback. It changes nothing: no file written, no network unless `--github`. Project names go to stdout only (rule 6/D8).

#### CLI
```
python3 araclar/kaynak-cikar.py --repo owner/ad --kuru [--neden "gerekçe"] [--json] [--github] [--siki]
python3 araclar/kaynak-cikar.py --skill <kimlik|ad> --kuru [--neden "gerekçe"] [--json] [--github] [--siki]
```
- Exactly one of `--repo` / `--skill`. `--kuru` is REQUIRED: a call without it prints `Bu sürümde yalnız --kuru var (etki raporu; hiçbir şey değiştirmez).` and exits 2. `--help` says the same in its first lines. Any applying flag (`--uygula`, `--evet`) is rejected by argparse (exit 2). Reason: a future applying mode must never change what a bare call does.
- `--repo`: accepts the current name or an old name (`repo_guncel`), case-insensitive.
- `--skill`: exact `id` first; otherwise bare `ad`: exactly one match -> proceed; several (tercih + `ad@kaynak` alternatives) -> print the candidate ids and exit 2 (`Birden çok kayıt: tam kimliği yaz: --skill <id>`).
- `--neden`: text copied into the ledger snippet; without it the snippet carries `"<NEDEN: kullanıcının onayladığı gerekçe>"` (P8's dogrula warns about the placeholder, section 6).
- `--github`: read-only network: (a) `gh api repos/<repo> --jq .full_name` -> `erişilebilir (full_name)` / `404: kaynak kayıp` / `okunamadı`; a different `full_name` prints `AD DEĞİŞMİŞ: <yeni>` and the verdict note `çıkarma değil, rehber/09 'Repo adı değişirse'`; (b) star state `gh api user/starred/<repo>` (rc 0 starred / non-zero not starred); (c) list membership through `gsl.listeler()` (read-only GraphQL). Each failure prints `okunamadı` and never fails the run.
- `--json`: prints ONE JSON object (shape below) instead of the text; stdout contains nothing else.
- `--siki`: exit 1 when the verdict is `engel` or `reddedildi`.
- Exit codes: 0 report produced (any verdict, per D4); 1 only with `--siki` and verdict engel/reddedildi; 2 usage error, target not found, ambiguous target, missing `--kuru`.
- Core function `rapor_uret(kok, hedef_turu, hedef, neden=None, github=False, bugun=None) -> dict` takes the library root so tests run on a temp tree; `main(argv=None)` is thin. All data paths (`registry.json`, `kaynaklar.json`, `roller/`, `profiller/`, `konu-takip.json`, `trend.json`, `projeler.json`, ...) are derived from `kok` inside the function (not module globals). It must NOT use `ortak.repo_guncel` (its cache `_TAKMA_ADLAR` reads the real `kaynaklar.json`): the old-name map is built locally from the `kaynaklar` dict already loaded (`{eski.lower(): repo}` from `repolar[*].eski_adlar`). The project lookup loads `proje-kullanimi.py` from the REAL `Path(__file__).parent` (never from `kok`) and calls `pk.projeleri_bul(ayar)` and `pk.oku(ayar)` with `ayar = json_oku(kok/"projeler.json", {})`; tests give a temp `ayar` whose `tarama_kokleri`/`ek_projeler` are absolute temp paths. If P5 later changes the module, only these two functions are used.

#### What it computes (report sections, in this order)
0. Target resolution.
   - Repo mode: canonical = `repo_guncel(arg)`; records = all `kaynaklar.repolar` entries with that repo (case-insensitive; a repo may have several records, e.g. T1 + T4); skills = registry skills of that repo. No record: if the repo is in `arsivden_cikarilan_repolar` print `Zaten çıkarılmış (tarih, neden). Geri alma: ...` verdict `yok` exit 0; if only registry skills exist (orphan) say so and continue with an `orphan` note; otherwise exit 2 `Bulunamadı`.
   - Skill mode: the registry record; its repo record(s); `kaynak_yol`, `commit`, `durum`, `kaynak_durumu`, `ortusme_grubu/rolu`. Note `bu repodaki tek skill: tüm kaynağı çıkarmak için --repo` when the repo has exactly this one skill.
   - Programme guard: any record with a `"program"` field -> verdict `reddedildi`, text `Bu kaynak bir PROGRAM olarak da izleniyor (kaynaklar.json "program": "<ad>"). Programı çıkarma rehber/11 → 'Programı çıkarma' bölümündedir; önce oradaki adımlar. Bu araç adım üretmez.` No step list printed. (Requested by P6, tasarim-p6 L537.)
1. Projeler. `pk.projeleri_bul(ayar)` empty -> `Bu bilgisayarda proje bulunamadı: etki BİLİNMİYOR (başka bilgisayar/bulut olabilir)` and the verdict can never be `hazir` (becomes `dikkat`). Otherwise per project: installed name, `id`, the skill's own `roller` list from the lock, matching rule: repo mode `repo_guncel(v["repo"]).lower()==canonical.lower()`; skill mode `v.get("id", ad)==id or (repo_guncel(v["repo"]).lower(), v.get("kaynak_yol"))==(repo.lower(), kaynak_yol)`. Per project the follow-up line `python3 araclar/skill-ekle.py "<yol>" --kaldir <ad> [<ad>...] --kuru` (never executed).
2. Roller ve profiller. `roller/*.json` `cekirdek` + `opsiyonel`; `profiller/*.json` `ek_skiller`. An entry matches when it equals a target `id`, or equals a target `ad` while that target skill is `tercih` (same resolution as `dogrula.py:112-116`). Each hit prints `roller/<dosya>: cekirdek|opsiyonel: <girdi>` / `profiller/<dosya>: ek_skiller: <girdi>`. Any hit = ENGEL (dogrula would raise `rol: skill yok`). Also lists the profiles that contain an affected role (informational).
3. Registry. Counts and the first 30 ids (`id (durum, kaynak_durumu)`); `kopya_kaynaklar` of the skills; same-`ad` siblings (other ids) with a note `çıkarınca tercih hangisine geçer: python3 araclar/skill-ekle.py --listele --ara <ad>`; `ortusme_grubu` members and `birincil` loss (`DİKKAT: <grup> grubunun birincil skili gidiyor`); children (`ust_skill == id`); `yamalar/<id>/` directory presence; `aciklama_duzeltme`/`yama` fields (travel with the record, informational).
4. Çıplak ad devri. (a) this record's `ad_devral` names and the registry holders `ad@...` of those bare names (`çıkarınca çıplak ad boşalır; kimlikler değişmez`); (b) other records' `ad_devral` containing an `ad` of the target skills (`başka kaynak bu adı devralmış`). DİKKAT only; no step beyond `--listele --ara`.
5. Yıldız ve liste. Offline: prints `GitHub yıldızı ve liste üyeliği git dışındadır; kullanıcının kararıdır. Kaldırmak: gh api -X DELETE user/starred/<repo> (listeden de çıkar). Geri: python3 araclar/listeye-ekle.py <repo>`. With `--github`: real state.
6. Kartlar, konular, kayıt dosyaları (mention counts only, never values). Case-insensitive occurrences of the repo string (repo mode) in: `kaynaklar.json, kategori-kurallari.json, ucret-siniflandirma.json, gelistiriciler.json, trend.json, konu-takip.json, yol-istisnalari.json, programlar.json, projeler.json, notlar/referans/*.md` (print `dosya: N satır`, plus first 3 line numbers for `notlar/referans/*.md`: T5/T6 card/row to delete). Skill mode: structured checks only (ids/ad as keys in `ucret-siniflandirma.json -> siniflar`, `yol-istisnalari.json` key `repo::kaynak_yol`, `projeler.json -> notlar` skill-id keys, `yamalar/<id>/`). Generated files (`registry.json, KATALOG*.md, notlar/proje-kullanimi.md, notlar/*denetimi*.md`) are NOT scanned; they refresh from the tools in the steps. Also: `konu-takip.json -> konular.*.repolar`, `degerlendirilen`, `izlenen` hits and `trend.json -> gecmis` hit.
7. Karar (verdict) rules: `engel` = roles/profiles hit. `reddedildi` = programme guard. `dikkat` = no engel but any of: projects using it, no project info on this machine, programme-free but `ad_devral` hits, birincil loss, T5/T6 card present, `kaynak_durumu` not None for skills, repo moved (`--github`). `hazir` = none of the above. `yok` = already removed.
8. Adımlar and Geri alma (text in section 4).

#### Output
Text: sections as above, Turkish, plain. `--json` shape:

```json
{
  "arac": "kaynak-cikar",
  "mod": "kuru",
  "hedef": {"tur": "repo", "repo": "owner/ad", "eski_adlar": ["eski/ad"], "tip": "T1", "kayit_sayisi": 1, "skill_sayisi": 12, "kayip": false, "program": null},
  "karar": "engel",
  "engeller": ["roller/web-gelistirici.json: cekirdek: gsap-core"],
  "dikkatler": ["projeler: 2 projede kurulu", "T6 kartı: notlar/referans/tasarim-teknolojileri.md satır 41"],
  "projeler": [{"proje": "ProjeA", "yol": "~/Documents/ProjeA", "skiller": [{"kurulu_ad": "gsap-core", "id": "gsap-core", "roller": ["web-gelistirici"]}]}],
  "proje_bilgisi": "var",
  "roller": [{"dosya": "roller/web-gelistirici.json", "alan": "cekirdek", "girdi": "gsap-core"}],
  "profiller": [{"dosya": "profiller/nextjs-web-uygulamasi.json", "alan": "ek_skiller", "girdi": "gsap-core"}],
  "registry": {"idler": ["gsap-core"], "alternatif_kardesler": [], "ortusme": [], "kopya_kaynaklar": []},
  "ad_devri": {"bu_kaydin": [], "baska_kayitlarin": []},
  "kayitlar": [{"dosya": "konu-takip.json", "satir": 3}],
  "github": null,
  "defter_taslagi": {"defter": "arsivden_cikarilan_repolar", "kayit": {"repo": "owner/ad", "skill_sayisi": 12, "neden": "<NEDEN: kullanıcının onayladığı gerekçe>", "tarih": "2026-11-12", "onay": {"kim": "kullanıcı", "tarih": "2026-11-12", "oturum": "<kısa not>"}, "son_commit": "95ea931a1ad8f9b2be132ae0cfb2aad964d71118", "geri_alma": "git revert <commit>; GitHub: python3 araclar/listeye-ekle.py owner/ad"}},
  "adimlar": ["0. git status --short ...", "1. ..."],
  "geri_alma": ["Commit atılmadıysa: ...", "Commit atıldıysa: git revert <commit>"]
}
```
Skill mode `defter_taslagi.defter` = `arsivden_cikarilanlar`, `kayit` = `{"repo","kaynak_yol","ad","neden","tarih","son_commit","onay":{...}}` with `son_commit` = registry `commit` of that skill. Repo mode `son_commit` = the (sorted first) distinct registry `commit` of the repo's skills. `tarih` = today (`bugun` parameter for tests).

#### Step list (generated; exact order; items marked `[koşullu]` appear only when the section has hits)
Repo mode, `tip` T1-T4 or KAYIP; skill mode differs only at steps 4 and 6 (shown).
```
 0. git status --short  -> boş olmalı. Değilse DUR, kullanıcıya söyle.
 1. Bu raporu kullanıcıya göster. Ölçüt ve içerik doğrulaması (rehber/03 D0) yapılmadıysa önce onu yap. Kullanıcının "evet, çıkar" cevabını bekle.
 2. [koşullu: roller/profiller] <dosya>: "<girdi>" girdisini çıkar ya da yerine geçeni koy (yoksa dogrula HATA verir).
 3. [koşullu: projeler] Her proje için kullanıcıya sor, onaylarsa: python3 araclar/skill-ekle.py "<yol>" --kaldir <adlar> (önce --kuru). Çıkarılmazsa projedeki kopya çalışır ama kaynak kütüphanede yoktur (--durum: kaynak-yok).
 4. kaynaklar.json: [repo modu] "<repo>" kaydını repolar'dan SİL (kaydı KAYIP yapıp bırakma: o ayrı bir karar, rehber/03 E) ve arsivden_cikarilan_repolar'a şu kaydı ekle: <JSON>
    [skill modu] kaydı SİLME; arsivden_cikarilanlar'a şu kaydı ekle: <JSON>
 5. [koşullu: T5/T6] notlar/referans/<dosya>: <satır/kart> sil.
 6. [skill modu] python3 araclar/kaynak-cek.py --repo <repo>      [repo modu] .gecici/cekilen/manifest.json yoksa: python3 araclar/kaynak-cek.py
    Sonra: python3 araclar/arsiv-yerlestir.py   (--kayba-izin-ver KULLANMA: defter kaydı güvenlik kilidini zaten geçirir)
 7. python3 araclar/kapsam-denetimi.py   (0 sorun)
 8. python3 araclar/katalog-uret.py
 9. python3 araclar/dogrula.py   (0 hata; uyarı sayısı 0. adımdaki başlangıçtan fazla olmasın)
10. python3 araclar/test.py
11. git status --short göster; tek commit: git add -A && git add -f arsiv && git commit -m "Kaynak çıkarıldı: <repo>"
12. GitHub (git dışı, kullanıcının kararı): yıldız/liste kalsın mı? Kaldırılacaksa kullanıcı onayıyla: gh api -X DELETE user/starred/<repo>
```
Rollback lines (section 4). Step 12 is last on purpose: GitHub effects are not undone by `git revert`.

#### Why no applying mode now (justification, also printed in `--help`)
(1) Removals are rare (9 whole-repo entries in the ledger since 2026-10); the manual edit is one JSON record plus role lines. (2) The dangerous, usually skipped part is the impact check, which this tool automates. (3) An applying mode would rewrite `kaynaklar.json` with `json_yaz` (re-indent of a 181-record file, risk of a large unrelated diff) and edit role/profile JSONs, each needing backups, dry-run default and `--evet`; the safety work is larger than the saved typing. (4) Revisit when more than ~10 removals happen per quarter or when a manual step is gotten wrong twice. A future `--uygula` would be `--kuru` + `--evet`, editing only `kaynaklar.json` (after `git status` clean) and printing the diff; roles stay manual. Recorded in section 8.

### 3.2 `araclar/kaynak-cek.py` (337 lines) — AŞAMA 1: K4 (`--atla`) and K2 (`lisans_riskli`); K1, K3 ERTELENDİ

Old: only `--repo`; one unreachable source: `GhBulunamadi` -> `sys.exit` at `:238-240` and the whole run (and, through `arsiv-guncelle.py`, the whole monthly update) stops.

- **K4 `--atla owner/ad[,owner/ad]`** (mandatory correction; P4 depends on it). `ap.add_argument("--atla", default="", help="owner/ad[,owner/ad]: bu kaynaklar için indirme ve repo ağacı okuması yapılmaz; arşiv kopyası korunur (erişilemeyen tek kaynak aylık güncellemeyi durdurmasın)")`. `--help` therefore shows `--atla`; P4's `kaynak_cek_atla_var()` greps it.
  - Pure helper `atla_kumesi(deger, kayitlar, cevir=repo_guncel) -> (set, tanimsiz)`: splits on `,`, strips, drops empties, maps each name through `cevir` (old name -> current name) and lower-cases. `repo_guncel` is added to the `from ortak import (...)` line at `:31`. `tanimsiz` = names that match no T1-T4 record (`k["tip"] in ARSIVLENEN_TIPLER`), compared case-insensitively on `cevir(k["repo"]).lower()`.
  - In `main()` after `kayitlar` is built (`:219`): `atla, tanimsiz = atla_kumesi(a.atla, kayitlar)`; for each name in `tanimsiz` print `UYARI: --atla <repo>: T1-T4 kaydı yok; yok sayıldı`.
  - At the top of the `for kayit in kayitlar:` loop (before `repo_agaci`, `:229`): `if cevir(repo).lower() in atla:` print once per repo `UYARI: <repo> atlandı (arşiv kopyası korunur)` and `continue`. No download, no `repo_agaci` call, NOTHING appended to `manifest["kayitlar"]`/`bilesenler`/`denetim` for that repo. (In all-repos mode the manifest starts empty, so the repo is simply absent; `arsiv-yerlestir.py:471-474` then keeps that repo's registry skills as `korunan_indirilmeyen` because the repo is still T1-T4 in `kaynaklar.json` and absent from `cekilen_repolar`; re-checked in code.)
  - Exit code: unchanged rule; if everything else succeeded the run ends 0. With `--repo X --atla X` the run prints the UYARI and ends 0 with `Toplam kayıt: 0`.
  - Without `--atla` the behaviour (including `:238-240` stop message) is byte-identical.
  - Final `json_yaz(cikis / "manifest.json", manifest)` and `Toplam kayıt` line unchanged.
- **K2** new constant `RISKLI_LISANS = ("belirtilmemiş", "NOASSERTION", "yok", "AGPL-3.0", "AGPL-3.0-only", "AGPL-3.0-or-later")`, prefixes `("CC-BY-NC", "PolyForm-Noncommercial", "BUSL", "SSPL")`, pure function `lisans_riskli(lisans) -> bool`. No printing, no call in `main()`. P8's dogrula loads it (hand-off) and `rehber/03` A3 tells the agent to ask the licence question.
- **K1 (early error for an unknown `--repo`) and K3 (summary block printed after each repo): ERTELENDİ.** K1 changes the exit code of an existing path and K3 adds output; neither is needed to close a gap now (the licence/commit/decision checks are in the A2 reading step and in P8's warning-level gates). `rehber/03` A5 tells the agent to check the printed line `<repo> ... skill=N` and `Toplam kayıt: N` (0 = repo name or tip wrong).

### 3.3 `araclar/yol-tara.py` (219 lines)

Old: exit always 0 (`:4,:191-192,:215`); `--repo` with nothing found prints a message and returns 0 (`:174-177`).
New (additive):
- `--siki` flag (`ap.add_argument("--siki", action="store_true")`, after `:188`). Without it every behaviour and exit code is byte-identical (test.py:501-503, 519-520).
- New function `kapi_kontrol(repo=None, skill_id=None, skiller=None) -> (sorunlar: [str], taranan: int, hata: str|None)`. For each target skill (registry or `.gecici/cekilen` fresh material, same selection as `repo_ayrinti` `:166-182`) it takes `d = ortak.yol_degerlendir(s, tum)` and reports a problem when `d["sutun"] == "cozulemez"` or any satır `(UYARI, kod, gövde)` with `kod in ("genele-yazabilir", "istisna-eskidi")`. Problem text: `KAPI: <id>: <kod>: <gövde kısa>`. Exceptions per skill are inside `ortak.yol_degerlendir` (a skill covered by `yol-istisnalari.json` has sütun `istisna`, so it passes).
- `--siki` rules in `main()`: allowed only with `--repo` or `--skill`; alone -> print `--siki için --repo ya da --skill ver.` and return 2. With a target: print the normal detail (unchanged), then the gate result and return 0/1:
  `YOL KAPISI: GEÇTİ (<n> skill tarandı)` -> 0; `YOL KAPISI: TAKILDI (<k> sorun / <n> skill)` followed by the `KAPI:` lines -> 1; target found nowhere or any exception -> `YOL KAPISI: TAKILDI (taranamadı: <kısa neden>)` -> 1 (nothing checked is never "passed").
- The user's way to clear the gate: `yol-istisnalari.json` record (only for teaching text, `kabul` only after the user saw the report; `rehber/03 A5`) or an `onay.yol_onay` justification on the source record (P8's dogrula honours it).
- Module stays importable (`kapi_kontrol` is used by P8's dogrula through importlib).

### 3.4 `araclar/github-skill-listesi.py` (153 lines) — ERTELENDİ (no change)

Review verdict: making `--ekle`/`--duzenle` ask consent (and stop in non-interactive shells), take a snapshot and offer `--geri-al` is a behaviour change the user did not ask for. The file stays byte-identical. Mitigation in documents only: `rehber/03` A9 does not use `--ekle`/`--duzenle`; it names `listeye-ekle.py` (which already asks `e` before writing, `listeye-ekle.py:58-68`). `--duzenle` is documented as "GitHub'a hemen yazar; yalnız kullanıcı sohbette açıkça isteyince ve önce okuma raporunu gösterdikten sonra" (it silently drops the repo from non-protected lists, `:138`). A tightened version (consent, snapshot, `--geri-al`) is sketched in section 8 for a later approved change.

### 3.5 `araclar/listeye-ekle.py` (100 lines) — AŞAMA 1: L1 bug fix only

- **L1 BUG FIX `:69-73`**: key `uyelik` by `x["nameWithOwner"].lower()`; lookups at `:82,:87` use `r.lower()`. Old: `listeye-ekle.py altin/repo` with a differently cased argument sent only the target list and silently removed protected-list memberships. New: always preserves existing memberships. This is a pure bug fix (no new flag, no new output).
- **L4** docstring only: `listeye-ekle.py` is THE tool for "star + add to the skill list a repo that is not in the library" (single repo or `--dosya` batch); consent stays the existing `input()` question (`e`). Non-interactive shell: `input()` hits EOF and the run stops before any write; with the user's "evet" in chat the agent runs `printf 'e\n' | python3 araclar/listeye-ekle.py owner/ad` (stated in `rehber/03` A9).
- L2 (`--evet`, shared `onay_al`) and L3 (snapshot, `--geri-al`): ERTELENDİ with 3.4. Rollback of a GitHub add is manual and written in `rehber/03` G: the user removes the star/list entry (`gh api -X DELETE user/starred/<repo>` and the list page); the agent never does it alone.

### 3.6 `araclar/konu-takip.py` (173 lines) — AŞAMA 1: shared elimination, validated `--karar`, one `--bekleyenler`

New pure functions (added after `bilinenler`, `:95-97`; no I/O besides what callers pass):
```python
IZLE_GUN = 90          # izlenen kaydın 'tekrar bak' süresi (tarih + 90 gün hesaplanır, alan tutulmaz)
BAYAT_GUN = 45         # --bekleyenler: tarama bayatlığı

def elenecekler(ayar, durum):
    """-> {'kaynak': set, 'cikarilan': set, 'karar': set, 'izlenen': set}; hepsi KÜÇÜK HARF.
    kaynak = repolar[*].repo + eski_adlar (T1..T6 ve KAYIP dahil); cikarilan = arsivden_cikarilan_repolar (str ya da {'repo':..});
    karar = durum['degerlendirilen'] anahtarları; izlenen = durum['izlenen'] anahtarları"""
def eleniyor(repo, e, izlenen_dahil=True): ...      # repo.lower() in kaynak|cikarilan|karar (|izlenen)
def aday_mi(repo, v, k, e): ...                     # tek aday ölçütü (aşağıda)
def izlenen_vadesi(kayit, bugun=None) -> (tekrar_bak_tarihi, vade_geldi)
def karar_uygula(durum, ayar, trend, repo, karar, neden, bugun=None) -> (mesajlar, hata)
```
`karar_uygula` rules (pure; mutates `durum` only when `hata is None`):
1. `repo` must match `^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$` else `geçersiz repo adı: <repo> (owner/ad biçimi)`.
2. `karar` in `("eklendi","reddedildi","izle")` else `karar: eklendi | reddedildi | izle`.
3. Canonical key: an existing key in `degerlendirilen`/`izlenen` equal case-insensitively (reuse that spelling, never create a case-variant duplicate); else the spelling in `durum["konular"][*]["repolar"]` or `trend["son_liste"]`; else as typed. If the repo is in none of those: `UYARI: bu repo hiçbir tarama kaydında yok (yazım hatası olabilir); yine de kaydedildi.` (not an error).
4. Repo is a library source (`elenecekler["kaynak"]`) and `karar` is `reddedildi`/`izle` -> error `kütüphanede olan repoya <karar> verilemez (çıkarmak için kaynak-cikar.py)`.
5. Existing `reddedildi` + new `izle` -> error `daha önce REDDEDİLDİ (<tarih>: <neden>); yeniden değerlendirmek kullanıcı kararıdır (konu-takip.json'dan o kaydı sil)`. Existing `eklendi` + `reddedildi`/`izle` -> same text with `EKLENDİ`. `reddedildi` -> `eklendi` allowed (message `önceki karar reddedildi idi: güncellendi`). (No `--yeniden-ac` flag now.)
6. Write: `eklendi`/`reddedildi` -> `degerlendirilen[key] = {"karar","neden","tarih": bugun}` and remove `key` from `izlenen`; `izle` -> `izlenen[key] = {"neden","tarih": bugun}`. Empty `neden` -> `"-"` (as today).

`izle` MEANING (single definition, printed in the docstring and in `rehber/03` F): "şimdilik değil, durum değişirse bak". Stored ONLY in `izlenen`; kept out of the candidate table of `konu-takip.py` reports; shown in its own `İzlenenler` section with `⏰ zamanı geldi` after `tarih + 90 gün`. `reddedildi` is permanent.
Edits to existing code:
- `:95-97` `bilinenler(durum, ayar)` (new signature; the call in `tara()` `:75` becomes `bilinenler(durum, ayar)`): lower-case union of `kaynak|cikarilan|karar` (NOT `izlenen`: izlenen repos keep getting refreshed info); membership test `:80` becomes `repo.lower() in bilinen`.
- `:112,:119,:166`: the three candidate computations use the one predicate `aday_mi` (case-insensitive, excludes `izlenen`, `cikarilan`, `eski_adlar`); `:120` library count uses `e["kaynak"]`, `:123` "değerlendirilmiş" count uses `e["karar"]`.
- `:131-133`: new section `## İzlenenler (şimdilik değil; durum değişirse bak)` with `| Repo | Tarih | Tekrar bak | Neden |`, empty -> `(yok)`.
- `:104-107` header: `Reddedilen/eklenen repo bir daha aday olarak gösterilmez; izlenen repo ayrı bölümde durur: konu-takip.py --karar owner/ad reddedildi|eklendi|izle "neden"`.
- `:140-148` `--karar`: call `karar_uygula`; on error print and `sys.exit(2)` without writing; on success write `DURUM` and regenerate the report as today.
- **NEW `--bekleyenler [--ozet-json] [--siki]`** (offline, writes no file, handled BEFORE any scan; D4). It reports the decision backlog of ALL THREE candidate sources so the other two tools stay untouched:
  1. konu-takip: per topic the focused candidates (same `aday_mi` filter) + due `izlenen`; staleness from `konular[*].son_tarama` (newest).
  2. trend: `trend.json` `son_liste` repos not eliminated whose cached `skill_sayisi[repo]["skill"] > 0`; staleness `son_tarama`.
  3. populer: `notlar/populer-skiller.md`: report date by regex `· (\d{4}-\d{2}-\d{2}) ·`, names from rows `| [owner/ad](https://github.com/` of section `## Yeni adaylar`, then filtered with the CURRENT `elenecekler` (a repo decided after the scan disappears). Heading missing -> that source is `dikkat` with `populer-skiller.md okunamadı`.
  - A missing file of source 2 or 3 = line `<kaynak>: rapor yok` and `dikkat` (never `sorun`). `sorun` only when `konu-takip.json` or `kaynaklar.json` cannot be parsed.
  - `durum`: `dikkat` if any candidate, any due izlenen, or any source older than `BAYAT_GUN` days/missing; else `temiz`.
  - `satirlar`, e.g. `e-ticaret: 4 odaklı aday, son tarama 2026-11-04 (7 gün önce)`, `trend: 2 aday`, `popüler: 31 aday (rapor 2026-10-02, 40 gün)`.
  - `karar_bekleyen` = triage view: AT MOST 5 names per source (`<repo> (★N, <konu>)`, highest ★ first) + at most 5 `<repo> (izlenen, vadesi geldi)`; the total per source is in `satirlar`. The monthly cap N ("kaç aday karara bağlanır") is a user question handed to P8 (`notlar/kararlar.md`, section 6).
  - Output: text mode 6-10 lines; `--ozet-json` prints exactly one JSON object `{"arac":"konu-takip","durum":...,"satirlar":[...],"karar_bekleyen":[...]}` and nothing else on stdout. Exit 0; 1 only with `--siki` and `durum == "sorun"`. Shared printer `ozet_yaz(arac, durum, satirlar, bekleyen)` in this module.
  - Decisions stay immediate: once `--karar` is written the repo vanishes from all three lists (the ledger is read each time), so closed decisions do not come back in the monthly summary.
- Everything else (`tara`, `kod_ara`, `repo_bilgisi`, network paths) unchanged.

### 3.7 `araclar/github-trend.py` (179 lines) — ERTELENDİ (no change)
### 3.8 `araclar/populer-tarama.py` (138 lines) — ERTELENDİ (no change)

Both stay byte-identical (their monthly-chain behaviour is untouched). Known, documented consequences: `github-trend.py` still lists rejected repos in its own candidate table (only the library sources are eliminated, `:118`); `populer-tarama.py --karar izle` still writes `izle` into `degerlendirilen` (hides the repo forever). Mitigations without code: `rehber/03` F says "kararı HER ZAMAN `konu-takip.py --karar` ile yaz; `populer-tarama.py --karar` kullanma"; the summary the user sees comes from `konu-takip.py --bekleyenler`, which filters with the full ledger. Design for the later rewrite is in section 8.

### 3.9 `rehber/03-yeni-skill-ekleme.md` (160 lines), `rehber/09-ad-kimlik-ve-cakisma.md` (55), `promptlar/07-yeni-skill-reposu-ekle.md` (47)

Full replacement text is in section 4. Edit map:
- `rehber/03`:
  - top (`:3-12`): programme/skill decision box and pointer to the single add order (A1..A9).
  - `:14-30` (inspect + conflict + ücret + proje-bağımsız) becomes A2 (adds licence reading, security reading, Claude-specific-tool check, "Global'de aynı ad" line made conditional); nothing of the old content is dropped.
  - `:31-60` (tip table, alanlar, kategori kuralı) kept as A4 reference; add `eklendi`, `onay{...}`, `kayip_tarihi` to the `Alanlar` list.
  - `:61-76` (command block) and `:84-88` (step 5) are REPLACED by A1..A9 (prompt 11 uyumu paragraph `:77-83` kept and referenced from A6).
  - `:146-160` section D replaced by new D (removal with `kaynak-cikar.py`), plus new E (kayıp kaynak), F (aday kararları), G (eklemeyi geri al), H (emekli etme).
- `rehber/09`: `:38-47` "Repo adı değişirse" rewritten (step 3 list completed); new final section "Kaynak çıkarılırsa".
- `promptlar/07`: fully rewritten (4.8) so that step 4 points at `rehber/03` A-steps instead of copying; `:37` "0 uyarı" -> "başlangıçtakinden fazla uyarı yok"; `:20` global line conditional; `:40` `--duzenle` removed (A9 names `listeye-ekle.py`).

### 3.10 NEW `promptlar/14-kaynak-cikar.md`
Copy-paste prompt (text in section 4) for "şu kaynağı / skili kütüphaneden çıkar ya da kayıp kaynağı ele al".

### 3.11 NEW `araclar/testler/test_p7-kaynak-yasam.py`
See section 5.

--------------------------------------------------------------------------------------------------------------------------

## 4 User-facing texts

### 4.1 `kaynak-cikar.py --help` (first lines)
```
Kaynak çıkarma ETKİ RAPORU (yalnız okuma). Bu sürümde SADECE --kuru vardır; hiçbir dosyayı ve hiçbir GitHub kaydını değiştirmez.
Bir kaynak repo (--repo) ya da bir skill (--skill) için: onu kullanan projeler, roller/profiller, registry, çıplak ad devri,
yıldız/liste, kartlar ve kayıt dosyaları; sonra sıralı adımlar ve geri alma. Uygulayan mod yok: adımları kullanıcı onayıyla ajan elle yapar.
```
### 4.2 Report text (key lines; exact wording)
```
KAYNAK ÇIKARMA ETKİ RAPORU (yalnız okuma; hiçbir şey değişmedi)
Hedef: kaynak owner/ad · tip T1 · öncelik 4 · registry'de 12 skill (11 tercih, 1 alternatif)
1. PROJELER  (bu bilgisayarda 3 proje bulundu)
   ProjeA: gsap-core (kimlik gsap-core; roller: web-gelistirici)
   sonra: python3 araclar/skill-ekle.py "<yol>" --kaldir gsap-core --kuru
   -- ya da: Bu bilgisayarda proje bulunamadı: etki BİLİNMİYOR (başka bilgisayar/bulut olabilir).
   -- ya da: Hiçbir projede kullanılmıyor.
2. ROLLER VE PROFİLLER
   ENGEL roller/web-gelistirici.json: cekirdek: gsap-core
3. REGISTRY ...      4. ÇIPLAK AD DEVRİ ...      5. YILDIZ VE LİSTE ...      6. KARTLAR, KONULAR, KAYIT DOSYALARI ...
KARAR: ENGEL (1) · DİKKAT (3)        |  KARAR: HAZIR (engel ve dikkat yok)  |  KARAR: REDDEDİLDİ (program)
ADIMLAR (sırayla; kullanıcı onayı olmadan 2. adımdan öteye geçme): ...
GERİ ALMA ...
```
### 4.3 Rollback block (printed by `kaynak-cikar.py` and copied in rehber/03 G)
```
GERİ ALMA
 - Commit atılmadıysa: değişiklikleri kullanıcıya göster; onaylarsa: git restore --source=HEAD --staged --worktree .   sonra: git clean -n -d arsiv   (listeyi göster; silmeden önce yine sor)
 - Commit atıldıysa (push edilse de edilmese de): git revert <commit>   (tek commit; merge commit ise -m 1). kaynaklar.json, registry, arşiv, katalog, roller geri gelir. Push yalnız kullanıcı isterse.
 - Projeden kaldırılan skiller: python3 araclar/skill-ekle.py "<yol>" --geri-al <yedek adı>   (kaldırma çıktısı yedek adını yazdı)
 - GitHub yıldız/liste (git revert kapsamaz): python3 araclar/listeye-ekle.py <owner/ad>   (kullanıcı onayıyla)
```
### 4.4 `rehber/03-yeni-skill-ekleme.md`: new top part (replaces `:1-12` header, keep the A) title)
```
# 03 — Sonradan Yeni Skill / Repo Ekleme, Çıkarma, Kayıp Kaynak

> Karar kutusu (ilk iş): repoda SKILL.md yok ve kendi sürümü/kurulumu olan çalışan bir program ise -> rehber/11 (programlar.json).
> SKILL.md var -> bu rehber. İkisi birden (ör. HyperFrames, OpenMontage) -> ikisi de: burada kaynak kaydı (alan "program": "<ad>"), rehber/11'de program kartı; kartlar birbirine bağlanır.
> Tek ekleme sırası aşağıdaki A1..A9'dur; promptlar/07 aynı sırayı kullanır. Onaysız hiçbir kaynak eklenmez, çıkarılmaz; GitHub'a hiçbir şey kendiliğinden yazılmaz.
```
### 4.5 `rehber/03` A) the single add order, 9 steps (replaces `:14-76` flow and `:84-88`)
Each step: what, command, stop condition. A2 keeps the existing texts of old step 1 (conflict check, ücret, projeden bağımsız değerlendirme); A4 keeps the tip table, alanlar, kategori kuralı.
```
A1  Başlangıç ve bul. `git status --short` BOŞ olmalı; değilse DUR ve kullanıcıya söyle (başka işin değişiklikleri yeni kaynak commitine karışır).
    `python3 araclar/dogrula.py | tail -3` -> "N skill · H hata · U uyarı" satırını not et (A7 ile karşılaştırılacak).
    `python3 araclar/github-skill-listesi.py` (YENİ / AD DEĞİŞMİŞ) ve `python3 araclar/github-trend.py --aday`. AD DEĞİŞMİŞ yeni kaynak DEĞİLDİR (rehber/09 'Repo adı değişirse').
    Karar kutusu (yukarıda): skill mi, program mı, ikisi mi. Aday kararı: bölüm F.
A2  İncele, tablo yap (kullanıcıya gösterilecek): ne yapıyor, kaç SKILL.md ve nerede (gh api ... git/trees), LİSANS (lisans_riskli: belirtilmemiş / NOASSERTION /
    AGPL / ticari-olmayan ise tabloya kırmızı yaz), son güncelleme, ücret, trend, çakışma kontrolü (aynı ad / aynı iş / repo içi çoklu sürüm / aynı adlı kendi skill;
    genel klasörler boşaltıldıktan sonra "global'de aynı ad" maddesi anlamsızdır, boşalmadan önce hâlâ bak), GÜVENLİK OKUMASI (en az bir SKILL.md ve her betik
    klasörünün örneği: ağdan kod indirip çalıştırma, proje dışına yazma, gizli bilgi okuma, `curl | sh`), UYUM (Claude'a özgü araç ister mi: TodoWrite, Task aracı...;
    Codex/Antigravity'de çalışmayacaksa tabloya yaz). Repo sabit commit'i: `gh api repos/OWNER/REPO/commits/HEAD --jq .sha` (A4'te onay.commit olacak).
A3  Kullanıcıya göster, ONAY bekle. Soru (aynen): "Bu kaynağı kütüphaneye ekleyeyim mi? Repo: <owner/ad>, <N> skill, lisans <L>, ücret <u>, tip <T>, commit <sha7>. Lisans/yol/güvenlik notları: <özet>."
    Cevap "evet" olmadan A4'e geçme. Lisans riskliyse ayrıca sor: "Lisans <L>; yine de ekleyeyim mi?" ve cevabı onay.lisans_onay'a yaz.
A4  Kayıt (yalnız onaydan sonra). kaynaklar.json -> repolar: tip, oncelik, gerekirse dahil/haric/bagimlilik/kimlik + ONAY KAYDI:
      "eklendi": "YYYY-AA-GG",
      "onay": {"kim": "kullanıcı", "tarih": "YYYY-AA-GG", "oturum": "<kısa not>", "commit": "<A2'deki 40 haneli sha>",
               "lisans_onay": "<yalnız riskli lisansta: kullanıcının gerekçesi>", "yol_onay": "<yalnız A5 yol kapısı takılırsa>",
               "guvenlik_notu": "<A2 güvenlik okumasının 1 cümlelik sonucu>"}
    + gerekirse ucret-siniflandirma.json, kategori-kurallari.json, T5/T6 kart/satır (aşağıdaki mevcut kurallar). Onay kaydında PROJE ADI yazma (kural 6).
A5  Ön kontrol (hepsi okuma/indirme; arşive henüz yazmaz): `python3 araclar/gelistirici-bilgisi.py --repo owner/ad`;
    `python3 araclar/kaynak-cek.py --repo owner/ad` -> çıktıda `owner/ad ... skill=N` satırı ve `Toplam kayıt: N` olmalı (0 ise repo adı ya da tip yanlıştır, DUR);
    `python3 araclar/yol-tara.py --repo owner/ad --siki` -> "YOL KAPISI: GEÇTİ" olmalı. TAKILDI ise satırları kullanıcıya göster; yol-istisnalari.json yalnız öğretici
    metin için, "kabul" ancak kullanıcı raporu gördükten sonra; ya da kullanıcının gerekçesini onay.yol_onay'a yaz.
A6  Arşive yerleştir ve denetle: `python3 araclar/arsiv-yerlestir.py` (güvenlik kilidi: başka skill kaybolursa durur; KİMLİK/KİMLİK DEVRİ satırlarını kullanıcıya göster);
    `python3 araclar/kapsam-denetimi.py` (0 sorun); `python3 araclar/katalog-uret.py`; `python3 araclar/skill-readme.py` (prompt 11 uyumu paragrafı geçerli).
A7  Skill testi ve doğrulama: yeni kimlikler: `python3 -c "import json;print(' '.join(s['id'] for s in json.load(open('registry.json'))['skiller'] if s['repo'].lower()=='owner/ad'))"`
    sonra `python3 araclar/skill-calistir.py --skill <o kimlikler>` (HATA varsa: yama, bölüm 'Çalışmayan skill'; TEST_RAPORU.md bu çağrıda yeniden yazılmaz);
    `python3 araclar/dogrula.py --github` (0 hata; uyarı sayısı A1'dekinden fazla olmamalı; fazlasını kullanıcıya göster).
A8  İncele, test, commit: sonuçları incele (KATALOG, tercih/alternatif, roller, rehber/07 inceleme kartları); `python3 araclar/test.py`; `python3 araclar/duman-testi.py`;
    kullanıcıya özet + `git status --short` göster; sonra TEK commit: `git add -A && git add -f arsiv && git commit -m "Yeni kaynak: owner/ad"`.
A9  GitHub (git commitinden SONRA; kullanıcı zaten listeye koyduysa HİÇBİR ŞEY yapma): repo "Yapay Zeka Skillleri" listesinde değilse önce kullanıcıdan "evet" al, sonra
    `printf 'e\n' | python3 araclar/listeye-ekle.py owner/ad` (araç hedef listeyi ve korunan listeleri gösterir, kendi onay sorusunu sorar). `github-skill-listesi.py --ekle/--duzenle` KULLANMA
    (onay sormadan GitHub'a yazar). Aday kararını deftere yaz: `python3 araclar/konu-takip.py --karar owner/ad eklendi "neden"`. Push yalnız kullanıcı isterse.
```
### 4.6 `rehber/03` D–H (replace `:146-160`; keep D0 content; new text starts at `## D)`, `## E)` kayıp kaynak, `## F)` aday kararları, `## G)` geri alma, `## H)` emekli)
```
## D) Kaynak / skill KALDIRMAK (azaltma)
Ölçüt (hepsi birlikte): GitHub güveni düşük (D) ve yıldız az ve işlevi daha iyi bir kaynaktan karşılanıyor ve hiçbir role/profile bağlı değil.
Benzersiz işi olan düşük güvenli kaynak tutulur.
D0  Önce içerik (zorunlu): [eski 0. madde aynen: her alt klasörden örnek SKILL.md OKU ...].
D1  Etki raporu: `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru` (ya da `--skill <kimlik> --kuru`; `--github` eklenirse repo/yıldız durumunu okur).
    Raporu kullanıcıya göster: engeller (role/profile bağlı), projeler, dikkatler. Onay al. (Eski `find ~ -path '*/kilit.json'` aramasını KULLANMA.)
D2  Aracın yazdığı ADIMLAR'ı sırayla uygula: roller/profiller -> projelerde `skill-ekle.py <proje> --kaldir` (her proje için ayrı onay) -> kaynaklar.json
    (tüm repo: `repolar`dan sil + `arsivden_cikarilan_repolar`a ekle; tek skill: `arsivden_cikarilanlar`a ekle; kayda `onay` ve `geri_alma` yaz)
    -> `arsiv-yerlestir.py` -> `kapsam-denetimi.py` -> `katalog-uret.py` -> `dogrula.py` -> `test.py` -> TEK commit "Kaynak çıkarıldı: owner/ad".
    `--kayba-izin-ver` kullanma. `konu-takip.py --karar ... reddedildi` GEREKMEZ: çıkarılan repolar aday olarak bir daha çıkmaz.
D3  GitHub tarafı (git dışı; kullanıcının kararı): yıldız ve liste üyeliği kalsın mı? Kaldırılacaksa onayla: `gh api -X DELETE user/starred/<owner/ad>` (listeden çıkarma GitHub sayfasından).
D4  Geri alma: bölüm G'deki "çıkarmayı geri al" (git revert + listeye-ekle.py).
Program kaydı olan ("program" alanlı) kaynak bu yolla çıkarılmaz: rehber/11 'Programı çıkarma'.

## H) Emekli etmek (kaldırmadan)
Emekli = skill kütüphanede ve projelerde kalır, yerine geçeni önerilir. Kaynakta silinen skill `kaynak_durumu: kaynakta-kaldirildi`, silinen repo
`kayip` olarak OTOMATİK emekli olur. Elle emekli: registry inceleme alanı `ortusme_rolu: emekli` (rehber/07 inceleme akışı) + rollerde yerine geçeni koy.
Projeler çalışmaya devam eder; `skill-ekle.py <proje> --durum` "EMEKLİ" der.

## E) Kayıp kaynak (repo 404 oldu, private oldu, silindi)
E1  Teyit: `python3 araclar/kaynak-cikar.py --repo owner/ad --kuru --github` ya da `gh api repos/owner/ad --jq .full_name`. `gh auth status` önce: oturum/ağ sorunu
    404 değildir. Yeni ad dönerse (full_name farklı) bu KAYIP değil taşınmadır: rehber/09 'Repo adı değişirse'.
E2  Etki: aynı raporu oku (projeler, roller). Projeler ETKİLENMEZ ama `--durum` "EMEKLİ: KAYNAK KAYIP" der; yenilenmez.
E3  Karar (kullanıcıya sor): (a) arşiv kopyası kalsın: kaynaklar.json'da kaydı SİLME; `"tip": "KAYIP"`, `"kayip_tarihi": "YYYY-AA-GG"` yaz ve `not`a
    "repo GitHub'da yok (404), <tarih>" ekle (bu işaretleme ELLE yapılır; otomatik `--kayip-isaretle` yoktur, kullanıcı kararıdır). Kaydı silmek güvenlik kilidini tetikler.
    (b) yerine geçeni var: rol/profilleri güncelle, sonra (a). (c) bilerek tamamen çıkar: bölüm D.
    Aylık güncelleme KAYIP olmayan ama o an erişilemeyen kaynağı `kaynak-cek.py --atla` ile atlar ve raporlar (arşiv kopyası korunur); kalıcıysa bu bölümle KAYIP yap.
E4  `kapsam-denetimi.py`, `dogrula.py`, commit. KAYIP kaynak aylık sorgulanmaz: ara sıra `kaynak-cikar.py --repo <kayıp> --kuru --github` ile geri geldi mi bak;
    geri geldiyse `tip`'i eski değerine döndür, `kayip_tarihi`ni sil, `kaynak-cek.py --repo` + `arsiv-yerlestir.py`.

## F) Aday kararları (trend, popüler, konu takibi)
Üç araç aynı defteri okur: `konu-takip.json` (`degerlendirilen`, `izlenen`). Kararı HER ZAMAN şununla yaz: `python3 araclar/konu-takip.py --karar owner/ad <karar> "neden"`
(`populer-tarama.py --karar` KULLANMA: `izle` kararını sonsuza kadar gizler).
| Karar | Anlamı | Raporlarda |
|---|---|---|
| eklendi | kütüphaneye eklendi (A4'ten sonra yaz) | aday olarak bir daha çıkmaz |
| reddedildi | eklenmeyecek | aday olarak bir daha çıkmaz (yeniden açmak kullanıcı kararı) |
| izle | şimdilik değil; durum değişirse bak | konu-takip.py raporunda "İzlenenler" bölümünde; 90 gün sonra "zamanı geldi" |
Karar bekleyen sayısı ve en çok 5 aday adı: `python3 araclar/konu-takip.py --bekleyenler` (tarama yapmaz, ağ kullanmaz, dosya yazmaz; üç kaynağı birden özetler).
Karar verilince HEMEN `--karar` yaz. Kütüphaneden çıkarılan repo ayrıca karar gerektirmez. Kararı kullanıcı verir; ajan tek başına karar yazmaz.

## G) Eklemeyi geri al / çıkarmayı geri al
- Commit atılmadıysa: `git status --short` göster; kullanıcı onaylarsa `git restore --source=HEAD --staged --worktree .`, sonra `git clean -n -d arsiv` ile izlenmeyen yeni arşiv klasörlerini göster ve silmeden önce sor.
- Commit atıldıysa: `git revert <commit>` (tek commit; merge commit ise `-m 1`). Kaynak kaydı, arşiv, registry, katalog, ücret/kategori kuralı, T5/T6 kartı tek hamlede geri gelir.
- GitHub (git revert kapsamaz): bu akış repoyu yıldızlayıp listeye ekledi ise, kullanıcıya söyle; kaldırmayı kullanıcı kendisi yapar ya da onayıyla `gh api -X DELETE user/starred/<owner/ad>`
  (liste üyeliği GitHub sayfasından). Kullanıcı kendisi koyduysa DOKUNMA. Çıkarmayı geri alırken yıldız/liste: `python3 araclar/listeye-ekle.py owner/ad` (kullanıcı onayıyla).
```
Also in `rehber/03` `Alanlar` list add: `eklendi`, `onay`, `kayip_tarihi` (one line each as above).

### 4.7 `rehber/09` edits (exact)
- `:38-47` section "Repo adı değişirse" step 1: `python3 araclar/github-skill-listesi.py` raporlar (yalnız `yeni` ve `eksik` birlikte doluyken) ve `python3 araclar/kaynak-cikar.py --repo <eski ad> --kuru --github` `AD DEĞİŞMİŞ` der.
- step 3 list: `registry.json`, `kategori-kurallari.json`, `ucret-siniflandirma.json`, `gelistiriciler.json`, `trend.json` + ADD `programlar.json` (kartın `repo`su), `konu-takip.json` (`konular.*.repolar`, `degerlendirilen`, `izlenen` anahtarları), `notlar/referans/*.md` (T5/T6 kart/satır). `yol-istisnalari.json` ve `projeler.json` el değmez (anahtarlar `eski_adlar` ile eşlenir / proje→skill kimliği tutar). Hangi dosyada kaç satır geçtiği: `kaynak-cikar.py --repo <eski ad> --kuru`.
- new section at the end `## Kaynak çıkarılırsa` : "Çıkarılan kaynağın `ad_devral` ile devraldığı çıplak ad boşalır; eski sahibin kimliği `ad@kaynak` olarak kalır (kimlikler değişmez). Çıkarmadan sonra `skill-ekle.py --listele --ara <ad>` ile tercihin kimde olduğuna bak; istenmiyorsa durum_elle ile sabitle. `ad_devral` devirden sonra kayıtta kalır (zararsız); kayıt çıkarılınca birlikte gider. Bilerek devir geri alınacaksa devralanın `ad_devral` girdisini sil ve eski kaydı `durum_elle` ile tercih yap (kullanıcı onayı)."
### 4.8 `promptlar/07-yeni-skill-reposu-ekle.md` (full new text; outer fence is four backticks, the file itself contains a three-backtick `kopyala` block)
````
# 07 — Yeni Skill Reposunu Kütüphaneye Ekle ("kontrol et")

**Ne zaman:** GitHub'da yeni bir skill reposunu yıldızlayıp **"Yapay Zeka Skillleri"** listesine ekledin.
**Nerede:** Claude Code, Codex, Antigravity ya da başka bir ajan, `~/Documents/SkillKutuphanesi` klasöründe. Tek adım sırası: `rehber/03-yeni-skill-ekleme.md` A1..A9.

```kopyala
Yapay Zeka Skillleri listeme yeni repolar ekledim, kontrol et ve kütüphaneye dahil et.
~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/03-yeni-skill-ekleme.md'yi oku. rehber/03'teki A1..A9 sırasını ATLAMADAN, aynı sırayla uygula:

1. A1: git status temiz mi (değilse dur ve söyle); dogrula başlangıç sayısını not et; python3 araclar/github-skill-listesi.py (YENİ / AD DEĞİŞMİŞ) ve
   python3 araclar/github-trend.py --aday. AD DEĞİŞMİŞ yeni kaynak değildir (rehber/09). Program mı skill mi karar kutusuna bak.
2. A2: Her yeni repo için incele ve bana tablo halinde göster: ne yapıyor, kaç SKILL.md ve nerede, lisans, son güncelleme,
   ÜCRET (ücretli = ücret ödemeden HİÇ kullanılamıyor; ücretli servis sadece bir seçenekse ya da ücretsiz katman varsa kısmen), GitHub trend durumu,
   güvenlik okuması (proje dışına yazma, ağdan kod indirme), Claude'a özgü araç gereksinimi, tip (T1–T6) ve kategori önerisi, ve program mı skill mı.
   ÇAKIŞMA KONTROLÜ (zorunlu): aynı ADLI skill (registry.json 'ad'; içerik aynı mı farklı mı), aynı İŞİ yapan skill (ortusme_grubu; birincil/tamamlayıcı/alternatif),
   repo içinde aynı adlı birden fazla SKILL.md, aynı adlı kendi skill'in (global klasörler henüz boşaltılmadıysa onlar da).
   Kural: çıplak ad kendiliğinden el değiştirmez; yeni gelen ad@kaynak olur. Ad aynı, iş farklıysa eski kaydı durum_elle ile tercih sabitle ve iki kayda fark notu yaz.
   Çıplak adı bilerek devretmek (ad_devral) için önce python3 araclar/proje-kullanimi.py --skill <ad> ve rolleri kontrol et, bana sor.
   Değerlendirmeyi yalnızca repo/skill'in kendi niteliğiyle yap; notlara ve öncelik gerekçesine proje adı ya da "şu projeye uyar" yazma.
3. A3: Bulgularını ve kararını gerekçeleriyle göster. Onayımı bekle. Lisans belirtilmemiş / NOASSERTION / AGPL ise ayrıca sor.
4. Onaylarsam A4-A8'i rehber/03'teki sırayla yap (kayıt + onay kaydı, gelistirici-bilgisi, kaynak-cek --repo, yol-tara --repo --siki, arsiv-yerlestir,
   kapsam-denetimi, katalog-uret, skill-readme, skill-calistir --skill <yeni kimlikler>, dogrula --github, inceleme, test, duman-testi, tek commit).
   Her adımda rehberdeki durma koşullarına uy. Eski kayıtların kategori/durum/ücret farkını git HEAD'deki registry ile karşılaştır; rollerde kullanılan
   bir adın tercihi değiştiyse (aynı ad, farklı iş) durum_elle ile sabitle.
5. A8: Yeni skilleri rehber/07-kategori-inceleme.md'ye göre incele (ozet_tr, kullanım, teknoloji, kalite, örtüşme rolü, ücret notu); gerekirse rollere/profillere ekle
   (ücretli skill çekirdeğe ancak gerekçeyle).
6. A9: GitHub'a yazma yalnız repo listede değilse ve bana sorduktan sonra: listeye-ekle.py. github-skill-listesi.py --ekle/--duzenle kullanma. Push yapma.
7. Özet ver: eklenen skiller, kararlar (tercih/alternatif/örtüşme), ücret ve lisans durumu, etkilenen roller, commit, geri alma komutu (git revert <commit>).

Aday kararı verdiğim repoları hemen konu-takip.py --karar ile deftere yaz (eklendi / reddedildi / izle). Kurallar: global skill klasörlerine dokunma,
arsiv/ altındaki skill dosyalarını elle düzenleme, push yapma, onaysız ekleme yapma.
```
````
### 4.9 `promptlar/14-kaynak-cikar.md` (full text; outer fence is four backticks)
````
# 14 — Kaynağı / Skili Kütüphaneden Çıkar, Kayıp Kaynağı Ele Al

**Ne zaman:** Bir skill reposunu ya da tek bir skili kütüphaneden çıkarmak, ya da GitHub'da kaybolan bir kaynağı ele almak istediğinde.
**Nerede:** herhangi bir ajan, `~/Documents/SkillKutuphanesi` klasöründe. Adımlar: `rehber/03-yeni-skill-ekleme.md` D, E, G, H.

```kopyala
Şu kaynağı/skili kütüphaneden çıkarmak istiyorum: <owner/ad ya da skill kimliği>. (Kayıpsa: şu kaynak GitHub'da kayboldu: <owner/ad>.)
~/Documents/SkillKutuphanesi/AGENTS.md ve rehber/03-yeni-skill-ekleme.md (D ve E bölümleri) dosyasını oku ve atlamadan uygula:

1. git status --short boş olmalı; değilse dur ve bana söyle.
2. python3 araclar/kaynak-cikar.py --repo <owner/ad> --kuru --github   (tek skill için --skill <kimlik> --kuru). Çıktıyı OLDUĞU GİBİ bana göster:
   engeller, projeler, roller/profiller, dikkatler. Bu araç yalnız okur.
3. D0: gerekçeyi içerikle doğrula (örnek SKILL.md oku; "daha iyi alternatif" diyorsan onu da oku). Onayımı bekle. Programa bağlı ("program" alanlı) kaynakta dur ve rehber/11'e bak.
4. Onaylarsam aracın yazdığı ADIMLAR'ı sırayla uygula; her projeden skill kaldırmak için ayrıca bana sor. Kaynak kayıpsa önce E bölümü: kaydı silme, tip'i KAYIP yap.
5. kapsam-denetimi, dogrula, test sonuçlarını göster; tek commit at; commit numarasını ve geri alma komutunu (git revert <commit>) söyle.
6. GitHub yıldızı/listesini bana sor; kendiliğinden kaldırma. Push yapma.
Kurallar: global skill klasörlerine dokunma, arsiv/ altındaki dosyaları elle düzenleme, --kayba-izin-ver kullanma, proje adlarını kayıt dosyalarına yazma.
```
````
### 4.10 `--help` / messages in other tools (exact)
- yol-tara: `--siki   --repo/--skill ile kapı gibi çalışır: çözülemez yol ya da genele-yazabilir/istisna-eskidi UYARI'sı varsa çıkış 1 ('YOL KAPISI: TAKILDI')`. Without `--siki` unchanged: "Çıkış kodu HER ZAMAN 0" docstring gets `(--siki hariç)`.
- kaynak-cek: `--atla owner/ad[,owner/ad]   bu kaynaklar için indirme ve repo ağacı okuması yapılmaz; arşiv kopyası korunur (erişilemeyen tek kaynak aylık güncellemeyi durdurmasın)`; message `UYARI: <repo> atlandı (arşiv kopyası korunur)`.
- konu-takip `--karar` errors as in 3.6; `--bekleyenler` help `kararı bekleyen adayları (konu takibi, trend, popüler) ve vadesi gelen izlenenleri özetler: tarama yapmaz, ağ kullanmaz, dosya yazmaz`.

--------------------------------------------------------------------------------------------------------------------------

## 5 Tests: `araclar/testler/test_p7-kaynak-yasam.py`

Rules: runnable alone (`python3 araclar/testler/test_p7-kaynak-yasam.py`); temp directories and fake data only (no real home, no real `registry.json`, no real `konu-takip.json`); no network, no `gh`, no `tara()`/`kod_ara()`/`repo_ara()`; last line `N/N test geçti`; exit 0/1. Harness traps (from the code read):
- Tools import constants by name: patch the TOOL module attributes (`kt.DURUM`, `kt.RAPOR`, `kt.KAYNAKLAR`, `kc.KAYNAKLAR`, `kc.GECICI`), not `ortak`'s.
- `ortak._TAKMA_ADLAR = None` before every test that touches `repo_guncel` (otherwise it reads the REAL `kaynaklar.json`); also patch `ortak.KAYNAKLAR`.
- `gsl.gql`, `subprocess.run`, `input` are replaced by fakes that record calls (case on `listeye-ekle.py`); `kc.repo_agaci` is replaced by a stub that raises `AssertionError` when called for an atlanan repo.
- Load tools with `importlib.util.spec_from_file_location` from the REAL `araclar/` folder; the library root for `kaynak-cikar.py` is a temp tree built by a `kur_kok()` helper (fake `kaynaklar.json`, `registry.json`, `roller/`, `profiller/`, `konu-takip.json`, `trend.json`, `projeler.json`, `notlar/referans/`, and a temp `projeler.json` with absolute temp `tarama_kokleri`). `kaynak-cikar.py` loads the REAL `proje-kullanimi.py` from the real `araclar/` (a copy in the temp tree would lose its `ortak` import and read the real `AYAR`).
- `konu-takip.py --bekleyenler` tests call the function with temp paths (injected `kok`/path arguments), never `main()` against the real files.

Cases (target 34):
kaynak-cikar
1. repo mode full report: temp tree with 1 T1 record, 3 registry skills, 1 role (`cekirdek` has one id), 1 profile (`ek_skiller`), a `konu-takip.json` hit, a T6 card line, one fake project lock -> JSON has the role/profile/project/kayit rows; `karar == "engel"`.
2. role matched by bare `ad` when the skill is `tercih`; NOT matched when the skill is `alternatif` and the id differs.
3. step order: JSON `adimlar` numbers 0..12 appear in the fixed order; conditional steps (2,3,5) disappear when no hit; step 4 text differs between repo and skill mode (`arsivden_cikarilan_repolar` vs `arsivden_cikarilanlar`) and never contains `--kayba-izin-ver` as an instruction.
4. ledger snippet: valid JSON; skill mode `son_commit` equals the registry `commit`; `tarih` equals the injected `bugun`; `neden` placeholder when `--neden` absent, real text when given.
5. programme guard: record with `"program"` -> `karar == "reddedildi"`, no steps, text contains `rehber/11` and `Programı çıkarma`; exit 0 without `--siki`, 1 with `--siki`.
6. no `--kuru` -> exit 2 and the message `Bu sürümde yalnız --kuru var`; `--uygula` -> exit 2; neither `--repo` nor `--skill` -> exit 2.
7. unknown target -> exit 2; ambiguous bare `ad` (tercih + `ad@x`) -> exit 2 and lists ids.
8. no project on machine (`projeleri_bul` empty) -> text `etki BİLİNMİYOR`, `proje_bilgisi == "yok"`, verdict is `dikkat`, never `hazir`; project exists but none uses the source -> `Hiçbir projede kullanılmıyor.`, `proje_bilgisi == "var"`.
9. old repo name (`eski_adlar`) and upper-case argument resolve to the same canonical repo.
10. `ad_devral` on the target record and the former holder (`ad@eski`) are reported; another record's `ad_devral` naming a target `ad` is reported.
11. `tip == "KAYIP"` record is reported (`kayip: true`) and the removal steps still print; a repo already in `arsivden_cikarilan_repolar` -> `Zaten çıkarılmış`, verdict `yok`, exit 0.
12. orphan: registry skills present, no `kaynaklar.json` record -> note printed, no crash.
13. read-only invariant: recursive file hash/mtime listing of the temp tree before and after `rapor_uret` and `main` is identical; no new file created.
14. `--json` stdout is exactly one JSON line parseable by `json.loads` with all keys of the example.
15. `--github` with a fake `gh` runner (injected callable): 404 -> `kaynak kayıp`; different `full_name` -> `AD DEĞİŞMİŞ` and verdict note; runner error -> `okunamadı`, run succeeds.
konu-takip
16. `elenecekler`: includes `eski_adlar`, both `arsivden_cikarilan_repolar` item forms (str and dict), `degerlendirilen`, `izlenen`; all lowercase; `eleniyor` is case-insensitive.
17. `karar_uygula(izle)`: writes `izlenen` only, nothing into `degerlendirilen`; `izlenen_vadesi` due after 90 days (injected `bugun`).
18. `reddedildi -> izle` refused (error text mentions `REDDEDİLDİ`), ledger untouched; `eklendi -> reddedildi` refused; `reddedildi -> eklendi` allowed.
19. case-variant: ledger has `Owner/Repo`, command with `owner/repo` -> same key reused, still one entry.
20. bad repo pattern and bad karar -> error, ledger untouched; unknown repo -> warning but written; library repo + `reddedildi` -> error.
21. `rapor()` (patched `kt.DURUM/RAPOR/KAYNAKLAR`): an `izlenen` repo is NOT in the topic candidate table but IS in the `İzlenenler` section; due marker `⏰ zamanı geldi` only past 90 days; a rejected repo in a different letter case is hidden (old case-sensitive behaviour would show it).
22. `aday_mi` is the single predicate: the three former code sites (report table, summary count, `main()` print) give the same count for the same data.
23. `--bekleyenler --ozet-json`: stdout is ONE JSON object `{arac,durum,satirlar,karar_bekleyen}`; `durum` `dikkat` with a focused candidate, a due izlenen, or a stale (>45 days) source, `temiz` otherwise, `sorun` with unreadable `konu-takip.json`; nothing else printed; no file written; exit 0, and 1 only with `--siki` + `sorun`.
24. `--bekleyenler` triage: 8 fake candidates in one source -> `karar_bekleyen` has at most 5 names from it, the total (8) is in `satirlar`; highest ★ first.
25. `--bekleyenler` trend source: `son_liste` repos that are rejected/izlenen/removed or have cached `skill == 0` are not counted; missing `trend.json` or missing populer report -> `dikkat` with `rapor yok`, not `sorun`; a populer candidate decided after the scan (added to the ledger) disappears; header date older than 45 days -> `dikkat`; heading missing -> `dikkat`.
kaynak-cek
26. `atla_kumesi`: comma list with spaces and empties, upper-case input, an OLD repo name (via a fake `cevir`) -> same canonical lower-case set; a name with no T1-T4 record is returned in `tanimsiz`.
27. `--atla` in `main()` (temp `kc.KAYNAKLAR` with one T1 record and one T5 record, temp `kc.GECICI`, `kc.repo_agaci` stub that raises): the atlanan T1 repo -> `UYARI: <repo> atlandı (arşiv kopyası korunur)` printed once, `repo_agaci` never called, `manifest["kayitlar"]` has no record of it, exit 0 (no `SystemExit`); two records of the same repo -> one UYARI.
28. `--atla` with an unknown repo -> `T1-T4 kaydı yok; yok sayıldı` printed, exit 0; without `--atla` the code path is the old one (a stub `repo_agaci` raising `GhBulunamadi` still ends in `SystemExit` with the old `HATA: ... erişilemiyor` text).
29. `kaynak-cek.py --help` (subprocess, exit 0) contains `--atla`.
30. `lisans_riskli`: True for `belirtilmemiş, NOASSERTION, yok, AGPL-3.0, CC-BY-NC-4.0, PolyForm-Noncommercial-1.0.0`; False for `MIT, Apache-2.0, BSD-3-Clause`.
yol-tara
31. default exit codes unchanged: `--skill` without value and `--bogus` -> 0; unknown skill -> 0 and writes nothing (in-process with temp `KOK`).
32. `--siki --repo` with a fake skill that has a `cozulemez` finding -> prints `YOL KAPISI: TAKILDI` and returns 1; same data without `--siki` returns 0; a clean skill -> `GEÇTİ` and 0; a skill covered by a valid exception -> `GEÇTİ`; repo found nowhere -> 1; `--siki` alone -> 2; an exception inside the scan under `--siki` -> 1. `kapi_kontrol()` returns `(sorunlar, taranan, hata)` with the documented codes (`genele-yazabilir` UYARI counts, `istisna-eskidi` counts, plain BİLGİ does not).
listeye-ekle
33. case fix: membership map keyed lowercase; argument `owner/Repo` for a repo listed as `Owner/repo` in a protected list keeps the protected list id in the mutation (old code dropped it); fakes for `listeler/gql/subprocess/input`.
documents
34. `rehber/03` and `promptlar/07` both contain every marker `A1`..`A9` in order (regex), neither contains `find ~ -path` nor `A17`, `rehber/03` contains `kaynak-cikar.py --repo`, `YOL KAPISI`; `promptlar/14-kaynak-cikar.md` exists and mentions `rehber/03` D/E; `kaynak-cikar.py --help` / `yol-tara.py --help` run (subprocess, exit 0) and mention `--kuru` / `--siki`.

--------------------------------------------------------------------------------------------------------------------------

## 6 Hand-off requests to other packages

### To P8 (integrator; owner of `dogrula.py`, `test.py`, `CLAUDE.md`, `AGENTS.md`, `README.md`, `promptlar/README.md`, `ortak.py`)
1. `araclar/test.py`: in the section P8 adds for `araclar/testler/`, include `test_p7-kaynak-yasam.py` (subprocess; exit code + last line `N/N test geçti`).
2. `dogrula.py` new checks. **Corrected after review: EVERY check below is UYARI, never HATA.** Reason: `arsiv-guncelle.py` `_uygula` and `--birlestir` run `dogrula.py` and a HATA makes them `git reset --hard` the branch (`arsiv-guncelle.py:243-268` region); a new HATA on the 181 existing records would silently roll back the monthly chain. Raising any of these to HATA is a separate decision that needs the user's own approval later.
   - **G-TIP (schema, all records): UYARI only.** `tip` not in `T1..T6, KAYIP, EMEKLI` (and any new type P6 defines; read the allowed set from one constant) -> UYARI; `repo` not `owner/ad` -> UYARI; `oncelik` present and not an int -> UYARI; unknown key outside `repo, tip, oncelik, not, haric, dahil, dahil_degil, bagimlilik, kimlik, dosya_haric, program, kok_dosyalari, eski_adlar, ad_devral, eklendi, onay, kayip_tarihi` -> UYARI.
   - **"New record" definition** (used by the four checks below): a `repolar` entry for which NEITHER its `repo` NOR any of its `eski_adlar` matches (case-insensitively) the `repo` or any `eski_adlar` of any record in `git show HEAD:kaynaklar.json` (a rehber/09 rename is NOT new). If git cannot read HEAD (fresh repo, other machine) skip silently. The 181 existing records are NEVER new under any condition (no baseline backfill). The check therefore fires only during an add, before the commit.
   - **G-ONAY (UYARI, new record only):** missing `eklendi` (`YYYY-AA-GG`) or missing `onay` dict with `kim`, `tarih`, `commit` (40 hex) -> `UYARI: kaynak kaydında onay yok: <repo> (rehber/03 A4)`.
   - **G-LISANS (UYARI, new record only):** the repo's registry skills have a `lisans` for which `lisans_riskli()` (load `kaynak-cek.py` by importlib; side-effect free) is True and `onay.lisans_onay` is empty -> `UYARI: lisans <L> için onay.lisans_onay yok: <repo>`.
   - **G-YOL (UYARI, new record only):** `yol-tara.py` `kapi_kontrol(repo=<repo>, skiller=<dogrula's loaded list>)` (importlib; the 22 MB registry is not reloaded) returns problems and `onay.yol_onay` is empty -> `UYARI: yol kapısı takıldı: <repo>: <ilk sorun>`; `hata` not None -> `UYARI: yol kapısı çalışmadı`.
   - **G-ONAY-CIKAR (UYARI, new entry only):** a new entry (not in HEAD) in `arsivden_cikarilan_repolar` or `arsivden_cikarilanlar` without `onay{kim,tarih}`; `neden` containing `<NEDEN`; `arsivden_cikarilan_repolar` entry without `geri_alma`.
   - **G-KAYIP (UYARI):** `tip == "KAYIP"` without `kayip_tarihi`. P7's implementation adds `kayip_tarihi` to the existing record (section 7) so the first run is clean; P8's known-warning list needs no entry for it.
   - The existing rule-6 scan (`dogrula.py:259-283`) already covers project names inside `onay` text; nothing new needed.
   - **P8 test must include** (new case, mandatory): a `kaynaklar.json` with a record of `tip = "EMEKLI"` and one with an unknown key (and an `oncelik` that is a string) passes the monthly path: `dogrula.py` exit code 0 and only UYARI lines (the monthly `arsiv-guncelle.py` `_uygula`/`--birlestir` must not roll back). Also: a renamed record (`repo` changed, old name in `eski_adlar`) is NOT new; a genuinely new repo without `onay` raises exactly one UYARI and no HATA.
   - `dogrula.py --siki` (exit 1 on any UYARI) as P8 already plans: P7's texts do NOT depend on it (A7 compares warning counts).
3. `CLAUDE.md` and `AGENTS.md` ("Bakım isteklerinde", identical bullets): add `- Kaynak/skill çıkarma, emekli, kayıp kaynak: python3 araclar/kaynak-cikar.py --repo owner/ad --kuru (yalnız okur: etki + sıralı adımlar + geri alma); onayla uygula. Ayrıntı: rehber/03 D-G, promptlar/14.` and `- Aday kararları: konu-takip.py --karar owner/ad eklendi|reddedildi|izle "neden" (populer-tarama.py --karar kullanma); bekleyenler: konu-takip.py --bekleyenler (üç kaynağı özetler).` Fix the "Yeni skill ekledim" bullet: `(…global'de farklı sürüm)` -> `(…aynı adlı kendi skill; genel klasörler boşaldıktan sonra global madde geçersiz)` and make it say `rehber/03 A1..A9 tek sıra; onay kaydı zorunlu`. `CLAUDE.md` change needs the user's approval (they decided P8 owns it).
4. `README.md`: tool table row for `kaynak-cikar.py` (`kaynak/skill çıkarma etki raporu (--kuru); sıralı adımlar + geri alma`); notes on the rows of `kaynak-cek.py` (`--atla`), `yol-tara.py` (`--siki`), `konu-takip.py` (`--bekleyenler`), `listeye-ekle.py` (küçük/büyük harf düzeltmesi). Order: the README row must exist when `kaynak-cikar.py` lands if any check lists every `araclar/*.py` (a grep of `test.py`/`dogrula.py`/`kapsam-denetimi.py` found none; the implementer re-checks).
5. `promptlar/README.md`: rows for `14-kaynak-cikar.md` (`Kaynağı/skili çıkar, kayıp kaynağı ele al; etki raporu + onaylı adımlar`) and update the row of `07` (`tek ekleme sırası rehber/03 A1..A9`).
6. Staleness UYARI in `dogrula.py` (B2): optional; the same data is produced by `konu-takip.py --bekleyenler --ozet-json` (45-day rule).
7. Optional later: move `konu-takip.elenecekler/eleniyor` into `ortak.py` (P7 keeps them in `konu-takip.py` to respect D5).
8. `araclar/duman-testi.py`: no P7 requirement. If P8 adds a smoke line: `python3 araclar/kaynak-cikar.py --repo <any library repo> --kuru --json` (exit 0, JSON parses), `python3 araclar/konu-takip.py --bekleyenler --ozet-json`, `python3 araclar/kaynak-cek.py --help | grep -- --atla`.
9. `notlar/kararlar.md` "Henüz sonuçlanmamış sorular" (B2 triage; the decision is the user's): `Aylık güncellemede en fazla kaç aday karara bağlanır? (öneri: 5; araç en çok 5 aday adı gösterir, toplam sayıyı ayrıca yazar.)`. Closed candidate decisions need no list there: a repo decided with `--karar` never returns (the ledger is `konu-takip.json`).
10. Not mine, noted for P8: `rehber/08-test-sureci.md` (one paragraph on `araclar/testler/test_<paket>.py`, last line `N/N test geçti`) and `promptlar/10-kutuphane-saglik-kontrolu.md` line 8 (old "44 güvenlik testi" count: delete the number) have no owner in any package list; P8 takes both.

### To P4 (monthly task, `arsiv-guncelle.py`, `aylik-ozet.py`, `rehber/02`, `promptlar/08`)
1. Candidate backlog: `aylik-ozet.py` runs ONE subprocess, `python3 araclar/konu-takip.py --bekleyenler --ozet-json` (offline, instant, no file written, D4 JSON shape; it already covers konu-takip, trend and populer, max 5 names per source, staleness 45 days). **`github-trend.py --bekleyenler` and `populer-tarama.py --bekleyenler` are NOT delivered (deferred); do not call them.** The monthly chain's own calls (`github-trend.py --aday`, `populer-tarama.py`, `konu-takip.py` without args) are unchanged.
2. `arsiv-guncelle.py` (B4 part left to P4): (a) **P4 USES `kaynak-cek.py --atla owner/ad[,owner/ad]`** (delivered in 3.2 K4: no download, no `repo_agaci`, `UYARI: <repo> atlandı (arşiv kopyası korunur)`, not added to `manifest["kayitlar"]`, exit 0 when the rest succeeded; `--help` shows `--atla`; without the flag the old stop at `:238-240` is unchanged). The KAYIP/unreachable stop `arsiv-guncelle.py:284-286` should skip the lost repo and record it. (b) write the line `AD DEĞİŞMİŞ: <eski> -> <yeni>` (from `repos/<repo>` `full_name`) and, for lost repos, the affected projects (`proje-kullanimi.py --repo` or `kaynak-cikar.py --repo <r> --kuru` text) into `notlar/guncelleme-gecmisi.md`. (c) **`--kayip-isaretle`: ertelendi; P7 does not implement it either.** Marking a source lost is the user's decision and stays the manual step in `rehber/03` E3 (field `kayip_tarihi`, `YYYY-AA-GG`). P4's spec line that calls it "P7's kaynak-cikar.py job" must say "ertelendi, P7 de uygulamıyor". (d) monthly: for `tip == KAYIP` records run `kaynak-cikar.py --repo <r> --kuru --github` (read-only) to notice a comeback; report a known lost source once per month at most (P4 decides how to remember it).
3. `rehber/02:124-126` (section 3b): wording "projeler etkilenmez" should say "projelerdeki kopya çalışır ama `--durum` EMEKLİ: KAYNAK KAYIP der (skill-ekle.py:1022,1437)"; point to `rehber/03` E. `rehber/02:42-48,152-153`: mention `--karar` meanings and `rehber/03` F.
4. `promptlar/08`: add the reminder that decisions go to the ledger immediately (`--karar`) and the "İzlenenler zamanı geldi" check (listed by `--bekleyenler`).

### To P5 (`proje-kullanimi.py`)
Keep stable: `projeleri_bul(ayar)`, `oku(ayar)` (dict keys `ad, yol, kilit, elle`), `kullanan_projeler(repolar, idler)`, constant `AYAR`; `kaynak-cikar.py` uses exactly `projeleri_bul` and `oku` (and `kilit["skiller"][ad]` keys `id, repo, kaynak_yol, commit, roller`). P5's `--yetim` is the monitoring counterpart of what P7's removal creates; P7 mentions only `skill-ekle.py --durum`.

### To P6 (programs)
`kaynak-cikar.py` refuses to produce steps for a `kaynaklar.json` record with `"program"` and points to `rehber/11` 'Programı çıkarma'. `rehber/03` carries the three-line programme/skill decision box; `rehber/11` should link back to `rehber/03` (decision box). Field `program` stays in P8's allowed key set.

### To P3 / P2 / P1
Nothing required.

------------------------------------------------------------------------------------------------------------------------

## 7 Needs the user's approval (at that time; this design approves nothing)

- Adding any source to the library (A3), including the licence question for risky licences (`onay.lisans_onay`) and every `yol_onay` / `kabul` exception.
- Removing any source or skill (D1): the impact report is shown first; removing a skill from each project (`skill-ekle.py --kaldir`) needs a separate yes per project; the GitHub un-star / list removal is the user's own decision (D3).
- Marking a source lost / back (E3, E4, manual) and retiring a skill (H).
- Every GitHub write (`listeye-ekle.py`): plan shown, the user says yes in chat, then the agent answers the tool's own `e` question. No push ever without the user asking (D12).
- Recording candidate decisions (`--karar`): the user decides `eklendi/reddedildi/izle`; the agent never decides alone.
- **One-time data edit (taken by P7 per the review decision):** add `"kayip_tarihi": "2026-11-10"` to the existing KAYIP record `J-DTurner/etsy-api-skill` in `kaynaklar.json` (date from its `not`: 404 on 2026-11-10). One field, no re-indent of the file (edit the line, do not `json_yaz` the file). Needs the user's approval; goes in the same commit as the P7 implementation or its own small commit.
- Edits to `CLAUDE.md` / `AGENTS.md` requested from P8 (user approval, as decided).
- Raising any P8 gate from UYARI to HATA (separate later decision).

------------------------------------------------------------------------------------------------------------------------

## 8 Deferred and why

| Item | Why deferred |
|---|---|
| Applying mode `kaynak-cikar.py --uygula` | See 3.1: removals are rare, the safe version (backups, dry-run, formatting of a 181-record JSON, role edits) costs more than it saves. Revisit at ~10 removals per quarter or after two wrong manual runs. `--kuru` is mandatory now so the future mode cannot change bare-call behaviour. |
| `kaynak-cek.py` K1 (resolve `--repo` before touching the manifest, exit 1 for unknown repo) and K3 (licence/commit/decision summary block) | K1 changes an existing exit-code path and K3 adds output; the review asked for the smallest set. Replaced by the A5 reading instruction (`skill=N`, `Toplam kayıt: N`). Design: pure helper `repo_kaydi_sec`, `repo_ozet_satirlari`; reuse when approved. |
| `github-skill-listesi.py` `--evet` / `--geri-al` / consent / snapshot, and `listeye-ekle.py` L2/L3 | Behaviour change (non-interactive `--ekle/--duzenle` would stop) that the user has not approved. Documented mitigation: `rehber/03` A9 names only `listeye-ekle.py`, never `--ekle/--duzenle`. Design (helpers `onay_al`, `yedek_yaz`, snapshot file under `.gecici/liste-yedek-*.json`, `--geri-al`) is only sketched here (helpers, snapshot file, flag names); it must be re-designed and approved before any implementation. |
| `github-trend.py` and `populer-tarama.py` restructuring (shared elimination, `İzlenenler` sections, `--bekleyenler`, `populer --karar` delegating to `konu-takip`) | They are steps of the monthly chain (`arsiv-guncelle.py:189-198`); changing them is a risk for little gain once `konu-takip.py --bekleyenler` already filters their candidates with the full ledger. The `populer --karar izle` hiding bug is closed by documentation (`rehber/03` F: never use it). |
| `--yeniden-ac` for rejected repos, `tekrar_bak` date for rejected repos | Reopening a rejected repo is rare; manual edit of `konu-takip.json` (user decision) is enough. |
| `--kayip-isaretle` (writes `kayip_tarihi`) | Marking a source lost is a user decision; the manual step in `rehber/03` E3 is valid. Neither P4 nor P7 implements it. |
| Bulk decision file (`--karar-dosya`) for the 320 `populer` candidates | The backlog is a triage-policy question (monthly cap N, user question in `notlar/kararlar.md`); individual validated `--karar` exists. |
| Program-candidate discovery (SKILL.md-less repos) | Network scans and the program taxonomy belong to P6/P4. |
| `paket-gerekli` and other `yol-tara` UYARI codes as gates | Only `cozulemez` plus `genele-yazabilir` / `istisna-eskidi` gate; the 125 UYARI-carrying skills include many legitimate `eklenti-koku` cases. |
| `ad_devral` lifecycle automation | Documented behaviour only (rehber/09 new section). |
| Backfilling `eklendi/onay` into the 181 legacy records | Not needed: the P8 gate compares with `git show HEAD`; the checks are UYARI. |
| Moving `elenecekler` into `ortak.py` | D5 forbids P7 editing `ortak.py`. |
| Content-security scanner for SKILL.md | A reading step (A2 "güvenlik okuması" + `onay.guvenlik_notu`) is added; an automated scanner is a separate design. |
| `kapsam-denetimi.py` re-polling KAYIP repos | Not a P7 file; covered by the monthly `kaynak-cikar.py --github` suggestion (P4 hand-off 2d). |
| `dogrula.py --siki`, GEMINI.md / other AI-tool files, Windows | P8 / P1; user decisions pending. |

------------------------------------------------------------------------------------------------------------------------

## 9 Risks and how the implementer verifies nothing existing broke

| Risk | Mitigation / check |
|---|---|
| `yol-tara.py` exit code contract (test.py:501-503, 519-520, arsiv-guncelle.py:201-203) | `--siki` is opt-in; without it no line of control flow changes. After editing: `python3 araclar/yol-tara.py --skill; echo $?` (0), `--bogus` (0), `--skill boyle-bir-skill-yok` (0) and `git status --short notlar/yol-denetimi.md` unchanged. (Do not run the full scan: it rewrites the report; unit tests cover it.) |
| `kaynak-cek.py --atla` touches the first lines of the loop of a monthly-chain tool | The flag defaults to empty; with an empty set the added `if` is never true, so the old path is identical (case 28 asserts the old `HATA: ... erişilemiyor` stop). `repo_guncel` import adds a cache read of `kaynaklar.json` only when `--atla` is given (the helper is called with an empty string otherwise and returns early without calling `cevir`). Do not run `kaynak-cek.py` for real (network, rewrites `.gecici`). |
| `konu-takip.py` report changes visibly | The 3 current `izlenen` repos (printful-mcp, vgv-ai-flutter-plugin, swiftui-autotest-skill) move from the candidate table to the new `İzlenenler` section; candidate counts in `notlar/konu-takip.md` drop by up to 3; 67 mixed-case ledger keys are now matched case-insensitively. Intended; mention it in the commit message. Verify through unit cases 21-22 only; do NOT run `konu-takip.py --rapor` (rewrites `konu-takip.json` and `notlar/konu-takip.md`; if run by accident, `git checkout -- konu-takip.json notlar/konu-takip.md`). `--bekleyenler` is safe to run. |
| `konu-takip.py` `tara()` is in the monthly chain | Only the membership test (`:80`) and the `bilinenler` signature change; unit case 22 and a read-only import test cover them. |
| `listeye-ekle.py` lower-case fix changes dict keys | Covered by case 33; `listeler()` in `gsl` is unchanged. Never run it for real during implementation (GitHub write). |
| `kaynak-cikar.py` loads the 22 MB registry | One `json.load` (about 1 s); the tests use a tiny fake registry. |
| `proje-kullanimi.py` API drift (P5) | `kaynak-cikar.py` uses only `projeleri_bul` and `oku`; cases 1/8 run against the REAL module with a temp `ayar`, so a signature change breaks the test immediately. |
| `ortak._TAKMA_ADLAR` cache reading the real file in tests | Reset in every test helper (section 5). |
| Rule 6 | `kaynak-cikar.py` writes nothing; report text with project names is never saved. The `onay` text written by the agent must not contain project names (A4 says so; dogrula's existing scan checks it). |
| Secrets | No tool prints or stores values. |
| `kaynaklar.json` one-field edit | Edit the single line by hand (no `json_yaz` re-indent); `git diff --stat` must show 1 insertion. |
| Existing tests keep passing | Before and after: `python3 araclar/testler/test_p7-kaynak-yasam.py`, then (the integrator) `python3 araclar/test.py`. P7 does not run `test.py` in the design stage. |

------------------------------------------------------------------------------------------------------------------------

## 10 Acceptance (commands that prove it is done)

Run from `KOK`, in a clean tree, after implementation (none of these write to GitHub or global folders):
```
python3 araclar/testler/test_p7-kaynak-yasam.py                      # last line "N/N test geçti", exit 0
python3 araclar/kaynak-cikar.py --help | head -4                     # says: yalnız --kuru
python3 araclar/kaynak-cek.py --help | grep -- --atla                # --atla görünür
python3 araclar/kaynak-cikar.py --repo J-DTurner/etsy-api-skill --kuru           # real data: KAYIP kaynak, roller/e-ticaret etkisi, adımlar, geri alma; exit 0
python3 araclar/kaynak-cikar.py --repo J-DTurner/etsy-api-skill --kuru --json | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['karar'] in ('engel','dikkat'); print(d['karar'])"
python3 araclar/kaynak-cikar.py --repo OpenMontageInc/OpenMontage --kuru --siki; echo $?   # "program": "openmontage" kaydı: REDDEDİLDİ -> exit 1
python3 araclar/kaynak-cikar.py --repo calesthio/OpenMontage --kuru     # eski ad (eski_adlar) aynı kayda çözülür; REDDEDİLDİ, exit 0
python3 araclar/kaynak-cikar.py --repo J-DTurner/etsy-api-skill; echo $?             # no --kuru: exit 2
python3 araclar/konu-takip.py --bekleyenler --ozet-json | python3 -c "import json,sys; d=json.loads(sys.stdin.read()); print(d['durum'], len(d['karar_bekleyen']))"
python3 araclar/yol-tara.py --skill; echo $?                          # 0 (unchanged)
python3 araclar/yol-tara.py --bogus; echo $?                          # 0 (unchanged)
python3 araclar/yol-tara.py --siki; echo $?                           # 2
python3 araclar/yol-tara.py --repo Graphify-Labs/graphify --siki; echo $?   # 1, YOL KAPISI: TAKILDI (graphify: sütun 'Çözülemez')
python3 araclar/yol-tara.py --repo Leonxlnx/earshot --siki; echo $?                                                            # 0, YOL KAPISI: GEÇTİ
python3 -c "import importlib.util as u, pathlib as p
for f in ('kaynak-cek.py','listeye-ekle.py','konu-takip.py','kaynak-cikar.py'):
    spec = u.spec_from_file_location('m', p.Path('araclar')/f); m = u.module_from_spec(spec); spec.loader.exec_module(m)
print('import tamam')"      # her araç yan etkisiz içe aktarılır
git status --short                                                    # only P7's owned files (+ kaynaklar.json one line, + konu-takip outputs NOT changed)
git diff --stat araclar/github-trend.py araclar/populer-tarama.py araclar/github-skill-listesi.py   # boş: bu üç dosya değişmedi
grep -c "A9" rehber/03-yeni-skill-ekleme.md promptlar/07-yeni-skill-reposu-ekle.md      # both >= 1
grep -n "A17\|find ~ -path" rehber/03-yeni-skill-ekleme.md promptlar/07-yeni-skill-reposu-ekle.md   # no output
```
Integrator (P8) afterwards, with the hand-offs applied: `python3 araclar/dogrula.py` (0 hata), `python3 araclar/kapsam-denetimi.py` (0 sorun), `python3 araclar/test.py` (includes the P7 file), `python3 araclar/duman-testi.py`.
Do NOT run during acceptance: `kaynak-cek.py` (other than `--help`), `arsiv-*.py`, `listeye-ekle.py`, any `tara()` path (network/GitHub writes).

------------------------------------------------------------------------------------------------------------------------

## 11 Review changes

Applied (mandatory):
1. **`kaynak-cek.py --atla` (K4) added** (section 3.2, 4.10, tests 26-29, acceptance). Semantics exactly as requested: comma list, case-insensitive match through `repo_guncel`, no download / no `repo_agaci`, `UYARI: <repo> atlandı (arşiv kopyası korunur)`, not added to `manifest["kayitlar"]`, exit 0 if the rest succeeded, old `:238-240` behaviour without the flag, `--help` shows `--atla`, tested with a faked `repo_agaci`. Re-checked in code: a T1-T4 repo absent from the manifest is kept by `arsiv-yerlestir.py:471-474` (`korunan_indirilmeyen`), so no safety-lock stop. The 'To P4' hand-off item 2(a) now says "P4 uses `--atla`". `--kayip-isaretle`: both sides say "ertelendi" (reason: marking lost is a user decision; manual `rehber/03` E3 stays); item (c) removed from the P7 hand-off; the P4 spec line (505) must say "ertelendi, P7 de uygulamıyor" (written in 'To P4' 2(c)).
2. **`Önkoşul` line added** at the top (order 0..8; P7 is step 4, before P4).
3. **`dogrula.py` hand-off rewritten:** G-TIP and all new-record checks are UYARI (no HATA anywhere), new-record checks only for records absent from `git show HEAD` (the 181 existing records never count as new), raising to HATA is a separate user-approved decision; P8 test case "tip=EMEKLI, unknown key, string `oncelik` passes the monthly `dogrula`" added as mandatory. Cause: `arsiv-guncelle.py` rolls back with `git reset --hard` on a `dogrula` HATA.

Applied (optional, partly):
4. **Scope reduced** (accepted): add order A0..A17 shrunk to **A1..A9** (all documents, prompts, tests, hand-offs renumbered; approval record fields kept because the P8 gate reads them); `github-trend.py`, `populer-tarama.py`, `github-skill-listesi.py` left unchanged; `kaynak-cek.py` K1/K3 and `listeye-ekle.py` L2/L3 deferred; `--yeniden-ac` dropped; test target 40 -> 34. Kept now: `kaynak-cikar.py --kuru`, `--atla`, `lisans_riskli`, `yol-tara.py --siki`, `listeye-ekle.py` L1 fix, shared elimination and one `--bekleyenler` in `konu-takip.py` (needed for P4's backlog view and the B2 triage), `kayip_tarihi` data edit.
   Not accepted from the "ertele" list (kept, with reason): `konu-takip.py` shared elimination + `--bekleyenler`: without it P4 has no cheap source for the 320-candidate backlog (B2) and old case-sensitive bugs keep re-listing decided repos; it touches only `konu-takip.py`, not the other two tools; `yol-tara.py --siki`: additive and opt-in, the P8 gate depends on `kapi_kontrol`.

Gaps taken from the unowned list: B2 triage (tool shows max 5 names per source and the total; the monthly cap N goes to `notlar/kararlar.md` as a user question via P8); `--kayip-isaretle` (documented as ertelendi on both sides); KAYIP record without `kayip_tarihi` (one-field data edit in this package's implementation, needs approval); the two "sahipsiz" P8 items (`promptlar/10` line 8, `rehber/08`) are passed to P8 explicitly in 'To P8' item 10; the repeated-lost-source report is passed to P4 ('To P4' 2(d)).
Not taken (other owners): taze klon "damga yok" (P4), "kabul edildi" ortak listesi for P3/P5/P6 decisions (P4/P8; for candidate decisions the ledger already does it), `--hizli` and rehber/14 wording (P1/P4), `program-denetim --ozet-json` writing the report file (P6/P4), Windows/GEMINI.md (P1/P8), library path in project instruction blocks (P1).
