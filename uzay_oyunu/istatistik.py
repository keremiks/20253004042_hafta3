"""
Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
GitHub deposu: https://github.com/keremiks/20253004042_hafta3
"""
from functools import reduce, partial

# 1. Gezegen adlarının büyük harfli listesi
def buyuk_harfli_map(gezegenler):
    return list(map(str.upper, gezegenler))

def buyuk_harfli_liste(gezegenler):
    return [g.upper() for g in gezegenler]

# 2. En az iki bağlantısı olan gezegenler
def iki_baglantili_filter(baglantilar):
    return list(filter(lambda g: len(baglantilar.get(g, [])) >= 2, baglantilar.keys()))

def iki_baglantili_liste(baglantilar):
    return [g for g, komsular in baglantilar.items() if len(komsular) >= 2]

# 3. Toplam bağlantı sayısı
def toplam_baglanti_reduce(baglantilar):
    return reduce(lambda acc, komsular: acc + len(komsular), baglantilar.values(), 0)

def toplam_baglanti_sum(baglantilar):
    return sum(len(komsular) for komsular in baglantilar.values())

# 4. Partial ile hizli_yolculuk fonksiyonu
def yolculuk(hedef, hiz):
    return f"{hedef} hedefine {hiz} hızıyla gidiliyor."

hizli_yolculuk = partial(yolculuk, hiz=3)

# HOCANIN İSTEDİĞİ YORUM SATIRI:
# Bence liste üreteçleri (list comprehension) ve sum() fonksiyonu, 
# map, filter ve reduce kullanımına göre çok daha okunaklı ve 'Pythonic' bir yazımdır.s