
word='y'
while word == 'y':
    pilihan = int(input("pilih ukuran TV: "))
    if pilihan == 14:
        hargaDiskon = 3000000 - (3000000*0.1)
        print("anda mendapatkan diskon sebesar 10%\n"
        "harga menjadi: ", hargaDiskon)
    elif pilihan == 21:
        hargaDiskon = 8000000 - (8000000*0.2)
        print("anda mendapatkan diskon sebesar 20%\n"
        "harga menjadi: ", hargaDiskon)
    else:
        print("maaf ukuran tv yang anda masukkan salah")
    
    word = str(input("apakah anda ingin memilih TV lagi? (y/n)"))

print("terimakasih telah berbelanja")


