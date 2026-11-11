# Yama B: CLAUDE.md kural 1 istisnası (P8, onay bekliyor)

Durum: UYGULANMADI. Yama A'dan AYRI onay ve AYRI commit ister. `CLAUDE.md` ve `AGENTS.md` bugün kural 1'i istisnasız söylüyor;
kural 1'in aynen kaldığı sürece kütüphane oturumu genel skill klasörlerine ve `~/.openmontage` klasörüne yazmaz
(`BASLA.md` kural 6 bunu söyler).

Ne zaman uygulanır: ilk onaylı program güncellemesinden (HyperFrames, OpenMontage) ya da ilk boşaltma adımından ÖNCE; hangisi önce gelirse.
Bu tek istisna metnidir: `rehber/11` ve `rehber/12` yalnızca "kural 1 istisnası" diye atıf yapar, kendi sürümünü yazmaz.
İstisna işlem başınadır, genel izin değildir; her işlem için kullanıcının AYRI ve açık onayı ve önceden alınmış yedek şarttır.

## Fark
```diff
-1. Global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) **asla** yazma,
-   kopyalama, symlink koyma ya da silme. Skiller sadece kullanıcının verdiği proje klasörüne, sadece `skill-ekle.py` ile kurulur.
+1. Global skill klasörlerine (`~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.openmontage`) **asla** yazma,
+   kopyalama, symlink koyma ya da silme. Tek istisna: kullanıcının o işlem için AYRI ve açık onay verdiği, önce yedeği alınmış iki iş:
+   (a) `rehber/11-program-yonetimi.md` adımlarıyla program güncelleme, geri alma, kaldırma; (b) `rehber/12-genel-klasor-bosaltma.md`
+   adımlarıyla boşaltma. Onay yalnız o işlem içindir, genel izin sayılmaz. Skiller sadece kullanıcının verdiği proje klasörüne,
+   sadece `skill-ekle.py` ile kurulur.
```

## Aynı commit'te yapılacak diğer üç değişiklik
1. `cp CLAUDE.md AGENTS.md` sonra `cmp CLAUDE.md AGENTS.md` (sessiz olmalı); commit iletisi "AGENTS.md eşitlendi".
2. `notlar/kararlar.md` "Geçerli kararlar" bölümüne bir satır: `- K-24 (<onay tarihi>) Kural 1 istisnası onaylandı: yalnız rehber/11 ve rehber/12 adımlarıyla, her işlem için ayrı onay ve önceden yedekle.` ("Henüz sonuçlanmamış sorular" altındaki "CLAUDE.md / AGENTS.md yamaları" satırı da silinmeden "[onaylandı]" notu alır.)
3. `promptlar/README.md` "Değişmeyen kurallar" ilk maddesi şu cümleyle biter: `(tek istisna: onaylı program güncellemesi ve onaylı boşaltma, promptlar/13 ve 16)`.

## Ayrıca kullanıcıya sorulacak
Claude'un kendi hafıza notu (`skill-kutuphanesi.md`, kütüphanenin dışında) hâlâ "global klasörlere dokunma" diyor. Yama B uygulanınca
notun güncellenmesi istenip istenmediği sorulur (kütüphane dosyası değildir; sorulmadan değiştirilmez).
