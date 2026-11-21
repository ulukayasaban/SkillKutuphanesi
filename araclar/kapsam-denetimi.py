#!/usr/bin/env python3
"""Kapsam denetimi: yıldızlı repolardaki HER SKILL.md dosyasının ne olduğunu açıklar. Açıklanamayan varsa çıkış kodu 1.

Bağımsız kontrol: arşivi üreten koddan ayrı olarak, her repo için GitHub'dan kayıtlı commit'teki tam dosya ağacını
yeniden çeker ve içindeki tüm SKILL.md (büyük/küçük harf fark etmez) dosyalarını tek tek şunlarla eşleştirir:
  1) registry.json'daki bir skill (ana yol, araç sürümü veya birebir kopya olarak), ya da
  2) gerekçeli bir hariç tutma kararı (ayna / başka AI aracı / test / örnek / şablon).
Ayrıca kütüphane/araç (T5/T6) repolarında sonradan skill eklenmiş mi diye bakar.
GitHub'da artık bulunamayan (silinmiş/private) repo denetimi çökertmez: raporda 'erişilemeyen' olarak yazılır. Çözüm:
kaynaklar.json'da kaydın tipini 'KAYIP' yapmak (arşiv kopyası korunur); KAYIP kaynaklar GitHub'da hiç sorgulanmaz.

Çıktı: notlar/kapsam-denetimi.md
Kullanım: python3 araclar/kapsam-denetimi.py
"""
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ortak import (ARSIV_DISI_BOLUMLER, KAYNAKLAR, KOK, REGISTRY, YEREL_TIPLER, GhBulunamadi, json_oku, klon_temizle,  # noqa: E402
                   arsive_cekilir, medya_haric_kumesi, repo_agaci, yerel_agac)

ACIKLAMA = {
    "secildi": "arşivde (ana sürüm)",
    "arac-varyanti": "arşivde (Claude/Codex'e özel sürüm)",
    "ayri-surum": "arşivde (aynı adlı farklı içerik, ayrı skill)",
    "ayna-ayni": "birebir kopya (tek kopya yeter)",
    "ayna-baska-arac": "başka AI aracı (Cursor/Gemini/Kiro…) için kopya",
    "haric": "bilinçli hariç (test/örnek/şablon)",
    "fihristte": "fihristte (arşive alınmadı; kurulumda kaynaktan alınır)",
    "KARAR_BEKLIYOR": "yeni/kapsam dışı skill: arşive alınmadı, karar bekliyor (kaynaklar.json: dahil'e ekle ya da haric'e yaz)",
}


def agac_al(repo, sha=None):
    """repo_agaci; repo GitHub'da yoksa (404/422: silinmiş, private ya da commit yeniden yazılmış) None döner, çökmez."""
    try:
        return repo_agaci(repo, sha)[1]
    except GhBulunamadi:
        return None


