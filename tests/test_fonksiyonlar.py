# Ad: Muhammed Kerem Acar
# Numara: 20253004042
# Tarih: 11/10/2026
# GitHub Deposu: https://github.com/keremiks/20253004042_hafta3

import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu
from uzay_oyunu.galaksi import galaksi_kur, veri_yukle
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler

def test_envanter_metni():
    """envanter_metni dogru ciktilari dondurur."""
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"
    assert envanter_metni(False, False, False) == ""

def test_hedef_menusu():
    """hedef_menusu numarali menu dondurur."""
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen

def test_galaksi_kur():
    """galaksi_kur kurulumunu ve varsayilan yakiti test eder."""
    g = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g["konum"] == "mars"
    assert g["yakit"] == 50

def test_galaksi_kur_hata():
    """Gecersiz baslangic gezegeninde ValueError firlatir."""
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "dünya")

def test_veri_yukle():
    """galaksi.json dosyasinin yuklendigini test eder."""
    g = veri_yukle()
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100

def test_en_bagli_gezegenler():
    """Gezegenlerin baglanti sayisina gore dogru sirada test eder."""
    g = veri_yukle()
    # Hoca'nin PDF'teki "kendi galaksinize gore yazin" izniyle guncellendi[cite: 3]
    assert en_bagli_gezegenler(g) == ['dünya', 'sirius', 'centauri', 'orion', 'kara_delik']

def test_hamle_sayaci():
    """hamle_sayaci closure yapisinin deger artirdigini test eder."""
    sayac = hamle_sayaci()
    assert sayac() == 1
    assert sayac() == 2