# 08 — Test süreci (kendi bilgisayarında)

Komutlar kütüphane kökünde çalışır (`cd ~/Documents/SkillKutuphanesi`). Hiçbiri global skill klasörlerine ya da Claude
hesabına yazmaz; deneme projesi geçici bir klasördür.

## 1. Otomatik kontroller (her değişiklikten sonra, ~2 dk, ücretsiz)
```bash
python3 araclar/dogrula.py          # 0 hata
python3 araclar/test.py             # tümü geçti (skill-ekle güvenlik senaryoları, onarım, yama, hesap çakışması)
python3 araclar/skill-calistir.py   # tüm skiller kurulup sınanır -> TEST_RAPORU.md (❌ 0 olmalı)
python3 araclar/kapsam-denetimi.py  # 0 sorun (GitHub erişimi gerekir)
```

## 2. Gerçek agent testi (ücretli, skill başına ≈ $0,15–0,30)
Örnek görev dosyası `{skill_id: görev}` biçimindedir (`araclar/ornek-gorevler.json`, 38 skill). Agent sadece okuma
araçlarıyla çalışır; skill'i kendisi seçip yüklediyse ✅:
```bash
python3 araclar/skill-calistir.py --ajan araclar/ornek-gorevler.json    # tamamı (≈ $6–12)
```
Tek skill için kendi görevini ver:
```bash
echo '{"docx": "Müşteriye 3 sayfalık hizmet sözleşmesini Word (.docx) olarak hazırla."}' > /tmp/gorev.json
python3 araclar/skill-calistir.py --skill docx --ajan /tmp/gorev.json
```
Çıktı `✅ docx ['docx']` olmalı. `['anthropic-skills:docx']` görürsen hesaptaki skill seçilmiş demektir (aşağıya bak).

## 3. Claude hesabıyla ad çakışması (docx, pdf, xlsx, pptx…) — elle uçtan uca
Claude hesabındaki skiller Claude Code'a `~/.claude/skills/synced/` altından `anthropic-skills:<ad>` adıyla gelir.
Önce bilgisayarında var mı bak (yoksa çakışma da yoktur, 3c–3d atlanır):
```bash
ls ~/.claude/skills/synced/*/
```
**a) Deneme projesi ve ön kontrol**
```bash
mkdir -p /tmp/docx-deneme && git -C /tmp/docx-deneme init -q
python3 araclar/skill-ekle.py /tmp/docx-deneme --skill docx --kuru
```
Raporda `[BİLGİ] hesap-cakismasi: docx: Claude hesabında aynı adlı skill var (anthropic-skills:docx)…` satırı olmalı.

**b) Kur ve ayarı gör**
```bash
python3 araclar/skill-ekle.py /tmp/docx-deneme --skill docx --evet
cat /tmp/docx-deneme/.claude/settings.json      # "skillOverrides": {"anthropic-skills:docx": "off"}
python3 araclar/skill-ekle.py /tmp/docx-deneme --dogrula   # ✅
```
**c) Agent'ın gördüğü skill listesi (kesin kanıt, ücretsize yakın)**
```bash
cd /tmp/docx-deneme && claude -p merhaba --output-format stream-json --verbose --max-turns 1 | grep '"subtype":"init"' | grep -o '"skills":\[[^]]*\]' | grep -oE '"[a-z-]*:?docx"'
```
Beklenen tek satır: `"docx"`. `"anthropic-skills:docx"` da çıkıyorsa gizleme çalışmıyor.

**d) Karşı deneme**
`.claude/settings.json`'da değeri `"on"` yap ve 3c'yi tekrarla: bu kez `"docx"` ve `"anthropic-skills:docx"` birlikte çıkar.
İkisi birlikteyken agent hangisini seçeceğine her seferinde kendisi karar verir; agent testinde bir kez hesaptakini seçti.
Bu yüzden kanıt olarak tek bir görevin sonucuna değil, bu listeye bak. Sonra değeri geri `"off"` yap. Anahtarı silersen
`python3 araclar/skill-ekle.py /tmp/docx-deneme --guncelle --evet` yeniden yazar; bilerek yazdığın `"on"`'a araç dokunmaz.

**Gerçek görevle (isteğe bağlı)**
```bash
cd /tmp/docx-deneme && claude
```
"Müşteriye 3 sayfalık hizmet sözleşmesini Word (.docx) olarak hazırla." yaz; ekranda `Skill(docx)` yüklenmeli
(`anthropic-skills:docx` değil). Etkileşimsiz:
```bash
cd /tmp/docx-deneme && claude -p "3 sayfalık hizmet sözleşmesini Word (.docx) olarak hazırla." --output-format stream-json --verbose --max-turns 2 --allowedTools Skill,Read | grep -o '"name":"Skill","input":{[^}]*}'
```
Beklenen: `"name":"Skill","input":{"skill":"docx"}`.

**e) Temizlik**
```bash
python3 araclar/skill-ekle.py /tmp/docx-deneme --kaldir hepsi --evet
cat /tmp/docx-deneme/.claude/settings.json 2>/dev/null || echo "settings.json kaldırıldı (araç oluşturmuştu)"
rm -rf /tmp/docx-deneme
```
Kendi ayarların olan bir projede `--kaldir` sadece aracın eklediği `skillOverrides` anahtarlarını siler; diğer ayarlar kalır.

## 4. Mevcut projeler
Bu skillerden biri (`docx`, `pdf`, `xlsx`, `pptx`, `docs`, `skill-creator` …) kurulu olan her projede:
```bash
python3 araclar/skill-ekle.py <proje> --guncelle --kuru     # "hesap-cakismasi … güncellenecek" satırları
python3 araclar/skill-ekle.py <proje> --guncelle --evet
python3 araclar/skill-ekle.py <proje> --dogrula
```
`.claude/settings.json` projede git'e girer; ekip arkadaşların da aynı skill'i kullanır.
