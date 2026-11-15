# Güvenlik ve riskli skiller — kütüphaneye alınmaz (K-58)

Kesin kural `CLAUDE.md` → "Saldırgan güvenlik / riskli skiller"; karar `notlar/kararlar.md` → K-58. Bu dosya gerekçeyi ve ayrıntıyı tutar.

## Neden kütüphaneye alınmıyor
- Saldırgan güvenlik / sızma testi araçları (pentest, exploit, komuta-kontrol/C2, saldırgan recon) **ikili kullanımlıdır**: aynı skill hem savunma hem saldırı için kullanılabilir, zararlı kullanım riski taşır.
- Bu skiller/repolar kütüphaneye entegre edilince (`skill-ekle.py` ile projelere kurulan çekirdek) zararlı kullanımı kolaylaştırabilir.
- Modele (ör. Opus 5.5 ve sonrası) güvenlik kısıtı yüzünden **sorun çıkarabilir**: skill içeriği reddedilebilir, çalışma yarıda kesilebilir, kurulum/değerlendirme akışı tıkanabilir.
- Bu yüzden: kaynak kaydı açılmaz, arşive çekilmez, kategori açılmaz, role/profile/öneriye girmez. Yalnız bir GitHub yıldız listesinde yer imi olarak toplanır.

## GitHub listesi
- Ad: **Güvenlik ve Riskli Skiller**
- Slug: `güvenlik-ve-riskli-skiller`
- `kaynaklar.json` → `korunan_listeler` içinde (ikinci sıra). Böylece `github-skill-listesi.py --duzenle` bu listedeki üyeliği **silmez** ve bu liste **kopya saymaz**. (Not: bu liste repoları `kaynaklar.json`'da OLMADIĞI ve skill listesi "Yapay Zeka Skillleri"nde de bulunmadığı için `github-skill-listesi.py` çıktısında zaten YENİ/kopya olarak görünmezler; `korunan_listeler` kaydı ileride bir güvenlik reposu kütüphane skili ile çapraz-listelenirse `--duzenle`/kopya yolunu korur.)

## Listedeki repolar (2026-11-15; hiçbiri kütüphaneye ALINMADI)
"Ne" sütunu repoların kendi GitHub açıklamasından (2026-11-15 doğrulandı); lisans `repos/<ad>/license` ucundan.
| Repo | Ne (kaynak açıklama) | Lisans | Risk notu |
|---|---|---|---|
| `SnailSploit/Claude-Red` | Claude skill sistemi için saldırgan güvenlik (offensive) skill kitaplığı; her skill bir SKILL.md (SQLi'den shellcode'a, EDR atlatmadan exploit geliştirmeye) | yok (API SPDX tanımadı) | İkili kullanımlı saldırgan araç; aday araçlarında da görünüyor (aşağı bak) |
| `usestrix/strix` | Açık kaynak AI sızma testi (pentest) aracı; uygulamadaki açıkları bulup düzeltir | yok (API SPDX tanımadı) | Otonom saldırgan araç; ikili kullanımlı |
| `KeygraphHQ/shannon` | Web uygulaması ve API'ler için AI pentester; kaynak kodu analiz eder, saldırı vektörlerini bulur ve **gerçek exploit çalıştırır** | **AGPL-3.0** (doğrulandı) | AGPL; gerçek exploit çalıştırdığı için çalıştırma riski yüksek (hedef veride hasar/silme olasılığı) |
| `vxcontrol/pentagi` | Karmaşık sızma testi görevlerini yürütebilen **tam otonom AI ajan sistemi** | yok (API SPDX tanımadı) | Tam otonom saldırgan sistem; ana oturum notuna göre 0 SKILL.md (skill değil, sistem); ikili kullanımlı |

## İleride böyle bir repo gelince

**Trend/popüler/aday taramasında (kural, kullanıcı 2026-11-15):** `github-trend.py`, `populer-tarama.py` ya da `konu-takip.py` bu türe benzer (saldırgan güvenlik / ikili kullanımlı / riskli) bir repo getirirse kütüphaneye aday olarak ALINMAZ, değerlendirilmez, A1..A9 çalıştırılmaz. Yalnız kullanıcı onayıyla "Güvenlik ve Riskli Skiller" listesine yıldızlanır, sonra `konu-takip.py --karar <repo> reddedildi "K-58"` ile aday listesinden düşülür. Başka hiçbir işlem yapılmaz.

1. Kaynak ajanı repoyu inceler (ne yaptığı, saldırgan mı/ikili kullanımlı mı, lisans, otonomi düzeyi) ve kullanıcıya bildirir. **Kütüphaneye eklemez, kategori açmaz, A1..A9 akışını çalıştırmaz.**
2. Kullanıcı onaylarsa **yalnız** "Güvenlik ve Riskli Skiller" listesine yıldızlanır (GitHub işlemi → ana oturum onayı). Kütüphaneye (`kaynaklar.json`, `arsiv/`, `registry.json`) hiçbir kayıt girmez.
3. Aday araçları (`populer-tarama.py`, `github-trend.py`, `konu-takip.py`) `korunan_listeler`'i okumaz; bu repoları aylık raporlarda tekrar gösterebilir. Tekrar gelmesini durdurmak için karar yazılır: `python3 araclar/konu-takip.py --karar <owner/ad> reddedildi "K-58: yalnız güvenlik listesi"` (kararı kullanıcı verir, kaynak ajanı yazar). **Şu an bekleyen:** `SnailSploit/Claude-Red` `notlar/github-trend.md` ve `notlar/populer-skiller.md` raporlarında görünüyor; kullanıcı onaylarsa bu karar yazılmalı.

## Sınır: savunma güvenliği bu kurala girmez
Sağlamlaştırma (hardening), güvenlik denetimi (security audit), açık/bağımlılık taraması (vulnerability/dependency scanning) gibi **savunma amaçlı** skiller `06-devops-guvenlik-performans` kategorisinde kalır (ör. `security-and-hardening`, `vulnerability-scanner`, `dependency-check`, `cloudflare/security-audit-skill`). Bunlar kütüphaneden çıkarılmaz.
