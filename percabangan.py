nama = input("masukkan nama:")
nilai_algoritma = int(input("masukkkan nilai algoritma:"))
nilai_agama = int(input("masukkkan nilai agama:"))
nilai_basis_data = int(input("masukkkan nilai basis data:"))
nilai_pancasila = int(input("masukkkan nilai pancasila:"))
nilai_bahasa_Indonesia = int(input("masukkkan nilai B.Indo:"))
nilai_bahasa_inggris = int(input("masukkkan nilai B.Inggris:"))
nilai_logika_informatika = int(input("masukkkan nilai logika informatika:"))

#menghitung rata-rata

rata_rata = (nilai_algoritma + nilai_agama + nilai_basis_data + nilai_pancasila + nilai_bahasa_Indonesia + nilai_bahasa_inggris + nilai_logika_informatika) / 7


# penentuan lulus atau tidak
if rata_rata >= 90 and rata_rata <=100:
    print("Nilai : A")
elif rata_rata >=70 and rata_rata <=80:
    print("Nilai : B")
elif rata_rata >=60 and rata_rata <=70:
    print("Nilai : C")
elif rata_rata >=50 and rata_rata <=60:
    print("Nilai : D")
else :
    print("Nilai : E")