def main():
    reg = json_oku(REGISTRY)
    denetim = reg.get("denetim", {})
    kayitlar = json_oku(KAYNAKLAR)["repolar"]
    arsiv_repolari = sorted({k["repo"] for k in kayitlar if arsive_cekilir(k)})
    fihrist_tutulan = {}
    for repo in arsiv_repolari:
        rk = [k for k in kayitlar if k["repo"] == repo and arsive_cekilir(k)]
        if rk and all(k.get("bolum") == "fihrist" for k in rk):
            fihrist_tutulan[repo] = {y for k in rk for y in (k.get("arsivde_tut") or []) if isinstance(y, str)}
    yerel_kayit = {k["repo"]: k for k in kayitlar if k["tip"] in YEREL_TIPLER}  # T7 kendi/, T8 site/: GitHub'a sorulmaz
    kayip_repolari = sorted({k["repo"] for k in kayitlar if k["tip"] == "KAYIP"})
    # bolum fihrist/katalog (dev koleksiyon, kit): skil dosyaları BİLEREK arşiv dışıdır; içlerindeki SKILL.md sorun sayılmaz (fihrist/ ve kitler.json tutar)
    arsiv_disi_repolari = sorted({k["repo"] for k in kayitlar if k.get("bolum") in ARSIV_DISI_BOLUMLER} - set(arsiv_repolari) - set(kayip_repolari))
    referans_repolari = sorted({k["repo"] for k in kayitlar} - set(arsiv_repolari) - set(kayip_repolari) - set(arsiv_disi_repolari))
    erisilemeyen = []
    yol_index, varyant_index = set(), set()
    for s in reg["skiller"]:
        for arac, v in (s.get("varyantlar") or {}).items():
            if (KOK / v / "SKILL.md").exists():
                varyant_index.add((s["repo"], arac))

        yol_index.add((s["repo"], s["kaynak_yol"]))
        for kk in s.get("kopya_kaynaklar", []):
            r, _, y = kk.partition(":")
            yol_index.add((r, "" if y == "." else y))

    sorunlar, satirlar, toplam, bekleyen = [], [], Counter(), []
    for s in reg["skiller"]:
        if not (KOK / s["yol"] / "SKILL.md").exists():
            sorunlar.append(f"registry'de var ama arşivde SKILL.md yok: {s['yol']}")
    for repo in arsiv_repolari:
        d = denetim.get(repo)
        if not d:
            sorunlar.append(f"{repo}: denetim kaydı yok (kaynak-cek çalışmamış)")
            continue
        if repo in yerel_kayit:  # yerel kaynak: diskteki güncel kendi/ ya da site/ klasörü (düzenlenmiş ama işlenmemiş skill burada görünür)
            ayar_k = json_oku(KAYNAKLAR)
            govde = {"tree": yerel_agac(KOK / yerel_kayit[repo]["yerel"],
                                        ayar_k["skill_ici_haric"] + yerel_kayit[repo].get("dosya_haric", []),
                                        tam_haric=medya_haric_kumesi(yerel_kayit[repo]))[0],
                     "truncated": False}
        else:
            govde = agac_al(repo, d["commit"])  # API kapalıysa git ile (bağımsız sayım yine yapılır)
        if govde is None:
            erisilemeyen.append(repo)
            continue
        klon_temizle(govde)
        if govde.get("truncated"):
            sorunlar.append(f"{repo}: GitHub ağacı kesik, bağımsız sayım yapılamadı")
        gercek = [e["path"] for e in govde["tree"] if e["type"] == "blob" and e["path"].split("/")[-1].lower() == "skill.md"]
        sayac = Counter()
        for p in gercek:
            klasor = p.rsplit("/", 1)[0] if "/" in p else ""
            if repo in fihrist_tutulan and klasor not in fihrist_tutulan[repo]:
                sayac["fihristte"] += 1
                continue
            karar = d["skill_md"].get(p)
            if karar == "dahil-disi":
                # Hiçbir kaydın kapsamına girmeyen skill (genelde upstream'in sonradan eklediği yeni skill): arşive ALINMAZ,
                # ama aylık güncellemeyi de durdurmaz; raporda "karar bekliyor" olarak görünür (dahil'e ekle ya da haric'e yaz).
                bekleyen.append(f"{repo}: {p}")
                sayac["KARAR_BEKLIYOR"] += 1
                continue
            if karar is None:
                sorunlar.append(f"{repo}: AÇIKLANAMAYAN SKILL.md (denetimde hiç kaydı yok) -> {p}")
                sayac["ACIKLANAMAYAN"] += 1
                continue
            tur = karar.split(":")[0]
            sayac[tur] += 1
            if tur == "fihristte":
                sorunlar.append(f"{repo}: arşiv/arsivde_tut kapsamında ama denetim kararı 'fihristte' -> {p}")
            if tur == "arac-varyanti" and (repo, karar.split(":")[1]) not in varyant_index:
                sorunlar.append(f"{repo}: araç sürümü kararı var ama arşivde sürüm yok -> {p}")
            if tur in ("secildi", "ayri-surum"):
                if (repo, klasor) not in yol_index:
                    sorunlar.append(f"{repo}: arşive seçildi ama registry'de yok -> {p}")
        if repo in fihrist_tutulan:
            for y in sorted(fihrist_tutulan[repo]):
                if (repo, y) not in yol_index:
                    sorunlar.append(f"{repo}: arsivde_tut yolu registry'de yok -> {y or '.'}")
        for p in d["skill_md"]:
            if p not in gercek:
                sorunlar.append(f"{repo}: denetimde var ama ağaçta yok -> {p}")
        toplam.update(sayac)
        satirlar.append((repo, len(gercek), sayac))

    yeni_skill, bagli_skill = [], []
    # Program kaydı olan ve kartında skill_koku dolu olan referans repo: skili program bağıyla verilir (K-28, K-46)
    try:
        _kartlar = json_oku(KOK / "programlar.json").get("programlar", {})
    except Exception:  # noqa: BLE001
        _kartlar = {}
    bagli_program_repolari = {k["repo"] for k in kayitlar if isinstance(k.get("program"), str)
                              and isinstance((_kartlar.get(k["program"]) or {}).get("skill_koku"), str)
                              and (_kartlar.get(k["program"]) or {}).get("skill_koku").strip()}
    ref_haric = defaultdict(list)
    for k in kayitlar:
        if k.get("bolum") == "not":
            for pat in (k.get("haric") or []):
                if isinstance(pat, str):
                    ref_haric[k["repo"]].append(re.compile(pat))
    for repo in referans_repolari:
        g = agac_al(repo)  # API kapalıysa git ile
        if g is None:
            erisilemeyen.append(repo)
            continue
        klon_temizle(g)
        desenler = ref_haric.get(repo, [])
        n = sum(
            1 for e in g.get("tree", [])
            if e["type"] == "blob"
            and e["path"].split("/")[-1].lower() == "skill.md"
            and not any(p.search(e["path"]) for p in desenler)
        )
        if n and repo in bagli_program_repolari:
            # Programın kendi paketiyle gelen skil projelere BAĞ olarak verilir (kart: skill_koku), arşive alınmaz: sorun değil, bilgi
            bagli_skill.append((repo, n))
        elif n:
            yeni_skill.append((repo, n))
            sorunlar.append(f"{repo}: referans (T5/T6) reposunda {n} SKILL.md var -> kaynaklar.json'a skill kaydı ekle")

    out = ["# Kapsam Denetimi", "",
           f"> `araclar/kapsam-denetimi.py` üretir · {date.today().isoformat()} · Bağımsız kontrol: her repo için "
           "GitHub'daki tam dosya ağacı yeniden çekilip içindeki tüm SKILL.md dosyaları tek tek açıklandı.", "",
           f"**Sonuç: {'✅ Açıklanamayan skill yok' if not sorunlar else f'❌ {len(sorunlar)} sorun'}"
           f"{f' · ⚠️ {len(erisilemeyen)} erişilemeyen kaynak' if erisilemeyen else ''}** · "
           f"Taranan SKILL.md: {sum(n for _, n, _ in satirlar)} · Arşivdeki skill kaydı: {len(reg['skiller'])} · "
           f"Bileşen (komut/agent): {len(reg.get('bilesenler', []))}", "",
           "| Karar | Sayı | Anlamı |", "|---|---|---|"]
    for k, v in toplam.most_common():
        out.append(f"| {k} | {v} | {ACIKLAMA.get(k, '')} |")
    out += ["", "## Repo bazında", "", "| Repo | SKILL.md | Dağılım |", "|---|---|---|"]
    for repo, n, s in satirlar:
        out.append(f"| {repo} | {n} | " + ", ".join(f"{k} {v}" for k, v in s.most_common()) + " |")
    out += ["", "## Referans repoları (T5/T6)", "",
            f"{len(referans_repolari)} repo tarandı; " +
            ("içlerinde skill yok." if not yeni_skill else "skill bulunanlar: " + ", ".join(f"{r} ({n})" for r, n in yeni_skill))
            + (" Program bağıyla verilen (arşive alınmayan) skiller: " + ", ".join(f"{r} ({n})" for r, n in bagli_skill) + "." if bagli_skill else "")]
    if arsiv_disi_repolari:
        out += ["", "## Arşive çekilmeyen kaynaklar (bolum fihrist/katalog)", "",
                f"{len(arsiv_disi_repolari)} repo bilerek arşiv dışı; içlerindeki SKILL.md dosyaları sorun sayılmaz: " + ", ".join(arsiv_disi_repolari)]
    if kayip_repolari:
        out += ["", "## KAYIP kaynaklar (GitHub'da yok; arşiv kopyası korunuyor, sorgulanmadı)", ""] + [f"- {x}" for x in kayip_repolari]
    if erisilemeyen:
        out += ["", f"## Erişilemeyen kaynaklar ({len(erisilemeyen)})", "",
                "GitHub'da bulunamadı (silinmiş, private olmuş ya da commit geçmişi yeniden yazılmış). Denetlenemedi. Çözüm: "
                "`kaynaklar.json`'da kaydın `tip`ini `KAYIP` yap (arşiv kopyası korunur); kaydı silme.", ""] + [f"- {x}" for x in erisilemeyen]
    hariclar = defaultdict(list)
    for repo, d in denetim.items():
        for p, k in d["skill_md"].items():
            if k.startswith("haric"):
                hariclar[repo].append(f"`{p}` ({k.split(':', 1)[1]})")
    if hariclar:
        out += ["", "## Bilinçli hariç tutulanlar (gerekçeli)", ""]
        for repo, l in hariclar.items():
            out.append(f"- **{repo}**: " + ", ".join(l[:20]) + (f" … (+{len(l) - 20})" if len(l) > 20 else ""))
    if bekleyen:
        out += ["", f"## Karar bekleyen yeni skiller ({len(bekleyen)})", "",
                "Hiçbir kayıt kapsamına girmiyor (upstream sonradan eklemiş olabilir). Almak için `kaynaklar.json` → repo kaydının `dahil` "
                "listesine ekle; almamak için `haric`e yaz. Bu skiller arşivde YOK ve güncellemeyi durdurmaz.", ""] + [f"- {x}" for x in bekleyen]
    if sorunlar:
        out += ["", "## Sorunlar", ""] + [f"- {x}" for x in sorunlar]
    hedef, yeni = KOK / "notlar" / "kapsam-denetimi.md", "\n".join(out) + "\n"
    tarihsiz = lambda m: re.sub(r"\d{4}-\d{2}-\d{2}", "", m, count=1)  # noqa: E731
    if not hedef.exists() or tarihsiz(hedef.read_text(encoding="utf-8")) != tarihsiz(yeni):
        hedef.write_text(yeni, encoding="utf-8")  # sadece içerik değişince yaz (gün değişti diye çalışma ağacı kirlenmesin)
    for x in bekleyen:
        print("KARAR BEKLİYOR:", x)
    for x in erisilemeyen:
        print("ERİŞİLEMEYEN KAYNAK (kaynaklar.json'da tip: KAYIP yap):", x)
    for x in sorunlar:
        print("SORUN:", x)
    print(f"Taranan SKILL.md: {sum(n for _, n, _ in satirlar)} · sorun: {len(sorunlar)} · erişilemeyen: {len(erisilemeyen)} · "
          f"dağılım: {dict(toplam)}")
    sys.exit(1 if sorunlar else 0)


if __name__ == "__main__":
    main()
