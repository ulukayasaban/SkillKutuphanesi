# Tetiklenme denetimi (klasör yapısı + description)

Son denetim: 2026-11-04 · 3815 skill (+ araç sürümleri) tarandı · **77 skill kurulunca doğru durumda tetiklenmiyordu**.
Hepsi kurulan kopyada düzeltilir; `arsiv/` altındaki orijinallere dokunulmadı. Yöntem: `rehber/03-yeni-skill-ekleme.md` →
"Description ve tetiklenme". Sürekli kontrol: `python3 araclar/dogrula.py` (kurulacak hali okur, tetiklenemeyen varsa HATA).

**Klasör yapısı:** Her kayıtta `SKILL.md` (tam bu adla) ve `KAYNAK.md` var; eksik/yanlış adlı dosya yok. Adı standart dışı
olanlar (ör. `Hook Development`) zaten kurulumda klasör adına eşitleniyor.

## Kendiliğinden düzelenler (biçim hatası)
| Sorun | Sayı | Kurulumda | Skiller |
|---|---|---|---|
| Frontmatter'ın önünde HTML yorumu (`<!-- AUTO-GENERATED -->`): araçlar frontmatter'ı hiç görmüyordu | 15 (+ Codex sürümleri) | Frontmatter başa alınır | `shopify-admin`, `shopify-custom-data`, `shopify-customer`, `shopify-dev`, `shopify-functions`, `shopify-hydrogen`, `shopify-liquid`, `shopify-partner`, `shopify-payments-apps`, `shopify-polaris-admin-extensions`, `shopify-polaris-app-home`, `shopify-polaris-checkout-extensions`, `shopify-polaris-customer-account-extensions`, `shopify-pos-ui`, `shopify-storefront-graphql` |
| `description` tırnaksız, `: ` ya da ` #` içeriyor: YAML ayrışmıyor ya da description `#`'te kesiliyor | 6 | Aynı metin tırnaklanır | `flake`, `playwright-cherry-pick`, `canvas-procedural-animation`, `character-rigging`, `nlweb-deployment`, `nlweb-dev-patterns` |

## `aciklama_duzeltme` yazılanlar (registry.json)
| Sorun | Sayı | Skiller |
|---|---|---|
| Frontmatter hiç yok (kurulumda `description: <ad>` yazılıyordu) | 26 | `affiliate-marketing-strategy`, `conversion-rate-optimization`, `ebay-advertising`, `ebay-product-research`, `ebay-seller-guide`, `ebay-seller-tools`, `ebay-seo`, `ecommerce-ab-testing`, `ecommerce-customer-retention`, `ecommerce-subscription-model`, `ecommerce-video-marketing`, `etsy-seller-guide`, `influencer-outreach`, `multichannel-ecommerce`, `omnichannel-ecommerce`, `shopify-ab-testing`, `shopify-analytics-guide`, `shopify-conversion-optimization`, `shopify-seo`, `shopify-store-setup`, `shoppable-video`, `tiktok-live-selling`, `walmart-advertising-strategy`, `walmart-seller-guide`, `walmart-seller-tools`, `woocommerce-seo` |
| Frontmatter var, `description` yok (sadece `nexscope:` bloğu) | 16 | `api-monitoring`, `domain-monitoring`, `file-integrity-monitoring`, `localization-testing`, `public-status-page`, `synthetic-monitoring`, `customer-feedback-analysis`, `ecommerce-feed-management`, `inventory-tracking-software`, `minimum-advertised-price`, `online-reputation-management`, `restock-alert`, `share-of-shelf`, `shopify-page-speed`, `visual-regression-testing`, `walmart-price-tracker` |
| `description` 40 karakterden kısa, ne zaman kullanılacağı yok (ör. "Router for all Remotion skills") | 12 | `add-sfx`, `release@remotion-dev`, `video-report`, `remotion-best-practices`, `remotion-create`, `remotion-docs`, `remotion-maps`, `remotion-multimedia`, `remotion-render`, `remotion-saas`, `remotion-studio`, `remotion-upgrade` |
| `description` 1024 karakterden uzun (Codex yüklemez) | 2 | `pixijs-custom-rendering`, `claude-api` |

## Mevcut projeler
Bu skillerden biri bir projede zaten kuruluysa: `python3 araclar/skill-ekle.py <proje> --guncelle --kuru` → `aciklama-onarim`
satırlarını gör → onaylanırsa `--evet`.

## Düzeltilmeyenler (bilerek)
- `description` içinde `<isprint>`, `<version>` gibi açılı ayraçlı örnekler (10 skill): Claude Code ve Codex sorunsuz yükler;
  sadece claude.ai'ye yüklemede XML etiketi kuralına takılabilir.
- `name` alanı olmayan 3 skill (`layers`, `upload`, `wake`): kurulumda klasör adı yazılır.
