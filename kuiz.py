nama = input("masukkan nama:")

if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    print("nama tidak tersedia")

print("Target nilai", nama, ":", target)

percobaan = 0 
lulus = False


while percobaan < 3 and lulus == False:
    percobaan += 1
    nilai = int(input("masukkan nilai:"))

    if nilai >= target:
        lulus = True
    elif percobaan < 3:
        print("nilai belum mencapai target, ikut remedial")

    if lulus == True:
        print(nama, "berhasil lulus setelah", percobaan, "kali percobaan")
    else:
        print(nama, "tidak lulus setelah", percobaan, "kali percobaan")