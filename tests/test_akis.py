"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""
import itertools
import pytest
from uzay_oyunu.akis import fibonacci, yakit_gostergesi

def test_fibonacci_ilk_uc():
    """next() ile ilk üç değerin (0, 1, 1) doğru geldiğini test eder."""
    g = fibonacci()
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 1

def test_fibonacci_islice():
    """itertools.islice ile ilk 12 değerin doğru geldiğini test eder."""
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(itertools.islice(fibonacci(), 12)) == beklenen

def test_fibonacci_takewhile():
    """itertools.takewhile ile 100'den küçük değerlerin doğru geldiğini test eder."""
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(itertools.takewhile(lambda x: x < 100, fibonacci())) == beklenen

def test_fibonacci_tek_kullanimlik():
    """Üretecin tek kullanımlık (exhaustible) olduğunu test eder."""
    g = fibonacci()
    liste1 = list(itertools.islice(g, 5))
    liste2 = list(itertools.islice(g, 5))
    
    assert liste1 == [0, 1, 1, 2, 3]
    assert liste2 == [5, 8, 13, 21, 34]
    assert liste1 != liste2

def test_yakit_gostergesi():
    """Yakıt göstergesi üretecinin PDF'teki değerleri verdiğini test eder."""
    beklenen = [70, 40, 10, 0]
    assert list(yakit_gostergesi(100, 30)) == beklenen

def test_yakit_gostergesi_stopiteration():
    """Yakıt bittikten sonra next() ile StopIteration fırlattığını test eder."""
    g = yakit_gostergesi(10, 5)
    assert next(g) == 5
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)