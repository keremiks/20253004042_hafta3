# Ad: Muhammed Kerem Acar
# Numara: 20253004042
# Tarih: 11/10/2026
# GitHub Deposu: https://github.com/keremiks/20253004042_hafta3

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Oyuncunun esyalarina gore envanter metnini dondurur."""
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("hiper motor")
    if copilot:
        esyalar.append("yetenekli bir pilot")
        
    if not esyalar:
        return ""
    return "Sende: " + ", ".join(esyalar)

def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralandirilmis menu seklinde dondurur."""
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, 1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)

def travel() -> None:
    """Galaksi haritasini veri dosyasindan okuyup oynatan ana fonksiyon."""
    # Play tuşuyla ve testlerle uyumlu olması için güvenli import
    try:
        from uzay_oyunu.galaksi import veri_yukle
        from uzay_oyunu.araclar import hamle_sayaci
        from uzay_oyunu.akis import yakit_gostergesi
    except ModuleNotFoundError:
        from galaksi import veri_yukle
        from araclar import hamle_sayaci
        from akis import yakit_gostergesi
    
    galaksi = veri_yukle()
    if not galaksi:
        return
        
    konum = galaksi.get("konum", "dünya")
    sayac = hamle_sayaci()
    
    # Oyunun başında hocanın istediği yakıt göstergesini oluşturuyoruz (100 yakıt, adım başı 5 tüketim)
    gosterge = yakit_gostergesi(100, 5)
    
    envanter = envanter_metni(True, False, True)
    if envanter:
        print(envanter)
    
    while True:
        hedefler = galaksi["baglantilar"].get(konum, [])
        
        if not hedefler:
            hamle = sayac()
            print(f"Oyunu {hamle} hamlede bitirdin!")
            break
            
        print(f"\nŞu anki konum: {konum}")
        print(hedef_menusu(hedefler))
        
        secim = input("Seçiminiz (Çıkış için q): ")
        if secim.lower() == 'q':
            hamle = sayac()
            print(f"Oyunu {hamle} hamlede bitirdin!")
            break
            
        try:
            index = int(secim) - 1
            if 0 <= index < len(hedefler):
                # Oyuncu geçerli bir yer seçip yola çıktığında yakıtı çekiyoruz
                try:
                    kalan_yakit = next(gosterge)
                except StopIteration:
                    print("Yakıtın bitti, uzayda sürükleniyorsun...")
                    break
                
                konum = hedefler[index]
                sayac()
                print(f"Yolculuk başarılı! Kalan yakıt: {kalan_yakit}")
            else:
                print("Gecersiz secim!")
        except ValueError:
            print("Lutfen gecerli bir sayi girin.")

if __name__ == "__main__":
    travel()