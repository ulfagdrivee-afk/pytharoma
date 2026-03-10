import rumus 

print("Menu:")
print("1. Segitiga")
print("2. Persegi")
print("3. Lingkaran")
print("4. Belah Ketupat")

menu_pilihan = int(input("Pilih menu (1/2/3): "))

if menu_pilihan == 1 :
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    hasil = rumus.hitung_luas(menu_pilihan, alas, tinggi)
elif menu_pilihan == 2:
    sisi = float(input("Masukkan panjang sisi persegi: "))
    hasil = rumus.hitung_luas(menu_pilihan, sisi)
elif menu_pilihan == 3:
    jari = float(input("Masukkan jari-jari lingkaran: "))
    hasil = rumus.hitung_luas(menu_pilihan, jari)
elif menu_pilihan == 4:
    diagonal1 = float(input("Masukkan diagonal 1 belah ketupat: "))
    diagonal2 = float(input("Masukkan diagonal 2 belah ketupat: "))
    hasil = rumus.hitung_luas(menu_pilihan, diagonal1, diagonal2)
else:
    print("Menu tidak valid")

    print("Luas bangun tersebut adalah {hasil} cm")