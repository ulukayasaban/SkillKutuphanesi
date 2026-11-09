# Silme Adayları (karar bekliyor) — 2026-10-31

> **Sonuç (2026-10-31, kullanıcı onayıyla):** #1, #2, #3 silindi; GitHub'da yıldızları kaldırıldı ve listelerden çıkarıldı. #4, #5, #6 ve B grubu tutuldu.
> İlk hâli: bu liste **öneriydi**. Kural (rehber/03 D, rehber/05 #97): her adayın SKILL.md'si okundu, gerekçe
> içerikle doğrulandı; silme ancak kullanıcı onayıyla. Varsayılan sonuç örtüşme grubudur. Rolde/projede kullanılan, resmî
> üreticiye ait ya da benzersiz işi olan kaynaklar listede "engel" sütunuyla belirtildi.

Ölçütler: GitHub güveni (0–100, D <50, kütüphanedeki skill kaynakları arasında göreli), yıldız, lisans, skill puanı, içerik
(dosya/boyut), kütüphanede karşılığı, rol/proje kullanımı.

## A. Güçlü adaylar (somut zayıflık var, engel yok)

| # | Repo | Güven | ★ | Lisans | Skill | İçerik (okundu) | Zayıflık | Karşılığı | Öneri |
|---|---|---|---|---|---|---|---|---|---|
| 1 ✅ silindi | [itsncki-design/app-store-submission-auditor](https://github.com/itsncki-design/app-store-submission-auditor) | 14 D | 34 | **yok** | 1 | iOS projesinde App Store ret risklerini tarar (19 KB) | Lisans yok, kütüphanedeki en düşük skill puanı (43) | Kısmen `ios-code-audit` (genel iOS denetimi) | Sil ya da lisans gelene kadar beklet |
| 2 ✅ silindi | [vagabond911/aso-auditor](https://github.com/vagabond911/aso-auditor) | 15 D | 33 | **yok** | 1 | ASO puanlama kontrol listesi | Lisans yok; SKILL.md **98 KB** (agent bağlamını tek başına doldurur) | Yok | Sil ya da beklet |
| 3 ✅ silindi | [magendooro/magento-claude-skills](https://github.com/magendooro/magento-claude-skills) | 21 D | 15 | MIT | 10 | Magento REST/GraphQL hızlı başvuru ve mağaza okuma (2–7 KB, tek dosya) | ★15, tek katkıcı, ince başvuru notları | Kısmen OrcaQubits `magento-api` (geliştirici tarafı) | Sil (Magento kullanmıyorsan) |
| 4 | [mmiani/kotlin-kmp-claude-agent-skills](https://github.com/mmiani/kotlin-kmp-claude-agent-skills) | 22 D | 89 | **NOASSERTION** | 15 | Kotlin Multiplatform mimari/Gradle/veri katmanı (5–11 KB) | Lisans belirsiz, tek katkıcı | Yok (KMP için tek kaynak) | Lisans netleşene kadar beklet |
| 5 | [lemomo-ai/codex-radar](https://github.com/lemomo-ai/codex-radar) | 19 D | 39 | **NOASSERTION** | 1 | Codex oturum geçmişinden HTML işbirliği raporu | Lisans belirsiz; yalnız Codex | Claude tarafında `session-report` (claude-plugins-official) | Codex'te kullanmıyorsan sil |
| 6 | [Harishwarrior/flutter-claude-skills](https://github.com/Harishwarrior/flutter-claude-skills) | 25 D | 68 | MIT | 2 | `flutter-tester` + `owasp-mobile-security-checker` | `flutter-tester` örtüşme grubunda alternatif (birincil evanca `testing`) | `owasp-mobile-security-checker`ın karşılığı yok | Silme; sadece `flutter-tester` alternatif kalsın |

## B. Kalite adayları (ince şablon) — ENGELLİ

| Repo | Güven | ★ | Skill | Bulgu | Engel |
|---|---|---|---|---|---|
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) | 43 D | 1.3k | 162 | **95'i tek dosyalık <2 KB genel şablon** ("Beta", yönergesi yüzeysel) | e-ticaret rollerinde 38 skill (22'si ince şablon), kurulu projede kullanılıyor (`python3 araclar/proje-kullanimi.py --repo nexscope-ai/eCommerce-Skills`). Silmeden önce rolleri sealeap/finsilabs ağırlıklı yeniden kurmak gerekir |
| [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills) | 41 D | 820 | 52 | 20'si ince şablon; daha zengin Amazon kaynağı (`sealeap-amazon-skills`) geri geldi | e-ticaret rollerinde 6 skill |

## C. Tutulması önerilenler (düşük güven ama benzersiz/korunan)

Trendyol (resmî, rolde), `J-DTurner/etsy-api-skill` (rolde + kurulu projede; `araclar/proje-kullanimi.py --repo`), Shopify/agent-skills (resmî, rolde), Mercado Pago
(resmî), Swift/iOS kaynakları (Vinicius 131 dosyalık kod inceleme, ios-code-audit, swiftui-design-principles: içerikli ve benzersiz),
codex-phone-lab (Expo canlı telefon, benzersiz), lemo-wake (benzersiz görsel animasyon), MADTeacher/evanca (Flutter), OrcaQubits
(Magento/BigCommerce/Medusa/Saleor tek kaynak), finsilabs ve sealeap-ecommerce (rolde/projede).
