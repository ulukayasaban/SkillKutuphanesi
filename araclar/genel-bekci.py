#!/usr/bin/env python3
"""Genel klasör bekçisi: makinedeki genel skill klasörlerini izler, tabanla karşılaştırır, boşaltma planını YAZDIRIR.

Izlenenler: ~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.gemini/skills (ve ~/.gemini/*/skills), ~/.cursor/skills,
~/.copilot/skills, ~/.claude/commands, ~/.claude/agents, skill kilit dosyası (~/.agents/.skill-lock.json), genel talimat dosyaları
ve tabandaki 'ek_klasorler'. Bilinmeyen ~/.<ad>/skills klasörleri de bulunup bildirilir.
Her girdi için sahip (uygulama, kullanıcı, hyperframes, openmontage, skills aracı, bilinmiyor) ve durum (kalacak, boşaltılacak)
tabanda (notlar/genel-klasor-tabani.json) tutulur. Rapor: YENİ / KAYIP / DEĞİŞTİ / KIRIK BAĞ / YENİ KLASÖR.
YENİ girdiyi yazdığı bilinen bir uygulama varsa (BILINEN_YAZICILAR) karar metni yazanı ve durdurma yolunu da söyler;
--ayrinti uzantı kimliğini ve kanıtın nereden okunacağını ekler.

Salt okuma: makinedeki genel klasörlere, ayar dosyalarına, kabuk dosyalarına YAZMAZ, hiçbir şeyi silmez ya da taşımaz ve
hiçbir komutu çalıştırmaz (--plan yalnız komut metni yazdırır). Yazdığı tek yerler kütüphane içinde: notlar/genel-bekci.md
(rapor) ve yalnız --taban-yaz --evet ile notlar/genel-klasor-tabani.json. Anahtar ve ayar dosyalarının değerlerini ASLA yazdırmaz:
ortam kontrolü dosyaları satır satır okur, yalnız HYPERFRAMES_SKIP_SKILLS satırını sınar, başka hiçbir satırı tutmaz.
Talimat, komut ve ajan dosyalarının içeriğini açmaz (yalnız var mı bakar).

Çıkış kodu rapor kipinde her zaman 0 (--siki ile yalnız 'sorun' durumunda 1). --taban-yaz reddi ve --yedek-dogrula
hatası 1; --plan reddi --siki ile 1.

Kullanım:
  python3 araclar/genel-bekci.py [--ev DIR] [--taban YOL] [--kart YOL] [--rapor YOL | --rapor-yok] [--siki] [--ozet-json] [--ayrinti]
  python3 araclar/genel-bekci.py --taban-yaz [--yenile] [--kalacak YOL ...] [--evet] [--tarih YYYY-AA-GG]
  python3 araclar/genel-bekci.py --plan {1,2,3,4,5a,5b,6,7} [--tarih YYYY-AA-GG] [--siki]
  python3 araclar/genel-bekci.py --yedek-dogrula YEDEK_KLASORU
Rehber: rehber/12-genel-klasor-bosaltma.md
"""
import argparse
import json
import os
import re
import shlex
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import KOK, GURULTU, json_oku, json_yaz  # noqa: E402

BOLGELER = [  # (anahtar, ev'e göre yol, tür)  tür: "skill" = skill klasörü, "liste" = dosya listesi
    ("claude", ".claude/skills", "skill"), ("agents", ".agents/skills", "skill"), ("codex", ".codex/skills", "skill"),
    ("gemini", ".gemini/skills", "skill"), ("cursor", ".cursor/skills", "skill"), ("copilot", ".copilot/skills", "skill"),
    ("komutlar", ".claude/commands", "liste"), ("ajanlar", ".claude/agents", "liste"),
]
KESIF_YOKSAY = {".openmontage", ".Trash", ".trash", ".npm", ".cache", ".local", ".config"}
DOSYALAR = [  # (bölge, yol, tür)
    ("kilit", ".agents/.skill-lock.json", "kilit"),
    ("talimat", ".claude/CLAUDE.md", "talimat"),
    ("talimat", ".codex/AGENTS.md", "talimat"),
    ("talimat", ".gemini/GEMINI.md", "talimat"),
    ("talimat", ".copilot/copilot-instructions.md", "talimat"),
]
IZINLI_VARSAYILAN = [
    {"yol": "~/.claude/skills/synced", "sahip": "uygulama", "neden": "Claude uygulamasının hesap skili senkronu"},
    {"yol": "~/.codex/skills/.system", "sahip": "uygulama", "neden": "Codex'in kendi yerleşik skilleri"},
    {"yol": "~/.cursor/skills-cursor", "sahip": "uygulama", "neden": "Cursor'un kendi yerleşik skilleri"},
]
TOHUM_KALACAK = {"~/.codex/skills/playwright": ("uygulama", "Codex'in playwright kopyası")}
SAHIPLER = ("uygulama", "kullanıcı", "hyperframes", "openmontage", "skills aracı", "bilinmiyor")
DURUMLAR = ("kalacak", "boşaltılacak")
KULLANICI_ADLARI = {"openmontage", "youtube-arama", "nlm-skill", "design-dna"}
ANAHTAR = "HYPERFRAMES_SKIP_SKILLS"
ANAHTAR_RE = re.compile(r"^\s*(?:export\s+)?HYPERFRAMES_SKIP_SKILLS=(?P<q>[\"']?)(?P<v>[^\"'\s#]*)(?P=q)\s*(?:#.*)?$")
ORTAM_DOSYALARI = [".zshenv", ".zshrc", ".claude/settings.json"]
SABIT_SKILL_BOLGELERI = {"claude", "agents", "codex", "gemini", "cursor", "copilot", "kilit"}
BULUNAN_ONEK = ("kesif-", "gemini-")
ADIM_SIRASI = ["3", "4", "5a", "5b", "6"]
SIDDET = {"sorun": 2, "dikkat": 1, "bilgi": 0}
BUYUK = {"temiz": "TEMİZ", "dikkat": "DİKKAT", "sorun": "SORUN"}
KARAR_KLASOR = ("Yeni bir yapay zeka aracı klasörü göründü (rehber/14): {y} — araç ise ek_klasorler'e eklensin mi, "
                "değilse izinli/yoksay mı?")
