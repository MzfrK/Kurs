#Not Belirleme
#vize = input('Vize Notunuz : ')
#final = input('Final Notunuz : ')
#ortalama=(float(vize)*0.3)+(float(final)*0.7)
#print("Ortalama :{0} ".format(ortalama))
#if(0<=ortalama<=45):
#      print("Kaldınız.")
#elif(45<=ortalama<=69):
#      print("Geçtiniz.")
#elif(70<=ortalama<=84):
#      print("İyi.")
#elif(84<=ortalama<=100):
#      print("Pekiyi.")
#else:
#      print("Hatalı Giriş Yaptınız!!!")

#Maaş Hesap
#gelir=int(0)
#isim = input( "Lütfen İsminizi Giriniz: " )
#yas = int( input( "Lütfen Yaşınızı Belirtinz: " ) )
#maas = int(input("Maaşınızı Belirtiniz: "))
#cocuk = int(input("Cocuk Sayısı Belirtiniz:"))
#if (yas<45) and (1<=cocuk<3):
# gelir+=(maas+(cocuk*250))
#elif (yas <45) and (cocuk>=3):
# gelir+=(maas+(cocuk*200))
#else:
# gelir+=(maas+500)
#print("Toplam Geliriniz:", gelir)

#Ekran Giriş
username = "muzaffer"
password = "123456"

kullanici_adi = input("Kullanıcı Adını Giriniz: ")
sifre = input("Şifre'yi Giriniz: ")

if (kullanici_adi == username) and (sifre != password):
    print("Kullanıcı adı veya şifre yanlış..Kayıt olmak ister misiniz?")
    Kayit=input("E/H?")
    if (Kayit == "H"):
        print("PEKİ!!")
    elif (Kayit == "E"):
        print("Kullanıcı adı ve şifre belirleyiniz:")
        kullanici_adi = input("Kullanıcı Adını Giriniz: ")
        sifre = input("Şifre'yi Giriniz: ")
    elif (kullanici_adi != username) and (sifre == password):
        print("Kullanıcı adı veya şifre yanlış..Kayıt olmak ister misiniz?")
    elif (kullanici_adi != username) and (sifre != password):
        print("Kullanıcı adı veya şifre yanlış..Kayıt olmak ister misiniz?")
    else:
        print("Giriş Başarılı!")
elif (kullanici_adi != username) and (sifre == password):
    print("Kullanıcı adı veya şifre yanlış..Kayıt olmak ister misiniz?")
    Kayit=input("E/H?")
    if (Kayit == "H"):
        print("PEKİ!!")
    elif (Kayit == "E"):
        print("Kullanıcı adı ve şifre belirleyiniz:")
        kullanici_adi = input("Kullanıcı Adını Giriniz: ")
        sifre = input("Şifre'yi Giriniz: ")
    elif (kullanici_adi != username) and (sifre == password):
        print("Kullanıcı adı veya şifre yanlış..Kayıt olmak ister misiniz?")
    elif (kullanici_adi != username) and (sifre != password):
        print("Kullanıcı adı veya şifre yanlış..Kayıt olmak ister misiniz?")
    else:
        print("Giriş Başarılı!")
elif (kullanici_adi != username) and (sifre != password):
    print("Kullanıcı adı veya şifre yanlış..Kayıt olmak ister misiniz?")
    Kayit=input("E/H?")
    if (Kayit == "H"):
        print("PEKİ!!")
    elif (Kayit == "E"):
        print("Kullanıcı adı ve şifre belirleyiniz:")
        kullanici_adi = input("Kullanıcı Adını Giriniz: ")
        sifre = input("Şifre'yi Giriniz: ")
    elif (kullanici_adi != username) and (sifre == password):
        print("Kullanıcı adı veya şifre yanlış..Kayıt olmak ister misiniz?")
    elif (kullanici_adi != username) and (sifre != password):
        print("Kullanıcı adı veya şifre yanlış..Kayıt olmak ister misiniz?")
    else:
        print("Giriş Başarılı!")
else:
    print("Giriş Başarılı!")