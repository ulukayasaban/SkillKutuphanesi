# 04-skill-plugin-yazimi — AI ve Otomasyon

_Skill yazma, plugin/hook/komut geliştirme_

> `araclar/katalog-uret.py` üretir; elle düzenleme. İnceleme bilgileri `registry.json`'a yazılır (bkz. `rehber/07-kategori-inceleme.md`). İncelenen: **15/15**

### agent-development  ·  anthropics/claude-code @ d014fc0  ·  puan 76 (B)

- **Ne yapar:** Claude Code eklentileri için alt-agent (subagent) yazımı: Markdown + YAML frontmatter yapısı, name/description/model/color/tools alanları, <example> bloklarıyla tetikleme koşulları, sistem istemi tasarımı, AI destekli üretim ve doğrulama kuralları; doğrulama betiği ve örnekler içerir.
- **Ne zaman:** Claude Code projesine/eklentisine özel alt-agent tanımı yazmak ya da mevcut agent'ın tetiklenmesini düzeltmek. · **Ne zaman değil:** Codex'te frontmatter biçimi geçerli değil: Codex özel agent'ları `.codex/agents/<ad>.toml` dosyasında `name`, `description`, `developer_instructions` (ve isteğe bağlı skills.config) alanlarıyla tanımlanır — bu kütüphanenin skill-ekle.py'si rolleri zaten bu biçimde üretir. Skill'in sistem istemi tasarımı ve 'ne zaman tetiklenmeli' açıklaması yazım ilkeleri Codex'te de geçerli; color/model/tools alanlarını atla.
- **Teknoloji:** claude-code, markdown, yaml
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152726, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih · **Örtüşme:** claude-alt-agent-tanimi → birincil · **Roller:** skill-gelistirici
- **Boyut:** 69 KB (SKILL.md 10.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Anthropic resmi plugin-dev setinden; alan alan doğrulama kuralları ve örnekler net. Claude Code'a özel (Codex için yukarıdaki uyarlama).

### command-development  ·  anthropics/claude-code @ d014fc0  ·  puan 76 (B)

- **Ne yapar:** Claude Code slash komutu yazımı: komut konumları (proje/kullanıcı/eklenti), YAML frontmatter (description, allowed-tools, model, argument-hint, disable-model-invocation), $ARGUMENTS ve konumsal argümanlar, @dosya başvuruları, satır içi bash çalıştırma, AskUserQuestion ile etkileşim ve organizasyon/namespacing.
- **Ne zaman:** Ekipte tekrar eden istemleri Claude Code slash komutuna çevirmek. · **Ne zaman değil:** Codex'te Claude slash komut biçimi yok: karşılığı `~/.codex/prompts/<ad>.md` özel istem dosyaları (`/prompts:<ad>` ile çağrılır; $ARGUMENTS/$1 yer tutucuları desteklenir) ya da doğrudan bir skill'dir. allowed-tools, model, satır içi `!bash` çalıştırma ve @dosya başvurusu Codex'te çalışmaz — bunları istemin içinde 'şu komutu çalıştır / şu dosyayı oku' talimatına çevir.
- **Teknoloji:** claude-code, markdown, yaml
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152726, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih · **Örtüşme:** claude-slash-komut → birincil · **Roller:** skill-gelistirici
- **Boyut:** 150 KB (SKILL.md 18.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Anthropic resmi, çok sayıda örnek ve referans; SKILL.md 19 KB ve klasör 150 KB ile ağırca. Claude Code'a özel.

### hook-development  ·  anthropics/claude-code @ d014fc0  ·  puan 84 (A)

- **Ne yapar:** Claude Code hook'ları: prompt tabanlı (LLM kararlı) ve komut hook'ları, eklenti hooks.json ve settings biçimi, PreToolUse/PostToolUse/Stop/SubagentStop/SessionStart/SessionEnd/UserPromptSubmit/PreCompact/Notification olayları, çıktı biçimi, ${CLAUDE_PLUGIN_ROOT}; doğrulama/test betikleri ve örnek hook'lar içerir.
- **Ne zaman:** Tehlikeli komutu engelleme, düzenleme sonrası otomatik format/test, oturum başında bağlam yükleme gibi olay tabanlı Claude Code otomasyonu. · **Ne zaman değil:** Codex'te Claude Code hook olayları ve hooks.json biçimi birebir yok; Codex'in kendi onay/sandbox politikası (`approval_policy`, `sandbox_mode`) ve sürümüne göre sunduğu hook/notify ayarları `~/.codex/config.toml` içinde yapılır. Bu skilldeki betik mantığı Codex'te sandbox kuralı, AGENTS.md talimatı ya da git pre-commit hook'u olarak uygulanabilir; prompt tabanlı hook'ların karşılığı yoktur. Basit 'şunu görünce uyar' kuralları için writing-hookify-rules daha hızlı.
- **Teknoloji:** claude-code, bash, json · **Paketler:** jq (betikler için)
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152726, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih · **Örtüşme:** claude-hook → birincil · **Roller:** skill-gelistirici
- **Boyut:** 63 KB (SKILL.md 15.9 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil, hook grubunda). Anthropic resmi; tüm olaylar, girdi/çıktı şemaları ve test betikleri tek yerde. hookify kuralına göre daha güçlü ama daha zahmetli.

### plugin-settings  ·  anthropics/claude-code @ d014fc0  ·  puan 76 (B)

- **Ne yapar:** Claude Code eklentilerinde kullanıcıya özel ayar ve durum saklama kalıbı: proje kökünde `.claude/<eklenti>.local.md` dosyası (YAML frontmatter + Markdown gövde); hook betiklerinden, komutlardan ve agent'lardan okuma, frontmatter ayrıştırma teknikleri ve geçici aktif hook, agent durum yönetimi gibi kalıplar.
- **Ne zaman:** Proje başına açılıp kapatılabilen ya da yapılandırılabilen bir Claude Code eklentisi yazarken. · **Ne zaman değil:** Codex'te `.claude/*.local.md` dosyalarını okuyan bir mekanizma yok; aynı kalıp Codex'te skill'in kendisinin okuyacağı bir proje dosyası (örn. `.agents/<ad>.local.md`) olarak elle uygulanabilir, hook entegrasyonu kısmı uygulanamaz.
- **Teknoloji:** claude-code, yaml, bash
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152726, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih · **Örtüşme:** claude-plugin-yapisi → tamamlayıcı · **Roller:** skill-gelistirici
- **Boyut:** 43 KB (SKILL.md 11.8 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT. Dar ama iyi örneklenmiş bir kalıp; plugin-structure ile birlikte kullanılır.

### plugin-structure  ·  anthropics/claude-code @ d014fc0  ·  puan 84 (A)

- **Ne yapar:** Claude Code eklenti mimarisi: dizin düzeni (.claude-plugin/plugin.json, commands, agents, skills, hooks, .mcp.json), manifest alanları ve bileşen yolu yapılandırması, otomatik keşif, ${CLAUDE_PLUGIN_ROOT} ile taşınabilir yollar ve dosya adlandırma kuralları.
- **Ne zaman:** Yeni Claude Code eklentisi iskeleti kurmak, bileşenleri düzenlemek, marketplace'e hazırlamak. · **Ne zaman değil:** Codex'te Claude Code eklenti biçimi (.claude-plugin/plugin.json, ${CLAUDE_PLUGIN_ROOT}) desteklenmez; bileşenler ayrı ayrı kurulur: skiller `.agents/skills/<ad>/SKILL.md`, agent'lar `.codex/agents/<ad>.toml`, MCP sunucuları `~/.codex/config.toml` [mcp_servers], özel istemler `~/.codex/prompts/`. Dizin düzeni ve adlandırma ilkeleri yine yol gösterir.
- **Teknoloji:** claude-code, json
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152726, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih · **Örtüşme:** claude-plugin-yapisi → birincil · **Roller:** skill-gelistirici
- **Boyut:** 73 KB (SKILL.md 13.5 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil, eklenti grubunda). plugin-dev ailesinin giriş noktası; diğer plugin-dev skilleri (komut, agent, hook, ayar, MCP) bunu tamamlar.

### skill-creator  ·  anthropics/skills @ dbd4588  ·  puan 90 (A)

- **Ne yapar:** Skill oluşturma, iyileştirme ve ölçme: niyet yakalama ve görüşme, SKILL.md yazım rehberi (aşamalı açılım, sürpriz olmama ilkesi), test istemleriyle skill'li/skill'siz çalıştırma, değerlendirici/karşılaştırıcı/analizci agent'lar, eval görüntüleyici, benchmark ve varyans analizi, açıklama (tetikleme) optimizasyonu ve paketleme betikleri.
- **Ne zaman:** Yeni skill yazmak ya da mevcut skill'i ölçülebilir biçimde iyileştirmek (tetikleme doğruluğu dahil). · **Ne zaman değil:** Claude Code eklentisine özgü yerleşim için skill-development'ı da oku. Eval döngüsü `claude -p` ile alt süreç çalıştırır; Codex'te bu adımlar `codex exec` ile değiştirilmeli ya da test istemleri elle çalıştırılmalı — yazım rehberi ve betiklerin çoğu (quick_validate, package_skill) araçtan bağımsız çalışır.
- **Teknoloji:** python, markdown · **Paketler:** python3, claude CLI (eval döngüsü için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** anthropics (kurum, resmî, ★182720, son güncelleme 2026-10-09, lisans yok)
- **Durum:** tercih · **Örtüşme:** skill-yazimi → birincil · **Roller:** skill-gelistirici
- **Boyut:** 220 KB (SKILL.md 32.4 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (birincil). Dört sürüm arasında en güncel ve tek ölçme/eval altyapısı olan Anthropic resmi sürüm. heyitsnoah kopyası bununla aynı (yalnızca NOTICE/LICENSE farkı); composiohq ve freshtechbro eski 'init_skill + package' sürümü. writing-skills tamamlayıcı (baskı testi/TDD yaklaşımı).

### skill-creator@composiohq  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 76 (B)

- **Ne yapar:** skill-creator'ın eski sürümü (ComposioHQ): skill anatomisi, aşamalı açılım ilkesi ve 6 adımlı süreç (örnekle anlama, içerik planlama, init_skill.py ile iskelet, düzenleme, package_skill.py ile paketleme, yineleme).
- **Ne zaman:** Ölçüm/eval istemeden, basit iskelet + paketleme akışı yeterliyse. · **Ne zaman değil:** Varsayılan olarak kullanma; anthropics/skill-creator güncel ve eval destekli.
- **Teknoloji:** python, markdown · **Paketler:** python3
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 38 KB (SKILL.md 11.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Eski sürüm; freshtechbro kopyasıyla neredeyse aynı (yalnızca package_skill.py farkı).

### skill-creator@freshtechbro  ·  freshtechbro/claudedesignskills @ 1da73fe  ·  puan 57 (C)

- **Ne yapar:** skill-creator'ın eski sürümünün freshtechbro/claudedesignskills kopyası: skill anatomisi, aşamalı açılım ve init/package betikli 6 adımlı süreç.
- **Ne zaman:** Güncel sürüme erişilemiyorsa yedek. · **Ne zaman değil:** Varsayılan olarak kullanma; composiohq kopyasıyla aynı içerik, anthropics/skill-creator güncel.
- **Teknoloji:** python, markdown · **Paketler:** python3
- **Claude / Codex:** tam / tam
- **Geliştirici:** freshtechbro (kisi, ★1107, son güncelleme 2025-11-20, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 41 KB (SKILL.md 11.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Eski sürümün ikinci kopyası; ek değer yok (MIT lisanslı olması tek fark).

### skill-creator@heyitsnoah  ·  heyitsnoah/claudesidian @ 6c56f35  ·  puan 64 (C)

- **Ne yapar:** Anthropic skill-creator'ın güncel sürümünün claudesidian içindeki birebir kopyası (eval görüntüleyici, değerlendirici agent'lar, benchmark ve açıklama optimizasyonu dahil); NOTICE.md ile lisans notu eklenmiş.
- **Ne zaman:** claudesidian kasası içinde skill geliştirirken (kasa bu kopyayı bekler). · **Ne zaman değil:** Diğer projelerde; anthropics/skill-creator ile aynı içerik.
- **Teknoloji:** python, markdown · **Paketler:** python3, claude CLI (eval döngüsü için)
- **Claude / Codex:** tam / tam
- **Geliştirici:** heyitsnoah (kisi, ★2599, son güncelleme 2026-04-11, lisans MIT)
- **Durum:** alternatif · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 221 KB (SKILL.md 32.4 KB, yük buyuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İçerik resmi sürümle aynı; çift kurulum bağlamı boşa harcar.

### skill-development  ·  anthropics/claude-code @ d014fc0  ·  puan 68 (B)

- **Ne yapar:** Claude Code eklentileri için skill yazım rehberi: skill anatomisi, aşamalı açılım, örnekle anlama → içerik planlama → yapı oluşturma → SKILL.md düzenleme adımları; eklentideki skills/ dizinine yerleştirme, üçüncü şahıs açıklama ve tetikleme ifadeleri, doğrulama kontrol listesi.
- **Ne zaman:** Bir Claude Code eklentisinin içine skill eklemek (plugin-dev akışı içinde). · **Ne zaman değil:** Bağımsız skill yazımı ve ölçümü için skill-creator birincil. Codex'te: eklenti yerleşimi (plugins/<ad>/skills/) ve ${CLAUDE_PLUGIN_ROOT} geçerli değil — skill'i doğrudan `.agents/skills/<ad>/SKILL.md` olarak yaz; SKILL.md yazım ilkeleri (frontmatter name/description, aşamalı açılım) Codex'te de aynen geçerli.
- **Teknoloji:** claude-code, markdown
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152726, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 34 KB (SKILL.md 22.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. İçeriğin çoğu eski skill-creator metninden türetilmiş (22 KB); eklentiye özgü kısım ince. writing-skills ve skill-creator varken ek değeri düşük.

### skill-share  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 69 (B)

- **Ne yapar:** Yeni skill iskeleti oluşturur, doğrular, zip paketler ve Rube (Composio) MCP üzerinden Slack kanalına paylaşır.
- **Ne zaman:** Ekipte skill paylaşımını Slack bildirimiyle otomatikleştirmek (Composio Rube bağlıysa). · **Ne zaman değil:** Rube/Composio bağlantısı yoksa; skill yazım kalitesi için skill-creator. Betik içermiyor — paketleme adımları agent'ın yorumuna kalıyor.
- **Teknoloji:** mcp, slack, composio · **Paketler:** Rube MCP (Composio)
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** tercih · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 3 KB (SKILL.md 2.8 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 2/5 — Karar: SADECE ARŞİV. Asıl değer Slack paylaşımı; skill oluşturma kısmı skill-creator'ın zayıf özeti.

### skillify  ·  vudovn/ag-kit @ 549ba3d  ·  puan 77 (B)

- **Ne yapar:** Tekrar eden çok adımlı iş akışlarını yeniden kullanılabilir SKILL.md'ye dönüştürür: kalıbı tanımla, şablondan SKILL.md üret, yerleştir, doğrula; adlandırma kuralları ve kalite kontrol listesi.
- **Ne zaman:** 'Bunu skill yap' dendiğinde ya da aynı iş 3+ kez tekrarlandığında hızlı skill çıkarımı. · **Ne zaman değil:** Ölçülebilir, test edilmiş skill gerekiyorsa (skill-creator, writing-skills). Şablon when_to_use/allowed-tools/effort gibi ag-kit/Claude Code'a özgü alanlar üretir; Codex için yalnızca name + description bırak.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam — Claude Code'a özgü frontmatter alanları: effort, when_to_use (Codex bunları yok sayar)
- **Geliştirici:** vudovn (kisi, ★8200, son güncelleme 2026-10-18, lisans MIT)
- **Durum:** tercih · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 3 KB (SKILL.md 3.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 3/5 — Karar: ALTERNATİF. Kısa ve pratik 'iş akışından skill' tarifi; doğrulama yüzeysel.

### template-skill  ·  ComposioHQ/awesome-claude-skills @ be2a406  ·  puan 61 (C)

- **Ne yapar:** Boş skill şablonu: yalnızca name/description yer tutucuları ve 'talimatları buraya yaz' satırı.
- **Ne zaman:** Yok — yeni skill için skill-creator'ın init/şablonları daha iyi. · **Ne zaman değil:** Hiçbir projeye kurma; içerik yok.
- **Teknoloji:** markdown
- **Claude / Codex:** tam / tam
- **Geliştirici:** ComposioHQ (kurum, resmî, ★77605, son güncelleme 2026-09-18, lisans yok)
- **Durum:** alternatif · **Örtüşme:** skill-yazimi → alternatif
- **Boyut:** 0 KB (SKILL.md 0.1 KB, yük kucuk)
- **İnceleme:** incelendi · kalite 1/5 — Karar: SADECE ARŞİV. 140 baytlık boş şablon.

### writing-hookify-rules  ·  anthropics/claude-code @ d014fc0  ·  puan 76 (B)

- **Ne yapar:** hookify eklentisi için kural yazımı: `.claude/hookify.<kural>.local.md` dosyalarında YAML frontmatter (name, enabled, event: bash/file/stop/prompt/all, pattern, action: warn/block) ve Claude'a gösterilecek mesaj; çoklu koşul, olay türü rehberi, regex ipuçları ve tuzaklar.
- **Ne zaman:** Kod yazmadan 'tehlikeli rm uyarısı', 'console.log engelle' gibi hızlı koruma kuralları eklemek (hookify kuruluysa). · **Ne zaman değil:** hookify eklentisi kurulu değilse; karmaşık mantık gerekiyorsa hook-development. Codex'te hookify yok: aynı korumalar Codex'in sandbox/onay politikasıyla (`~/.codex/config.toml`), AGENTS.md'deki yasak komut listesiyle ya da git pre-commit hook'uyla sağlanır; kuralın regex'i ve mesajı bu araçlara aynen taşınabilir.
- **Teknoloji:** claude-code, yaml, regex · **Paketler:** hookify Claude Code eklentisi
- **Claude / Codex:** tam / konu-claude-ozel — Konu Claude Code plugin/hook/komut/alt-agent geliştirme. Codex'in de kendi hook, plugin ve slash command sistemi var ama dosya formatları farklı (Claude: hooks.json, plugin.json, ${CLAUDE_PLUGIN_ROOT}). Codex'te sadece kavram referansı olarak kullan. 
- **Geliştirici:** anthropics (kurum, resmî, ★152726, son güncelleme 2026-10-21, lisans yok)
- **Durum:** tercih · **Örtüşme:** claude-hook → alternatif · **Roller:** skill-gelistirici
- **Boyut:** 8 KB (SKILL.md 8.2 KB, yük orta)
- **İnceleme:** incelendi · kalite 4/5 — Karar: TUT (alternatif, hook grubunda). Anthropic resmi; kısa ve örnekli. hook-development'ın kod gerektirmeyen hafif alternatifi.

### writing-skills  ·  obra/superpowers @ 2ce8aa1  ·  puan 95 (A)

- **Ne yapar:** Skill yazımını süreç dokümantasyonuna uygulanmış TDD olarak ele alır: önce alt-agent'larla baskı senaryosu çalıştırıp skill'siz başarısızlığı gözle (RED), skill'i yaz (GREEN), açıkları kapat (REFACTOR). Skill türleri, yapı, keşfedilebilirlik (SDO), ikna ilkeleri ve Anthropic en iyi uygulamaları ekleri içerir.
- **Ne zaman:** Agent davranışını değiştiren süreç/disiplin skillerini yazmak ve gerçekten işe yaradığını kanıtlamak. · **Ne zaman değil:** Basit başvuru/format skilleri için ağır (skill-creator yeterli). superpowers:test-driven-development'ı ön koşul sayar. Codex'te: alt-agent baskı testleri ayrı `codex exec` oturumlarıyla yapılır; skill yolu `~/.agents/skills/` (skill bunu kendisi belirtir).
- **Teknoloji:** markdown, graphviz · **Paketler:** graphviz (isteğe bağlı, render-graphs.js için node)
- **Claude / Codex:** tam / tam
- **Geliştirici:** obra (kisi, ★303068, son güncelleme 2026-10-21, lisans MIT)
- **Durum:** tercih · **Örtüşme:** skill-yazimi → tamamlayıcı · **Roller:** skill-gelistirici
- **Boyut:** 107 KB (SKILL.md 16.3 KB, yük orta)
- **İnceleme:** incelendi · kalite 5/5 — Karar: TUT (tamamlayıcı). Skill'in işe yaradığını test etme disiplini başka hiçbir sürümde yok; çok harness'li yol bilgisi var. 27 KB + ekler ağır. skill-creator birincil kalır (eval altyapısı ve daha geniş kapsam), bu onu tamamlar.
