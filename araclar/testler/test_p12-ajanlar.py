#!/usr/bin/env python3
"""P12 testleri: kütüphanenin kendi ajanları (araclar/ajan-uret.py) ve dogrula.py'deki ajan denetimi.

Yalnız geçici klasör ve sahte veri kullanır; gerçek kütüphane dosyalarına yalnız OKUMA için bakar (gerçek ajan kaynağı tutarlı mı),
gerçek ev klasörlerine bakmaz, ağ kullanmaz. Son satır 'N/N test geçti'; çıkış 0 yalnız hepsi geçerse. test.py'yi çağırmaz.
"""
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent.parent
KOK = ARACLAR.parent
sys.path.insert(0, str(ARACLAR))

SONUC = []
GECICI = []


def yukle(dosya, ad):
    spec = importlib.util.spec_from_file_location(ad, dosya)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


au = yukle(ARACLAR / "ajan-uret.py", "ajan_uret_p12")
dg = yukle(ARACLAR / "dogrula.py", "dogrula_p12")


def t(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-500:]}"))


def kok_yap(dosyalar):
    k = Path(tempfile.mkdtemp(prefix="p12-"))
    GECICI.append(k)
    for yol, metin in dosyalar.items():
        f = k / yol
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(metin, encoding="utf-8")
    return k


def var(liste, parca):
    return any(parca in x for x in liste)


ORTAK = "# Ortak\n1. Kural bir.\n"


def ajan(ad="kutuphane-deneme", model="sonnet", effort="medium", tools=None, govde="# görev\nİş: `rehber/01-x.md` oku.\n", desc='Deneme ajanı: "kontrol et" için kullan.'):
    bas = [f"name: {ad}", f"description: {desc}", f"model: {model}", f"effort: {effort}"] + ([f"tools: {tools}"] if tools else [])
    return "---\n" + "\n".join(bas) + "\n---\n\n" + govde


TEMEL = {"ajanlar/ORTAK.md": ORTAK, "ajanlar/kutuphane-deneme.md": ajan(), "rehber/01-x.md": "x\n"}

# 1 ajanlar/ yok -> sessiz
k = kok_yap({"CLAUDE.md": "x\n"})
t("1a ajanlar/ yok: denetim mesaj vermez", au.ajan_denetimi(k) == ([], []) and dg.ajan_denetimi(k) == ([], []))
yaz, sil, h = au.uret(k)
t("1b ajanlar/ yok: üretim hata döner, dosya yazmaz", h and not yaz and not (k / ".claude").exists())

# 2 üretim
k = kok_yap(dict(TEMEL))
h, u = au.ajan_denetimi(k)
t("2a üretilmeden önce: iki dosya da 'yok' HATA", len(h) == 2 and var(h, ".claude/agents/kutuphane-deneme.md yok") and var(h, ".codex/agents/kutuphane-deneme.toml yok"), h)
yaz, sil, h = au.uret(k)
t("2b üretim: 2 dosya yazıldı, hata yok", sorted(yaz) == [".claude/agents/kutuphane-deneme.md", ".codex/agents/kutuphane-deneme.toml"] and not h and not sil, (yaz, h))
t("2c üretimden sonra denetim temiz (ajan-uret ve dogrula)", au.ajan_denetimi(k) == ([], []) and dg.ajan_denetimi(k) == ([], []))
md = (k / ".claude/agents/kutuphane-deneme.md").read_text(encoding="utf-8")
t("2d Claude dosyası: başlık alanları ve işaret satırı", md.startswith("---\nname: kutuphane-deneme\n") and "\nmodel: sonnet\n" in md and "\neffort: medium\n" in md
  and au.ISARET in md and "tools:" not in md)
t("2e Claude dosyası: description tırnaklı ve içindeki tırnak kaçışlı", '\ndescription: "Deneme ajanı: \\"kontrol et\\" için kullan."\n' in md, md[:300])
t("2f Claude dosyası: ortak kurallar ve görev tanımı gövdede", "Kural bir." in md and "İş: `rehber/01-x.md` oku." in md and md.index("Kural bir.") < md.index("İş:"))
tm = tomllib.loads((k / ".codex/agents/kutuphane-deneme.toml").read_text(encoding="utf-8"))
t("2g Codex dosyası geçerli TOML: name, description, çaba, talimat; model yok",
  tm.get("name") == "kutuphane-deneme" and tm.get("model_reasoning_effort") == "medium" and "Kural bir." in tm.get("developer_instructions", "")
  and tm.get("description") == 'Deneme ajanı: "kontrol et" için kullan.' and "model" not in tm, tm)
yaz2, sil2, h2 = au.uret(k)
t("2h ikinci üretim hiçbir şey yazmaz (idempotent)", not yaz2 and not sil2 and not h2)

# 3 tools alanı
k = kok_yap({**TEMEL, "ajanlar/kutuphane-deneme.md": ajan(tools="Read, Grep, Glob, Bash")})
au.uret(k)
t("3a tools alanı Claude dosyasına yazılır, Codex'e yazılmaz", "\ntools: Read, Grep, Glob, Bash\n" in (k / ".claude/agents/kutuphane-deneme.md").read_text(encoding="utf-8")
  and "tools" not in tomllib.loads((k / ".codex/agents/kutuphane-deneme.toml").read_text(encoding="utf-8")))
