"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""

from typing import Iterator

def fibonacci() -> Iterator[int]:
    """
    Sonsuz bir Fibonacci dizisi üreten üreteç fonksiyonu.
    Değerleri bellekte bekletmeyerek her çağrıda bir sonraki sayıyı üretir.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b