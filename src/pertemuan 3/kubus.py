def tampiltext():
    print("menghitung volume kubus")

def volumekubus(s):
    volume = s * s * s
    return volume

tampiltext()
sisi = int(input("Masukkan panjang sisi: "))
volume = volumekubus(sisi)
print(f"volume kubus adalah : {volume}")