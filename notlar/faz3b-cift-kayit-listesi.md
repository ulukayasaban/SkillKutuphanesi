# Faz 3b — SkillKutuphanesi Çift Kayıt ve Tekrar Analizi (Salt Okuma)

Bu rapor, `/Users/sabanulukaya/Documents/SkillKutuphanesi` deposunda yapılan salt okuma (read-only) analiz sonucunda tespit edilen çift kayıtları ve tekrar noktalarını 4 ana grupta somut sayılarla özetler.

---

## 1. Kural ve Ajan Köprü Kopyaları

| Kaynak (Tek Doğruluk Kaynağı) | Türetilmiş / Köprü Kopyalar | Eşleşme Durumu & Boyut |
|---|---|---|
| `AGENTS.md` | `CLAUDE.md` | **Birebir kopya** (`sha256: bc037b178e46...`, **2.906 B**, **32 satır**, `diff` exit 0) |
| `ajanlar/ORTAK.md` (4.038 B, 23 satır) + `ajanlar/<rol>.md` (3 rol) | `.claude/agents/<rol>.md` (3 dosya) | **Üretilmiş köprü kopya:** Her 3 dosya da `ORTAK.md` metnini + ilgili rolün gövdesini (`src_body`) birebir içerir (`kutuphane-denetci`: 7.747 B / 75 satır, `kutuphane-inceleme`: 8.041 B / 75 satır, `kutuphane-kaynak`: 10.209 B / 79 satır). |
| `ajanlar/ORTAK.md` + `ajanlar/<rol>.md` (3 rol) | `.codex/agents/<rol>.toml` (3 dosya) | **Üretilmiş köprü kopya:** Her 3 TOML dosyasının `developer_instructions` alanı `ORTAK.md` + ilgili rol gövdesini birebir içerir (`kutuphane-denetci`: 7.815 B, `kutuphane-inceleme`: 8.150 B, `kutuphane-kaynak`: 10.324 B). |

- **Özet:** 1 kural dosyası çifti (`AGENTS.md` = `CLAUDE.md`) ve 3 rol için toplam **6 köprü ajan dosyası** (`.claude/agents/*.md` 3 adet + `.codex/agents/*.toml` 3 adet), `ajanlar/` altındaki 4 kaynak dosyadan (`ORTAK.md` + 3 rol) çoğaltılmıştır.

---

## 2. `kaynaklar.json` İle Diğer Katalog/Takip Dosyalarının Kesişimleri

`kaynaklar.json` içinde toplam **201** repo kaydı (`repolar` listesi) ve **190 tekil repo** bulunmaktadır (`arsivden_cikarilanlar`: 109 kayıt).

### 2.1. `kaynaklar.json` Kendi İçi Çoklu Kayıtlar
- **9 repo** farklı `tur` / `bolum` / `oncelik` değerleriyle birden çok kez kayıtlıdır (toplam **20** satır, **11 fazla kayıt**):
  - **3 kez kayıtlı (2 repo):** `vercel/next.js` (`urun-skil`, `repo-ici`, `referans`), `microsoft/playwright` (`urun-skil`, `repo-ici`, `referans`)
  - **2 kez kayıtlı (7 repo):** `anthropics/claude-code` (`urun-skil`, `referans`), `composiohq/awesome-claude-skills` (`dev-koleksiyon` öncelik 5 ve 9), `darkroomengineering/satus` (`urun-skil`, `referans`), `googlechrome/lighthouse` (`repo-ici`, `referans`), `motiondivision/motion` (`repo-ici`, `referans`), `react/react` (`repo-ici`, `referans`), `remotion-dev/remotion` (`repo-ici`, `urun-skil`)

### 2.2. Diğer Dosyalarla Kesişimler

