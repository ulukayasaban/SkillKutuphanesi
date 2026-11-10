# 1. adım: biten ve kalan iş (çalışma kâğıdı; kullanıcıya sunulmaz)

Son güncelleme: 2026-11-11. Yeni oturum buradan devam eder; konuşma geçmişine gerek yoktur.

## Biten (commit edildi)
- Tarama tarafı: `araclar/ortak.py` (yol_taramasi, skill_yol_taramasi, yol_degerlendir, kardes_coz, istisna_* …),
  `araclar/yol-tara.py`, `yol-istisnalari.json` (10 kayıt), `notlar/yol-denetimi.md`, `dogrula.py` istisna denetimi,
  `test.py` → `yol_testleri()`. Sonuç: 5649 skill, 431'inde bulgu, 125'inde UYARI. test 201/201, kapsam 0 sorun, dogrula 0 hata.
- Eski planlar `rafta/` içine alındı.

## Kalan A: kurulum tarafı (`skill-ekle.py`, `skill-calistir.py` HENÜZ DEĞİŞMEDİ)
Kural: "dar çevir, geniş uyar". Kod dosyaları (.py .js .sh …) bu turda çevrilmez, UYARI verir.
1. `on_kontrol`: her skill için `yol_degerlendir(s, skiller, kurulacak_idler=K)` satırları rapora eklenir
   (K = kurulacaklar + kilitte kurulu olanların kimlikleri). Mevcut `kardes_bagimliliklari` döngüsüyle aynı kardeş
   **kimliğe göre** tekilleştirilir. `yol_degerlendir` çıktısına yapısal hedef bilgisi eklenir (yol-tara çıktısı değişmez).
2. `kardes-yol` mesajı doğru saysın: yalnız gerçekten çevrilen bulgular (tur genel-baska/eklenti-kardes/skil-disi-yol,
   engel yok, dosya var, kalan dolu); sıfırsa satır yok.
3. Yeni `yollari_yerellestir`, `hazirla(kaynak, hedef, s, ad, kardes=None, onek=None, skiller=None)` içinde en son çalışır;
   `onek=None` ise atlanır. `kur()`: sadece-Claude → `.claude/skills`; varsayılan ana kopya → `.agents/skills`;
   claude varyantı → `.claude/skills`. `skill-calistir.py` 154 ve 180. satırlar da onek verir.
   Satır eşleştirme: arşiv satırının tam içeriğiyle; bulunamazsa çevrilmez, sayısı görünür uyarı olur.
   `registry()` önbelleksiz (22 MB) → `skiller` parametreyle taşınır.
4. `yollari_yeniden_adlandir`: yalnız ev önekleri (`~/`, `$HOME/`, `${HOME}/`) için geriye bakış engeli;
   `${CLAUDE_PROJECT_DIR}/.claude/skills/x` çevrilmeye devam eder. Uzantı listesi tek sabit.
5. `kardes_haritasi`: eşleşme yalnız kimlikle; aynı ad farklı kimlik → `kardes-farkli-kaynak`, yol çevrilmez.
   Çevrilebilir genel-yol kardeşi varsa kilide `genel:<ad>` girer.
6. `onarim_izi(s, skiller=None)`: yol bileşeni yalnız `cevrilecek` boş değilse eklenir (6 skill etkilenir:
   ui-ux-pro-max, siege, swift-code-reviewer, code-tour, etsy-seller, mp-integrate). `ONARIM_SURUMU` değişmez.
7. `ekle()` açığı: kur çağrılmadan yeni iz damgalanıyor → kur koşuluna `or (k and k.get("onarim") != onarim_izi(s))`;
   elle değiştirilmiş kopyada (`--zorla` yoksa) ne yeniden kur ne yeni izi yaz. `guncelle` mesajına
   "sabit yol çevirisi" bileşeni, kod `yol-yerellestirme`.
8. Açık karar: sadece-Claude kurulumda `.agents/skills/<kendi>/…` → `.claude/skills/<kurulum adı>/…` (11 skill uygun).
   Öneri: `onek == ".claude/skills"` iken dar bir geçiş olarak ekle.
9. Yeni testler: `test.py` → `kurulum_yol_testleri()`, yalnız tempfile projelerde.
   Elle deneme: ui-ux-pro-max, etsy-seller, code-tour, bir seo çifti, swift-code-reviewer.

## Kalan B: zincir ve belgeler
- `arsiv-guncelle.py` aylık zincirine `yol-tara.py` ve `program-denetim.py` (başarısızlık zinciri durdurmaz).
- `rehber/04` B tablosuna yeni kodlar (yol-yerellestirme, genel-yol, eklenti-koku, skil-disi-yol, genele-yazabilir,
  yol-istisna, istisna-eskidi, kardes-farkli-kaynak) ve 43-44. satırların güncellenmesi; `rehber/03` + `promptlar/07`
  (`kaynak-cek.py --repo` sonrası, `arsiv-yerlestir` öncesi `yol-tara.py --repo`); gerekirse CLAUDE.md + AGENTS.md (aynı kalmalı).

## Kalan C: kapanış
kapsam-denetimi (0 sorun), dogrula (0 hata), test (hepsi geçer), `DURUM.md` 1. adım "bitti", commit (push yok).

## Sonra, kapı açılınca
- Kayıtlı projelerde `--guncelle --kuru` önizlemesi: ui-ux-pro-max ve etsy-seller kullananlarda yol çevirisi önerisi çıkacak.
- Eklenti kökünden dosya çekme (`ek_dosyalar`, 115 skill) lisans ve ücret onayı ister; bu turda yok.
- dogrula'daki tek uyarı (etsy-api emekli) bu işten değil; `duman-testi.py:72` " 0 uyarı" bekliyor, kapanışta bak.
