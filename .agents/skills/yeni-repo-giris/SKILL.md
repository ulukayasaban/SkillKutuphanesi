---
name: yeni-repo-giris
description: Yapay Zeka Skillleri GitHub listesinden gelen yeni repoları ön-kapı, hafif güvenlik/tür/medya kontrolü, onaysız KESİN kayıt veya konu-takip.json kuyruğu ile işler (Kaynak işini yapan rolü).
---

# Yeni Repo Giriş Süreci (Kaynak İşini Yapan Rolü)

## Ön-Kapı (Zorunlu)
1. `git status --short` çalıştır; çalışma ağacı boş değilse hemen dur.
2. `master` dalında olmadığını doğrula; aktif faz veya çalışma dalında ol.

## Adımlar
1. **Liste farkı (Python):** `araclar/dogrula.py --github` ve mevcut `kaynaklar.json` / `konu-takip.json` ile yeni, değişen, `301` yönlendirilen ve kesin `404` repoları ayır. `403`/`429`/`5xx`/timeout geçici hatadır, asla KAYIP yazma.
2. **Hafif Kapı (Python, 0 token):** Her yeni repo için `araclar/tur-belirle.py` çalıştır ve 10 sıralı kuralı uygula:
   - **Saldırgan güvenlik (K-58):** Sorulmadan reddet (`araclar/konu-takip.py --karar <owner/ad> reddedildi "K-58"`). Savunma amaçlı güvenlik skilleri bu kurala girmez.
   - **Lisanssız / kısıtlı, gri alan güvenlik (tersine mühendislik, yerel proxy), açıklaması boş, `SKILL.md` yok (`CLAUDE.md`/`DESIGN.md`), `ADAY` tür veya ad çakışması:** Akışı durdurma; mevcut `konu-takip.json` kuyruğuna yaz. `yerel/kendi` adı asla el değiştirmez (`ad@yerel`).
3. **Boyut ve medya kapısı (Python):** Arşivlenecek (`tek-skil`, `koleksiyon`, `urun-skil`) repolarda `araclar/boyut-hesapla.py` çalıştır; eşik üstü medya/model dosyalarını `skill_ici_haric`/`dosya_haric` ile dışla, gerekenleri `ne_indirir` alanına yaz.
4. **Bölüme göre onaysız kayıt (`onay.kim: "kural"`):**
   - `arsiv`: `tek-skil`, `koleksiyon`, `urun-skil` (yalnız skil kısmı).
   - `fihrist`: `dev-koleksiyon` (200+ skill; yalnız aktif kullanılan `arsivde_tut` arşivde kalır).
   - `katalog`: `kit` (`kitler.json`, kurulum betiğini ASLA çalıştırma) ve `program` (`programlar.json` yalnız hedefli metin düzenlemesi, yeniden serileştirme yok).
   - `not`: `referans` (`notlar/referans/kutuphaneler.md` veya `tasarim-teknolojileri.md`).
   - `repo-ici`: Yeni repo-içi skil alınmaz.
5. **3'lü çıkış kapısı ve commit:** Her kaynak için `dogrula`, `kapsam-denetimi`, `test` %100 geçince ana oturumda kaynak bazında ayrı commit at.
6. **Kapanış:** `olcum.jsonl` satırını yaz ve `konu-takip.json` kuyruğundaki bekleyenleri oturum sonunda **tek toplu mesajla** kullanıcıya sun.

## Yasaklar
- Kit kurulum betiği çalıştırma, `programlar.json` yeniden serileştirme, K-58 istisnası verme, onaysız GitHub `push` veya yıldız listesine yazma.
