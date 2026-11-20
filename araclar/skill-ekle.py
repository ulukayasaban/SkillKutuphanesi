#!/usr/bin/env python3
"""Projeye skill / rol / profil ekler. SADECE verilen proje klasörüne yazar; global klasörlere asla dokunmaz.

Projede oluşanlar:
  .agents/skills/<skill>/          Codex'in okuduğu kopya (varsa Codex'e özel sürüm)
  .claude/skills/<skill>           Claude Code: symlink -> ../../.agents/skills/<skill>
                                   (skill'in Claude'a özel sürümü varsa symlink yerine o sürümün kopyası)
                                   --arac yalniz-claude (eski ad: claude): proje sadece Claude kullanır; skill burada gerçek kopya olur,
                                   .agents/skills, .codex/agents ve AGENTS.md bloğu kurulmaz (kilit.json -> "araclar")
                                   --arac ortak (eski ad: ikisi): Claude + Codex + Antigravity + Cursor + VS Code Copilot (varsayılan)
  Programla gelen skiller    --program-skill: .claude/skills/<ad> (ortak düzende .agents/skills/<ad> de) programın kendi klasörüne SYMLINK; kilit: dis_skiller
                             --dondur: projenin kendi gerçek kopyası (kütüphane güncellemez); kilit: dis_skiller (tur: donmus)
  .claude/agents/<rol>.md          Claude alt-agent'ı (frontmatter 'skills:' = sadece o rolün skilleri)
  .codex/agents/<rol>.toml         Codex alt-agent'ı (rol dışı proje skilleri [[skills.config]] ile kapalı)
  AGENTS.md / CLAUDE.md            işaretli blok (sadece o blok yeniden yazılır)
  .skill-kutuphanesi/kilit.json    hangi skill, hangi commit, hangi rol, kurulu içerik parmak izi
  .skill-kutuphanesi/yedek/        her işlemden önce otomatik yedek (son 10; --yedekler, --geri-al [ad])
  .skill-kutuphanesi/son-rapor.md  son UYGULANAN kurulumun ön kontrol raporu (--kuru hiçbir dosya yazmaz)
  Sabit yollar               kurulan kopyada ~/.claude/skills/<ad>/…, ${CLAUDE_PLUGIN_ROOT}/…/skills/<ad>/… gibi bilgisayar geneli yollar
                             "dar çevir, geniş uyar" kuralıyla proje içi yola çevrilir (yollari_yerellestir); çevrilemeyenler ön kontrolde UYARI

Güvenlik kuralları:
  * Her işlemden önce ÖN KONTROL çalışır. HATA varsa işlem yapılmaz (--zorla ile yedek alınarak geçilebilir).
    UYARI varsa onay istenir; etkileşimsiz çalışmada (agent) --evet verilmedikçe işlem yapılmaz.
  * Kütüphanedeki TÜM skiller taranır; seçilmeyen ama ilgili adaylar raporda listelenir (hiçbiri görmezden gelinmez).
  * Projedeki, kütüphaneden gelmeyen aynı isimli skill'in üzerine asla yazılmaz.
  * Elle değiştirilmiş kurulu skill güncelleme/kaldırmada ezilmez (--zorla ile yedeklenip ezilir).
  * Hata olursa yapılan değişiklikler yedekten otomatik geri alınır. Elle geri alma: --geri-al

Örnekler:
  python3 araclar/skill-ekle.py ~/Projeler/site --profil landing-page --kuru     # önce sadece rapor
  python3 araclar/skill-ekle.py ~/Projeler/site --profil landing-page --evet     # uygula
  python3 araclar/skill-ekle.py ~/Projeler/site --rol motion-gelistirici --opsiyonel --evet
  python3 araclar/skill-ekle.py ~/Projeler/site --skill design-taste-frontend gsap-core --rol-adi ui-tasarimci --evet
  python3 araclar/skill-ekle.py ~/Projeler/site --oner "3d ürün tanıtım sitesi scroll animasyonlu"
  python3 araclar/skill-ekle.py ~/Projeler/site --durum | --dogrula | --guncelle | --yenile | --geri-al
  python3 araclar/skill-ekle.py ~/Projeler/site --kaldir gsap-core     (ya da --kaldir hepsi)
  python3 araclar/skill-ekle.py ~/Projeler/site --program-skill openmontage:ffmpeg hyperframes:hyperframes --kuru  # programla gelen skile BAĞ (kopya değil)
  python3 araclar/skill-ekle.py ~/Projeler/site --fihrist-skill github/awesome-copilot:agent-governance --kuru     # fihristten (ağsız ön rapor; --evet indirir, inceler, kurar)
  python3 araclar/skill-ekle.py ~/Projeler/site --kit sirioberati/YouTube-AI-Video-Editing-System --kuru           # kit kataloğundan (boş proje iskeleti; başlamış projede --kit-parca)
  python3 araclar/skill-ekle.py ~/Projeler/site --rapor --oner "video kurgu düzeni"                                # Plan Bölüm 10: 10 bölümlü tam proje raporu (ağsız)
  python3 araclar/skill-ekle.py ~/Projeler/site --dondur ~/.claude/skills/eski-skill --kuru              # genel klasördeki skili projenin kendi skili olarak dondur
  python3 araclar/skill-ekle.py ~/Projeler/site --arac yalniz-claude --kuru  # sadece Claude'a geç
  python3 araclar/skill-ekle.py ~/Projeler/site --arac ortak --kuru          # ortak düzene geç (Claude + Codex + ...)
  python3 araclar/skill-ekle.py --araclar [--ozet-json] [--siki]             # yapay zeka araçları belgesi/sürüm kontrolü (salt okunur)
  python3 araclar/skill-ekle.py --listele --kategori 03 --teknoloji react
"""
import argparse
import json
import os
import posixpath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import (GLOBAL_KLASORLER, HESAP_ONEK, KAYNAKLAR, KOK, REGISTRY, hesap_skilleri, frontmatter, frontmatter_onar,  # noqa: E402
                   frontmatter_teshis, git_blob_hash, global_durum, json_oku, json_yaz, klasor_hash, medya_mi, onemli_dosyalar,
                   onarim_izi, repo_guncel, symlink_taslaklari, taslak_baglantilarini_cevir, yamalari_uygula, skill_adlari,
                   skill_yol_taramasi, tum_skiller, yol_degerlendir, yol_izi, yol_dosya_sinifi_haritasi, yol_taramasi,
                   ev_ici_kendi_cevir, _var_bak, program_klasor_skill_adi, program_skill_ham_klasoru_mu, program_skill_klasoru,
                   yerel_agac, yerel_commit, _ATIF_PARCA, _eklenti_koku_yolu, _yol_kes)

ROLLER = KOK / "roller"
PROFILLER = KOK / "profiller"
KAYNAKLAR_DOSYA = KAYNAKLAR            # testler yeniden atar
FIHRIST_KLASOR = KOK / "fihrist"       # testler yeniden atar
KITLER_DOSYA = KOK / "kitler.json"     # testler yeniden atar
KAYNAK_URL_CEVIRICI = None             # testler yerel git deposuna yönlendirir: fn(repo) -> url|Path
FIHRIST_INCELEME_YAZ = True            # fihrist kurulumunda inceleme sonucunu fihrist dosyasına kaydet
FIHRIST_KLON_ZAMAN_ASIMI = 300         # fihrist yolu için git klon/checkout zaman aşımı (sn)
KIT_KLON_ZAMAN_ASIMI = 600             # kit için git klon zaman aşımı (sn)
BLOK_BAS, BLOK_SON = "<!-- skill-kutuphanesi:basla -->", "<!-- skill-kutuphanesi:bitir -->"
URETILDI = "skill-kutuphanesi tarafından üretildi"
META = ".skill-kutuphanesi"
KILIT_SURUM = 3
ARACLAR = {"ikisi": ["claude", "codex"], "claude": ["claude"],
           "ortak": ["claude", "codex"], "yalniz-claude": ["claude"]}
ARAC_TAKMA = {"ikisi": "ortak", "claude": "yalniz-claude"}  # eski ad -> ad
DUZEN_KLASORLERI = {"ortak": [".agents/skills", ".claude/skills"], "yalniz-claude": [".claude/skills"]}
DUZEN_TALIMAT = {"ortak": ["CLAUDE.md", "AGENTS.md"], "yalniz-claude": ["CLAUDE.md"]}
ARAC_JSON = KOK / "yapay-zeka-araclari.json"
ARAC_BELGE_GUN = 45  # araç belgesi bu kadar günden eskiyse --araclar "dikkat" der
ROL_ADI = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
YEDEK_SAYISI = 10
# --zorla ile bile GEÇİLEMEYEN hatalar (güvenlik / tutarlılık)
ZORLANAMAZ = {"gecersiz-rol-adi", "global-baglanti", "proje-disi-baglanti", "ayni-klasor", "bulunamadi",
              "isim-cakismasi", "onyukleme-siniri", "farkli-kaynak", "kendi-agent-dosyan",
              # programla gelen skiller (bağ) ve dondurma (K-28)
              "program-skill-bicim", "program-bilinmiyor", "program-skillsiz", "program-kurulu-degil", "program-skill-yok",
              "program-skill-ad", "dis-ad-cakismasi", "bag-farkli", "bag-degismis", "dondur-yol", "dondur-kaynak-yok",
              "dondur-program-skili", "dondur-kutuphane-adi", "dondur-gizli", "dondur-dis-baglanti", "dondur-kendisi",
              "dondur-ad", "dondur-cok-buyuk", "dondur-ozel-dosya", "bag-gercek-klasor", "program-skill-ham-klasor",
              # fihrist ve kit kurulumu (plan 4. adım)
              "fihrist-skill-bicim", "fihrist-yok", "fihrist-kaynak-kayip", "fihrist-skill-yok", "fihrist-skill-belirsiz",
              "fihrist-gizli", "fihrist-symlink", "kit-bulunamadi", "kit-kaynak-kayip", "kit-baslamis-proje",
              "kit-korunan-dosya", "kit-dosya-cakismasi", "kit-parca-gecersiz", "kit-gizli", "kit-symlink", "kaynak-erisim"}
GUVENLIK_ONAY_KODLARI = {"guvenlik-ag", "guvenlik-veri", "guvenlik-talimat", "genele-yazabilir"}
PROGRAMLAR = KOK / "programlar.json"   # testler yeniden atar
FIHRIST_ONERI_SINIRI = 3               # plan 5.5: bir ihtiyaç için fihristten en çok 3 aday
MEDYA_ISTISNA_BAYT = 200 * 1024        # plan ortak kural 1: ≤200 KB istisna
BAKIMSIZ_GUN = 365                     # plan 5.1 & 7: 12 aydır değişmeyen kaynak 'bakımsız'
KIT_KORUNAN_DOSYALAR = {"CLAUDE.md", "AGENTS.md", ".claude/settings.json", "package.json", "pyproject.toml", ".gitignore"}
KIT_KORUNAN_ONEKLER = (".env", ".git/")
KIT_BETIK_AD = re.compile(r"^(?:install|setup|bootstrap|init)(?:[-_.].*)?\.(?:sh|bash|zsh|py|js|mjs|ts|ps1|cmd|bat)$", re.I)
GUVENLIK_ENJEKSIYON = re.compile(
    r"\b(?:ignore\s+(?:all\s+)?previous\s+instructions|skip\s+(?:user\s+)?confirmation|do\s+not\s+ask(?:\s+the\s+user)?|"
    r"without\s+asking(?:\s+permission|\s+confirmation)?|bypass\s+approval|override\s+safety|onay\s+isteme|onay\s+almadan)\b", re.I)
GUVENLIK_AG_CALISTIR = re.compile(
    r"(?:\b(?:curl|wget)\b[^\n|]{1,220}\|\s*(?:sh|bash|zsh|python3?|node)\b|\beval\s+\"\$\(\s*(?:curl|wget)\b|\biwr\b[^\n|]{1,180}\|\s*iex\b)", re.I)
GUVENLIK_VERI_GONDER = re.compile(
    r"(?:\.env\b|id_rsa|id_ed25519|\.ssh/|credentials|api[_-]?key)[^\n]{0,160}\b(?:curl|wget|fetch\(|requests\.post|http\.request)\b|"
    r"\b(?:curl|wget|fetch\(|requests\.post)\b[^\n]{0,160}(?:\.env\b|id_rsa|id_ed25519|\.ssh/|credentials)", re.I)
GUVENLIK_GENEL_YAZ = re.compile(
    r"(?:\b(?:cp|mv|rsync|install)\s+\S|\bln\s+-\w*s|\bmkdir\s+-p\b|\bgit\s+clone\b|\b(?:write|save|copy|create)\b[^\n]{0,60}?\b(?:to|into)\s+)[^\n]{0,200}"
    r"(?:~|\$HOME|\$\{HOME\}|/Users/[\w.-]+|/home/[\w.-]+)/\.(?:claude|agents|codex)/(?:skills|agents)\b|"
    r"\bnpx\s+(?:-y\s+|--yes\s+)?skills(?:@[\w.-]+)?\s+(?:add|update)\b[^\n]{0,200}(?:\s-g\b|--global\b)", re.I)
UCRET_IPUCU = re.compile(r"\b(?:OPENAI_API_KEY|ANTHROPIC_API_KEY|ELEVENLABS_API_KEY|HEYGEN_API_KEY|STRIPE_SECRET_KEY|paid\s+plan|subscription\s+required|billing\s+account)\b", re.I)
CLAUDE_OZEL_IPUCU = re.compile(r"\b(?:AskUserQuestion|CLAUDE_PLUGIN_ROOT|\.claude-plugin|PreToolUse|PostToolUse)\b")
DIS_TURLER = ("program-bag", "donmus")
DIS_AD = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}")   # fullmatch ile kullanılır ($ satır sonunu kabul ederdi); video_toolkit gibi '_' içeren adlar
DONDUR_GIZLI_TAM = {".env", ".envrc", ".npmrc", ".netrc", ".pypirc", "auth.json", "token.json", "credentials.json", "credentials",
                    ".git-credentials", ".gitconfig", "apikey.txt", "api_key.txt", "api-key.txt", "apikey", "secret", "secrets"}
DONDUR_GIZLI_ONEK = (".env.", "id_rsa", "id_ed25519", "secrets.", "secret.", "service-account", "service_account", "client_secret", "authkey_")
DONDUR_GIZLI_SON = (".pem", ".key", ".p12", ".pfx", ".keystore", ".p8", ".jks", ".ppk", ".kdbx")
DONDUR_GIZLI_DIZIN = {".aws", ".ssh", ".gnupg", ".git", ".kube", ".docker", ".gcloud"}
DONDUR_TAVAN_KLASOR = 2000    # ZORLANAMAZ (dondur-cok-buyuk)
DONDUR_ATLANAN_DIZIN = {"node_modules", "__pycache__", ".venv"}
DONDUR_BUYUK_MB = 50          # UYARI
DONDUR_TAVAN_MB = 200         # ZORLANAMAZ
DONDUR_TAVAN_DOSYA = 5000     # ZORLANAMAZ
SINIR_ROL_SKILL = 12          # bir role önerilen en fazla skill
SINIR_ROL_KB = 150            # bir rolün önyüklenen SKILL.md toplamı (KB)
SINIR_CLAUDE_ONYUKLEME = 32   # Claude alt-agent 'skills:' sınırı
GENEL_KARDES = "genel:"       # kilit 'kardes' alanında: sabit (bilgisayar geneli / eklenti kökü) yolla anılan kardeşin anahtarı = "genel:<ad>"
# Sabit yol taraması (ortak.yol_degerlendir) satırlarının kodları: ön kontrol bunları rapora alır; tanınmayan kod UYARI sayılır (sessiz geçmez).
# yol-yerellestirme BİLGİ · genel-yol UYARI · eklenti-koku UYARI · skil-disi-yol UYARI · kardes-eksik UYARI · kardes-yol BİLGİ ·
# genele-yazabilir UYARI/BİLGİ · yol-istisna BİLGİ · istisna-eskidi UYARI · kardes-farkli-kaynak UYARI (aynı ad, farklı kimlik: yol çevrilmez)
YOL_KODLARI = ("yol-yerellestirme", "genel-yol", "eklenti-koku", "skil-disi-yol", "kardes-eksik", "kardes-yol", "genele-yazabilir",
               "yol-istisna", "istisna-eskidi", "kardes-farkli-kaynak")
# yollari_yeniden_adlandir'ın dokunduğu dosya uzantıları (tek sabit)
YENIDEN_ADLANDIRMA_UZANTI = (".md", ".sh", ".cmd", ".ps1", ".py", ".js", ".mjs", ".json", ".txt", "")
YEREL_UZANTI = (".md", ".mdx", ".txt", "")  # dar geçiş (.agents/skills/<kendi> -> .claude/skills/<kurulum adı>) yalnız bu metin dosyalarında

ES_ANLAM = {  # Türkçe sorgu -> İngilizce açıklamalarda aranacak kelimeler
    "animasyon": "animation animate motion", "hareket": "motion animation", "kaydırma": "scroll", "scroll": "scroll",
    "3d": "3d three webgl", "üç boyut": "3d three", "tasarım": "design ui ux", "arayüz": "ui interface frontend",
    "renk": "color palette", "yazı tipi": "font typography", "tipografi": "typography font", "marka": "brand",
    "logo": "logo brand", "test": "test testing", "hata": "debug bug error", "doküman": "document docs",
    "belge": "document", "rapor": "report document", "sunum": "presentation slides pptx", "tablo": "spreadsheet xlsx",
    "excel": "xlsx spreadsheet", "word": "docx", "pdf": "pdf", "oyun": "game", "video": "video",
    "ses": "audio voice speech", "seslendirme": "tts text-to-speech voice narration", "müzik": "music",
    "altyazı": "caption subtitle", "görsel": "image visual", "resim": "image", "erişilebilirlik": "accessibility a11y",
    "performans": "performance", "güvenlik": "security", "veritabanı": "database", "api": "api",
    "plan": "plan planning", "inceleme": "review", "diyagram": "diagram", "not": "notes obsidian",
    "araştırma": "research", "web sitesi": "website web landing", "site": "website web", "tanıtım": "promo launch marketing landing",
    "ürün": "product", "panel": "dashboard admin", "mobil": "mobile", "e-ticaret": "ecommerce shop",
    "yapay zeka": "ai generative", "ajan": "agent", "otomasyon": "automation", "karakter": "character",
}
TEKNOLOJI_IPUCU = {  # package.json bağımlılığı -> teknoloji etiketi
    "react": "react", "next": "next.js", "vue": "vue", "svelte": "svelte", "tailwindcss": "tailwind",
    "three": "three.js", "@react-three/fiber": "r3f", "gsap": "gsap", "motion": "motion", "framer-motion": "motion",
    "lenis": "lenis", "lottie-web": "lottie", "playwright": "playwright", "@playwright/test": "playwright",
    "typescript": "typescript", "remotion": "remotion",
}


# ================================================================== yardımcılar
class Rapor:
    def __init__(self):
        self.satirlar = []

    def ekle(self, seviye, kod, mesaj):
        self.satirlar.append((seviye, kod, mesaj))

    def say(self, seviye):
        return sum(1 for s in self.satirlar if s[0] == seviye)

    def gruplu(self, seviye):
        """'ad: açıklama' biçimindeki aynı kod + aynı açıklamalı satırları tek satırda toplar."""
        gruplar = {}
        for s, kod, m in self.satirlar:
            if s != seviye:
                continue
            ad, ayir, govde = m.partition(": ")
            anahtar = (kod, govde if ayir and " " not in ad else m)
            gruplar.setdefault(anahtar, []).append(ad if ayir and " " not in ad else None)
        for (kod, govde), adlar in gruplar.items():
            adlar = [a for a in adlar if a]
            yield kod, (f"{', '.join(adlar)}: {govde}" if adlar else govde)

    def yazdir(self):
        for seviye in ("HATA", "UYARI", "BİLGİ"):
            for kod, m in self.gruplu(seviye):
                print(f"  [{seviye}] {kod}: {m}")

    def markdown(self, baslik):
        out = [f"# {baslik}", "", f"Tarih: {datetime.now():%Y-%m-%d %H:%M}", ""]
        for seviye in ("HATA", "UYARI", "BİLGİ"):
            liste = list(self.gruplu(seviye))
            if liste:
                out += [f"## {seviye} ({self.say(seviye)})", ""] + [f"- **{k}**: {m}" for k, m in liste] + [""]
        return "\n".join(out)


def registry():
    r = json_oku(REGISTRY)
    if not r or not r.get("skiller"):
        sys.exit("registry.json yok ya da boş. Önce: python3 araclar/arsiv-yerlestir.py")
    return r["skiller"]


def bul(skiller, anahtar):
    """Kullanıcı isteği için: id ile tam eşleşme; yoksa ad ile 'tercih' kaydı."""
    for s in skiller:
        if s["id"] == anahtar:
            return s
    adaylar = sorted((s for s in skiller if s["ad"] == anahtar), key=lambda s: s["durum"] != "tercih")
    return adaylar[0] if adaylar else None


def kaynak_bul(skiller, k):
    """Kurulu bir skill'i KAYNAĞINA göre bul (repo + repo içi yol). id değişse bile doğru skill bulunur;
    kaynak artık yoksa None (başka bir repo'nun aynı adlı skill'i ASLA yerine konmaz)."""
    repo = repo_guncel(k.get("repo"))  # repo GitHub'da taşındıysa (kaynaklar.json -> eski_adlar) kilitteki eski ad da eşleşir
    if "kaynak_yol" in k:
        return next((s for s in skiller if s["repo"] == repo and s["kaynak_yol"] == k["kaynak_yol"]), None)
    s = next((s for s in skiller if s["id"] == k["id"]), None)  # eski kilit: sadece aynı repodan kabul et
    return s if s and s["repo"] == (repo or s["repo"]) else None


def canli_global(s):
    """Global klasörler kurulum anında yeniden okunur (registry'deki bilgi eskimiş olabilir)."""
    return global_durum(s["ad"], s.get("ana_hash") or s["klasor_hash"])


def kurulum_adi(s, kilit=None):
    """Projede kullanılacak klasör/skill adı.
    - Kilitte bu KAYNAK zaten kuruluysa: o ad (ad sonradan değişmez, çift kurulum olmaz).
    - Alternatif sürüm: <ad>--<kaynak>.
    - Global klasörde aynı adlı FARKLI içerik varsa (Claude'da kişisel skill proje skill'ini ezer): <ad>--kutuphane."""
    if kilit:
        for ad, k in kilit["skiller"].items():
            if repo_guncel(k.get("repo")) == s["repo"] and k.get("kaynak_yol", None) == s["kaynak_yol"]:
                return ad
    ad = s["ad"] if ROL_ADI.match(s["ad"]) else (re.sub(r"[^a-z0-9-]+", "-", s["ad"].lower()).strip("-")[:64] or "skill")
    if "@" in s["id"]:
        ad = f"{ad}--{s['id'].split('@')[1]}"
    elif any(v == "farkli" for v in canli_global(s).values()):
        ad = f"{ad}--kutuphane"
    return ad[:64]


def meta(proje):
    return proje / META


def kilit_oku(proje):
    k = json_oku(meta(proje) / "kilit.json")
    if k is None:
        eski = proje / ".agents" / "skills" / "SKILLS.lock.json"  # sürüm 1 kilidi
        k = json_oku(eski) if eski.exists() else None
    if k is None:
        k = {"surum": KILIT_SURUM, "kutuphane": str(KOK), "profil": None, "roller": [], "skiller": {}}
    k.setdefault("roller", [])
    k.setdefault("skiller", {})
    k.setdefault("profil", None)
    k.setdefault("arac_secimi", "secildi" if "araclar" in k else "varsayilan")  # diske yalnız kilit_yaz yazar
    for v in k["skiller"].values():
        v.setdefault("roller", [])
    k["surum"] = KILIT_SURUM
    return k


def kilit_yaz(proje, kilit):
    kilit["guncelleme"] = date.today().isoformat()
    kilit["proje_yolu"] = str(proje)
    if isinstance(kilit.get("dis_skiller"), dict) and not kilit["dis_skiller"]:
        del kilit["dis_skiller"]  # önceden olan anahtar boşaldı: kilit dış skili olmayan projelerle aynı biçime döner
    if isinstance(kilit.get("kitler"), dict) and not kilit["kitler"]:
        del kilit["kitler"]       # boşalan kitler anahtarı kaldırılır: kitsiz projelerin kilit biçimi değişmez
    if "araclar" not in kilit:  # seçim hiç yapılmadıysa varsayılan kayda geçer ve "varsayılan" diye işaretlenir
        kilit["araclar"] = list(ARACLAR["ikisi"])
        kilit.setdefault("arac_secimi", "varsayilan")
    meta(proje).mkdir(exist_ok=True)
    json_yaz(meta(proje) / "kilit.json", kilit)


def codex_var(kilit):
    """Proje Codex'i de kullanıyor mu? (kilit 'araclar'; eski kilitlerde varsayılan: ikisi)"""
    return "codex" in kilit.get("araclar", ARACLAR["ikisi"])


def duzen_adi(kilit):
    """Projenin araç düzeni: 'ortak' (Claude + Codex + ...) ya da 'yalniz-claude'."""
    return "ortak" if codex_var(kilit) else "yalniz-claude"


def duzen_uygula(kilit, secim):
    """--arac değerini (eski adlar dahil) kilide yazar. Kilitteki liste hep ['claude','codex'] ya da ['claude'] kalır."""
    d = ARAC_TAKMA.get(secim, secim)
    kilit["araclar"] = list(ARACLAR[d])
    kilit["arac_secimi"] = "secildi"
    return d


def arac_kayitlari(yol=None):
    """yapay-zeka-araclari.json -> kayıt listesi; yok/bozuksa None (çağıran satırları atlar, çökmez)."""
    try:
        d = json_oku(Path(yol) if yol else ARAC_JSON)
    except (OSError, ValueError):
        return None
    if not isinstance(d, dict) or not isinstance(d.get("araclar"), list):
        return None
    return [k for k in d["araclar"] if isinstance(k, dict)]


def arac_korunan_yollar(kayitlar=None):
    """Araçların kullanıcı klasörleri (ör. ~/.gemini): proje olarak kabul edilmez. Veri yoksa []."""
    kayitlar = arac_kayitlari() if kayitlar is None else kayitlar
    out = []
    for k in kayitlar or []:
        kok = k.get("kullanici_koku")
        if isinstance(kok, str) and kok.startswith("~"):
            out.append(Path(kok).expanduser().resolve())
    return out


def _adlar(kayitlar):
    return ", ".join(k["ad_kisa"] for k in kayitlar)


def arac_satirlari(proje, kilit, rapor, secim=None, kayitlar=None):
    """Araç düzeni bilgi satırları (hepsi BİLGİ): hangi araç bu projedeki skilleri görür/görmez."""
    kayitlar = arac_kayitlari() if kayitlar is None else kayitlar
    if not kayitlar:
        rapor.ekle("BİLGİ", "arac-belge-yok", "yapay-zeka-araclari.json okunamadı; hangi aracın skilleri göreceği satırları atlandı "
                   "(kurulum etkilenmez).")
        return
    duzen = duzen_adi(kilit)
    klasorler = DUZEN_KLASORLERI[duzen]
    kurulu = [k for k in kayitlar if k.get("kurulu")]
    gorur = lambda k: bool(set(k.get("proje_skill_okur", [])) & set(klasorler))  # noqa: E731
    gorenler = [k for k in kurulu if gorur(k)]
    gormeyenler = [k for k in kurulu if not gorur(k)]
    if duzen == "ortak":
        klasor_metni = "Klasörler: .agents/skills (gerçek kopya) + .claude/skills (bağ)."
    else:
        klasor_metni = "Klasör: .claude/skills (gerçek kopya)."
    metin = (f"Araç düzeni: {duzen} (seçim: {'seçildi' if kilit.get('arac_secimi') == 'secildi' else 'varsayılan'}). {klasor_metni} "
             f"Skilleri görenler: {_adlar(gorenler) or 'yok'}. Görmeyenler: {_adlar(gormeyenler) or 'yok'}. "
             f"Talimat bloğu: {', '.join(DUZEN_TALIMAT[duzen])}.")
    yok = [k for k in kayitlar if k.get("destek") == "istege-bagli" and not k.get("kurulu")]
    if duzen == "ortak" and yok:
        metin += f" Kurulu olmayan: {_adlar(yok)} (.agents/skills'i okur; GEMINI.md yazılmıyor)."
    rapor.ekle("BİLGİ", "arac-duzeni", metin)
    if gormeyenler:
        rapor.ekle("BİLGİ", "arac-gormez", f"Bu düzende {_adlar(gormeyenler)} bu projedeki skilleri GÖRMEZ "
                   "(okudukları klasör: .agents/skills). Onları da kullanacaksan: --arac ortak.")
    if kilit.get("arac_secimi") == "varsayilan" and secim is None:
        rapor.ekle("BİLGİ", "arac-secimi-yok", "Bu proje için araç düzeni hiç seçilmedi; varsayılan 'ortak' uygulanıyor. Projenin hangi "
                   "araçlarla açılacağını (Claude Code, Codex, Antigravity, Cursor, VS Code Copilot, Windows) kullanıcıya sor, sonra "
                   "--arac ortak ya da --arac yalniz-claude ile kaydet (rehber/14).")
    if duzen == "ortak":
        cift = [k for k in kurulu if set(klasorler) <= set(k.get("proje_skill_okur", []))]
        if cift:
            rapor.ekle("BİLGİ", "arac-cift-okuma", f"{_adlar(cift)} hem .agents/skills hem .claude/skills klasörünü okur; aynı skill iki kez "
                       "listelenebilir (belgede yok, denenmedi). Görürsen kullanıcıya bildir (rehber/14 bölüm 9).")
        if (proje / ".git").exists():
            rapor.ekle("BİLGİ", "arac-symlink", ".claude/skills altındaki bağlar symlink'tir; Windows'ta ve core.symlinks kapalı git'te düz "
                       "metin dosyasına döner, Claude skilleri göremez. Proje Windows'ta açılacaksa --arac yalniz-claude kullan "
                       "(Codex ve Antigravity görmez; rehber/14 bölüm 5).")
    if kilit.get("roller"):
        rolsuz = [k for k in kurulu if not (k.get("rol_dosyasi") or {}).get("uretilir", True) and k.get("anahtar") != "cursor"]
        if rolsuz:
            rapor.ekle("BİLGİ", "arac-rolsuz", "Rol dosyaları yalnız Claude (.claude/agents) ve Codex (.codex/agents) için üretilir. Cursor "
                       f".claude/agents dosyalarını da okur (belge). {_adlar(rolsuz)} için rol dosyası üretilmez: orada her ajan projedeki "
                       "tüm skilleri görür.")
        if codex_var(kilit):
            rapor.ekle("BİLGİ", "arac-mutlak-yol", ".codex/agents/*.toml içinde bu bilgisayarın mutlak yolları var; proje başka klasöre ya da "
                       "bilgisayara taşınırsa Codex rol dışı skilleri kapatamaz. Kütüphanenin olduğu bilgisayarda --yenile çalıştır.")


def kurulu_hash(proje, ad):
    h = proje / ".agents" / "skills" / ad
    c = proje / ".claude" / "skills" / ad
    return {"codex": klasor_hash(h) if h.is_dir() else None,
            "claude": klasor_hash(c) if (c.is_dir() and not c.is_symlink()) else "symlink" if c.is_symlink() else None}


def elle_degismis(proje, ad, kayit):
    beklenen = kayit.get("kurulu_hash")
    if not beklenen:
        return False
    simdi = kurulu_hash(proje, ad)
    if simdi == beklenen:
        return False
    # Claude symlink'i aynı içerikli gerçek kopyaya dönmüşse (klasör kopyalanınca/commit edilince olur) içerik değişmemiştir
    return not (beklenen.get("claude") == "symlink" and simdi["codex"] == beklenen.get("codex")
                and simdi["claude"] == beklenen.get("codex"))


# ================================================================== yedek / geri alma
def meta_gitignore(proje):
    """.skill-kutuphanesi/.gitignore: yedek/ klasörü git'e girmesin. Var olan satırlar asla değiştirilmez, yalnız eksikse eklenir."""
    g = meta(proje) / ".gitignore"
    try:
        mevcut = g.read_text(encoding="utf-8") if g.exists() else ""
        if any(s.strip().rstrip("/") == "yedek" for s in mevcut.splitlines()):
            return
        with g.open("a", encoding="utf-8") as f:
            f.write(("" if not mevcut or mevcut.endswith("\n") else "\n") + "yedek/\n")
    except OSError:
        pass  # yan ürün: yedeği asla engellemez


def goreli_proje_yolu_gecerli(rel):
    """Proje içi göreli dosya/klasör yolu mu? Mutlak yol, boş, '.' ve '..' bileşeni içeremez."""
    if not isinstance(rel, str) or not rel or rel.startswith("/") or "\0" in rel:
        return False
    p = Path(rel)
    return not p.is_absolute() and bool(p.parts) and ".." not in p.parts and p.parts != (".",)


