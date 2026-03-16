import random
from datetime import datetime

# Struktur Data 
lagu_pop = [
    "Hati-Hati di Jalan - Tulus",
    "Komang - Raim Laode",
    "Tak Segampang Itu - Anggi Marito",
    "Melukis Senja - Budi Doremi"
]

lagu_indie = [
    "Sial - Mahalini",
    "Rumah ke Rumah - Hindia",
    "Evaluasi - Hindia",
    "Zona Nyaman - Fourtwnty"
]

lagu_kpop = [
    "Dynamite - BTS",
    "How You Like That - BLACKPINK",
    "Love Dive - IVE",
    "Next Level - aespa"
]


sekarang = datetime.now()

print("===================================")
print("PROGRAM REKOMENDASI LAGU")
print("Tanggal :", sekarang.strftime("%d-%m-%Y"))
print("===================================")

nama = input("Masukkan nama kamu: ")

print("\nHalo", nama)
print("Pilih genre lagu yang kamu suka:")
print("1. Pop")
print("2. Indie")
print("3. K-Pop")

pilihan = input("Masukkan pilihan (1/2/3): ")

# Struktur kontrol 
if pilihan == "1":
    lagu = random.choice(lagu_pop)
elif pilihan == "2":
    lagu = random.choice(lagu_indie)
elif pilihan == "3":
    lagu = random.choice(lagu_kpop)
else:
    lagu = "Pilihan tidak tersedia"

print("\nRekomendasi lagu buat kamu:", lagu)

# Perulangan while
ulang = input("\nMau rekomendasi lagu lagi? (y/n): ")

while ulang == "y":
    if pilihan == "1":
        lagu = random.choice(lagu_pop)
    elif pilihan == "2":
        lagu = random.choice(lagu_indie)
    elif pilihan == "3":
        lagu = random.choice(lagu_kpop)

    print("Rekomendasi lagu berikutnya:", lagu)
    ulang = input("Coba lagi? (y/n): ")

print("\nTerima kasih udah pakai program ini, semoga suka lagunya!")