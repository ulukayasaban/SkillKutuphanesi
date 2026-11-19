# CHECKPOINT — SkillKutuphanesi
Son güncelleme: 2026-11-19 23:10

## Şimdi
- Plan: `notlar/plan-tur-surecleri.md` (repo türlerine göre süreçler). 1. ve 2. adım uygulandı; **3. adım (mevcut yapıları yeni düzene alma) sürüyor.**
- 3. adımın şu anki parçası: altı dev koleksiyonu fihriste taşımak. Kullanıcı onayladı ("Önerilerinle devam", 2026-11-19): rolde/projede kullanılan 7 skil arşivde kalır (`arsivde_tut`), ajan/komutlar fihriste yazılır, inceleme notları ve Türkçe açıklamalar fihriste taşınır.
- Durum: altı fihrist dosyası üretildi ve commit edildi (`fihrist/`, commit 8a8da0bf8). **ruvnet/ruflo taşındı** (commit bf230e8d6). Zincir sealeap'te, dosyaya hiçbir şey yazmadan, kullanıcı isteğiyle güvenle durduruldu. Çalışma ağacı temiz; arka planda süreç yok.
- Araç: `python3 araclar/fihriste-tasi.py owner/ad [--arsivde-tut yol1,yol2] --kuru|--evet` (Neon yazdı, iki bağımsız Neon incelemesinden geçti, 53 test). `--evet` git temiz değilse durur; her taşımadan sonra commit şart.

## Sıradaki
1. Kalan beş koleksiyonu BU SIRAYLA taşı (sıra önemli: awesome-copilot taşınınca bir kısa ad ruflo'ya geçecekti, ruflo önce taşındı). Her biri: `--evet` → `python3 araclar/dogrula.py` (0 hata) → `git add -A && git commit`:
   - `python3 araclar/fihriste-tasi.py xjli360/sealeap-amazon-skills --evet`
   - `python3 araclar/fihriste-tasi.py openai/plugins --evet`
   - `python3 araclar/fihriste-tasi.py OrcaQubits/agentic-commerce-skills-plugins --arsivde-tut medusa-commerce/skills/medusa-setup,saleor-commerce/skills/saleor-setup --evet`
   - `python3 araclar/fihriste-tasi.py github/awesome-copilot --arsivde-tut skills/caption-qa --evet`
   - `python3 araclar/fihriste-tasi.py ComposioHQ/awesome-claude-skills --arsivde-tut content-research-writer,twitter-algorithm-optimizer,file-organizer,connect --evet`
   Not (zsh): argümanları değişkene koyup `$a` ile verme, kelimelere bölünmez; komutu açık yaz.
2. Hepsi bitince: `python3 araclar/katalog-uret.py && python3 araclar/skill-readme.py`, sonra `python3 araclar/kapsam-denetimi.py` (0 sorun), `python3 araclar/test.py` (hepsi geçmeli), `python3 araclar/dogrula.py` (0 hata; fihrist "karşılığı yok" uyarıları kaybolmalı), commit.
3. Kontrol: Composio'nun iki kaydı var (T1 ve T4); T1 kaydında Neon'un yazdığı `tur: koleksiyon` duruyor. Taşımadan sonra iki kaydın da `dev-koleksiyon/fihrist` olduğunu doğrula; değilse düzelt.
4. Sonra kullanıcıya tek özet ver ve 3. adımın sonraki parçasını sor: iki kit (herk-edit-kit, Donchitos/Claude-Code-Game-Studios) için etki raporu → onay → kataloğa taşıma; sonra arşivdeki 465 medya dosyası (83 MB) için ihtiyaç listesi ve etki raporu.
5. Planın kalan adımları: 4 (kurulum aracı: fihrist/kitten kurulum + proje raporu), 5 (aylık çalışma türlere göre), 6 (Windows taşınabilir paket). Her adım ayrı onay.

## Karar bekleyen
- [ ] Push: yerelde 14 commit var, push edilmedi — kullanıcı isteyince `git push origin master`.
- [ ] Genel klasörde iki yeni girdi: `~/.claude/skills/checkpoint-kapanis`, `~/.claude/skills/oturum-acilis` (2026-11-18 14:11, bu oturumdan önce; kütüphane yazmadı). Kalsın mı, boşaltılsın mı — kullanıcı (rehber/12).
- [ ] sirioberati/YouTube-AI-Video-Editing-System'i GitHub "Yapay Zeka Skillleri" listesine eklemek (A9) — kullanıcı onayı.
- [ ] İki KAYIP kaynağa (J-DTurner/etsy-api-skill, buluslan/ecommerce-competitor-analyzer) tür yazılmadı (bekletildi).

## Çalışma düzeni (kullanıcı kararları, bu hafta)
- Uzun / çok token işler Gemini 4 Neon'a (Antigravity CLI `~/.local/bin/agy`); Claude yalnız yönetir ve doğrular. Ayrıntı ve komut kalıbı: hafıza `uzun-isleri-neona-yaptir.md`.
- Neon her zaman canlı: `--output-format stream-json ... | python3 araclar/neon-izle.py --sonuc <dosya>` arka plan görevi olarak.
- Repo yazan Neon işi ayrı worktree'de (`git worktree add ../SK-neon-<iş> -b neon/<iş>`) ve `--sandbox` ile; sonra ikinci bir Neon bağımsız inceler; temizse birleştirilir.
- Onaylanmış parça arada soru sorulmadan sonuna kadar yürütülür; sonda tek özet (hafıza `onaylanan-parcayi-sonuna-kadar-yurut.md`).
- Neon eforu idareli: kurallı işlerde low/medium, yargı ve kodda high, xhigh yok.

## Bilinen sorunlar / dikkat
- `gh` normal PATH'te yok: GitHub kullanan araçlardan önce `export PATH=/usr/local/opt/gh/bin:$PATH`.
- `dogrula.py` şu an 6 uyarı: 1 eski rol uyarısı (etsy-api) + 5 "fihrist karşılığı yok" (taşınmamış beş koleksiyon; taşınınca kaybolur).
- Antigravity hesabında `--mode auto` yok; varsayılan kipte çalışıyor (sorun değil).
- Boyut hesabı ağır, betikle kurulan programlarda alt sınırdır (OpenMontage %36, HyperFrames %84); kullanıcı "tahmini yeterli" dedi (R25).
