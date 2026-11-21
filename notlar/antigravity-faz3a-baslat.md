# Antigravity: Faz 3a başlatma (Faz 2 tamam, etiket v2-faz2-tamam)

Faz 3 ikiye bölündü. **3a (bu dosya):** kod ve temizlik, ağ yok, gerçek kayıt yok. **3b (sonra, ayrı karar):** gerçek 1 yeni repo + 1 aylık takip ölçümü ve sayısal hedefler; ağ ve gerçek yazım içerdiği için ayrı onayla.
Dal: `yeni-surec-faz3`. Model: Orchestrator Gemini 4 Neon High.

## Sırayla
1. Antigravity App: proje `SkillKutuphanesi`, dal `yeni-surec-faz3`.
2. Aşağıdaki kutuyu yapıştır. Plan çıkınca bana ya da kendi gözünle şunlara bak: ağ/gerçek repo yok mu, projelere yazma yok mu, hafıza dosyalarına dokunma yok mu, `tip` kaldırma planı risklerini ve KAYIP/EMEKLI durumunun yeni yerini gösteriyor mu.
3. Bitince `dogrula` 0 hata, `kapsam-denetimi` 0 sorun, `test` tamamı yeşil olmadan commit onayı verme.

## Başlatma komutu
```text
/plan notlar/yeni-surec-plani.md dosyasını oku (bölüm 3, 8, 9 Faz 3, 10, 11; Faz 2 sonucu: git tag v2-faz2-tamam). Yalnızca Faz 3a (kod ve temizlik) kapsamını planla ve uygula, bu sırayla: (1) 14 kabul senaryosunun tamamı için çevrimdışı, sahte verili test paketi (test_p24); (2) tip alanının kaldırılması: önce etkilenen araç, test ve kayıt listesini ve KAYIP/EMEKLI gibi durumların yeni yerini (tip alanı bu durumları da taşıyor) riskleriyle birlikte planla ve benden onay al; onaydan sonra tüm araçları tur+bolum okuyacak şekilde güncelle, sonra tip alanını kaldır; (3) 7 ayrı ajan dosyasının planın bölüm 8'deki 4 role (ana oturum, kaynak işini yapan, inceleme yapan, denetim yapan) sadeleştirilmesi: ajanlar/ kaynağı, ajan-uret.py, rehber/15-ajanlar.md, AGENTS.md/CLAUDE.md ajan satırı ve test_p12 birlikte güncellensin, üretilen .claude/agents ve .codex/agents dosyaları ajan-uret.py ile yeniden üretilsin. Kesin sınırlar: gerçek ağ taraması, gerçek yeni repo girişi, gerçek aylık çalışma ve sayısal hedef yazımı YAPMA (3b'dir); olcum.jsonl'e gerçek satır yazma; bilgisayardaki hafıza dosyalarına (~/.claude, ~/.codex, ~/.gemini) ve hiçbir projenin klasörüne/kilit.json dosyasına dokunma; çift kayıt temizliği olarak yalnız depo içi tekrarları listele, silme; arsiv/ dosyalarını silme/değiştirme, programlar.json'u yeniden serileştirme; eski sürüm ve incelemeleri silme; GitHub'a yazma/push yapma; master'a birleştirme yapma; notlar/onceki-planlar/ altına dokunma. Planı ve değişecek dosya listesini önce bana göster, onayımı bekle. Her adımdan sonra tam test.py koştur, kırılan test varsa düzeltmeden sonraki adıma geçme. Bitince dogrula.py, kapsam-denetimi.py (zaman aşımıyla), test.py sonuçlarını ve git diff --stat çıktısını raporla; commit öncesi benden onay al.
```

## Geri dönüş
`git switch yeni-surec-faz2` (Faz 2 hali), `git switch master` (eski düzen).
