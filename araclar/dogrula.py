#!/usr/bin/env python3
"""Tutarlılık kontrolü. Hata varsa çıkış kodu 1.

- Her registry kaydının klasörü + SKILL.md + KAYNAK.md var mı
- Arşivde registry'de olmayan klasör var mı
- 'tercih' durumunda aynı isimden iki kayıt var mı
- Roller/profiller var olan skillere/rollere mi bakıyor
- Bir rol aynı örtüşme grubundan en fazla 1 birincil + 1 tamamlayıcı alıyor mu
- Kaynaklar.json yıldızlı repoların hepsini kapsıyor mu (--github ile)
"""
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import ARSIV, KAYNAKLAR, KOK, REGISTRY, json_oku, klasor_hash  # noqa: E402


def main():
    hatalar, uyarilar = [], []
    skiller = json_oku(REGISTRY)["skiller"]
    ids = {s["id"]: s for s in skiller}
    for s in skiller:
        k = KOK / s["yol"]
        if not (k / "SKILL.md").exists():
            hatalar.append(f"SKILL.md yok: {s['yol']}")
        if not (k / "KAYNAK.md").exists():
            hatalar.append(f"KAYNAK.md yok: {s['yol']}")
        if k.exists() and s.get("ana_hash") and klasor_hash(k) != s["ana_hash"]:
            hatalar.append(f"arşivdeki dosyalar registry ile uyuşmuyor (elle değiştirilmiş?): {s['yol']}")
        for arac, v in (s.get("varyantlar") or {}).items():
            if not (KOK / v / "SKILL.md").exists():
                hatalar.append(f"araç sürümü eksik: {s['id']} -> {v}")
            elif s.get("varyant_hash", {}).get(arac) and klasor_hash(KOK / v) != s["varyant_hash"][arac]:
                hatalar.append(f"araç sürümü registry ile uyuşmuyor: {v}")
    for s in skiller:
        if s.get("ucret") == "belirsiz" and not s.get("gizli"):
            uyarilar.append(f"ücret sınıflandırılmadı: {s['id']} ({s.get('ucret_notu', '')[:90]})")
        if "ucret" not in s:
            hatalar.append(f"ücret alanı yok: {s['id']} (arsiv-yerlestir.py çalıştır)")
    eksik_gel = sorted({s["repo"] for s in skiller if not s.get("gelistirici")})
    if eksik_gel:
        uyarilar.append(f"geliştirici bilgisi yok (değerlendirme puanı düşük çıkar): {', '.join(eksik_gel[:6])} "
                        "-> python3 araclar/gelistirici-bilgisi.py && python3 araclar/arsiv-yerlestir.py")
    kayitli = {str((KOK / s["yol"]).resolve()) for s in skiller}
    for sm in ARSIV.rglob("KAYNAK.md"):
        if str(sm.parent.resolve()) not in kayitli:
            hatalar.append(f"registry'de olmayan klasör: {sm.parent.relative_to(KOK)}")
    for ad, n in Counter(s["ad"] for s in skiller if s["durum"] == "tercih").items():
        if n > 1:
            hatalar.append(f"aynı isimde birden fazla 'tercih': {ad}")
    for f in sorted((KOK / "roller").glob("*.json")):
        r = json_oku(f)
        for x in r["cekirdek"] + r.get("opsiyonel", []):
            if x not in ids and not any(s["ad"] == x for s in skiller):
                hatalar.append(f"rol {f.stem}: skill yok -> {x}")
        for x in r["cekirdek"] + r.get("opsiyonel", []):
            s = ids.get(x) or next((y for y in skiller if y["ad"] == x and y["durum"] == "tercih"), None)
            if s and (s.get("kaynak_durumu") in ("kaynakta-kaldirildi", "kayip") or s.get("ortusme_rolu") == "emekli"):
                uyarilar.append(f"rol {f.stem}: '{x}' emekli/kaynakta kaldırılmış; arşiv kopyası kullanılıyor (yerine yenisini düşün)")
        for x in r["cekirdek"]:
            s = ids.get(x) or next((y for y in skiller if y["ad"] == x and y["durum"] == "tercih"), None)
            if s and s.get("ucret") == "ucretli" and "ucretli_bilincli" not in r:
                uyarilar.append(f"rol {f.stem}: çekirdekte ÜCRETLİ skill '{x}' (ücretsiz alternatif varsa çekirdeğe onu koy; "
                                "rol bilinçli olarak ücretliyse rol dosyasına \"ucretli_bilincli\": \"gerekçe\" ekle)")
            if s and s.get("inceleme") == "yeniden-incelenecek":
                uyarilar.append(f"rol {f.stem}: çekirdek skill '{x}' güncellemeden sonra yeniden incelenmeli")
        gruplar = Counter()
        for x in r["cekirdek"]:
            s = ids.get(x)
            if s and s.get("ortusme_grubu"):
                gruplar[(s["ortusme_grubu"], s.get("ortusme_rolu"))] += 1
        for (g, rol), n in gruplar.items():
            if rol == "birincil" and n > 1:
                uyarilar.append(f"rol {f.stem}: '{g}' grubundan {n} birincil skill")
    # Örtüşme grupları: 'alternatif' üyesi olan grubun mutlaka bir 'birincil'i olmalı (yoksa alternatif neye alternatif?)
    gruplar = {}
    for s in skiller:
        if s.get("ortusme_grubu"):
            gruplar.setdefault(s["ortusme_grubu"], []).append(s)
    for g, uyeler in sorted(gruplar.items()):
        roller_g = {u.get("ortusme_rolu") for u in uyeler}
        if "alternatif" in roller_g and "birincil" not in roller_g:
            uyarilar.append(f"örtüşme grubu '{g}': alternatifler var ama birincil yok ({', '.join(u['id'] for u in uyeler[:4])}…)")
        gecersiz = roller_g - {"birincil", "tamamlayıcı", "alternatif", "emekli", None}
        if gecersiz:
            hatalar.append(f"örtüşme grubu '{g}': geçersiz rol değeri {sorted(map(str, gecersiz))}")
    roller = {f.stem for f in (KOK / "roller").glob("*.json")}
    for f in sorted((KOK / "profiller").glob("*.json")):
        p = json_oku(f)
        for r in p["roller"]:
            if r not in roller:
                hatalar.append(f"profil {f.stem}: rol yok -> {r}")
        for x in p.get("ek_skiller", []):
            if x not in ids and not any(s["ad"] == x for s in skiller):
                hatalar.append(f"profil {f.stem}: skill yok -> {x}")
    # PROMPT UYUMU: promptlar/11 (başka projenin agent'ı) sabit bilgi içermez; her şeyi bu yapılardan okur.
    # Kütüphane ne kadar büyürse büyüsün bu sözleşme bozulmamalı.
    import re as _re
    p11 = KOK / "promptlar" / "11-guvenilir-skill-secimi-mevcut-proje.md"
    if p11.exists():
        for f in set(_re.findall(r"~/Documents/SkillKutuphanesi/([\w./-]+\.(?:md|json|py))", p11.read_text(encoding="utf-8"))):
            if not (KOK / f).exists():
                hatalar.append(f"prompt 11 olmayan dosyaya bakıyor: {f}")
    for s in skiller:  # prompt 11'deki kanıt sorgusunun okuduğu alanlar
        if not all(k in s for k in ("id", "ad", "durum", "degerlendirme", "ucret", "uyum", "yol", "repo", "teknoloji_oto")) \
                or "puan" not in s["degerlendirme"] or "codex" not in s["uyum"]:
            hatalar.append(f"prompt uyumu: {s['id']} kaydında kanıt alanı eksik (arsiv-yerlestir.py çalıştır)")
    gel = json_oku(KOK / "gelistiriciler.json", {"repolar": {}})
    guvensiz = sorted({s["repo"] for s in skiller if not (s.get("gelistirici") or {}).get("guven")})
    if guvensiz:
        uyarilar.append(f"prompt uyumu: kaynak güveni yok: {', '.join(guvensiz[:5])} -> gelistirici-bilgisi.py, arsiv-yerlestir.py, katalog-uret.py")
    rehber = KOK / "notlar" / "guven-siralamasi.md"
    if not rehber.exists():
        hatalar.append("prompt uyumu: notlar/guven-siralamasi.md yok -> katalog-uret.py")
    else:
        t = rehber.read_text(encoding="utf-8")
        for b in ("## 0.", "## 1.", "## 2.", "## 3.", "## 4."):
            if b not in t:
                hatalar.append(f"prompt uyumu: guven-siralamasi.md bölümü eksik: {b}")
        eksik_r = [r for r, v in gel["repolar"].items() if (v.get("guven") or {}).get("sira") or (v.get("guven") or {}).get("referans_sira")]
        eksik_r = [r for r in eksik_r if f"| {r} |" not in t]
        if eksik_r or gel.get("guncelleme", "") not in t:
            uyarilar.append(f"prompt uyumu: guven-siralamasi.md eski ({', '.join(eksik_r[:4]) or 'tarih'}) -> katalog-uret.py")
    # Prompt 11'in andığı komut bayrakları ve ön kontrol kodları skill-ekle.py'de gerçekten var mı? (yeniden adlandırma promptu sessizce bozmasın)
    if p11.exists():
        ptxt = p11.read_text(encoding="utf-8")
        ekle_kaynak = (KOK / "araclar" / "skill-ekle.py").read_text(encoding="utf-8")
        for bayrak in sorted(set(_re.findall(r"(?<![\w-])(--[a-z]+(?:-[a-z]+)*)", ptxt))):
            if bayrak not in ekle_kaynak and bayrak not in ("--porcelain", "--skip-git-repo-check"):
                hatalar.append(f"prompt 11 olmayan bayrağı anıyor: {bayrak} (skill-ekle.py)")
        kodlar04 = set(_re.findall(r"^\| `([a-z]+(?:-[a-z]+)+)` \|", (KOK / "rehber" / "04-kontrol-listesi.md").read_text(encoding="utf-8"), _re.M))
        for kod in sorted(set(_re.findall(r"`([a-z]+(?:-[a-z]+)+)`", ptxt)) & kodlar04):
            if kod not in ekle_kaynak:
                hatalar.append(f"prompt 11 olmayan ön kontrol kodunu anıyor: {kod} (skill-ekle.py)")
        for jeton in ("kaynak-yok", "emekli"):  # prompt 11 ADIM 10: --durum çıktısında geçmesi beklenen sözcükler
            if jeton in ptxt and jeton not in ekle_kaynak:
                hatalar.append(f"prompt 11 --durum çıktısında '{jeton}' bekliyor ama skill-ekle.py üretmiyor")
    rehber2 = KOK / "notlar" / "guven-siralamasi.md"
    if rehber2.exists() and "| Kart |" not in rehber2.read_text(encoding="utf-8"):
        hatalar.append("prompt uyumu: guven-siralamasi.md bölüm 3'te 'Kart' sütunu yok (prompt 11 ADIM 3 buna dayanır)")
    # Roldeki bir skill son kayıttan beri başka bir KAYNAĞA geçtiyse (öncelik/yeni kaynak yüzünden) fark edilsin
    git_eski = subprocess.run(["git", "show", "HEAD:registry.json"], cwd=KOK, capture_output=True, text=True)
    if git_eski.returncode == 0:
        try:
            eski_reg = {x["id"]: x["repo"] for x in json.loads(git_eski.stdout)["skiller"]}
            eski_tercih = {x["ad"]: x["repo"] for x in json.loads(git_eski.stdout)["skiller"] if x["durum"] == "tercih"}
            for f in sorted((KOK / "roller").glob("*.json")):
                r = json_oku(f)
                for x in r["cekirdek"] + r.get("opsiyonel", []):
                    simdi = ids.get(x) or next((y for y in skiller if y["ad"] == x and y["durum"] == "tercih"), None)
                    once = eski_reg.get(x) or eski_tercih.get(x)
                    if simdi and once and simdi["repo"] != once:
                        uyarilar.append(f"rol {f.stem}: '{x}' kaynağı değişti ({once} -> {simdi['repo']}); rolün istediği sürüm bu mu? "
                                        "(sabitlemek için registry.json'da durum_elle)")
        except (ValueError, KeyError):
            pass
    kartlar = (KOK / "notlar" / "referans" / "tasarim-teknolojileri.md").read_text(encoding="utf-8") + \
        (KOK / "notlar" / "referans" / "kutuphaneler.md").read_text(encoding="utf-8")
    kartsiz = [k["repo"] for k in json_oku(KAYNAKLAR)["repolar"] if k["tip"] in ("T5", "T6")
               and f"`{k['repo']}`" not in kartlar and f"| {k['repo']} |" not in kartlar]
    if kartsiz:
        uyarilar.append(f"prompt uyumu: referans kütüphanesinin kartı/satırı yok: {', '.join(kartsiz[:5])} "
                        "-> notlar/referans/tasarim-teknolojileri.md (T6 kart) ya da kutuphaneler.md (T5 satır)")
    # Skillerin kendi .gitignore'u yüzünden git'e girmeyen arşiv dosyası var mı? (git yedeği eksik kalır)
    gi = subprocess.run(["git", "status", "--ignored", "--porcelain", "arsiv"], cwd=KOK, capture_output=True, text=True)
    from ortak import GURULTU
    for satir in gi.stdout.splitlines():
        if satir.startswith("!! ") and not GURULTU.search(satir[3:].rstrip("/")):
            hatalar.append(f"git'e girmeyen arşiv dosyası (skill'in kendi .gitignore'u): {satir[3:]} -> `git add -f arsiv`")
    if "--github" in sys.argv:
        r = subprocess.run(["gh", "api", "graphql", "--paginate", "-f",
                            "query=query($endCursor:String){viewer{starredRepositories(first:100,after:$endCursor)"
                            "{pageInfo{hasNextPage endCursor} nodes{nameWithOwner}}}}",
                            "--jq", ".data.viewer.starredRepositories.nodes[].nameWithOwner"],
                           capture_output=True, text=True)
        if r.returncode != 0 or not r.stdout.strip():
            uyarilar.append("GitHub yıldız listesi okunamadı (gh auth status?); yeni repo kontrolü YAPILMADI")
        tanimli = {k["repo"] for k in json_oku(KAYNAKLAR)["repolar"]}
        # Skill listesindeki ('Yapay Zeka Skillleri') ama kütüphanede olmayan repolar: yeni eklenecek skill kaynakları
        hs = json_oku(KAYNAKLAR).get("github_skill_listesi", "yapay-zeka-skillleri")
        # Listedeki TÜM öğeler (GitHub sayfa başına 100 öğe verir; sayfalanmazsa yeni eklenen repolar kaçar)
        import importlib.util
        spec = importlib.util.spec_from_file_location("gsl", Path(__file__).parent / "github-skill-listesi.py")
        gsl = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gsl)
        try:
            liste_repolari = [x["nameWithOwner"] for l in gsl.listeler() if l["slug"] == hs for x in l["items"]["nodes"] if x]
        except RuntimeError:
            liste_repolari = []
            uyarilar.append("GitHub skill listesi okunamadı; YENİ SKILL REPOSU kontrolü YAPILMADI")
        for repo in liste_repolari:
            if repo not in tanimli:
                uyarilar.append(f"YENİ SKILL REPOSU (skill listesinde, kütüphanede yok): {repo} -> rehber/03-yeni-skill-ekleme.md")
        for repo in r.stdout.split():
            if repo not in tanimli:
                uyarilar.append(f"yıldızlı ama kaynaklar.json'da yok: {repo}")
    for u in uyarilar:
        print("UYARI:", u)
    for h in hatalar:
        print("HATA:", h)
    print(f"{len(skiller)} skill · {len(hatalar)} hata · {len(uyarilar)} uyarı")
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()
