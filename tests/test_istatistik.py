"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""
from uzay_oyunu.istatistik import (
    buyuk_harfli_map, buyuk_harfli_liste,
    iki_baglantili_filter, iki_baglantili_liste,
    toplam_baglanti_reduce, toplam_baglanti_sum, hizli_yolculuk
)

def test_buyuk_harfli():
    gezegenler = ["dünya", "mars", "venüs"]
    beklenen = ["DÜNYA", "MARS", "VENÜS"]
    assert buyuk_harfli_map(gezegenler) == beklenen
    assert buyuk_harfli_liste(gezegenler) == beklenen

def test_iki_baglantili():
    baglantilar = {"dünya": ["mars", "venüs"], "mars": ["dünya"], "venüs": ["dünya"]}
    assert iki_baglantili_filter(baglantilar) == ["dünya"]
    assert iki_baglantili_liste(baglantilar) == ["dünya"]

def test_toplam_baglanti():
    baglantilar = {"dünya": ["mars", "venüs"], "mars": ["dünya"], "venüs": ["dünya"]}
    assert toplam_baglanti_reduce(baglantilar) == 4
    assert toplam_baglanti_sum(baglantilar) == 4

def test_hizli_yolculuk():
    assert hizli_yolculuk("mars") == "mars hedefine 3 hızıyla gidiliyor."