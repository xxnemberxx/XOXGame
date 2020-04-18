tahta = ["","","","","","","","",""]
secim = ['O','X']
a = ""
b = ""

def harfSec():
    sec =int(input("sec 1[X]/0[O]:"))
    return sec

def tahtaGetir():
    print(tahta[:3])
    print(tahta[3:6])
    print(tahta[6:9])

def kazandimi():
    if tahta[0] == tahta[1] == tahta[2] != "":
        print("", tahta[0], " KAZANDI")
        return True
    elif tahta[0] == tahta[3] == tahta[6] != "":
        print("", tahta[0], " KAZANDI")
        return True
    elif tahta[3] == tahta[4] == tahta[5] != "":
        print("", tahta[3], " KAZANDI")
        return True
    elif tahta[6] == tahta[7] == tahta[8] != "":
        print("", tahta[6], " KAZANDI")
        return True
    elif tahta[1] == tahta[4] == tahta[7] != "":
        print("", tahta[1], " KAZANDI")
        return True
    elif tahta[2] == tahta[5] == tahta[8] != "":
        print("", tahta[2], " KAZANDI")
        return True
    if tahta[0] != "" and tahta[1] != "" and tahta[2] != "":
        if tahta[3] != "" and tahta[4] != "" and tahta[5] != "":
            if tahta[6] != "" and tahta[7] != "" and tahta[8] != "":
                print("BERABERE")
                return True

    return False


def kordinatSec():
    while kazandimi() == False:
        try:

            for x in range(8):
                if kazandimi() == False:
                    if x % 2 == 0:
                        harf = a

                    else:
                        harf = b

                tahtaGetir()
                bolge = int(input("sec 1 -> 9 :"))
                if bolge == 1:
                    tahta[0] = harf
                elif bolge == 2:
                    tahta[1] = harf
                elif bolge == 3:
                    tahta[2] = harf
                elif bolge == 4:
                    tahta[3] = harf
                elif bolge == 5:
                    tahta[4] = harf
                elif bolge == 6:
                    tahta[5] = harf
                elif bolge == 7:
                    tahta[6] = harf
                elif bolge == 8:
                    tahta[7] = harf
                elif bolge == 9:
                    tahta[8] = harf
                else:
                    print("verilen rakamlar arasından seçim yapınız...")
        except ValueError:
            print("Sadece Tam  Sayı Giriniz...")


while True:
    try:
        deger = harfSec()
        if deger>= 0 and deger <= 1:
            a = secim[deger]
            if deger == 0:
                b = "X"
            else:
                b = "O"
            kordinatSec()
            tahtaGetir()
            break
        else:
            print("1[X] ya da 0[O] seçin...")
    except ValueError:
        print("Sadece Tam  Sayı Giriniz...")

input("ÇIKIŞ İÇİN ENTER")