#!/usr/bin/env python3
"""P22 testleri: Faz 2 Adım 2 — yeni-repo onaysız KESİN akışı, konu-takip.json kuyruğu,
K-58 güçlü işaret otomatik ret, savunma istisnası ve tek zayıf kelimeli repo -> gri_guvenlik.

Ağ kullanmaz, gerçek kütüphaneye/ev klasörüne yazmaz.
Son satır 'N/N test geçti'; çıkış 0 yalnız hepsi geçerse.
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
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


yr = yukle(ARACLAR / "yeni-repo.py", "yeni_repo_p22")
kt = yukle(ARACLAR / "konu-takip.py", "konu_takip_p22")
dg = yukle(ARACLAR / "dogrula.py", "dogrula_p22")


def t(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul)))
    print(("  ✅ " if kosul else "  ❌ ") + ad + ("" if kosul else f"\n     {str(ayrinti)[-500:]}"))


def sahte_git_kok(dal="yeni-surec-faz2", kirli=False):
    k = Path(tempfile.mkdtemp(prefix="p22-"))
    GECICI.append(k)
    (k / "kaynaklar.json").write_text(json.dumps({"repolar": []}), encoding="utf-8")
    (k / "registry.json").write_text(json.dumps({"skiller": [
        {"id": "var-olan", "ad": "var-olan", "repo": "eski/repo"}
    ]}), encoding="utf-8")
    (k / "konu-takip.json").write_text(json.dumps({"degerlendirilen": {}, "konular": {}, "izlenen": {}}), encoding="utf-8")
    (k / "kendi" / "benim-skilim").mkdir(parents=True)
    (k / "kendi" / "benim-skilim" / "SKILL.md").write_text("---\nname: benim-skilim\n---\n", encoding="utf-8")
    e = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t",
             GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_SYSTEM="/dev/null")
    subprocess.run(["git", "init", "-q", "-b", dal], cwd=k, env=e, check=True)
    subprocess.run(["git", "add", "-A"], cwd=k, env=e, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "ilk"], cwd=k, env=e, check=True)
    if kirli:
        (k / "kirli.txt").write_text("x", encoding="utf-8")
    return k


def blob(yol, size=100):
    return {"path": yol, "type": "blob", "size": size}


# 1. Ön-kapı kontrolü
k_temiz = sahte_git_kok("yeni-surec-faz2", kirli=False)
k_kirli = sahte_git_kok("yeni-surec-faz2", kirli=True)
k_master = sahte_git_kok("master", kirli=False)
t("1a ön-kapı: temiz faz dalında geçer", yr.on_kapi_kontrol(k_temiz)[0] is True)
t("1b ön-kapı: kirli ağaçta durur", yr.on_kapi_kontrol(k_kirli)[0] is False)
t("1c ön-kapı: master dalında durur", yr.on_kapi_kontrol(k_master)[0] is False)

try:
    yr.otomatik_isle(k_kirli, [], uygula=True)
    t("1d kirli ağaçta otomatik_isle(uygula=True) hata verir", False)
except RuntimeError:
    t("1d kirli ağaçta otomatik_isle(uygula=True) hata verir", True)

# 2. Liste farkı
lf = yr.liste_farki(
    ["yeni/repo", "eski/repo", "red/repo", "kuy/repo", "eski/tasinan", "yok/404"],
    {"repolar": [{"repo": "eski/repo"}]},
    {"degerlendirilen": {"red/repo": {"karar": "reddedildi"}}, "kuyruk": {"kuy/repo": {"durum": "bekliyor"}}},
    yonlendirmeler={"eski/tasinan": "yeni/tasinan"},
    kayip_404=["yok/404"],
)
t("2 liste_farki: yeni, degisen, 301 ve 404 doğru ayrılır",
  lf["yeni"] == ["yeni/repo"] and lf["degisen"] == ["eski/repo"]
  and lf["yonlendirilen_301"] == {"eski/tasinan": "yeni/tasinan"} and lf["kesin_404"] == ["yok/404"], lf)

# 3. K-58 güçlü işaretler, savunma istisnası ve tek zayıf kelime -> gri_guvenlik
g_k58_coklu = yr.guvenlik_siniflandir("x/red", "Automated reverse shell and credential dump toolkit", [], {})
t("3a çoklu güçlü saldırı işareti -> K-58", g_k58_coklu[0] == "K-58", g_k58_coklu)

g_k58_etiket = yr.guvenlik_siniflandir("x/pt", "Security helper", [], {}, konular=["pentest"])
t("3b net saldırgan konu etiketi ('pentest') -> K-58", g_k58_etiket[0] == "K-58", g_k58_etiket)

g_zayif = yr.guvenlik_siniflandir("x/payload-helper", "Inspect HTTP payload schema in tests", [], {})
t("3c tek zayıf kelime ('payload') -> K-58 DEĞİL, gri_guvenlik", g_zayif[0] == "gri_guvenlik", g_zayif)

g_zayif2 = yr.guvenlik_siniflandir("x/exploit-notes", "Notes about a fixed exploit", [], {})
t("3d tek zayıf kelime ('exploit') -> K-58 DEĞİL, gri_guvenlik", g_zayif2[0] == "gri_guvenlik", g_zayif2)

g_savunma = yr.guvenlik_siniflandir(
    "org/sec-audit", "OWASP hardening, vulnerability scan and dependency check skill",
    [blob("SKILL.md")], {"SKILL.md": "---\nname: sec-audit\n---\nRun security audit and secret scan.\n"},
    konular=["security", "devsecops"],
)
t("3e masum savunma reposu -> temiz (K-58 ve gri değil)", g_savunma[0] == "temiz", g_savunma)

g_gri = yr.guvenlik_siniflandir("x/proxy", "Local proxy and mitmproxy traffic inspector", [], {})
t("3f gri alan (local proxy / mitmproxy) -> gri_guvenlik", g_gri[0] == "gri_guvenlik", g_gri)

# 4. Hafif Kapı 10 sıralı kural ve KESİN otomatik kayıt
sha40 = "a" * 40
girdiler = [
    {"repo": "x/k58", "meta": {"aciklama": "Cobalt strike and mimikatz c2 server", "lisans": "MIT", "commit": sha40},
     "agac": [blob("SKILL.md")], "icerikler": {"SKILL.md": "---\nname: k58\n---\n"}},
    {"repo": "x/savunma", "meta": {"aciklama": "OWASP security audit and hardening", "lisans": "MIT", "commit": sha40},
     "agac": [blob("SKILL.md")], "icerikler": {"SKILL.md": "---\nname: sec-audit\n---\n"}},
    {"repo": "x/zayif-payload", "meta": {"aciklama": "Inspect webhook payload", "lisans": "MIT", "commit": sha40},
     "agac": [blob("SKILL.md")], "icerikler": {"SKILL.md": "---\nname: wh\n---\n"}},
    {"repo": "x/lisanssiz", "meta": {"aciklama": "No license skill", "lisans": None, "commit": sha40},
     "agac": [blob("SKILL.md")], "icerikler": {"SKILL.md": "---\nname: nl\n---\n"}},
    {"repo": "x/bos-aciklama", "meta": {"aciklama": "", "lisans": "MIT", "commit": sha40},
     "agac": [blob("SKILL.md")], "icerikler": {"SKILL.md": "---\nname: ba\n---\n"}},
    {"repo": "x/claude-md-only", "meta": {"aciklama": "Only CLAUDE.md", "lisans": "MIT", "commit": sha40},
     "agac": [blob("CLAUDE.md")], "icerikler": {}},
    {"repo": "x/cakisan-kendi", "meta": {"aciklama": "Collides with local", "lisans": "MIT", "commit": sha40},
     "agac": [blob("SKILL.md")], "icerikler": {"SKILL.md": "---\nname: benim-skilim\n---\n"}},
    {"repo": "x/cakisan-reg", "meta": {"aciklama": "Collides with registry", "lisans": "MIT", "commit": sha40},
     "agac": [blob("SKILL.md")], "icerikler": {"SKILL.md": "---\nname: var-olan\n---\n"}},
    {"repo": "x/urun-aday", "meta": {"aciklama": "App with skills", "lisans": "MIT", "commit": sha40},
     "agac": [blob("skills/a/SKILL.md"), blob("skills/b/SKILL.md")] + [blob(f"src/m{i}.ts") for i in range(25)],
     "icerikler": {"skills/a/SKILL.md": "---\nname: ua\n---\n", "skills/b/SKILL.md": "---\nname: ub\n---\n"}},
    {"repo": "x/medya-skil", "meta": {"aciklama": "Video skill", "lisans": "MIT", "commit": sha40},
     "agac": [blob("SKILL.md"), blob("demo.mp4", 5 * 1024 * 1024)],
     "icerikler": {"SKILL.md": "---\nname: ms\n---\n"}},
]

kuru = yr.otomatik_isle(k_temiz, girdiler, uygula=False, bugun="2026-11-21")
t("4a kuru mod diske yazmaz",
  json.loads((k_temiz / "kaynaklar.json").read_text(encoding="utf-8"))["repolar"] == []
  and len(kuru["otomatik"]) == 2 and len(kuru["reddedilen_k58"]) == 1 and len(kuru["kuyruk"]) == 7, kuru)

uyg = yr.otomatik_isle(k_temiz, girdiler, uygula=True, bugun="2026-11-21")
kay_son = json.loads((k_temiz / "kaynaklar.json").read_text(encoding="utf-8"))["repolar"]
kt_son = json.loads((k_temiz / "konu-takip.json").read_text(encoding="utf-8"))
t("4b uygula=True: masum savunma ve medya-skil kim='kural' ile kaydedildi, medya dışlandı",
  len(kay_son) == 2
  and all(x["onay"]["kim"] == "kural" and x["tip"] == "T1" and x["bolum"] == "arsiv" for x in kay_son)
  and "demo.mp4" in (kay_son[1].get("medya_haric") or {}), kay_son)
t("4c K-58 otomatik ret degerlendirilen'e yazıldı, zayıf 'payload' ise gri_guvenlik kuyruğunda",
  kt_son["degerlendirilen"]["x/k58"]["karar"] == "reddedildi"
  and kt_son["degerlendirilen"]["x/k58"]["neden"] == "K-58"
  and kt_son["kuyruk"]["x/zayif-payload"]["durum"] == "bekliyor"
  and kt_son["kuyruk"]["x/zayif-payload"]["neden"] == "gri_guvenlik", kt_son)

nedenler = {v["neden"] for v in kt_son["kuyruk"].values()}
t("4d tüm beklenen kuyruk nedenleri üretildi (lisans_yok, gri_guvenlik, aciklama_veya_skill_yok, tur_aday, ad_cakismasi, K-58)",
  {"K-58", "lisans_yok", "gri_guvenlik", "aciklama_veya_skill_yok", "tur_aday", "ad_cakismasi"} <= nedenler, nedenler)

oz = kt.kuyruk_ozeti(kt_son)
t("4e kuyruk_ozeti 7 bekleyen kaydı toplu raporda gruplar", oz["toplam_bekleyen"] == 7 and "x/zayif-payload" in oz["mesaj"], oz)

# 5. dogrula _e10_konu_takip_kuyruk ve konu-takip karar güncellemesi
h_d, u_d = dg.kayit_semalari_denetimi(k_temiz)
t("5a dogrula _e10_konu_takip_kuyruk geçerli kuyrukta sessiz", h_d == [] and u_d == [], (h_d, u_d))
kt.kuyruk_karar_ver(kt_son, "x/lisanssiz", "karar_verildi", "sonra lisans geldi", bugun="2026-11-21")
t("5b kuyruk_karar_ver durumu karar_verildi yapar", kt_son["kuyruk"]["x/lisanssiz"]["durum"] == "karar_verildi")
kt_son["kuyruk"]["x/lisanssiz"]["neden"] = "bilinmeyen_neden"
(k_temiz / "konu-takip.json").write_text(json.dumps(kt_son), encoding="utf-8")
h_d2, u_d2 = dg.kayit_semalari_denetimi(k_temiz)
t("5c dogrula geçersiz kuyruk nedenini UYARI olarak yakalar", h_d2 == [] and any("geçersiz neden" in x for x in u_d2), (h_d2, u_d2))

for g in GECICI:
    shutil.rmtree(g, ignore_errors=True)
basarisiz = [a for a, ok in SONUC if not ok]
print(f"\n{len(SONUC) - len(basarisiz)}/{len(SONUC)} test geçti")
sys.exit(1 if basarisiz else 0)
