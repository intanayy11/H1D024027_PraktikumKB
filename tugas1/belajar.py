import random
from datetime import datetime

topik_ai = [
    "Logika Fuzzy",
    "Sistem Pakar",
    "Jaringan Saraf Tiruan",
    "Algoritma Genetika",
    "Machine Learning Dasar"
]

mahasiswa = {"Intan", "Raka", "Dinda", "Aldi"}

sekarang = datetime.now()
print("=================================")
print("Rekomendasi Lagu")
print("Tanggal :", sekarang.strftime("%d-%m-%Y"))
print("=================================")

nama = input("Masukkan nama kamu: ")

if nama in mahasiswa:
    print("Halo", nama, "Selamat datang di Lagua-lah siapa lagi?")
else:
    print("Halo", nama, "Kamu belum terdaftar, tetap bisa coba program ini kok!")

topik = random.choice(topik_ai)
print("\n Lagu yang direkomendasikan hari ini adalah:", topik)

print("\nDaftar Mata Kuliah:")
for i in range(len(topik_ai)):
    print(i+1, ".", topik_ai[i])

ulang = input("\nApakah ingin rekomendasi topik lain? (y/n): ")

while ulang == "y":
    topik = random.choice(topik_ai)
    print("Topik rekomendasi berikutnya:", topik)
    ulang = input("Coba lagi? (y/n): ")

print("\nTerima kasih telah menggunakan program ini!")