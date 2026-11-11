# Boşluk eleştirisi (2026-11-11, salt okuma)

Tam not: `/private/tmp/claude-501/-Users-sabanulukaya-Documents-SkillKutuphanesi/50d6b09a-ea20-4d05-8336-58e58084ecab/scratchpad/plan/bosluk-elestiri.md`

## 0. Girdi sorunu
- `bosluklar.md` yalnız araç tablosunu (bölüm 1) içeriyor. "2-4: bkz. aşağı" kısmı boş.
- Önerilen iş paketi listesi yok. Paket çakışması ve onay kontrolünü akış notlarındaki önerilerden çıkardım (bölüm 3).

## 1. Senaryolar
Her satır: durum, kapsayan başlık ya da eksik olan.

1. **Yeni AI aracı:** KISMEN. Kapsayanlar: akis-09 eksik 3, akis-11 #7 (`araclar.json`), akis-08 F. Eksik: uçtan uca prosedür ve prompt.
2. **Yeni proje:** KISMEN (akis-05 #8, A-F). CLAUDE.md "Skill ekleme akışı" 1. adım araç sormuyor.
3. **Proje başka Mac'e ya da Windows'a kopyalandı:** KISMEN. Eksik:
   - `kilit.json` içindeki `proje_yolu` ve `kurulu_hash` başka makinede geçersiz kalıyor.
   - Kütüphane o makinede yok; güncelleme yalnız kütüphane makinesinden yapılır, bu yazılı değil.
   - Windows'ta `skill-ekle.py` çalışır mı belirsiz.
4. **Kaynak upstream'de kayboldu:** KAPSANDI (akis-03 #3/#5). Açık nokta: tek kayıp repo yüzünden `arsiv-guncelle.py:285` bütün `--uygula`'yı durduruyor. Zincir kayıp repoyu atlayıp devam etmeli.
5. **Program kırıcı sürüm çıkardı:** KISMEN (akis-07 #2, #8). Eksik:
   - Kırıcı sürüm sınıflaması yok (HF major, OM 244 commit sıçraması).
   - Güncellemeden önce ayrı klasörde kuru deneme yok.
   - OM'nin yerel yamaları (9 izli dosya) güncellemede ezilir; kartta yama kaydı ve geri uygulama adımı yok.
6. **Aylık çalışma iki ay tetiklenmedi:** KISMEN (akis-10 E, akis-11 #5). Eksik:
   - Kütüphane içinde "son aylık çalışma" damgası yok.
   - Kaçırılan ay için telafi yok.
   - Zamanlayıcı yalnız Claude'a özgü (`~/.claude/scheduled-tasks`, kütüphane dışı). Uygulama kapalıyken ya da Mac uykudayken tetiklenmez.
7. **Kütüphane oturumu hafızasını kaybetti:** KISMEN (akis-11 #1 BASLA.md, #2). Eksik:
   - Kararların bir kısmı yalnız Claude MEMORY.md'sinde (konu konu ilerle, yedek silme hatırlatması, güncellemeyi kütüphane oturumu yapar). Codex ve Antigravity oturumu bunları göremez (akis-09 kaçırılan #4; çözüm paketinde yok).
   - `DURUM.md` "iş bitince arşivlenir" diyor; arşivlenince kararlar da gider. Kalıcı bir KARARLAR.md gerekir.
8. **Mac yedekten geri yüklendi:** KISMEN (akis-06 #7, akis-12). Eksik:
   - Makine dışı durumun tek envanteri yok: `~/.zshenv`, `~/.zshrc`, `settings.json` env, `~/.config/openmontage/.env`, `~/.openmontage` venv pinleri, LaunchAgents, scheduled-tasks, gh oturumu, projelerdeki kilitler.
   - Yedek klasörü geri gelince `zshrc.yedek` içindeki düz metin anahtar satırı da geri gelir.
9. **İki araç aynı projede:** KISMEN (akis-09). Eksik:
   - Eşzamanlı `skill-ekle` çalışmasına karşı proje kilidi yok (`.guncelleme-kilidi` yalnız kütüphane için).
   - Bir aracın kendi eklediği skill'i yakalayan tarama zincirde yok (akis-05 D yalnız öneri).
10. **Araç yine makine geneline skill yazdı:** KAPSANDI (akis-08 A/B). Açık kalanlar:
    - Tespit aylık, yani 1 ay gecikmeli; oturum başında da çalışmalı.
    - Tespit sonrası prosedür yazılı değil.
    - Araçların genel yolları sürümle değişebilir; `araclar.json`'da araç başına yol ve sürüm kaydı olmalı.
11. **GitHub oturumu ya da token bitti:** KISMEN (akis-10 G; aylık görev SKILL.md:17 durur). Eksik:
    - Oturum yoksa bütün zincir duruyor; "yalnız yerel denetimler" modu yok.
    - Kullanıcının `gh auth login` yapacağı yönerge yazılı değil.
12. **Depo taze klonlandı:** KISMEN (akis-06 #7 ve ikinci okuma). Eksik:
    - Skill'in `.gitignore`'u arşiv dosyalarını dışarıda bırakıyor, klon eksik gelir.
    - Tek komutlu bootstrap ve doğrulama yok.
    - Depo görünürlüğü (private) hiçbir araçta denetlenmiyor.

## 2. Kimsenin sahiplenmediği
- **Push gecikmesi:** 9 commit geride. Kullanıcı takip etmiyor. Uyarı oturum başında (CLAUDE.md "ilk iş") çalışmalı.
- **Araç sürüm kayması:** Codex 0.167, Antigravity 2.29, Cursor 3.25. `arac-*.md` belirsizleri hiçbir yerde periyodik doğrulanmıyor.
- **GEMINI.md:** kütüphane kökünde yok.
- **Gizli veri:** `~/.zshrc` ve yedeğindeki düz metin anahtar. Ortam denetimi değeri değil, yalnız satır sayısını raporlamalı.

## 3. İş paketi eleştirisi
Aynı dosyaya dokunduğu için tek pakette birleşmesi gerekenler:
- `arsiv-guncelle.py`: en az 6 öneri (akis-03, 04, 07, 08, 10, 11).
- `CLAUDE.md` ve `AGENTS.md`: 8 akış dokunuyor. Birlikte düzenlenmeli, sonda `diff -q` ile eşitlik doğrulanmalı.
- `dogrula.py` ve `test.py`.
- `duman-testi.py` ile `ortak.py` (`parmak_izi`).
- `rehber/02` ve `rehber/11`.
- `skill-ekle.py` araç genişlemesi (`araclar.json`).

Onay gerektiren ama işaretsiz olanlar:
- CLAUDE.md kesin kural 1 istisnası.
- `~/.claude/scheduled-tasks` değişikliği (kütüphane dışı).
- Yedek silme hatırlatma görevi.
- `launchctl setenv`.
- `.gitignore` değişikliği.
- `--taban-yaz`.
- Eski belgeleri (PLAN.md, 'Kullanılacak Promt Örneği.md', `yerel-yapilacaklar-2026-11.md`) rafa taşımak.
- `skill/lottiefiles-motion-design` dalını silmek.
- Her push (kural 5).
- Cursor ve Copilot'un kullanılıp kullanılmadığı sorusu.

Önerilen sıra:
1. git-durum ve commit. `programlar/` izlenmiyor ve `duman-testi` temiz ağaç istiyor.
2. `araclar.json` ve `skill-ekle` araç genişlemesi.
3. genel-bekci, ortam-denetimi ve aylık zincir.
4. yedek-denetim.
5. Belge ve prompt turu. En sona; bayrak adları değişirse promptlar bayatlar.
6. Boşaltma (kapı 2).

## 4. En kritik 5 eksik
1. Kalıcı KARARLAR.md ve hafızasız açılış belgesi; Claude MEMORY.md kararları kütüphaneye alınmalı.
2. Son aylık çalışma damgası ve kaçırılan ay telafisi.
3. Yeni makine ve klon bootstrap'i ile dış ortam envanteri.
4. Kayıp repo zinciri durdurmamalı; gh oturumsuz yerel mod.
5. OM yama kaydı ve kırıcı sürüm kuru denemesi.