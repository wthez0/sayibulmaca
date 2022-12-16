import random

sayi=random.randint(1,20)

print("Merhaba Oyunumuza Hoşgeldiniz !")
print("Şimdi İçimden 1 İle 20 Arasında Bir Sayı Tutacağım.")
print("Sende Bu Sayıyı Tahmin Ediceksin !")
print("Sadece 3 Hakkın Var Unutma.")
hazirlik=input("Hazır Mısın? E/H ")

while hazirlik == "E":
    tahmin=int(input("Lütfen Bir Tahminde Bulunuz : "))
    if tahmin == sayi:
        print("Tahmininiz Doğru Tebrikler")
        break
    elif tahmin!=sayi:
        print("Tahmininiz Yalnış Geriye Kalan Hakkınız : 2")

    tahmin2=int(input("Lütfen Bir Tahminde Bulunuz : "))
    if tahmin2 == sayi:
        print("Tahmininiz Doğru Tebrikler")
        break
    elif tahmin2!=sayi:
        print("Tahmininiz Yalnış Geriye Kalan Hakkınız : 1")
        if tahmin2<sayi:
            print("Lütfen Daha Büyük Bir Değer Giriniz.")
        elif tahmin>sayi:
            print("Lütfen Daha Küçük Bir Değer Giriniz")
    
    tahmin3=int(input("Lütfen Bir Tahminde Bulunuz : "))
    if tahmin3 == sayi:
        print("Tahmininiz Doğru Tebrikler")
        break
    elif tahmin3!=sayi:
        print("Tahmileriniz Doğru Değil Tuttuğum Sayı :", sayi)
