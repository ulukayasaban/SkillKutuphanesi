# Süreçler

Kütüphaneye gelen her repo için yapılacak işler, repo türüne göre bu klasörde düz metin olarak yazılıdır. Dosyalar belirli bir yapay zeka aracına,
ajan adına ya da modele bağlı değildir: yalnız `python3 araclar/...` komutları, karar kuralları ve rol adları ("kaynak işini yapan", "inceleme yapan",
"ana oturum") geçer. Kuralın kendisi `CLAUDE.md`, `rehber/` ve `notlar/kararlar.md` içindedir; bu dosyalar oraya işaret eder, kuralı kopyalamaz.
Plan: `notlar/plan-tur-surecleri.md`. Her dosyanın yanında örnek istem `promptlar/17-repo-turune-gore-ekle.md` dosyasındadır.

Rol adları: **ana oturum** kullanıcıyla konuşan ve onay alan taraftır; **kaynak işini yapan** kayıt işini yürütür; **inceleme yapan** skilleri okur;
**denetim yapan** kontrolleri çalıştırır ve raporlar. Kullanıcıyla yalnız ana oturum konuşur; onay isteyen adımı onaysız kimse atmaz; commit ve push ana oturumundur.

"HENÜZ YOK (plan adım N)" yazan adım, planın ilgili adımı uygulanana kadar araçsızdır: elle yapılmaz, yapılmış gibi yazılmaz; raporda "henüz yok" diye belirtilir.

## Repo geldi: hangi dosya?

| Durum | Dosya |
|---|---|
| Herhangi bir yeni repo (ilk dosya) | [yeni-repo.md](yeni-repo.md) |
| Birden çok bağımsız skil (2-199) | [tur-koleksiyon.md](tur-koleksiyon.md) (eklenti paketi ek kuralları orada) |
| Tek skil | [tur-tek-skil.md](tur-tek-skil.md) |
| Asıl işi bir yazılım; skiller o yazılımın kullanıcıları için | [tur-urun-skil.md](tur-urun-skil.md) |
| Asıl işi bir yazılım; skiller o yazılımın geliştiricileri için | [tur-repo-ici.md](tur-repo-ici.md) |
| 200 ve üstü skil | [tur-dev-koleksiyon.md](tur-dev-koleksiyon.md) |
| Hazır proje iskeleti (skiller kökteki klasörlere, ayarlara, betiklere bağlı) | [tur-kit.md](tur-kit.md) |
| Bilgisayara kurulan, sürümü olan yazılım | [tur-program.md](tur-program.md) |
| Skil yok ama bilinmeye değer araç | [tur-referans.md](tur-referans.md) |
| Kullanıcının kendi skilleri ya da bir web sitesinden alınanlar | [tur-kendi-ve-site.md](tur-kendi-ve-site.md) |
| Saldırgan güvenlik ya da kötüye kullanılabilecek repo | [tur-riskli.md](tur-riskli.md) |

Türü belirleyen soru sırası `yeni-repo.md` içindedir. Bir repo iki türe uyuyorsa iki kayıt açılır, her parça kendi türünün dosyasıyla işlenir.
