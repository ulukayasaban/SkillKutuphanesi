# Antigravity: Faz 1 başlatma (Adım 0 tamam)

Ön koşul: dal `yeni-surec-iskelet`, `v0-eski-surec-yedek` etiketi var, `git status --short` boş (bkz. `aktarim-yz-araci/` notu).

## Sırayla
1. Terminal: `git add AGENTS.md CLAUDE.md .agents .claude/skills notlar/yeni-surec-plani.md notlar/antigravity-faz1-baslat.md` → `git commit -m "Adim 0: ortak iskelet ve yeni surec plani"` → `git tag -a v0.1-iskelet-hazir -m "Ortak iskelet kuruldu, testler yesil"` (testler yeşil olduktan sonra; commit'i Claude yapabilir).
2. `git switch -c yeni-surec-faz1`
3. Antigravity App'te `SkillKutuphanesi` projesini aç. Model: **Orchestrator** (planlama `High`, uygulama `Medium`). Aşağıdaki komutu yapıştır.

## Başlatma komutu
```text
/plan notlar/yeni-surec-plani.md dosyasını oku (bölüm 9 Faz 1, bölüm 10 şemalar, bölüm 11 hata matrisi). Yalnızca Faz 1 (Temel ve ölçüm) kapsamını planla ve uygula: kaynaklar.json tur+bolum ana kaynak ve tip geçici senkron, 4 projenin kilit.json dosyasına surum_modu: "yalniz_onayli", olcum.jsonl yazıcısı, ince BASLA.md özeti (<= 3 KB). Faz 2-3'e geçme. Hiçbir arşiv dosyasını silme, programlar.json'u yeniden serileştirme. Projelerin kilit.json dosyasına yazmadan önce her proje için benden onay al. notlar/onceki-planlar/ altındaki belgeleri uygulama; yalnız geçmiştir. Bitince dogrula.py, kapsam-denetimi.py (zaman aşımıyla) ve test.py çalıştırıp sonucu raporla; commit öncesi benden onay al.
```

## Bilinen notlar (plana göre)
- Ana dal `master` (planda `main` yazar).
- `CLAUDE.md` = `AGENTS.md` birebir kopya (dogrula kuralı); planın "3 satırlık CLAUDE.md" fikri Faz 1'de dogrula.py'ye işlenmedikçe uygulanmaz.
- `dogrula.py` uyarısı "CLAUDE.md ilk satırı BASLA.md'ye işaret etmiyor": Faz 1'de ince `BASLA.md` ile çözülür.
- Projelerin `kilit.json` dosyası proje sayılır: K-50 gereği her biri için ayrı onay.
- Eski kurallar: `git show v0-eski-surec-yedek:CLAUDE.md`.
- Geri dönüş: `git switch master` (dokunulmadı) ya da `git switch -c kurtarma v0-eski-surec-yedek`.