k = kok_yap({**TEMEL, "ajanlar/kutuphane-deneme.md": ajan(tools="Read; rm -rf")})
t("3b bozuk tools -> HATA", var(au.kaynak_hatalari(k), "tools virgülle"))

# 4 kaynak hataları
for no, (degisim, parca) in enumerate([
        ({"ajanlar/kutuphane-deneme.md": ajan(ad="kutuphane-baska")}, "name alanı dosya adıyla aynı"),
        ({"ajanlar/kutuphane-deneme.md": ajan(model="gpt-x")}, "model geçersiz"),
        ({"ajanlar/kutuphane-deneme.md": ajan(effort="cok")}, "effort geçersiz"),
        ({"ajanlar/kutuphane-deneme.md": ajan(desc="")}, "description boş"),
        ({"ajanlar/kutuphane-deneme.md": ajan(govde="")}, "görev tanımı boş"),
        ({"ajanlar/kutuphane-deneme.md": ajan().replace("effort: medium", "effort: medium\nrenk: mavi")}, "bilinmeyen başlık alanı 'renk'"),
        ({"ajanlar/kutuphane-deneme.md": ajan(govde="# g\n`rehber/99-yok.md` oku.\n")}, "olmayan dosyaya işaret ediyor: rehber/99-yok.md"),
        ({"ajanlar/kutuphane-deneme.md": "başlık bloğu yok\n"}, "name alanı dosya adıyla aynı"),
], 1):
    k = kok_yap({**TEMEL, **degisim})
    h = au.kaynak_hatalari(k)
    t(f"4.{no} kaynak hatası yakalanır: {parca}", var(h, parca), h)
    hd, _ = dg.ajan_denetimi(k)
    yaz, sil, hu = au.uret(k)
    t(f"4.{no}b hatalı kaynakta dogrula HATA verir ve üretim yazmaz", var(hd, parca) and not yaz and hu and not (k / ".claude").exists(), (hd, yaz))
k = kok_yap({"ajanlar/kutuphane-deneme.md": ajan(), "rehber/01-x.md": "x\n"})
t("4.9 ORTAK.md yok -> HATA", var(au.kaynak_hatalari(k), "ajanlar/ORTAK.md yok"))
k = kok_yap({"ajanlar/ORTAK.md": ORTAK})
t("4.10 ajan kaynağı yok -> HATA", var(au.kaynak_hatalari(k), "kutuphane-*.md yok"))
k = kok_yap({**TEMEL, "ajanlar/ORTAK.md": ORTAK + "Bkz `araclar/yok-arac.py`.\n"})
t("4.11 ORTAK.md olmayan araca işaret ediyor -> HATA", var(au.kaynak_hatalari(k), "ajanlar/ORTAK.md: olmayan dosyaya işaret ediyor: araclar/yok-arac.py"))
k = kok_yap({**TEMEL, "ajanlar/kutuphane-deneme.md": ajan(model="claude-opus-5-5", effort="xhigh")})
t("4.12 tam model kimliği ve xhigh kabul edilir", au.kaynak_hatalari(k) == [])
k = kok_yap({**TEMEL, "ajanlar/kutuphane-deneme.md": ajan(model="inherit", govde="# g\n`araclar/testler/test_p*.py` ve `notlar/<alan>/<kategori>.md` desendir.\n")})
t("4.13 desen içeren yollar (yıldız, köşeli) atıf sayılmaz", au.kaynak_hatalari(k) == [])

# 5 eskime ve elle düzenleme
k = kok_yap(dict(TEMEL))
au.uret(k)
f = k / ".claude/agents/kutuphane-deneme.md"
f.write_text(f.read_text(encoding="utf-8") + "\nelle ek\n", encoding="utf-8")
h, _ = au.ajan_denetimi(k)
t("5a üretilen dosya elle değişti -> HATA (yalnız o dosya)", len(h) == 1 and var(h, ".claude/agents/kutuphane-deneme.md kaynakla aynı değil"), h)
au.uret(k)
t("5b yeniden üretim elle eki siler, denetim temiz", "elle ek" not in f.read_text(encoding="utf-8") and au.ajan_denetimi(k) == ([], []))
(k / "ajanlar/ORTAK.md").write_text(ORTAK + "2. Kural iki.\n", encoding="utf-8")
h, _ = au.ajan_denetimi(k)
t("5c ortak kural değişti -> iki üretilen dosya da eski", len(h) == 2 and all("kaynakla aynı değil" in x for x in h), h)
au.uret(k)
t("5d yeniden üretim yeni kuralı iki dosyaya da taşır", "Kural iki." in f.read_text(encoding="utf-8")
  and "Kural iki." in tomllib.loads((k / ".codex/agents/kutuphane-deneme.toml").read_text(encoding="utf-8"))["developer_instructions"])

