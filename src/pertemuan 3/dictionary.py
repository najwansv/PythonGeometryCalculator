listmahasiswa = []

def registerMahasiswa():
    mahasiswa = {
        "Nama" : "",
        "NIM" : "",
        "No telepon" : " "    
    }
    mahasiswa["Nama"] = input("Masukkan Nama       : ")
    mahasiswa["NIM"] = input("Masukkan NIM        : ")
    mahasiswa["No telepon"] = input("Masukkan No telepon : ")
    listmahasiswa.append(mahasiswa)

def tampilMahasiswa():
    print(listmahasiswa)
    
    # print("Nama       : ", mahasiswa["Nama"])
    # print("NIM        : ", mahasiswa["NIM"])
    # print("No telepon : ", mahasiswa["No telepon"])

for x in range(3):
    registerMahasiswa()

tampilMahasiswa()