def tampilmenu():
    print('=' * 10)
    print("Menghitung luas bangun datar")
    print("1. Persegi")
    print("2. Segitiga")
    print("3. Lingkaran")
    print("4. Keluar program")
    print('=' * 10)

def persegi(s):
    luas = s * s
    return luas
def segitiga(a,t):
    luas = (a * t)/2
    return luas
def lingkaran(r):
    luas = (22/7) * r**2
    return luas


pilihan = 0
while pilihan != 4: 
    tampilmenu()
    pilihan = int(input("masukkan pilihan : "))
    if pilihan == 1:
        sisi = float(input("masukkan sisi : "))
        print("luas persegi adalah : ", persegi(sisi))
    elif pilihan == 2:
        alas = float(input("masukkan alas : "))
        tinggi = float(input("masukkan tinggi :"))
        print("luas segitiga adalah : ", segitiga(alas, tinggi))
    elif pilihan == 3:
        jarijari = float(input("masukkan jarijari : "))
        print("luas persegi adalah : ", lingkaran(jarijari))
    elif pilihan == 4:
        break
    else:
        print("anda salah memasukkan input")
        