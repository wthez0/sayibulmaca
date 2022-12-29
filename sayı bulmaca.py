from colorama import Fore, Back, Style
import random

print("Merhaba Oyunumuza Hoşgeldiniz !")
print("Seviyemize Göre Bir Sayı Tutacağım")
print("Sadece 3 Hakkın Var Unutma.")
hazirlik=input("Hazır Mısın? E/H : ")

while hazirlik == "E" and "e":
    seviye=input("Seviyeniz Ne Olsun ? Kolay-Orta-Zor :")
    sayi=random.randint(1,20)
    if seviye == "orta":
        print(Fore.BLACK+"Orta Seviye Oyunumuza Hoşgeldiniz !")
        print(Fore.BLACK+"1 İle 20 Arasında Bir Sayı Tutacağım")
        print(Fore.BLACK+"4 Adet Tahmin Hakkın Var Unutma !")
        print(Fore.BLACK+"İyi Oyunlar !")
        otahmin=int(input(Fore.CYAN +("Lütfen Bir Tahminde Bulunuz : ")))
        if otahmin == sayi:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif otahmin!=sayi:
            print(Fore.RED + "Tahmininiz Yalnış Geriye Kalan Hakkınız : 3")
        if otahmin<sayi:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif otahmin>sayi:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")
        otahmin2=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
        if otahmin2 == sayi:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif otahmin2!=sayi:
            print(Fore.RED +"Tahmininiz Yalnış Geriye Kalan Hakkınız : 2")
        if otahmin2<sayi:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif otahmin2>sayi:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")                   
        otahmin3=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
        if otahmin3 == sayi:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        if otahmin3<sayi:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif otahmin3>sayi:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")
        elif otahmin3!=sayi:
            print(Fore.RED +"Tahmininiz Yalnış Geriye Kalan Hakkınız : 1")
            print(Style.RESET_ALL)
        otahmin4=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
        if otahmin4 == sayi:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif otahmin4!=sayi:
            print(Fore.LIGHTMAGENTA_EX +"Tahmileriniz Doğru Değil Tuttuğum Sayı :", sayi)
            print(Style.RESET_ALL)
            break
    if seviye == "kolay":    
        sayi2=random.randint(1,10)
        print(Fore.BLACK+"Kolay Seviye Oyunumuza Hoşgeldiniz !")
        print(Fore.BLACK+"1 İle 10 Arasında Bir Sayı Tutacağım")
        print(Fore.BLACK+"5 Adet Tahmin Hakkın Var Unutma !")
        print(Fore.BLACK+"İyi Oyunlar !")
        ktahmin=int(input(Fore.CYAN +("Lütfen Bir Tahminde Bulunuz : ")))
        if ktahmin == sayi2:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif ktahmin!=sayi2:
            print(Fore.RED + "Tahmininiz Yalnış Geriye Kalan Hakkınız : 4")
        if ktahmin<sayi2:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif ktahmin>sayi2:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")
        ktahmin2=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
        if ktahmin2 == sayi2:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif ktahmin2!=sayi2:
            print(Fore.RED +"Tahmininiz Yalnış Geriye Kalan Hakkınız : 3")
        if ktahmin2<sayi2:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif ktahmin2>sayi2:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")  
        ktahmin3=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
        if ktahmin3 == sayi2:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif ktahmin3!=sayi2:
            print(Fore.RED +"Tahmininiz Yalnış Geriye Kalan Hakkınız : 2")
        if ktahmin3<sayi2:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif ktahmin3>sayi2:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")   
            print(Style.RESET_ALL)
        ktahmin4=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
        if ktahmin4 == sayi2:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif ktahmin4!=sayi2:
            print(Fore.RED +"Tahmininiz Yalnış Geriye Kalan Hakkınız : 1")
        if ktahmin4<sayi2:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif ktahmin4>sayi2:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")   
            print(Style.RESET_ALL)
        ktahmin5=int(input(Fore.CYAN +("Lütfen Bir Tahminde Bulunuz : ")))
        if ktahmin5 == sayi2:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif ktahmin5!=sayi2:
            print(Fore.LIGHTRED_EX + "Maelesef Doğru Tahminde Bulunamadınız Tuttuğum Sayı : ", sayi2)
            break
    if seviye == "zor":
        sayi3=random.randint(1,50)
        print(Fore.BLACK+"Zor Seviye Oyunumuza Hoşgeldiniz !")
        print(Fore.BLACK+"1 İle 50 Arasında Bir Sayı Tutacağım")
        print(Fore.BLACK+"3 Adet Tahmin Hakkın Var Unutma !")
        print(Fore.BLACK+"İyi Oyunlar !")
        ztahmin=int(input(Fore.CYAN +("Lütfen Bir Tahminde Bulunuz : ")))
        if ztahmin == sayi3:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif ztahmin!=sayi3:
            print(Fore.RED + "Tahmininiz Yalnış Geriye Kalan Hakkınız : 2")
        if ztahmin<sayi3:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif ztahmin>sayi3:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")
        ztahmin2=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
        if ztahmin2 == sayi3:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif ztahmin2!=sayi3:
            print(Fore.RED +"Tahmininiz Yalnış Geriye Kalan Hakkınız : 1")
        if ztahmin2<sayi3:
            print(Fore.YELLOW +"Lütfen Daha Büyük Bir Değer Giriniz.")
        elif ztahmin2>sayi3:
            print(Fore.YELLOW +"Lütfen Daha Küçük Bir Değer Giriniz")  
        ztahmin3=int(input(Fore.CYAN +"Lütfen Bir Tahminde Bulunuz : "))
        if ztahmin3 == sayi3:
            print(Fore.GREEN +"Tahmininiz Doğru Tebrikler")
            print(Style.RESET_ALL)
            break
        elif ztahmin3!=sayi3:
            print(Fore.LIGHTRED_EX + "Maelesef Doğru Tahminde Bulunamadınız Tuttuğum Sayı : ", sayi3)
            print(Style.RESET_ALL)
            break
    
else:
    print(Fore.GREEN)
    print(Back.RED +"Oyunu Oynamamanıza Üzüldük Tekrar Bekleriz")
    print(Style.RESET_ALL)
