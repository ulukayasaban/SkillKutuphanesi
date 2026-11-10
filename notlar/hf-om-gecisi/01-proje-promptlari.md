# Proje oturumları için hazır promptlar (2. sürüm)

Ne zaman: `00-plan.md` Adım 4 bittikten sonra (planın 5. adımı).
Nasıl: önce **KURALLAR** bloğunu, hemen altına o projenin bölümünü yapıştır. `<PROJE>` yerine proje adını yaz.
Hepsi sadece okur; projede hiçbir şeyi değiştirmez. Onarım için en alttaki ek prompt var.

## KURALLAR (her promptun başına)
```
Bu oturumda sadece inceleme yapacaksın. Kurallar istisnasız:
1. Hiçbir dosyayı değiştirme, silme, taşıma. Yazacağın tek dosya: ~/Documents/Claude/hf-om-raporlar/<PROJE>.md
2. Şu klasörlere hiçbir şey yazma: ~/.claude/skills, ~/.agents, ~/.codex/skills, ~/.openmontage, ~/.hyperframes
3. Şunları çalıştırma: npx skills …, hyperframes update / init / skills / upgrade / clean, npm install, pip install,
   make setup, git pull, git checkout, git reset, git clean, git commit, git push.
4. HyperFrames sürümünü komutla değil dosyadan oku: /usr/local/lib/node_modules/hyperframes/package.json
5. Üretim, render ya da test betiği çalıştırma. Son çalışmanın kaydını oku.
6. "find -L" kullanma (kendini gösteren bağlantı var). Bağlantılar için: find <klasör> -type l, sonra readlink.
7. .env ve anahtar dosyalarını açma, içeriğini yazma.
8. Emin olmadığın her satırın yanına "doğrulanmadı" yaz. Tahmin yürütme.
9. Raporu kısa tut: başlık, madde madde bulgu, en sonda "risk var / yok" ve tek cümle öneri.
```

## 1. IstatistikYoutube
```
Bu projenin HyperFrames ve OpenMontage'a nasıl bağlı olduğunu raporla:
- status/skill-global.yaml içindeki "kullanilan" listesi ve tools/skill_durum.py'nin neyi denetlediği (betiği çalıştırma, oku).
- Son taban testi (duman.sh) kaydı: tarih, sonuç, hangi HyperFrames sürümüyle.
- Bugün kurulu HyperFrames sürümü bu kayıttakinden farklı mı?
- ~/.openmontage yolunu kullanan dosya sayısı ve yolun hâlâ doğru olup olmadığı.
- Bilgisayarın genelindeki skill klasörlerine sabit yol: grep -rIE --exclude-dir=node_modules '/\.(codex|agents|claude)/skills' .
- HyperFrames kendiliğinden güncellenseydi bu projede ne bozulurdu? Kanıtıyla yaz.
```

## 2. Akıl Dışı (Claude oturumunda)
```
Bu projenin skillerini ve bilgisayarın geneline bağımlılığını raporla:
- Projenin içindeki skiller: gerçek klasör mü, bağlantı mı; bağlantıysa nereyi gösteriyor, hedef var mı.
- Adı "--kutuphane" ile biten kopyalar ve aynı adlı genel skilden farkı (sadece var/yok ve ilk satır).
- Kendini gösteren ya da ölü bağlantılar (hyperframes-creative dahil).
- Genel klasöre sabit yol kullanan betikler: grep -rIE --exclude-dir=node_modules '/\.(codex|agents|claude)/skills' ..
  Her biri için: hangi dosya, hangi skill, hedef bugün yerinde mi.
- .codex altındaki toml dosyalarında artık var olmayan yollar.
- "npx … hyperframes" çağıran betikler ve hangi sürümü bekledikleri.
- Yüklü skill listeni ve hyperframes-core skilinin ilk satırını yaz.
```

## 2b. Akıl Dışı (Codex oturumunda)
```
Aynı proje, bu kez Codex gözüyle:
- Şu an gördüğün skillerin listesi ve her birinin geldiği klasör.
- Aynı adla iki yerde duran skill var mı; hangisini kullanıyorsun? Emin değilsen "doğrulanmadı" yaz.
- ~/.codex/config.toml ve proje içindeki .codex ayarlarında var olmayan yol var mı (içerikteki anahtarları yazma).
```

## 3. Psikolojik Danışman Sosyal Medya
```
Bu proje OpenMontage'ı yanlış yerde arıyor olabilir. Raporla:
- "Documents/OpenMontage" ya da başka bir OpenMontage yolu geçen her dosya ve satır (config/, .claude/agents/, .claude/agent-memory/).
- Doğru yol ~/.openmontage. Hangi satırlar yanlış?
- Proje bugüne kadar OpenMontage ya da HyperFrames ile gerçekten üretim yapmış mı? Kanıtı ne?
- Projenin içindeki skiller ve bilgisayarın geneline sabit yol: grep -rIE --exclude-dir=node_modules '/\.(codex|agents|claude)/skills' .
Hiçbir şeyi düzeltme; sadece listele.
```

## 4. Diğer projeler (blenderTest, Etsy-Yeni, AntigravityTest2, IsBasvuruClaude, Yetisio, Tekfen…)
```
Bu proje HyperFrames, OpenMontage ya da bilgisayarın genelindeki skilleri kullanıyor mu? Raporla:
- Projenin içindeki skiller ve varsa kilit dosyası (.agents/skills/kilit.json).
- "hyperframes", "openmontage" ya da genel skill klasörü yolu geçen dosyalar.
- Kullanmıyorsa tek satır: "bağımlılık yok".
```
Etsy-Arif için aynı prompt, şu ekle: `Bu depo Arif'in. git status dışında git komutu çalıştırma; ajan dosyalarına ve elle kurulmuş skillere dokunma.`

## Ek: Onarım (planda adım değil; yalnız arıza çıkarsa)
Ön şart: kütüphane oturumu "tamam" dedi, yedek 24 saatten yeni, o projede başka oturum ya da üretim çalışmıyor.
```
<YAPILACAK İŞ: kütüphane oturumundan gelen madde madde liste>
Kurallar: KURALLAR bloğundaki 2, 3, 4, 6, 7, 8. maddeler aynen geçerli. Ek olarak:
- Başlamadan: touch /tmp/onarim-isareti
- Değiştireceğin her dosyanın önce yanına ".yedek-YYYYAAGG-SSDDSS" kopyasını al.
- Listede olmayan hiçbir dosyaya dokunma.
- Bitince değişen dosyaları yaz: find . -type f -newer /tmp/onarim-isareti | sort
- Raporu ~/Documents/Claude/hf-om-raporlar/<PROJE>-onarim.md dosyasına yaz.
```