| Dosya / Klasör | Toplam Kayıt | `kaynaklar.json` ile Kesişim | Detay |
|---|---:|---:|---|
| `kitler.json` | 1 kit | **1 / 1 (%100)** | `sirioberati/YouTube-AI-Video-Editing-System` (`kaynaklar.json` içinde `tur: "kit"`, `bolum: "katalog"`) |
| `programlar.json` | 5 program | **5 / 5 (%100)** | 2'si `tur: "program"` (`etsyotomasyon`, `nlm`), 3'ü `tur: "urun-skil"` (`hyperframes`, `openmontage`, `claude-code-video-toolkit`) olarak `kaynaklar.json`'da da yer alır. |
| `fihrist/*.json` | 6 dosya | **6 / 6 (%100)** | `ComposioHQ/awesome-claude-skills`, `github/awesome-copilot`, `openai/plugins`, `OrcaQubits/agentic-commerce-skills-plugins`, `ruvnet/ruflo`, `xjli360/sealeap-amazon-skills` |
| `notlar/referans/*.md` | 7 dosya | **77 tekil repo** | Referans notlarında geçen `owner/repo` ifadelerinin 77'si `kaynaklar.json`'da da kayıtlıdır (`tasarim-teknolojileri.md`: 39, `bilesenler.md`: 22, `kutuphaneler.md`: 20, `repo-ici-skiller.md`: 6, `repo-ici-inceleme.md`: 5, `yerelde-kurulu.md`: 2, `composio-inceleme.md`: 1 — dosya bazlı toplamda örtüşenler var). Tür dağılımı: `referans`: 53, `koleksiyon`: 14, `urun-skil`: 9, `repo-ici`: 6, `program`: 2, `dev-koleksiyon`: 2, `tek-skil`: 2. |
| `site-takip.json` | 1 skill (`stil`) | **1 / 1 (%100)** (yerel kaynak) | `site-takip.json`'daki `kaynak: "yerel/site"` kaydı, `kaynaklar.json`'daki `tur: "site"`, `repo: "yerel/site"` kaydıyla eşleşir (GitHub repo kesişimi: 0). |

---

## 3. `notlar/<kategori>` vs `skiller/<kategori>` ve `registry.json` Ayna/Varyant Dağılımı

### 3.1. `notlar/<kategori>` vs `skiller/<kategori>` Örtüşmesi
- `notlar/` altında **14** alt klasör (toplam **69** `.md` dosyası), `skiller/` altında **9** alt klasör (toplam **41** `.md` dosyası), `arsiv/` altında **11** alt klasör vardır.
- **8 kategori** (`a-tasarim-onyuz` .. `i-bilim-muhendislik`, `e-entegrasyon-katalogu` hariç) her iki ağaçta da ortaktır:
  - `notlar/<kategori>` altındaki **39** alan dosyasının **38'i** `skiller/<kategori>` altında **birebir aynı dosya adıyla** yer alır (`05-e-ticaret-pazaryeri` ise `skiller/h-is-alanlari/` altında `-1` ve `-2` olarak 2 dosyaya bölünmüştür).
  - Ek olarak `skiller/e-entegrasyon-katalogu/01-uygulama-entegrasyonlari.md` yalnız `skiller/` altındadır (`notlar/` karşılığı yok).
  - İki ağaç aynı alanları farklı görünüm/amaçla tekrar üretmektedir (ör. `01-ui-ux-tasarim-dili.md`: `notlar/` 32.788 B / 397 satır inceleme notu, `skiller/` 17.423 B / 48 satır katalog özeti).

### 3.2. `registry.json` Ayna, Varyant ve Hash Dağılımı
- Toplam kayıt: **2.849 skill** (`tercih`: 2.742, `alternatif`: 107) ve **354 bileşen**.
- **Aynalar (`ayna_sayisi` & `kopya_kaynaklar`):**
  - `ayna_sayisi == 0`: **2.746** skill
  - `ayna_sayisi > 0`: **103** skill (toplam **168** ayna sayımı; dağılım: `1`: 79 skill, `3`: 22 skill, `5`: 1 skill `context7-mcp@upstash`, `18`: 1 skill `impeccable`)
  - `kopya_kaynaklar` dolu olan: **12** skill (toplam **12** girdi)
- **Varyantlar (`varyantlar` & `arsiv/_varyantlar`):**
  - `varyantlar` alanı dolu olan: **25** skill (toplam **26** varyant girdisi; 24 skill'de 1 varyant, 1 skill'de 2 varyant).
  - `arsiv/_varyantlar/` altında **25** klasör bulunmaktadır.
