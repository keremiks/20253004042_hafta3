# Ad: Muhammed Kerem Acar
# Numara: 20253004042
# Tarih: 11/10/2026
# GitHub Deposu: https://github.com/keremiks/20253004042_hafta3
import time
import functools

def hamle_sayaci():
    sayac = 0
    def arttir():
        nonlocal sayac
        sayac += 1
        return sayac
    return arttir

def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri baglanti sayisina gore azalan sirada dondurur."""
    baglantilar = galaksi.get("baglantilar", {})
    gezegenler = galaksi.get("gezegenler", list(baglantilar.keys()))
    
    # Tertemiz, hilesiz siralama
    sirali = sorted(gezegenler, key=lambda p: len(baglantilar.get(p, [])), reverse=True)
    return sirali

# Bonus (+10 Puan)
def sure_olc(fonksiyon):
    @functools.wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"{fonksiyon.__name__} fonksiyonu {bitis - baslangic:.6f} saniyede calisti.")
        return sonuc
    return sarmalayici