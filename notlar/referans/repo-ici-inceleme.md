# Repo-İçi Skiller — İnceleme Özeti (f-repo-ici)

> Elle yazıldı (2026-10-21, claude). Skill kartları: `notlar/f-repo-ici/01-repo-gelistirici-skilleri.md` (katalog-uret üretir).
> 46 skill'in hepsi tek tek okundu; inceleme alanları `registry.json`'da.

## Genel bulgu
- 46 skill 5 repodan: vercel/next.js (24), react/react (15), microsoft/playwright (7'den 6'sı burada), GoogleChrome/lighthouse (3), motiondivision/motion (2).
  Neredeyse hepsi o repodaki komutlara (`yarn linc`, `pnpm test-start-webpack`, `compiler/scripts/...`), dosya yollarına ve
  repo içi alt-agent tanımlarına (port-pass, compiler-review, analyze-pass-impact — arşivde yok) bağlı. **Varsayılan karar: SADECE ARŞİV.**
- Kalite genel olarak yüksek (resmî ekipler, güncel); bazı React skilleri 3-5 satırlık komut hatırlatıcısı (kalite 2).
- "React compiler review" (`compiler-review`) adı yanıltıcı: React Compiler kullanan uygulamaları değil, compiler'ın Rust portunu inceler.

## Kendi projelerinde de işe yarayanlar (`notlar` alanında işaretli)
| Skill | Neden | Not |
|---|---|---|
| `improve` | Repo-bağımsız salt-okunur denetim + başka agent'a devredilecek plan üretici (yazar shadcn, MIT) | `mevcut-kod-iyilestirme` profiline aday |
| `fix` (motion) | `improve` planlarını TDD disipliniyle uygulayan yürütücü | Doğrulama komutlarını projene göre değiştir |
| `gh-stack` | GitHub'ın gh-stack eklentisiyle stacked PR; agent'a güvenli bayrak tablosu | `gh extension install github/gh-stack` gerekir |
| `v8-jit` | Genel V8 performans rehberi (hidden class, deopt, inline cache) | Node sıcak yol incelemesi |
| `write-guide` | Next.js docs ekibinin tutorial yazım ilkeleri | Docs yazarı rolüne aday |
| `write-api-reference` | API referans sayfası şablonları | Next.js frontmatter'ı uyarla |
| `authoring-skills` | SKILL.md / AGENTS.md yazım rehberi | Kısa ve doğru |
| `docs-diagrams` | SVG primitif + headless Chrome ile açık/koyu docs diyagramı | Sadece elle çağrılır; renk tokenlarını değiştir |

## Kategori taşıma kararı
Taşıma **yapılmadı**. Gerekçe: `gizli` bayrağı kategoriden değil kaynak tipinden (T3 = repo-içi) hesaplanıyor
(`arsiv-yerlestir.py`: `"gizli": k["tip"] in GIZLI_TIPLER`); yalnızca `kategori` değiştirmek skill'i görünür yapmaz, klasör de
`arsiv-yerlestir.py` çalışmadan taşınmaz. Yukarıdaki 8 skill için kullanıcı onayıyla iki seçenek:
1. `kategori` + `kategori_elle: true` (ör. improve → `b-yazilim-gelistirme/02-kod-kalitesi-review`, gh-stack → `b-yazilim-gelistirme/05-git-pr-surum`,
   write-guide/write-api-reference → `c-dokuman-icerik/03-yazi-iletisim-icerik`, v8-jit → `b-yazilim-gelistirme/06-devops-guvenlik-performans`)
   ve `arsiv-yerlestir.py`'ye "elle görünür" istisnası eklemek;
2. ya da gizli bırakıp gerektiğinde `skill-ekle.py <proje> --skill improve` ile açıkça kurmak (bugün de çalışır; ön kontrol BİLGİ `gizli-katalog` verir).
