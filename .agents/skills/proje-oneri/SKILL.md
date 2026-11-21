---
name: proje-oneri
description: Yeni veya mevcut bir proje için arşiv, fihrist, katalog ve not bölümlerinden uygun skill, kit ve araç öneri raporu üretir (İnceleme yapan rolü).
---

# Proje İçin Skill Öneri Raporu (İnceleme Yapan Rolü)

## Kurallar
- Yalnız projenin gerçek ihtiyacına uyan kayıtları öner; riskli (K-58) repoları asla önerme.
- `repo-ici` kayıtları yalnız o yazılımın kendi projesinde önerilir.
- Tam ücretli kayıtlar mutlaka `"ücretli"` etiketiyle işaretlenir.
- Bu adımda hiçbir kurulum yapılmaz; kullanıcı seçtiklerini onaylayınca `skill-kurulum-inceleme` devreye girer.

## Adımlar
1. Projenin dilini, çerçevesini, hedef platformunu (Web/iOS/Android/Masaüstü/Video vb.) ve kullandığı YZ aracını (Antigravity / Claude Code / Codex) belirle.
2. Önce Python aracıyla adayları daralt (`python3 araclar/skill-ekle.py <proje> --oner "<ihtiyaç>"`), gerekirse ilgili `fihrist/`, `kitler.json`, `programlar.json` ve `notlar/referans/` başlıklarını kontrol et.
3. Kısa öneri raporunu şu sütunlarla sun: **Skill / Araç**, **Bölüm (`arsiv`/`fihrist`/`katalog`/`not`)**, **Ücret (`ücretsiz`/`kısmen`/`ücretli`)**, **Gereksinim (`ne_ister`)**, **Neden uygun**.
