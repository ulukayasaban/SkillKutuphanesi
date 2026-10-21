# 04 — Agent'a Skill Verirken Kontrol Listesi

Bu listenin büyük kısmı `skill-ekle.py`'nin **ön kontrolü** tarafından otomatik yapılır. Kod adları, rapordaki
`[HATA] kod:` / `[UYARI] kod:` etiketleridir. Agent'lar (Claude/Codex) bu raporu sana göstermeden `--evet` kullanmamalıdır.

## A. Kurulumdan önce (senin kararın)
- [ ] **Kapsam:** `--oner "<ihtiyaç>"` çalıştı mı? Rapordaki `tarama` satırı tüm kütüphanenin tarandığını gösterir;
      `ek-aday:<rol>` satırları seçilmemiş ama ilgili skilleri listeler. Bunlara bilerek "hayır" de.
- [ ] **Rol başına skill sayısı:** çekirdek 3–6 skill ideal. 12'den fazlası ya da 150 KB'tan fazla SKILL.md → `baglam-yuku`.
- [ ] **Aynı işi yapan iki skill aynı role verilmedi** → `ortusme`, `ayni-skill-iki-surum`.
- [ ] **Teknoloji uyumu:** skill'in teknolojisi projenle aynı mı (React mı, vanilla mı, Three r17x mi)? KATALOG.md → Teknoloji sütunu.
- [ ] **Codex'te de kullanacak mısın?** `codex-uyum` / `claude-ozel` uyarılarını oku.

## B. Ön kontrolün denetledikleri

| Kod | Seviye | Ne demek | Ne yapmalı |
|---|---|---|---|
| `bulunamadi` | HATA | İstenen skill kütüphanede yok | `--ara <kelime>` ile doğru adı bul |
| `isim-cakismasi` | HATA | İki farklı skill aynı klasör adına kurulacaktı | Birini çıkar |
| `projede-kendi-skillin` | HATA | Projede kütüphaneden gelmemiş aynı adlı skill var | Dokunulmaz. Seninkini yeniden adlandır ya da `--zorla` (yedeklenir) |
| `farkli-kaynak` | HATA | O ad projede başka bir kaynaktan kurulu | Önce `--kaldir` |
| `elle-degistirilmis` | HATA | Kurulu skill sonradan elle değiştirilmiş | Değişikliği korumak için dokunma; ezmek için `--zorla` |
| `onyukleme-siniri` | HATA | Rolde 32'den fazla skill (Claude sınırı) | Rolü böl |
| `baglam-yuku` | UYARI | Rol çok fazla skill/metin önyükleyecek | Opsiyonelleri çıkar |
| `ortusme` | UYARI | Aynı örtüşme grubundan birden çok birincil ya da aynı skill'in iki sürümü | Birini seç |
| `alternatif-surum` | UYARI | Tercih edilen değil, alternatif sürüm seçildi | Bilerek seçtiysen sorun yok |
| `codex-uyum` | UYARI | SKILL.md'de Claude'a özgü araç adları var | Codex mantığı uygular; kritik işte test et |
| `claude-ozel` | UYARI | Konu Claude Code'a özel (plugin/hook) | Codex agent'ına verme |
| `bagimlilik` | UYARI | Başka bir kurulum gerekir (ör. OpenMontage) | Kurulumun hazır olduğundan emin ol |
| `kirik-baglanti` | UYARI | SKILL.md'nin gösterdiği bir dosya yok | Kaynak repoda da yoksa önemsiz; değilse kategoriyi incele |
| `lisans` | UYARI | Lisans belirtilmemiş | Ticari projede dikkat |
| `dusuk-puan` | UYARI | Değerlendirme < 50 (D) | Alternatife bak |
| `yapi` | UYARI/BİLGİ | Frontmatter sorunları (uzun açıklama, standart dışı ad, otomatik çağrılamaz) | Ad kurulumda otomatik düzeltilir |
| `ekli-ad` | BİLGİ | Globalde farklı bir sürüm olduğu için `--kutuphane` ekli adla kurulur | Agent dosyaları bu adı kullanır |
| `globalde-ayni` | BİLGİ | Globalde birebir aynısı var | Sorun değil |
| `arac-surumu` | BİLGİ | Claude ve Codex'e ayrı uyarlanmış sürümler kurulacak | — |
| `alt-skill` | BİLGİ | Başka bir skill'in alt klasörü | Üst skill'i de kurmak isteyebilirsin |
| `gizli-katalog` | BİLGİ | Entegrasyon ya da repo-içi katalogdan | — |
| `incelenmedi` | BİLGİ | Kategori incelemesi henüz yapılmadı | Kritik işte SKILL.md'yi oku |

## C. Kurulumdan sonra
- [ ] `--dogrula` → ✅ (kopya, symlink, SKILL.md adı = klasör adı, agent dosyaları, Codex yolları, yarım kurulum yok)
- [ ] `--durum` → her skill "güncel"
- [ ] Claude'da: projeyi aç, alt-agent listesinde rol görünüyor mu (`/agents`)
- [ ] Codex'te: `codex exec "list available skills"` proje skillerini gösteriyor mu
- [ ] Proje git'teyse `.agents/`, `.claude/`, `.codex/`, `.skill-kutuphanesi/kilit.json` commit edilebilir;
      `.skill-kutuphanesi/yedek/` için `.gitignore` önerilir.

## D. Agent'lar için kural (CLAUDE.md / AGENTS.md'de de yazılı)
1. Önce `--oner`, sonra `--kuru`. Raporu **olduğu gibi** kullanıcıya göster.
2. HATA varsa kurulum yapma; nedenini ve çözüm seçeneklerini söyle.
3. UYARI varsa kullanıcı açıkça onaylamadan `--evet` kullanma. `--zorla`'yı sadece kullanıcı isterse kullan.
4. Kurulumdan sonra `--dogrula` sonucunu bildir.
5. Global skill klasörlerine elle dosya kopyalama, symlink ya da silme yapma.
