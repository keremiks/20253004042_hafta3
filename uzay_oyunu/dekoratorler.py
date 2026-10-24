"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""
import time
from functools import wraps

def sure_olc(fonk):
    """Fonksiyonun çalışma süresini ölçüp ekrana yazdıran dekoratör."""
    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonk(*args, **kwargs)
        bitis = time.perf_counter()
        
        gecen_sure = bitis - baslangic
        print(f"{fonk.__name__}: {gecen_sure:.4f} sn")
        
        return sonuc
    return sarmalayici

def say(fonk):
    """Fonksiyonun kaç kere çağrıldığını sayan dekoratör."""
    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri += 1
        return fonk(*args, **kwargs)
    sarmalayici.cagri = 0
    return sarmalayici