def yedekle(proje, adlar, neden, ek_hedefler=()):
    zaman = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    hedefler = [".claude/agents", ".codex/agents", "AGENTS.md", "CLAUDE.md", str(AYAR), f"{META}/kilit.json"]
    hedefler += [f".agents/skills/{a}" for a in adlar] + [f".claude/skills/{a}" for a in adlar]
    for ek in ek_hedefler:
        if ek and ek not in hedefler:
            hedefler.append(ek)
    for rel in hedefler:
        if not goreli_proje_yolu_gecerli(rel) or not proje_ici(proje, proje / rel):
            raise RuntimeError(f"yedek hedefi proje dışına gidiyor: {rel!r}")
    y = meta(proje) / "yedek" / zaman
    y.mkdir(parents=True)
    meta_gitignore(proje)
    var_olan = []
    var_olan_ust = set()
    for rel in hedefler:
        kaynak = proje / rel
        ust = Path(rel).parent
        while str(ust) not in ("", "."):
            if (proje / ust).exists() or (proje / ust).is_symlink():
                var_olan_ust.add(ust.as_posix())
            ust = ust.parent
        if kaynak.is_symlink():
            (y / rel).parent.mkdir(parents=True, exist_ok=True)
            os.symlink(os.readlink(kaynak), y / rel)
            var_olan.append(rel)
        elif kaynak.is_dir():
            shutil.copytree(kaynak, y / rel, symlinks=True)
            var_olan.append(rel)
        elif kaynak.is_file():
            (y / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(kaynak, y / rel)
            var_olan.append(rel)
    json_yaz(y / "yedek.json", {"neden": neden, "zaman": zaman, "hedefler": hedefler, "var_olan": var_olan,
                                "var_olan_ust": sorted(var_olan_ust)})
    yedekler = sorted((meta(proje) / "yedek").iterdir())
    for eski in yedekler[:-YEDEK_SAYISI]:
        shutil.rmtree(eski, ignore_errors=True)
    return y


def sil_yol(p: Path):
    if p.is_symlink() or p.is_file():
        p.unlink()
    elif p.is_dir():
        shutil.rmtree(p)


def geri_yukle(proje, y: Path):
    bilgi = json_oku(y / "yedek.json")
    hedefler = bilgi.get("hedefler") or []
    var_olan = bilgi.get("var_olan") or []
    for rel in list(hedefler) + list(var_olan):
        if not goreli_proje_yolu_gecerli(rel) or not proje_ici(proje, proje / rel) or not proje_ici(y, y / rel):
            raise RuntimeError(f"yedek kaydı proje dışına gidiyor: {rel!r}")
    for rel in hedefler:
        sil_yol(proje / rel)
    for rel in var_olan:
        k, h = y / rel, proje / rel
        h.parent.mkdir(parents=True, exist_ok=True)
        if k.is_symlink():
            os.symlink(os.readlink(k), h)
        elif k.is_dir():
            shutil.copytree(k, h, symlinks=True)
        else:
            shutil.copy2(k, h)
    if "var_olan_ust" in bilgi:
        var_olan_ust = set(bilgi.get("var_olan_ust") or [])
        var_olan_set = set(var_olan)
        for rel in hedefler:
            if rel in var_olan_set:
                continue
            ust = Path(rel).parent
            while str(ust) not in ("", "."):
                rel_ust = ust.as_posix()
                if rel_ust in var_olan_ust or rel_ust == META or rel_ust.startswith(META + "/"):
                    break
                p_ust = proje / ust
                if not proje_ici(proje, p_ust) or p_ust == proje or p_ust.is_symlink() or not p_ust.is_dir():
                    break
                try:
                    if not any(p_ust.iterdir()):
                        p_ust.rmdir()
                        ust = ust.parent
                    else:
                        break
                except OSError:
                    break
    return bilgi


# ================================================================== kurulum
def metin_oku(f: Path):
    return f.read_bytes().decode("utf-8")


def metin_yaz(f: Path, metin: str):
    f.write_bytes(metin.encode("utf-8"))  # satır sonları (CRLF/LF) olduğu gibi kalır


_EV_YOLU = re.compile(r"/(?:Users|home)/[^/\s]+/$")


def ad_metni_degistir(metin: str, eski_adlar, yeni: str) -> str:
    """Metindeki proje içi '.claude|.agents|.codex/skills/<eski ad>' yollarını yeni adla değiştirir (yollari_yeniden_adlandir'ın metin çekirdeği).
    Ev önekli (~/ $HOME/ ${HOME}/ /Users/<ad>/ /home/<ad>/) bilgisayar geneli yollar DEĞİŞMEZ: onlar yollari_yerellestir'in işidir (arşivdeki
    satırla eşleşebilsin). Proje içi biçimler (.claude/skills/x, ${CLAUDE_PROJECT_DIR}/.claude/skills/x) adlandırılır."""
    eski_adlar = {a for a in eski_adlar if a and a != yeni}
    if not eski_adlar:
        return metin
    desen = re.compile(r"(?<!~/)(?<!\$HOME/)(?<!\$\{HOME\}/)(\.(?:claude|agents|codex)/skills/)(?:" + "|".join(re.escape(a) for a in eski_adlar)
                       + r")(?=[/\s`'\")\]]|$)", re.M)
    return desen.sub(lambda m: m.group(0) if _EV_YOLU.search(m.string[max(0, m.start() - 256):m.start()]) else m.group(1) + yeni, metin)


def yollari_yeniden_adlandir(klasor: Path, eski_adlar, yeni: str):
    """Skill kendi yolunu içeriyorsa (.claude/skills/<ad>/scripts…) yeniden adlandırınca bu yolları da düzelt."""
    if not {a for a in eski_adlar if a and a != yeni}:
        return
    for f in klasor.rglob("*"):
        if f.is_file() and f.suffix.lower() in YENIDEN_ADLANDIRMA_UZANTI:
            try:
                metin = metin_oku(f)
            except (UnicodeDecodeError, OSError):
                continue
            yeni_metin = ad_metni_degistir(metin, eski_adlar, yeni)
            if yeni_metin != metin:
                metin_yaz(f, yeni_metin)


def kardes_haritasi(s, skiller, kilit, kur_listesi=None, adlar=None, farkli=None):
    """Skill'in kardeş bağlantıları için {anahtar: (projedeki kurulum adı, kurulu mu)}. Eşleşme YALNIZ KİMLİKLE yapılır
    (aynı ad, farklı kimlik = başka skill: kurulu sayılmaz, yol çevrilmez; farkli listesine (anahtar, kardeş kimliği, bulunan kimlik) eklenir).
    - ../<kardeş>/ bağlantıları (kardes_bagimliliklari): anahtar kardeş adı. Öncelik: bu işlemde kurulan, sonra projede kurulu olan;
      ikisi de yoksa kardeşin alacağı ad tahmin edilir (kurulu=False).
    - sabit yolla anılan kardeş (~/.claude/skills/<kardeş>/…, ${CLAUDE_PLUGIN_ROOT}/skills/<kardeş>/…; ortak.yol_degerlendir 'cevrilecek_kardes'):
      anahtar "genel:<ad>"; YALNIZ kardeş kuruluyorsa ya da kurulu ise girer (kilitte 'kardes' alanına yazılır: kardeş sonradan kurulunca/kaldırılınca
      değer değişir ve yollar yeniden yazılır). Sabit kardeş yolu olmayan skill'in haritası eskisiyle aynıdır."""
    harita, kur_listesi, kilitli = {}, kur_listesi or {}, {}

    def kilitliler():
        if not kilitli:
            kilitli.update({ad: x for ad, k in kilit["skiller"].items() if (x := kaynak_bul(skiller, k))})
        return kilitli

    def ara(kid, kad):
        """(kurulum adı, None) kimlik eşleşirse; (None, başka kimlik) yalnız aynı ad başka skill'de varsa; (None, None) hiçbiri."""
        if kid in kur_listesi:
            return adlar[kid], None
        for ad, x in kilitliler().items():
            if x["id"] == kid:
                return ad, None
        for sid, (x, _) in kur_listesi.items():
            if x["ad"] == kad or x.get("klasor_adi") == kad:
                return None, sid
        for ad, x in kilitliler().items():
            if x["ad"] == kad or x.get("klasor_adi") == kad:
                return None, x["id"]
        return None, None

    for kad, bilgi in (s.get("kardes_bagimliliklari") or {}).items():
        ad, baska = ara(bilgi["id"], kad)
        if ad:
            harita[kad] = (ad, True)
        elif baska:
            harita[kad] = (kad, False)  # yol çevrilmez
            if farkli is not None:
                farkli.append((kad, bilgi["id"], baska))
        else:
            x = next((x for x in skiller if x["id"] == bilgi["id"]), None)
            harita[kad] = (kurulum_adi(x, kilit) if x else kad, False)
    for hedef, kid in sorted({(b["hedef"], b["kardes_id"]) for b in yol_degerlendir(s, skiller).get("cevrilecek_kardes", [])}):
        ad, baska = ara(kid, hedef)
        if ad:
            harita[GENEL_KARDES + hedef] = (ad, True)
        elif baska and farkli is not None:
            farkli.append((GENEL_KARDES + hedef, kid, baska))
    return harita


def kardes_metni_degistir(metin: str, derinlik: int, harita) -> str:
    """../<kardeş>/ yollarını (derinlik = dosyanın skill köküne göre derinliği: ../ sayısı) kardeşin projedeki adına çevirir (metin çekirdeği)."""
    harita = {k: v for k, v in harita.items() if k != v and not k.startswith(GENEL_KARDES)}  # genel:<ad> anahtarları sabit yollar içindir (yollari_yerellestir)
    if not harita:
        return metin
    adlar = "|".join(re.escape(a) for a in sorted(harita, key=len, reverse=True))
    desen = re.compile(r"(?<![\w./-])(" + re.escape("../" * derinlik) + r")(" + adlar + r")(?=[/)\s`'\"#]|$)", re.M)
    return desen.sub(lambda m: m.group(1) + harita[m.group(2)], metin)


def kardes_yollarini_yeniden_adlandir(klasor: Path, harita):
    """../<kardeş>/... bağlantılarını kardeşin projedeki adına çevirir (ör. ../hyperframes/ -> ../hyperframes--kutuphane/).
    Sadece skill kökünden tam bir seviye yukarı çıkan yollar değişir (dosya derinliğine göre ../ sayısı)."""
    if not {k: v for k, v in harita.items() if k != v and not k.startswith(GENEL_KARDES)}:
        return
    for f in klasor.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in (".md", ".mdx", ".txt", ".sh", ".py", ".js", ".mjs", ".json", ""):
            continue
        try:
            metin = metin_oku(f)
        except (UnicodeDecodeError, OSError):
            continue
        yeni_metin = kardes_metni_degistir(metin, len(f.relative_to(klasor).parts), harita)
        if yeni_metin != metin:
            metin_yaz(f, yeni_metin)


def isim_esitle(skill_md: Path, ad: str, aciklama=None):
    """SADECE frontmatter içindeki name alanını klasör adına eşitler (gövdedeki örnek yaml'lara dokunmaz)."""
    metin = metin_oku(skill_md)
    m = re.match(r"^(\ufeff?---[ \t]*(\r?\n))(.*?)(\r?\n---[ \t]*(?:\r?\n|$))", metin, re.S)
    if not m:
        nl = "\r\n" if "\r\n" in metin else "\n"
        metin_yaz(skill_md, f"---{nl}name: {ad}{nl}description: {json.dumps(aciklama or ad, ensure_ascii=False)}{nl}---{nl}{nl}" + metin)
        return
    bas, nl, govde, son = m.group(1), m.group(2), m.group(3), m.group(4)
    nm = re.search(r"^name:[ \t]*(.*)$", govde, re.M)
    if nm and nm.group(1).strip().strip("'\"") == ad:
        return
    govde = (govde[:nm.start()] + f"name: {ad}" + govde[nm.end():]) if nm else f"name: {ad}{nl}" + govde
    metin_yaz(skill_md, bas + govde + son + metin[m.end():])


def tetikleme_sorunu(y: str) -> bool:
    """Bu yapısal sorun skill'in description'la tetiklenmesini engeller/bozar mı?"""
    return any(x in y for x in ("frontmatter yok", "description yok", "description çok uzun", "description çok kısa",
                                "dosya başında değil", "tırnaksız"))


def oto_onarilir(y: str) -> bool:
    """aciklama_duzeltme gerekmeden kurulumda kendiliğinden düzelen sorunlar."""
    return "dosya başında değil" in y or "tırnaksız" in y


def symlink_taslaklarini_coz(klasor: Path):
    """Kaynakta git symlink'i olan, arşive düz metin olarak gelmiş '../<kardeş>' taslaklarını kaldırır ve onlara giden
    bağlantıları kardeş skill yoluna çevirir (sonra kardes_yollarini_yeniden_adlandir projedeki ada eşler)."""
    taslaklar = symlink_taslaklari(klasor)
    if not taslaklar:
        return
    for ad in taslaklar:
        (klasor / ad).unlink()
    for f in klasor.rglob("*"):
        if f.is_file() and f.suffix.lower() in (".md", ".mdx", ".txt"):
            metin = metin_oku(f)
            yeni = taslak_baglantilarini_cevir(metin, taslaklar, len(f.relative_to(klasor).parts) - 1)
            if yeni != metin:
                metin_yaz(f, yeni)


def aciklama_onar(skill_md: Path, s, ad):
    """Tetiklenmeyi engelleyen frontmatter sorunlarını KURULAN KOPYADA düzeltir (arşivdeki orijinal değişmez):
    yorum arkasındaki frontmatter başa alınır, YAML'ı bozan description tırnaklanır, registry'deki
    aciklama_duzeltme.description (eksik/kısa/uzun description için elle yazılmış) uygulanır."""
    metin = metin_oku(skill_md)
    yeni, yapilan = frontmatter_onar(metin, ad, (s.get("aciklama_duzeltme") or {}).get("description"))
    if yeni != metin:
        metin_yaz(skill_md, yeni)
    return yapilan


def frontmatter_adi(skill_md: Path):
    m = re.match(r"^\ufeff?---[ \t]*\r?\n(.*?)\r?\n---", metin_oku(skill_md), re.S)
    nm = re.search(r"^name:[ \t]*(.*)$", m.group(1), re.M) if m else None
    return nm.group(1).strip().strip("'\"") if nm else None


def _satirlari_cevir(metin: str, arsiv_satirlar, isler, donustur=None):
    """isler: [(bulgu, yeni yol)]. Her bulgunun ARŞİV satırının TAM içeriği kurulan dosyada aynen aranır; bulunan satırlarda bulgunun ham yolu yeni yolla
    değişir (aynı içerikli satırların hepsinde; CRLF/LF olduğu gibi kalır). donustur(satır): kurulumda önce çalışan ad/kardeş yeniden adlandırma geçişlerinin
    aynısı (satır ve yol onlardan geçmiş halleriyle de aranır: yeniden adlandırılmış kurulumda eşleşme kaybolmasın). Döner: (yeni metin, bulunamayan bulgular)."""
    satirlar = metin.split("\n")
    mevcut, degisecek, bulunamayan = set(satirlar), {}, []
    for b, yeni in isler:
        if not 0 < b["satir"] <= len(arsiv_satirlar):
            bulunamayan.append(b)
            continue
        satir, ham = arsiv_satirlar[b["satir"] - 1], b["ham"]
        if satir not in mevcut and donustur:
            satir, ham = donustur(satir), donustur(ham)  # önceki geçişlerin değiştirdiği biçim
        if satir in mevcut and ham in satir:
            degisecek.setdefault(satir, set()).add((ham, yeni))
        else:
            bulunamayan.append(b)
    for i, satir in enumerate(satirlar):
        for ham, yeni in sorted(degisecek.get(satir, ()), key=lambda x: -len(x[0])):
            # sınır denetimi: daha uzun (çevrilebilir olmayan) bir yolun öneki olan metin değişmez (a.md, a.mdx içinde değişmez)
            satirlar[i] = re.sub(re.escape(ham) + r"(?![\w~@+-]|[./]\w)", lambda m, y=yeni: y, satirlar[i])
    return "\n".join(satirlar), bulunamayan


def yollari_yerellestir(klasor: Path, kaynak: Path, s, ad: str, kardes, onek: str, skiller):
    """Kurulan kopyada (klasor) arşiv taramasının 'çevrilebilir' bulduğu sabit yolları proje içi yola çevirir; hazirla()'nın SON geçişidir.
    'Dar çevir': yalnız ajan sınıfı metin dosyaları; doküman dosyaları, install/setup/bootstrap ve karışık dosyalar, kod dosyaları, iki yerleşim kökü
    ya da kurulum komutu olan satırlar, kalan boş yollar ve arşivde olmayan hedefler çevrilmez (ortak.yol_taramasi bunları 'cevrilebilir' saymaz).
      kendi yolu     ~/.claude/skills/<ad>/<kalan>, ${CLAUDE_PLUGIN_ROOT}/.claude/skills/<ad>/<kalan>  ->  <onek>/<kurulum adı>/<kalan>
      kardeş yolu    …/skills/<kardeş>/<kalan>  ->  <onek>/<kardeşin kurulum adı>/<kalan>  (yalnız kardeş kuruluyorsa: kardes['genel:<ad>'])
      dar geçiş      onek == .claude/skills iken proje içi .agents/skills/<kendi ad>/<kalan>  ->  .claude/skills/<kurulum adı>/<kalan>
    Döner: görünür uyarı metinleri (arşiv satırı kurulan kopyada bulunamayan, yani önceki bir geçişin değiştirdiği yollar çevrilmez ve sayılır)."""
    skiller = tum_skiller(skiller)
    sv = s  # taranan klasör = kurulan kaynak klasör: claude/codex varyantı kendi sabit yollarıyla taranır (ana arşive göre değil)
    if Path(kaynak) != KOK / s["yol"]:
        sv = dict(s, yol=str(kaynak), klasor_hash=None)  # KOK / <mutlak yol> = o yol; önbellek anahtarı yol içerdiği için ana arşivle karışmaz
    d = yol_degerlendir(sv, skiller)
    isler = [(b, f"{onek}/{ad}/{b['kalan']}") for b in d["cevrilecek"] if _var_bak(kaynak, b["kalan"]) is not False]
    for b in d.get("cevrilecek_kardes", []):
        v = (kardes or {}).get(GENEL_KARDES + b["hedef"])
        if v and v[1]:
            isler.append((b, f"{onek}/{v[0]}/{b['kalan']}"))
    yamali = set((s.get("yama") or {}).get("dosyalar") or {})  # yama dosyanın TAMAMINI elle yazılmış halle değiştirir: yol çevirisi o dosyaya uygulanmaz
    dosyalar, bulunamayan = {}, []
    for b, yeni in isler:
        if b["dosya"] not in yamali:
            dosyalar.setdefault(b["dosya"], []).append((b, yeni))
    for rel, liste in sorted(dosyalar.items()):
        try:
            arsiv_satirlar = metin_oku(kaynak / rel).split("\n")
            hedef_dosya = klasor / rel
            if not hedef_dosya.is_file():
                raise OSError(rel)
            metin = metin_oku(hedef_dosya)
        except (UnicodeDecodeError, OSError):
            bulunamayan += [b for b, _ in liste]
            continue
        derinlik = len(Path(rel).parts)
        yeni_metin, yok = _satirlari_cevir(
            metin, arsiv_satirlar, liste,
            lambda x: kardes_metni_degistir(ad_metni_degistir(x, {s["ad"], s.get("klasor_adi")}, ad), derinlik, {k: v[0] for k, v in (kardes or {}).items()}))
        bulunamayan += yok
        if yeni_metin != metin:
            metin_yaz(hedef_dosya, yeni_metin)
    uyarilar = []
    if onek == ".claude/skills":  # dar geçiş: sadece-Claude kurulumda kendi klasörüne .agents/skills/<ad>/… diyen proje içi yollar
        adlar = skill_adlari(s, skiller) | {ad}
        karisik = {b["dosya"] for b in skill_yol_taramasi(sv, skiller)
                   if b["tur"] in ("genel-kendi", "genel-baska", "genele-kopyalar") or "kurulum-komutu" in b["engeller"]}
        for rel, (sinif, betik) in sorted(yol_dosya_sinifi_haritasi(kaynak).items()):
            if sinif != "ajan" or betik or rel in karisik or Path(rel).suffix.lower() not in YEREL_UZANTI:
                continue
            f = klasor / rel
            try:
                metin = metin_oku(f)
            except (UnicodeDecodeError, OSError):
                continue
            yeni_metin, n = ev_ici_kendi_cevir(metin, adlar, ad, onek, kaynak)
            if n:
                metin_yaz(f, yeni_metin)
    if bulunamayan:
        ornek = "; ".join(sorted({f"{b['dosya']}:{b['satir']} {b['ham'][:60]}" for b in bulunamayan})[:3])
        uyarilar.append(f"{ad}: {len(bulunamayan)} sabit yol çevrilemedi (arşivdeki satır kurulan kopyada aynen yok: önceki bir düzeltme ya da yama "
                        f"değiştirmiş, ya da bu sürümde dosya yok): {ornek}")
    return uyarilar


def hazirla(kaynak: Path, hedef: Path, s, ad, kardes=None, onek=None, skiller=None, symlink_yasak=False):
    """Geçici klasöre kopyala, adı ve iç yolları düzelt, sonra yerine taşı (yarım kurulum kalmaz).
    onek: kopyanın proje içi skills klasörü ('.agents/skills' | '.claude/skills'); verilirse sabit yollar son geçişte proje içi yola çevrilir
    (None = çevrilmez). symlinks=True ile kopyalanır ki symlink hedefleri çözümlenip dış dosya içeriği sızmasın.
    Döner: görünür uyarı metinleri listesi (çoğu zaman boş)."""
    gecici = hedef.parent / f".{ad}.kurulum-tmp"
    sil_yol(gecici)
    gecici.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(kaynak, gecici, symlinks=True, ignore=shutil.ignore_patterns("KAYNAK.md"))
    if symlink_yasak:
        for yol_, dizinler_, dosyalar_ in os.walk(gecici, followlinks=False):
            for isim_ in list(dizinler_) + list(dosyalar_):
                if (Path(yol_) / isim_).is_symlink():
                    sil_yol(gecici)
                    raise RuntimeError(f"{ad}: kaynakta symlink bulundu ({isim_}); güvenlik nedeniyle kurulmaz")
    symlink_taslaklarini_coz(gecici)
    yamalari_uygula(gecici, s)
    aciklama_onar(gecici / "SKILL.md", s, ad)
    isim_esitle(gecici / "SKILL.md", ad, s.get("aciklama"))
    yollari_yeniden_adlandir(gecici, {s["ad"], s.get("klasor_adi")}, ad)
    kardes_yollarini_yeniden_adlandir(gecici, {k: v[0] for k, v in (kardes or {}).items()})
    uyarilar = yollari_yerellestir(gecici, kaynak, s, ad, kardes, onek, skiller) if onek else []
    sil_yol(hedef)
    gecici.rename(hedef)
    return uyarilar


def kur(s, proje: Path, ad: str, kardes=None, codex=True, skiller=None):
    """Skill'i projeye kurar. Döner: hazirla()'nın görünür uyarıları (çevrilemeyen sabit yollar)."""
    codex_hedef = proje / ".agents" / "skills" / ad
    claude_hedef = proje / ".claude" / "skills" / ad
    var = s.get("varyantlar") or {}
    if not codex:  # sadece Claude: gerçek kopya .claude/skills'te, .agents/skills kopyası kaldırılır
        uyari = hazirla(KOK / var.get("claude", s["yol"]), claude_hedef, s, ad, kardes, ".claude/skills", skiller)
        sil_yol(codex_hedef)
        return uyari
    uyari = hazirla(KOK / var.get("codex", s["yol"]), codex_hedef, s, ad, kardes, ".agents/skills", skiller)
    claude_hedef.parent.mkdir(parents=True, exist_ok=True)
    if var.get("claude"):
        uyari += hazirla(KOK / var["claude"], claude_hedef, s, ad, kardes, ".claude/skills", skiller)
    else:
        sil_yol(claude_hedef)
        os.symlink(os.path.relpath(codex_hedef, claude_hedef.parent), claude_hedef)
    return uyari


# ================================================================== dış skiller: program bağı ve dondurma (K-28)
# Kilitte ayrı üst anahtar: dis_skiller (eski kod yalnız kilit["skiller"]'e bakar). tur: "program-bag" (programın kendi klasörüne bağ)
# ya da "donmus" (projenin kendi kopyası; kütüphane güncellemez). Program klasörüne ASLA yazılmaz; bağlar izlenmez (sil_yol unlink eder).
def dis_ad_gecerli(ad):
    """Dış skill klasör adı: tek yol bileşeni; ilk karakter harf/rakam; fullmatch (satır sonu kabul edilmez); '.kurulum-tmp' ile bitemez."""
    return isinstance(ad, str) and bool(DIS_AD.fullmatch(ad)) and not ad.endswith(".kurulum-tmp")


def dis_kayit_gecerli(anahtar, g):
    return (dis_ad_gecerli(anahtar) and isinstance(g, dict) and g.get("ad") == anahtar and g.get("tur") in DIS_TURLER
            and isinstance(g.get("hedef"), str) and os.path.isabs(g["hedef"])
            and (g["tur"] != "program-bag" or isinstance(g.get("program"), str)))


def dis_kayitlari(kilit):
    """kilit['dis_skiller'] içindeki GEÇERLİ kayıtlar (anahtar, ad, tür, mutlak hedef doğrulanır; geçersizler yok sayılır). Yol bileşeni olarak
    kilitten doğrulanmadan hiçbir ad kullanılmaz."""
    ham = kilit.get("dis_skiller")
    if not isinstance(ham, dict):
        return {}
    return {k: g for k, g in ham.items() if dis_kayit_gecerli(k, g)}


def dis_gecersizleri(kilit):
    """dogrula için: geçersiz dış skill kayıtlarının mesajları."""
    ham = kilit.get("dis_skiller")
    if ham is None:
        return []
    if not isinstance(ham, dict):
        return ["dis_skiller kilitte sözlük değil; kayıtlar yok sayıldı"]
    out = []
    for k, g in ham.items():
        if dis_kayit_gecerli(k, g):
            continue
        if dis_ad_gecerli(k) and isinstance(g, dict) and g.get("ad") == k and g.get("tur") not in DIS_TURLER:
            out.append(f"{k}: bilinmeyen dış skill türü ({g.get('tur')})")
        else:
            out.append(f"{str(k)[:60]!r}: geçersiz dış skill kaydı (anahtar, ad, tür ya da hedef bozuk; kayıt yok sayıldı)")
    return out


def yol_goster(p):
    """Mutlak yol; ev klasörü '~' ile kısaltılır (bloklar proje depolarına girer: kullanıcının ev adı yazılmaz)."""
    s, ev = str(p), str(Path.home())
    if s == ev:
        return "~"
    return "~" + s[len(ev):] if s.startswith(ev + os.sep) else s


def program_kartlari():
    try:
        d = json_oku(PROGRAMLAR)
    except (OSError, ValueError):
        return {}
    k = d.get("programlar") if isinstance(d, dict) else None
    return {a: v for a, v in k.items() if isinstance(v, dict)} if isinstance(k, dict) else {}


def program_karti(program):
    return program_kartlari().get(program) if isinstance(program, str) else None


def program_skill_koku(kart):
    """Kartın skill_koku'nu mutlak Path olarak ('~' açılır); yok/boş/göreli ise None."""
    v = (kart or {}).get("skill_koku")
    if not isinstance(v, str) or not v.strip():
        return None
    p = Path(v.strip()).expanduser()
    return p if p.is_absolute() else None


def program_surumu(kart):
    """Karttaki KAYITLI sürüm (program çalıştırılmaz): git-checkout -> kutuphane_commit ('commit'), diğerleri kutuphane_surumu ('surum')."""
    kart = kart or {}
    if (kart.get("yerinde") or {}).get("tur") == "git-checkout" and kart.get("kutuphane_commit"):
        return kart["kutuphane_commit"], "commit"
    if kart.get("kutuphane_surumu"):
        return kart["kutuphane_surumu"], "surum"
    return None, None


def surum_metni(deger, tur):
    if not deger:
        return "sürüm kayıtsız"
    return str(deger)[:8] if tur == "commit" else str(deger)


def dis_bag_hedefi(g):
    """Bağın BEKLENEN hedefi: kilitten değil karttan türetilir (program + ad -> skill_koku/<klasör>; klasör kartın skill_klasorleri eşlemesinden,
    yoksa skill adı; abspath, realpath değil). Kart yoksa None."""
    kart = program_karti(g.get("program"))
    koku = program_skill_koku(kart)
    return Path(os.path.abspath(koku / program_skill_klasoru(kart, g["ad"]))) if koku else None


def gizli_ad_mi(ad):
    a = ad.casefold()
    return a in DONDUR_GIZLI_TAM or a.startswith(DONDUR_GIZLI_ONEK) or a.endswith(DONDUR_GIZLI_SON)


def dondur_tara(kaynak):
    """Dondurulacak kaynağı SALT OKUR (os.walk, lstat, readlink; dosya İÇERİĞİ açılmaz, hiçbir şey kopyalanmaz). Boyut kopyadan ÖNCE hesaplanır.
    Döner: dosya, bayt, gizli, baglar, ozel, atlanan (göreli yollar), cok (tavan aşıldı; tarama erken bıraktı)."""
    kok = os.path.realpath(kaynak)
    r = {"dosya": 0, "bayt": 0, "gizli": [], "baglar": [], "ozel": [], "atlanan": [], "cok": False, "klasor": 0}
    for yol, dizinler, dosyalar in os.walk(kok, followlinks=False):
        g = os.path.relpath(yol, kok)
        rel = (lambda n, g=g: n if g == "." else f"{g}/{n}")
        r["klasor"] += 1
        if r["klasor"] > DONDUR_TAVAN_KLASOR:
            r["cok"] = True
            return r
        for d in list(dizinler):
            if os.path.islink(os.path.join(yol, d)):
                r["baglar"].append(rel(d) + " (klasör bağı)")
                dizinler.remove(d)
            elif d.casefold() in DONDUR_GIZLI_DIZIN:
                r["gizli"].append(rel(d) + "/")
                dizinler.remove(d)
            elif d in DONDUR_ATLANAN_DIZIN:
                r["atlanan"].append(rel(d) + "/")
                dizinler.remove(d)
        for f in dosyalar:
            if f == ".DS_Store":
                continue
            p = os.path.join(yol, f)
            if gizli_ad_mi(f):
                r["gizli"].append(rel(f))
            st = os.lstat(p)
            if stat.S_ISLNK(st.st_mode):
                hedef = os.path.realpath(p)
                parcalar = set(Path(os.path.relpath(hedef, kok)).parts) if (hedef == kok or hedef.startswith(kok + os.sep)) else None
                if parcalar is None or not os.path.isfile(hedef) or parcalar & (DONDUR_GIZLI_DIZIN | DONDUR_ATLANAN_DIZIN):
                    r["baglar"].append(rel(f))
                    continue
                st = os.stat(hedef)
            elif not stat.S_ISREG(st.st_mode):
                r["ozel"].append(rel(f))
                continue
            r["dosya"] += 1
            r["bayt"] += st.st_size
            if r["dosya"] > DONDUR_TAVAN_DOSYA or r["bayt"] > DONDUR_TAVAN_MB * 1024 * 1024:
                r["cok"] = True
                return r
    return r


def dis_istek_coz(a):
    """--program-skill ve --dondur isteklerini ayrıştırır (yalnız biçim). Döner: (liste, hatalar[(kod, mesaj)]). Doğrulama dis_on_kontrol'de."""
    liste, hatalar, gorulen = [], [], {}
    for x in (getattr(a, "program_skill", None) or []):
        program, ayir, ad = x.partition(":")
        if not ayir or not program.strip() or not ad.strip():  # ad kırpılmaz: 'ffmpeg\n' gibi adlar program-skill-ad ile reddedilir
            hatalar.append(("program-skill-bicim", f"`{x}`: PROGRAM:AD biçiminde yaz, örn. openmontage:ffmpeg"))
            continue
        liste.append({"tur": "program-bag", "ad": ad, "program": program.strip(), "ham": x})
    for x in (getattr(a, "dondur", None) or []):
        yol = Path(x).expanduser()
        if not yol.is_absolute():
            hatalar.append(("dondur-yol", f"`{x}`: mutlak yol ver (~ kullanılabilir)"))
            continue
        liste.append({"tur": "donmus", "ad": yol.name, "kaynak": Path(os.path.abspath(yol)), "ham": x})
    kalan = []
    for it in liste:
        k = it["ad"].casefold()
        if k in gorulen:
            hatalar.append(("dis-ad-cakismasi", f"{it['ad']}: bu çalışmada iki kez isteniyor ({gorulen[k]} ve {it['ham']}); iki tür aynı adı taşıyamaz"))
            continue
        gorulen[k] = it["ham"]
        kalan.append(it)
    return kalan, hatalar


def _program_skilleri_adlari(koku, kart=None):
    """Programdaki skill adları (klasörler; eşlenmiş klasör skill adıyla listelenir, ham klasör adıyla değil)."""
    try:
        return sorted(program_klasor_skill_adi(kart, e.name) for e in os.scandir(koku)
                      if e.is_dir() and os.path.isfile(os.path.join(e.path, "SKILL.md")))
    except OSError:
        return []


def bag_git_izlenenler(proje, adlar, codex):
    """Proje bir git deposuysa: bağ yolları .gitignore'da değil mi? (git check-ignore, salt okur; çıkış 1 = ignore edilmiyor)"""
    if not (proje / ".git").exists():
        return []
    out = []
    for ad in adlar:
        for rel in ([f".agents/skills/{ad}"] if codex else []) + [f".claude/skills/{ad}"]:
            try:
                r = subprocess.run(["git", "-C", str(proje), "-c", "core.fsmonitor=false", "--no-optional-locks", "check-ignore", "-q", "--", rel], capture_output=True, timeout=20,
                                   stdin=subprocess.DEVNULL)
            except (OSError, subprocess.SubprocessError):
                continue
            if r.returncode == 1:
                out.append(rel)
    return out


def dis_sorunlar(proje, kilit, ad, g):
    """Bir dış skill'in sağlık satırları: [(kod, mesaj)]. Bağın hedefi kilitten değil karttan türetilir. Hiçbir şey yazmaz."""
    out = []
    codex = codex_var(kilit)
    h, c = proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad
    rel_h = os.path.relpath(h, c.parent)
    if g["tur"] == "program-bag":
        hedef = dis_bag_hedefi(g)
        if hedef is None:
            return [("kart-yok", f"{ad}: program kartı ya da skill_koku yok ({g.get('program')}); bağ doğrulanamaz (kart geri gelene kadar --kaldir {ad})")]
        if not (hedef / "SKILL.md").is_file():
            koku = hedef.parent
            neden = (f"program klasörü yok: {yol_goster(koku)}; program kurulu değil ya da taşınmış" if not koku.is_dir()
                     else f"skill klasörü yok ya da içinde SKILL.md yok: {yol_goster(hedef)}")
            out.append(("kirik", f"{ad}: program bağı kırık ({g.get('program')}: {neden}); program kuruluysa --yenile, "
                        f"program bu skili kaldırdıysa --kaldir {ad}"))
        elif str(hedef) != g["hedef"]:
            out.append(("hedef-farkli", f"{ad}: kilitteki hedef karttaki program yolundan farklı ({yol_goster(g['hedef'])} -> "
                        f"{yol_goster(hedef)}); --yenile yeni hedefe bağlar"))
        slotlar = [(c, str(hedef))] if not codex else [(h, str(hedef)), (c, rel_h)]
        for slot, beklenen in slotlar:
            rel = slot.relative_to(proje)
            if slot.is_symlink():
                if os.readlink(slot) != beklenen:
                    out.append(("eksik", f"{ad}: bağ eksik ya da başka yere gidiyor ({rel}); --yenile onarır"))
            elif slot.exists():
                out.append(("gercek-klasor", f"{ad}: bağ yerine gerçek klasör var ({rel}); elle değiştirilmiş, --kaldir {ad} ile temizle"))
            else:
                out.append(("eksik", f"{ad}: bağ eksik ya da başka yere gidiyor ({rel}); --yenile onarır"))
        if not codex and (h.exists() or h.is_symlink()):
            out.append(("eksik", f"{ad}: proje sadece Claude kullanıyor ama .agents/skills/{ad} duruyor; --yenile onarır"))
        return out
    # donmuş
    yerlesim = ("yerlesim", f"{ad}: donmuş skill yerleşimi araç düzenine uymuyor; --yenile onarır")
    gercek_mi = lambda p: p.is_dir() and not p.is_symlink() and (p / "SKILL.md").is_file()  # noqa: E731
    beklenen, diger = (h, c) if codex else (c, h)
    if not gercek_mi(beklenen):
        if gercek_mi(diger):
            return [yerlesim]
        return [("donmus-yok", f"{ad}: donmuş skill klasörü yok ya da içinde SKILL.md yok; --geri-al <yedek> ile geri getir ya da --kaldir {ad}")]
    if codex:
        if not (c.is_symlink() and os.readlink(c) == rel_h):
            out.append(yerlesim)
    elif h.exists() or h.is_symlink():
        out.append(yerlesim)
    return out


def proje_ici(proje, p):
    """p'nin (kendisi izlenmeden) proje içinde olduğunu doğrular: üst klasörü proje içinde çözülmeli."""
    kok = os.path.realpath(proje)
    ust = os.path.realpath(p.parent)
    return ust == kok or ust.startswith(kok + os.sep)


def dis_sil(proje, ad):
    """İki slotu siler. Bağ ise yalnız bağ silinir (unlink; hedefe girilmez). Proje dışına asla dokunmaz."""
    if not dis_ad_gecerli(ad):
        raise RuntimeError(f"geçersiz dış skill adı: {ad!r}")
    for p in (proje / ".claude" / "skills" / ad, proje / ".agents" / "skills" / ad):
        if not proje_ici(proje, p):
            raise RuntimeError(f"{p}: proje dışına gidiyor; silinmedi")
        sil_yol(p)


def dis_kur_bag(proje, kilit, ad, hedef):
    """Bağı kurar (program klasörüne hiçbir şey yazılmaz). ortak: .agents/skills/<ad> -> mutlak hedef, .claude/skills/<ad> -> göreli bağ;
    yalniz-claude: .claude/skills/<ad> -> mutlak hedef."""
    h, c = proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad
    for p in (h, c):
        if not proje_ici(proje, p):
            raise RuntimeError(f"{p}: proje dışına gidiyor")
    c.parent.mkdir(parents=True, exist_ok=True)
    if codex_var(kilit):
        h.parent.mkdir(parents=True, exist_ok=True)
        sil_yol(h)
        os.symlink(str(hedef), h)
        sil_yol(c)
        os.symlink(os.path.relpath(h, c.parent), c)
    else:
        sil_yol(h)
        sil_yol(c)
        os.symlink(str(hedef), c)
    if not (c / "SKILL.md").exists():
        raise RuntimeError(f"{ad}: bağ kuruldu ama {yol_goster(hedef)}/SKILL.md görünmüyor")


def dis_kur_donmus(proje, kilit, ad, kaynak):
    """Kaynağı (bağlar çözülerek) projeye GERÇEK klasör olarak bir kez kopyalar; içerik hiç değiştirilmez. Döner: kilit girişi."""
    codex = codex_var(kilit)
    h, c = proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad
    final = h if codex else c
    gercek = Path(os.path.realpath(kaynak))
    gecici = final.parent / f".{ad}.kurulum-tmp"
    for p in (h, c, gecici):
        if not proje_ici(proje, p):
            raise RuntimeError(f"{p}: proje dışına gidiyor")
    final.parent.mkdir(parents=True, exist_ok=True)
    sil_yol(gecici)
    try:
        shutil.copytree(gercek, gecici, symlinks=False,
                        ignore=shutil.ignore_patterns(".DS_Store", *sorted(DONDUR_ATLANAN_DIZIN)))
        if any(x.is_symlink() for x in gecici.rglob("*")):
            raise RuntimeError(f"{ad}: kopyada bağlantı kaldı; dondurma iptal")
        sil_yol(final)
        gecici.rename(final)
    finally:
        sil_yol(gecici)
    if codex:
        c.parent.mkdir(parents=True, exist_ok=True)
        sil_yol(c)
        os.symlink(os.path.relpath(final, c.parent), c)
    else:
        sil_yol(h)
    return {"ad": ad, "tur": "donmus", "hedef": str(kaynak), "tarih": date.today().isoformat(),
            "icerik_hash": klasor_hash(final), "dosya_sayisi": len(onemli_dosyalar(final))}


def dis_yerlestir(proje, kilit):
    """Her dış skill'in slotlarını güncel araç düzenine uydurur (--yenile ve düzen değişimi). Döner: mesajlar.
    Bağ: yalnız kendi bağlarını yeniden kurar (gerçek klasöre dokunmaz; hedef yoksa kurmaz). Donmuş: gerçek klasör TAŞINIR (içerik okunmaz/kopyalanmaz)."""
    mesaj = []
    codex = codex_var(kilit)
    for ad, g in sorted(dis_kayitlari(kilit).items()):
        h, c = proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad
        if g["tur"] == "program-bag":
            hedef = dis_bag_hedefi(g)
            if hedef is None:
                mesaj.append(f"{ad}: program kartı ya da skill_koku yok ({g.get('program')}); bağ yeniden kurulmadı")
                continue
            if not (hedef / "SKILL.md").is_file():
                mesaj.append(f"{ad}: hedef yok ({yol_goster(hedef)}); bağ yeniden kurulmadı (program kurulu mu?)")
                continue
            gercek = [p for p in (h, c) if p.exists() and not p.is_symlink() and (codex or p == c)]
            if gercek:
                mesaj.append(f"{ad}: {gercek[0].relative_to(proje)} gerçek klasör; dokunulmadı")
                continue
            if not codex and h.exists() and not h.is_symlink():
                mesaj.append(f"{ad}: .agents/skills/{ad} gerçek klasör; dokunulmadı")
                continue
            if str(hedef) != g["hedef"]:
                mesaj.append(f"{ad}: bağ karttaki yeni program yoluna alındı ({yol_goster(g['hedef'])} -> {yol_goster(hedef)})")
                g["hedef"] = str(hedef)
            dis_kur_bag(proje, kilit, ad, hedef)
            continue
        rel_h = os.path.relpath(h, c.parent)
        h_gercek = h.is_dir() and not h.is_symlink()
        c_gercek = c.is_dir() and not c.is_symlink()
        if codex:
            if not h_gercek and c_gercek:
                h.parent.mkdir(parents=True, exist_ok=True)
                sil_yol(h) if h.is_symlink() else None
                os.replace(c, h)
                h_gercek = True
            elif h_gercek and c_gercek:
                mesaj.append(f"{ad}: .agents/skills ve .claude/skills altında iki gerçek klasör var; dokunulmadı")
                continue
            if h_gercek:
                if not (c.is_symlink() and os.readlink(c) == rel_h):
                    sil_yol(c)
                    c.parent.mkdir(parents=True, exist_ok=True)
                    os.symlink(rel_h, c)
            else:
                mesaj.append(f"{ad}: donmuş klasör yok; --geri-al <yedek> ile geri getir ya da --kaldir {ad}")
        else:
            if not c_gercek and h_gercek:
                sil_yol(c)
                c.parent.mkdir(parents=True, exist_ok=True)
                os.replace(h, c)
                c_gercek = True
            elif h_gercek and c_gercek:
                mesaj.append(f"{ad}: .agents/skills ve .claude/skills altında iki gerçek klasör var; dokunulmadı")
                continue
            if c_gercek:
                if h.is_symlink():
                    sil_yol(h)
            else:
                mesaj.append(f"{ad}: donmuş klasör yok; --geri-al <yedek> ile geri getir ya da --kaldir {ad}")
    return mesaj


def dis_on_kontrol(proje, kilit, liste, lib_adlar, rapor: Rapor):
    """--program-skill / --dondur ön kontrolü (A3). Döner: kurulabilecek (HATA'sız) istekler; her isteğe kaynak, kart, tarama gibi alanlar eklenir."""
    codex = codex_var(kilit)
    kurulu_lib = {x.casefold() for x in kilit["skiller"]}
    lib_cf = {x.casefold() for x in lib_adlar}
    dis = dis_kayitlari(kilit)
    dis_cf = {k.casefold(): k for k in dis}
    kartlar = program_kartlari()
    gecerli = []
    for it in liste:
        ad, tur = it["ad"], it["tur"]
        ok = True
        if tur == "program-bag":
            if not dis_ad_gecerli(ad):
                rapor.ekle("HATA", "program-skill-ad", f"{ad!r}: geçersiz skill adı (ilk karakter harf ya da rakam olmalı; harf, rakam, . _ - "
                           "içerebilir; / olamaz; en çok 64 karakter; '.kurulum-tmp' ile bitemez)")
                continue
            kart = kartlar.get(it["program"])
            if kart is None:
                rapor.ekle("HATA", "program-bilinmiyor", f"{it['program']}: programlar.json'da böyle bir program yok (kartlar: {', '.join(sorted(kartlar)) or '-'})")
                continue
            koku = program_skill_koku(kart)
            if koku is None:
                ham = kart.get("skill_koku")
                rapor.ekle("HATA", "program-skillsiz", f"{it['program']}: " + ("skill_koku mutlak yol olmalı (~/ ya da /)" if isinstance(ham, str) and ham.strip()
                                                                               else "bu programın skili yok (kartta skill_koku boş ya da yok)"))
                continue
            if not koku.is_dir():
                boyut_ek = program_boyut_metni(it["program"])
                rapor.ekle("HATA", "program-kurulu-degil",
                           f"{it['program']}: skill klasörü bu bilgisayarda yok ({yol_goster(koku)}); program kurulu değil ya da taşınmış"
                           + (f" (kurulumu {boyut_ek} yer tutar; program kurulumu ayrı onay ister)" if boyut_ek else ""))
                continue
            if program_skill_ham_klasoru_mu(kart, ad):
                dogru = next(a for a, k in kart["skill_klasorleri"].items() if k == ad)
                rapor.ekle("HATA", "program-skill-ham-klasor", f"{it['program']}:{ad}: `{ad}` programın ham klasör adı, skill adı değil; "
                           f"doğru ad: --program-skill {it['program']}:{dogru}")
                continue
            hedef = Path(os.path.abspath(koku / program_skill_klasoru(kart, ad)))
            if not (hedef / "SKILL.md").is_file():
                adlar = _program_skilleri_adlari(koku, kart)
                rapor.ekle("HATA", "program-skill-yok", f"{it['program']}:{ad}: {yol_goster(hedef)} klasörü ya da içinde SKILL.md yok. Programdaki skiller: "
                           + (", ".join(adlar[:8]) + (f" …+{len(adlar) - 8}" if len(adlar) > 8 else "") if adlar else "-"))
                continue
            it.update(hedef=hedef, kart=kart)
            it["surum"], it["surum_turu"] = program_surumu(kart)
        else:
            if not dis_ad_gecerli(ad):
                rapor.ekle("HATA", "dondur-ad", f"{ad!r}: geçersiz klasör adı (ilk karakter harf ya da rakam olmalı; harf, rakam, . _ - içerebilir; "
                           "en çok 64 karakter; '.kurulum-tmp' ile bitemez)")
                continue
            gercek = Path(os.path.realpath(it["kaynak"]))
            it["gercek"] = gercek
            if not gercek.is_dir() or not (gercek / "SKILL.md").is_file():
                rapor.ekle("HATA", "dondur-kaynak-yok", f"{yol_goster(it['kaynak'])}: klasör ya da içinde SKILL.md yok")
                continue
            for pa, kart in sorted(kartlar.items()):
                koku = program_skill_koku(kart)
                if koku:
                    kr = Path(os.path.realpath(koku))
                    if gercek == kr or kr in gercek.parents:
                        rapor.ekle("HATA", "dondur-program-skili", f"{ad}: bu skill {pa} programıyla geliyor ({yol_goster(gercek)}); dondurma, "
                                   f"--program-skill {pa}:{program_klasor_skill_adi(kart, gercek.name)} kullan (kopya olmasın, program güncellenince kendiliğinden güncel kalsın)")
                        ok = False
                        break
            if not ok:
                continue
            if gercek in Path(os.path.realpath(proje)).parents:
                rapor.ekle("HATA", "dondur-kendisi", f"{ad}: kaynak projeyi kendi içinde barındırıyor; dondurulmaz (kopya kendi içine inerdi)")
                continue
            for rel in (".agents/skills", ".claude/skills", META):
                kr = Path(os.path.realpath(proje / rel))
                if gercek == kr or kr in gercek.parents:
                    rapor.ekle("HATA", "dondur-kendisi", f"{ad}: kaynak projenin kendi {rel} klasörünün içinde; dondurulmaz")
                    ok = False
                    break
            if not ok:
                continue
            t = dondur_tara(gercek)
            it["tarama"] = t
            if t["cok"]:
                rapor.ekle("HATA", "dondur-cok-buyuk", f"{ad}: {DONDUR_TAVAN_MB} MB ya da {DONDUR_TAVAN_DOSYA} dosya tavanı aşıldı; dondurulmaz "
                           "(proje deposuna konacak bir skill bu kadar büyük olmamalı)")
                continue
            if t["gizli"]:
                rapor.ekle("HATA", "dondur-gizli", f"{ad}: gizli değer taşıyabilecek dosya/klasör adı var: {', '.join(sorted(t['gizli'])[:5])}; dondurulmaz (dosya açılmadı)")
                ok = False
            if t["baglar"]:
                rapor.ekle("HATA", "dondur-dis-baglanti", f"{ad}: kaynağın içinde klasör bağı, klasör dışına giden ya da bozuk bağlantı var: "
                           f"{', '.join(sorted(t['baglar'])[:5])}; dondurulmaz")
                ok = False
            if t["ozel"]:
                rapor.ekle("HATA", "dondur-ozel-dosya", f"{ad}: normal dosya olmayan öğe var (FIFO/soket/aygıt): {', '.join(sorted(t['ozel'])[:5])}; dondurulmaz")
                ok = False
            if not ok:
                continue
        # ad çakışmaları (iki tür aynı adı taşıyamaz; büyük/küçük harf duyarsız: macOS dosya sistemi)
        cf = ad.casefold()
        cak = None
        if cf in lib_cf or cf in kurulu_lib:
            cak = "kütüphaneden kurulacak" if cf in lib_cf else "kütüphaneden kurulu"
            if tur == "donmus":
                rapor.ekle("HATA", "dondur-kutuphane-adi", f"{ad}: projede bu adla {cak} bir skill var; iki tür aynı adı taşıyamaz")
                continue
        elif cf in dis_cf:
            anahtar, g = dis_cf[cf], dis[dis_cf[cf]]
            if anahtar != ad:
                cak = f"{anahtar} adıyla kayıtlı; harf boyutu farkı"
            elif g["tur"] != tur:
                cak = "program bağı olarak kayıtlı" if g["tur"] == "program-bag" else "donmuş skill olarak kayıtlı"
            elif tur == "program-bag":
                if g["hedef"] != str(it["hedef"]):
                    rapor.ekle("HATA", "bag-farkli", f"{ad}: zaten {yol_goster(g['hedef'])} yoluna bağlı; önce --kaldir {ad}")
                    continue
                it["mevcut"] = True
                sor = dis_sorunlar(proje, kilit, ad, g)
                it["var"] = not sor
                if any(k == "gercek-klasor" for k, _ in sor):
                    rapor.ekle("HATA", "bag-gercek-klasor", f"{ad}: bağ yerine elle konmuş gerçek klasör var; üzerine bağ kurulmaz (silinirdi). "
                               f"Klasörü sen taşı ya da --kaldir {ad} ile temizle")
                    continue
            else:
                it["mevcut"] = it["var"] = True
                rapor.ekle("BİLGİ", "dondurma-var", f"{ad}: zaten donmuş; yeniden kopyalanmaz (yeniden dondurmak için önce --kaldir {ad})")
        if cak:
            rapor.ekle("HATA", "dis-ad-cakismasi", f"{ad}: projede başka bir skill bu adı kullanıyor ({cak}); iki tür aynı adı taşıyamaz")
            continue
        if cf not in dis_cf and cf not in kurulu_lib:
            for yer in (proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad):
                if yer.exists() or yer.is_symlink():
                    rapor.ekle("HATA", "projede-kendi-skillin", f"{yer.relative_to(proje)} zaten var ve kütüphaneden gelmemiş; üzerine yazılmaz "
                               "(--zorla ile yedeklenip değiştirilir)")
        if tur == "donmus" and not it.get("mevcut"):
            t = it["tarama"]
            kb = max(1, round(t["bayt"] / 1024)) if t["bayt"] else 0
            rapor.ekle("BİLGİ", "dondurma-guncellenmez", f"{ad}: donmuş kopya projenin kendi skilidir; kütüphane onu güncellemez, düzeltmez, kaynağı değişse de izlemez.")
            rapor.ekle("BİLGİ", "dondurma-kopya", f"{ad}: {yol_goster(it['kaynak'])} içeriği gerçek klasör olarak kopyalanacak ({t['dosya']} dosya, {kb} KB); "
                       "dosya bağlantıları gerçek dosyaya çevrilir; içerik taranmadı (yalnız dosya adları): proje deposuna koymadan önce dosyaları gözden geçir.")
            if t["atlanan"]:
                rapor.ekle("BİLGİ", "dondurma-atlanan", f"{ad}: kopyalanmayacak klasörler: {', '.join(sorted(t['atlanan'])[:5])}")
            if t["bayt"] > DONDUR_BUYUK_MB * 1024 * 1024:
                rapor.ekle("UYARI", "dondur-buyuk", f"{ad}: {t['bayt'] // (1024 * 1024)} MB; proje deposunu şişirir, gerçekten gerekli mi?")
            try:
                fad = frontmatter_adi(it["gercek"] / "SKILL.md")
            except (UnicodeDecodeError, OSError):
                fad = None
            if fad and fad != ad:
                rapor.ekle("UYARI", "dondur-ad-farkli", f"{ad}: SKILL.md içindeki ad ({fad}) klasör adından farklı; kopya olduğu gibi alınır, değiştirilmez")
            it["kb"] = kb
        gecerli.append(it)
    baglar = [it for it in gecerli if it["tur"] == "program-bag"]
    if baglar:
        rapor.ekle("BİLGİ", "bag-makineye-ozel", "Bağlar bu bilgisayardaki program klasörünü gösterir (mutlak yol). Başka bilgisayarda ve Windows'ta çalışmaz. "
                   "Bağları ve .claude/skills ile .agents/skills altındaki bağlı klasörleri paylaşılan bir git deposuna koyma (git'e girmesin: .gitignore'a ekle) "
                   "ya da yalnız bu Mac'te kullan.")
        yeni = [it for it in baglar if not it.get("var")]
        for program in sorted({it["program"] for it in yeni}):
            ads = sorted(it["ad"] for it in yeni if it["program"] == program)
            ornek = next(it for it in yeni if it["program"] == program)
            rapor.ekle("BİLGİ", "bag-programla-guncel",
                       f"{program}: {len(ads)} bağ ({', '.join(ads[:6])}{f' …+{len(ads) - 6}' if len(ads) > 6 else ''}); program güncellenince kendiliğinden "
                       f"güncel kalır, kütüphane kopyalamaz; bağlandığı sürüm {surum_metni(ornek['surum'], ornek['surum_turu'])} (karttaki kayıt; program "
                       f"çalıştırılmadı); program bir skili kaldırırsa bağ kırılır (program-denetim.py --oncesi {program} önceden söyler).")
        var = sorted(it["ad"] for it in baglar if it.get("var"))
        if var:
            rapor.ekle("BİLGİ", "bag-var", f"{', '.join(var)}: zaten bağlı; değişiklik yok")
        izlenen = bag_git_izlenenler(proje, [it["ad"] for it in yeni], codex)
        if izlenen:
            rapor.ekle("UYARI", "bag-git-izlenir", f"git'e girecek (mutlak yollu bağ başka bilgisayarda/Windows'ta bozulur): {', '.join(izlenen[:6])}; "
                       ".gitignore'a ekle ya da yalnız bu Mac'te kullan")
    return gecerli


# ================================================================== fihrist, kit ve proje raporu (plan 4. adım)
class KaynakErisimHatasi(RuntimeError):
    """Kaynak repoya erişilemedi (internet yok, 404, yetki veya klon hatası)."""


class KaynakYolYokHatasi(RuntimeError):
    """Fihristteki skil yolu kaynak repoda artık yok."""


def kaynaklar_haritasi():
    """kaynaklar.json -> {repo.lower(): kayıt}. Dosya yoksa ya da bozuksa {}."""
    try:
        d = json_oku(KAYNAKLAR_DOSYA, {}) or {}
    except (OSError, ValueError):
        return {}
    repolar = d.get("repolar") if isinstance(d, dict) else None
    if not isinstance(repolar, list):
        return {}
    out = {}
    for k in repolar:
        if isinstance(k, dict) and isinstance(k.get("repo"), str):
            out.setdefault(k["repo"].lower(), k)
    return out


def kaynak_kaydi(repo):
    return kaynaklar_haritasi().get(repo_guncel(repo or "").lower())


def fihrist_dosya_yolu(repo):
    return FIHRIST_KLASOR / (repo.replace("/", "__") + ".json")


def fihrist_oku(repo):
    """fihrist/<owner>__<ad>.json dosyasını okur; yoksa ya da bozuksa None."""
    p = fihrist_dosya_yolu(repo)
    if not p.is_file():
        # büyük/küçük harf duyarsız eşleme
        hedef = p.name.lower()
        if FIHRIST_KLASOR.is_dir():
            p = next((f for f in FIHRIST_KLASOR.glob("*.json") if f.name.lower() == hedef), None)
        else:
            p = None
    if not p or not p.is_file():
        return None
    try:
        d = json_oku(p)
        return d if isinstance(d, dict) and isinstance(d.get("skiller"), list) else None
    except (OSError, ValueError):
        return None


def fihrist_tumu():
    """FIHRIST_KLASOR altındaki tüm geçerli fihrist dosyaları."""
    if not FIHRIST_KLASOR.is_dir():
        return []
    out = []
    for f in sorted(FIHRIST_KLASOR.glob("*.json")):
        try:
            d = json_oku(f)
            if isinstance(d, dict) and isinstance(d.get("repo"), str) and isinstance(d.get("skiller"), list):
                out.append(d)
        except (OSError, ValueError):
            continue
    return out


def kitler_listesi():
    """kitler.json -> kitler listesi; yoksa/bozuksa []."""
    try:
        d = json_oku(KITLER_DOSYA, {}) or {}
    except (OSError, ValueError):
        return []
    liste = d.get("kitler") if isinstance(d, dict) else None
    return [k for k in liste if isinstance(k, dict) and isinstance(k.get("repo"), str)] if isinstance(liste, list) else []


def kit_bul(anahtar):
    """kitler.json içinde repo tam eşleşmesi (case-insensitive) ya da benzersiz repo son adı."""
    if not anahtar:
        return None
    liste = kitler_listesi()
    a = anahtar.strip().lower()
    for k in liste:
        if k["repo"].lower() == a:
            return k
    son = [k for k in liste if k["repo"].split("/")[-1].lower() == a]
    return son[0] if len(son) == 1 else None


def kit_kayitlari(kilit):
    """kilit['kitler'] içindeki geçerli kit kayıtları: {repo: kayıt}."""
    ham = kilit.get("kitler") if isinstance(kilit, dict) else None
    if not isinstance(ham, dict):
        return {}
    return {r: g for r, g in ham.items() if isinstance(r, str) and isinstance(g, dict) and isinstance(g.get("commit"), str)}


def proje_baslamis_mi(proje):
    """Proje klasörü başlamış mı? (.skill-kutuphanesi, .git ve .DS_Store dışında herhangi bir dosya/klasör varsa True)."""
    if not proje or not proje.is_dir():
        return False
    yoksay = {META, ".git", ".DS_Store"}
    return any(p.name not in yoksay for p in proje.iterdir())


def proje_paket_surumleri(proje):
    """package.json bağımlılık sürümleri: {paket: surum_str}."""
    out = {}
    if not proje:
        return out
    pj = proje / "package.json"
    if pj.is_file():
        try:
            d = json.loads(pj.read_text(encoding="utf-8"))
            for bol in ("dependencies", "devDependencies"):
                if isinstance(d.get(bol), dict):
                    for k, v in d[bol].items():
                        if isinstance(v, str):
                            out[k] = v
        except (OSError, ValueError):
            pass
    return out


def kaynak_bakimsiz_mi(kayit, bugun=None):
    """Kaynak 12 aydan (365 gün) uzun süredir değişmemiş ya da bakim=='bakimsiz' mı?"""
    if not isinstance(kayit, dict):
        return False
    if kayit.get("bakim") == "bakimsiz":
        return True
    bugun = bugun or date.today()
    for t in (kayit.get("son_degisiklik"), (kayit.get("son_kontrol") or {}).get("son_commit_tarihi")):
        if isinstance(t, str) and len(t) >= 10:
            try:
                if (bugun - date.fromisoformat(t[:10])).days > BAKIMSIZ_GUN:
                    return True
            except ValueError:
                pass
    return False


def boyut_bicim(bayt):
    if bayt is None:
        return "hesaplanamadı"
    if bayt < 1024:
        return f"{bayt} B"
    if bayt < 1024 * 1024:
        return f"{bayt / 1024:.1f} KB"
    return f"{bayt / (1024 * 1024):.2f} MB"


def kaynak_boyut_metni(kayit, dev_dahil=False):
    """kaynaklar.json -> boyut alanından tahmini kurulum boyutu metni."""
    if not isinstance(kayit, dict):
        return ""
    b = kayit.get("boyut")
    if not isinstance(b, dict):
        return ""
    mb = b.get("kurulum_mb_devdahil") if (dev_dahil and b.get("kurulum_mb_devdahil") is not None) else b.get("kurulum_mb")
    hesp = [x for x in (b.get("hesaplanamayan") or []) if isinstance(x, str) and x.strip()]
    parca = []
    if mb is not None:
        parca.append(f"~{mb} MB (tahmini)")
    elif b.get("kutuphane_kb") is not None:
        parca.append(f"~{b['kutuphane_kb']} KB")
    if hesp:
        parca.append("artı hesaplanamayan: " + ", ".join(hesp[:3]))
    return "; ".join(parca)


def program_boyut_metni(program_adi):
    """Program kurulu değilken kaynaklar.json'dan tahmini kurulum boyutunu döner."""
    kart = program_karti(program_adi)
    if not kart:
        return ""
    kay = kaynak_kaydi(kart.get("repo"))
    if not kay:
        for k in kaynaklar_haritasi().values():
            if k.get("program") == program_adi:
                kay = k
                break
    return kaynak_boyut_metni(kay, dev_dahil=True)


def token_tahmini(bayt):
    """Model hafızası yükü sayısal hesabı (plan bölüm 18): bayt / 4 (~4 bayt/token)."""
    return max(1, round(bayt / 4)) if bayt and bayt > 0 else 0


def kit_korunan_mi(rel):
    rel = rel.strip("/")
    return rel in KIT_KORUNAN_DOSYALAR or any(rel.startswith(p) for p in KIT_KORUNAN_ONEKLER) or rel.startswith(META + "/")


def guvenlik_tara(klasor):
    """Geçici klasördeki dosyaları güvenlik, gizli dosya, symlink, medya ve genel klasör yazımı açısından tarar (salt okur)."""
    klasor = Path(klasor)
    r = {"betikler": [], "ag_calistir": [], "veri_gonder": [], "talimat_enjeksiyon": [],
         "genel_yazma": [], "gizli_dosyalar": [], "symlinkler": [], "medya_buyuk": [], "ucret_ipucu": [], "claude_ozel": False}
    for yol, dizinler, dosyalar in os.walk(klasor, followlinks=False):
        g = os.path.relpath(yol, klasor)
        rel_fn = lambda n, g=g: n if g == "." else f"{g}/{n}"  # noqa: E731
        for d in list(dizinler):
            if d == ".git":
                dizinler.remove(d)
                continue
            dp = Path(yol) / d
            if dp.is_symlink():
                r["symlinkler"].append(rel_fn(d).replace(os.sep, "/") + "/")
                dizinler.remove(d)
                continue
            if d.casefold() in DONDUR_GIZLI_DIZIN:
                r["gizli_dosyalar"].append(rel_fn(d) + "/")
                dizinler.remove(d)
            elif d in DONDUR_ATLANAN_DIZIN:
                dizinler.remove(d)
        for f in sorted(dosyalar):
            if f == ".DS_Store":
                continue
            p = Path(yol) / f
            rel = rel_fn(f).replace(os.sep, "/")
            if p.is_symlink():
                r["symlinkler"].append(rel)
                continue
            if gizli_ad_mi(f):
                r["gizli_dosyalar"].append(rel)
                continue
            try:
                st = p.stat()
            except OSError:
                continue
            if medya_mi(rel) and st.st_size > MEDYA_ISTISNA_BAYT:
                r["medya_buyuk"].append((rel, st.st_size))
                continue
            uz = p.suffix.lower()
            betik = uz in (".sh", ".bash", ".zsh", ".py", ".js", ".mjs", ".cjs", ".ts", ".ps1", ".cmd", ".bat")
            if st.st_size > 512 * 1024:
                if betik:
                    r["betikler"].append(rel)
                continue
            try:
                ham = p.read_bytes()
            except OSError:
                continue
            if b"\0" in ham:
                continue
            if not betik and uz == "" and ham.startswith(b"#!"):
                betik = True
            if betik:
                r["betikler"].append(rel)
            metin = ham.decode("utf-8", errors="replace")
            for no, satir in enumerate(metin.splitlines(), 1):
                if GUVENLIK_ENJEKSIYON.search(satir):
                    r["talimat_enjeksiyon"].append((rel, no, satir.strip()[:100]))
                if GUVENLIK_AG_CALISTIR.search(satir):
                    r["ag_calistir"].append((rel, no, satir.strip()[:100]))
                if GUVENLIK_VERI_GONDER.search(satir):
                    r["veri_gonder"].append((rel, no, satir.strip()[:100]))
                if GUVENLIK_GENEL_YAZ.search(satir):
                    r["genel_yazma"].append((rel, no, satir.strip()[:100]))
                if UCRET_IPUCU.search(satir):
                    r["ucret_ipucu"].append((rel, no, satir.strip()[:80]))
                if CLAUDE_OZEL_IPUCU.search(satir):
                    r["claude_ozel"] = True
    return r


_GIT_SUNUCU_ERISIM_HATASI = re.compile(
    r"(?:could not resolve host(?:name)?|unable to access\b.*?(?:could not resolve|failed to connect|couldn't connect|"
    r"connection refused|network is unreachable|no route to host|connection reset|recv failure|ssl_connect)|"
    r"failed to connect to\b|couldn't connect to server|connection refused|network is unreachable|no route to host|"
    r"temporary failure in name resolution|name or service not known|nodename nor servname provided|"
    r"no address associated with hostname|erişilemiyor:\s*failed to connect)",
    re.I | re.S,
)
_GIT_ZAMAN_ASIMI_HATASI = re.compile(
    r"(?:operation timed out|connection timed out|timed out after|zaman aşımı)",
    re.I,
)


def _git_hata_iletisi(repo, adim, zaman_asimi, exc=None, stderr=""):
    """Git hata iletisini zaman aşımı, erişilemeyen sunucu (internet gerekli) ve diğer git hatası olarak ayırır."""
    metin = (stderr or str(exc or "")).strip()
    detay = metin[-200:]
    if isinstance(exc, subprocess.TimeoutExpired) or _GIT_ZAMAN_ASIMI_HATASI.search(metin):
        return f"{repo}: kaynak indirme zaman aşımına uğradı ({zaman_asimi} sn sınırı aşıldı; {adim})" + (f": {detay}" if detay else "")
    if _GIT_SUNUCU_ERISIM_HATASI.search(metin):
        return f"{repo}: sunucuya erişilemedi (internet gerekli): {detay}"
    return f"{repo}: git hatası ({adim}): {detay or 'işlem başarısız'}"


def _git_calistir(komut, repo, adim, zaman_asimi, env):
    try:
        res = subprocess.run(komut, capture_output=True, text=True, timeout=zaman_asimi, env=env, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired as e:
        stderr = (e.stderr.decode("utf-8", "replace") if isinstance(e.stderr, bytes) else (e.stderr or "")).strip()
        raise KaynakErisimHatasi(_git_hata_iletisi(repo, adim, zaman_asimi, exc=e, stderr=stderr)) from e
    except (OSError, subprocess.SubprocessError) as e:
        raise KaynakErisimHatasi(_git_hata_iletisi(repo, adim, zaman_asimi, exc=e)) from e
    if res.returncode != 0:
        raise KaynakErisimHatasi(_git_hata_iletisi(repo, adim, zaman_asimi, stderr=res.stderr))
    return res


def _fihrist_referans_adaylari(skil_klasoru, alt_yol, repo):
    """İndirilen fihrist skilinin SKILL.md (ve yardımcı dosyalarının) başvurduğu kardeş/kök yolları mevcut yol taramasıyla çıkarır."""
    skil_klasoru = Path(skil_klasoru)
    if not skil_klasoru.is_dir() or skil_klasoru.is_symlink():
        return []
    adaylar = []
    ust_dizin = posixpath.dirname(alt_yol) if alt_yol else ""
    ek_kok = _eklenti_koku_yolu(alt_yol)

    def _ekle(p):
        if not isinstance(p, str):
            return
        temiz = posixpath.normpath(p.strip("/")) if p.strip("/") else ""
        if not goreli_proje_yolu_gecerli(temiz):
            return
        if alt_yol and (temiz == alt_yol or temiz.startswith(alt_yol + "/")):
            return
        if temiz not in adaylar:
            adaylar.append(temiz)

    for kardes_ad in symlink_taslaklari(skil_klasoru).values():
        if alt_yol:
            _ekle(posixpath.join(alt_yol, "..", kardes_ad))

    kendi_ad = Path(alt_yol).name if alt_yol else repo.split("/")[-1]
    for b in yol_taramasi(skil_klasoru, {kendi_ad}):
        tur = b.get("tur")
        hedef = b.get("hedef")
        kalan = b.get("kalan") or ""
        ham = b.get("ham") or ""
        dosya = b.get("dosya") or "SKILL.md"
        dosya_dizin = posixpath.dirname(posixpath.join(alt_yol, dosya)) if alt_yol else posixpath.dirname(dosya)
        if tur in ("kardes-goreli", "ortak-dizin"):
            if ham.startswith("../"):
                _ekle(posixpath.join(dosya_dizin, ham))
            if hedef:
                if kalan:
                    _ekle(posixpath.join(ust_dizin, hedef, kalan))
                _ekle(posixpath.join(ust_dizin, hedef))
        elif tur == "genel-baska" and hedef:
            if kalan:
                _ekle(posixpath.join(ust_dizin, hedef, kalan))
            _ekle(posixpath.join(ust_dizin, hedef))
        elif tur == "skil-disi-yol":
            m_sd = re.match(r"^(?:\$\{CLAUDE_SKILL_DIR\}|\$CLAUDE_SKILL_DIR)/?(.*)$", ham)
            if m_sd and m_sd.group(1):
                _ekle(posixpath.join(alt_yol, m_sd.group(1)))
            if hedef:
                if kalan:
                    _ekle(posixpath.join(ust_dizin, hedef, kalan))
                _ekle(posixpath.join(ust_dizin, hedef))
        elif tur == "eklenti-kok-yol" and kalan:
            _ekle(kalan)
            if ek_kok:
                _ekle(posixpath.join(ek_kok, kalan))
        elif tur == "eklenti-kardes" and hedef:
            tabanlar = [posixpath.join(ek_kok, "skills"), ust_dizin, "skills"] if ek_kok else [ust_dizin, "skills"]
            for taban in tabanlar:
                if kalan:
                    _ekle(posixpath.join(taban, hedef, kalan))
                _ekle(posixpath.join(taban, hedef))

    sm = next((p for p in skil_klasoru.iterdir() if p.is_file() and not p.is_symlink() and p.name.lower() == "skill.md"), None)
    if sm:
        try:
            metin = sm.read_text(encoding="utf-8", errors="replace")
        except OSError:
            metin = ""
        for hedef in re.findall(r"\]\(([^)\s]+)\)", metin):
            if re.match(r"^(?:https?:|#|mailto:|<|\$|\{)", hedef) or "*" in hedef:
                continue
            yol_h = hedef.split("#")[0].split("?")[0].strip()
            if yol_h:
                _ekle(posixpath.join(alt_yol, yol_h) if alt_yol else yol_h.lstrip("./"))
        for tok in _ATIF_PARCA.findall(metin):
            tok_temiz = _yol_kes(tok).strip("/")
            if not tok_temiz or tok_temiz.startswith(("http", "www.")):
                continue
            if tok_temiz.startswith("../") and alt_yol:
                _ekle(posixpath.join(alt_yol, tok_temiz))
            elif "/" in tok_temiz and not tok_temiz.startswith("."):
                ilk = tok_temiz.split("/", 1)[0]
                if not alt_yol or not (skil_klasoru / ilk).exists():
                    _ekle(tok_temiz)
    return adaylar


def _fihrist_ek_yollar(klon_dir, skil_klasoru, alt_yol, repo, mevcut_sparse, env):
    """SKILL.md'nin başvurduğu kardeş/kök yollardan repo HEAD ağacında gerçekten bulunanları döner."""
    adaylar = [p for p in _fihrist_referans_adaylari(skil_klasoru, alt_yol, repo) if p not in mevcut_sparse]
    if not adaylar:
        return []
    try:
        r = subprocess.run(["git", "-C", str(klon_dir), "ls-tree", "-r", "-t", "--name-only", "HEAD"],
                           capture_output=True, text=True, timeout=30, env=env, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError):
        return []
    if r.returncode != 0:
        return []
    agac_yollari = set(r.stdout.splitlines())
    return [p for p in adaylar if p in agac_yollari]


def kaynak_indir(repo, hedef_dir, alt_yol=None, zaman_asimi=None):
    """Kaynağı geçici klasöre (hedef_dir) indirir. Döner: (commit_sha, kaynak_klasor).
    Fihrist skili (alt_yol verilmişse): seyrek kısmi klon (--depth 1 --filter=blob:none --sparse --no-checkout +
    sparse-checkout set --no-cone <skil yolu> + kardeş/kök yollar + checkout; zaman aşımı 300 sn).
    Kit (alt_yol None): kısmi klon (--depth 1 --filter=blob:none; zaman aşımı 600 sn). LFS kapalıdır.
    KAYNAK_URL_CEVIRICI ayarlıysa (testlerde yerel git deposu / klasör) oradan alır; ağ kullanmaz.
    Hata olursa hedef_dir temizlenir."""
    hedef_dir = Path(hedef_dir)
    klon_dir = hedef_dir / "repo"
    if zaman_asimi is None:
        zaman_asimi = FIHRIST_KLON_ZAMAN_ASIMI if alt_yol is not None else KIT_KLON_ZAMAN_ASIMI
    try:
        if alt_yol and not goreli_proje_yolu_gecerli(alt_yol):
            raise KaynakYolYokHatasi(f"{repo}: geçersiz skil yolu ({alt_yol!r}); geçici klon dışına çıkamaz")
        url = KAYNAK_URL_CEVIRICI(repo) if callable(KAYNAK_URL_CEVIRICI) else f"https://github.com/{repo}.git"
        url_str = str(url)
        yerel_yol = Path(url_str) if not url_str.startswith(("http://", "https://", "git@", "file://")) else None
        if yerel_yol is not None and yerel_yol.is_dir() and not (yerel_yol / ".git").exists():
            # Düz yerel dizin (test kolaylığı)
            shutil.copytree(yerel_yol, klon_dir, ignore=shutil.ignore_patterns(".git", ".DS_Store"))
            agac, _ = yerel_agac(klon_dir)
            commit = yerel_commit(agac)
        else:
            klon_url = yerel_yol.resolve().as_uri() if (yerel_yol is not None and yerel_yol.exists()) else url_str
            env = {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_LFS_SKIP_SMUDGE": "1"}
            lfs_ayar = ["-c", "filter.lfs.smudge=", "-c", "filter.lfs.required=false"]
            yerel_filter = []
            if klon_url.startswith("file://"):
                up = "git -c uploadpack.allowFilter=true -c uploadpack.allowAnySHA1InWant=true upload-pack"
                yerel_filter = ["-c", f"remote.origin.uploadpack={up}", f"--upload-pack={up}"]
            if alt_yol is not None:
                komut = ["git", "clone", "-q", "--depth", "1", "--filter=blob:none", "--sparse", "--no-checkout",
                         *lfs_ayar, *yerel_filter, klon_url, str(klon_dir)]
                _git_calistir(komut, repo, "git clone", zaman_asimi, env)
                sparse_yollar = [alt_yol] if alt_yol else ["/SKILL.md", "/skill.md"]
                kay = kaynak_kaydi(repo)
                for kd in (kay.get("kok_dosyalari") or []) if isinstance(kay, dict) else ():
                    if isinstance(kd, str) and goreli_proje_yolu_gecerli(kd.strip("/")):
                        temiz_kd = kd.strip("/")
                        if temiz_kd not in sparse_yollar:
                            sparse_yollar.append(temiz_kd)
                _git_calistir(["git", "-C", str(klon_dir), "sparse-checkout", "set", "--no-cone", *sparse_yollar],
                              repo, "git sparse-checkout", zaman_asimi, env)
                _git_calistir(["git", "-C", str(klon_dir), "checkout", "-q"],
                              repo, "git checkout", zaman_asimi, env)
                skil_aday = (klon_dir / alt_yol) if alt_yol else klon_dir
                ek_yollar = _fihrist_ek_yollar(klon_dir, skil_aday, alt_yol, repo, sparse_yollar, env)
                if ek_yollar:
                    tum_sparse = list(dict.fromkeys([*sparse_yollar, *ek_yollar]))
                    _git_calistir(["git", "-C", str(klon_dir), "sparse-checkout", "set", "--no-cone", *tum_sparse],
                                  repo, "git sparse-checkout", zaman_asimi, env)
                    _git_calistir(["git", "-C", str(klon_dir), "checkout", "-q"],
                                  repo, "git checkout", zaman_asimi, env)
            else:
                komut = ["git", "clone", "-q", "--depth", "1", "--filter=blob:none",
                         *lfs_ayar, *yerel_filter, klon_url, str(klon_dir)]
                _git_calistir(komut, repo, "git clone", zaman_asimi, env)
            rev = _git_calistir(["git", "-C", str(klon_dir), "rev-parse", "HEAD"],
                                repo, "git rev-parse", min(30, max(1, zaman_asimi)), env)
            commit = rev.stdout.strip()
            if not commit:
                raise KaynakErisimHatasi(f"{repo}: commit okunamadı")
        if alt_yol is None:
            return commit, klon_dir
        if alt_yol:
            skil_klasoru = klon_dir / alt_yol
            if skil_klasoru.is_symlink():
                raise KaynakYolYokHatasi(f"{repo}: '{alt_yol}' symlink; güvenlik nedeniyle reddedildi")
            klon_kok = os.path.realpath(klon_dir)
            hedef_gercek = os.path.realpath(skil_klasoru)
            if hedef_gercek != klon_kok and not hedef_gercek.startswith(klon_kok + os.sep):
                raise KaynakYolYokHatasi(f"{repo}: '{alt_yol}' yolu geçici klon dışına çıkıyor; reddedildi")
        else:
            skil_klasoru = klon_dir
        if not skil_klasoru.is_dir():
            raise KaynakYolYokHatasi(f"{repo}: '{alt_yol}' yolu kaynakta artık yok (kaldırılmış olabilir)")
        sm = next((p for p in skil_klasoru.iterdir() if p.is_file() and not p.is_symlink() and p.name.lower() == "skill.md"), None)
        if not sm:
            raise KaynakYolYokHatasi(f"{repo}: '{alt_yol}' içinde SKILL.md yok")
        if sm.name != "SKILL.md":
            sm.rename(skil_klasoru / "SKILL.md")
        return commit, skil_klasoru
    except Exception:
        if hedef_dir.exists() and hedef_dir != KOK and KOK not in hedef_dir.parents:
            shutil.rmtree(hedef_dir, ignore_errors=True)
        raise


def gecici_skil_incele(klasor, repo, yol, commit, ad, onceki_inceleme=None):
    """Fihristten geçici klasöre alınan tek bir skili inceler (plan 5.5, 6.6, 15.2)."""
    klasor = Path(klasor)
    sm = klasor / "SKILL.md"
    metin = metin_oku(sm)
    fm = frontmatter(metin)
    yapisal = frontmatter_teshis(metin)
    guv = guvenlik_tara(klasor)
    s_sahte = {"id": f"{ad}@{repo.split('/')[-1]}", "ad": fm.get("name") or ad, "klasor_adi": ad,
               "repo": repo, "kaynak_yol": yol, "yol": str(klasor), "klasor_hash": None}
    yol_d = yol_degerlendir(s_sahte, [], kurulacak_idler=set())
    yol_bulgulari = skill_yol_taramasi(s_sahte, [])
    dosyalar = [p.relative_to(klasor).as_posix() for p in onemli_dosyalar(klasor) if not p.is_symlink()]
    toplam_bayt = sum((klasor / d).stat().st_size for d in dosyalar if (klasor / d).is_file())
    sm_bayt = sm.stat().st_size
    onceden = bool(isinstance(onceki_inceleme, dict) and onceki_inceleme.get("commit") == commit)
    uyarilar = []
    if guv["symlinkler"]:
        uyarilar.append(("HATA", "fihrist-symlink", f"{ad}: symlink içeriyor ({', '.join(guv['symlinkler'][:4])}); dış dosya kopyalama riski nedeniyle kurulmaz"))
    if guv["gizli_dosyalar"]:
        uyarilar.append(("HATA", "fihrist-gizli", f"{ad}: gizli dosya/klasör içeriyor ({', '.join(guv['gizli_dosyalar'][:4])}); kurulmaz"))
    if guv["ag_calistir"]:
        ornek = f"{guv['ag_calistir'][0][0]}:{guv['ag_calistir'][0][1]}"
        uyarilar.append(("UYARI", "guvenlik-ag", f"{ad}: ağdan indirip çalıştıran komut var ({ornek}); otomatik çalıştırılmaz"))
    if guv["veri_gonder"]:
        ornek = f"{guv['veri_gonder'][0][0]}:{guv['veri_gonder'][0][1]}"
        uyarilar.append(("UYARI", "guvenlik-veri", f"{ad}: hassas dosya ile ağ komutu aynı satırda ({ornek}); incele"))
    if guv["talimat_enjeksiyon"]:
        ornek = f"{guv['talimat_enjeksiyon'][0][0]}:{guv['talimat_enjeksiyon'][0][1]}"
        uyarilar.append(("UYARI", "guvenlik-talimat", f"{ad}: onay atlama/yönlendirme metni var ({ornek}); veri olarak işlendi, uygulanmadı"))
    if guv["genel_yazma"]:
        ornek = f"{guv['genel_yazma'][0][0]}:{guv['genel_yazma'][0][1]}"
        uyarilar.append(("UYARI", "genele-yazabilir", f"{ad}: genel klasöre yazan satır var ({ornek}); kütüphane kuralı genel klasöre yazmayı yasaklar"))
    for sv, kod, govde in yol_d.get("satirlar", []):
        if kod == "genele-yazabilir" and guv["genel_yazma"]:
            continue
        uyarilar.append((sv, kod, f"{ad}: {govde}"))
    if guv["medya_buyuk"]:
        uyarilar.append(("BİLGİ", "medya-dosya", f"{ad}: >200 KB medya/ikili dosya var ({len(guv['medya_buyuk'])} dosya)"))
    if guv["claude_ozel"]:
        uyarilar.append(("UYARI", "codex-uyum", f"{ad}: Claude'a özgü araç/eklenti referansı içeriyor; Codex'te sınırlı olabilir"))
    if guv["ucret_ipucu"]:
        uyarilar.append(("BİLGİ", "ucret-ipucu", f"{ad}: ücretli API anahtarı/plan ifadesi içeriyor ({guv['ucret_ipucu'][0][0]}:{guv['ucret_ipucu'][0][1]})"))
    if yapisal:
        uyarilar.append(("BİLGİ", "yapi", f"{ad}: frontmatter notu ({'; '.join(yapisal)}) -> kurulan kopyada onarılır"))
    sonuc = "uyarili" if any(s in ("HATA", "UYARI") for s, _, _ in uyarilar) else "temiz"
    ozet_not = "; ".join(f"{k}" for s, k, _ in uyarilar if s in ("HATA", "UYARI")) or "temiz"
    return {"ad": ad, "fm": fm, "yapisal": yapisal, "guvenlik": guv, "yol_bulgulari": yol_bulgulari,
            "dosyalar": dosyalar, "toplam_bayt": toplam_bayt, "skill_md_bayt": sm_bayt,
            "onceden_incelendi": onceden, "sonuc": sonuc, "not": ozet_not, "satirlar": uyarilar}


def fihrist_inceleme_commit(yollar):
    """Fihrist inceleme notu yazılınca (yalnız master dalında ve KOK altındaysa) kütüphane çalışma ağacını temiz tutmak için
    yalnızca bu fihrist dosyalarını yerelde commit eder; push asla yapılmaz."""
    try:
        rel_yollar = []
        kok_r = KOK.resolve()
        for p in yollar:
            pr = Path(p).resolve()
            if kok_r in pr.parents:
                rel_yollar.append(str(pr.relative_to(kok_r)))
        if not rel_yollar or not (KOK / ".git").exists() or guncelleme_suruyor():
            return
        g = lambda *a: subprocess.run(["git", *a], cwd=KOK, capture_output=True, text=True)  # noqa: E731
        if g("branch", "--show-current").stdout.strip() == "master":
            if g("commit", "-q", "-m", "Fihrist inceleme notu kaydedildi (skill-ekle.py)", "--", *sorted(set(rel_yollar))).returncode == 0:
                print("  (kütüphanede yalnızca fihrist inceleme notu commit edildi; push yapılmadı)")
    except Exception:  # noqa: BLE001
        pass


def fihrist_inceleme_kaydet(repo, yol, commit, inceleme):
    """Plan 5.5: Bir kez incelenen fihrist skilinin sonucunu fihrist dosyasına yazar; aynı sürüm tekrar incelenmez."""
    if not FIHRIST_INCELEME_YAZ:
        return False
    p = fihrist_dosya_yolu(repo)
    if not p.is_file():
        return False
    try:
        d = json_oku(p)
        if not isinstance(d, dict) or not isinstance(d.get("skiller"), list):
            return False
        degisti = False
        for x in d["skiller"]:
            if isinstance(x, dict) and x.get("yol") == yol:
                eski = x.get("inceleme")
                yeni = {"commit": commit, "tarih": date.today().isoformat(), "sonuc": inceleme["sonuc"]}
                if inceleme.get("not") and inceleme["not"] != "temiz":
                    yeni["not"] = inceleme["not"]
                if isinstance(eski, dict) and eski.get("commit") == commit and eski.get("sonuc") == yeni["sonuc"]:
                    return False
                if isinstance(eski, dict):
                    # arşivden taşınmış alanları koru
                    korunan = {k: v for k, v in eski.items() if k not in ("commit", "tarih", "sonuc", "not")}
                    yeni = {**korunan, **yeni}
                x["inceleme"] = yeni
                degisti = True
                break
        if degisti:
            json_yaz(p, d)
        return degisti
    except (OSError, ValueError):
        return False


def fihrist_istek_coz(a, skiller):
    """--fihrist-skill REPO:AD|YOL isteklerini çözer (ağsız).
    Döner: (fihrist_liste, arsiv_yonlendirme[(s, rol)], hatalar[(kod, mesaj)], bilgiler[(kod, mesaj)])."""
    liste, arsiv_plan, hatalar, bilgiler = [], [], [], []
    gorulen = set()
    kay_map = kaynaklar_haritasi()
    for x in (getattr(a, "fihrist_skill", None) or []):
        repo, ayir, hedef = x.partition(":")
        repo, hedef = repo.strip(), hedef.strip()
        if not ayir or "/" not in repo or not hedef:
            hatalar.append(("fihrist-skill-bicim", f"`{x}`: REPO:AD ya da REPO:YOL biçiminde yaz, örn. github/awesome-copilot:agent-governance"))
            continue
        kay = kay_map.get(repo_guncel(repo).lower())
        if kay and kay.get("tip") == "KAYIP":
            hatalar.append(("fihrist-kaynak-kayip", f"{repo}: kaynak KAYIP olarak işaretli; yeni kurulumda kullanılmaz"))
            continue
        fh = fihrist_oku(repo)
        if not fh:
            hatalar.append(("fihrist-yok", f"{repo}: fihrist dosyası yok ({fihrist_dosya_yolu(repo).name})"))
            continue
        sk_list = fh["skiller"]
        tam_yol = [g for g in sk_list if g.get("yol") == hedef]
        if tam_yol:
            secilen = tam_yol[0]
        else:
            ad_es = [g for g in sk_list if (g.get("ad") or "").lower() == hedef.lower()]
            if not ad_es:
                hatalar.append(("fihrist-skill-yok", f"{x}: fihristte böyle bir skil yok ({fh['repo']})"))
                continue
            if len(ad_es) > 1:
                yollar = ", ".join(g["yol"] for g in ad_es[:5])
                hatalar.append(("fihrist-skill-belirsiz", f"{x}: fihristte aynı adda {len(ad_es)} skil var; tam yolu yaz: {yollar}"))
                continue
            secilen = ad_es[0]
        anahtar = (fh["repo"].lower(), secilen["yol"])
        if anahtar in gorulen:
            continue
        gorulen.add(anahtar)
        if not goreli_proje_yolu_gecerli(secilen.get("yol", "")):
            hatalar.append(("kaynak-erisim", f"{x}: fihrist kaydındaki yol geçersiz ({secilen.get('yol')!r}); klon dışına çıkamaz"))
            continue
        # Plan 5.5: aynı skil arşivde de varsa arşivdeki kayıt geçerlidir
        if secilen.get("arsivde"):
            arsiv_kay = next((s for s in skiller if s["repo"].lower() == fh["repo"].lower() and s["kaynak_yol"] == secilen["yol"]), None)
            if arsiv_kay:
                arsiv_plan.append((arsiv_kay, getattr(a, "rol_adi", None)))
                bilgiler.append(("fihrist-arsivde", f"{secilen['ad']} ({fh['repo']}): arşivde zaten var (`{arsiv_kay['id']}`); arşivdeki kayıt geçerlidir, ağ gerekmeden arşivden kurulacak"))
                continue
        liste.append({"repo": fh["repo"], "yol": secilen["yol"], "ad": secilen["ad"], "aciklama": secilen.get("aciklama", ""),
                      "fihrist_commit": fh.get("commit", ""), "fihrist_tarih": fh.get("tarih", ""),
                      "onceki_inceleme": secilen.get("inceleme"), "kaynak": kay, "rol": getattr(a, "rol_adi", None), "ham": x})
    return liste, arsiv_plan, hatalar, bilgiler


def fihrist_kurulum_adi(it, kilit, mevcut_adlar):
    """Fihrist skilinin projedeki klasör adı (kilitte aynı kaynak varsa o ad korunur)."""
    for ad, k in kilit["skiller"].items():
        if repo_guncel(k.get("repo", "")).lower() == it["repo"].lower() and k.get("kaynak_yol") == it["yol"]:
            return ad
    temiz = it["ad"] if ROL_ADI.match(it["ad"]) else (re.sub(r"[^a-z0-9-]+", "-", it["ad"].lower()).strip("-")[:64] or "skill")
    if temiz in mevcut_adlar or (temiz in kilit["skiller"]):
        repo_kisa = re.sub(r"[^a-z0-9-]+", "-", it["repo"].split("/")[-1].lower()).strip("-")[:20]
        temiz = f"{temiz[:40]}--{repo_kisa}"
    return temiz[:64]


def fihrist_on_kontrol(proje, kilit, fihrist_liste, lib_adlar, dis_adlari, rapor: Rapor):
    """Fihrist skilleri için AĞSIZ ön kontrol (plan 5.5). Döner: [(it, kurulum_adi)]."""
    if not fihrist_liste:
        return []
    mevcut_adlar = set(lib_adlar)
    dis_cf = {k.casefold() for k in dis_kayitlari(kilit)} | set(dis_adlari)
    hazir = []
    for it in fihrist_liste:
        ad = fihrist_kurulum_adi(it, kilit, mevcut_adlar)
        if ad in mevcut_adlar:
            rapor.ekle("HATA", "isim-cakismasi", f"{it['repo']}:{it['ad']} -> `{ad}` başka bir kurulum kalemiyle aynı adı alıyor")
            continue
        mevcut_adlar.add(ad)
        if ad.casefold() in dis_cf:
            rapor.ekle("HATA", "dis-ad-cakismasi", f"{ad}: projede aynı adlı program bağı/donmuş skill var; önce --kaldir")
            continue
        onceki = kilit["skiller"].get(ad)
        for yer in (proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad):
            if (yer.exists() or yer.is_symlink()) and not onceki:
                rapor.ekle("HATA", "projede-kendi-skillin", f"{yer.relative_to(proje)} zaten var ve kütüphaneden gelmemiş; üzerine yazılmaz (--zorla ile yedeklenip değiştirilir)")
        if onceki and (repo_guncel(onceki.get("repo", "")).lower(), onceki.get("kaynak_yol")) != (it["repo"].lower(), it["yol"]):
            rapor.ekle("HATA", "farkli-kaynak", f"{ad} projede {onceki.get('repo')}:{onceki.get('kaynak_yol')} kaynağından kurulu; önce --kaldir")
            continue
        if onceki and elle_degismis(proje, ad, onceki):
            rapor.ekle("HATA", "elle-degistirilmis", f"{ad} projede elle değiştirilmiş; ezilmez (--zorla: yedekle ve ez)")
        kay = it.get("kaynak") or {}
        if kay.get("lisans") in ("belirtilmemiş", "NOASSERTION", "yok"):
            rapor.ekle("UYARI", "lisans", f"{ad}: lisans belirtilmemiş ({it['repo']}); ticari kullanımda dikkat")
        uyum = kay.get("arac_uyumu") or {}
        if codex_var(kilit) and uyum.get("codex") is False:
            rapor.ekle("UYARI", "arac-uyumsuz", f"{ad}: kaynak kaydına göre Codex ile uyumlu değil ({it['repo']})")
        inc = it.get("onceki_inceleme")
        if isinstance(inc, dict) and inc.get("commit") == it.get("fihrist_commit"):
            rapor.ekle("BİLGİ", "fihrist-onceden-incelendi", f"{ad}: bu sürüm ({it['fihrist_commit'][:7]}) {inc.get('tarih', '?')} tarihinde incelendi (sonuç: {inc.get('sonuc', '?')})")
        else:
            rapor.ekle("UYARI", "fihrist-ilk-inceleme", f"{ad}: ilk kez inceleniyor ({it['repo']}:{it['yol']}); --evet ile geçici klasöre alınıp güvenlik/yol/araç incelemesinden sonra kurulacak")
        rapor.ekle("BİLGİ", "fihrist-internet", f"{ad}: fihrist kalemi — kurulum anında (--evet) GitHub'dan geçici klasöre alınır (internet gerekli); --kuru ağ kullanmaz")
        hazir.append((it, ad))
    return hazir


def fihrist_skil_kur(gecici_skil, proje, ad, it, codex):
    """Geçici klasördeki doğrulanmış fihrist skilini projeye atomik olarak kurar."""
    s_sahte = {"id": f"{ad}@{it['repo'].split('/')[-1]}", "ad": it["ad"], "klasor_adi": ad,
               "repo": it["repo"], "kaynak_yol": it["yol"], "yol": str(gecici_skil),
               "aciklama": it.get("aciklama", ""), "yama": None, "aciklama_duzeltme": None, "klasor_hash": None}
    codex_hedef = proje / ".agents" / "skills" / ad
    claude_hedef = proje / ".claude" / "skills" / ad
    if not codex:
        uyari = hazirla(gecici_skil, claude_hedef, s_sahte, ad, None, ".claude/skills", [], symlink_yasak=True)
        sil_yol(codex_hedef)
        return uyari
    uyari = hazirla(gecici_skil, codex_hedef, s_sahte, ad, None, ".agents/skills", [], symlink_yasak=True)
    claude_hedef.parent.mkdir(parents=True, exist_ok=True)
    sil_yol(claude_hedef)
    os.symlink(os.path.relpath(codex_hedef, claude_hedef.parent), claude_hedef)
    return uyari


def kit_istek_coz(a):
    """--kit ve --kit-parca isteklerini çözer (ağsız). Döner: (kit_liste, parcalar, hatalar)."""
    liste, hatalar = [], []
    parcalar = []
    for p in (getattr(a, "kit_parca", None) or []):
        temiz = p.strip().strip("/")
        if not temiz or temiz.startswith("/") or ".." in Path(temiz).parts:
            hatalar.append(("kit-parca-gecersiz", f"`{p}`: geçersiz parça yolu (proje içi göreli yol ver, '..' olamaz)"))
            continue
        parcalar.append(temiz)
    if parcalar and not getattr(a, "kit", None):
        hatalar.append(("kit-parca-gecersiz", "--kit-parca yalnız --kit ile kullanılır"))
    gorulen = set()
    kay_map = kaynaklar_haritasi()
    for x in (getattr(a, "kit", None) or []):
        k = kit_bul(x)
        if not k:
            hatalar.append(("kit-bulunamadi", f"`{x}`: kitler.json içinde böyle bir kit yok"))
            continue
        r_low = k["repo"].lower()
        if r_low in gorulen:
            continue
        gorulen.add(r_low)
        kay = kay_map.get(r_low)
        if kay and kay.get("tip") == "KAYIP":
            hatalar.append(("kit-kaynak-kayip", f"{k['repo']}: kit kaynağı KAYIP olarak işaretli; yeni projede kurulmaz"))
            continue
        liste.append({"kit": k, "kaynak": kay, "repo": k["repo"], "ad": k["ad"]})
    return liste, parcalar, hatalar


def kit_on_kontrol(proje, kilit, kit_liste, parcalar, rapor: Rapor):
    """Kitler için AĞSIZ ön kontrol (plan 5.7)."""
    if not kit_liste:
        return []
    baslamis = proje_baslamis_mi(proje)
    hazir = []
    for it in kit_liste:
        k, kay, repo = it["kit"], it.get("kaynak") or {}, it["repo"]
        if repo in kit_kayitlari(kilit):
            rapor.ekle("UYARI", "kit-zaten-kurulu", f"{repo}: bu kit projede zaten kurulu; kitteki değişiklikler projeye kendiliğinden uygulanmaz")
        if baslamis and not parcalar:
            rapor.ekle("HATA", "kit-baslamis-proje",
                       f"{repo}: proje başlamış, kit bütün olarak kurulmaz (var olan dosyaların, CLAUDE.md/AGENTS.md ve ayarların üzerine yazılmaz). "
                       f"Rehber: {k.get('baslamis_projede', '-')}. Yalnız çakışmayan parçaları seçmek için: --kit {repo} --kit-parca <yol>")
            continue
        if parcalar:
            ok_p = True
            for p in parcalar:
                if kit_korunan_mi(p):
                    rapor.ekle("HATA", "kit-korunan-dosya", f"{repo}: `{p}` korunan proje dosyası (CLAUDE.md/AGENTS.md/ayar); kit parçası olarak kurulamaz")
                    ok_p = False
                elif (proje / p).exists() or (proje / p).is_symlink():
                    rapor.ekle("HATA", "kit-dosya-cakismasi", f"{repo}: `{p}` projede zaten var; üzerine yazılmaz")
                    ok_p = False
            if not ok_p:
                continue
        kb = k.get("kurulum_betigi") or {}
        if kb.get("var"):
            rapor.ekle("UYARI", "kit-kurulum-betigi",
                       f"{repo}: kurulum betiği var ({kb.get('yol', '?')}): {kb.get('ne_yapar', '-')}. Betik araç tarafından kendiliğinden ÇALIŞTIRILMAZ.")
        if k.get("genel_klasore_yazar"):
            rapor.ekle("UYARI", "kit-genel-klasor",
                       f"{repo}: kit genel klasöre yazmak istiyor (~/.claude, ~/.agents vb.); bu adım ATLANIR (kütüphane kuralı).")
        for kp in (kay.get("kurulmayan_parcalar") or []):
            rapor.ekle("BİLGİ", "kit-atlanan", f"{repo}: kurulmayan/atlanan parça: {kp}")
        uyum = kay.get("arac_uyumu") or {}
        if codex_var(kilit) and uyum.get("codex") is False:
            rapor.ekle("UYARI", "arac-uyumsuz", f"{repo}: kaynak kaydına göre Codex ile tam uyumlu değil")
        if kay.get("lisans") in ("belirtilmemiş", "NOASSERTION", "yok"):
            rapor.ekle("UYARI", "lisans", f"{repo}: lisans belirtilmemiş; ticari kullanımda dikkat")
        bm = kaynak_boyut_metni(kay, dev_dahil=True)
        rapor.ekle("BİLGİ", "kit-internet",
                   f"{repo}: kit katalog kaydı — kurulum anında (--evet) GitHub'dan geçici klasöre alınır, incelenir ve "
                   + (f"yalnız seçilen parçalar ({', '.join(parcalar)})" if parcalar else "boş projeye iskelet olarak")
                   + f" kurulur (internet gerekli){f'; tahmini boyut: {bm}' if bm else ''}.")
        it["mod"] = "parca" if parcalar else "iskelet"
        it["parcalar"] = list(parcalar)
        hazir.append(it)
    return hazir


def kit_skilleri_bul(klon_dir):
    """Kit klonundaki SKILL.md içeren klasörleri bulur (symlink izlemez). Döner: [{ad, yol, arac_ici}]."""
    klon_dir = Path(klon_dir)
    sonuc = []
    for yol, dizinler, dosyalar in os.walk(klon_dir, followlinks=False):
        dizinler[:] = sorted(d for d in dizinler
                             if d != ".git" and d.casefold() not in DONDUR_GIZLI_DIZIN
                             and d not in DONDUR_ATLANAN_DIZIN and not (Path(yol) / d).is_symlink())
        for f in sorted(dosyalar):
            if f.lower() != "skill.md":
                continue
            sm = Path(yol) / f
            if sm.is_symlink() or not sm.is_file():
                continue
            klasor = sm.parent
            rel = klasor.relative_to(klon_dir).as_posix()
            if rel == ".":
                continue
            fm = frontmatter(sm.read_text(encoding="utf-8", errors="replace"))
            ham_ad = (fm.get("name") or klasor.name).strip()
            ad = ham_ad if ROL_ADI.match(ham_ad) else (re.sub(r"[^a-z0-9-]+", "-", ham_ad.lower()).strip("-")[:64] or "skill")
            arac_ici = rel.startswith((".claude/skills/", ".agents/skills/", ".codex/skills/"))
            sonuc.append({"ad": ad, "yol": rel, "klasor": klasor, "arac_ici": arac_ici})
    return sonuc


def gecici_kit_incele(klon_dir, kit_kaydi, proje, kilit, mod, parcalar, mevcut_skil_adlari, mevcut_dosyalar=()):
    """Geçici klasöre alınan kiti kurulum öncesi inceler (plan 5.7, 6.6, 6.8, 6.10)."""
    klon_dir = Path(klon_dir)
    guv = guvenlik_tara(klon_dir)
    skiller = kit_skilleri_bul(klon_dir)
    hedef_dosyalar = []
    atlanan_adimlar = []
    cakisanlar = []
    korunan_cakisma = []
    skil_cakisma = []
    secilen_skiller = []
    mevcut_dosya_set = set(mevcut_dosyalar or ())

    if kit_kaydi.get("genel_klasore_yazar") or guv["genel_yazma"]:
        atlanan_adimlar.append("genel klasöre yazan adımlar atlandı (~/.claude, ~/.agents, ~/.codex)")
    if (kit_kaydi.get("kurulum_betigi") or {}).get("var"):
        atlanan_adimlar.append(f"kurulum betiği çalıştırılmadı ({kit_kaydi['kurulum_betigi'].get('yol', '?')})")

    for yol, dizinler, dosyalar in os.walk(klon_dir, followlinks=False):
        g = os.path.relpath(yol, klon_dir)
        rel_fn = lambda n, g=g: n if g == "." else f"{g}/{n}"  # noqa: E731
        for d in list(dizinler):
            if d == ".git" or d.casefold() in DONDUR_GIZLI_DIZIN or d in DONDUR_ATLANAN_DIZIN or (Path(yol) / d).is_symlink():
                dizinler.remove(d)
        for f in sorted(dosyalar):
            if f == ".DS_Store" or gizli_ad_mi(f):
                continue
            p = Path(yol) / f
            if p.is_symlink():
                continue
            rel = rel_fn(f).replace(os.sep, "/")
            if rel.startswith((".claude/skills/", ".agents/skills/", ".codex/skills/")):
                continue  # araç içi skiller araç düzenine göre ayrıca yerleştirilir
            if mod == "parca":
                if not any(rel == pc or rel.startswith(pc + "/") for pc in parcalar):
                    continue
                if kit_korunan_mi(rel):
                    korunan_cakisma.append(rel)
                    continue
            else:
                if rel == META or rel.startswith(META + "/"):
                    korunan_cakisma.append(rel)
                    continue
                if rel in ("CLAUDE.md", "AGENTS.md"):
                    try:
                        tm = p.read_text(encoding="utf-8", errors="replace")
                        if BLOK_BAS in tm or BLOK_SON in tm:
                            korunan_cakisma.append(rel)
                            continue
                    except OSError:
                        pass
            if (proje / rel).exists() or (proje / rel).is_symlink() or rel in mevcut_dosya_set:
                cakisanlar.append(rel)
            hedef_dosyalar.append(rel)

    gorulen_skil_ad = set(mevcut_skil_adlari)
    dis_cf = {k.casefold() for k in dis_kayitlari(kilit)}
    for sk in skiller:
        if mod == "parca" and not any(sk["yol"] == pc or sk["yol"].startswith(pc + "/") or pc.startswith(sk["yol"] + "/") for pc in parcalar):
            continue
        ad = sk["ad"]
        a_h, c_h = proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad
        if (not dis_ad_gecerli(ad) or ad in gorulen_skil_ad or ad in kilit["skiller"] or ad.casefold() in dis_cf
                or a_h.exists() or a_h.is_symlink() or c_h.exists() or c_h.is_symlink()):
            skil_cakisma.append(ad)
        else:
            gorulen_skil_ad.add(ad)
            secilen_skiller.append(sk)

    eksik_parca = []
    if mod == "parca":
        for pc in parcalar:
            if not (klon_dir / pc).exists():
                eksik_parca.append(pc)

    toplam_bayt = sum((klon_dir / rel).stat().st_size for rel in hedef_dosyalar if (klon_dir / rel).is_file())
    satirlar = []
    if guv["symlinkler"]:
        satirlar.append(("HATA", "kit-symlink", f"{kit_kaydi['repo']}: symlink içeriyor ({', '.join(guv['symlinkler'][:4])}); dış dosya kopyalama riski nedeniyle kurulmaz"))
    if guv["gizli_dosyalar"]:
        satirlar.append(("HATA", "kit-gizli", f"{kit_kaydi['repo']}: gizli dosya/klasör içeriyor ({', '.join(guv['gizli_dosyalar'][:4])}); kurulmaz"))
    if eksik_parca:
        satirlar.append(("HATA", "kit-parca-gecersiz", f"{kit_kaydi['repo']}: istenen parça kitte yok: {', '.join(eksik_parca)}"))
    if korunan_cakisma:
        satirlar.append(("HATA", "kit-korunan-dosya", f"{kit_kaydi['repo']}: korunan dosyalara dokunulmaz: {', '.join(korunan_cakisma[:5])}"))
    if cakisanlar:
        satirlar.append(("HATA", "kit-dosya-cakismasi", f"{kit_kaydi['repo']}: projede zaten var olan ya da başka kitle çakışan {len(cakisanlar)} dosya: {', '.join(cakisanlar[:6])}"))
    if skil_cakisma:
        satirlar.append(("HATA", "isim-cakismasi", f"{kit_kaydi['repo']}: kit skilleri projedeki/kitteki skillerle çakışıyor: {', '.join(skil_cakisma[:5])}"))
    if guv["ag_calistir"]:
        satirlar.append(("UYARI", "guvenlik-ag", f"{kit_kaydi['repo']}: ağdan indirip çalıştıran komut var ({guv['ag_calistir'][0][0]}:{guv['ag_calistir'][0][1]}); çalıştırılmadı"))
    if guv["veri_gonder"]:
        satirlar.append(("UYARI", "guvenlik-veri", f"{kit_kaydi['repo']}: hassas dosya ile ağ komutu aynı satırda ({guv['veri_gonder'][0][0]}:{guv['veri_gonder'][0][1]}); incele"))
    if guv["talimat_enjeksiyon"]:
        satirlar.append(("UYARI", "guvenlik-talimat", f"{kit_kaydi['repo']}: onay atlama/yönlendirme metni var ({guv['talimat_enjeksiyon'][0][0]}:{guv['talimat_enjeksiyon'][0][1]}); uygulanmadı"))
    if guv["genel_yazma"]:
        kb_yol = (kit_kaydi.get("kurulum_betigi") or {}).get("yol")
        beklenmeyen_gy = [g for g in guv["genel_yazma"] if not (kit_kaydi.get("genel_klasore_yazar") and kb_yol and g[0] == kb_yol)]
        if beklenmeyen_gy:
            satirlar.append(("UYARI", "genele-yazabilir", f"{kit_kaydi['repo']}: genel klasöre yazan satır var ({beklenmeyen_gy[0][0]}:{beklenmeyen_gy[0][1]}); kütüphane kuralı genel klasöre yazmayı yasaklar"))
        else:
            satirlar.append(("BİLGİ", "kit-genel-atlandi", f"{kit_kaydi['repo']}: kurulum betiğindeki genel klasöre yazan satır atlandı ({guv['genel_yazma'][0][0]}:{guv['genel_yazma'][0][1]})"))
    return {"dosyalar": hedef_dosyalar, "skiller": secilen_skiller, "atlanan_adimlar": atlanan_adimlar,
            "cakisanlar": cakisanlar, "korunan_cakisma": korunan_cakisma, "skil_cakisma": skil_cakisma,
            "guvenlik": guv, "toplam_bayt": toplam_bayt, "satirlar": satirlar}


def kit_kur(klon_dir, proje, kilit, kit_kaydi, inceleme, commit, mod, parcalar):
    """Doğrulanmış kit dosyalarını ve skillerini projeye kurar (mevcut dosyanın üzerine asla yazmaz). Döner: kilit kaydı."""
    klon_dir = Path(klon_dir)
    codex = codex_var(kilit)
    dosya_hash = {}
    talimat_temiz_hash = {}
    toplam_bayt = 0
    for rel in inceleme["dosyalar"]:
        hedef = proje / rel
        if not goreli_proje_yolu_gecerli(rel) or not proje_ici(proje, hedef):
            raise RuntimeError(f"{rel}: proje dışına gidiyor")
        if hedef.exists() or hedef.is_symlink():
            raise RuntimeError(f"{rel}: projede zaten var; üzerine yazılmaz")
        hedef.parent.mkdir(parents=True, exist_ok=True)
        veri = (klon_dir / rel).read_bytes()
        hedef.write_bytes(veri)
        dosya_hash[rel] = git_blob_hash(veri)
        if rel in ("CLAUDE.md", "AGENTS.md"):
            talimat_temiz_hash[rel] = git_blob_hash(veri.decode("utf-8", errors="replace").strip().encode("utf-8"))
        toplam_bayt += len(veri)

    kurulan_skiller = []
    skil_hashleri = {}
    for sk in inceleme["skiller"]:
        ad = sk["ad"]
        if not dis_ad_gecerli(ad):
            raise RuntimeError(f"{ad}: geçersiz kit skil adı")
        s_sahte = {"id": f"{ad}@{kit_kaydi['repo'].split('/')[-1]}", "ad": ad, "klasor_adi": ad,
                   "repo": kit_kaydi["repo"], "kaynak_yol": sk["yol"], "yol": str(sk["klasor"]),
                   "aciklama": "", "yama": None, "aciklama_duzeltme": None, "klasor_hash": None}
        c_h = proje / ".claude" / "skills" / ad
        a_h = proje / ".agents" / "skills" / ad
        if not proje_ici(proje, c_h) or not proje_ici(proje, a_h):
            raise RuntimeError(f"{ad}: kit skili proje dışına gidiyor")
        if a_h.exists() or a_h.is_symlink() or c_h.exists() or c_h.is_symlink():
            raise RuntimeError(f"{ad}: projede zaten var; üzerine yazılmaz")
        if codex:
            hazirla(sk["klasor"], a_h, s_sahte, ad, None, ".agents/skills", [], symlink_yasak=True)
            c_h.parent.mkdir(parents=True, exist_ok=True)
            sil_yol(c_h)
            os.symlink(os.path.relpath(a_h, c_h.parent), c_h)
            toplam_bayt += sum(p.stat().st_size for p in onemli_dosyalar(a_h))
        else:
            hazirla(sk["klasor"], c_h, s_sahte, ad, None, ".claude/skills", [], symlink_yasak=True)
            sil_yol(a_h)
            toplam_bayt += sum(p.stat().st_size for p in onemli_dosyalar(c_h))
        kurulan_skiller.append(ad)
        skil_hashleri[ad] = kurulu_hash(proje, ad)

    kay = {"ad": kit_kaydi["ad"], "repo": kit_kaydi["repo"], "bolum": "katalog", "tur": "kit",
           "commit": commit, "tarih": date.today().isoformat(), "mod": mod, "parcalar": list(parcalar),
           "dosyalar": dosya_hash, "skiller": sorted(kurulan_skiller), "skil_hashleri": skil_hashleri,
           "boyut_bayt": toplam_bayt, "atlanan_adimlar": list(inceleme["atlanan_adimlar"])}
    if talimat_temiz_hash:
        kay["talimat_temiz_hash"] = talimat_temiz_hash
    return kay


def kit_dosya_degismis_mi(rel, p: Path, eski_h, talimat_temiz_hash=None):
    """Kit dosyası kurulumdan sonra kullanıcı tarafından değiştirilmiş mi?
    CLAUDE.md/AGENTS.md için aracın kendi eklediği skill-kutuphanesi bloğu değişiklik sayılmaz."""
    if not (p.is_file() and not p.is_symlink()):
        return True
    ham = p.read_bytes()
    if git_blob_hash(ham) == eski_h:
        return False
    if rel in ("CLAUDE.md", "AGENTS.md"):
        metin = ham.decode("utf-8", errors="replace")
        if BLOK_BAS in metin and BLOK_SON in metin:
            temiz = re.sub(r"\n*" + re.escape(BLOK_BAS) + r".*?" + re.escape(BLOK_SON) + r"\n?", "\n", metin, flags=re.S).strip()
            beklenen_temiz = (talimat_temiz_hash or {}).get(rel)
            if beklenen_temiz:
                return git_blob_hash(temiz.encode("utf-8")) != beklenen_temiz
            return git_blob_hash((temiz + "\n").encode("utf-8")) != eski_h and git_blob_hash(temiz.encode("utf-8")) != eski_h
    return True


def yerel_skil_duzene_al(proje, ad, codex):
    """Fihrist veya kit skilini ağa çıkmadan yeni araç düzenine taşır (içeriğe dokunmaz). Döner: hata/uyarı mesajı ya da None."""
    if not dis_ad_gecerli(ad):
        return f"{ad}: geçersiz skil adı; dokunulmadı"
    h, c = proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad
    if not proje_ici(proje, h) or not proje_ici(proje, c):
        return f"{ad}: proje dışına gidiyor; dokunulmadı"
    rel_h = os.path.relpath(h, c.parent)
    h_gercek = h.is_dir() and not h.is_symlink()
    c_gercek = c.is_dir() and not c.is_symlink()
    if codex:
        if not h_gercek and c_gercek:
            h.parent.mkdir(parents=True, exist_ok=True)
            if h.is_symlink():
                sil_yol(h)
            os.replace(c, h)
            h_gercek = True
        elif h_gercek and c_gercek:
            return f"{ad}: .agents/skills ve .claude/skills altında iki gerçek klasör var; dokunulmadı"
        if h_gercek:
            if not (c.is_symlink() and os.readlink(c) == rel_h):
                sil_yol(c)
                c.parent.mkdir(parents=True, exist_ok=True)
                os.symlink(rel_h, c)
        else:
            return f"{ad}: skil klasörü yok; taşınamadı"
    else:
        if not c_gercek and h_gercek:
            sil_yol(c)
            c.parent.mkdir(parents=True, exist_ok=True)
            os.replace(h, c)
            c_gercek = True
        elif h_gercek and c_gercek:
            return f"{ad}: .agents/skills ve .claude/skills altında iki gerçek klasör var; dokunulmadı"
        if c_gercek:
            if h.is_symlink():
                sil_yol(h)
        else:
            return f"{ad}: skil klasörü yok; taşınamadı"
    return None


def fihrist_yerlestir(proje, kilit):
    """Kurulu fihrist skillerini güncel araç düzenine taşır ve kurulu_hash'lerini yeniler."""
    mesaj = []
    codex = codex_var(kilit)
    for ad, k in sorted(kilit["skiller"].items()):
        if k.get("bolum") != "fihrist":
            continue
        degismis = elle_degismis(proje, ad, k)
        m = yerel_skil_duzene_al(proje, ad, codex)
        if m:
            mesaj.append(m)
        elif not degismis:
            k["kurulu_hash"] = kurulu_hash(proje, ad)
    return mesaj


def kit_yerlestir(proje, kilit):
    """Kurulu kit skillerini güncel araç düzenine taşır ve değişmemiş olanların skil_hashleri kaydını yeniler."""
    mesaj = []
    codex = codex_var(kilit)
    for kr, kg in sorted(kit_kayitlari(kilit).items()):
        sh = kg.get("skil_hashleri") if isinstance(kg.get("skil_hashleri"), dict) else {}
        for sk in list(kg.get("skiller") or []):
            if not dis_ad_gecerli(sk):
                mesaj.append(f"kit {kr} skili {sk}: geçersiz skil adı; dokunulmadı")
                continue
            eski_h = sh.get(sk)
            degismis = bool(eski_h and elle_degismis(proje, sk, {"kurulu_hash": eski_h}))
            m = yerel_skil_duzene_al(proje, sk, codex)
            if m:
                mesaj.append(f"kit {kr} {m}")
            elif not degismis:
                if not isinstance(kg.get("skil_hashleri"), dict):
                    kg["skil_hashleri"] = {}
                kg["skil_hashleri"][sk] = kurulu_hash(proje, sk)
    return mesaj


def fihrist_oner(sorgu_metni, teknolojiler, arsiv_adlari=(), sinir=FIHRIST_ONERI_SINIRI):
    """Plan 5.5: Fihristten en çok `sinir` (3) aday önerir; arşivde olanlar ve kaynağı KAYIP olanlar elenir."""
    sorgu = kelimeler(sorgu_metni)
    if not sorgu and not teknolojiler:
        return []
    kay_map = kaynaklar_haritasi()
    arsiv_cf = {a.lower() for a in arsiv_adlari}
    adaylar = []
    for fh in fihrist_tumu():
        repo = fh["repo"]
        kay = kay_map.get(repo.lower())
        if kay and kay.get("tip") == "KAYIP":
            continue
        for g in fh["skiller"]:
            if g.get("arsivde") or (g.get("ad") or "").lower() in arsiv_cf:
                continue
            metin = " ".join([g.get("ad", ""), g.get("aciklama", ""), g.get("yol", "")]).lower()
            esl = [w for w in sorgu if re.search(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])", metin)]
            tek_esl = [t for t in teknolojiler if t in metin]
            p = 3 * len(esl) + 2 * len(tek_esl)
            if p > 0:
                inc = g.get("inceleme")
                if isinstance(inc, dict) and inc.get("sonuc") == "temiz":
                    p += 0.5
                adaylar.append((p, repo, g, esl + tek_esl))
    adaylar.sort(key=lambda x: (-x[0], x[1], x[2].get("ad", "")))
    return adaylar[:sinir]


def kit_oner(sorgu_metni, teknolojiler, sinir=3):
    """Kit kataloğundan eşleşen adaylar (kaynağı KAYIP olmayanlar)."""
    sorgu = kelimeler(sorgu_metni)
    if not sorgu and not teknolojiler:
        return []
    kay_map = kaynaklar_haritasi()
    adaylar = []
    for k in kitler_listesi():
        kay = kay_map.get(k["repo"].lower())
        if kay and kay.get("tip") == "KAYIP":
            continue
        metin = " ".join([k.get("ad", ""), k.get("repo", ""), k.get("ne_yapar", ""), " ".join(k.get("skiller", [])),
                          " ".join(k.get("yapi_ozeti", []))]).lower()
        esl = [w for w in sorgu if re.search(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])", metin)]
        tek_esl = [t for t in teknolojiler if t in metin]
        p = 3 * len(esl) + 2 * len(tek_esl)
        if p > 0:
            adaylar.append((p, k, kay, esl + tek_esl))
    adaylar.sort(key=lambda x: (-x[0], x[1]["repo"]))
    return adaylar[:sinir]


def program_oner(sorgu_metni, teknolojiler, sinir=4):
    """programlar.json içinden ihtiyaca uyan programlar (kurulu durumu ve tahmini boyutla)."""
    sorgu = kelimeler(sorgu_metni)
    if not sorgu and not teknolojiler:
        return []
    adaylar = []
    for ad, kart in sorted(program_kartlari().items()):
        metin = " ".join([ad, kart.get("repo", ""), kart.get("ne_yapar", ""), " ".join(kart.get("skilleri", []))]).lower()
        esl = [w for w in sorgu if re.search(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])", metin)]
        tek_esl = [t for t in teknolojiler if t in metin]
        p = 3 * len(esl) + 2 * len(tek_esl)
        if p > 0:
            koku = program_skill_koku(kart)
            kurulu = bool(koku and koku.is_dir())
            adaylar.append((p, ad, kart, kurulu, program_boyut_metni(ad), esl + tek_esl))
    adaylar.sort(key=lambda x: (-x[0], x[1]))
    return adaylar[:sinir]


def referans_oner(sorgu_metni, teknolojiler, sinir=5):
    """kaynaklar.json içindeki T5/T6 referans kaynaklarından ihtiyaca uyanlar."""
    sorgu = kelimeler(sorgu_metni)
    if not sorgu and not teknolojiler:
        return []
    adaylar = []
    for k in kaynaklar_haritasi().values():
        if k.get("tip") not in ("T5", "T6"):
            continue
        metin = " ".join([k.get("repo", ""), k.get("not", ""), k.get("tur_gerekce", ""), k.get("ne_ister", "")]).lower()
        esl = [w for w in sorgu if re.search(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])", metin)]
        tek_esl = [t for t in teknolojiler if t in metin]
        p = 3 * len(esl) + 2 * len(tek_esl)
        if p > 0:
            adaylar.append((p, k, esl + tek_esl))
    adaylar.sort(key=lambda x: (-x[0], x[1]["repo"]))
    return adaylar[:sinir]


def proje_raporu_uret(proje, kilit, skiller, rapor: Rapor, kur_listesi=None, adlar=None,
                      fihrist_hazir=(), kit_hazir=(), dis_liste=(), sorgu="", roller=()):
    """Plan Bölüm 10: 10 bölümlü tam Proje Raporu (+ başlamış projede ek 3 bölüm + tek net öneri).
    Her zaman AĞSIZ ve salt okunurdur; kurulumdan önce verilir."""
    kur_listesi = kur_listesi or {}
    adlar = adlar or {}
    kay_map = kaynaklar_haritasi()
    tek = proje_teknolojileri(proje) if proje else set()
    baslamis = proje_baslamis_mi(proje) if proje else False
    out = ["", "=" * 68, "PROJE RAPORU (Plan Bölüm 10 — ağsız ön rapor)", "=" * 68]

    # 1. Öneriler
    out.append("\n## 1. Öneriler")
    if kur_listesi:
        out.append("- Arşiv skilleri (seçilen):")
        for sid, (s, rk) in kur_listesi.items():
            rol_m = ", ".join(sorted(r for r in rk if r)) or "genel"
            out.append(f"  - `{adlar.get(sid, sid)}` ({s['repo']}, rol: {rol_m}) — {(s.get('ozet_tr') or s.get('aciklama', ''))[:90]}")
    if fihrist_hazir:
        out.append("- Fihrist skilleri (seçilen, kurulum anında geçici klasörde incelenir):")
        for it, ad in fihrist_hazir:
            out.append(f"  - `{ad}` ({it['repo']}:{it['yol']}) — {(it.get('aciklama') or 'fihrist skili')[:90]}")
    if kit_hazir:
        out.append("- Kitler (seçilen, katalog):")
        for it in kit_hazir:
            out.append(f"  - `{it['repo']}` ({it['ad']}, mod: {it['mod']}) — {it['kit'].get('ne_yapar', '')[:90]}")
    if dis_liste:
        out.append("- Program bağı / donmuş skiller (seçilen):")
        for it in dis_liste:
            if it["tur"] == "program-bag":
                out.append(f"  - `{it['program']}:{it['ad']}` (bağ: kurulu program klasörüne)")
            else:
                out.append(f"  - `{it['ad']}` (donmuş kopya: {yol_goster(it['kaynak'])})")
    if sorgu or (not kur_listesi and not fihrist_hazir and not kit_hazir and not dis_liste):
        sorgu_ef = sorgu or " ".join(sorted(tek))
        arsiv_ad, _, _ = kutuphane_taramasi(skiller, sorgu_ef, tek, haric_idler=set(kur_listesi), n=5, kategori_basi=2) if sorgu_ef else ([], 0, 0)
        if arsiv_ad:
            out.append("- Arşiv önerileri (incelenmiş/arşivde, ağ gerekmez):")
            for _, s, e, t in arsiv_ad:
                out.append(f"  - `{s['id']}` (puan {s['degerlendirme']['puan']}, eşleşen: {', '.join(e + sorted(t))})")
        fh_ad = fihrist_oner(sorgu_ef, tek, arsiv_adlari=[s["ad"] for _, s, _, _ in arsiv_ad] + [s["ad"] for s, _ in kur_listesi.values()])
        if fh_ad:
            out.append(f"- Fihrist önerileri (en çok {FIHRIST_ONERI_SINIRI} aday; kurulumda internet gerekir):")
            for _, repo, g, e in fh_ad:
                out.append(f"  - `{repo}:{g['ad']}` (eşleşen: {', '.join(e[:4])}) — {g.get('aciklama', '')[:80]}")
        kt_ad = kit_oner(sorgu_ef, tek)
        if kt_ad:
            out.append("- Kit önerileri (hazır proje iskeleti):")
            for _, kt, kay, e in kt_ad:
                bm = kaynak_boyut_metni(kay, dev_dahil=True)
                out.append(f"  - `{kt['repo']}` ({kt['ad']}; eşleşen: {', '.join(e[:4])}){f' · {bm}' if bm else ''}")
        pr_ad = program_oner(sorgu_ef, tek)
        if pr_ad:
            out.append("- Program önerileri:")
            for _, pad, kart, kurulu, bm, e in pr_ad:
                dur = "kurulu (bağ verilebilir)" if kurulu else f"kurulu değil{f', kurulumu {bm} yer tutar' if bm else ''} (ayrı onay ister)"
                out.append(f"  - `{pad}` ({dur}) — {kart.get('ne_yapar', '')[:80]}")
        rf_ad = referans_oner(sorgu_ef, tek)
        if rf_ad:
            out.append("- Referans araç/kütüphaneler (skili yok, bilinmeye değer):")
            for _, rk, e in rf_ad:
                out.append(f"  - `{rk['repo']}` ({rk['tip']}, eşleşen: {', '.join(e[:4])})")
    if len(out) <= 5 or out[-1] == "\n## 1. Öneriler":
        out.append("- Ek öneri yok.")

    # 2. Güncellik
    out.append("\n## 2. Güncellik")
    guncellik_var = False
    for sid, (s, _) in kur_listesi.items():
        guncellik_var = True
        kay = kay_map.get(s["repo"].lower()) or {}
        tarih = (s.get("gelistirici") or {}).get("son_guncelleme") or (kay.get("son_kontrol") or {}).get("tarih") or s.get("eklendi") or "?"
        out.append(f"- Arşiv `{adlar.get(sid, sid)}`: commit `{str(s.get('commit', '?'))[:7]}` · tarih {tarih}")
    for it, ad in fihrist_hazir:
        guncellik_var = True
        inc = it.get("onceki_inceleme")
        dur = f"önceden incelendi ({inc.get('tarih', '?')})" if (isinstance(inc, dict) and inc.get("commit") == it.get("fihrist_commit")) else "ilk kez inceleniyor"
        out.append(f"- Fihrist `{ad}` ({it['repo']}): fihrist tarihi {it.get('fihrist_tarih') or '?'} · commit `{it.get('fihrist_commit', '?')[:7]}` · {dur} (kurulumda son sürüm alınır)")
    for it in kit_hazir:
        guncellik_var = True
        sk_ = (it.get("kaynak") or {}).get("son_kontrol") or {}
        out.append(f"- Kit `{it['repo']}`: son kontrol {sk_.get('tarih', '?')} · commit `{str(sk_.get('commit', '?'))[:7]}` (kurulumda son sürüm alınır)")
    for it in dis_liste:
        guncellik_var = True
        if it["tur"] == "program-bag":
            out.append(f"- Program bağı `{it['program']}:{it['ad']}`: kart sürümü {surum_metni(it.get('surum'), it.get('surum_turu'))} (programla güncel)")
        else:
            out.append(f"- Donmuş `{it['ad']}`: yerel kopya (kütüphane güncellemez)")
    if not guncellik_var:
        out.append("- Seçili kurulum kalemi yok.")

    # 3. Boyut
    out.append("\n## 3. Boyut")
    arsiv_bayt = 0
    for sid, (s, _) in kur_listesi.items():
        yol = KOK / s["yol"]
        b = sum(p.stat().st_size for p in onemli_dosyalar(yol)) if yol.is_dir() else int(round((s.get("skill_md_kb") or 0) * 1024))
        arsiv_bayt += b
        out.append(f"- Arşiv `{adlar.get(sid, sid)}`: {boyut_bicim(b)}")
    for it, ad in fihrist_hazir:
        bm = kaynak_boyut_metni(it.get("kaynak"))
        out.append(f"- Fihrist `{ad}`: kurulumda geçici klasörde ölçülür" + (f" (kaynak tahmini: {bm})" if bm else ""))
    kit_mb_toplam = 0.0
    hesaplanamayanlar, inecekler = [], []
    for it in kit_hazir:
        kay = it.get("kaynak") or {}
        b = kay.get("boyut") or {}
        mb = b.get("kurulum_mb_devdahil") if b.get("kurulum_mb_devdahil") is not None else b.get("kurulum_mb")
        if isinstance(mb, (int, float)):
            kit_mb_toplam += mb
        bm = kaynak_boyut_metni(kay, dev_dahil=True)
        out.append(f"- Kit `{it['repo']}`: {bm or 'kurulumda ölçülür'}")
        hesaplanamayanlar += list(b.get("hesaplanamayan") or [])
        if kay.get("ne_indirir"):
            inecekler.append(f"{it['repo']}: {kay['ne_indirir']}")
    for it in dis_liste:
        if it["tur"] == "program-bag":
            out.append(f"- Program bağı `{it['program']}:{it['ad']}`: ~0 KB (symlink; program bilgisayarda tek kurulum)")
        else:
            out.append(f"- Donmuş `{it['ad']}`: {boyut_bicim((it.get('tarama') or {}).get('bayt', 0))}")
    don_bayt = sum((it.get("tarama") or {}).get("bayt", 0) for it in dis_liste if it["tur"] == "donmus")
    out.append(f"- Toplam (kesin yerel): {boyut_bicim(arsiv_bayt + don_bayt)}"
               + (f" + kit tahmini ~{kit_mb_toplam:.0f} MB" if kit_mb_toplam else "")
               + (f" + {len(fihrist_hazir)} fihrist skili (kurulumda ölçülür)" if fihrist_hazir else ""))
    if inecekler:
        out.append("- Kurulumda / çalışırken inecekler: " + "; ".join(inecekler[:4]))
    if hesaplanamayanlar:
        out.append("- Hesaplanamayanlar: " + ", ".join(sorted(set(hesaplanamayanlar))[:6]) + " (kurulum betiği veya çalışırken inen modeller)")
    else:
        out.append("- Not: bağımlılık listesinde olmayıp kurulum betiğiyle kurulan parçalar ve çalışırken inen modeller önceden hesaplanamaz; kurulumdan sonra gerçek boyut ölçülür.")

    # 4. Kurulamayanlar
    out.append("\n## 4. Kurulamayanlar")
    kurulamayan_kod = {"bulunamadi", "fihrist-yok", "fihrist-kaynak-kayip", "fihrist-skill-yok", "fihrist-skill-belirsiz",
                       "kit-bulunamadi", "kit-kaynak-kayip", "kit-baslamis-proje", "kit-korunan-dosya",
                       "program-kurulu-degil", "program-bilinmiyor", "program-skillsiz", "kaynak-erisim"}
    kurulamayan = [(k, m) for sv, k, m in rapor.satirlar if sv == "HATA" and k in kurulamayan_kod]
    for it, ad in fihrist_hazir:
        if (it.get("kaynak") or {}).get("tek_basina") is False:
            kurulamayan.append(("koke-bagli", f"{ad}: kaynak tek başına kurulmaz işaretli"))
    if kurulamayan:
        for k, m in kurulamayan:
            out.append(f"- **{k}**: {m}")
    else:
        out.append("- Yok.")
    if fihrist_hazir or kit_hazir:
        out.append("- İnternet notu: fihrist ve kit kalemleri çevrimdışı ortamda kurulamaz (internet gerekli).")

    # 5. Araç uyumu
    out.append("\n## 5. Araç uyumu")
    arac_s = [(k, m) for _, k, m in rapor.satirlar if k.startswith("arac-") or k in ("codex-uyum", "claude-ozel")]
    if arac_s:
        for k, m in arac_s:
            out.append(f"- **{k}**: {m}")
    else:
        out.append(f"- Seçilen düzen: `{duzen_adi(kilit)}` (Claude Code, Codex, Antigravity).")
    if any(it["tur"] == "program-bag" for it in dis_liste):
        out.append("- Windows: program bağları mutlak Mac yoludur; Windows'ta çalışmaz.")

    # 6. Çakışmalar
    out.append("\n## 6. Çakışmalar")
    cak_kod = {"isim-cakismasi", "dis-ad-cakismasi", "projede-kendi-skillin", "farkli-kaynak", "ayni-ad",
               "ortusme", "ayni-skill-iki-surum", "kit-dosya-cakismasi", "hesap-cakismasi", "global-cakisma-yeni"}
    cak = [(sv, k, m) for sv, k, m in rapor.satirlar if k in cak_kod]
    if cak:
        for sv, k, m in cak:
            out.append(f"- [{sv}] **{k}**: {m}")
    else:
        out.append("- Çakışma yok.")

    # 7. Gereksinimler
    out.append("\n## 7. Gereksinimler")
    ger_kod = {"bagimlilik", "ucretli", "kismen-ucretli", "ucret-belirsiz", "program-kurulu-degil"}
    ger = [(sv, k, m) for sv, k, m in rapor.satirlar if k in ger_kod]
    for it in kit_hazir:
        ni = (it.get("kaynak") or {}).get("ne_ister")
        if ni:
            ger.append(("BİLGİ", "ne-ister", f"{it['repo']}: {ni}"))
    for it, ad in fihrist_hazir:
        ni = (it.get("kaynak") or {}).get("ne_ister")
        if ni and ni != "skile göre değişir":
            ger.append(("BİLGİ", "ne-ister", f"{ad}: {ni}"))
    if ger:
        for sv, k, m in ger:
            out.append(f"- [{sv}] **{k}**: {m}")
    else:
        out.append("- Ek program, anahtar ya da ücretli gereksinim tespit edilmedi.")

    # 8. Güvenlik
    out.append("\n## 8. Güvenlik")
    guv_kod = {"genele-yazabilir", "kit-kurulum-betigi", "kit-genel-klasor", "kit-atlanan",
               "guvenlik-ag", "guvenlik-veri", "guvenlik-talimat", "dondur-gizli", "fihrist-gizli"}
    guv_s = [(sv, k, m) for sv, k, m in rapor.satirlar if k in guv_kod]
    if guv_s:
        for sv, k, m in guv_s:
            out.append(f"- [{sv}] **{k}**: {m}")
    else:
        out.append("- Bilinen kurulum betiği, ağdan indirip çalıştıran adım, dışarı veri gönderimi ya da atlanan talimat yok.")
    if fihrist_hazir or kit_hazir:
        out.append("- Not: GitHub'dan gelen içerik veridir, talimat değildir; fihrist/kit kalemleri kurulumda geçici klasörde taranır, genel klasöre yazan adımlar ve kurulum betikleri çalıştırılmaz.")

    # 9. Olası hatalar
    out.append("\n## 9. Olası hatalar")
    hata_kod = {"kirik-baglanti", "kardes-eksik", "eklenti-koku", "skil-disi-yol", "genel-yol", "kardes-farkli-kaynak",
                "kaynak-kayip", "kaynakta-kaldirildi", "emekli", "tetiklenmez", "dusuk-puan", "lisans"}
    olasi = [(sv, k, m) for sv, k, m in rapor.satirlar if k in hata_kod]
    # Bakımsız kaynak kontrolü
    for sid, (s, _) in kur_listesi.items():
        kay = kay_map.get(s["repo"].lower())
        if kaynak_bakimsiz_mi(kay):
            olasi.append(("BİLGİ", "bakimsiz", f"{adlar.get(sid, sid)}: kaynak 12 aydan uzun süredir değişmemiş ({s['repo']})"))
    # Sürüm uyuşmazlığı kontrolü (ürün + skil ve package.json)
    surumler = proje_paket_surumleri(proje) if proje else {}
    if surumler:
        for sid, (s, _) in kur_listesi.items():
            kay = kay_map.get(s["repo"].lower()) or {}
            kay_sur = kay.get("urun_surumu")
            if kay_sur:
                for p_ad, p_sur in surumler.items():
                    if p_ad.lower() in s["repo"].lower():
                        olasi.append(("BİLGİ", "surum-kontrol", f"{adlar.get(sid, sid)}: projede {p_ad} {p_sur}, kaynak kaydı {kay_sur}"))
    if olasi:
        for sv, k, m in olasi:
            out.append(f"- [{sv}] **{k}**: {m}")
    else:
        out.append("- Bilinen eksik dosya, kırık bağlantı, köke bağlı yol ya da bakımsız kaynak yok.")

    # 10. Model hafızası
    out.append("\n## 10. Model hafızası")
    toplam_sm_bayt = 0
    for sid, (s, _) in kur_listesi.items():
        yol = KOK / s["yol"] / "SKILL.md"
        b = yol.stat().st_size if yol.is_file() else int(round((s.get("skill_md_kb") or 0) * 1024))
        toplam_sm_bayt += b
    # Projede zaten kurulu (ve bu işlemde tekrar gelmeyen) skillerin yükü
    mevcut_kurulu_bayt = 0
    for kad, kv in kilit.get("skiller", {}).items():
        if kad in set(adlar.values()):
            continue
        p = proje / (".agents/skills" if codex_var(kilit) else ".claude/skills") / kad / "SKILL.md" if proje else None
        if p and p.is_file():
            mevcut_kurulu_bayt += p.stat().st_size
    tum_bayt = toplam_sm_bayt + mevcut_kurulu_bayt
    ek_olculmeyen = len(fihrist_hazir) + sum(len(it["kit"].get("skiller", [])) for it in kit_hazir)
    out.append(f"- Kurulacak arşiv skilleri SKILL.md yükü: {toplam_sm_bayt / 1024:.1f} KB (~{token_tahmini(toplam_sm_bayt)} token)"
               + (f" · projede mevcutlarla toplam: {tum_bayt / 1024:.1f} KB (~{token_tahmini(tum_bayt)} token)" if mevcut_kurulu_bayt else "")
               + (f" + {ek_olculmeyen} fihrist/kit skili (kurulum anında ölçülür)" if ek_olculmeyen else ""))
    for rol in roller:
        rs = [s for s, rk in kur_listesi.values() if rol in rk]
        kb = sum(x.get("skill_md_kb", 0) for x in rs)
        out.append(f"  - Rol `{rol}`: {len(rs)} skill, {kb:.1f} KB (~{token_tahmini(int(kb * 1024))} token; öneri ≤{SINIR_ROL_SKILL} skill, ≤{SINIR_ROL_KB} KB)")

    # Başlamış projede ek bölümler
    if baslamis:
        out.append("\n## Başlamış proje ek bilgileri")
        kurulu_sk = sorted(kilit.get("skiller", {}))
        kurulu_dis = sorted(dis_kayitlari(kilit))
        kurulu_kt = sorted(kit_kayitlari(kilit))
        out.append(f"- **Projede olanlar:** {len(kurulu_sk)} skill ({', '.join(kurulu_sk[:8]) or '-'}) · "
                   f"{len(kurulu_dis)} dış skill ({', '.join(kurulu_dis[:6]) or '-'}) · "
                   f"{len(kurulu_kt)} kit ({', '.join(kurulu_kt) or '-'}) · teknolojiler: {', '.join(sorted(tek)) or '-'}")
        gunc_list = []
        for kad, kv in sorted(kilit.get("skiller", {}).items()):
            if kv.get("bolum") == "fihrist":
                fh = fihrist_oku(kv.get("repo", ""))
                if fh and fh.get("commit") and fh["commit"] != kv.get("commit"):
                    gunc_list.append(f"{kad} (fihrist: {kv['commit'][:7]} -> {fh['commit'][:7]})")
            else:
                s_ = kaynak_bul(skiller, kv)
                if s_ and s_["klasor_hash"] != kv.get("klasor_hash"):
                    gunc_list.append(f"{kad} ({kv['commit'][:7]} -> {s_['commit'][:7]})")
        for kr, kv in sorted(kit_kayitlari(kilit).items()):
            sc = ((kay_map.get(kr.lower()) or {}).get("son_kontrol") or {}).get("commit")
            if sc and sc != kv.get("commit"):
                gunc_list.append(f"kit {kr} ({kv['commit'][:7]} -> {sc[:7]}; otomatik uygulanmaz)")
        out.append(f"- **Güncellenebilecekler:** {', '.join(gunc_list) or 'yok'}")
        dokun = []
        yer = ".agents/skills" if codex_var(kilit) else ".claude/skills"
        for ad in sorted(set(adlar.values()) | {ad for _, ad in fihrist_hazir} | {it["ad"] for it in dis_liste}):
            dokun.append(f"{yer}/{ad}")
            if codex_var(kilit):
                dokun.append(f".claude/skills/{ad}")
        for it in kit_hazir:
            dokun += it.get("parcalar") or [f"{it['repo']} (iskelet)"]
        if kur_listesi or fihrist_hazir or dis_liste or kit_hazir:
            dokun += [f"{META}/kilit.json", "CLAUDE.md"] + (["AGENTS.md"] if codex_var(kilit) else [])
        out.append(f"- **Dokunulacak dosyalar:** {', '.join(dokun[:14]) or 'yok'}" + (f" (+{len(dokun) - 14})" if len(dokun) > 14 else ""))

    # Sonda tek, net öneri
    out.append("\n## Öneri")
    hata_n, uyari_n = rapor.say("HATA"), rapor.say("UYARI")
    if hata_n:
        out.append(f"Şu an KURMA: {hata_n} HATA var. Önce yukarıdaki HATA satırlarını çöz, sonra tekrar `--kuru` ile kontrol et.")
    elif not kur_listesi and not fihrist_hazir and not kit_hazir and not dis_liste:
        out.append("Henüz kurulum kalemi seçilmedi. Bölüm 1'deki adaylardan uygun olanları `--profil`, `--skill`, `--fihrist-skill`, `--kit` veya `--program-skill` ile seçip `--kuru` çalıştır.")
    elif fihrist_hazir or kit_hazir:
        out.append(f"Onaylıyorsan aynı komutu `--evet` ile çalıştır ({uyari_n} uyarı; fihrist/kit kalemleri geçici klasöre alınıp incelendikten sonra kurulur, internet gerekli).")
    elif uyari_n:
        out.append(f"Onaylıyorsan aynı komutu `--evet` ile çalıştır ({uyari_n} uyarı var, engelleyici hata yok).")
    else:
        out.append("Hazır — engelleyici hata ve uyarı yok; `--evet` ile kurulabilir.")
    return "\n".join(out)


# ================================================================== agent dosyaları
def toml_str(x):
    return json.dumps(x, ensure_ascii=False)  # JSON dizgesi geçerli bir TOML temel dizgesidir


def onyuklenebilir(s):
    return not any("disable-model-invocation" in x for x in s.get("yapisal_sorunlar", []))


def agent_dosyalari(proje: Path, kilit: dict, skiller):
    rol_kur = {}
    for ad, k in kilit["skiller"].items():
        for r in k["roller"]:
            rol_kur.setdefault(r, []).append(ad)
    tum = sorted(kilit["skiller"])
    codex = codex_var(kilit)
    if kilit["roller"]:
        (proje / ".claude" / "agents").mkdir(parents=True, exist_ok=True)
        if codex:
            (proje / ".codex" / "agents").mkdir(parents=True, exist_ok=True)
    for rol in kilit["roller"]:
        if not ROL_ADI.match(rol):  # savunma: geçersiz ad asla dosya yoluna dönüşmez
            continue
        tanim = json_oku(ROLLER / f"{rol}.json") or {"aciklama": rol, "gorev": f"{rol} rolü."}
        benim = sorted(rol_kur.get(rol, []))
        onyukle = [a for a in benim if onyuklenebilir(kaynak_bul(skiller, kilit["skiller"][a]) or {})]
        elle = [a for a in benim if a not in onyukle]
        talimat = (f"{tanim['gorev']}\n\nBu rolün skilleri: {', '.join(benim) or '-'}.\n"
                   "İşe başlamadan önce ilgili skill'in SKILL.md dosyasını oku ve kurallarına uy. "
                   "Skill'de olmayan bir konuda varsayım yapma; emin değilsen ana agent'a sor."
                   + (f"\nŞu skiller otomatik yüklenmez, gerektiğinde açıkça çağır: {', '.join(elle)}." if elle else ""))
        (proje / ".claude" / "agents" / f"{rol}.md").write_text(
            "---\n" f"name: {rol}\n" f"description: {json.dumps(tanim['aciklama'], ensure_ascii=False)}\n"
            + ("skills:\n" + "".join(f"  - {a}\n" for a in onyukle) if onyukle else "")
            + "---\n\n" f"<!-- {URETILDI}; elle değiştirme, skill-ekle.py --yenile ile yeniden üret -->\n\n{talimat}\n",
            encoding="utf-8")
        if not codex:
            continue
        toml = [f"# {URETILDI}; elle değiştirme, skill-ekle.py --yenile ile yeniden üret",
                f"name = {json.dumps(rol)}", f'description = {toml_str(tanim["aciklama"])}',
                f"developer_instructions = {toml_str(talimat)}"]
        for a in tum:
            if a not in benim:  # Codex'te allowlist yok: rol dışı proje skilleri kapatılır
                toml += ["", "[[skills.config]]",
                         f'path = {json.dumps(str((proje / ".agents" / "skills" / a / "SKILL.md").resolve()), ensure_ascii=False)}',
                         "enabled = false"]
        (proje / ".codex" / "agents" / f"{rol}.toml").write_text("\n".join(toml) + "\n", encoding="utf-8")
    for klasor, uz in ((proje / ".claude" / "agents", ".md"), (proje / ".codex" / "agents", ".toml")):
        if klasor.is_dir():
            for f in klasor.glob(f"*{uz}"):
                if (f.stem not in kilit["roller"] or (uz == ".toml" and not codex)) and URETILDI in f.read_text(encoding="utf-8"):
                    f.unlink()
            if not any(klasor.iterdir()):
                klasor.rmdir()


def blok_yaz(dosya: Path, icerik: str):
    eski = dosya.read_text(encoding="utf-8") if dosya.exists() else ""
    blok = f"{BLOK_BAS}\n{icerik}\n{BLOK_SON}"
    if (BLOK_BAS in eski) != (BLOK_SON in eski) or eski.count(BLOK_BAS) > 1:
        raise RuntimeError(f"{dosya.name}: skill-kutuphanesi işaretleri bozuk (başlangıç/bitiş eşleşmiyor); "
                           "kullanıcı metnini korumak için dokunulmadı. İşaretleri elle düzelt.")
    if BLOK_BAS in eski and BLOK_SON in eski:
        yeni = re.sub(re.escape(BLOK_BAS) + r".*?" + re.escape(BLOK_SON), lambda _: blok, eski, flags=re.S)
    else:
        yeni = (eski.rstrip() + "\n\n" if eski.strip() else "") + blok + "\n"
    dosya.write_text(yeni, encoding="utf-8")


def blok_sil(d: Path):
    if d.exists() and BLOK_BAS in d.read_text(encoding="utf-8"):
        t = re.sub(r"\n*" + re.escape(BLOK_BAS) + r".*?" + re.escape(BLOK_SON) + r"\n?", "\n",
                   d.read_text(encoding="utf-8"), flags=re.S).strip()
        d.unlink() if not t else d.write_text(t + "\n", encoding="utf-8")


def dis_blok_satirlari(kilit):
    """Talimat bloğuna eklenen dış skill satırları (bağlı / donmuş); dış skill yoksa []. Yollar '~' ile kısaltılır."""
    dis = dis_kayitlari(kilit)
    baglar = [(a, g) for a, g in sorted(dis.items()) if g["tur"] == "program-bag"]
    donmus = [(a, g) for a, g in sorted(dis.items()) if g["tur"] == "donmus"]
    out = []
    if baglar:
        out.append("Programla gelen skiller (bağ; kopya değil, programın kendi klasörü; program güncellenince kendiliğinden güncel kalır): "
                   + ", ".join(f"`{a}` ({g['program']}, {yol_goster(g['hedef'])})" for a, g in baglar))
    if donmus:
        out.append("Donmuş skiller (projenin kendi kopyası, kütüphane güncellemez): "
                   + ", ".join(f"`{a}` (kaynak: {yol_goster(g['hedef'])}, {g.get('tarih', '?')})" for a, g in donmus))
    if baglar:
        out.append("Bağlı skillerin dosyalarını düzenleme (programın dosyaları); donmuş skiller projenindir.")
    return out


def kit_blok_satirlari(kilit):
    """Talimat bloğuna eklenen kurulu kit satırları; kit yoksa []."""
    kt = kit_kayitlari(kilit)
    if not kt:
        return []
    return ["Kurulu kitler (katalog; kitteki yeni sürümler kendiliğinden uygulanmaz): "
            + ", ".join(f"`{r}` (commit `{g['commit'][:7]}`, {g.get('mod', 'iskelet')})" for r, g in sorted(kt.items()))]


def talimat_bloklari(proje: Path, kilit: dict):
    dis_satir = dis_blok_satirlari(kilit) + kit_blok_satirlari(kilit)
    if not kilit["skiller"] and not dis_satir:
        for f in ("AGENTS.md", "CLAUDE.md"):
            blok_sil(proje / f)
        return
    codex = codex_var(kilit)
    if not kilit["skiller"]:
        # yalnız dış skiller: profil satırı, tablo ve sayı cümlesi yok
        s = ["## Proje skilleri (SkillKutuphanesi)", ""] + [x for t in dis_satir for x in (t, "")]
        s += [("Skiller `.agents/skills/` (Codex) ve `.claude/skills/` (Claude) altında." if codex else
               "Skiller `.claude/skills/` altında (proje sadece Claude kullanır).")
              + " Ekleme/güncelleme/kaldırma yalnızca kütüphaneyle, kütüphanenin olduğu bilgisayarda: "
              "`python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py <proje> --guncelle`"]
        blok_yaz(proje / "CLAUDE.md", "\n".join(s))
        blok_yaz(proje / "AGENTS.md", "\n".join(s)) if codex else blok_sil(proje / "AGENTS.md")
        return
    if kilit.get("blok") == "kisa":
        # Kısa blok (token tasarrufu): tablo yok; liste kilit.json'da. --blok kisa ile seçilir, kilitte kalır.
        n = len(kilit["skiller"])
        yer = ("`.agents/skills/` (Codex) ve `.claude/skills/` (Claude)" if codex else "`.claude/skills/`")
        s = ["## Proje skilleri (SkillKutuphanesi)", "",
             f"{n} skill {yer} altında (liste, kaynak ve commit: `.skill-kutuphanesi/kilit.json`; güncelleme "
             f"{kilit['guncelleme']}"
             + (f"; roller: {', '.join(f'`{r}`' for r in kilit['roller'])}" if kilit["roller"] else "") + "). "
             "Bu skilleri elle düzenleme; ekleme/güncelleme/kaldırma yalnızca kütüphaneyle, kütüphanenin olduğu bilgisayarda: "
             "`python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py <proje> --durum` / `--guncelle`. "
             "Kütüphanesiz bilgisayarda (ör. Windows) skill ekleme/silme yapma; ihtiyacı not düş, kütüphane sahibi kurar. "
             "Kütüphane dışı, elle kurulan skiller (varsa): `.skill-kutuphanesi/elle-kurulan.json`."]
        s += [x for t in dis_satir for x in ("", t)]
        blok_yaz(proje / "CLAUDE.md", "\n".join(s))
        blok_yaz(proje / "AGENTS.md", "\n".join(s)) if codex else blok_sil(proje / "AGENTS.md")
        return
    s = ["## Proje skilleri (SkillKutuphanesi)", "",
         f"Profil: {kilit.get('profil') or '-'} · Güncelleme: {kilit['guncelleme']}", "",
         "| Skill | Roller | Kaynak |", "|---|---|---|"]
    for ad, k in sorted(kilit["skiller"].items()):
        s.append(f"| `{ad}` | {', '.join(k['roller']) or 'genel'} | {k['repo']} |")
    s += ["", "Roller: " + (", ".join(f"`{r}`" for r in kilit["roller"]) or "-"),
          ("Skiller `.agents/skills/` (Codex) ve `.claude/skills/` (Claude) altında." if codex else
           "Skiller `.claude/skills/` altında (proje sadece Claude kullanır).")
          + " Bu skilleri elle düzenleme; "
          "değişiklik/güncelleme: `python3 ~/Documents/SkillKutuphanesi/araclar/skill-ekle.py <proje> --guncelle`"]
    s += [x for t in dis_satir for x in ("", t)]
    blok_yaz(proje / "CLAUDE.md", "\n".join(s))
    if codex:
        blok_yaz(proje / "AGENTS.md", "\n".join(s))
    else:
        blok_sil(proje / "AGENTS.md")


AYAR = Path(".claude") / "settings.json"


def hesap_gizleme_hedefi(kilit):
    """Kurulu skillerden Claude hesabında aynı adlısı olanlar için gizlenecek anahtarlar."""
    hesap = hesap_skilleri()
    return sorted(f"{HESAP_ONEK}:{ad}" for ad in (set(kilit["skiller"]) | set(dis_kayitlari(kilit))) if ad in hesap)


def hesap_gizle(proje, kilit):
    """Proje .claude/settings.json → skillOverrides'ta, kurulu kütüphane skill'ini gölgeleyen hesap skill'ini "off" yapar.
    Sadece kendi eklediği anahtarları yönetir (kilit: hesap_gizlenen); kullanıcının yazdığı değere (ör. "on") dokunmaz.
    Döner: hata mesajı ya da None."""
    hedef, onceki = set(hesap_gizleme_hedefi(kilit)), set(kilit.get("hesap_gizlenen", []))
    if not hedef and not onceki:
        return None
    f = proje / AYAR
    try:
        veri = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
        if not isinstance(veri, dict):
            raise ValueError("JSON nesnesi değil")
    except (ValueError, OSError) as e:
        return f"{AYAR} okunamadı ({e}); hesap skilleri gizlenmedi, dosyayı düzelt ve --guncelle çalıştır"
    so = veri.get("skillOverrides") if isinstance(veri.get("skillOverrides"), dict) else {}
    yonetilen = set()
    for k in onceki - hedef:
        if so.get(k) == "off":
            del so[k]
    for k in hedef:
        if k not in so or (k in onceki and so[k] == "off"):
            so[k] = "off"
            yonetilen.add(k)
    if so:
        veri["skillOverrides"] = dict(sorted(so.items()))
    else:
        veri.pop("skillOverrides", None)
    if veri:
        f.parent.mkdir(parents=True, exist_ok=True)
        yeni = json.dumps(veri, ensure_ascii=False, indent=2) + "\n"
        if not f.exists() or f.read_text(encoding="utf-8") != yeni:
            f.write_text(yeni, encoding="utf-8")
    elif f.exists():
        f.unlink()
    if yonetilen:
        kilit["hesap_gizlenen"] = sorted(yonetilen)
    else:
        kilit.pop("hesap_gizlenen", None)
    return None


def hesap_gizleme_eksik(proje, kilit):
    """Gizlenmesi gerekip settings.json'da "off" olmayan hesap skilleri (kullanıcı bilerek "on" yazdıysa sayılmaz)."""
    f = proje / AYAR
    try:
        so = (json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}).get("skillOverrides") or {}
    except (ValueError, OSError, AttributeError):
        so = {}
    return [k for k in hesap_gizleme_hedefi(kilit) if k not in so] + \
           [k for k in kilit.get("hesap_gizlenen", []) if k not in hesap_gizleme_hedefi(kilit) and so.get(k) == "off"]


def tumunu_yaz(proje, kilit, skiller):
    hata = hesap_gizle(proje, kilit)
    if hata:
        print("UYARI:", hata)
    kilit_yaz(proje, kilit)
    agent_dosyalari(proje, kilit, skiller)
    talimat_bloklari(proje, kilit)


# ================================================================== öneri (tüm kütüphane taraması)
def proje_teknolojileri(proje: Path):
    tek = set()
    pj = proje / "package.json"
    if pj.exists():
        try:
            d = json.loads(pj.read_text(encoding="utf-8"))
            for k in {**d.get("dependencies", {}), **d.get("devDependencies", {})}:
                if k in TEKNOLOJI_IPUCU:
                    tek.add(TEKNOLOJI_IPUCU[k])
        except (json.JSONDecodeError, OSError):
            pass
    if any((proje / f).exists() for f in ("requirements.txt", "pyproject.toml")):
        tek.add("python")
    return tek


DURAK = {"ile", "ve", "veya", "için", "icin", "bir", "bu", "şu", "olan", "gibi", "çok", "daha", "yapmak", "yapacağız",
         "the", "and", "for", "with", "use", "using", "when", "this", "that", "from", "your", "you"}


def tr_kucuk(x):
    return x.replace("İ", "i").replace("I", "ı").lower()


def kelimeler(metin):
    metin = tr_kucuk(metin)
    ek = " ".join(v for k, v in ES_ANLAM.items() if k in metin)
    sozcuk = re.findall(r"[\w.+#-]+", metin + " " + ek, re.U)
    # Türkçe karakter içeren kelimeler İngilizce açıklamalarda eşleşmez; onlar ES_ANLAM ile çevrildi
    return {w for w in sozcuk if w not in DURAK and (len(w) > 2 or w in ("3d", "ai", "ui", "ux"))
            and re.fullmatch(r"[a-z0-9.+#-]+", w)}


def puanla(s, sorgu, teknolojiler):
    metin = " ".join([s["id"], s["aciklama"], s.get("ozet_tr", ""), s.get("kullanim_alani", ""),
                      s["kategori"].replace("-", " ")]).lower()
    eslesen = [w for w in sorgu if re.search(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])", metin)]
    tek = set(s.get("teknoloji") or s["teknoloji_oto"])
    tek_esl = tek & teknolojiler
    p = 3 * len(eslesen) + 2 * len(tek_esl)
    if p:
        p += s["degerlendirme"]["puan"] / 50
        if s["durum"] == "alternatif":
            p -= 1
        p -= {"ucretli": 2, "belirsiz": 1, "kismen": 0.5}.get(s.get("ucret"), 0)  # ücretsizler önde
        # GitHub Trending'e girmiş kaynak: konuya UYGUN skiller arasında öne al (eşleşme yoksa p=0, trend tek başına sokmaz)
        p += {"trendde": 1.5, "yakinda": 1, "gecmiste": 0.3}.get((s.get("trend") or {}).get("seviye"), 0)
        if s.get("ortusme_rolu") == "emekli" or s.get("kaynak_durumu"):
            p -= 6  # emekli / kaynakta kaldırılmış: yerine geçeni varken öne çıkmasın
    return p, eslesen, tek_esl


def kutuphane_taramasi(skiller, sorgu_metni, teknolojiler, haric_idler=(), n=12, gizli=False, kategori_basi=None):
    """TÜM skilleri puanlar. kategori_basi verilirse her kategoriden en fazla o kadar (tek kategoriye yığılmasın)."""
    sorgu = kelimeler(sorgu_metni)
    sonuc, gizli_esl = [], 0
    for s in skiller:
        p, e, t = puanla(s, sorgu, teknolojiler)
        if p <= 0 or s["id"] in haric_idler:
            continue
        if s.get("kaynak_durumu"):
            continue  # K-49: kaynağı kayıp ya da kaynakta kaldırılmış skill yeni kurulumda önerilmez (--oner, ek-aday); açık --skill yine uyarıyla kurulur
        if s.get("gizli") and not gizli:
            gizli_esl += 1
            continue
        sonuc.append((p, s, e, t))
    sonuc.sort(key=lambda x: -x[0])
    if kategori_basi:
        sayac, secilen = {}, []
        for x in sonuc:
            k = x[1]["kategori"]
            if sayac.get(k, 0) < kategori_basi:
                secilen.append(x)
                sayac[k] = sayac.get(k, 0) + 1
        return secilen[:n], len(sonuc), gizli_esl
    return sonuc[:n], len(sonuc), gizli_esl


# ================================================================== ön kontrol
def proje_yapisi_kontrol(proje, roller, rapor: Rapor):
    """Projede skill/agent klasörleri güvenli mi? (symlink ile başka yere/globale gidiyor mu, rol adları geçerli mi)"""
    korunan = [g.resolve() for g in GLOBAL_KLASORLER.values()] + [KOK.resolve(), (Path.home() / ".openmontage").resolve()] + arac_korunan_yollar()
    hedefler = {}
    for rel in (".agents/skills", ".claude/skills", ".claude/agents", ".codex/agents", ".agents", ".claude", ".codex"):
        p = proje / rel
        if p.is_symlink() or p.exists():
            gercek = p.resolve()
            if any(gercek == k or k in gercek.parents for k in korunan):
                rapor.ekle("HATA", "global-baglanti", f"{rel} -> {gercek}: global/korunan bir klasöre gidiyor; işlem yapılmaz")
            elif proje.resolve() not in [gercek, *gercek.parents]:
                rapor.ekle("HATA", "proje-disi-baglanti", f"{rel} -> {gercek}: proje dışına gidiyor; işlem yapılmaz")
            hedefler[rel] = gercek
    if ".agents/skills" in hedefler and hedefler.get(".agents/skills") == hedefler.get(".claude/skills"):
        rapor.ekle("HATA", "ayni-klasor", ".claude/skills ve .agents/skills aynı klasöre gidiyor (symlink); "
                   "araç sürümleri ve bağlantılar bozulur. İkisini ayrı klasör yap.")
    for rol in roller:
        if not ROL_ADI.match(rol or ""):
            rapor.ekle("HATA", "gecersiz-rol-adi", f"'{rol}': rol adı sadece küçük harf, rakam ve - içerebilir")
            continue
        for dosya in (proje / ".claude" / "agents" / f"{rol}.md", proje / ".codex" / "agents" / f"{rol}.toml"):
            if dosya.exists() and URETILDI not in dosya.read_text(encoding="utf-8", errors="replace"):
                rapor.ekle("HATA", "kendi-agent-dosyan", f"{dosya.relative_to(proje)} senin dosyan (kütüphane üretmedi); "
                           "üzerine yazılmaz. Rolü farklı adla ekle ya da dosyayı yeniden adlandır")


def sabit_yol_satirlari(rapor: Rapor, s, ad, skiller, kilit, kur_listesi, adlar, kurulacak_idler, dis_adlari=frozenset()):
    """Bir skill'in kardeş ve sabit yol bağımlılıklarının ön kontrol satırları. ../<kardeş>/ bağlantıları (kardes_bagimliliklari) ile sabit yollar
    (ortak.yol_degerlendir) AYNI kardeşe işaret ederse kardeş KİMLİĞE göre tek satırda anılır: kurulmuyorsa tek 'kardes-eksik', kuruluyorsa tek
    'kardes-yol' (parçalar birleşir; yalnız GERÇEKTEN çevrilecek yollar sayılır, sıfırsa satır yok). Aynı ad başka kimlik: 'kardes-farkli-kaynak'.
    dis_adlari: projede program bağı/donmuş olarak kayıtlı ya da bu işlemde isteneni dış skill adları (küçük harf); ../<ad>/ ile anılan kardeş
    böyle bir adsa kurulu sayılır (bağ ya da donmuş klasör aynı adla projede durur)."""
    farkli = []
    harita = kardes_haritasi(s, skiller, kilit, kur_listesi, adlar, farkli)
    farkli_anahtar = {x[0] for x in farkli}
    eksik, yol = set(), {}  # kardeş kimliği -> bildirildi / satır parçaları
    dis_kid = set()  # ../<kardeş>/ ile anılan ve projede dış skill (bağ/donmuş) olarak bulunan kardeşler
    for kad, (kurulum, kurulu) in harita.items():
        if kad.startswith(GENEL_KARDES) or kad in farkli_anahtar:
            continue
        bilgi = s["kardes_bagimliliklari"][kad]
        if not kurulu and kad.casefold() in dis_adlari:
            dis_kid.add(bilgi["id"])
            continue
        if not kurulu:
            rapor.ekle("UYARI", "kardes-eksik", f"{ad}: {bilgi['dosya_sayisi']} dosyası ../{kad}/ bağlantısıyla kardeş "
                       f"skill'e dayanıyor ama '{kad}' projeye kurulmuyor; bağlantılar boşa düşer (ekle: --skill {bilgi['id']})")
            eksik.add(bilgi["id"])
        elif kurulum != kad:
            yol.setdefault(bilgi["id"], []).append(f"../{kad}/ bağlantıları projedeki ada çevrilecek: ../{kurulum}/")
    bildirilen = set()
    for anahtar, kid, baska in farkli:
        if kid in bildirilen:  # ../<kardeş>/ ve sabit yol aynı kardeşe işaret edebilir: tek uyarı
            continue
        bildirilen.add(kid)
        rapor.ekle("UYARI", "kardes-farkli-kaynak", f"{ad}: {anahtar.replace(GENEL_KARDES, '')} kardeşi {kid} olmalı, ama projede/kurulumda aynı adlı "
                   f"BAŞKA bir skill var ({baska}); yol çevrilmez, kardeş {kid} ayrıca eklenmeli (--skill {kid})")
        eksik.add(kid)
    d = yol_degerlendir(s, skiller, kurulacak_idler=kurulacak_idler)
    for hedef, bilgi in d["kardesler"].items():
        if hedef.casefold() in dis_adlari and all(b["tur"] == "kardes-goreli" for b in bilgi["bulgular"]):
            dis_kid.add(bilgi["id"])  # yalnız göreli ../<kardeş>/ yolları: bağ/donmuş klasör aynı adla orada durur
    for (sv, kod, govde), kid in zip(d["satirlar"], d.get("satir_kardes") or [None] * len(d["satirlar"])):
        if kod == "kardes-yol":
            continue  # aşağıda yalnız gerçekten çevrilenleri sayarak yeniden üretilir
        yok_kardes = kod == "kardes-eksik" and "dosya arşivde yok" not in govde  # "kardeş projeye kurulmuyor" satırı (eksik dosya satırı ayrıdır)
        if yok_kardes and (kid in eksik or kid in dis_kid):
            continue  # bu kardeş zaten bildirildi ya da projede dış skill olarak var
        if yok_kardes and kid is not None:
            eksik.add(kid)
        rapor.ekle(sv if kod in YOL_KODLARI else "UYARI", kod, f"{ad}: {govde}")
    for hedef, bilgi in sorted(d["kardesler"].items()):
        if not bilgi["kurulu"] or bilgi["id"] in eksik:
            continue
        n = sum(1 for b in d.get("cevrilecek_kardes", []) if b["kardes_id"] == bilgi["id"])
        if n and (GENEL_KARDES + hedef) in harita:
            yol.setdefault(bilgi["id"], []).append(f"{hedef} ({bilgi['id']}) kardeşine {n} sabit yol, kardeşin proje içi yoluna çevrilecek")
    for parcalar in yol.values():
        rapor.ekle("BİLGİ", "kardes-yol", f"{ad}: " + "; ".join(parcalar))


def on_kontrol(proje, kilit, plan, roller, skiller, rapor: Rapor, zorla=False, dis_liste=None):
    """plan: [(skill kaydı, rol|None)] -> (kur_listesi {id: (s, roller)}, adlar {id: kurulum adı})"""
    proje_yapisi_kontrol(proje, roller, rapor)
    kur_listesi, adlar, hedef_adlar = {}, {}, {}
    for s, rol in plan:
        kur_listesi.setdefault(s["id"], (s, set()))[1].add(rol)
    for sid, (s, _) in kur_listesi.items():
        adlar[sid] = ad = kurulum_adi(s, kilit)
        if ad in hedef_adlar:
            rapor.ekle("HATA", "isim-cakismasi", f"{sid} ve {hedef_adlar[ad]} aynı adla ({ad}) kurulacaktı")
        hedef_adlar[ad] = sid

    # sabit yol taraması için "kurulacak ya da projede kurulu" kimlikler (kardeş kuruluyor mu?)
    kurulacak_idler = set(kur_listesi) | {x["id"] for k in kilit["skiller"].values() if (x := kaynak_bul(skiller, k))}
    dis_adlari = {k.casefold() for k in dis_kayitlari(kilit)} | {it["ad"].casefold() for it in (dis_liste or [])}  # bağ/donmuş kardeş: kilitte ya da bu işlemde
    for sid, (s, rol_kumesi) in kur_listesi.items():
        ad = adlar[sid]
        onceki = kilit["skiller"].get(ad)
        dis_ayni = next((k for k in dis_kayitlari(kilit) if k.casefold() == ad.casefold()), None)
        if dis_ayni:  # projede bağ/donmuş olarak kayıtlı slot: --zorla ile bile değiştirilmez
            rapor.ekle("HATA", "dis-ad-cakismasi", f"{ad}: projede {dis_ayni} adıyla programdan bağlı ya da donmuş bir skill var; "
                       "iki tür aynı adı taşıyamaz (önce --kaldir)")
        for yer in (proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad):
            if (yer.exists() or yer.is_symlink()) and not onceki and not dis_ayni:
                rapor.ekle("HATA", "projede-kendi-skillin",
                           f"{yer.relative_to(proje)} zaten var ve kütüphaneden gelmemiş; üzerine yazılmaz "
                           f"(--zorla ile yedeklenip değiştirilir)")
        if onceki and (repo_guncel(onceki.get("repo")), onceki.get("kaynak_yol", s["kaynak_yol"])) != (s["repo"], s["kaynak_yol"]):
            rapor.ekle("HATA", "farkli-kaynak", f"{ad} projede {onceki.get('repo')}:{onceki.get('kaynak_yol', '?')} kaynağından "
                       f"kurulu; {s['repo']}:{s['kaynak_yol']} ile değiştirilmez (önce --kaldir)")
        canli = canli_global(s)
        if onceki and ad == s["ad"] and any(v == "farkli" for v in canli.values()):
            rapor.ekle("UYARI", "global-cakisma-yeni", f"{ad}: globale sonradan aynı adlı FARKLI skill eklenmiş; Claude'da global "
                       "sürüm kazanır. Kütüphane sürümü için: --kaldir ve yeniden ekle (ekli adla kurulur)")
        if onceki and elle_degismis(proje, ad, onceki):
            rapor.ekle("HATA", "elle-degistirilmis", f"{ad} projede elle değiştirilmiş; ezilmez (--zorla: yedekle ve ez)")
        if ad != s["ad"]:
            neden = "global klasörde aynı adlı FARKLI skill var (kişisel skill proje skill'ini ezerdi)" \
                if "--kutuphane" in ad else "aynı adlı alternatif sürüm"
            rapor.ekle("BİLGİ", "ekli-ad", f"{s['id']} -> `{ad}` adıyla kurulacak: {neden}"
                       + ("; skill içindeki kendi yol referansları da düzeltilecek" if s.get("yol_bagimliligi") else ""))
        if any(v == "ayni" for v in canli.values()):
            rapor.ekle("BİLGİ", "globalde-ayni", f"{ad}: bilgisayarında birebir aynısı global olarak da var (sorun değil)")
        if ad in hesap_skilleri():
            rapor.ekle("BİLGİ", "hesap-cakismasi", f"{ad}: Claude hesabında aynı adlı skill var (`{HESAP_ONEK}:{ad}`); agent "
                       f"onu seçerdi. Bu projede gizlenecek: {AYAR} → skillOverrides \"{HESAP_ONEK}:{ad}\": \"off\" "
                       "(hesaba ve globale dokunulmaz; hesaptakini istersen değeri \"on\" yap)")
        u = s["uyum"]
        if not codex_var(kilit):
            pass
        elif u["codex"] == "uyarlanabilir":
            rapor.ekle("UYARI", "codex-uyum", f"{ad}: {u['not'][:220]}")
        elif u["codex"] == "konu-claude-ozel":
            rapor.ekle("UYARI", "claude-ozel", f"{ad}: konu Claude Code'a özel; Codex'te sadece kavram referansı")
        if s.get("varyantlar"):
            rapor.ekle("BİLGİ", "arac-surumu", f"{ad}: " + ", ".join(s["varyantlar"]) + " için ayrı uyarlanmış sürüm kurulacak")
        adaslar = [x for x in skiller if x["ad"] == s["ad"] and x["id"] != s["id"]]
        if adaslar:  # aynı ad her zaman aynı iş değildir: hangi kaynağın kurulduğu ve diğerleri açıkça görünsün
            rapor.ekle("BİLGİ", "ayni-ad", f"'{s['ad']}' adında {len(adaslar) + 1} skill var; kurulan: {s['id']} ({s['repo']}, "
                       f"{s['durum']}). Diğerleri: " + ", ".join(f"{x['id']} ({x['repo']})" for x in adaslar[:6])
                       + ". Başka sürüm için tam kimliği yaz (--skill <ad@kaynak>)")
        if s["durum"] == "alternatif":
            tercih = next((x for x in skiller if x["ad"] == s["ad"] and x["durum"] == "tercih"), None)
            rapor.ekle("UYARI", "alternatif-surum", f"{s['id']} alternatif sürüm; tercih edilen: {tercih['id'] if tercih else '?'}")
            if tercih and tercih["id"] in kur_listesi:
                rapor.ekle("UYARI", "ayni-skill-iki-surum", f"{s['ad']} için hem tercih hem alternatif kuruluyor; agent karışabilir")
        if s["lisans"] in ("belirtilmemiş", "NOASSERTION"):
            rapor.ekle("UYARI", "lisans", f"{ad}: lisans belirtilmemiş ({s['repo']}); ticari kullanımda dikkat")
        if s["degerlendirme"]["not"] == "D":
            rapor.ekle("UYARI", "dusuk-puan", f"{ad}: değerlendirme {s['degerlendirme']['puan']}/100 (D)")
        duz = s.get("aciklama_duzeltme") or {}
        for y in s.get("yapisal_sorunlar", []):
            if tetikleme_sorunu(y) and not duz.get("description") and not oto_onarilir(y):
                rapor.ekle("UYARI", "tetiklenmez", f"{ad}: {y} -> kurulunca doğru durumda tetiklenmez "
                           "(registry.json'a aciklama_duzeltme yaz: rehber/03-yeni-skill-ekleme.md)")
            elif tetikleme_sorunu(y):
                rapor.ekle("BİLGİ", "yapi", f"{ad}: {y} -> kurulan kopyada düzeltilir")
            else:
                rapor.ekle("UYARI" if "disable-model" in y else "BİLGİ", "yapi", f"{ad}: {y}")
        if s.get("yama"):
            rapor.ekle("BİLGİ", "yama", f"{ad}: kurulan kopyada yamalı dosya: {', '.join(s['yama']['dosyalar'])} "
                       f"({s['yama'].get('neden', '')}); arşivdeki orijinal değişmez")
        if duz.get("description"):
            rapor.ekle("BİLGİ", "aciklama-onarim", f"{ad}: description kurulan kopyada düzeltilecek "
                       f"({duz.get('neden', 'aciklama_duzeltme')}); arşivdeki orijinal değişmez")
        if s.get("kirik_baglantilar"):
            rapor.ekle("UYARI", "kirik-baglanti", f"{ad}: SKILL.md'nin gösterdiği {len(s['kirik_baglantilar'])} dosya "
                       f"kaynakta da yok ya da arşive alınmadı: {', '.join(s['kirik_baglantilar'][:5])}")
        sabit_yol_satirlari(rapor, s, ad, skiller, kilit, kur_listesi, adlar, kurulacak_idler, dis_adlari)
        if s.get("ucret") == "ucretli":
            rapor.ekle("UYARI", "ucretli", f"{ad}: ÜCRETLİ — ücret ödemeden kullanılamaz — {s.get('ucret_notu', '')}")
        elif s.get("ucret") == "kismen":
            rapor.ekle("BİLGİ", "kismen-ucretli", f"{ad}: ücret ödemeden kullanılabilir, bazı yollar ücretli — {s.get('ucret_notu', '')}")
        elif s.get("ucret") == "belirsiz":
            rapor.ekle("UYARI", "ucret-belirsiz", f"{ad}: ücret durumu sınıflandırılmadı ({s.get('ucret_notu', '')})")
        if s.get("ortusme_rolu") == "emekli" and s.get("kaynak_durumu") != "kaynakta-kaldirildi":
            rapor.ekle("UYARI", "emekli", f"{ad}: eski/emekli bir sürüm (yerine geçeni var); inceleme notu: "
                       f"{(s.get('kalite_notu') or '')[-160:]}")
        if s.get("kaynak_durumu") == "kaynakta-kaldirildi":
            rapor.ekle("UYARI", "kaynakta-kaldirildi", f"{ad}: geliştiricisi bu skill'i {s.get('kaldirilma_tarihi', '?')} "
                       f"tarihli güncellemede kaldırdı ({s['repo']}); arşivdeki son sürüm kuruluyor, artık güncellenmeyecek")
        elif s.get("kaynak_durumu") == "kayip":
            rapor.ekle("UYARI", "kaynak-kayip", f"{ad}: kaynak repo erişilemiyor ({s['repo']}); arşivdeki son sürüm kuruluyor")
        if s.get("bagimlilik"):
            rapor.ekle("UYARI", "bagimlilik", f"{ad}: {s['bagimlilik']}")
        if s.get("notlar"):
            rapor.ekle("BİLGİ", "inceleme-notu", f"{ad}: {s['notlar']}")
        if s.get("gizli"):
            rapor.ekle("BİLGİ", "gizli-katalog", f"{ad}: varsayılan listede gizli kategoriden ({s['kategori']})")
        if s.get("ust_skill"):
            rapor.ekle("BİLGİ", "alt-skill", f"{ad}: '{s['ust_skill']}' skill'inin alt klasörü; tek başına da çalışır")
        if s.get("inceleme") == "yeniden-incelenecek":
            rapor.ekle("UYARI", "inceleme-eskidi", f"{ad}: içeriği son güncellemede değişti, inceleme notları eski sürüme ait "
                       "(rehber/07-kategori-inceleme.md ile yeniden incele)")
        if s.get("inceleme", "otomatik") == "otomatik":
            rapor.ekle("BİLGİ", "incelenmedi", f"{ad}: henüz elle incelenmedi (otomatik bilgilerle)")

    # rol bazında bağlam ve örtüşme
    for rol in roller:
        rs = [s for s, rk in kur_listesi.values() if rol in rk]
        eski = [kaynak_bul(skiller, k) for a, k in kilit["skiller"].items() if rol in k["roller"]]
        rs += [x for x in eski if x and x["id"] not in {y["id"] for y in rs}]
        kb = sum(x["skill_md_kb"] for x in rs)
        if len(rs) > SINIR_CLAUDE_ONYUKLEME:
            rapor.ekle("HATA", "onyukleme-siniri", f"rol {rol}: {len(rs)} skill > Claude alt-agent sınırı {SINIR_CLAUDE_ONYUKLEME}")
        elif len(rs) > SINIR_ROL_SKILL or kb > SINIR_ROL_KB:
            rapor.ekle("UYARI", "baglam-yuku", f"rol {rol}: {len(rs)} skill, {kb:.0f} KB SKILL.md önyüklenecek "
                       f"(öneri ≤{SINIR_ROL_SKILL} skill, ≤{SINIR_ROL_KB} KB); agent bağlamı dolabilir")
        gruplar = {}
        for x in rs:
            if x.get("ortusme_grubu"):
                gruplar.setdefault((x["ortusme_grubu"], x.get("ortusme_rolu")), []).append(x["id"])
        for (g, r), ids in gruplar.items():
            if r == "birincil" and len(ids) > 1:
                rapor.ekle("UYARI", "ortusme", f"rol {rol}: '{g}' grubundan {len(ids)} birincil skill: {', '.join(ids)}")
        surumler = {}
        for x in rs:
            surumler.setdefault(x["ad"], []).append(x["id"])
        for a, ids in surumler.items():
            if len(ids) > 1:
                rapor.ekle("UYARI", "ortusme", f"rol {rol}: aynı skill'in birden fazla sürümü: {', '.join(ids)}")
    return kur_listesi, adlar


def kapsam_raporu(proje, roller, kur_listesi, skiller, rapor: Rapor, ek_sorgu=""):
    """Kütüphanedeki tüm skilleri tarar; kurulmayan ama ilgili adayları raporlar (hiçbiri görmezden gelinmez)."""
    teknolojiler = proje_teknolojileri(proje)
    secilen = set(kur_listesi)
    gorunur = sum(1 for s in skiller if not s.get("gizli"))
    rapor.ekle("BİLGİ", "tarama", f"Kütüphanedeki {len(skiller)} skill tarandı (görünür {gorunur}, gizli "
               f"{len(skiller) - gorunur}); projede tespit edilen teknoloji: {', '.join(sorted(teknolojiler)) or '-'}")
    for rol in roller or [None]:
        tanim = json_oku(ROLLER / f"{rol}.json") if rol else None
        metin = ((tanim or {}).get("aciklama", "") + " " + (tanim or {}).get("gorev", "") + " " + ek_sorgu).strip()
        if not metin and not teknolojiler:
            continue
        adaylar, n, gizli_n = kutuphane_taramasi(skiller, metin, teknolojiler, haric_idler=secilen, n=6, kategori_basi=2)
        if adaylar:
            rapor.ekle("BİLGİ", f"ek-aday{':' + rol if rol else ''}",
                       f"{n} ilgili skill daha var; ilk {len(adaylar)}: " +
                       ", ".join(f"{s['id']} ({s['kategori'].split('/')[1]}, {s['degerlendirme']['puan']})" for _, s, _, _ in adaylar)
                       + (f" · gizli katalogda {gizli_n} eşleşme" if gizli_n else ""))


# ================================================================== komutlar
def istek_coz(a, skiller):
    roller, istek, profil = list(a.rol or []), [], None
    if a.profil:
        profil = json_oku(PROFILLER / f"{a.profil}.json")
        if not profil:
            sys.exit(f"Profil yok: {a.profil}. Mevcut: {', '.join(sorted(p.stem for p in PROFILLER.glob('*.json')))}")
        roller += profil["roller"]
        istek += [(x, a.rol_adi) for x in profil.get("ek_skiller", [])]
    if a.planlayici:
        roller.append("planlayici")
    roller = list(dict.fromkeys(roller))
    for r in roller:
        t = json_oku(ROLLER / f"{r}.json")
        if not t:
            sys.exit(f"Rol yok: {r}. Mevcut: {', '.join(sorted(p.stem for p in ROLLER.glob('*.json')))}")
        istek += [(x, r) for x in t["cekirdek"]] + ([(x, r) for x in t.get("opsiyonel", [])] if a.opsiyonel else [])
    if a.rol_adi and a.rol_adi not in roller:
        roller.append(a.rol_adi)
    istek += [(x, a.rol_adi) for x in (a.skill or [])]
    plan, bulunamayan = [], []
    for anahtar, rol in istek:
        s = bul(skiller, anahtar)
        (plan.append((s, rol)) if s else bulunamayan.append(anahtar))
    return plan, roller, (a.profil if profil else None), bulunamayan


def onay(a, rapor):
    kesin = sorted({k for s, k, _ in rapor.satirlar if s == "HATA" and k in ZORLANAMAZ})
    if kesin:
        print(f"\nDURDU: şu hatalar --zorla ile de geçilemez: {', '.join(kesin)}")
        return False
    if rapor.say("HATA") and not a.zorla:
        print(f"\nDURDU: {rapor.say('HATA')} hata var. Düzelt ya da (yedek alınarak) --zorla ile geç.")
        return False
    if a.kuru:
        print("\n[kuru] Hiçbir şey değiştirilmedi.")
        return False
    if rapor.say("UYARI") and not a.evet:
        if sys.stdin.isatty():
            return input(f"\n{rapor.say('UYARI')} uyarı var. Devam edilsin mi? [e/H] ").strip().lower() in ("e", "evet", "y")
        print(f"\nDURDU: {rapor.say('UYARI')} uyarı var. Raporu kullanıcıya göster; onaylarsa --evet ile tekrar çalıştır.")
        return False
    return True


def kardes_adlari(harita):
    return {k: v[0] for k, v in harita.items()}


def kayit_guncelle(kilit, proje, ad, s, roller=(), kardes=None, skiller=None):
    k = kilit["skiller"].setdefault(ad, {"roller": []})
    k.update(id=s["id"], repo=s["repo"], kaynak_yol=s["kaynak_yol"], commit=s["commit"], klasor_hash=s["klasor_hash"],
             bolum="arsiv", varyantlar=sorted(s.get("varyantlar") or {}), kurulu_hash=kurulu_hash(proje, ad))
    iz = onarim_izi(s, skiller)
    if iz:
        k["onarim"] = iz
    else:
        k.pop("onarim", None)
    if kardes is not None:
        k["kardes"] = kardes_adlari(kardes)
    for r in roller:
        if r and r not in k["roller"]:
            k["roller"].append(r)


def claude_baglanti_saglam(proje, ad):
    c = proje / ".claude" / "skills" / ad
    return (c / "SKILL.md").exists()


def kurulum_eksik(proje, ad, kilit):
    """Kurulum projenin araç düzenine uymuyor mu? (eksik kopya, bozuk bağlantı, sadece-Claude'da symlink/fazla .agents kopyası)"""
    if not claude_baglanti_saglam(proje, ad):
        return True
    if codex_var(kilit):
        c = proje / ".claude" / "skills" / ad
        varyant = "claude" in (kilit["skiller"].get(ad, {}).get("varyantlar") or [])
        return kurulu_hash(proje, ad)["codex"] is None or (not varyant and not c.is_symlink())
    return (proje / ".claude" / "skills" / ad).is_symlink() or (proje / ".agents" / "skills" / ad).exists()


def guvenli_islem(proje, yedek, islem):
    """islem() hata verirse yedekten geri alır."""
    try:
        islem()
    except Exception as e:  # noqa: BLE001
        geri_yukle(proje, yedek)
        sys.exit(f"HATA: {e}\nYapılan değişiklikler geri alındı ({yedek.name}).")


def ekle(a, proje, skiller):
    kilit = kilit_oku(proje)
    onceki = list(kilit.get("araclar", ARACLAR["ikisi"]))
    onceki_duzen = duzen_adi(kilit)
    if a.arac:
        duzen_uygula(kilit, a.arac)
    if a.blok:
        kilit["blok"] = a.blok
    plan, roller, profil, bulunamayan = istek_coz(a, skiller)
    rapor = Rapor()
    for b in bulunamayan:
        rapor.ekle("HATA", "bulunamadi", f"kütüphanede yok: {b} (ara: skill-ekle.py --ara {b})")
    fihrist_liste, arsiv_yonlendirme, fihrist_hatalar, fihrist_bilgiler = fihrist_istek_coz(a, skiller)
    for kod, m in fihrist_hatalar:
        rapor.ekle("HATA", kod, m)
    for kod, m in fihrist_bilgiler:
        rapor.ekle("BİLGİ", kod, m)
    if arsiv_yonlendirme:
        plan += arsiv_yonlendirme
    kit_liste, kit_parcalar, kit_hatalar = kit_istek_coz(a)
    for kod, m in kit_hatalar:
        rapor.ekle("HATA", kod, m)
    dis_liste, dis_hatalar = dis_istek_coz(a)
    for kod, m in dis_hatalar:
        rapor.ekle("HATA", kod, m)
    kur_listesi, adlar = on_kontrol(proje, kilit, plan, roller, skiller, rapor, dis_liste=dis_liste)
    dis_liste = dis_on_kontrol(proje, kilit, dis_liste, set(adlar.values()), rapor)
    dis_adlari = [it["ad"] for it in dis_liste]
    fihrist_hazir = fihrist_on_kontrol(proje, kilit, fihrist_liste, set(adlar.values()), {x.casefold() for x in dis_adlari}, rapor)
    kit_hazir = kit_on_kontrol(proje, kilit, kit_liste, kit_parcalar, rapor)
    arac_satirlari(proje, kilit, rapor, secim=a.arac)
    fihrist_adlari = [ad for _, ad in fihrist_hazir]
    eskiler = sorted(set(kilit["skiller"]) - set(adlar.values()) - set(fihrist_adlari))
    eskiler = sorted(set(eskiler) | (set(dis_kayitlari(kilit)) - set(dis_adlari))
                     | {sk for kg in kit_kayitlari(kilit).values() for sk in (kg.get("skiller") or []) if dis_ad_gecerli(sk)})
    if a.arac and kilit["araclar"] != onceki and eskiler:
        rapor.ekle("HATA", "arac-karisik", f"--arac {ARAC_TAKMA.get(a.arac, a.arac)} verildi ama projede {len(eskiler)} skill {onceki_duzen} "
                   f"düzeninde kurulu ({', '.join(eskiler)}). Önce yalnız --arac {ARAC_TAKMA.get(a.arac, a.arac)} --kuru, sonra "
                   f"--arac {ARAC_TAKMA.get(a.arac, a.arac)} --evet çalıştır; ardından skill ekle.")
    yalniz_dis = bool((getattr(a, "program_skill", None) or getattr(a, "dondur", None)) and not plan and not fihrist_liste and not kit_liste)
    if not yalniz_dis:  # yalnız bağ/dondurma çalışmasında kütüphane adayı listelenmez
        kapsam_raporu(proje, roller, kur_listesi, skiller, rapor, a.oner or "")
    print(f"Proje: {proje}\nKurulacak: {len(kur_listesi)} skill"
          + (f" + {len(fihrist_hazir)} fihrist" if fihrist_hazir else "")
          + (f" + {len(kit_hazir)} kit" if kit_hazir else "")
          + f" · Roller: {', '.join(roller) or '-'}")
    for sid, (s, rk) in kur_listesi.items():
        print(f"  {sid:42s} -> {adlar[sid]:42s} [{', '.join(sorted(r for r in rk if r)) or 'genel'}]")
    for it, ad in fihrist_hazir:
        print(f"  [fihrist] {it['repo']}:{it['yol']} -> {ad}  (commit {it['fihrist_commit'][:7]})")
    for it in kit_hazir:
        print(f"  [kit] {it['repo']} ({it['ad']}, mod: {it['mod']})")
    yeni_baglar = [it for it in dis_liste if it["tur"] == "program-bag" and not it.get("var")]
    yeni_donmus = [it for it in dis_liste if it["tur"] == "donmus" and not it.get("var")]
    yer = ".agents/skills" if codex_var(kilit) else ".claude/skills"
    if yeni_baglar:
        print(f"Programla gelen (bağ): {len(yeni_baglar)}")
        for it in yeni_baglar:
            print(f"  {it['program']}:{it['ad']}  -> {yer}/{it['ad']} -> {yol_goster(it['hedef'])}  "
                  f"({it['program']} {surum_metni(it['surum'], it['surum_turu'])})")
    if yeni_donmus:
        print(f"Dondurulacak (projenin kendi kopyası): {len(yeni_donmus)}")
        for it in yeni_donmus:
            print(f"  {yol_goster(it['kaynak'])} -> {yer}/{it['ad']}  ({it['tarama']['dosya']} dosya, {it['kb']} KB)")
    print("\nÖN KONTROL:")
    rapor.yazdir()
    if getattr(a, "rapor", False) or (a.kuru and (fihrist_hazir or kit_hazir)):
        print(proje_raporu_uret(proje, kilit, skiller, rapor, kur_listesi=kur_listesi, adlar=adlar,
                                fihrist_hazir=fihrist_hazir, kit_hazir=kit_hazir, dis_liste=dis_liste,
                                sorgu=a.oner or "", roller=roller))
    if not onay(a, rapor):
        return 2

    # Ağ ve geçici klasör aşaması (yalnız --evet / onay sonrası; ortak kural 7 ve 8)
    gecici_kok = None
    fihrist_hazirlanan = []  # [(it, ad, commit, gecici_skil, inceleme)]
    kit_hazirlanan = []      # [(it, commit, klon_dir, inceleme)]
    try:
        if fihrist_hazir or kit_hazir:
            gecici_kok = Path(tempfile.mkdtemp(prefix="skill-kutuphanesi-kurulum-"))
            ag_rapor = Rapor()
            for idx, (it, ad) in enumerate(fihrist_hazir):
                try:
                    commit, skil_dir = kaynak_indir(it["repo"], gecici_kok / f"fh-{idx}", alt_yol=it["yol"])
                except (KaynakErisimHatasi, KaynakYolYokHatasi) as e:
                    ag_rapor.ekle("HATA", "kaynak-erisim", str(e))
                    continue
                inc = gecici_skil_incele(skil_dir, it["repo"], it["yol"], commit, ad, it.get("onceki_inceleme"))
                for sv, kod, m in inc["satirlar"]:
                    ag_rapor.ekle(sv, kod, m)
                    rapor.ekle(sv, kod, m)
                if not any(sv == "HATA" for sv, _, _ in inc["satirlar"]):
                    fihrist_hazirlanan.append((it, ad, commit, skil_dir, inc))
            mevcut_skil_ad = set(adlar.values()) | set(fihrist_adlari) | set(dis_adlari)
            mevcut_kit_dosya = set()
            for idx, it in enumerate(kit_hazir):
                try:
                    commit, klon_dir = kaynak_indir(it["repo"], gecici_kok / f"kit-{idx}", alt_yol=None)
                except KaynakErisimHatasi as e:
                    ag_rapor.ekle("HATA", "kaynak-erisim", str(e))
                    continue
                inc = gecici_kit_incele(klon_dir, it["kit"], proje, kilit, it["mod"], it["parcalar"], mevcut_skil_ad,
                                        mevcut_dosyalar=mevcut_kit_dosya)
                for sv, kod, m in inc["satirlar"]:
                    ag_rapor.ekle(sv, kod, m)
                    rapor.ekle(sv, kod, m)
                if not any(sv == "HATA" for sv, _, _ in inc["satirlar"]):
                    mevcut_skil_ad |= {sk["ad"] for sk in inc["skiller"]}
                    mevcut_kit_dosya |= set(inc["dosyalar"])
                    kit_hazirlanan.append((it, commit, klon_dir, inc))
            if ag_rapor.satirlar:
                print("\nGEÇİCİ KLASÖR İNCELEMESİ:")
                ag_rapor.yazdir()
            if ag_rapor.say("HATA"):
                print(f"\nDURDU: geçici klasör aşamasında {ag_rapor.say('HATA')} hata oluştu; projeye hiçbir şey yazılmadı.")
                return 2
            guv_uyari = [(sv, kod, m) for sv, kod, m in ag_rapor.satirlar if sv == "UYARI" and kod in GUVENLIK_ONAY_KODLARI]
            if guv_uyari and not getattr(a, "guvenlik_onay", False):
                if not a.evet and sys.stdin.isatty():
                    cevap = input(f"\nGeçici klasör incelemesinde {len(guv_uyari)} güvenlik uyarısı bulundu (--kuru raporunda görünmemişti). "
                                  "Yine de kurulsun mu? [e/H] ").strip().lower()
                    if cevap not in ("e", "evet", "y"):
                        print("\nDURDU: güvenlik uyarıları onaylanmadı; projeye hiçbir şey yazılmadı.")
                        return 2
                else:
                    print(f"\nDURDU: geçici klasör incelemesinde {len(guv_uyari)} güvenlik uyarısı bulundu (--kuru raporunda görünmemişti); "
                          "projeye hiçbir şey yazılmadı. Raporu inceleyip yine de kurmak istiyorsan --evet --guvenlik-onay ile tekrar çalıştır.")
                    return 2

        ek_yedek = []
        kit_skil_adlari = []
        for _, _, _, inc in kit_hazirlanan:
            ek_yedek += inc["dosyalar"]
            kit_skil_adlari += [sk["ad"] for sk in inc["skiller"]]
        yedek = yedekle(proje, list(adlar.values()) + fihrist_adlari + dis_adlari + kit_skil_adlari, "ekle", ek_hedefler=ek_yedek)
        olculen_bayt = [0]

        def islem():
            for sid, (s, rk) in kur_listesi.items():
                ad = adlar[sid]
                k = kilit["skiller"].get(ad)
                kardes = kardes_haritasi(s, skiller, kilit, kur_listesi, adlar)
                if k and not a.zorla and elle_degismis(proje, ad, k):
                    # savunma (normalde on_kontrol zaten HATA verir, bu yüzden buraya inilmez; test.py on_kontrol'ü atlatarak sınar): elle değiştirilmiş kopya yeniden kurulmaz ve yeni onarım izi / kaynak damgası YAZILMAZ
                    print(f"  ! {ad}: projede elle değiştirilmiş; yeniden kurulmadı, kilitteki kayıt aynen bırakıldı (--zorla: yedekle ve ez)")
                    k["roller"] = list(dict.fromkeys(k["roller"] + [r for r in rk if r]))
                    continue
                if (not k or k["klasor_hash"] != s["klasor_hash"] or a.zorla or k.get("kardes", {}) != kardes_adlari(kardes)
                        or kurulum_eksik(proje, ad, kilit) or k.get("onarim") != onarim_izi(s, skiller)):
                    for u in kur(s, proje, ad, kardes, codex_var(kilit), skiller):
                        print(f"  ! {u}")
                    print(f"  + {ad}")
                kayit_guncelle(kilit, proje, ad, s, rk, kardes, skiller)
                hedef_k = proje / (".agents/skills" if codex_var(kilit) else ".claude/skills") / ad
                if hedef_k.is_dir():
                    olculen_bayt[0] += sum(p.stat().st_size for p in onemli_dosyalar(hedef_k))
            for it, ad, commit, skil_dir, inc in fihrist_hazirlanan:
                for u in fihrist_skil_kur(skil_dir, proje, ad, it, codex_var(kilit)):
                    print(f"  ! {u}")
                hedef_k = proje / (".agents/skills" if codex_var(kilit) else ".claude/skills") / ad
                bayt = sum(p.stat().st_size for p in onemli_dosyalar(hedef_k)) if hedef_k.is_dir() else inc["toplam_bayt"]
                olculen_bayt[0] += bayt
                fk = kilit["skiller"].setdefault(ad, {"roller": []})
                fk.update(id=f"{ad}@{it['repo'].split('/')[-1]}", repo=it["repo"], kaynak_yol=it["yol"], commit=commit,
                          bolum="fihrist", tur="dev-koleksiyon", klasor_hash=klasor_hash(skil_dir),
                          kurulu_hash=kurulu_hash(proje, ad), varyantlar=[], dosyalar=inc["dosyalar"],
                          boyut_bayt=bayt, tarih=date.today().isoformat(),
                          inceleme={"commit": commit, "tarih": date.today().isoformat(), "sonuc": inc["sonuc"]})
                if it.get("rol") and it["rol"] not in fk["roller"]:
                    fk["roller"].append(it["rol"])
                print(f"  + {ad} (fihrist, {boyut_bicim(bayt)}, inceleme: {inc['sonuc']})")
            for it, commit, klon_dir, inc in kit_hazirlanan:
                if not isinstance(kilit.get("kitler"), dict):
                    kilit["kitler"] = {}
                kk = kit_kur(klon_dir, proje, kilit, it["kit"], inc, commit, it["mod"], it["parcalar"])
                kilit["kitler"][it["repo"]] = kk
                olculen_bayt[0] += kk["boyut_bayt"]
                print(f"  + {it['repo']} (kit/{it['mod']}, {len(kk['dosyalar'])} dosya, {len(kk['skiller'])} skil, {boyut_bicim(kk['boyut_bayt'])})")
            for it in dis_liste:
                ad = it["ad"]
                if it.get("mevcut"):
                    if it["tur"] == "program-bag" and not it.get("var"):
                        dis_kur_bag(proje, kilit, ad, it["hedef"])
                        print(f"  + {ad} (bağ yeniden kuruldu)")
                    continue
                if not isinstance(kilit.get("dis_skiller"), dict):
                    kilit["dis_skiller"] = {}
                if it["tur"] == "program-bag":
                    dis_kur_bag(proje, kilit, ad, it["hedef"])
                    kilit["dis_skiller"][ad] = {"ad": ad, "tur": "program-bag", "program": it["program"], "hedef": str(it["hedef"]),
                                                "tarih": date.today().isoformat(), "program_surum": it["surum"],
                                                "program_surum_turu": it["surum_turu"]}
                    print(f"  + {ad} (bağ)")
                else:
                    kilit["dis_skiller"][ad] = dis_kur_donmus(proje, kilit, ad, it["kaynak"])
                    olculen_bayt[0] += (it.get("tarama") or {}).get("bayt", 0)
                    print(f"  + {ad} (donmuş kopya)")
            kilit["roller"] = list(dict.fromkeys(kilit["roller"] + roller))
            kilit["profil"] = profil or kilit.get("profil")
            tumunu_yaz(proje, kilit, skiller)
            (meta(proje) / "son-rapor.md").write_text(rapor.markdown("Skill ekleme ön kontrol raporu"), encoding="utf-8")
        guvenli_islem(proje, yedek, islem)
        degisen_fh = []
        for it, ad, commit, _, inc in fihrist_hazirlanan:
            if fihrist_inceleme_kaydet(it["repo"], it["yol"], commit, inc):
                degisen_fh.append(fihrist_dosya_yolu(it["repo"]))
        if degisen_fh:
            fihrist_inceleme_commit(degisen_fh)
    finally:
        # Plan ortak kural 7: yalnız aracın kendi oluşturduğu geçici klasör kendiliğinden silinir
        if gecici_kok and gecici_kok.exists():
            shutil.rmtree(gecici_kok, ignore_errors=True)
    sonuc = dogrula(proje, skiller, sessiz=True)
    n_bag = sum(1 for it in dis_liste if it["tur"] == "program-bag")
    n_don = sum(1 for it in dis_liste if it["tur"] == "donmus")
    n_kit = len(kit_kayitlari(kilit))
    print(f"\nTamam: {len(kilit['skiller'])} skill, {len(kilit['roller'])} rol"
          + (f" · {n_kit} kit" if n_kit else "")
          + (f" · {n_bag} program bağı, {n_don} donmuş skill" if n_bag + n_don else "")
          + (f" · ölçülen boyut: {boyut_bicim(olculen_bayt[0])}" if olculen_bayt[0] and (n_kit or fihrist_hazirlanan) else "")
          + f" · doğrulama: {'✅' if not sonuc else '❌ ' + '; '.join(sonuc)} · yedek: {yedek.name}")
    return 0 if not sonuc else 1


def kaldir(a, proje, skiller):
    kilit = kilit_oku(proje)
    hedefler = list(kilit["skiller"]) if a.kaldir == ["hepsi"] else a.kaldir
    rapor = Rapor()
    proje_yapisi_kontrol(proje, [], rapor)
    dis = dis_kayitlari(kilit)
    kitler = kit_kayitlari(kilit)
    kit_esleme = {}  # istenen ad -> kit repo anahtarı
    kit_plan = {}    # repo -> (silinecek_dosyalar, korunan_dosyalar, silinecek_skiller)
    donmus_yedek = False
    for ad in hedefler:
        if ad in kilit["skiller"]:
            if elle_degismis(proje, ad, kilit["skiller"][ad]):
                rapor.ekle("HATA", "elle-degistirilmis", f"{ad} elle değiştirilmiş (--zorla: yedekle ve sil)")
            else:
                rapor.ekle("BİLGİ", "silinecek", ad)
        elif ad in dis and dis_ad_gecerli(ad):
            g = dis[ad]
            h, c = proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad
            if g["tur"] == "program-bag":
                kart_hedef = dis_bag_hedefi(g)
                bizim = {g["hedef"]} | ({str(kart_hedef)} if kart_hedef else set())
                bozuk = []
                for slot in (h, c):
                    if not (slot.exists() or slot.is_symlink()):
                        continue
                    ok = slot.is_symlink() and (os.readlink(slot) in bizim or os.readlink(slot) == os.path.relpath(h, c.parent) and slot == c)
                    if not ok:
                        bozuk.append(str(slot.relative_to(proje)))
                if bozuk:
                    rapor.ekle("HATA", "bag-degismis", f"{ad}: {', '.join(bozuk)} bağ değil ya da başka yere gidiyor; elle değiştirilmiş "
                               "(kullanıcı verisi olabilir: elle sil; --zorla bunu geçmez)")
                else:
                    rapor.ekle("BİLGİ", "silinecek", f"{ad} (program bağı; programın kendi klasörüne DOKUNULMAZ)")
            else:
                gercek = h if codex_var(kilit) else c
                rapor.ekle("BİLGİ", "silinecek", f"{ad} (donmuş skill; silmeden önce yedeğe kopyalanır: --geri-al ile dönülür)")
                donmus_yedek = True
                if gercek.is_dir() and not gercek.is_symlink() and g.get("icerik_hash") and klasor_hash(gercek) != g["icerik_hash"]:
                    rapor.ekle("UYARI", "dondurma-degismis", f"{ad}: donmuş kopya sonradan değiştirilmiş; silinirse yalnız yedekte kalır")
        elif (kt_repo := next((r for r in kitler if r.lower() == ad.lower() or r.split("/")[-1].lower() == ad.lower()), None)):
            g = kitler[kt_repo]
            kit_esleme[ad] = kt_repo
            sil_d, koru_d, sil_sk, koru_sk = [], [], [], []
            for rel, eski_h in sorted((g.get("dosyalar") or {}).items()):
                if not goreli_proje_yolu_gecerli(rel) or not proje_ici(proje, proje / rel):
                    rapor.ekle("HATA", "proje-disi-baglanti", f"{kt_repo}: kilitte proje dışı dosya yolu (`{rel}`); güvenlik nedeniyle işlem durduruldu")
                    continue
                p = proje / rel
                if not p.exists() and not p.is_symlink():
                    continue
                if not kit_dosya_degismis_mi(rel, p, eski_h, g.get("talimat_temiz_hash")):
                    sil_d.append(rel)
                else:
                    koru_d.append(rel)
            sk_hashler = g.get("skil_hashleri") if isinstance(g.get("skil_hashleri"), dict) else {}
            for sk in list(g.get("skiller") or []):
                if (not dis_ad_gecerli(sk) or not proje_ici(proje, proje / ".claude" / "skills" / sk)
                        or not proje_ici(proje, proje / ".agents" / "skills" / sk)):
                    rapor.ekle("HATA", "proje-disi-baglanti", f"{kt_repo}: kilitte geçersiz/proje dışı skil adı (`{sk}`); güvenlik nedeniyle işlem durduruldu")
                    continue
                eski_sh = sk_hashler.get(sk)
                if eski_sh and elle_degismis(proje, sk, {"kurulu_hash": eski_sh}):
                    koru_sk.append(sk)
                else:
                    sil_sk.append(sk)
            kit_plan[kt_repo] = (sil_d, koru_d, sil_sk)
            rapor.ekle("BİLGİ", "silinecek", f"{kt_repo} (kit: {len(sil_d)} değişmemiş dosya, {len(sil_sk)} skil silinecek)")
            if koru_d:
                rapor.ekle("UYARI", "kit-dosya-degismis", f"{kt_repo}: kullanıcının değiştirdiği {len(koru_d)} dosya SİLİNMEYECEK (korunur): {', '.join(koru_d[:6])}")
            if koru_sk:
                rapor.ekle("UYARI", "kit-skil-degismis", f"{kt_repo}: kullanıcının değiştirdiği {len(koru_sk)} kit skili SİLİNMEYECEK (korunur): {', '.join(koru_sk[:6])}")
        else:
            rapor.ekle("HATA", "kutuphaneden-degil", f"{ad} bu projeye kütüphaneden, kit olarak, programdan ya da dondurma ile eklenmemiş; dokunulmaz")
    if donmus_yedek:
        rapor.ekle("BİLGİ", "dondurma-yedek", f"Yedekler en son {YEDEK_SAYISI} işlemle sınırlıdır; donmuş kopyayı kalıcı saklamak istiyorsan yedek klasörünü "
                   "başka yere kopyala.")
    rapor.yazdir()
    if not onay(a, rapor):
        return 2
    ek_yedek = [rel for sil_d, _, _ in kit_plan.values() for rel in sil_d]
    kit_sk_yedek = [sk for _, _, sks in kit_plan.values() for sk in sks]
    yedek = yedekle(proje, [ad for ad in hedefler if ad in kilit["skiller"] or ad in dis or dis_ad_gecerli(ad)] + kit_sk_yedek,
                    "kaldir", ek_hedefler=ek_yedek)

    def islem():
        for ad in hedefler:
            if ad in kilit["skiller"]:
                sil_yol(proje / ".claude" / "skills" / ad)
                sil_yol(proje / ".agents" / "skills" / ad)
                del kilit["skiller"][ad]
            elif ad in dis:
                dis_sil(proje, ad)  # bağsa yalnız bağ silinir; program klasörüne girilmez
                del kilit["dis_skiller"][ad]
            elif ad in kit_esleme:
                kt_repo = kit_esleme[ad]
                sil_d, _, sks = kit_plan[kt_repo]
                for rel in sil_d:
                    p = proje / rel
                    if proje_ici(proje, p) and p.is_file() and not p.is_symlink():
                        p.unlink()
                        # boş kalan üst klasörleri proje köküne kadar temizle
                        ust = p.parent
                        while ust != proje and proje_ici(proje, ust):
                            try:
                                if not any(ust.iterdir()):
                                    ust.rmdir()
                                    ust = ust.parent
                                else:
                                    break
                            except OSError:
                                break
                for sk in sks:
                    if not dis_ad_gecerli(sk):
                        raise RuntimeError(f"geçersiz kit skil adı: {sk!r}")
                    for slot in (proje / ".claude" / "skills" / sk, proje / ".agents" / "skills" / sk):
                        if not proje_ici(proje, slot):
                            raise RuntimeError(f"{slot}: proje dışına gidiyor; silinmedi")
                        sil_yol(slot)
                del kilit["kitler"][kt_repo]
        if a.kaldir == ["hepsi"]:
            kilit["roller"] = []
        tumunu_yaz(proje, kilit, skiller)
    guvenli_islem(proje, yedek, islem)
    print(f"Kaldırıldı. Geri almak için: --geri-al {yedek.name}")
    return 0


def guncelle(a, proje, skiller, kilit=None, yapi_degisti=False):
    kilit = kilit or kilit_oku(proje)
    rapor, degisen = Rapor(), []
    proje_yapisi_kontrol(proje, kilit["roller"], rapor)
    arac_satirlari(proje, kilit, rapor)
    for ad, k in kilit["skiller"].items():
        if k.get("bolum") == "fihrist":
            if yapi_degisti:
                if elle_degismis(proje, ad, k) and not a.zorla:
                    rapor.ekle("HATA", "elle-degistirilmis", f"{ad} elle değiştirilmiş; araç düzenine taşınmaz (--zorla)")
                else:
                    rapor.ekle("BİLGİ", "arac-tasinacak", f"{ad}: fihrist skili yeni araç düzenine taşınacak")
                continue
            fh = fihrist_oku(k.get("repo", ""))
            if not fh:
                rapor.ekle("BİLGİ", "fihrist-kaynak-yok", f"{ad}: fihrist dosyası artık yok ({k.get('repo')}); projede çalışmaya devam eder")
            elif not any(x.get("yol") == k.get("kaynak_yol") for x in fh["skiller"]):
                rapor.ekle("UYARI", "fihrist-kaldirildi", f"{ad}: fihristte artık yok ({k.get('repo')}:{k.get('kaynak_yol')}); projede olduğu gibi bırakıldı")
            elif fh.get("commit") and fh["commit"] != k.get("commit"):
                rapor.ekle("BİLGİ", "fihrist-guncelleme",
                           f"{ad}: fihristte yeni sürüm ({k.get('commit', '?')[:7]} -> {fh['commit'][:7]}); "
                           f"güncellemek için: --fihrist-skill {k['repo']}:{k['kaynak_yol']} --evet (geçici klasörde yeniden incelenir)")
            continue
        s = kaynak_bul(skiller, k)
        if not s:
            rapor.ekle("UYARI", "kaynak-yok", f"{ad}: kaynağı ({k.get('repo')}:{k.get('kaynak_yol', k['id'])}) kütüphanede artık "
                       "yok; projede olduğu gibi bırakıldı. Başka bir repo'nun aynı adlı skill'i otomatik konmaz")
            continue
        canli = canli_global(s)
        if ad == s["ad"] and any(v == "farkli" for v in canli.values()):
            rapor.ekle("UYARI", "global-cakisma-yeni", f"{ad}: globale aynı adlı FARKLI skill eklenmiş; Claude'da global sürüm "
                       "kazanır. Kütüphane sürümü için --kaldir ve yeniden ekle")
        farkli = []
        yeni_kardes = kardes_adlari(kardes_haritasi(s, skiller, kilit, None, None, farkli))
        farkli_anahtar = {x[0] for x in farkli}
        bildirilen = set()
        for anahtar, kid, baska in farkli:  # aynı ad başka kimlik: yol çevrilmez, çalışan bağlantı bozulmasın; kardeş başına tek uyarı
            if kid not in bildirilen:
                bildirilen.add(kid)
                rapor.ekle("UYARI", "kardes-farkli-kaynak", f"{ad}: {anahtar.replace(GENEL_KARDES, '')} kardeşi {kid} olmalı, ama projede aynı adlı "
                           f"BAŞKA bir skill var ({baska}); yol çevrilmez, kardeş {kid} ayrıca eklenmeli (--skill {kid})")
        # yalnız farkli-kaynak anahtarlarından doğan fark yeniden yazma sebebi değildir (kilitteki bağlantı çalışır durumda kalır)
        kardes_degisti = ({a: v for a, v in k.get("kardes", {}).items() if a not in farkli_anahtar}
                          != {a: v for a, v in yeni_kardes.items() if a not in farkli_anahtar})
        if s["klasor_hash"] == k["klasor_hash"]:
            if kurulum_eksik(proje, ad, kilit):
                if elle_degismis(proje, ad, k) and not a.zorla:
                    rapor.ekle("HATA", "elle-degistirilmis", f"{ad} elle değiştirilmiş; yeniden kurulmaz (--zorla: yedekle ve ez)")
                    continue
                degisen.append((ad, s))
                rapor.ekle("BİLGİ", "onarilacak", f"{ad}: eksik/bozuk kurulum onarılacak")
                continue
            if not kardes_degisti and k.get("onarim") != onarim_izi(s, skiller):
                if elle_degismis(proje, ad, k) and not a.zorla:
                    rapor.ekle("HATA", "elle-degistirilmis", f"{ad} elle değiştirilmiş; frontmatter/yol onarımı uygulanmaz (--zorla)")
                    continue
                degisen.append((ad, s))
                yol_var = bool(yol_izi(s, skiller))
                ne = (["description/frontmatter düzeltmesi"] if (s.get("aciklama_duzeltme") or any(
                    "dosya başında değil" in y or "tırnaksız" in y for y in s.get("yapisal_sorunlar", []))) else []) + \
                     ([f"betik yaması ({', '.join(s['yama']['dosyalar'])})"] if s.get("yama") else []) + \
                     (["sabit yol çevirisi"] if yol_var else [])
                rapor.ekle("BİLGİ", "yol-yerellestirme" if yol_var and len(ne) == 1 else "yama" if s.get("yama") and len(ne) == 1 else "aciklama-onarim",
                           f"{ad}: kurulan kopyaya uygulanacak: {' + '.join(ne) or 'onarım'}")
                continue
            if not kardes_degisti:
                continue
            if elle_degismis(proje, ad, k) and not a.zorla:
                rapor.ekle("HATA", "elle-degistirilmis", f"{ad} elle değiştirilmiş; kardeş yolları düzeltilmez (--zorla)")
                continue
            degisen.append((ad, s))
            rapor.ekle("BİLGİ", "kardes-yol", f"{ad}: kardeş yolları (../<kardeş>/ bağlantıları ve sabit kardeş yolları) projedeki adlara göre yeniden yazılacak")
            continue
        if elle_degismis(proje, ad, k) and not a.zorla:
            rapor.ekle("HATA", "elle-degistirilmis", f"{ad} elle değiştirilmiş; güncellenmez (--zorla: yedekle ve ez)")
            continue
        degisen.append((ad, s))
        rapor.ekle("BİLGİ", "guncellenecek", f"{ad}: {k['commit'][:7]} -> {s['commit'][:7]}")
        for u in s.get("yapisal_sorunlar", []):
            rapor.ekle("BİLGİ", "yapi", f"{ad}: {u}")
    dis = dis_kayitlari(kilit)
    if dis:
        n_bag = sum(1 for g in dis.values() if g["tur"] == "program-bag")
        rapor.ekle("BİLGİ", "dis-skiller", f"{n_bag} skill programla güncel (bağ), {len(dis) - n_bag} donmuş (kütüphane güncellemez): bunlar güncellenmez")
        for ad, g in sorted(dis.items()):
            if g["tur"] == "program-bag":
                for kod, _ in dis_sorunlar(proje, kilit, ad, g):
                    if kod in ("kirik", "kart-yok"):
                        hedef = dis_bag_hedefi(g)
                        rapor.ekle("UYARI", "bag-kirik", f"{ad}: program bağı kırık ({yol_goster(hedef) if hedef else g.get('program')}); "
                                   f"--yenile ya da --kaldir {ad}")
    for kr, kg in sorted(kit_kayitlari(kilit).items()):
        kay = kaynak_kaydi(kr)
        sc = ((kay or {}).get("son_kontrol") or {}).get("commit")
        if sc and sc != kg.get("commit"):
            rapor.ekle("BİLGİ", "kit-guncelleme", f"kit {kr}: kaynakta değişiklik var ({kg['commit'][:7]} -> {sc[:7]}); "
                       "kitler projeye kendiliğinden uygulanmaz (kullanıcı dosyalarını korumak için)")
        else:
            rapor.ekle("BİLGİ", "kit-guncelleme", f"kit {kr}: kurulu commit {kg['commit'][:7]} (kitler kendiliğinden güncellenmez)")
    hesap_eksik = hesap_gizleme_eksik(proje, kilit)
    for k in hesap_eksik:
        rapor.ekle("BİLGİ", "hesap-cakismasi", f"{AYAR} → skillOverrides \"{k}\" güncellenecek (Claude hesabındaki aynı adlı "
                   "skill kütüphane sürümünü gölgelemesin)")
    print(f"Güncellenecek/onarılacak: {len(degisen)}")
    rapor.yazdir()
    if not degisen and not yapi_degisti and not hesap_eksik:
        return 1 if rapor.say("HATA") else 0
    if not onay(a, rapor):
        return 2
    kit_sk_yedek = [sk for kg in kit_kayitlari(kilit).values() for sk in (kg.get("skiller") or []) if dis_ad_gecerli(sk)]
    yedek = yedekle(proje, (list(kilit["skiller"]) + list(dis_kayitlari(kilit)) + kit_sk_yedek) if yapi_degisti else [d for d, _ in degisen],
                    "arac" if yapi_degisti else "guncelle")

    def islem():
        for ad, s in degisen:
            kardes = kardes_haritasi(s, skiller, kilit)
            for u in kur(s, proje, ad, kardes, codex_var(kilit), skiller):
                print(f"  ! {u}")
            kayit_guncelle(kilit, proje, ad, s, kardes=kardes, skiller=skiller)
        if yapi_degisti:
            for m in dis_yerlestir(proje, kilit) + fihrist_yerlestir(proje, kilit) + kit_yerlestir(proje, kilit):
                print(f"  ! {m}")
        tumunu_yaz(proje, kilit, skiller)
        if not codex_var(kilit):  # boş kalan Codex klasörleri (içinde kullanıcının kendi dosyası varsa dokunulmaz)
            for d in (proje / ".agents" / "skills", proje / ".agents"):
                if d.is_dir() and not d.is_symlink() and not any(x.name != ".DS_Store" for x in d.iterdir()):
                    shutil.rmtree(d)
    guvenli_islem(proje, yedek, islem)
    if yapi_degisti:
        sonuc = dogrula(proje, skiller, sessiz=True)
        print(f"Araç düzeni değişti · doğrulama: {'✅' if not sonuc else '❌ ' + '; '.join(sonuc)}")
    print(f"Güncellendi. Geri almak için: --geri-al {yedek.name}")
    return 0


def arac_degistir(a, proje, skiller):
    """Projenin araç düzenini değiştirir (ör. sadece Claude) ve kurulu skilleri yeni düzene göre yeniden kurar.
    Skill içerikleri değişmez; elle değiştirilmiş skill --zorla olmadan yeniden kurulmaz."""
    kilit = kilit_oku(proje)
    eski_duzen = duzen_adi(kilit)
    yeni_duzen = duzen_uygula(kilit, a.arac)
    print(f"Proje: {proje}\nAraçlar: {'Claude + Codex' if eski_duzen == 'ortak' else 'sadece Claude'} ({eski_duzen}) -> "
          f"{'Claude + Codex' if yeni_duzen == 'ortak' else 'sadece Claude'} ({yeni_duzen})")
    return guncelle(a, proje, skiller, kilit=kilit, yapi_degisti=True)


def dogrula(proje, skiller, sessiz=False):
    kilit = kilit_oku(proje)
    codex = codex_var(kilit)
    sorun = []
    for ad, k in kilit["skiller"].items():
        c, cl = proje / ".agents" / "skills" / ad, proje / ".claude" / "skills" / ad
        if codex and not (c / "SKILL.md").exists():
            sorun.append(f"{ad}: .agents/skills kopyası yok")
        if not codex and (c.exists() or c.is_symlink()):
            sorun.append(f"{ad}: proje sadece Claude kullanıyor ama .agents/skills kopyası duruyor (--guncelle)")
        if not (cl / "SKILL.md").exists():
            sorun.append(f"{ad}: .claude/skills bağlantısı/kopyası çalışmıyor")
        elif cl.is_symlink() and (not codex or cl.resolve() != c.resolve()):
            sorun.append(f"{ad}: .claude/skills bağlantısı yanlış yere gidiyor ({cl.resolve()})")
        if codex and "claude" not in k.get("varyantlar", []) and cl.exists() and not cl.is_symlink():
            sorun.append(f"{ad}: .claude/skills'te beklenmeyen gerçek klasör (symlink olmalıydı)")
        for yer in (c, cl):
            if (yer / "SKILL.md").exists() and frontmatter_adi(yer / "SKILL.md") != ad:
                sorun.append(f"{yer.relative_to(proje)}: SKILL.md name klasör adıyla aynı değil")
        if elle_degismis(proje, ad, k):
            sorun.append(f"{ad}: kurulumdan sonra elle değiştirilmiş")
        if k.get("bolum") != "fihrist" and not kaynak_bul(skiller, k):
            sorun.append(f"{ad}: kaynağı kütüphanede artık yok ({k.get('repo')}:{k.get('kaynak_yol', k['id'])})")
    kitler = kit_kayitlari(kilit)
    for kr, kg in sorted(kitler.items()):
        for rel in (kg.get("dosyalar") or {}):
            if not goreli_proje_yolu_gecerli(rel) or not proje_ici(proje, proje / rel):
                sorun.append(f"kit {kr}: kilitte geçersiz/proje dışı dosya yolu (`{rel}`)")
        for sk in kg.get("skiller", []):
            if not dis_ad_gecerli(sk):
                sorun.append(f"kit {kr}: kilitte geçersiz skil adı (`{sk}`)")
                continue
            c, cl = proje / ".agents" / "skills" / sk, proje / ".claude" / "skills" / sk
            if codex and not (c / "SKILL.md").exists():
                sorun.append(f"kit {kr} skili {sk}: .agents/skills kopyası yok")
            if not codex and (c.exists() or c.is_symlink()):
                sorun.append(f"kit {kr} skili {sk}: proje sadece Claude kullanıyor ama .agents/skills kopyası duruyor (--guncelle)")
            if not (cl / "SKILL.md").exists():
                sorun.append(f"kit {kr} skili {sk}: .claude/skills bağlantısı/kopyası çalışmıyor")
            elif cl.is_symlink() and (not codex or cl.resolve() != c.resolve()):
                sorun.append(f"kit {kr} skili {sk}: .claude/skills bağlantısı yanlış yere gidiyor ({cl.resolve()})")
            if codex and cl.exists() and not cl.is_symlink():
                sorun.append(f"kit {kr} skili {sk}: .claude/skills'te beklenmeyen gerçek klasör (symlink olmalıydı)")
    tum = set(kilit["skiller"])
    for rol in kilit["roller"]:
        md, toml = proje / ".claude" / "agents" / f"{rol}.md", proje / ".codex" / "agents" / f"{rol}.toml"
        if not md.exists() or (codex and not toml.exists()):
            sorun.append(f"rol {rol}: agent dosyası eksik (--yenile)")
            continue
        for a in re.findall(r"^  - (.+)$", md.read_text(encoding="utf-8"), re.M):
            if a not in tum:
                sorun.append(f"rol {rol}: Claude agent'ı olmayan skill'e bakıyor: {a}")
        if not codex:
            if toml.exists() and URETILDI in toml.read_text(encoding="utf-8"):
                sorun.append(f"rol {rol}: proje sadece Claude kullanıyor ama Codex agent dosyası duruyor (--yenile)")
            continue
        rol_skilleri = {a for a, k in kilit["skiller"].items() if rol in k["roller"]}
        kapali = set()
        for p in re.findall(r'^path = "(.+)"$', toml.read_text(encoding="utf-8"), re.M):
            if not Path(p).exists():
                sorun.append(f"rol {rol}: Codex agent'ında geçersiz yol (proje taşınmış olabilir, --yenile): {p}")
            kapali.add(Path(p).parent.name)
        acik_kalan = tum - rol_skilleri - kapali
        if acik_kalan:
            sorun.append(f"rol {rol}: Codex'te kapatılmamış rol dışı skiller: {', '.join(sorted(acik_kalan))} (--yenile)")
    for m in dis_gecersizleri(kilit):
        sorun.append(m)
    dis = dis_kayitlari(kilit)
    for ad, g in sorted(dis.items()):
        for _, m in dis_sorunlar(proje, kilit, ad, g):
            sorun.append(m)
    if kilit["skiller"] or dis or kitler:
        for f in ("AGENTS.md", "CLAUDE.md") if codex else ("CLAUDE.md",):
            d = proje / f
            if not d.exists() or BLOK_BAS not in d.read_text(encoding="utf-8") or BLOK_SON not in d.read_text(encoding="utf-8"):
                sorun.append(f"{f}: skill-kutuphanesi bloğu eksik/bozuk (--yenile)")
        if not codex and (proje / "AGENTS.md").exists() and BLOK_BAS in (proje / "AGENTS.md").read_text(encoding="utf-8"):
            sorun.append("AGENTS.md: proje sadece Claude kullanıyor ama skill-kutuphanesi bloğu duruyor (--yenile)")
    for k in hesap_gizleme_eksik(proje, kilit):
        sorun.append(f"{AYAR}: hesap skill'i `{k}` için skillOverrides güncel değil; kütüphane sürümü gölgelenebilir (--guncelle)")
    if kilit.get("proje_yolu") and kilit["proje_yolu"] != str(proje):
        sorun.append(f"proje taşınmış ({kilit['proje_yolu']} -> {proje}); --yenile çalıştır")
    for d in (proje / ".agents" / "skills", proje / ".claude" / "skills"):
        if d.is_dir():
            for x in d.iterdir():
                if x.name.endswith(".kurulum-tmp"):
                    sorun.append(f"yarım kalmış kurulum klasörü: {x.relative_to(proje)}")
    if not sessiz:
        print("Doğrulama: " + ("✅ sorun yok" if not sorun else f"❌ {len(sorun)} sorun"))
        for x in sorun:
            print("  -", x)
    return sorun


def durum(proje, skiller):
    kilit = kilit_oku(proje)
    print(f"Proje: {proje}\nProfil: {kilit.get('profil')}  Roller: {', '.join(kilit['roller']) or '-'}  "
          f"Araçlar: {'Claude + Codex' if codex_var(kilit) else 'sadece Claude'}"
          f" · düzen: {duzen_adi(kilit)} ({'seçildi' if kilit.get('arac_secimi') == 'secildi' else 'varsayılan: seçim yapılmadı'})")
    for ad, k in sorted(kilit["skiller"].items()):
        if k.get("bolum") == "fihrist":
            fh = fihrist_oku(k.get("repo", ""))
            if not fh:
                isaret = "KAYNAK KÜTÜPHANEDE YOK (fihrist; projede çalışmaya devam eder)"
            elif not any(x.get("yol") == k.get("kaynak_yol") for x in fh["skiller"]):
                isaret = "KAYNAKTA KALDIRILDI (fihrist; projede çalışmaya devam eder)"
            elif elle_degismis(proje, ad, k):
                isaret = "ELLE DEĞİŞTİRİLMİŞ (fihrist)"
            elif fh.get("commit") and fh["commit"] != k.get("commit"):
                isaret = f"GÜNCELLEME VAR (fihrist: {k.get('commit', '?')[:7]} -> {fh['commit'][:7]})"
            elif kurulum_eksik(proje, ad, kilit):
                isaret = "KURULUM EKSİK/BOZUK (fihrist)"
            else:
                isaret = "güncel (fihrist)"
            print(f"  {ad:42s} {', '.join(k['roller']) or 'fihrist':34s} {isaret}")
            continue
        s = kaynak_bul(skiller, k)
        if not s:
            isaret = "KAYNAK KÜTÜPHANEDE YOK (kaynak-yok: yerine geçeni KATALOG.md / guven-siralamasi.md'den bul)"
        elif s.get("kaynak_durumu") in ("kaynakta-kaldirildi", "kayip"):
            # Kaynak GitHub'da kaldırıldı/kayboldu: arşiv kopyası duruyor ama artık güncellenmeyecek (güncel gibi görünmesin)
            isaret = "EMEKLİ: KAYNAKTA KALDIRILDI" if s["kaynak_durumu"] == "kaynakta-kaldirildi" else "EMEKLİ: KAYNAK KAYIP"
            isaret += " (emekli: artık güncellenmez, yerine geçeni bul)"
        elif elle_degismis(proje, ad, k):
            isaret = "ELLE DEĞİŞTİRİLMİŞ"
        elif s["klasor_hash"] != k["klasor_hash"]:
            isaret = f"GÜNCELLEME VAR ({k['commit'][:7]} -> {s['commit'][:7]})"
        elif kurulum_eksik(proje, ad, kilit):
            isaret = "KURULUM EKSİK/BOZUK (--guncelle onarır)"
        else:
            isaret = "güncel"
        print(f"  {ad:42s} {', '.join(k['roller']) or 'genel':34s} {isaret}")
    for ad, g in sorted(dis_kayitlari(kilit).items()):
        sor = dict(dis_sorunlar(proje, kilit, ad, g))
        if g["tur"] == "program-bag":
            kolon2 = f"bağ: {g['program']}"
            hedef = dis_bag_hedefi(g)
            if "kirik" in sor or "kart-yok" in sor:
                isaret = (f"BAĞ KIRIK (hedef yok: {yol_goster(hedef)}; --yenile ya da --kaldir {ad})" if hedef else
                          f"BAĞ KIRIK (program kartı yok: {g['program']}; --kaldir {ad})")
            elif "gercek-klasor" in sor:
                isaret = f"KURULUM EKSİK/BOZUK (bağ yerine gerçek klasör var; --kaldir {ad})"
            elif sor:
                isaret = "KURULUM EKSİK/BOZUK (--yenile onarır)"
            else:
                isaret = "programla güncel (bağ)"
                simdi = program_surumu(program_karti(g["program"]))[0]
                if simdi != g.get("program_surum"):
                    isaret += f" · bağlandığında {surum_metni(g.get('program_surum'), g.get('program_surum_turu'))}, kart şimdi {surum_metni(simdi, g.get('program_surum_turu'))}"
        else:
            kolon2 = "donmuş"
            if "donmus-yok" in sor:
                isaret = f"DONMUŞ KLASÖR YOK (--geri-al <yedek> ya da --kaldir {ad})"
            elif sor:
                isaret = "KURULUM EKSİK/BOZUK (--yenile onarır)"
            else:
                isaret = "donmuş (kütüphane güncellemez)"
        print(f"  {ad:42s} {kolon2:34s} {isaret}")
    for kr, kg in sorted(kit_kayitlari(kilit).items()):
        kay = kaynak_kaydi(kr)
        kt = kit_bul(kr)
        sc = ((kay or {}).get("son_kontrol") or {}).get("commit")
        if not kt or (kay and kay.get("tip") == "KAYIP"):
            isaret = "KAYNAK KÜTÜPHANEDE YOK / KAYIP (kit; projede çalışmaya devam eder)"
        elif sc and sc != kg.get("commit"):
            isaret = f"KİTTE DEĞİŞİKLİK VAR ({kg['commit'][:7]} -> {sc[:7]}; otomatik uygulanmaz)"
        else:
            isaret = f"güncel (kit/{kg.get('mod', 'iskelet')}, {len(kg.get('dosyalar', {}))} dosya, {boyut_bicim(kg.get('boyut_bayt'))})"
        print(f"  {kr:42s} {'kit (katalog)':34s} {isaret}")


def yedekler_listesi(proje):
    ydir = meta(proje) / "yedek"
    return sorted(ydir.iterdir()) if ydir.is_dir() else []


def geri_al(a, proje):
    yedekler = yedekler_listesi(proje)
    if not yedekler:
        sys.exit("Yedek yok.")
    if a.geri_al is True:
        hedef = next((y for y in reversed(yedekler) if json_oku(y / "yedek.json", {}).get("neden") != "geri-al-oncesi"), None)
    else:
        hedef = next((y for y in yedekler if y.name == a.geri_al), None)
    if not hedef:
        sys.exit("Uygun yedek bulunamadı. Liste: --yedekler")
    kilit = kilit_oku(proje)
    bilgi = json_oku(hedef / "yedek.json")
    adlar = set(kilit["skiller"]) | set(dis_kayitlari(kilit)) | {r.split("/")[-1] for r in bilgi["hedefler"] if "/skills/" in r}
    ek_kit = [rel for kg in kit_kayitlari(kilit).values() for rel in (kg.get("dosyalar") or {})]
    ek_kit += [r for r in bilgi["hedefler"] if not r.startswith((".agents/", ".claude/", ".codex/", META)) and r not in ("AGENTS.md", "CLAUDE.md")]
    once = yedekle(proje, sorted(adlar), "geri-al-oncesi", ek_hedefler=ek_kit)  # geri almanın kendisi de geri alınabilir
    geri_yukle(proje, hedef)
    shutil.rmtree(hedef)
    print(f"Geri alındı: {bilgi['neden']} ({bilgi['zaman']}). Bunu da geri almak için: --geri-al {once.name}")
    return 0


def oner(a, proje, skiller):
    tek = proje_teknolojileri(proje) if proje else set()
    if a.teknoloji:
        tek.add(a.teknoloji.lower())
    adaylar, n, gizli_n = kutuphane_taramasi(skiller, a.oner, tek, n=a.adet, gizli=a.gizli, kategori_basi=a.kategori_basi)
    print(f"Taranan: {len(skiller)} skill · eşleşen: {n} · teknoloji: {', '.join(sorted(tek)) or '-'}"
          + (f" · gizli katalogda {gizli_n} eşleşme daha (--gizli)" if gizli_n else ""))
    kategori = {}
    for p, s, e, t in adaylar:
        kategori.setdefault(s["kategori"], []).append((p, s, e, t))
    for k, l in kategori.items():
        print(f"\n## {k}")
        for p, s, e, t in l:
            ucret = {"ucretli": " 💲ÜCRETLİ", "kismen": " (kısmen ücretli)", "belirsiz": " (ücret?)"}.get(s.get("ucret"), "")
            if s.get("ortusme_rolu") == "emekli" or s.get("kaynak_durumu"):
                ucret += " 🗄️emekli"
            if s.get("trend"):
                ucret += " 🔥trend"
            print(f"  {s['id'] + ucret:40s} puan {s['degerlendirme']['puan']:3d} ({s['degerlendirme']['not']}) · "
                  f"Codex {s['uyum']['codex']:16s} · eşleşen: {', '.join(e + sorted(t))}")
    roller = {}
    for f in ROLLER.glob("*.json"):
        r = json_oku(f)
        ortak = {s["id"] for _, s, _, _ in adaylar} & set(r["cekirdek"] + r.get("opsiyonel", []))
        if ortak:
            roller[f.stem] = len(ortak)
    if roller:
        print("\nBu ihtiyaca en uygun roller: " + ", ".join(f"{r} ({n})" for r, n in sorted(roller.items(), key=lambda x: -x[1])))
    fh_ad = fihrist_oner(a.oner, tek, arsiv_adlari=[s["ad"] for _, s, _, _ in adaylar])
    if fh_ad:
        print(f"\n## Fihrist adayları (en çok {FIHRIST_ONERI_SINIRI}; kurulumda internet gerekir)")
        for _, repo, g, e in fh_ad:
            print(f"  {repo}:{g['ad']:30s} · eşleşen: {', '.join(e[:4])} · {g.get('aciklama', '')[:70]}")
    kt_ad = kit_oner(a.oner, tek)
    if kt_ad:
        print("\n## Kit kataloğu (hazır proje iskeleti)")
        for _, kt, kay, e in kt_ad:
            bm = kaynak_boyut_metni(kay, dev_dahil=True)
            print(f"  {kt['repo']:40s} · {kt['ad']} · eşleşen: {', '.join(e[:4])}" + (f" · {bm}" if bm else ""))
    pr_ad = program_oner(a.oner, tek)
    if pr_ad:
        print("\n## Programlar (bilgisayarda tek kurulum)")
        for _, pad, kart, kurulu, bm, e in pr_ad:
            dur = "kurulu (bağ verilebilir)" if kurulu else f"kurulu değil{f', kurulumu {bm} yer tutar' if bm else ''}"
            print(f"  {pad:24s} · {dur} · eşleşen: {', '.join(e[:4])}")
    rf_ad = referans_oner(a.oner, tek)
    if rf_ad:
        print("\n## Referans araç/kütüphaneler (skili yok)")
        for _, rk, e in rf_ad:
            print(f"  {rk['repo']:40s} ({rk['tip']}) · eşleşen: {', '.join(e[:4])}")
    if getattr(a, "rapor", False):
        kilit = kilit_oku(proje) if proje else {"surum": KILIT_SURUM, "roller": [], "skiller": {}, "arac_secimi": "varsayilan"}
        if a.arac:
            duzen_uygula(kilit, a.arac)
        rapor = Rapor()
        if proje:
            arac_satirlari(proje, kilit, rapor, secim=a.arac)
        print(proje_raporu_uret(proje, kilit, skiller, rapor, sorgu=a.oner))


def rapor_komutu(a, proje, skiller):
    """--rapor: Plan Bölüm 10 Proje Raporu (her zaman ağsız, salt okunur; hiçbir şey yazmaz)."""
    kilit = kilit_oku(proje) if proje else {"surum": KILIT_SURUM, "roller": [], "skiller": {}, "arac_secimi": "varsayilan"}
    if a.arac:
        duzen_uygula(kilit, a.arac)
    plan, roller, _, bulunamayan = istek_coz(a, skiller)
    rapor = Rapor()
    for b in bulunamayan:
        rapor.ekle("HATA", "bulunamadi", f"kütüphanede yok: {b}")
    fihrist_liste, arsiv_yonlendirme, fihrist_hatalar, fihrist_bilgiler = fihrist_istek_coz(a, skiller)
    for kod, m in fihrist_hatalar:
        rapor.ekle("HATA", kod, m)
    for kod, m in fihrist_bilgiler:
        rapor.ekle("BİLGİ", kod, m)
    if arsiv_yonlendirme:
        plan += arsiv_yonlendirme
    kit_liste, kit_parcalar, kit_hatalar = kit_istek_coz(a)
    for kod, m in kit_hatalar:
        rapor.ekle("HATA", kod, m)
    dis_liste, dis_hatalar = dis_istek_coz(a)
    for kod, m in dis_hatalar:
        rapor.ekle("HATA", kod, m)
    if proje:
        kur_listesi, adlar = on_kontrol(proje, kilit, plan, roller, skiller, rapor, dis_liste=dis_liste)
        dis_liste = dis_on_kontrol(proje, kilit, dis_liste, set(adlar.values()), rapor)
        fihrist_hazir = fihrist_on_kontrol(proje, kilit, fihrist_liste, set(adlar.values()), {it["ad"].casefold() for it in dis_liste}, rapor)
        kit_hazir = kit_on_kontrol(proje, kilit, kit_liste, kit_parcalar, rapor)
        arac_satirlari(proje, kilit, rapor, secim=a.arac)
    else:
        kur_listesi = {s["id"]: (s, {r}) for s, r in plan}
        adlar = {sid: s["ad"] for sid, (s, _) in kur_listesi.items()}
        fihrist_hazir = [(it, it["ad"]) for it in fihrist_liste]
        kit_hazir = [dict(it, mod="parca" if kit_parcalar else "iskelet", parcalar=list(kit_parcalar)) for it in kit_liste]
    print(proje_raporu_uret(proje, kilit, skiller, rapor, kur_listesi=kur_listesi, adlar=adlar,
                            fihrist_hazir=fihrist_hazir, kit_hazir=kit_hazir, dis_liste=dis_liste,
                            sorgu=a.oner or "", roller=roller))
    return 0


def listele(a, skiller):
    n = 0
    for s in skiller:
        if s.get("gizli") and not a.gizli:
            continue
        if a.kategori and a.kategori not in s["kategori"]:
            continue
        if a.teknoloji and a.teknoloji.lower() not in [t.lower() for t in (s.get("teknoloji") or s["teknoloji_oto"])]:
            continue
        if a.ara and a.ara.lower() not in (s["id"] + " " + s["aciklama"] + " " + s.get("ozet_tr", "")).lower():
            continue
        n += 1
        ozet = (s.get("ozet_tr") or s["aciklama"])[:80]
        u = {"ucretli": "💲", "kismen": "½", "belirsiz": "?"}.get(s.get("ucret"), " ")
        print(f"{s['kategori']:46s} {u} {s['id']:38s} {s['degerlendirme']['puan']:3d} {s['uyum']['codex']:16s} {ozet}")
    print(f"\n{n} skill")


def guncelleme_suruyor():
    """arsiv-guncelle.py çalışırken kütüphane onaylanmamış güncelleme dalındadır: kurulum/güncelleme o içeriği projeye taşımasın."""
    kilit = KOK / ".guncelleme-kilidi"
    if not kilit.exists():
        return None
    try:
        b = json.loads(kilit.read_text())
        canli = subprocess.run(["kill", "-0", str(b["pid"])], capture_output=True).returncode == 0
        yas = (datetime.now() - datetime.fromisoformat(b["baslangic"])).total_seconds()
    except Exception:  # noqa: BLE001
        return None
    return b if canli and yas < 6 * 3600 else None  # ölü süreç ya da 6 saatten eski kilit = bayat, yok say


ARAC_ZORUNLU = ("anahtar", "ad", "kurulu", "proje_skill_okur", "dogrulama_tarihi", "surumler")


SURUM_KOMUT_ADLARI = ("claude", "codex", "gemini", "copilot")
SURUM_KOMUT_IZIN_KONTROLU = True  # yalnız testler kapatır (sahte komut için)


def surum_oku(okuma):
    """Bir aracın sürümünü okur: {'komut': [ad, '--version']} (yalnız sürüm komutu çalışır) ya da {'plist': yol}. Okunamazsa None (hata fırlatmaz)."""
    try:
        if isinstance(okuma, dict) and okuma.get("komut"):
            k = okuma["komut"]
            # izin listesi: yalnız ['<ad>', '--version'] ve bilinen dört araç adı; başka komut çalıştırılmaz
            if SURUM_KOMUT_IZIN_KONTROLU and not (isinstance(k, list) and len(k) == 2 and k[0] in SURUM_KOMUT_ADLARI and k[1] == "--version"):
                return None
            r = subprocess.run(okuma["komut"], capture_output=True, text=True, timeout=10, stdin=subprocess.DEVNULL)
            m = re.search(r"\d+(?:\.\d+)+", r.stdout) if r.returncode == 0 else None
            return m.group(0) if m else None
        if isinstance(okuma, dict) and okuma.get("plist"):
            import plistlib
            yol = Path(okuma["plist"])
            if not yol.is_file():
                return None
            with yol.open("rb") as f:
                v = plistlib.load(f).get("CFBundleShortVersionString")
            return str(v) if v else None
    except Exception:  # noqa: BLE001  (komut yok, süre doldu, bozuk plist ...)
        return None
    return None


def araclar_raporu(a, kayitlar=None, simdi=None):
    """Yapay zeka araçları belgesi: kayıtlı sürüm/tarih ile makinedeki gerçek durumu karşılaştırır. Hiçbir şey yazmaz.
    --ozet-json: stdout'a TEK JSON nesnesi. Çıkış 0 (araç doğru çalıştıysa); --siki ile yalnız durum 'sorun' ise 1."""
    simdi = simdi or date.today()
    satirlar, karar, sorun = [], [], None
    if kayitlar is None:
        try:
            d = json_oku(ARAC_JSON)
        except (OSError, ValueError):
            d = None
        if d is None:
            sorun = f"{ARAC_JSON.name} yok ya da geçerli JSON değil"
        elif not isinstance(d, dict) or not isinstance(d.get("araclar"), list):
            sorun = f"{ARAC_JSON.name} beklenen biçimde değil (araclar listesi yok)"
        else:
            kayitlar = d["araclar"]
    if kayitlar is not None and sorun is None:
        for k in kayitlar:
            eksik = [z for z in ARAC_ZORUNLU if not isinstance(k, dict) or z not in k]
            if eksik:
                sorun = f"{k.get('anahtar', '?') if isinstance(k, dict) else '?'} kaydında eksik alan: {', '.join(eksik)}"
                break
    tablo = []
    if sorun:
        durum_ = "sorun"
        satirlar.append(sorun)
    else:
        en_eski = None
        for k in kayitlar:
            ad = k.get("ad_kisa") or k["ad"]
            try:
                gun = (simdi - date.fromisoformat(k["dogrulama_tarihi"])).days
            except (ValueError, TypeError):
                sorun = f"{k['anahtar']} kaydında dogrulama_tarihi geçersiz"
                break
            en_eski = gun if en_eski is None else max(en_eski, gun)
            if gun > ARAC_BELGE_GUN:
                karar.append(f"{ad}: belge {gun} gün önce doğrulandı (sınır {ARAC_BELGE_GUN}); resmi sayfaları yeniden oku ve dogrulama_tarihi'ni güncelle (rehber/14 bölüm 8)")
            bulunanlar = []
            for e in k["surumler"]:
                b = surum_oku(e.get("okuma"))
                kay = e.get("kayitli")
                bulunanlar.append(b)
                if b is not None and kay is not None and b != kay:
                    karar.append(f"{ad}: sürüm {kay} -> {b}; belgeleri yeniden doğrula (rehber/14 bölüm 8) ve kayıtlı sürümle dogrulama_tarihi'ni güncelle")
                    satirlar.append(f"{ad}: kayıtlı sürüm {kay}, bulunan {b}")
            if k["kurulu"] and not any(b is not None for b in bulunanlar):
                karar.append(f"{ad}: kayıtta kurulu görünüyor ama sürüm okunamadı; kaldırıldı mı ya da komut/yol değişti mi bak")
            if not k["kurulu"] and any(b is not None for b in bulunanlar):
                karar.append(f"{ad}: kayıtta kurulu değil ama artık kurulu görünüyor ({', '.join(b for b in bulunanlar if b)}); "
                             "kaydı güncelle (kurulu: true) ve belgelerini doğrula (rehber/14 bölüm 7)")
            tablo.append((ad, "evet" if k["kurulu"] else "hayır", ", ".join(k["proje_skill_okur"]) or "-",
                          ", ".join(str(e.get("kayitli") or "-") for e in k["surumler"]) or "-",
                          ", ".join(str(b or "-") for b in bulunanlar) or "-", f"{gun} gün önce"))
        if sorun:
            durum_ = "sorun"
            satirlar.append(sorun)
        else:
            durum_ = "dikkat" if karar else "temiz"
            kurulu_n = sum(1 for k in kayitlar if k["kurulu"])
            satirlar.insert(0, f"{len(kayitlar)} araç kayıtlı, {kurulu_n} kurulu; en eski doğrulama {en_eski} gün önce")
    if getattr(a, "ozet_json", False):
        print(json.dumps({"arac": "arac-belgeleri", "durum": durum_, "satirlar": satirlar, "karar_bekleyen": karar}, ensure_ascii=False))
    else:
        if tablo:
            basliklar = ("Araç", "Kurulu", "Okuduğu proje skill klasörleri", "Kayıtlı sürüm", "Bulunan sürüm", "Doğrulama")
            for sat in [basliklar] + tablo:
                print(" | ".join(sat))
        for s in satirlar:
            print(s)
        for s in karar:
            print(f"  [KARAR] {s}")
        print(f"Durum: {durum_}")
    return 1 if (getattr(a, "siki", False) and durum_ == "sorun") else 0


def windows_mu():
    return os.name == "nt"


def kurulum_istegi(a, planlayici=True):
    """Komut skill/rol/bağ/dondurma/fihrist/kit kurmak istiyor mu? (main'deki ayrı koşulların tek yeri)"""
    return bool(a.profil or a.rol or a.skill or getattr(a, "program_skill", None) or getattr(a, "dondur", None)
                or getattr(a, "fihrist_skill", None) or getattr(a, "kit", None)
                or (planlayici and a.planlayici))


def main():
    ap = argparse.ArgumentParser(description="SkillKutuphanesi: projeye skill ekle (güvenli)")
    ap.add_argument("proje", nargs="?")
    ap.add_argument("--profil")
    ap.add_argument("--rol", nargs="+")
    ap.add_argument("--skill", nargs="+")
    ap.add_argument("--fihrist-skill", nargs="+", metavar="REPO:AD", dest="fihrist_skill",
                    help="fihristteki (dev koleksiyon) skili kur: --kuru ağsız ön rapor üretir; --evet o gün GitHub'dan geçici klasöre alır, "
                    "inceler, kurar ve kilide yazar. Örn: --fihrist-skill github/awesome-copilot:agent-governance")
    ap.add_argument("--kit", nargs="+", metavar="OWNER/REPO",
                    help="kit kataloğundaki (kitler.json) hazır proje iskeletini kur: --kuru ağsız ön rapor; --evet geçici klasöre alır, inceler, "
                    "boş projeye iskelet olarak kurar (başlamış projede --kit-parca ile çakışmayan parçalar)")
    ap.add_argument("--kit-parca", nargs="+", metavar="YOL", dest="kit_parca",
                    help="--kit ile: başlamış projede yalnız çakışmayan, korunan olmayan (CLAUDE.md/AGENTS.md/ayar hariç) parçaları kur")
    ap.add_argument("--rapor", action="store_true",
                    help="Plan Bölüm 10: 10 bölümlü tam proje raporunu üret (ağsız, salt okunur; hiçbir şey kurmaz)")
    ap.add_argument("--program-skill", nargs="+", metavar="PROGRAM:AD", dest="program_skill",
                    help="programla gelen skili projeye BAĞ ile ver (kopya değil; programın kendi klasörü, program güncellenince kendiliğinden güncel). "
                    "Her skil adıyla yazılır (PROGRAM:* yok). --profil/--rol/--skill ile aynı çalışmada kullanılabilir. Proje yolunu ÖNCE yaz. "
                    "Örn: --program-skill openmontage:ffmpeg hyperframes:hyperframes")
    ap.add_argument("--dondur", nargs="+", metavar="YOL", help="genel klasördeki (ya da herhangi bir mutlak klasördeki) skili projenin KENDİ skili olarak "
                    "dondur: araç gerçek içeriği bir kez kopyalar, kilide 'donmuş' yazar; kütüphane bir daha güncellemez. Proje yolunu ÖNCE yaz")
    ap.add_argument("--rol-adi", help="--skill ile eklenenleri bu role bağla (yeni rol adı da olabilir)")
    ap.add_argument("--planlayici", action="store_true")
    ap.add_argument("--opsiyonel", action="store_true", help="rollerin opsiyonel skillerini de ekle")
    ap.add_argument("--kaldir", nargs="+")
    ap.add_argument("--guncelle", action="store_true")
    ap.add_argument("--durum", action="store_true")
    ap.add_argument("--dogrula", action="store_true")
    ap.add_argument("--yenile", action="store_true", help="agent dosyalarını ve blokları yeniden üret (proje taşındıysa)")
    ap.add_argument("--blok", choices=("tam", "kisa"), help="CLAUDE.md/AGENTS.md skill bloğu: tam (tablo) | kisa (tek paragraf, "
                    "token tasarrufu). Kilide yazılır; sonraki kurulum/güncellemelerde korunur. Tek başına verilirse bloğu yeniler")
    ap.add_argument("--geri-al", nargs="?", const=True, default=None, help="son yedeğe (ya da adı verilen yedeğe) dön")
    ap.add_argument("--yedekler", action="store_true", help="yedekleri listele")
    ap.add_argument("--oner", help="ihtiyacı yaz; tüm kütüphane taranır")
    ap.add_argument("--adet", type=int, default=24)
    ap.add_argument("--kategori-basi", type=int, default=5, help="--oner: her kategoriden en fazla (0 = sınırsız)")
    ap.add_argument("--listele", action="store_true")
    ap.add_argument("--ara")
    ap.add_argument("--kategori")
    ap.add_argument("--teknoloji")
    ap.add_argument("--gizli", action="store_true", help="gizli katalogları (entegrasyon, repo-içi) da göster")
    ap.add_argument("--kuru", action="store_true", help="sadece ön kontrol raporu; hiçbir şey değişmez")
    ap.add_argument("--evet", action="store_true", help="uyarıları onayla (agent/etkileşimsiz kullanım)")
    ap.add_argument("--guvenlik-onay", action="store_true", dest="guvenlik_onay",
                    help="geçici klasör incelemesinde çıkan güvenlik uyarılarını (guvenlik-ag, guvenlik-veri, guvenlik-talimat, genele-yazabilir) görerek onayla")
    ap.add_argument("--zorla", action="store_true", help="hataları geç (önce yedek alınır)")
    ap.add_argument("--arac", choices=sorted(ARACLAR), help="proje hangi araçlarla açılacak: ortak (Claude + Codex + Antigravity + Cursor + "
                    "VS Code Copilot; varsayılan) | yalniz-claude (yalnız Claude; Cursor ve VS Code Copilot da .claude/skills'i okur); "
                    "eski adlar: ikisi = ortak, claude = yalniz-claude. Kurulu skiller yeni düzene göre yeniden kurulur")
    ap.add_argument("--araclar", action="store_true", help="yapay zeka araçları belgesi/sürüm kontrolü (yapay-zeka-araclari.json); salt okunur")
    ap.add_argument("--ozet-json", action="store_true", help="--araclar ile: stdout'a tek JSON nesnesi")
    ap.add_argument("--siki", action="store_true", help="--araclar ile: durum 'sorun' ise çıkış kodu 1")
    a = ap.parse_args()
    if (a.ozet_json or a.siki) and not a.araclar:
        ap.error("--ozet-json ve --siki yalnız --araclar ile kullanılır")
    if a.araclar:  # registry yüklenmeden (22 MB), proje gerekmeden
        return araclar_raporu(a)
    if a.proje and windows_mu():
        if a.program_skill or a.dondur:
            sys.exit("Programla gelen skiller Windows'a bağlanamaz: bağ bu Mac'teki program klasörünü gösterir. Windows'ta açılacak projeler için "
                     "skill kütüphanenin olduğu Mac'te kurulur (rehber/14 bölüm 5).")
        sys.exit("skill-ekle.py Windows'ta çalıştırılmaz (symlink, kill -0 ve Mac yolları). Skill ekleme/güncelleme kütüphanenin olduğu "
                 "Mac'te yapılır; Windows'ta açılan projeler için rehber/14 bölüm 5.")
    skiller = registry()

    if a.listele or (a.ara and not a.proje):
        return listele(a, skiller)
    if a.oner and not kurulum_istegi(a, planlayici=False):
        return oner(a, Path(a.proje).expanduser().resolve() if a.proje else None, skiller)
    if a.rapor and not a.proje:
        return rapor_komutu(a, None, skiller)
    if not a.proje:
        ap.error("proje klasörü gerekli")
    proje = Path(a.proje).expanduser().resolve()
    korunan = [g.resolve() for g in GLOBAL_KLASORLER.values()] + [KOK.resolve(), (Path.home() / ".openmontage").resolve(),
                                                                   (Path.home() / ".claude").resolve(), (Path.home() / ".codex").resolve()] + arac_korunan_yollar()
    if proje == Path.home().resolve() or any(proje == k or k in proje.parents for k in korunan):
        sys.exit(f"Güvenlik: {proje} bir proje klasörü değil (global skill klasörü, kütüphane ya da ev dizini).")
    if META in proje.parts:  # .skill-kutuphanesi/yedek/<zaman>/ içindeki eski anlık görüntüler proje değildir
        gercek = Path(*proje.parts[:proje.parts.index(META)])
        sys.exit(f"Güvenlik: {proje} bir yedek/meta klasörü, proje değil. Asıl proje: {gercek}")
    if not proje.is_dir():
        sys.exit(f"Klasör yok: {proje}")
    if a.rapor and not a.evet:
        return rapor_komutu(a, proje, skiller)
    gk = guncelleme_suruyor()
    if gk and (kurulum_istegi(a) or a.guncelle or a.yenile or a.arac or a.blok):
        sys.exit(f"BEKLE: kütüphane şu an aylık güncelleniyor ({gk['baslangic']}); onaylanmamış içerik projeye kurulmasın diye "
                 "kurulum/güncelleme birkaç dakika bekletiliyor. Bitince tekrar dene (--durum/--dogrula/--oner çalışır).")
    if a.durum:
        return durum(proje, skiller)
    if a.dogrula:
        return 1 if dogrula(proje, skiller) else 0
    if a.yedekler:
        for y in yedekler_listesi(proje):
            b = json_oku(y / "yedek.json", {})
            print(f"  {y.name}  {b.get('neden', '?')}")
        return 0
    if a.kuru and (a.yenile or a.geri_al or (a.blok and not (kurulum_istegi(a) or a.guncelle))):
        print(f"[kuru] Hiçbir şey değiştirilmedi. (yapılacak: {'yenile' if a.yenile else 'geri-al' if a.geri_al else 'blok'})")
        return 0
    if a.geri_al:
        return geri_al(a, proje)
    if a.yenile or (a.blok and not (kurulum_istegi(a) or a.guncelle)):
        kilit = kilit_oku(proje)
        if a.blok:
            kilit["blok"] = a.blok
        rapor = Rapor()
        proje_yapisi_kontrol(proje, kilit["roller"], rapor)
        if rapor.say("HATA"):
            rapor.yazdir()
            return 2
        kit_sk_y = [sk for kg in kit_kayitlari(kilit).values() for sk in (kg.get("skiller") or []) if dis_ad_gecerli(sk)]
        yedek = yedekle(proje, list(kilit["skiller"]) + list(dis_kayitlari(kilit)) + kit_sk_y, "yenile")

        def yenile_islem():
            for m in dis_yerlestir(proje, kilit) + fihrist_yerlestir(proje, kilit) + kit_yerlestir(proje, kilit):
                print(f"  ! {m}")
            tumunu_yaz(proje, kilit, skiller)
        guvenli_islem(proje, yedek, yenile_islem)
        return 1 if dogrula(proje, skiller) else 0
    if a.kaldir:
        return kaldir(a, proje, skiller)
    if a.arac and not kurulum_istegi(a):
        return arac_degistir(a, proje, skiller)
    if a.guncelle:
        return guncelle(a, proje, skiller)
    if not kurulum_istegi(a):
        ap.error("--profil, --rol, --skill, --fihrist-skill, --kit, --program-skill, --dondur veya --rapor ver")
    return ekle(a, proje, skiller)


def proje_raporunu_yenile():
    """Projede değişiklik yapan işlemden sonra notlar/proje-kullanimi.md'yi yeniler (proje bilgisinin tek yeri).
    Sadece projeler.json'daki tarama köklerinde/ek_projeler'de olan projeler rapora girer; geçici klasörler girmez."""
    salt_okur = {"--kuru", "--durum", "--dogrula", "--oner", "--listele", "--ara", "--yedekler", "--araclar", "--rapor"}
    if salt_okur & set(sys.argv):
        return
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("projekullanimi", Path(__file__).parent / "proje-kullanimi.py")
        pk = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pk)
        if pk.rapor_guncelle():
            print(f"Proje kullanım raporu yenilendi: {pk.RAPOR.relative_to(KOK)}")
            # Kütüphane çalışma ağacı kirli kalmasın (aylık güncelleme ve --birlestir temiz ağaç ister): SADECE bu dosya kaydedilir.
            # Güncelleme dalındayken ya da kilit varken kaydedilmez; push hiçbir zaman yapılmaz.
            import subprocess
            g = lambda *a: subprocess.run(["git", *a], cwd=KOK, capture_output=True, text=True)  # noqa: E731
            if g("branch", "--show-current").stdout.strip() == "master" and not guncelleme_suruyor():
                rel = str(pk.RAPOR.relative_to(KOK))
                if g("commit", "-q", "-m", "Proje kullanım raporu yenilendi (skill-ekle.py)", "--", rel).returncode == 0:
                    print("  (kütüphanede yalnızca bu dosya commit edildi; push yapılmadı)")
    except Exception as e:  # rapor yan üründür; kurulumu asla bozmaz
        print(f"UYARI: proje kullanım raporu yenilenemedi ({e}); elle: python3 araclar/proje-kullanimi.py")


if __name__ == "__main__":
    kod = main() or 0
    proje_raporunu_yenile()
    sys.exit(kod)