# 6 kaynağı silinen ajan ve elle yazılmış yabancı dosya
k = kok_yap({**TEMEL, "ajanlar/kutuphane-ikinci.md": ajan(ad="kutuphane-ikinci")})
au.uret(k)
(k / ".claude/agents/benim-ajanim.md").write_text("---\nname: benim-ajanim\n---\nelle\n", encoding="utf-8")
(k / ".claude/agents/kutuphane-elle.md").write_text("---\nname: kutuphane-elle\n---\nelle yazıldı, işaret yok\n", encoding="utf-8")
(k / "ajanlar/kutuphane-ikinci.md").unlink()
h, _ = au.ajan_denetimi(k)
t("6a kaynağı silinen ajanın üretilmiş dosyaları HATA", len(h) == 2 and all("kaynağı kalmamış" in x for x in h), h)
yaz, sil, hh = au.uret(k)
t("6b üretim yalnız kendi ürettiği fazlaları siler", sorted(sil) == [".claude/agents/kutuphane-ikinci.md", ".codex/agents/kutuphane-ikinci.toml"] and not hh
  and (k / ".claude/agents/benim-ajanim.md").is_file() and (k / ".claude/agents/kutuphane-elle.md").is_file(), sil)
t("6c sonra denetim temiz", au.ajan_denetimi(k) == ([], []))

# 7 komut satırı
k = kok_yap(dict(TEMEL))
r = subprocess.run([sys.executable, str(ARACLAR / "ajan-uret.py"), "--kontrol", "--kok", str(k)], capture_output=True, text=True)
t("7a --kontrol üretilmemiş kökte çıkış 1 ve yazmaz", r.returncode == 1 and "HATA:" in r.stdout and not (k / ".claude").exists(), r.stdout)
r = subprocess.run([sys.executable, str(ARACLAR / "ajan-uret.py"), "--kok", str(k)], capture_output=True, text=True)
t("7b üretim çıkış 0", r.returncode == 0 and "2 dosya yazıldı" in r.stdout, r.stdout)
r = subprocess.run([sys.executable, str(ARACLAR / "ajan-uret.py"), "--kontrol", "--kok", str(k)], capture_output=True, text=True)
t("7c sonra --kontrol çıkış 0", r.returncode == 0 and "0 hata" in r.stdout, r.stdout)
r = subprocess.run([sys.executable, str(ARACLAR / "ajan-uret.py"), "--help"], capture_output=True, text=True)
t("7d --help çıkış 0 ve hiçbir şey yazmaz", r.returncode == 0 and "--kontrol" in r.stdout)

# 8 dogrula bağlantısı ve belge taraması
h, u = dg.belge_ve_kayit_denetimleri(kok_yap({**TEMEL}), [])
t("8a dogrula toplu denetimi ajan hatasını taşır", var(h, "ajan: .claude/agents/kutuphane-deneme.md yok"), h)
k = kok_yap({**TEMEL, "araclar/ornek.py": '"""ornek\n  --var\n"""\n',
             "ajanlar/kutuphane-deneme.md": ajan(govde="# g\nÇalıştır: `python3 araclar/ornek.py --yok-bayrak`\n")})
h, u = dg.bayrak_denetimi(k)
t("8b ajan görev tanımındaki olmayan bayrak dogrula uyarısı olur", var(u, "--yok-bayrak"), (h, u))

# 9 gerçek kütüphane (yalnız okuma)
if (KOK / "ajanlar").is_dir():
    h, _ = au.ajan_denetimi(KOK)
    t("9a gerçek kütüphane: ajan kaynağı ve üretilen dosyalar tutarlı", h == [], h)
    adlar = [ad for ad, *_ in au.kaynaklar(KOK)]
    t("9b gerçek kütüphane: yedi ajan", adlar == ["kutuphane-denetci", "kutuphane-gelistirici", "kutuphane-guncelleme", "kutuphane-inceleme",
                                              "kutuphane-kaynak", "kutuphane-program", "kutuphane-proje"], adlar)
    den = dict((ad, alan) for ad, alan, *_ in au.kaynaklar(KOK))["kutuphane-denetci"]
    t("9c denetçide dosya düzenleme aracı yok (Edit, Write)", "tools" in den and "Edit" not in den["tools"] and "Write" not in den["tools"], den)
    rehber = (KOK / "rehber" / "15-ajanlar.md").read_text(encoding="utf-8") if (KOK / "rehber" / "15-ajanlar.md").is_file() else ""
    t("9d rehber/15 her ajanı anıyor", all(f"`{a}`" in rehber for a in adlar))
    ana = (KOK / "CLAUDE.md").read_text(encoding="utf-8")
    t("9e CLAUDE.md ajanlar maddesi rehbere ve kaynağa işaret ediyor", "rehber/15-ajanlar.md" in ana and "ajanlar/" in ana)
else:
    print("  BİLGİ: gerçek kütüphanede ajanlar/ yok; 9. grup atlandı")

for g in GECICI:
    shutil.rmtree(g, ignore_errors=True)
basarisiz = [a for a, ok in SONUC if not ok]
print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
sys.exit(1 if basarisiz else 0)
