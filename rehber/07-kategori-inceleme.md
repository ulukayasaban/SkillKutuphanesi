# 07 — Kategori İnceleme Süreci

Otomatik arşiv; her skill'in ne yaptığını, hangi teknolojide çalıştığını ve hangi agent'a uygun olduğunu
**tahmin** eder. Kategori incelemesi bu tahminleri kesinleştirir. **Bir oturumda bir kategori** incelenir.

## Sıra (bağımlılığa göre)
1. `a-tasarim-onyuz/01-ui-ux-tasarim-dili` (en çok örtüşme burada)
2. `a-tasarim-onyuz/02-tasarim-sistemi-marka`
3. `a-tasarim-onyuz/03-animasyon-motion` → `04-scroll-deneyimi`
4. `a-tasarim-onyuz/05-3d-webgl` (CloudAI-X ↔ freshtechbro ↔ OpenMontage sürümleri)
5. `g-video-ses-medya/*` (AI medya üretimi; senin için öncelikli)
6. `a-tasarim-onyuz/06–08`
7. `b-yazilim-gelistirme/*`
8. `c-dokuman-icerik/*`, `d-ai-otomasyon/*`
Bağımsız kategoriler (ör. 05, g, b) ayrı oturumlarda paralel incelenebilir.

## Her skill için yapılacaklar
1. `arsiv/<kategori>/<skill>/SKILL.md` ve `KAYNAK.md` oku.
2. `registry.json`'da kaydı güncelle:
   ```json
   "ozet_tr": "2-3 cümle Türkçe: ne yapar",
   "kullanim_alani": "ne zaman seçilir",
   "kullanma": "ne zaman seçilmez",
   "teknoloji": ["gsap", "react"],
   "gerekli_paketler": ["gsap", "@gsap/react"],
   "proje_tipleri": ["landing-page", "scroll-hikaye-sitesi"],
   "roller": ["motion-gelistirici"],
   "zorluk": "orta",
   "kalite": 4, "kalite_notu": "…",
   "ortusme_grubu": "scroll-animasyonu", "ortusme_rolu": "birincil",
   "inceleme": "incelendi", "inceleyen": "claude", "inceleme_tarihi": "YYYY-MM-DD"
   ```
   Kategori yanlışsa `"kategori": "…"` + `"kategori_elle": true`. Tercih/alternatif yanlışsa `"durum": "…"` + `"durum_elle": true`.
3. `notlar/<alan>/<kategori>.md` raporuna skill kartı yaz (şablon aşağıda).
4. Örtüşme grubu kararı: **birincil** (profillerde varsayılan), **tamamlayıcı** (birlikte kullanılır), **alternatif** (aynı iş, özel durum).
5. Etkilenen `roller/*.json`'u güncelle.
6. Kontrol: `python3 araclar/arsiv-yerlestir.py && python3 araclar/katalog-uret.py && python3 araclar/dogrula.py`
7. `git commit -m "İnceleme: <kategori>"`

## Kart şablonu (`notlar/<alan>/<kategori>.md`)
```markdown
### <skill-id>  ·  <owner/repo> @ <commit7>  ·  puan <n> (<not>)
- **Ne yapar:** …
- **Ne zaman:** … · **Ne zaman değil:** …
- **Teknoloji:** … · **Paketler:** …
- **Uygun proje tipleri:** … · **Zorluk:** …
- **Claude / Codex:** ✅ / 🟡 (…)
- **Geliştirici:** <sahip> (<kurum/kişi>, ★…, son güncelleme …, lisans …)
- **Örtüşme:** <grup> → <birincil/tamamlayıcı/alternatif>; benzerleri: …
- **Roller:** …
- **Karar:** TUT | ALTERNATİF | SADECE ARŞİV
```

## Bitiş kriteri
- Kategorideki her skill `inceleme: incelendi`
- Örtüşme grupları ve birincil seçimleri belli
- `dogrula.py` 0 hata; profillerin `--kuru` çalıştırması HATA vermiyor
