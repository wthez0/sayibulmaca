from colorama import Fore, Back, Style
import random

sayi=random.randint(1,20)

print("Merhaba Oyunumuza Hoşgeldiniz !")
print("Şimdi İçimden 1 İle 20 Arasında Bir Sayı Tutacağım.")
print("Sende Bu Sayıyı Tahmin Ediceksin !")
print("Sadece 3 Hakkın Var Unutma.")
hazirlik=input("Hazır Mısın? E/H ")

while hazirlik == "E" and "e":
    tahmin=int(input(Fore.CYAN +("Lütfen Bir Tahminde Bulunuz : ")))
    if tahmin == sayi:
        print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
        print(Style.RESET_ALL)
        break
    elif tahmin!=sayi:
        print(Fore.RED + "Tahmininiz Yalnış Geriye Kalan Hakkınız : 2")

    tahmin2=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
    if tahmin2 == sayi:
        print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
        print(Style.RESET_ALL)
        break
    elif tahmin2!=sayi:
        print(Fore.RED +"Tahmininiz Yalnış Geriye Kalan Hakkınız : 1")
        if tahmin2<sayi:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif tahmin>sayi:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")
    
    tahmin3=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
    if tahmin3 == sayi:
        print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
        print(Style.RESET_ALL)
        break
    elif tahmin3!=sayi:
        print(Fore.LIGHTMAGENTA_EX +"Tahmileriniz Doğru Değil Tuttuğum Sayı :", sayi)
        print(Style.RESET_ALL)
else:
    print(Fore.Yellow)
    print(Back.RED +"Oyunu Oynamamanıza Üzüldük Tekrar Bekleriz")
    print(Style.RESET_ALL)
