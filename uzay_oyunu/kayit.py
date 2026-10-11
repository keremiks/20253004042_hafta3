# Ad: Muhammed Kerem Acar
# Numara: 20253004042
# Tarih: 11/10/2026
# GitHub Deposu: https://github.com/keremiks/20253004042_hafta3

def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> None:
    """Gorev detaylarini, adimlari ve ek bilgileri ekrana bicimli yazdirir."""
    print(f"[{oncelik.upper()}] {baslik}")
    
    for i, adim in enumerate(adimlar, 1):
        print(f"{i}. {adim}")
        
    for anahtar, deger in ekler.items():
        print(f" {anahtar}: {deger}")

if __name__ == "__main__":
    # 1. Bicim: Standart argumanlarla cagirma
    gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al", oncelik="yüksek", sorumlu="Ayşe")
    
    print("-" * 30)
    
    # 2. Bicim: Listeyi (*) ve sozlugu (**) acarak cagirma
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler_sozlugu = {"sorumlu": "Ayşe"}
    gorev_kaydi("Kara deliğe atla", *adim_listesi, oncelik="yüksek", **ekler_sozlugu)