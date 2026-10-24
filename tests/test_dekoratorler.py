"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""
from uzay_oyunu.dekoratorler import sure_olc, say

def test_sure_olc_sonuc_degismiyor():
    @sure_olc
    def topla(a, b):
        return a + b
    assert topla(3, 5) == 8

def test_sure_olc_kwargs_calisiyor():
    @sure_olc
    def selam_ver(isim, mesaj="Merhaba"):
        return f"{mesaj} {isim}"
    assert selam_ver("Kerem", mesaj="Selam") == "Selam Kerem"

def test_sure_olc_isim_ve_belge_korunuyor():
    @sure_olc
    def ornek_fonk():
        """Bu bir örnek fonksiyondur."""
        pass
    assert ornek_fonk.__name__ == "ornek_fonk"
    assert ornek_fonk.__doc__ == "Bu bir örnek fonksiyondur."

def test_say_dekoratoru():
    @say
    def carp(a, b):
        return a * b
        
    carp(2, 3)
    carp(4, 5)
    assert carp.cagri == 2