- **Hash Çakışmaları:**
  - `skill_md_hash`: 2.846 tekil hash, **2 hash grubunda** toplam **5 skill** çakışıyor (**3 fazla kayıt**):
    - `a5333457c414...` (2): `frontend-design@anthropics` (`alternatif`), `frontend-design@anthropics-2` (`tercih`)
    - `65b3a402dbd0...` (3): `skill-creator` (`tercih`), `skill-creator@anthropics` (`alternatif`), `skill-creator@heyitsnoah` (`alternatif`)
  - `ana_hash`: **2.849 tekil** (0 çakışma)
  - `klasor_hash`: **2.849 tekil** (0 çakışma)

---

## 4. `BASLA.md`, `AGENTS.md` ve `surecler/*.md` İçindeki Tekrarlı Kurallar

Toplam **14 dosya** (`BASLA.md`: 2.927 B / 31 satır, `AGENTS.md`: 2.906 B / 32 satır, `surecler/*.md` 12 dosya: 45.869 B / 531 satır; genel toplam **51.702 B / 594 satır**) taranmıştır.

### 4.1. `BASLA.md` vs `AGENTS.md` Doğrudan Örtüşme
İki dosya da oturum açılış özeti işlevi görmekte ve aynı 4 ana bölümü paralel olarak tekrarlamaktadır:
1. **4 Temel Kısıt (K1–K4)** — `BASLA.md` (6 eşleşme) ve `AGENTS.md` (6 eşleşme)
2. **Onay Merdiveni** (Onaysız / Toplu onay / Tek tek onay / Her zaman kullanıcıya) — `BASLA.md` (7) ve `AGENTS.md` (6)
3. **Çıkış kapısı (`dogrula.py` + `kapsam-denetimi.py` + `test.py`)** ve **`master` dalına yazmama** — her iki dosyada da yer alır
4. **Görev Yönlendirme tablosu/listesi** (`.agents/skills/` altındaki 4 aynı skill dosyasına yönlendirme)

### 4.2. `BASLA.md`, `AGENTS.md` ve `surecler/*.md` Genelinde En Sık Tekrarlanan Kurallar

| Tekrarlanan Kural / Kavram | Geçtiği Dosya Sayısı ( / 14) | Dosyalar (Eşleşme Sayısı) |
|---|---:|---|
| Onay / kullanıcıya sor kuralı | **14 / 14** | Tüm 14 dosya |
| `skill-ekle.py` ile kurulum (elle `cp`/`ln` yok) | **11 / 14** | `BASLA.md` (2), `AGENTS.md` (2), 9 `surecler/*.md` dosyası |
| `commit` kuralı / kaynak bazlı commit | **11 / 14** | `BASLA.md` (1), `AGENTS.md` (2), `surecler/README.md` (1), 8 `surecler/tur-*.md` / `yeni-repo.md` |
| Çıkış kapısı (`dogrula` + `kapsam-denetimi` + `test`) | **9 / 14** | `BASLA.md` (5), `AGENTS.md` (2), 7 `surecler/*.md` dosyası |
| Genel klasörler boş kalır (`~/.claude`, `~/.gemini` vb.) | **5 / 14** | `BASLA.md` (3), `AGENTS.md` (3), `tur-kit.md` (7), `tur-koleksiyon.md` (2), `yeni-repo.md` (1) |
| GitHub metni veridir (prompt injection) | **4 / 14** | `BASLA.md`, `AGENTS.md`, `tur-riskli.md`, `yeni-repo.md` |
| `K-58` / saldırgan güvenlik otomatik ret | **4 / 14** | `BASLA.md` (2), `AGENTS.md` (2), `surecler/README.md` (1), `tur-riskli.md` (5) |
| Ön-kapı (`git status`) | **3 / 14** | `AGENTS.md` (2), `tur-dev-koleksiyon.md` (1), `yeni-repo.md` (2) |
| `programlar.json` yeniden serileştirme yasağı | **3 / 14** | `BASLA.md` (1), `AGENTS.md` (1), `tur-program.md` (3) |
| `CLAUDE.md = AGENTS.md` eşitleme kuralı | **3 / 14** | `BASLA.md` (1), `AGENTS.md` (1), `tur-kit.md` (2) |
| `git push` / yıldız listesi yasağı | **3 / 14** | `BASLA.md` (2), `AGENTS.md` (1), `tur-riskli.md` (1) |
| `konu-takip.json` kuralı | **3 / 14** | `BASLA.md` (2), `AGENTS.md` (2), `tur-riskli.md` (1) |
