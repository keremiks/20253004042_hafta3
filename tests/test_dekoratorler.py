"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""
import pytest
from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri
from uzay_oyunu.komutlar import KOMUTLAR, komut

# --- GÖREV 1 TESTLERİ (sure_olc) ---
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


# --- GÖREV 2 TESTİ (say) ---
def test_say_dekoratoru():
    @say
    def carp(a, b):
        return a * b
        
    carp(2, 3)
    carp(4, 5)
    assert carp.cagri == 2


# --- GÖREV 3 TESTİ (log_cagri) ---
def test_log_cagri(capsys):
    @log_cagri
    def yolculuk(hedef, hiz):
        return f"{hedef} hiz={hiz}"
        
    sonuc = yolculuk('orion', hiz=3)
    assert sonuc == "orion hiz=3"
    
    yakalanan = capsys.readouterr().out
    assert "-> yolculuk('orion', hiz=3)" in yakalanan
    assert "<<- yolculuk 'orion hiz=3'" in yakalanan


# --- GÖREV 4 TESTLERİ (Her komut için özel testler) ---
def test_komut_kayit_hatasi():
    # Aynı isimle kayıt ValueError vermeli
    with pytest.raises(ValueError):
        @komut("yardim", "baska aciklama")
        def kopya_komut(durum):
            pass

def test_yardim_komutu_ciktisi():
    durum = {}
    sonuc = KOMUTLAR["yardim"][0](durum)
    assert "yardim komutları listeler" in sonuc
    assert "harita gidebileceğin gezegenleri gösterir" in sonuc

def test_envanter_komutu_ciktisi():
    durum = {"credits": True, "engines": False, "copilot": True}
    sonuc = KOMUTLAR["envanter"][0](durum)
    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"

def test_harita_komutu_ciktisi():
    durum = {"konum": "dünya", "baglantilar": {"dünya": ["orion", "mars"]}}
    sonuc = KOMUTLAR["harita"][0](durum)
    assert sonuc == "orion, mars"