KARAR_YENI = "Yeni girdi {y} (sahip: {s}): kalacak mı, boşaltılacak mı? Karar sonrası: --taban-yaz --yenile --evet (onay gerekir)."
EK = {0: "0'ında", 1: "1'inde", 2: "2'sinde", 3: "3'ünde"}
# Genel alana kendiliğinden yazdığı bilinen uygulamalar (rehber/12 "Genel alana kendiliğinden yazan uygulamalar"; tek kaynak bu tablo).
# Yalnız YENİ girdinin karar metnine kısa ek ("yazan", "durdurmak") ve --ayrinti satırı (kimlik, kanıt) üretir; sahip sınıfı değişmez.
# Eşleşme, sırayla ilk bulunan kazanır: (1) "adlar": girdi adı (bağda hedef adı) bu listede; kilit ve kaynak aranmaz.
# (2) "kaynak": skill kilidinde o adın source alanında bu owner/ad geçer; ya da "manifest": ~/ altındaki bu JSON dosyasının
# "skills" listesinde o ad var. Kaynak metni ve manifest içeriği yalnız sınanır; saklanmaz, yazdırılmaz.
# Yeni yazıcı: bir satır ekle, test_p2-genel-bekci.py'ye sahte ev testi ekle, rehber/12 bölümüne bir satır yaz.
BILINEN_YAZICILAR = [
    {"ad": "foundry-toolkit", "adlar": ["microsoft-foundry"],
     "yazan": "VS Code Foundry Toolkit uzantısı",
     "durdur": "VS Code ayarı windowsaistudio.autoCheckFoundrySkill=false",
     "kimlik": "ms-windows-ai-studio.windows-ai-studio; her etkinleşmede skill yoksa kurar",
     "kanit": "~/Library/Application Support/Code/logs/<oturum>/window1/exthost/ms-windows-ai-studio.windows-ai-studio/"
              "Foundry Toolkit.log ('[FoundrySkill] ... Installing' satırı)"},
    {"ad": "copilot-for-azure", "kaynak": ["microsoft/azure-skills"],
     "manifest": "~/.agents/.copilot-for-azure-skills-manifest.json",
     "yazan": "VS Code GitHub Copilot for Azure uzantısı",
     "durdur": "kurulum bildiriminde \"Don't Ask Again\" (ayarı yok)",
     "kimlik": "ms-azuretools.vscode-azure-github-copilot; 30 günde bir sorar; ~/.github/hooks/azureSkills* de yazar",
     "kanit": "~/.agents/.copilot-for-azure-skills-manifest.json; ~/Library/Application Support/Code/logs/<oturum>/window1/exthost/"
              "ms-azuretools.vscode-azure-github-copilot/@azure.log; durduğu: ~/Library/Application Support/Code/User/globalStorage/"
              "ms-azuretools.vscode-azure-github-copilot/skills-state.json içinde toastDismissedPermanently: true"},
]
KABUK_IPUCU = (" Olası neden: kabuk dosyasını yeniden yazan bir kurulum betiği silmiş olabilir; HYPERFRAMES_* satırları "
               "dosyanın sonuna geri eklenir (onayla).")


# ------------------------------------------------------------------ yol yardımcıları
class Ev:
    def __init__(self, yol):
        self.yol = str(Path(yol))

    def kisalt(self, p):
        p = str(p)
        if p == self.yol:
            return "~"
        if p.startswith(self.yol.rstrip("/") + "/"):
            return "~/" + p[len(self.yol.rstrip("/")) + 1:]
        return p

    def ac(self, s):
        if s == "~":
            return self.yol
        if s.startswith("~/"):
            return os.path.join(self.yol, s[2:])
        return s


def altinda(yol, kok):
    return yol == kok or yol.startswith(kok.rstrip("/") + "/")


def hedef_kisa(ev, yol_abs):
    """Bağ hedefi: göreliyse bağın klasörüne göre sözdizimsel çözülür (bağ izlenmez), sonra ~/ biçimine kısaltılır."""
    t = os.readlink(yol_abs)
    if not os.path.isabs(t):
        t = os.path.normpath(os.path.join(os.path.dirname(yol_abs), t))
    return ev.kisalt(t)


def olc(ev, yol_abs, bolge):
    """Tek girdinin ölçümü (salt okuma; bağ izlenmez; talimat/komut/ajan dosyalarının içine bakılmaz)."""
    if os.path.islink(yol_abs):
        return {"tur": "bag", "hedef": hedef_kisa(ev, yol_abs), "kirik": not os.path.exists(yol_abs)}
    if os.path.isdir(yol_abs):
        n = b = 0
        kesik = False
        for kok, dirs, files in os.walk(yol_abs, followlinks=False):
            for ad in files + [d for d in dirs if os.path.islink(os.path.join(kok, d))]:
                rel = os.path.relpath(os.path.join(kok, ad), yol_abs)
                if GURULTU.search(rel):
                    continue
                n += 1
                try:
                    b += os.lstat(os.path.join(kok, ad)).st_size
                except OSError:
                    pass
                if n >= 50000:
                    kesik = True
                    break
            dirs[:] = [d for d in dirs if not GURULTU.search(d) and not os.path.islink(os.path.join(kok, d))]
            if kesik:
                break
        o = {"tur": "klasor", "dosya": n, "bayt": b}
        if kesik:
            o["kesik"] = True
        return o
    if bolge in ("komutlar", "ajanlar", "talimat"):
        return {"tur": "dosya"}
    try:
        st = os.lstat(yol_abs)
        return {"tur": "dosya", "bayt": st.st_size, "mtime": int(st.st_mtime)}
    except OSError:
        return {"tur": "dosya"}


# ------------------------------------------------------------------ bölgeler ve tarama
def bolge_listesi(ev, ek_klasorler):
    """[(anahtar, '~/..' yol, tür)]: sabitler, ~/.gemini/*/skills, ek_klasorler, bilinmeyen ~/.<ad>/skills (kesif-)."""
    liste = [(k, "~/" + y, t) for k, y, t in BOLGELER]
    bilinen = {y for _, y, _ in liste}
    gem = os.path.join(ev.yol, ".gemini")
    try:
        adlar = sorted(e.name for e in os.scandir(gem) if e.is_dir(follow_symlinks=False))
    except OSError:
        adlar = []
    for ad in adlar:
        y = f"~/.gemini/{ad}/skills"
        if ad != "skills" and y not in bilinen and os.path.isdir(ev.ac(y)):
            liste.append((f"gemini-{ad}", y, "skill"))
            bilinen.add(y)
    for e in ek_klasorler or []:
        if isinstance(e, dict) and isinstance(e.get("yol"), str) and e["yol"] not in bilinen:
            liste.append((str(e.get("ad") or "ek"), e["yol"], e.get("tur") if e.get("tur") in ("skill", "liste") else "skill"))
            bilinen.add(e["yol"])
    try:
        adlar = sorted(e.name for e in os.scandir(ev.yol) if e.name.startswith(".") and e.is_dir(follow_symlinks=False))
    except OSError:
        adlar = []
    for ad in adlar:
        y = f"~/{ad}/skills"
        if ad in KESIF_YOKSAY or y in bilinen:
            continue
        if os.path.isdir(ev.ac(y)):
            liste.append((f"kesif-{ad}", y, "skill"))
            bilinen.add(y)
    return liste


def izinli_mi(yol, izinli):
    return any(altinda(yol, i) for i in izinli)


def tara(ev, ek_klasorler, izinli):
    """Canlı tarama: {'bolgeler': {anahtar: {yol, tur, var}}, 'girdiler': {yol: girdi}}. Hiçbir şeye yazmaz."""
    bolgeler, girdiler = {}, {}
    for anahtar, yol, tur in bolge_listesi(ev, ek_klasorler):
        ab = ev.ac(yol)
        var = os.path.isdir(ab)
        bolgeler[anahtar] = {"yol": yol, "tur": tur, "var": var}
        if not var:
            continue
        try:
            adlar = sorted(os.listdir(ab))
        except OSError:
            continue
        for ad in adlar:
            if GURULTU.search(ad):
                continue
            y = f"{yol}/{ad}"
            if izinli_mi(y, izinli):
                continue
            g = olc(ev, os.path.join(ab, ad), anahtar if tur == "liste" else "skill")
            g.update({"yol": y, "bolge": anahtar})
            girdiler[y] = g
    for bolge, yol, tur in DOSYALAR:
        ab = ev.ac("~/" + yol)
        if os.path.lexists(ab):
            y = "~/" + yol
            if izinli_mi(y, izinli):
                continue
            g = olc(ev, ab, bolge if tur == "talimat" else "kilit")
            g.update({"yol": y, "bolge": bolge})
            girdiler[y] = g
    return {"bolgeler": bolgeler, "girdiler": girdiler}


