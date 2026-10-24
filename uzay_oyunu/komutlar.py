"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""

KOMUTLAR = {}

def komut(ad, aciklama=""):
    """Komutları KOMUTLAR sözlüğüne kaydeden dekoratör."""
    def sarmalayici(fonk):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten kayitli!")
        
        KOMUTLAR[ad] = (fonk, aciklama)
        return fonk
    return sarmalayici

@komut("envanter", "eşyalarını gösterir")
def envanter_komutu(durum):
    esyalar = []
    if durum.get("credits"): esyalar.append("bol kredi")
    if durum.get("engines"): esyalar.append("hiper motor")
    if durum.get("copilot"): esyalar.append("yetenekli bir pilot")
    
    if not esyalar:
        return ""
    return "Sende: " + ", ".join(esyalar)

@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita_komutu(durum):
    su_anki_konum = durum.get("konum")
    baglantilar = durum.get("baglantilar", {})
    hedefler = baglantilar.get(su_anki_konum, [])
    return ", ".join(hedefler)

@komut("yardim", "komutları listeler")
def yardim_komutu(durum):
    satirlar = []
  
    for k_ad in sorted(KOMUTLAR.keys()):
        _, k_aciklama = KOMUTLAR[k_ad]
        satirlar.append(f"{k_ad} {k_aciklama}")
    return "\n".join(satirlar)