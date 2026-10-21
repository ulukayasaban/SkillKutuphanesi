# Bilgisayarda Zaten Kurulu Skiller (dokunulmaz)

Karar (2026-10-21): Global skill klasörleri **olduğu gibi kalır**; mevcut/eski agent'lar onları kullanmaya devam eder.
Yeni projeler skillerini sadece bu kütüphaneden alır. Araçlar bu klasörleri **sadece okur**.

| Klasör | İçerik | Kim kullanır |
|---|---|---|
| `~/.claude/skills` | ~139 skill: OpenMontage (video, hyperframes, gsap-*, threejs-*, design-dna…) + addyosmani/agent-skills | Tüm Claude Code oturumları |
| `~/.agents/skills` | ~55 skill: addyosmani/agent-skills + OpenMontage video | Codex (kullanıcı seviyesi) |
| `~/.codex/skills` | ~28 skill: OpenMontage video | Codex |
| `~/.openmontage` | calesthio/OpenMontage kurulumu (91 skill kaynağı) | OpenMontage komutları |

OpenMontage skillerinin bir kopyası kütüphanede de var (`g-video-ses-medya` ve diğer kategoriler) ki yeni projeler onları
buradan alabilsin. Bu skillerin komutları yine `~/.openmontage` kurulumundan çalışır (ön kontrolde `bagimlilik` uyarısı).

## İsim çakışması nasıl çözülür?
Claude Code'da aynı isimli skill hem kişisel (`~/.claude/skills`) hem proje klasöründe varsa **kişisel olan kazanır**.
Bu yüzden `skill-ekle.py`:
- Global sürümle **birebir aynı** skill'i normal adıyla kurar (hangisi yüklenirse yüklensin içerik aynı).
- Global sürümden **farklı** içerikli skill'i `<ad>--kutuphane` adıyla kurar (ör. `threejs-fundamentals--kutuphane`);
  böylece yeni agent kütüphanedeki sürümü kullanır, eski agent'lar global sürümle çalışmaya devam eder.
- Aynı isimli alternatif sürümler `<ad>--<kaynak>` adıyla kurulur (ör. `gsap-scrolltrigger--freshtechbro`).

Hangi skillerin globalde olduğu `registry.json` → `globalde` alanında ve KATALOG.md'de görünür.
