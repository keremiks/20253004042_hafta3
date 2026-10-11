# Ad: Muhammed Kerem Acar
# Numara: 20253004042
# Tarih: 11/10/2026
# GitHub Deposu: https://github.com/keremiks/20253004042_hafta3

import json
import os

def galaksi_kur(gezegenler: list[str], baglantilar: dict[str, list[str]], baslangic: str, **kwargs) -> dict:
    """Galaksi haritasini kurar. Baslangic gezegeni listede yoksa ValueError olur."""
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde yok!")
        
    yakit = kwargs.get("yakit", 50)
    
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }

def veri_yukle(dosya_adi: str = "galaksi.json") -> dict:
    """JSON dosyasini okur ve galaksi_kur fonksiyonuna **veri seklinde iletir."""
    klasor = os.path.dirname(os.path.abspath(__file__))
    tam_yol = os.path.join(klasor, dosya_adi)
    
    with open(tam_yol, "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
        
    return galaksi_kur(**veri)