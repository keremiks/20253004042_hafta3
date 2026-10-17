"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""

from typing import Iterator 
from functools import lru_cache

def fibonacci() -> Iterator[int]:
    """
    Sonsuz bir Fibonacci dizisi üreten üreteç (generator) fonksiyonu.
    Değerleri bellekte tutmadan her çağrıda bir sonraki sayıyı üretir.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """
    Her çağrıda yakıtı tüketim kadar azaltan üreteç.
    Yakıt 0 veya altına düştüğünde 0 üretir ve durur.
    """
    while yakit > 0:
        yakit -= tuketim
        if yakit <= 0:
            yakit = 0
            yield yakit
            break
        yield yakit

def satirlari_oku(yol: str):
    """Boş satırları ve # ile başlayan yorum satırlarını atlayarak okur."""
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz

def ayristir(satirlar):
    """Satırları (kaynak, hedef, yakit) demetine dönüştürür."""
    for satir in satirlar:
        parcalar = satir.split()
        if len(parcalar) >= 4:
            kaynak = parcalar[0]
            hedef = parcalar[2]
            yakit = int(parcalar[3])
            yield (kaynak, hedef, yakit)

def uzun_yolculuklar(kayitlar, esik: int):
    """Yakıtı eşikten büyük olan yolculukları süzer."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield (kaynak, hedef, yakit)

def rota_sayaci(baglantilar: dict):
    """Verilen bağlantılara göre n adımlık rota sayısını hesaplayan fonksiyonu döndürür."""
    
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """Gezegenden başlayıp tam 'adim' sayısında biten farklı rota sayısını bulur."""
        if adim == 0:
            return 1  # 0 adım kaldıysa hedefe ulaştık demektir (1 geçerli rota)
            
        toplam = 0
        for komsu in baglantilar.get(gezegen, []):
            toplam += rota_sayisi(komsu, adim - 1)
        return toplam
        
    return rota_sayisi