# ------------------------------------------------------------------ sahip ve durum
class Bilgi:
    """Sahip bulmak için kilit ve kart ipuçları. Kaynak metinleri yalnız sınanır; saklanmaz ve yazdırılmaz."""

    def __init__(self, ev, kart_yolu):
        self.kilit = {}
        self.kilit_okunamadi = False
        self.hf_skilleri = set()
        self.yazici_adlari = {}  # yazıcı anahtarı -> kilit kaynağı ya da manifest ile eşleşen adlar (kaynak metni tutulmaz)
        yol = ev.ac("~/.agents/.skill-lock.json")
        if os.path.lexists(yol):
            try:
                with open(yol, encoding="utf-8") as f:
                    veri = json.load(f)
                sk = veri.get("skills") if isinstance(veri, dict) else None
                if not isinstance(sk, dict):
                    raise ValueError
                kilit, eslesen = {}, {}
                for ad, v in sk.items():
                    if isinstance(v, dict):
                        kilit[ad] = (self._hf(v.get("source"), v.get("sourceType")))
                        for y in BILINEN_YAZICILAR:
                            if any(self._kaynak_eslesir(v.get("source"), k) for k in y.get("kaynak", [])):
                                eslesen.setdefault(y["ad"], set()).add(ad)
                self.kilit = kilit
                for k, adlar in eslesen.items():
                    self.yazici_adlari.setdefault(k, set()).update(adlar)
            except Exception:  # noqa: BLE001  sabit ifade: içerik/hata metni asla yansıtılmaz
                self.kilit_okunamadi = True
                self.kilit = {}
        for y in BILINEN_YAZICILAR:
            if y.get("manifest"):
                adlar = self._manifest_adlari(ev.ac(y["manifest"]))
                if adlar:
                    self.yazici_adlari.setdefault(y["ad"], set()).update(adlar)
        try:
            kart = json_oku(Path(kart_yolu), {}) if kart_yolu else {}
            sk = kart["programlar"]["hyperframes"]["skilleri"]
            self.hf_skilleri = {s for s in sk if isinstance(s, str)}
        except Exception:  # noqa: BLE001
            self.hf_skilleri = set()

    @staticmethod
    def _hf(source, tur):
        s = source if isinstance(source, str) else ""
        if "heygen-com/hyperframes" in s:
            return "hf"
        if tur == "local" and "hf-skills" in s.replace("\\", "/").split("/"):
            return "hf"
        return "diger"

    @staticmethod
    def _kaynak_eslesir(source, owner_ad):
        """source içinde owner/ad tam parça olarak geçiyor mu (owner/ad, URL, .git sonekli). Metin saklanmaz."""
        if not isinstance(source, str):
            return False
        return re.search(r"(?<![\w.-])" + re.escape(owner_ad.lower()) + r"(?![\w-])", source.lower()) is not None

    @staticmethod
    def _manifest_adlari(yol):
        """Manifestteki "skills" listesinden yalnız metin adlar; dosya yoksa, büyükse ya da bozuksa boş küme."""
        try:
            if not os.path.isfile(yol) or os.path.getsize(yol) > 1_000_000:
                return set()
            with open(yol, encoding="utf-8") as f:
                veri = json.load(f)
            sk = veri.get("skills") if isinstance(veri, dict) else None
            return {s for s in sk if isinstance(s, str)} if isinstance(sk, list) else set()
        except Exception:  # noqa: BLE001  sabit ifade
            return set()

    @staticmethod
    def aranan_ad(ad, tur, hedef):
        """Bağ ~/.agents/skills/<ad> hedefliyse hedefin adı, değilse girdinin adı."""
        if tur == "bag" and hedef:
            m = re.search(r"(?:^|/)\.agents/skills/([^/]+)$", hedef)
            if m:
                return m.group(1)
        return ad

    def _yazici_ad(self, ad):
        for y in BILINEN_YAZICILAR:
            if ad in y.get("adlar", []):
                return [y]
        for y in BILINEN_YAZICILAR:
            if ad in self.yazici_adlari.get(y["ad"], set()):
                return [y]
        return []

    def yazici(self, ad, tur, hedef, bolge):
        """Girdiyi yazdığı bilinen uygulamalar (BILINEN_YAZICILAR satırları; tablo sırasıyla). Eşleşme yoksa []."""
        if bolge in ("komutlar", "ajanlar", "talimat"):
            return []
        if bolge == "kilit":
            bulunan = {y["ad"] for n in self.kilit for y in self._yazici_ad(n)}
            return [y for y in BILINEN_YAZICILAR if y["ad"] in bulunan]
        return self._yazici_ad(self.aranan_ad(ad, tur, hedef)) or self._yazici_ad(ad)

    def sahip(self, ad, tur, hedef, bolge, yol, izinli_sahipleri):
        if yol in izinli_sahipleri:
            return izinli_sahipleri[yol]
        if yol in TOHUM_KALACAK:
            return TOHUM_KALACAK[yol][0]
        if ad in KULLANICI_ADLARI:
            return "kullanıcı"
        if tur == "bag" and hedef and hedef.startswith("~/.openmontage/"):
            return "openmontage"
        aranan = self.aranan_ad(ad, tur, hedef)
        if bolge in ("komutlar", "ajanlar", "talimat"):
            return "kullanıcı"
        if bolge == "kilit":
            return "skills aracı"
        if aranan in self.kilit:
            return "hyperframes" if self.kilit[aranan] == "hf" else ("hyperframes" if aranan.startswith("hyperframes") else "skills aracı")
        if aranan.startswith("hyperframes") or aranan in self.hf_skilleri or ad in self.hf_skilleri:
            return "hyperframes"
        return "bilinmiyor"


def durum_ver(bolge, ad, yol):
    if bolge in ("komutlar", "ajanlar", "talimat") or bolge not in SABIT_SKILL_BOLGELERI:
        return "kalacak"   # keşfedilen, ~/.gemini/*/skills ve ek klasörler boşaltma adımlarının dışındadır
    if (ad.startswith(".") and bolge != "kilit") or yol in TOHUM_KALACAK:
        return "kalacak"
    return "boşaltılacak"


def girdi_yaz(g, sahip, durum):
    """Tabana yazılacak satır: kirik canlı bir özelliktir, yazılmaz."""
    s = {"yol": g["yol"], "bolge": g["bolge"], "tur": g["tur"]}
    for k in ("hedef", "dosya", "bayt", "mtime", "kesik"):
        if k in g:
            s[k] = g[k]
    s["sahip"] = sahip
    s["durum"] = durum
    return s


