import random

sayi=random.randint(1,20)

print("Merhaba Oyunumuza Hoşgeldiniz !")
print("Şimdi İçimden 1 İle 20 Arasında Bir Sayı Tutacağım.")
print("Sende Bu Sayıyı Tahmin Ediceksin !")
print("Sadece 3 Hakkın Var Unutma.")
print("Hazırsan Başlıyorum")
tahmin=int(input("Lütfen Bir Tahminde Bulununuz : "))

if tahmin==sayi:
    print("Tebrikler Doğru Tahminde Bulundunuz")
else:
    print("Maelesef Doğru Değil Geriye Kalan Hakkınız : 2")

tahmin2=int(input("Lüthen Bir Tahminde Bulununuz : "))
if tahmin2==sayi:
    print("Tebrikler Doğru Tahminde Bulundunuz")
elif tahmin2!=sayi:
    print("Maelesef Doğru Değil Geriye Kalan Hakkınız : 1")

tahmin3=int(input("Lüthen Bir Tahminde Bulununuz : "))
if tahmin3==sayi:
    print("Tebrikler Doğru Tahminde Bulundunuz")
elif tahmin3!=sayi:
    print("Maelesef Doğru Değil Tuttuğum Sayı", sayi)








