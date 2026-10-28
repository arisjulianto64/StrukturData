def input_nilai():
    nilai = int(input("Masukkan nilai: "))
    return nilai

# Fungsi untuk menghitung rata-rata
def hitung_rata_rata(n1, n2):
    return (n1 + n2) / 2

# Fungsi untuk menampilkan hasil
def tampilkan_hasil(rata):
    print("Rata-rata nilai:", rata)

# Program utama
nilai1 = input_nilai()
nilai2 = input_nilai()
rata_rata = hitung_rata_rata(nilai1, nilai2)
tampilkan_hasil(rata_rata)