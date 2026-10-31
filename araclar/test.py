#!/usr/bin/env python3
"""Uçtan uca test: geçici bir projede skill-ekle.py'nin tüm güvenlik senaryolarını dener.
Global klasörlerin test boyunca değişmediğini de kontrol eder. Kütüphaneyi değiştirmez.

Kullanım: python3 araclar/test.py
"""
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import GLOBAL_KLASORLER, KOK, json_oku  # noqa: E402

ARAC = [sys.executable, str(KOK / "araclar" / "skill-ekle.py")]
SONUC = []


def calistir(*args, girdi=None):
    r = subprocess.run(ARAC + [str(a) for a in args], capture_output=True, text=True, stdin=subprocess.DEVNULL)
    return r.returncode, r.stdout + r.stderr


def test(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {ayrinti[-600:]}"))


def parmak_izi():
    h = hashlib.sha256()
    for g in list(GLOBAL_KLASORLER.values()) + [Path.home() / ".openmontage" / ".agents" / "skills"]:
        if g.exists():
            for p in sorted(g.iterdir()):
                if p.name in ("synced", ".system"):  # Claude hesap senkronu / Codex'in kendi yerleşik skilleri
                    continue
                h.update(p.name.encode())
                h.update(str(p.lstat().st_mtime_ns).encode())
    return h.hexdigest()


def agac(p: Path):
    """Proje içeriği (yedek klasörü hariç: her işlem yeni yedek bırakır)."""
    return sorted(str(x.relative_to(p)) for x in p.rglob("*") if "/yedek" not in "/" + str(x.relative_to(p)))


def main():
    once = parmak_izi()
    kok = Path(tempfile.mkdtemp(prefix="skill-test-"))
    proje = kok / "proje"
    proje.mkdir()
    (proje / "AGENTS.md").write_text("# Benim notlarım\n\nBu satır korunmalı.\n", encoding="utf-8")
    (proje / "package.json").write_text('{"dependencies": {"next": "16", "three": "0.186", "gsap": "3.15"}}', encoding="utf-8")
    print(f"Geçici proje: {proje}")

    kod, out = calistir(proje, "--profil", "3d-urun-sergisi", "--kuru")
    test("kuru çalıştırma hiçbir şey kurmaz", not (proje / ".agents").exists() and "ÖN KONTROL" in out, out)
    test("ön kontrol tüm kütüphaneyi tarar", "skill tarandı" in out and "ek-aday" in out, out)
    test("package.json teknolojileri tespit edilir", "next.js" in out and "three.js" in out, out)

    kod, out = calistir(proje, "--profil", "3d-urun-sergisi")
    test("uyarı varken onaysız (etkileşimsiz) kurulum durur", kod == 2 and not (proje / ".agents" / "skills").exists(), out)

    kod, out = calistir(proje, "--profil", "3d-urun-sergisi", "--evet")
    test("profil kurulumu başarılı ve doğrulama temiz", kod == 0 and "doğrulama: ✅" in out, out)
    kilit = json_oku(proje / ".skill-kutuphanesi" / "kilit.json")
    test("kilit dosyası oluştu", kilit and len(kilit["skiller"]) >= 8)
    test("Claude agent dosyaları oluştu", (proje / ".claude" / "agents" / "3d-gelistirici.md").exists())
    test("Codex agent dosyaları oluştu", (proje / ".codex" / "agents" / "3d-gelistirici.toml").exists())
    toml = (proje / ".codex" / "agents" / "3d-gelistirici.toml").read_text(encoding="utf-8")
    test("Codex rol dışı skilleri kapatır", "enabled = false" in toml and "impeccable" in toml)
    test("AGENTS.md'deki kullanıcı metni korunur", "Bu satır korunmalı." in (proje / "AGENTS.md").read_text(encoding="utf-8"))

    farkli = [a for a in kilit["skiller"] if a.endswith("--kutuphane")]
    if farkli:
        sm = (proje / ".agents" / "skills" / farkli[0] / "SKILL.md").read_text(encoding="utf-8")
        test("globalde farklı sürümü olan skill ekli adla kurulur ve name eşitlenir", f"name: {farkli[0]}" in sm)

    c_imp, x_imp = proje / ".claude" / "skills" / "impeccable", proje / ".agents" / "skills" / "impeccable"
    if (KOK / "arsiv" / "_varyantlar" / "impeccable").exists():
        test("araç sürümü: Claude'a gerçek kopya (symlink değil)", c_imp.is_dir() and not c_imp.is_symlink())
        test("araç sürümü: Claude kopyası .claude yolunu, Codex kopyası .agents yolunu kullanır",
             ".claude/skills/impeccable" in (c_imp / "SKILL.md").read_text(encoding="utf-8")
             and ".agents/skills/impeccable" in (x_imp / "SKILL.md").read_text(encoding="utf-8"))
    sym = next((p for p in (proje / ".claude" / "skills").iterdir() if p.is_symlink()), None)
    test("varyantı olmayan skill Claude'a symlink ile bağlanır", sym is not None and (sym / "SKILL.md").exists())

    kod, out = calistir(proje, "--profil", "3d-urun-sergisi", "--evet")
    test("aynı kurulumu tekrar çalıştırmak güvenli (idempotent)", kod == 0, out)

    (proje / ".claude" / "skills" / "benim-skillim").mkdir(parents=True)
    # profille kurulmamış bir kütüphane skill'i seç (rol içerikleri değişse de test sağlam kalsın)
    kurulu = {a.removesuffix("--kutuphane") for a in (json_oku(proje / ".skill-kutuphanesi" / "kilit.json") or {}).get("skiller", {})}
    kendi = next(a for a in ("pixijs-2d", "gsap-core", "d3-viz") if a not in kurulu and not (proje / ".agents" / "skills" / a).exists())
    (proje / ".agents" / "skills" / kendi).mkdir(parents=True)
    (proje / ".agents" / "skills" / kendi / "SKILL.md").write_text(f"---\nname: {kendi}\n---\nbenim\n", encoding="utf-8")
    kod, out = calistir(proje, "--skill", kendi, "--evet")
    test("projedeki kendi skill'inin üzerine yazılmaz", kod == 2 and "projede-kendi-skillin" in out
         and "benim" in (proje / ".agents" / "skills" / kendi / "SKILL.md").read_text(encoding="utf-8"), out)
    shutil.rmtree(proje / ".agents" / "skills" / kendi)

    hedef = next(iter(kilit["skiller"]))
    (proje / ".agents" / "skills" / hedef / "SKILL.md").open("a", encoding="utf-8").write("\nelle eklendi\n")
    kod, out = calistir(proje, "--kaldir", hedef, "--evet")
    test("elle değiştirilmiş skill silinmez", kod == 2 and "elle-degistirilmis" in out, out)
    kod, out = calistir(proje, "--dogrula")
    test("doğrulama elle değişikliği yakalar", kod == 1 and "elle değiştirilmiş" in out, out)

    kod, out = calistir(proje, "--kaldir", "yok-boyle-skill", "--evet")
    test("kütüphaneden gelmeyen skill kaldırılmaz", kod == 2 and "kutuphaneden-degil" in out, out)

    once_agac = agac(proje)
    kod, out = calistir(proje, "--kaldir", "hepsi", "--evet", "--zorla")
    test("hepsini kaldır (zorla, yedekli)", kod == 0 and not any((proje / ".agents" / "skills").iterdir()), out)
    test("kullanıcı metni kaldırmadan sonra da korunur", "Bu satır korunmalı." in (proje / "AGENTS.md").read_text(encoding="utf-8"))
    test("kendi klasörüne (benim-skillim) dokunulmaz", (proje / ".claude" / "skills" / "benim-skillim").exists())
    kod, out = calistir(proje, "--geri-al")
    test("geri al: önceki duruma döner", kod == 0 and agac(proje) == once_agac, out)

    yeni = kok / "tasinmis-proje"
    shutil.move(str(proje), str(yeni))
    kod, out = calistir(yeni, "--dogrula")
    test("proje taşınınca doğrulama uyarır", kod == 1 and "taşınmış" in out, out)
    kod, out = calistir(yeni, "--yenile")
    out2 = calistir(yeni, "--dogrula")[1]
    test("--yenile Codex yollarını düzeltir", "taşınmış" not in out2 and "geçersiz yol" not in out2, out2)

    # --- inceleme sonrası eklenen senaryolar
    p2 = kok / "proje2"
    p2.mkdir()
    kod, out = calistir(p2, "--skill", "gsap-core", "--kuru")
    test("--kuru projeye hiçbir dosya yazmaz", not any(p2.iterdir()), out)

    kod, out = calistir(p2, "--skill", "gsap-core", "--rol-adi", "../../kacis", "--evet", "--zorla")
    test("geçersiz rol adı --zorla ile bile reddedilir (proje dışına yazılamaz)",
         kod == 2 and "gecersiz-rol-adi" in out and not (kok / "kacis.md").exists() and not (p2 / "kacis.md").exists(), out)

    (p2 / ".claude" / "agents").mkdir(parents=True)
    (p2 / ".claude" / "agents" / "planlayici.md").write_text("benim agent'ım\n", encoding="utf-8")
    kod, out = calistir(p2, "--rol", "planlayici", "--evet", "--zorla")
    test("kullanıcının kendi agent dosyasının üzerine yazılmaz",
         kod == 2 and "kendi-agent-dosyan" in out
         and (p2 / ".claude" / "agents" / "planlayici.md").read_text(encoding="utf-8") == "benim agent'ım\n", out)
    shutil.rmtree(p2 / ".claude")

    (p2 / ".agents" / "skills").mkdir(parents=True)
    (p2 / ".claude").mkdir()
    (p2 / ".claude" / "skills").symlink_to("../.agents/skills")
    kod, out = calistir(p2, "--skill", "gsap-core", "--evet", "--zorla")
    test(".claude/skills ve .agents/skills aynı klasörse kurulum yapılmaz", kod == 2 and "ayni-klasor" in out, out)
    (p2 / ".claude" / "skills").unlink()

    kod, out = calistir(p2, "--skill", "gsap-core", "gsap-timeline", "--rol-adi", "animasyoncu", "--evet")
    test("tek tek skill + özel rol adı kurulur", kod == 0, out)
    (p2 / ".agents" / "skills" / "gsap-core" / ".DS_Store").write_bytes(b"x")
    kod, out = calistir(p2, "--dogrula")
    test(".DS_Store elle değişiklik sayılmaz", kod == 0, out)

    import json as _j
    kp = p2 / ".skill-kutuphanesi" / "kilit.json"
    kl = _j.loads(kp.read_text(encoding="utf-8"))
    kl["skiller"]["gsap-timeline"]["kaynak_yol"] = "yok/boyle/bir/yol"
    kl["skiller"]["gsap-timeline"]["klasor_hash"] = "eski"
    kp.write_text(_j.dumps(kl), encoding="utf-8")
    once_tl = (p2 / ".agents" / "skills" / "gsap-timeline" / "SKILL.md").read_bytes()
    kod, out = calistir(p2, "--guncelle", "--evet")
    test("kaynağı kaybolan skill'in yerine başka repo'nun aynı adlı skill'i konmaz",
         "kaynak-yok" in out and (p2 / ".agents" / "skills" / "gsap-timeline" / "SKILL.md").read_bytes() == once_tl, out)

    sys.path.insert(0, str(KOK / "araclar"))
    import importlib.util
    spec = importlib.util.spec_from_file_location("se", KOK / "araclar" / "skill-ekle.py")
    se = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(se)
    sm = kok / "SKILL.md"
    sm.write_bytes(b"---\r\ndescription: x\r\n---\r\n\r\n```yaml\r\nname: ornek\r\n```\r\n")
    se.isim_esitle(sm, "yeni-ad")
    b = sm.read_bytes()
    test("ad eşitleme sadece frontmatter'a dokunur ve CRLF'yi korur",
         b.startswith(b"---\r\nname: yeni-ad\r\n") and b"name: ornek\r\n" in b, b.decode())

    # --- kardeş skill bağımlılıkları (../<kardeş>/ bağlantıları)
    kd = kok / "kardes"
    ana_kok = kok / "baska-kategori" / "ana"  # arşivde kardeşler farklı kategori klasörlerinde durur
    for yer, govde in {ana_kok: "# ana\n", kd / "yan": "[r](../ana/references/x.md) [k](../yok-skill/a.md) [d](../../disari.md)\n"}.items():
        (yer / "references").mkdir(parents=True)
        (yer / "SKILL.md").write_text(f"---\nname: {yer.name}\n---\n{govde}", encoding="utf-8")
    (ana_kok / "references" / "x.md").write_text("x", encoding="utf-8")
    (kd / "yan" / "references" / "r.md").write_text("[a](../../ana/references/x.md) `../ana/` ../anaconda/\n", encoding="utf-8")
    spec_y = importlib.util.spec_from_file_location("ay", KOK / "araclar" / "arsiv-yerlestir.py")
    ay = importlib.util.module_from_spec(spec_y)
    spec_y.loader.exec_module(ay)
    kayit = lambda ad: {"id": ad, "ad": ad, "klasor_adi": ad, "repo": "r/r", "durum": "tercih"}
    kardes, cozulen = ay.kardes_baglantilari(kd / "yan", {"ana": [(kayit("ana"), ana_kok)]}, kayit("yan"))
    test("arşiv: ../<kardeş>/ bağlantısı kardeş bağımlılığı sayılır, kırık sayılmaz",
         kardes == {"ana": {"id": "ana", "dosya_sayisi": 2}} and cozulen == {"../ana/references/x.md"}
         and "../ana/references/x.md" in ay.kirik_baglantilar(kd / "yan"), str((kardes, cozulen)))
    se.kardes_yollarini_yeniden_adlandir(kd / "yan", {"ana": "ana--kutuphane"})
    test("kurulum: kardeş yolları dosya derinliğine göre projedeki ada çevrilir",
         "](../ana--kutuphane/references/x.md)" in (kd / "yan" / "SKILL.md").read_text(encoding="utf-8")
         and (kd / "yan" / "references" / "r.md").read_text(encoding="utf-8")
         == "[a](../../ana--kutuphane/references/x.md) `../ana/` ../anaconda/\n",
         (kd / "yan" / "references" / "r.md").read_text(encoding="utf-8"))

    reg = json_oku(KOK / "registry.json")["skiller"]
    idler = {s["id"]: s for s in reg}
    ornek = next((s for s in reg if s["durum"] == "tercih" and not s.get("kirik_baglantilar")
                  and len(s.get("kardes_bagimliliklari") or {}) == 1
                  and not idler[next(iter(s["kardes_bagimliliklari"].values()))["id"]].get("kardes_bagimliliklari")), None)
    if ornek:
        kad, bilgi = next(iter(ornek["kardes_bagimliliklari"].items()))
        p3 = kok / "proje3"
        p3.mkdir()
        kod, out = calistir(p3, "--skill", ornek["id"], "--kuru")
        test("kardeş skill kurulmuyorsa uyarılır", "kardes-eksik" in out and "kirik-baglanti" not in out, out)
        kod, out = calistir(p3, "--skill", ornek["id"], bilgi["id"], "--evet")
        kl3 = json_oku(p3 / ".skill-kutuphanesi" / "kilit.json")["skiller"]
        ad3 = next(a for a, k in kl3.items() if k["id"] == ornek["id"])
        kardes_ad = next(a for a, k in kl3.items() if k["id"] == bilgi["id"])
        kok3 = p3 / ".agents" / "skills" / ad3
        import os as _os, re as _re
        kirik3 = [h for f in kok3.rglob("*.md") for h in _re.findall(r"\]\(([^)\s#]+)", f.read_text(encoding="utf-8"))
                  if h.startswith("../") and _os.path.normpath(f.parent / h).startswith(str(kok3.parent))
                  and not Path(_os.path.normpath(f.parent / h)).exists()]
        test(f"kardeşle birlikte kurulunca ../{kad}/ bağlantıları projede çözülür (kardeş adı: {kardes_ad})",
             kod == 0 and "kardes-eksik" not in out and not kirik3 and kl3[ad3].get("kardes") == {kad: kardes_ad},
             out + str(kirik3))

    kod, out = calistir(p2, "--kaldir", "gsap-core", "--evet")
    kod2, out2 = calistir(p2, "--geri-al")
    test("geri al: kaldırılan skill geri gelir", kod2 == 0 and (p2 / ".agents" / "skills" / "gsap-core" / "SKILL.md").exists(), out2)
    ad = out2.strip().split("--geri-al ")[-1].split()[0] if "--geri-al " in out2 else ""
    kod3, out3 = calistir(p2, "--geri-al", ad)
    test("geri almanın kendisi de geri alınabilir", kod3 == 0 and not (p2 / ".agents" / "skills" / "gsap-core").exists(), out3)

    # Kaynakta kaldırılan (emekli) skill kurulmak istenirse ön kontrol uyarır
    reg = json_oku(KOK / "registry.json")["skiller"]
    emekli = next((s for s in reg if s.get("kaynak_durumu") == "kaynakta-kaldirildi" and s["durum"] == "tercih"), None)
    if emekli:
        p3 = kok / "proje-emekli"
        p3.mkdir()
        kod, out = calistir(p3, "--skill", emekli["id"], "--kuru")
        test("emekli skill için ön kontrol 'kaynakta-kaldirildi' uyarısı verir", "kaynakta-kaldirildi" in out and not any(p3.iterdir()), out)

    # 'emekli' rolündeki (eski/yerine geçeni olan) skill ön kontrolde uyarı verir
    om_eski = next((s for s in reg if s.get("ortusme_rolu") == "emekli" and s["repo"] == "calesthio/OpenMontage" and s["durum"] == "tercih"), None)
    if om_eski:
        p4 = kok / "proje-emekli-om"
        p4.mkdir()
        kod, out = calistir(p4, "--skill", om_eski["id"], "--kuru")
        test("emekli (eski kopya) skill için ön kontrol 'emekli' uyarısı verir", "[UYARI] emekli" in out, out)

    # Ücretli skill ön kontrolde 'ucretli' uyarısı verir; ücretsiz skill vermez
    ucretli = next((s for s in reg if s.get("ucret") == "ucretli" and not s.get("gizli") and s["durum"] == "tercih"), None)
    ucretsiz = next((s for s in reg if s.get("ucret") == "ucretsiz" and not s.get("gizli") and s["durum"] == "tercih"
                     and not s.get("globalde")), None)
    if ucretli and ucretsiz:
        p5 = kok / "proje-ucret"
        p5.mkdir()
        kod, out = calistir(p5, "--skill", ucretli["id"], "--kuru")
        kod2, out2 = calistir(p5, "--skill", ucretsiz["id"], "--kuru")
        test("ücretli skill 'ucretli' uyarısı verir, ücretsiz vermez",
             "[UYARI] ucretli" in out and "[UYARI] ucretli" not in out2, out + out2)

    # Ücret dedektörü: yeni arşiv (.arsiv-yeni) yolundan okur; İngilizce "replicate"/"prepaid" yanlış pozitif vermez
    import importlib.util
    spec = importlib.util.spec_from_file_location("yerlestir", KOK / "araclar" / "arsiv-yerlestir.py")
    yer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(yer)
    yeni_arsiv = kok / "arsiv-yeni"
    for ad, metin in (("ucretli-iz", "Set FAL_KEY and call fal.ai"), ("fiil", "Replicate the experiment; book prepaid expenses.")):
        (yeni_arsiv / ad).mkdir(parents=True)
        (yeni_arsiv / ad / "SKILL.md").write_text(f"---\nname: {ad}\n---\n{metin}\n")
    s1 = {"id": "ucretli-iz", "ad": "ucretli-iz", "yol": "arsiv/ucretli-iz", "tip": "T1"}
    s2 = {"id": "fiil", "ad": "fiil", "yol": "arsiv/fiil", "tip": "T1"}
    test("ücret dedektörü yeni arşivdeki SKILL.md'yi okur (yeni skill sessizce 'ücretsiz' sayılmaz)",
         yer.ucret_belirle(s1, {}, yeni_arsiv)[0] == "belirsiz")
    test("'replicate' fiili / 'prepaid' muhasebe terimi ücretli iz sayılmaz", yer.ucret_belirle(s2, {}, yeni_arsiv)[0] == "ucretsiz")

    # Kimlik/tercih ataması KARARLI olmalı (yeni kaynak eşit öncelikte eskinin yerini alamaz; elle tercih ezilmez; tek tercih)
    def kayit(repo, kh, oncelik=3, yol="skills/x"):
        return {"ad": "x", "repo": repo, "kaynak_yol": yol, "_kh": kh, "oncelik": oncelik}
    eski = {("zzz/eski", "skills/x"): {"durum": "tercih", "id": "x"}}
    yeni = yer.kimlik_ata({"x": [kayit("aaa/yeni", "H2"), kayit("zzz/eski", "H1")]}, eski)
    d = {k["repo"]: k for k in yeni}
    test("kimlik: eşit öncelikte alfabetik önce gelen YENİ kaynak eski kaydın tercihini/kimliğini almaz",
         d["zzz/eski"]["durum"] == "tercih" and d["zzz/eski"]["id"] == "x" and d["aaa/yeni"]["durum"] == "alternatif", str(yeni))
    yeni = yer.kimlik_ata({"x": [kayit("aaa/yeni", "H1"), kayit("zzz/eski", "H1")]}, eski)
    test("kimlik: birebir aynı içerikte ESKİ (incelenmiş) kayıt temsilci kalır, yeni kopya olarak notlanır",
         len(yeni) == 1 and yeni[0]["repo"] == "zzz/eski" and any("aaa/yeni" in c for c in yeni[0].get("kopya_kaynaklar", [])), str(yeni))
    eski2 = {("zzz/eski", "skills/x"): {"durum": "tercih", "durum_elle": True, "id": "x"}}
    yeni = yer.kimlik_ata({"x": [kayit("aaa/oto", "H3", oncelik=1), kayit("zzz/eski", "H1", oncelik=5)]}, eski2)
    test("kimlik: elle verilen tercih (durum_elle) otomatik tercihi ezer ve aynı adda TEK tercih kalır",
         sorted(k["durum"] for k in yeni) == ["alternatif", "tercih"]
         and next(k for k in yeni if k["durum"] == "tercih")["repo"] == "zzz/eski", str(yeni))

    # Trend: seviye hesabı, değerlendirme bonusu ve öneride sadece konuya uygun skille bonus
    from ortak import trend_durumu
    from datetime import date as _d, timedelta as _td
    gun = lambda n: (_d.today() - _td(days=n)).isoformat()  # noqa: E731  (testler tarihten bağımsız: hep bugüne göre)
    tr = {"son_tarama": gun(3), "gecmis": {"a/b": {"ilk": gun(30), "son": gun(3), "gorulme": 3},
                                           "c/d": {"ilk": gun(200), "son": gun(60), "gorulme": 1},
                                           "e/f": {"ilk": gun(900), "son": gun(500), "gorulme": 1}}}
    test("trend seviyeleri: trendde / yakinda / gecmiste / yok",
         [(trend_durumu(r, tr) or {}).get("seviye") for r in ("a/b", "c/d", "e/f", "x/y")] == ["trendde", "yakinda", "gecmiste", None])
    tr_eski = {"son_tarama": gun(60), "gecmis": {"a/b": {"ilk": gun(90), "son": gun(60), "gorulme": 3}}}
    test("trend bonusu söner: tarama durursa (60 gün önce) 'trendde' olmaz, 'yakinda'ya düşer",
         trend_durumu("a/b", tr_eski)["seviye"] == "yakinda")
    spec = importlib.util.spec_from_file_location("skillekle", KOK / "araclar" / "skill-ekle.py")
    ekle = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ekle)
    taban = {"id": "x", "aciklama": "android compose helper", "kategori": "b/08-mobil", "teknoloji_oto": [],
             "degerlendirme": {"puan": 80}, "durum": "tercih", "ucret": "ucretsiz"}
    p_yok = ekle.puanla(dict(taban), ["android"], set())[0]
    p_trend = ekle.puanla(dict(taban, trend={"seviye": "trendde"}), ["android"], set())[0]
    p_alakasiz = ekle.puanla(dict(taban, trend={"seviye": "trendde"}), ["video"], set())[0]
    test("öneride trend bonusu: uygun skill öne çıkar, alakasız skill trend yüzünden öneriye girmez",
         p_trend > p_yok and p_alakasiz == 0, f"{p_yok} {p_trend} {p_alakasiz}")

    for g in GLOBAL_KLASORLER.values():
        kod, out = calistir(g, "--skill", "gsap-core", "--evet")
        test(f"güvenlik: {g} reddedilir", kod != 0 and "Güvenlik" in out, out)
        break
    kod, out = calistir(KOK, "--skill", "gsap-core", "--evet")
    test("güvenlik: kütüphanenin kendisi reddedilir", kod != 0 and "Güvenlik" in out, out)

    test("global klasörler test boyunca DEĞİŞMEDİ", parmak_izi() == once)
    shutil.rmtree(kok, ignore_errors=True)
    basarisiz = [a for a, ok in SONUC if not ok]
    print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
    sys.exit(1 if basarisiz else 0)


if __name__ == "__main__":
    main()