# ------------------------------------------------------------------ taban
def taban_oku(yol):
    """-> (taban, hata, gecersiz_satirlar). taban yoksa (None, None, []); okunamazsa (None, neden, [])."""
    yol = Path(yol)
    if not yol.exists():
        return None, None, []
    try:
        t = json.loads(yol.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None, "geçersiz JSON", []
    if not isinstance(t, dict) or t.get("surum") != 1:
        return None, "taban sürümü desteklenmiyor", []
    if not isinstance(t.get("girdiler"), list):
        return None, "girdiler listesi yok", []
    t.setdefault("izinli", [])
    t.setdefault("ek_klasorler", [])
    t.setdefault("klasorler", {})
    t.setdefault("gecmis", [])
    kotu, iyi = [], []
    for g in t["girdiler"]:
        if not isinstance(g, dict) or not isinstance(g.get("yol"), str):
            continue
        if g.get("sahip") not in SAHIPLER:
            kotu.append(f"{g['yol']} (sahip geçersiz)")
        elif g.get("durum") not in DURUMLAR:
            kotu.append(f"{g['yol']} (durum geçersiz)")
        iyi.append(g)
    t["girdiler"] = iyi
    return t, None, kotu


def izinli_liste(taban):
    d = {i["yol"]: i["sahip"] for i in IZINLI_VARSAYILAN}
    if taban:
        for i in taban.get("izinli", []):
            if isinstance(i, dict) and isinstance(i.get("yol"), str):
                d[i["yol"]] = i.get("sahip") if i.get("sahip") in SAHIPLER else "uygulama"
    return d


def klasorler_yaz(tarama):
    return {k: {"yol": b["yol"], "var": b["var"]} for k, b in sorted(tarama["bolgeler"].items())}


def taban_kur(ev, tarama, bilgi, eski, tarih, kalacaklar):
    """Yeni taban sözlüğü + mesajlar. eski None ise ilk taban; değilse yenileme."""
    izinli_d = izinli_liste(eski)
    mesaj = []
    girdiler = []
    eski_g = {g["yol"]: g for g in (eski or {}).get("girdiler", [])}
    for yol, g in sorted(tarama["girdiler"].items()):
        ad = yol.rsplit("/", 1)[-1]
        if yol in eski_g:
            sahip, durum = eski_g[yol].get("sahip"), eski_g[yol].get("durum")
            if sahip not in SAHIPLER:
                sahip = bilgi.sahip(ad, g["tur"], g.get("hedef"), g["bolge"], yol, izinli_d)
            if durum not in DURUMLAR:
                durum = durum_ver(g["bolge"], ad, yol)
        else:
            sahip = TOHUM_KALACAK[yol][0] if yol in TOHUM_KALACAK else bilgi.sahip(ad, g["tur"], g.get("hedef"), g["bolge"], yol, izinli_d)
            durum = durum_ver(g["bolge"], ad, yol) if eski is None else "kalacak"
            if eski is not None:
                mesaj.append(f"kabul edildi: {yol}")
        girdiler.append(girdi_yaz(g, sahip, durum))
    if eski is not None:
        for yol, g in sorted(eski_g.items()):
            if yol not in tarama["girdiler"] and g.get("durum") == "kalacak" and not izinli_mi(yol, izinli_d):
                mesaj.append(f"düşürüldü (kalacak idi): {yol}")
    by = {g["yol"]: g for g in girdiler}
    for k in kalacaklar:
        if k not in by:
            return None, [f"Tabanda yok: {k}"]
        if by[k]["durum"] != "kalacak":
            by[k]["durum"] = "kalacak"
            mesaj.append(f"kalacak yapıldı: {k}")
    if eski is None:
        for k, b in sorted(tarama["bolgeler"].items()):
            if k.startswith(BULUNAN_ONEK) and b["var"]:
                mesaj.append(f"{b['yol']} hangi araca ait? Genel boşaltma kapsamında mı?")
    gecmis = list((eski or {}).get("gecmis", []))
    gecmis.append({"tarih": tarih, "islem": "ilk-taban" if eski is None else "yenile", "girdi": len(girdiler)})
    neden_eski = {i["yol"]: i for i in (eski or {}).get("izinli", []) if isinstance(i, dict) and "yol" in i}
    izinli_out = []
    for y, sh in izinli_d.items():
        if "neden" in neden_eski.get(y, {}):
            izinli_out.append(neden_eski[y])
        else:
            izinli_out.append({"yol": y, "sahip": sh, "neden": next((i["neden"] for i in IZINLI_VARSAYILAN if i["yol"] == y), "elle eklendi")})
    taban = {
        "surum": 1, "yazildi": tarih,
        "izinli": izinli_out,
        "ek_klasorler": list((eski or {}).get("ek_klasorler", [])),
        "klasorler": klasorler_yaz(tarama),
        "girdiler": girdiler,
        "gecmis": gecmis[-20:],
    }
    return taban, mesaj


# ------------------------------------------------------------------ ortam kontrolü (yalnız var/yok)
def ortam_dosyasi(ev, goreli):
    """-> 'var' | 'dosya yok' | 'okunamadı' | 'geçersiz değer' | 'satır yok'. Hiçbir satırı tutmaz ya da yansıtmaz."""
    yol = os.path.join(ev.yol, goreli)
    try:
        if goreli.endswith(".json"):
            if os.path.getsize(yol) > 2_000_000:
                return "okunamadı"
            with open(yol, encoding="utf-8") as f:
                veri = json.load(f)
            env = veri.get("env") if isinstance(veri, dict) else None
            if not isinstance(env, dict) or ANAHTAR not in env:
                return "satır yok"
            return "var" if str(env[ANAHTAR]) == "1" else "geçersiz değer"
        toplam, satir_n, sonuc = 0, 0, "satır yok"
        with open(yol, encoding="utf-8", errors="replace") as f:
            while True:
                s = f.readline(8192)
                if not s:
                    break
                toplam += len(s)
                if s.endswith("\n"):
                    satir_n += 1
                if toplam > 1_000_000 or satir_n > 20000:
                    break
                m = ANAHTAR_RE.match(s.rstrip("\r\n"))
                s = None  # noqa: F841  satır hemen atılır
                if m:
                    return "var" if m.group("v") == "1" else "geçersiz değer"
        return sonuc
    except FileNotFoundError:
        return "dosya yok"
    except Exception:  # noqa: BLE001  sabit ifade; hata metni ve yol yansıtılmaz
        return "okunamadı"


def ortam_kontrol(ev):
    eksik, var = [], 0
    for g in ORTAM_DOSYALARI:
        d = ortam_dosyasi(ev, g)
        if d == "var":
            var += 1
        else:
            eksik.append(f"~/{g} ({d})")
    satir = f"{ANAHTAR} satırı: {len(ORTAM_DOSYALARI)} dosyanın {EK[var]} var."
    if eksik:
        satir += " EKSİK: " + ", ".join(eksik)
        if any(e.startswith(("~/.zshenv ", "~/.zshrc ")) and e.endswith("(satır yok)") for e in eksik):
            satir += KABUK_IPUCU
    return var == len(ORTAM_DOSYALARI), satir, eksik


# ------------------------------------------------------------------ karşılaştırma
def fark(b, e):
    if b.get("tur") != e["tur"]:
        return f"tür: {b.get('tur')} -> {e['tur']}"
    if e["tur"] == "bag":
        return f"hedef: {b.get('hedef')} -> {e['hedef']}" if b.get("hedef") != e["hedef"] else None
    if e["tur"] == "klasor":
        if b.get("dosya") != e["dosya"]:
            return f"dosya sayısı: {b.get('dosya')} -> {e['dosya']}"
        if b.get("bayt") != e["bayt"]:
            return f"boyut: {b.get('bayt')} -> {e['bayt']}"
        return None
    if "bayt" in b or "bayt" in e:
        if b.get("bayt") != e.get("bayt"):
            return f"boyut: {b.get('bayt')} -> {e.get('bayt')}"
        if b.get("mtime") != e.get("mtime"):
            return "tarih değişti"
    return None


def karsilastir(ev, tarama, taban, hata, kotu, ortam):
    """-> dict(durum, satirlar [(siddet, metin)], karar, sayac)."""
    satirlar, karar, yazicilar = [], [], []

    def ekle(sd, m):
        satirlar.append((SIDDET[sd], m))

    if not ev_var(ev):
        ekle("sorun", f"Ev klasörü yok ya da klasör değil: {ev.yol}")
    if hata:
        ekle("sorun", f"TABAN OKUNAMADI: {hata}")
    elif taban is None:
        ekle("dikkat", "TABAN YOK: notlar/genel-klasor-tabani.json yazılmamış. İlk taban için: "
                       "python3 araclar/genel-bekci.py --taban-yaz  (kuru çalışma); onaydan sonra --evet ekle.")
        karar.append("İlk taban yazılsın mı? (--taban-yaz --evet; kullanıcı onayı gerekir, önce kuru çalışma gösterilir)")
        for k, b in sorted(tarama["bolgeler"].items()):
            if k.startswith(BULUNAN_ONEK) and b["var"]:
                karar.append(f"{b['yol']} hangi araca ait? Genel boşaltma kapsamında mı?")
    sayac = {"duruyor": 0, "bosaltilan": 0, "kirik_bosaltilacak": 0}
    if taban is not None:
        for k in kotu:
            ekle("sorun", f"TABAN SORUNU: {k}")
        base = {g["yol"]: g for g in taban["girdiler"]}
        klas = taban.get("klasorler", {})
        izinli = list(izinli_liste(taban))
        yeni_klasor = set()
        for k, b in sorted(tarama["bolgeler"].items()):
            tb = klas.get(k)
            if b["var"] and (not isinstance(tb, dict) or not tb.get("var")):
                n = sum(1 for g in tarama["girdiler"].values() if g["bolge"] == k)
                ekle("sorun" if n else "dikkat", f"YENİ KLASÖR {b['yol']} ({n} girdi)")
                karar.append(KARAR_KLASOR.format(y=b["yol"]))
                yeni_klasor.add(k)
        for k, tb in sorted(klas.items()):
            if isinstance(tb, dict) and tb.get("var") and not tarama["bolgeler"].get(k, {}).get("var"):
                ekle("bilgi", f"KLASÖR YOK {tb.get('yol')}")
        for yol, e in sorted(tarama["girdiler"].items()):
            if izinli_mi(yol, izinli) or e["bolge"] in yeni_klasor:
                continue
            b = base.get(yol)
            if b is None:
                sahip = e.get("_sahip", "bilinmiyor")
                sd = "dikkat" if e["bolge"] in ("komutlar", "ajanlar", "talimat") else "sorun"
                ekle(sd, f"YENİ      {yol} ({'klasör' if e['tur'] == 'klasor' else 'bağ' if e['tur'] == 'bag' else 'dosya'}, sahip: {sahip})")
                yz = e.get("_yazici") or []
                if yz:
                    yazicilar.append((yol, yz))
                karar.append(KARAR_YENI.format(y=yol, s=sahip + yazici_eki(yz)))
                if e.get("kirik"):
                    ekle("dikkat", f"KIRIK BAĞ {yol} -> {e.get('hedef')}")
                continue
            f = fark(b, e)
            if f:
                ekle("dikkat", f"DEĞİŞTİ   {yol} ({f})")
            if e.get("kirik"):
                if b.get("durum") == "boşaltılacak":
                    sayac["kirik_bosaltilacak"] += 1
                else:
                    ekle("dikkat", f"KIRIK BAĞ {yol} -> {e.get('hedef')}")
            if b.get("durum") == "boşaltılacak":
                sayac["duruyor"] += 1
        for yol, b in sorted(base.items()):
            if yol in tarama["girdiler"] or izinli_mi(yol, izinli):
                continue
            if b.get("durum") == "kalacak":
                ekle("dikkat", f"KAYIP     {yol} (kalacak girdi yok)")
            else:
                sayac["bosaltilan"] += 1
        if sayac["duruyor"]:
            ekle("bilgi", f"boşaltılacak girdi duruyor: {sayac['duruyor']} (bekleniyor, taban: {taban.get('yazildi')})")
        if sayac["bosaltilan"]:
            ekle("bilgi", f"boşaltılan: {sayac['bosaltilan']}")
        if sayac["kirik_bosaltilacak"]:
            ekle("bilgi", f"kırık bağ (boşaltılacak): {sayac['kirik_bosaltilacak']}")
    tamam, satir, eksik = ortam
    ekle("bilgi" if tamam else "sorun", satir)
    if not tamam:
        karar.append(f"{ANAHTAR} satırı {', '.join(e.split(' (')[0] for e in eksik)} içine eklensin mi? "
                     "(ayar dosyası: onay gerekir; ajan kendi eklemez)")
    en = max([s for s, _ in satirlar] or [0])
    durum = {2: "sorun", 1: "dikkat", 0: "temiz"}[en]
    return {"durum": durum, "satirlar": satirlar, "karar": list(dict.fromkeys(karar)), "sayac": sayac, "yazicilar": yazicilar}


def yazici_eki(yazicilar):
    """Karar metnine kısa ek: '; yazan: ...; durdurmak: ...' (eşleşme yoksa boş). Birden çok yazıcıda (yalnız kilit dosyası)
    satır aylık özetin 300 karakter sınırını aşmasın diye durdurma yolları --ayrinti satırlarına bırakılır."""
    if not yazicilar:
        return ""
    if len(yazicilar) == 1:
        return f"; yazan: {yazicilar[0]['yazan']}; durdurmak: {yazicilar[0]['durdur']}"
    return "; yazan: " + " ya da ".join(y["yazan"] for y in yazicilar) + "; durdurmak: --ayrinti satırlarında"


def ev_var(ev):
    return os.path.isdir(ev.yol)


def sahipleri_doldur(tarama, bilgi, izinli_d):
    for yol, g in tarama["girdiler"].items():
        ad = yol.rsplit("/", 1)[-1]
        g["_sahip"] = bilgi.sahip(ad, g["tur"], g.get("hedef"), g["bolge"], yol, izinli_d)
        g["_yazici"] = bilgi.yazici(ad, g["tur"], g.get("hedef"), g["bolge"])


def calistir(ev, taban_yolu, kart):
    """Tarama + karşılaştırma. -> (sonuc, tarama, taban, bilgi)."""
    taban, hata, kotu = taban_oku(taban_yolu)
    izinli_d = izinli_liste(taban)
    tarama = tara(ev, (taban or {}).get("ek_klasorler", []), list(izinli_d))
    bilgi = Bilgi(ev, kart)
    sahipleri_doldur(tarama, bilgi, izinli_d)
    sonuc = karsilastir(ev, tarama, taban, hata, kotu, ortam_kontrol(ev))
    return sonuc, tarama, taban, bilgi


# ------------------------------------------------------------------ çıktı
def sayim_satirlari(tarama):
    sat = []
    for k, b in sorted(tarama["bolgeler"].items()):
        n = sum(1 for g in tarama["girdiler"].values() if g["bolge"] == k)
        sat.append(f"  {b['yol']}: {n} girdi" if b["var"] else f"  {b['yol']}: klasör yok")
    return sat


def rapor_metni(sonuc, tarama, taban, ayrinti, tarih=None):
    sorun = sum(1 for s, _ in sonuc["satirlar"] if s == 2)
    dikkat = sum(1 for s, _ in sonuc["satirlar"] if s == 1)
    out = [f"Genel klasör bekçisi: {BUYUK[sonuc['durum']]} (sorun: {sorun}, dikkat: {dikkat})"]
    for s, m in sorted(sonuc["satirlar"], key=lambda x: -x[0]):
        out.append(m)
    if ayrinti:
        out.append("Bölgeler:")
        out += sayim_satirlari(tarama)
        if taban:
            for g in taban["girdiler"]:
                if g.get("durum") == "boşaltılacak" and g["yol"] in tarama["girdiler"]:
                    out.append(f"  boşaltılacak: {g['yol']} ({g.get('tur')}, sahip: {g.get('sahip')})")
        for yol, yz in sonuc.get("yazicilar", []):
            for y in yz:
                out.append(f"  yazan: {yol}: {y['yazan']} ({y['kimlik']}); durdurmak: {y['durdur']}; kanıt: {y['kanit']}")
    if sonuc["karar"]:
        out.append("Karar bekleyen:")
        out += [f"  - {k}" for k in sonuc["karar"]]
    return out


def ozet_json(sonuc):
    sat = [m for s, m in sorted(sonuc["satirlar"], key=lambda x: -x[0])]
    if len(sat) > 12:
        sat = sat[:11] + [f"... ve {len(sat) - 11} satır daha"]
    return {"arac": "genel-bekci", "durum": sonuc["durum"], "satirlar": sat, "karar_bekleyen": sonuc["karar"][:10]}


def yazma_izinli(hedef, ev, bolge_yollari):
    """Yazma koruması: hedef izlenen bir klasörün ya da ev altındaki araç klasörlerinin içinde olamaz."""
    h = os.path.realpath(str(hedef))
    yasak = [os.path.realpath(os.path.join(ev.yol, d)) for d in (".claude", ".agents", ".codex", ".gemini", ".cursor", ".copilot")]
    yasak += [os.path.realpath(ev.ac(y)) for y in bolge_yollari]
    return not any(altinda(h, y) for y in yasak)


def tarihsiz(m):
    return re.sub(r"\d{4}-\d{2}-\d{2}", "", m, count=1)


# ------------------------------------------------------------------ plan
def adim_kumesi(adim, taban, canli):
    sec = []
    for g in taban["girdiler"]:
        if g.get("durum") != "boşaltılacak" or g["yol"] not in canli:
            continue
        b, t, s = g.get("bolge"), canli[g["yol"]]["tur"], g.get("sahip")
        if (adim == "3" and b == "codex") or (adim == "4" and b == "claude" and t == "bag") \
                or (adim == "5a" and b == "claude" and t != "bag" and s == "hyperframes") \
                or (adim == "5b" and b == "claude" and t != "bag" and s != "hyperframes") \
                or (adim == "6" and b in ("agents", "kilit")):
            sec.append(g["yol"])
    return sorted(sec)


def q(s):
    return shlex.quote(str(s))


def plan_uret(adim, ev, taban, tarama, sonuc, tarih):
    """-> (satirlar, durdur_listesi). Hiçbir şeyi çalıştırmaz."""
    ust = ["# zsh/bash uyumlu; glob yok", "# Bu araç yalnız okur ve yazdırır; hiçbir komutu kendisi çalıştırmaz."]
    if adim in ("1", "2"):
        return ust + [f"Bu adım elle: rehber/12 bölüm {adim}"], []
    if taban is None:
        return ust, ["DURDUR: taban yok ya da okunamadı (notlar/genel-klasor-tabani.json yazılmadan plan üretilmez)"]
    canli = tarama["girdiler"]
    if adim == "7":
        return ust + plan7(tarih), []
    dur = []
    if sonuc["durum"] == "sorun":
        dur.append("DURDUR: rapor 'sorun' veriyor (önce python3 araclar/genel-bekci.py çalıştırıp YENİ girdileri ve eksik anahtarı sınıflandır)")
    for onceki in ADIM_SIRASI[:ADIM_SIRASI.index(adim)]:
        k = adim_kumesi(onceki, taban, canli)
        if k:
            dur.append(f"DURDUR: ÖNCEKİ ADIM BİTMEMİŞ: adım {onceki} ({len(k)} girdi)")
    kume = adim_kumesi(adim, taban, canli)
    kset = set(kume)
    for yol, e in sorted(canli.items()):
        if e["tur"] != "bag" or yol in kset:
            continue
        h = e.get("hedef", "")
        if any(altinda(h, k) for k in kset):
            dur.append(f"DURDUR: BAĞIMLI: {yol} -> {h} bu adımla kırılır")
    if dur:
        return ust, dur
    yedek = f"genel-klasorler-{tarih}"
    ad_ = {"3": "~/.codex/skills bağlarını kaldır", "4": "~/.claude/skills bağlarını kaldır",
           "5a": "~/.claude/skills içindeki HyperFrames kopyalarını yedeğe taşı",
           "5b": "~/.claude/skills içindeki diğer gerçek klasörleri yedeğe taşı",
           "6": "~/.agents/skills klasörlerini ve skill kilit dosyasını yedeğe taşı"}[adim]
    s = ust + [f"# ADIM {adim} - {ad_} ({len(kume)} girdi). ONAY GEREKİR: bu listeyi kullanıcıya göster, \"evet\" gelmeden çalıştırma."]
    if not kume:
        return s + ["# Bu adımda yapılacak girdi yok."], []
    s.append('cd "$HOME/Documents/SkillKutuphanesi" || exit 1  # araç komutları kütüphane klasöründen çalışır')
    bolge_ad = {"codex": "codex", "claude": "claude", "agents": "agents"}
    ana = {"3": "~/.codex/skills", "4": "~/.claude/skills", "5a": "~/.claude/skills", "5b": "~/.claude/skills", "6": "~/.agents/skills"}[adim]
    if adim in ("5a", "5b", "6"):
        s.append(f'[ "$(stat -f %d {q(ev.ac(ana))})" = "$(stat -f %d "$HOME/Documents/Claude")" ] || '
                 "{ echo 'FARKLI DİSK: mv kopyalar, durdur'; exit 1; }")
    s.append(f'YEDEK="$HOME/Documents/Claude/yedek/{yedek}"; mkdir -p "$YEDEK"')
    baglar = [y for y in kume if canli[y]["tur"] == "bag"]
    digerler = [y for y in kume if canli[y]["tur"] != "bag"]
    s.append("# 1) yedek")
    bolge_son = {}
    for y in baglar:
        bolge_son.setdefault(canli[y]["bolge"], []).append(y)
    for b, liste in sorted(bolge_son.items()):
        tsv = f'"$YEDEK/bag-listesi-{b}.tsv"'
        for i, y in enumerate(liste):
            a = ev.ac(y)
            s.append(f"printf '%s\\t%s\\n' {q(a)} \"$(readlink {q(a)})\" {'>' if i == 0 else '>>'} {tsv}")
    s.append(f'ls -la {q(ev.ac(ana))} > "$YEDEK/ls-{adim}-oncesi.txt"')
    gerial = []
    s.append("# 2) uygula")
    for b in sorted(bolge_son):
        for y in bolge_son[b]:
            s.append(f"rm -- {q(ev.ac(y))}")
    ara = sorted({canli[y]["bolge"] for y in digerler if canli[y]["bolge"] != "kilit"})
    for b in ara:
        s.append(f'mkdir -p "$YEDEK/{bolge_ad.get(b, b)}-skills"')
    if any(canli[y]["bolge"] == "kilit" for y in digerler):
        s.append('mkdir -p "$YEDEK/agents-kilit"')
        s.append(f'cp -p {q(ev.ac("~/.agents/.skill-lock.json"))} "$YEDEK/agents-kilit/skill-lock.json.kopya"')
    for y in digerler:
        g = canli[y]
        a = ev.ac(y)
        ad = y.rsplit("/", 1)[-1]
        if g["bolge"] == "kilit":
            hedef_klasor, geri = '"$YEDEK/agents-kilit/"', '"$YEDEK/agents-kilit/"' + q(ad)
        else:
            hedef_klasor = f'"$YEDEK/{bolge_ad.get(g["bolge"], g["bolge"])}-skills/"'
            geri = hedef_klasor + q(ad)
        s.append(f'if [ -e {geri} ] || [ -L {geri} ]; then '
                 f"echo {q('YEDEKTE AYNI AD VAR, durdur: ' + ad)}; exit 1; fi")
        s.append(f"mv -- {q(a)} {hedef_klasor}")
        gerial.append(f"if [ -e {q(a)} ] || [ -L {q(a)} ]; then echo {q('ÇAKIŞMA: ' + a)}; else mv -- {geri} {q(a)}; fi")
    s.append("# 3) kontrol")
    s.append('python3 araclar/genel-bekci.py --yedek-dogrula "$YEDEK" ; python3 araclar/genel-bekci.py')
    s.append("# 4) geri alma (bu adımı geri al)")
    for b in sorted(bolge_son):
        s.append('while IFS=$\'\\t\' read -r p t; do if [ -e "$p" ] || [ -L "$p" ]; then echo "ÇAKIŞMA: $p"; else ln -s -- "$t" "$p"; fi; done '
                 f'< "$YEDEK/bag-listesi-{b}.tsv"')
    s += gerial
    return s, []


def plan7(tarih):
    return [
        "# ADIM 7 - Kapanış. ONAY GEREKİR: yenileme ve kayıt adımları ayrı ayrı onay ister.",
        "python3 araclar/genel-bekci.py --ayrinti   # temiz olmalı; ~/.gemini, ~/.cursor, ~/.copilot skills klasörleri boş ya da yok",
        "python3 araclar/genel-bekci.py --taban-yaz --yenile --evet   # ONAY GEREKİR (kabul edildi listesi gösterilir; kalacak yapılacaklar için --kalacak YOL)",
        "python3 araclar/genel-bekci.py   # yenilemeden sonra TEMİZ olmalı",
        "# Yedek kaydı (yedekler.json satırı, onayla):",
        f"#   yol: ~/Documents/Claude/yedek/genel-klasorler-{tarih}/   tür: genel-klasor   tarih: {tarih}",
        "#   neden: Genel skill klasörleri boşaltıldı (rehber/12). İçerik: bağ listeleri (tsv), taşınan skill klasörleri, skill kilit dosyası, giriş dosyaları kopyaları.",
        "#   silme_tetigi: 30 gün geçince VE kullanıcı \"sil\" deyince (kendi kendine silinmez)   gizli_icerir: hayır",
        "# Hatırlatma önerisi (zamanlanmış görev; onay gerekir; boşaltmanın son günü kurulur):",
        "#   başlık: Genel skill klasörü yedeğini silme zamanı (30 gün sonra, tek seferlik)",
        f"#   metin: ~/Documents/Claude/yedek/genel-klasorler-{tarih}/ 30 gündür duruyor. Önce python3 araclar/genel-bekci.py çalıştır: temiz ise kullanıcıya sor: "
        "\"Yedeği silelim mi?\" Kullanıcı açıkça evet demeden hiçbir şeyi silme. Ayrıca ayar-2026-11-11 yedeğinde düz metin anahtar satırı olabilir; onu da hatırlat (içeriği yazdırma).",
        "# Açık oturumlar eski skill listesini tutar: Claude ve Codex oturumlarını yeniden başlat.",
    ]


# ------------------------------------------------------------------ yedek doğrulama
def yedek_dogrula(ev, taban, tarama, klasor):
    k = Path(klasor)
    if not k.is_dir():
        return ["YEDEKTE YOK: yedek klasörü yok"], 0, 1
    tsv = {}
    for p in sorted(k.glob("bag-listesi-*.tsv")):
        try:
            for satir in p.read_text(encoding="utf-8").splitlines():
                if "\t" in satir:
                    yol, hedef = satir.split("\t", 1)
                    if not os.path.isabs(hedef):
                        hedef = os.path.normpath(os.path.join(os.path.dirname(yol), hedef))
                    tsv[ev.kisalt(yol)] = ev.kisalt(hedef)
        except OSError:
            continue
    tamam, sorunlar = 0, []
    for g in taban["girdiler"]:
        yol = g["yol"]
        if g.get("durum") != "boşaltılacak" or yol in tarama["girdiler"]:
            continue
        ad = yol.rsplit("/", 1)[-1]
        if g["tur"] == "bag":
            if yol not in tsv:
                sorunlar.append(f"YEDEKTE YOK: {yol}")
            elif tsv[yol] != g.get("hedef"):
                sorunlar.append(f"FARKLI: {yol} (hedef: {g.get('hedef')} -> {tsv[yol]})")
            else:
                tamam += 1
        elif g["bolge"] == "kilit":
            if (k / "agents-kilit" / ad).exists():
                tamam += 1
            else:
                sorunlar.append(f"YEDEKTE YOK: {yol}")
        else:
            p = k / f"{g['bolge']}-skills" / ad
            if not os.path.lexists(p):
                sorunlar.append(f"YEDEKTE YOK: {yol}")
            elif g["tur"] == "klasor":
                o = olc(ev, str(p), g["bolge"])
                if o.get("dosya") != g.get("dosya") or o.get("bayt") != g.get("bayt"):
                    sorunlar.append(f"FARKLI: {yol} (dosya/bayt: {g.get('dosya')}/{g.get('bayt')} -> {o.get('dosya')}/{o.get('bayt')})")
                else:
                    tamam += 1
            else:
                tamam += 1
    return sorunlar, tamam, 1 if sorunlar else 0


# ------------------------------------------------------------------ ana akış
def main(argv=None):
    ap = argparse.ArgumentParser(description="Genel klasör bekçisi (salt okuma; kütüphane dışına yazmaz)")
    ap.add_argument("--ev", help="ev klasörü (testler için; varsayılan: SKILL_BEKCI_EV ya da gerçek ev)")
    ap.add_argument("--taban", help="taban dosyası (varsayılan: notlar/genel-klasor-tabani.json)")
    ap.add_argument("--kart", help="programlar.json yolu (HyperFrames sahip ipucu)")
    ap.add_argument("--rapor", help="rapor dosyası (varsayılan: notlar/genel-bekci.md)")
    ap.add_argument("--rapor-yok", action="store_true", help="rapor dosyası yazma")
    ap.add_argument("--siki", action="store_true", help="durum 'sorun' ise çıkış kodu 1")
    ap.add_argument("--ozet-json", action="store_true", help="tek satır JSON özeti (aylık zincir için)")
    ap.add_argument("--ayrinti", action="store_true", help="bölge sayıları ve duran boşaltılacak girdiler")
    ap.add_argument("--taban-yaz", action="store_true", help="tabanı yaz (--evet yoksa kuru çalışma)")
    ap.add_argument("--yenile", action="store_true", help="--taban-yaz ile: var olan tabanı canlı durumla yenile")
    ap.add_argument("--kalacak", action="append", default=[], metavar="YOL", help="--taban-yaz --yenile ile: girdiyi kalacak yap (~/... biçimi)")
    ap.add_argument("--evet", action="store_true", help="kullanıcı onayı verildi: gerçekten yaz")
    ap.add_argument("--tarih", help="YYYY-AA-GG (varsayılan bugün)")
    ap.add_argument("--plan", choices=["1", "2", "3", "4", "5a", "5b", "6", "7"], help="boşaltma adımının komutlarını YAZDIR (çalıştırmaz)")
    ap.add_argument("--yedek-dogrula", metavar="YEDEK_KLASORU", help="yedeği tabandaki sayılarla karşılaştır")
    a = ap.parse_args(argv)
    if a.ozet_json and (a.taban_yaz or a.plan or a.yedek_dogrula):
        ap.error("--ozet-json; --taban-yaz, --plan ve --yedek-dogrula ile birlikte kullanılamaz")
    if (a.yenile or a.evet or a.kalacak) and not a.taban_yaz:
        ap.error("--yenile, --evet ve --kalacak yalnız --taban-yaz ile kullanılır")
    if a.kalacak and not a.yenile:
        ap.error("--kalacak yalnız --taban-yaz --yenile ile kullanılır")
    ev = Ev(a.ev or os.environ.get("SKILL_BEKCI_EV") or str(Path.home()))
    taban_yolu = Path(a.taban) if a.taban else KOK / "notlar" / "genel-klasor-tabani.json"
    kart = a.kart or str(KOK / "programlar.json")
    tarih = a.tarih or date.today().isoformat()

    if a.ozet_json:
        try:
            sonuc, _, _, _ = calistir(ev, taban_yolu, kart)
            j = ozet_json(sonuc)
        except Exception:  # noqa: BLE001
            j = {"arac": "genel-bekci", "durum": "sorun", "satirlar": ["Bekçi çalışırken hata verdi (ayrıntı yazdırılmaz)"], "karar_bekleyen": []}
        print(json.dumps(j, ensure_ascii=False))
        return 1 if (a.siki and j["durum"] == "sorun") else 0

    sonuc, tarama, taban, bilgi = calistir(ev, taban_yolu, kart)
    bolge_yollari = [b["yol"] for b in tarama["bolgeler"].values()]

    if a.yedek_dogrula:
        if taban is None:
            print("DURDUR: taban yok ya da okunamadı")
            return 1
        sorunlar, tamam, kod = yedek_dogrula(ev, taban, tarama, a.yedek_dogrula)
        for m in sorunlar:
            print(m)
        print(f"yedekte tamam: {tamam}")
        return kod

    if a.plan:
        satirlar, dur = plan_uret(a.plan, ev, taban, tarama, sonuc, tarih)
        for m in satirlar + dur:
            print(m)
        return 1 if (dur and a.siki) else 0

    if a.taban_yaz:
        return taban_yaz_islem(a, ev, taban_yolu, tarama, taban, bilgi, tarih, bolge_yollari)

    for m in rapor_metni(sonuc, tarama, taban, a.ayrinti):
        print(m)
    if not a.rapor_yok:
        hedef = Path(a.rapor) if a.rapor else KOK / "notlar" / "genel-bekci.md"
        if yazma_izinli(hedef, ev, bolge_yollari):
            govde = "\n".join(["# Genel Klasör Bekçisi Raporu", "",
                               f"> `araclar/genel-bekci.py` üretir · {date.today().isoformat()} · salt okuma; kural: `rehber/12-genel-klasor-bosaltma.md`", "",
                               "```"] + rapor_metni(sonuc, tarama, taban, False) + ["```"]) + "\n"
            if not hedef.exists() or tarihsiz(hedef.read_text(encoding="utf-8")) != tarihsiz(govde):
                hedef.write_text(govde, encoding="utf-8")
        else:
            print("Yazma reddedildi: hedef izlenen bir klasörün içinde")
    return 1 if (a.siki and sonuc["durum"] == "sorun") else 0


def taban_yaz_islem(a, ev, taban_yolu, tarama, taban, bilgi, tarih, bolge_yollari):
    if not yazma_izinli(taban_yolu, ev, bolge_yollari):
        print("Yazma reddedildi: hedef izlenen bir klasörün içinde")
        return 1
    var_mi = Path(taban_yolu).exists()
    if var_mi and taban is None:
        print(f"Taban okunamadı ({taban_yolu}); elle düzeltmeden üzerine yazılmaz.")
        return 1
    if var_mi and not a.yenile:
        if a.evet:
            print(f"Taban zaten var ({taban_yolu}). Üzerine yazmak için --yenile kullan; önce raporu kullanıcıya göster.")
            return 1
    if a.kalacak and not var_mi:
        print("Tabanda yok: " + a.kalacak[0])
        return 1
    yeni, mesaj = taban_kur(ev, tarama, bilgi, taban if (var_mi and a.yenile) else None, tarih, a.kalacak)
    if yeni is None:
        print(mesaj[0])
        return 1
    n = len(yeni["girdiler"])
    sayi = lambda d: sum(1 for g in yeni["girdiler"] if g["durum"] == d)  # noqa: E731
    bilinmeyen = [g["yol"] for g in yeni["girdiler"] if g["sahip"] == "bilinmiyor"]
    if not a.evet:
        print(f"Kuru çalışma: {n} girdi yazılacak (boşaltılacak: {sayi('boşaltılacak')}, kalacak: {sayi('kalacak')}, "
              f"bilinmeyen sahip: {len(bilinmeyen)}). Hedef: {ev.kisalt(taban_yolu) if altinda(str(taban_yolu), ev.yol) else taban_yolu}. "
              "Yazmak için --evet ekle (kullanıcı onayı gerekir).")
        if var_mi and not a.yenile:
            print("Not: taban zaten var; var olanı yenilemek için --yenile gerekir.")
        for y in bilinmeyen:
            print(f"bilinmeyen sahip: {y}")
        for k, b in sorted(tarama["bolgeler"].items()):
            if k.startswith(BULUNAN_ONEK) and b["var"]:
                print(f"bulunan klasör: {b['yol']}")
        for m in mesaj:
            print(m)
        return 0
    Path(taban_yolu).parent.mkdir(parents=True, exist_ok=True)
    json_yaz(taban_yolu, yeni)
    for m in mesaj:
        print(m)
    sonuc = karsilastir(ev, tarama, yeni, None, [], ortam_kontrol(ev))
    print(f"Taban yazıldı: {n} girdi. Yeni rapor durumu: {BUYUK[sonuc['durum']]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
