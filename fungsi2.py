def sayHai(pelanggan):
   print("Hai %s, apakabar?" %pelanggan)

def menu():
   print("Ketik 1 untuk menyapa")
   print("Ketik 2 untuk keluar")

def keluar(nama):
   print("Terima kasih atas kunjungan anda %s" %nama)

pengunjung=input("Nama: ")          
pilihan=1
while pilihan!=2:
   sayHai(pengunjung)
   menu()
   pilihan=int(input(), base=10)
keluar(pengunjung)