# Yerelde yapılacaklar — PR #3 sonrası (2026-11-04)

PR: https://github.com/ulukayasaban/SkillKutuphanesi/pull/3 (dal `claude/pensive-goldberg-kp5qv6`, 9 commit).
Bulut oturumundan yapılamayanlar ve projelerin güncellenmesi. Komutlar `~/Documents/SkillKutuphanesi` içinde çalışır.
Her adımın beklenen sonucu yazılı; farklı bir şey görürsen çıktıyı Claude'a yapıştır.

## 1. PR dalını al
```bash
cd ~/Documents/SkillKutuphanesi && git fetch origin && git switch claude/pensive-goldberg-kp5qv6
```
Beklenen: `Switched to branch 'claude/pensive-goldberg-kp5qv6'`. Arşiv 1435 skill büyüdüğü için indirme biraz sürebilir.
Kontrol: `python3 araclar/dogrula.py` → `5250 skill · 0 hata`.

## 2. Yıldız listesi ↔ kütüphane kontrolü (bulutta GraphQL kapalıydı)
```bash
python3 araclar/github-skill-listesi.py
```
Beklenen: "YENİ" repo **yok** (listeye eklediğin 20 repo artık kütüphanede). YENİ görünen repo varsa adını Claude'a yaz.

## 3. Projeleri güncelle
Önce sadece rapor (hiçbir şeyi değiştirmez). Yedek klasörleri dışlanır:
```bash
find ~ -path ~/Library -prune -o -path "*/.skill-kutuphanesi/yedek" -prune -o -name kilit.json -path "*/.skill-kutuphanesi/*" -print | while read -r k; do p="$(dirname "$(dirname "$k")")"; echo "===== $p"; python3 araclar/skill-ekle.py "$p" --guncelle --kuru; done
```
Beklenen projeler: Etsy-Arif, IstatistikYoutube, Akil Disi Youtube Kanali, Etsy-Yeni. Raporda görebileceklerin:

| Satır | Anlamı | Ne yap |
|---|---|---|
| `aciklama-onarim` | description/frontmatter düzeltmesi kurulan kopyaya uygulanacak | onayla |
| `yama` | bozuk betik düzeltmesi (react-three-fiber) | onayla |
| `hesap-cakismasi` | Claude hesabındaki aynı adlı skill (docx, pdf…) bu projede gizlenecek | onayla |
| `guncellenecek` | kaynak yeni commit'e geçti | onayla |
| `kaynağı değişti` (Obsidian skilleri) | kepano'nun resmî sürümü kurulacak | onayla |
| `UYARI global-cakisma-yeni` | globalde aynı adlı FARKLI skill var; Claude globali kullanır | bkz. 4 |
| `HATA elle-degistirilmis` | o skill'i projede sen değiştirmişsin | araç dokunmaz; ezmek istersen o proje için `--zorla` |

Raporu beğendiğin her proje için:
```bash
python3 araclar/skill-ekle.py <proje> --guncelle --evet
python3 araclar/skill-ekle.py <proje> --dogrula
```
Beklenen: `Doğrulama: ✅ sorun yok`. Projede yeni `.claude/settings.json` oluştuysa onu da projenin git'ine commit et.

## 4. Etsy-Yeni: global çakışma (isteğe bağlı)
`context-engineering, frontend-ui-engineering, api-and-interface-design, security-and-hardening, test-driven-development,
documentation-and-adrs` skillerinin farklı içerikli kopyaları `~/.claude/skills` altında (global) var; Claude Code globali kullanır.
- Global sürümü bilerek kullanıyorsan: bir şey yapma.
- Kütüphane sürümünü istiyorsan: kaldırıp yeniden ekle; araç `<ad>--kutuphane` adıyla kurar, çakışma biter.
  ```bash
  python3 araclar/skill-ekle.py ~/Documents/Etsy-Yeni --durum        # skiller hangi role bağlı?
  python3 araclar/skill-ekle.py ~/Documents/Etsy-Yeni --kaldir context-engineering frontend-ui-engineering api-and-interface-design security-and-hardening test-driven-development documentation-and-adrs --evet
  python3 araclar/skill-ekle.py ~/Documents/Etsy-Yeni --skill context-engineering frontend-ui-engineering api-and-interface-design security-and-hardening test-driven-development documentation-and-adrs --rol <rol-adı> --kuru
  ```
  Rapor temizse aynı komutu `--evet` ile. Rolsüz kurulmuşlarsa `--rol …` kısmını sil.

## 5. PR'ı birleştir
GitHub'da PR #3 → **Merge pull request**. Sonra:
```bash
git switch master && git pull origin master
```
Beklenen: `python3 araclar/dogrula.py` → `5250 skill · 0 hata`.

## 6. Bekleyen tek karar
`kapsam-denetimi.py` 1 "karar bekliyor" bırakıyor: `darkroomengineering/satus` reposu sonradan `.agents/skills/next-bundle-optimizer`
skill'ini eklemiş. Kütüphaneye alınsın mı? Kararını Claude'a söyle (`dahil`e ekler ya da gerekçeli `haric` yazar).
