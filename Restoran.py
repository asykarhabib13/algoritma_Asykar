# ==========================================
#       APLIKASI KASIR RESTORAN
# ==========================================

print("=" * 40)
print("      APLIKASI KASIR RESTORAN")
print("=" * 40)

total = 0

while True:
    print("\n--------- DAFTAR MENU ---------")
    print("----------- MENU MAKANAN -----------")
    print("1. Nasi Goreng Kampung - Rp25.000")
    print("2. Mie Ayam - Rp15.000")
    print("3. Ayam Geprek - Rp20.000")
    print("4. Sate Ayam - Rp25.000")
    print("5. Bakso - Rp18.000")
    print("6. Ayam Bakar - Rp25.000")
    print("7. Nasi Uduk - Rp15.000")
    print("8. Mie Goreng Jawa - Rp18.000")
    print("9. Nasi Telur Sambal Matah - Rp15.000")
    print("10. Chicken Katsu Rice - Rp25.000")
    print("11. Nasi Goreng Seafood - Rp25.000")
    print("12. Kwetiau Goreng - Rp20.000")

    print("----------- MENU MINUMAN -----------")
    print("13. Es Teh Manis - Rp5.000")
    print("14. Lemon Tea - Rp10.000")
    print("15. Aneka Jus - Rp15.000")
    print("16. Es Kopi Susu - Rp17.000")
    print("17. Air Mineral - Rp3.000")
    print("18. Matcha Latte - Rp20.000")
    print("19. Es Cokelat - Rp15.000")
    print("20. Es Teler - Rp15.000")
    print("21. Thai Tea - Rp15.000")
    print("22. Lychee Yakult - Rp17.000")
    print("23. Es Kopi Gula Aren - Rp17.000")
    print("24. Es Kopi Hitam - Rp15.000")
    print("0. Selesai Memilih")
    print("-" * 40)

    pilihan = input("Pilih menu (0-24): ")

    if not pilihan.isdigit():
        print("Input harus berupa angka!")
        continue

    pilihan = int(pilihan)

    if pilihan == 0:
        break

    # Daftar menu dan harga
    menu = {
        1: ("Nasi Goreng Kampung", 25000),
        2: ("Mie Ayam", 15000),
        3: ("Ayam Geprek", 20000),
        4: ("Sate Ayam", 25000),
        5: ("Bakso", 18000),
        6: ("Ayam Bakar", 25000),
        7: ("Nasi Uduk", 15000),
        8: ("Mie Goreng Jawa", 18000),
        9: ("Nasi Telur Sambal Matah", 15000),
        10: ("Chicken Katsu Rice", 25000),
        11: ("Nasi Goreng Seafood", 25000),
        12: ("Kwetiau Goreng", 20000),
        13: ("Es Teh Manis", 5000),
        14: ("Lemon Tea", 10000),
        15: ("Aneka Jus", 15000),
        16: ("Es Kopi Susu", 17000),
        17: ("Air Mineral", 3000),
        18: ("Matcha Latte", 20000),
        19: ("Es Cokelat", 15000),
        20: ("Es Teler", 15000),
        21: ("Thai Tea", 15000),
        22: ("Lychee Yakult", 17000),
        23: ("Es Kopi Gula Aren", 17000),
        24: ("Es Kopi Hitam", 15000)
    }

    if pilihan in menu:
        nama, harga = menu[pilihan]
    else:
        print("Menu tidak tersedia. Pilih angka 0-24.")
        continue

    jumlah = input("Jumlah " + nama + ": ")

    if jumlah.isdigit() and int(jumlah) > 0:
        jumlah = int(jumlah)
    else:
        print("Jumlah tidak valid. Pesanan dibatalkan.")
        continue

    subtotal = harga * jumlah
    total += subtotal

    print("->", nama, "x" + str(jumlah), "= Rp" + format(subtotal, ",").replace(",", "."))
    print("Total sementara: Rp" + format(total, ",").replace(",", "."))

# ==========================================
#             HITUNG DISKON
# ==========================================

if total > 200000:
    persen_diskon = 20
else:
    persen_diskon = 0

potongan = total * persen_diskon // 100
total_bayar = total - potongan

# ==========================================
#           STRUK PEMBAYARAN
# ==========================================

print("\n" + "=" * 40)
print("          STRUK PEMBAYARAN")
print("=" * 40)

if total == 0:
    print("Belum ada pesanan.")
else:
    print("Total Belanja : Rp" + format(total, ",").replace(",", "."))
    print("Diskon        :", str(persen_diskon) + "%")
    print("Potongan      : Rp" + format(potongan, ",").replace(",", "."))
    print("-" * 40)
    print("Total Bayar   : Rp" + format(total_bayar, ",").replace(",", "."))

print("=" * 40)
print("          Terima Kasih!")
print("=" * 40)