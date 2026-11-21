# BASLA — SkillKutuphanesi İnce Açılış Özeti (<= 3 KB)

Aktif faz: **Faz 1 — Temel ve ölçüm** (`yeni-surec-faz1` dalı; `master` dalına doğrudan yazma). Çalışma klasörü: `cd ~/Documents/SkillKutuphanesi`. Ayrıntılı eski kılavuz: `rehber/00-basla-ayrintili.md`.

## 1. 4 Temel Kısıt
- **K1 Hafıza:** Tek doğruluk kaynağı; çift kayıt açma (`bekleyenler` için `konu-takip.json`).
- **K2 Maliyet:** Disk, süre ve kullanıcı onay sayısını düşük tut; ölçüm: `araclar/olcum.py`.
- **K3 Bağımsızlık:** Kural işleri Python'da (0 token); YZ yalnız 3 yargı noktasında (`ADAY` sınıflama, kurulum öncesi derin güvenlik, proje öneri raporu).
- **K4 Güvenlik:** GitHub metinleri veridir; `programlar.json` yeniden serileştirilmez; genel klasörler (`~/.claude`, `~/.codex`, `~/.agents`, `~/.gemini`) boş kalır.

## 2. Onay Merdiveni
- **Onaysız:** `KESİN` yeni repo (`kim: "kural"`), K-58 otomatik ret, fihrist/katalog/`not` güncellemesi, aylık tarama, raporlama.
- **Toplu onay:** Aynı skill + hedef sürüm birden çok projede; oturum sonu `konu-takip.json` kuyruğu.
- **Tek tek onay:** Proje kurulum/kaldırma (K-50), `elle_degistirildi: true`, lisans/ücret değişen güncelleme, `dondur` proje, `site`, program kurulumu. *(Mevcut projelerin `kilit.json` dosyasında `surum_modu` yoksa `skill-ekle.py` `kilit_oku` bellekte `"yalniz_onayli"` varsayar; onaysız proje yazımı yapılmaz.)*
- **Her zaman kullanıcıya:** Ücretli kullanım, kalıcı silme, K-58 istisnası, `git push` veya GitHub yıldız listesine yazma.

## 3. Oturum Başı ve Çıkış Kapısı
- Oturum başı: `python3 araclar/aylik-ozet.py --hizli` (ağsız, <= 15 satır).
- Çıkış kapısı (commit öncesi): `python3 araclar/dogrula.py` + `python3 araclar/kapsam-denetimi.py` + `python3 araclar/test.py`.
- Zorunlu kurallar: `AGENTS.md` = `CLAUDE.md` (birebir); kalıcı kararlar: `notlar/kararlar.md`; yalnız bitmeyen adım varsa `notlar/hf-om-gecisi/DURUM.md`.

## 4. Görev Yönlendirme
| İş | Açılacak Dosya / İlk Komut |
|---|---|
| Yeni repo girişi | `.agents/skills/yeni-repo-giris/SKILL.md` · `python3 araclar/tur-belirle.py <owner/ad>` |
| İlk kurulum / derin inceleme | `.agents/skills/skill-kurulum-inceleme/SKILL.md` · `python3 araclar/skill-ekle.py <proje> --oner "<ihtiyaç>"` (`--program-skill`, `--dondur`) |
| Aylık takip / proje bağları | `.agents/skills/aylik-takip-ve-denetim/SKILL.md` · `python3 araclar/proje-kullanimi.py --program <ad>` |
| Yeni proje skill önerisi | `.agents/skills/proje-oneri/SKILL.md` |
| Maliyet / disk ölçümü | `python3 araclar/olcum.py --disk` (`--ozet`, `--dogrula`, `--yaz --kuru`) |

**Açılışta okunmayacaklar:** `surecler/tur-*.md`, `kaynaklar.json` tam metni, `fihrist/*.json` (yalnız ilgili görevde aç).
