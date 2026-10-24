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
def log_cagri(fonk):
    """Çağrı öncesi ve sonrası bilgileri yazdıran dekoratör."""
    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
      # Argümanları hocanın istediği formata çeviriyoruz
        arg_listesi = [repr(a) for a in args]
        kwarg_listesi = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        tum_arglar = ", ".join(arg_listesi + kwarg_listesi)
        
        print(f"-> {fonk.__name__}({tum_arglar})")
        
        sonuc = fonk(*args, **kwargs)
        
        print(f"<<- {fonk.__name__} {repr(sonuc)}")
        return sonuc
    return sarmalayici
def sinirla(alt, ust):
    """Dekore edilen fonksiyonun ilk argümanının belirtilen aralıkta olmasını zorunlu kılar."""
    def dekorator(fonk):
        # functools'dan wraps zaten yukarıda import edilmiştir (sure_olc için)
        from functools import wraps 
        @wraps(fonk)
        def sarmalayici(*args, **kwargs):
          
            deger = args[0]
            
            # Değer sınırlar içinde mi kontrol et
            if not (alt <= deger <= ust):
            
                raise ValueError(f"{fonk.__name__}: {deger} değeri {alt}-{ust} aralığında değil")
                
            return fonk(*args, **kwargs)
        return sarmalayici
    return dekorator


@sinirla(0, 100)
def yakit_harca(miktar):
    """100 birimlik depodan harcanan miktarı düşer ve kalanı döndürür."""
    return 100 - miktar