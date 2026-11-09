# 10 — Proje Kullanımı (hangi proje hangi skili kullanıyor)

**Kural:** Skill ve kaynak kayıtları (`registry.json` inceleme alanları, `kaynaklar.json` notları, kategori ve referans kartları,
ücret notları, öncelik gerekçeleri) projeden bağımsız yazılır. Proje adı ve "şu projeye uyar/uymaz" bilgisi oralara girmez.
Projeye uygunluk kurulum sırasında (`--oner`, `--kuru`) incelenir. Proje ↔ skill bilgisi **tek yerde** tutulur:

| Dosya | İçerik | Kim yazar |
|---|---|---|
| `notlar/proje-kullanimi.md` | Proje özeti, proje → skiller (kaynak, commit, rol), birden fazla projede kullanılan skiller | `araclar/proje-kullanimi.py` |
| `projeler.json` | `tarama_kokleri`, `ek_projeler`, projeye özel elle notlar (`notlar` → proje → skill kimliği) | Elle |
| `<proje>/.skill-kutuphanesi/kilit.json` | Asıl kaynak: projede ne kurulu | `skill-ekle.py` |

## Kullanım
```bash
python3 araclar/proje-kullanimi.py                  # raporu yeniden üret (projelere dokunmaz)
python3 araclar/proje-kullanimi.py --skill <kimlik> # bu skili kullanan projeler
python3 araclar/proje-kullanimi.py --repo owner/ad  # bu kaynaktan skill kullanan projeler
python3 araclar/proje-kullanimi.py --kontrol        # rapor güncel mi (yazmaz)
```

## Yapıya bağlandığı yerler
- **`skill-ekle.py`**: projede değişiklik yapan her işlemden (kurulum, `--guncelle`, `--kaldir`, `--geri-al`, `--yenile`,
  `--arac`) sonra raporu kendisi yeniler. `--kuru`, `--durum`, `--dogrula`, `--oner` raporu değiştirmez. Rapor değiştiyse ve
  kütüphane `master` dalındaysa **yalnızca bu dosya** kendiliğinden commit edilir (kütüphane çalışma ağacı temiz kalsın diye;
  aylık güncelleme ve `--birlestir` temiz ağaç ister). Push hiçbir zaman kendiliğinden yapılmaz.
- **`dogrula.py`**: rapor güncel değilse ve kayıt dosyalarında proje adı geçiyorsa UYARI verir.
- **`arsiv-guncelle.py`**: aylık raporda değişen kaynakları kullanan projeleri listeler.
- **Silme, tercih değiştirme, ad devri öncesi**: `--skill` / `--repo` sorgusuyla etkilenen projelere bakılır.

## Yeni proje nasıl rapora girer
`~/Documents` altında bir seviyedeki projeler kendiliğinden bulunur. Başka yerdeki proje için `projeler.json` → `ek_projeler`
listesine tam yol yazılır. Projeye özel bir not (ör. "şu tarihten beri bu sürüm kullanılıyor") `projeler.json` → `notlar` →
`<proje klasör adı>` → `<skill kimliği>` altına yazılır; raporda o skilin "Not" sütununda görünür.

## Claude Code, Codex ve diğer araçlar
Araçlar yalnızca Python standart kütüphanesini kullanır; hangi yapay zekâ aracından çağrıldığı fark etmez. Claude Code
`CLAUDE.md`'yi, Codex ve `AGENTS.md` okuyan diğer araçlar `AGENTS.md`'yi okur; iki dosyada aynı kural (kural 6) ve aynı komutlar
yazılıdır. Rapor yalnızca bu bilgisayardaki projeleri görür: başka bilgisayarda ya da bulut oturumunda proje bulunamazsa rapora
dokunulmaz ve güncellik denetimi atlanır.
