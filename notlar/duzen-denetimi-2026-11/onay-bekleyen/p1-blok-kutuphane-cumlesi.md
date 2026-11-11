# P1 onay bekleyen: proje bloklarına kütüphane yolu cümlesi (soru Q3)

Durum: UYGULANMADI. Kullanıcı onaylamadan `araclar/skill-ekle.py` içindeki `talimat_bloklari` değişmez; projelerdeki
`CLAUDE.md` / `AGENTS.md` bloğu bugünkü metniyle kalır.

Sorulacak soru: "Projelerin CLAUDE.md / AGENTS.md bloğuna 'Kütüphane: ~/Documents/SkillKutuphanesi; skill ekleme/silme yalnız
kütüphane oturumunda; kütüphanesiz bilgisayarda (ör. Windows) yapma' cümlesi eklensin mi? (Projelerde sonraki yazımda blok bir iki cümle uzar.)"

Önerilen sabit (onaylanırsa `skill-ekle.py` içine):

```python
BLOK_KUTUPHANE = "Kütüphane: `~/Documents/SkillKutuphanesi` (kütüphanenin CLAUDE.md/AGENTS.md dosyası orada). Skill ekleme, silme ve güncelleme yalnız kütüphane klasöründe açılan oturumda yapılır; bu proje klasöründen açılan oturumdaysan kullanıcıdan kütüphane klasöründe oturum açmasını iste ya da ihtiyacı not düş. Kütüphanesiz bilgisayarda (ör. Windows) skill ekleme/silme yapma."
```

Uygulama yeri:
- `kisa` blok: şu anki "Kütüphanesiz bilgisayarda (ör. Windows) skill ekleme/silme yapma; ihtiyacı not düş, kütüphane sahibi kurar. " cümlesinin yerine `BLOK_KUTUPHANE + " "`.
- `tam` blok: son paragrafa, `--guncelle` komutundan sonra ` ` + `BLOK_KUTUPHANE` eklenir (tam blokta Windows cümlesi bugün yok).
- Aynı metin CLAUDE.md ve AGENTS.md bloklarında olur (ikisi aynı listeden yazılır).

Etki: mevcut projelerdeki bloklar ancak bir sonraki yazımda (`--yenile`, `--guncelle`, `--skill`, `--kaldir`, `--arac`) değişir; hiçbir proje toplu yazılmaz.
Onaylanırsa test 36 (`araclar/testler/test_p1-arac-destegi.py`) şu iki ifadeyi arayacak şekilde güncellenir: `Kütüphane: ~/Documents/SkillKutuphanesi` ve `Kütüphanesiz bilgisayarda`
(şu an test 36 bu cümlenin YOK olduğunu da doğrular; onayda o koşul kaldırılır).
