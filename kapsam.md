Öğrenci: Muhammed Kerem Acar
Numara: 20253004042
Tarih: 11/10/2026
GitHub Deposu: https://github.com/keremiks/20253004042_hafta3
Kapsam Örnekleri
Örnek 1: Dışarıdan Okuma
x = 10

def oku():

    print(x)

oku()

Tahmin: Bence 10 çıkardı. Çünkü tırnak işareti  koymamışız, x zaten 10 olarak tanımlı olduğu için doğrudan 10 yazardı diye düşündüm.
Gerçek Sonuç: 10
Nedeni: Python, fonksiyonun içinde x değişkenini bulamayınca hata vermek yerine doğrudan dışarıdaki tanımlı değeri okuyor.


Örnek 2: İçeride Değiştirme
x = 10

def degistir():

    x = 20

    print("İçeride:", x)

degistir()

print("Dışarıda:", x)

Tahmin: İlk başta içeride 10 yazar, dışarıda 20 yazar diye düşünmüştüm çünkü kodu tam anlamamıştım. Ama çalıştırınca oradaki değiştir (def degistir) diye atanan komutun kodun giriş çıkış kısmına hükmettiğini fark ettim.
Gerçek Sonuç: İçeride: 20, Dışarıda: 10
Nedeni: Fonksiyonun içine girdiğimizde x'e 20 atayınca, dışarıdaki 10'a dokunmadan sadece o fonksiyonun içine özel yeni bir x tanımlamış oluyoruz.


Örnek 3: Hata Durumu (UnboundLocalError)
x = 10

def arttir():

    x = x + 1

arttir()

Tahmin: Orada eşittir (=) koyduğumuz için yeni bir şey tanımlamaya çalışıyor diye düşünürdüm. Normalde += 1 şeklinde olmalıydı, o yüzden bu şekilde artmayacağını ve programın hata vereceğini tahmin ederdim.
Gerçek Sonuç: UnboundLocalError hatası verdi.
Nedeni: Fonksiyonun içinde eşittir işaretiyle x'e değer atamaya çalıştığımız an, Python bunu  içeriye ait bir değişken zannediyor. Ama eşittirin sağında o yerel değişkene 1 eklemeye çalışınca, yerel değişkenin henüz bir değeri olmadığı için dışarıdakini de göremiyor ve çöküyor.
