"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""

from typing import Iterator

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