# 1. adım: bitti (çalışma kâğıdı; kullanıcıya sunulmaz)

Son güncelleme: 2026-11-11. 1. adımın tamamı commit edildi. Geçerli durum `DURUM.md` içindedir.

## Ne yapıldı
- **Tarama tarafı:** `araclar/ortak.py` (yol_taramasi, skill_yol_taramasi, yol_degerlendir, kardes_coz, istisna_* …),
  `araclar/yol-tara.py`, `yol-istisnalari.json` (10 kayıt), `notlar/yol-denetimi.md`, `dogrula.py` istisna denetimi.
- **Kurulum tarafı:** `skill-ekle.py` ön kontrolü yol satırlarını gösterir (`YOL_KODLARI`); `hazirla(…, onek, skiller)`
  içinde en son `yollari_yerellestir` çalışır; kardeş eşleşmesi yalnız kimlikle; kilitte `genel:<ad>`;
  `onarim_izi(s, skiller)` yol bileşeni yalnız çevrilecek kendi yolu olan skillerde; `ekle()` iz farkında yeniden kurar,
  elle değişmiş kopyaya `--zorla` olmadan dokunmaz; `skill-calistir.py` de `onek` verir.
- **Zincir ve belgeler:** `arsiv-guncelle.py` aylık zincirinde `yol-tara.py` ve `program-denetim.py` (hata zinciri durdurmaz);
  `rehber/04` B tablosu, `rehber/03`, `promptlar/07`.
- **Kural:** "dar çevir, geniş uyar". Yalnız ajan sınıfı metin dosyaları çevrilir; kod dosyaları çevrilmez, UYARI verir.

## Son ölçüm
test 260/260 · kapsam 0 sorun · dogrula 0 hata, 1 uyarı (etsy-api emekli; bu işten değil) ·
yol taraması: 5649 skill, UYARI alan 125, kurulumda düzelir 3, kardeşle düzelir 103, paket gerekli 115, çözülemez 7,
istisna 10. İnceleme: 9 bulgu, 8'i doğrulandı ve düzeltildi.

## Bilinen sınırlar (hata değil, bilerek)
- Sadece-Claude dar geçişi (`.agents/skills/<kendi>/…` → `.claude/skills/<kurulum adı>/…`) ize girmez: mevcut
  sadece-Claude kurulumlarda `--guncelle` bunu kendiliğinden önermez; yeniden kurulumda uygulanır. Ön kontrolde ayrı satırı yok.
- Yamalı dosyada yol çevirisi atlanır (yama dosyanın tamamını zaten değiştirir); sayım buna göre düzeltildi.
- `onarim_izi` 5 skilde değişti (ui-ux-pro-max, siege, swift-code-reviewer, code-tour, mp-integrate).
- Kod dosyalarındaki (.py .js .sh …) sabit yollar çevrilmez; `genel-yol` UYARI olarak kalır.

## Sonra, kapı açılınca
- Kayıtlı projelerde `--guncelle --kuru` önizlemesi: izi değişen 5 skili kullananlarda "sabit yol çevirisi" önerisi çıkar.
- Eklenti kökünden dosya çekme (`ek_dosyalar`, 115 skill) lisans ve ücret onayı ister; bu turda yok.
- `duman-testi.py:72` " 0 uyarı" bekliyor; dogrula'daki etsy-api uyarısı çözülünce bak.
