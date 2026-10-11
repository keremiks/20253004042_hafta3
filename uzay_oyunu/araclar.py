# Ad: Muhammed Kerem Acar
# Numara: 20253004042
# Tarih: 11/10/2026
# GitHub Deposu: https://github.com/keremiks/20253004042_hafta3
import time

def hamle_sayaci():
    """Her cagrildiginda bir artan sayac dondurur (Closure)."""
    sayac = 0
    def arttir():
        nonlocal sayac
        sayac += 1
        return sayac
    return arttir

def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri baglanti sayisina gore azalan, esitlikte alfabetik sirayla dondurur."""
    baglantilar = galaksi.get("baglantilar", {})
    gezegenler = list(baglantilar.keys())
    
    # lambda ile once baglanti sayisinin eksilisi (azalan sira), sonra isme gore (alfabetik) siralama
    sirali = sorted(gezegenler, key=lambda p: (-len(baglantilar[p]), p))
    return sirali

# Bonus (+10 Puan)
def sure_olc(fonksiyon):
    """Verilen fonksiyonun calisma suresini olcen sarmalayici."""
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"{fonksiyon.__name__} fonksiyonu {bitis - baslangic:.6f} saniyede calisti.")
        return sonuc
    return sarmalayici