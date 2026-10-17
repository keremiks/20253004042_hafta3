"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""
import itertools
import pytest
from uzay_oyunu.akis import fibonacci, yakit_gostergesi, satirlari_oku, ayristir, uzun_yolculuklar , rota_sayaci

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
def test_seyir_defteri_boru_hatti(tmp_path):
    """Görev 3: Boru hattının tembel (generator) çalıştığını ve doğru süzdüğünü test eder."""
    # Test için geçici bir dosya oluşturuyoruz
    dosya = tmp_path / "test_seyir.txt"
    dosya.write_text("dünya -> sirius 12\n#bakım molası\nsirius -> orion 8\n\n", encoding="utf-8")
    
    # Boru hattını kur
    satirlar = satirlari_oku(str(dosya))
    kayitlar = ayristir(satirlar)
    uzunlar = uzun_yolculuklar(kayitlar, 10)
    
    # 1. Tembellik Testi: Fonksiyonların liste değil üreteç (generator) döndüğünü kontrol et
    assert iter(satirlar) is satirlar
    assert iter(kayitlar) is kayitlar
    assert iter(uzunlar) is uzunlar
    
    # 2. Doğruluk Testi: Yorum satırı atlanmalı ve sadece yakıtı 10'dan büyük olan kalmalı
    sonuc = list(uzunlar)
    assert sonuc == [("dünya", "sirius", 12)]
def test_rota_sayaci():
    """Görev 4: Önbellekli rota sayacının doğru hesap yaptığını test eder."""
    baglantilar = {
        "dünya": ["mars", "venüs"],
        "mars": ["dünya"],
        "venüs": ["dünya"]
    }
    say = rota_sayaci(baglantilar)
    
    # 0 adım
    assert say("dünya", 0) == 1
    # 1 adım: dünya -> mars veya dünya -> venüs (2 rota)
    assert say("dünya", 1) == 2
    # 2 adım: dünya -> mars -> dünya veya dünya -> venüs -> dünya (2 rota)
    assert say("dünya", 2) == 2
    
    # Lru_cache'in çalıştığını kontrol edelim
    bilgi = say.cache_info()
    assert bilgi.misses > 0