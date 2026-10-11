# Ad: Muhammed Kerem Acar
# Numara: 20253004042
# Tarih: 11/10/2026
# GitHub Deposu: https://github.com/keremiks/20253004042_hafta3

import pytest

# GÖREV 4(a) - Hatalı fonksiyonun None kalıbıyla düzeltilmiş hali
def yakit_ekle(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

def test_yakit_ekle_tuzak():
    """Varsayılan argüman (mutable default argument) hatasının çözüldüğünü test eder."""
    gemi1_depo = yakit_ekle(50)
    assert gemi1_depo == [50]

    gemi2_depo = yakit_ekle(30)
    assert gemi2_depo == [30]