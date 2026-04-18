# ============================================================
# PROGRAM : Rekomendasi Pemilihan Buku
# PRAKTIKUM: Kecerdasan Buatan - Pertemuan 1
# KONSEP   : Struktur Kontrol, Struktur Data, Library
# LIBRARY  : random, math
# ============================================================

import random   # Library 1 : untuk memilih buku rekomendasi secara acak
import math     # Library 2 : untuk menghitung skor akhir rekomendasi

# ============================================================
# STRUKTUR DATA
# ============================================================

# LIST : daftar buku beserta informasinya (mutable, terurut)
daftar_buku = [
    {"judul": "Python Crash Course",         "kategori": "Pemrograman",  "rating": 4.8, "halaman": 544},
    {"judul": "Clean Code",                  "kategori": "Pemrograman",  "rating": 4.7, "halaman": 431},
    {"judul": "Artificial Intelligence",     "kategori": "AI",           "rating": 4.9, "halaman": 1152},
    {"judul": "Deep Learning",               "kategori": "AI",           "rating": 4.8, "halaman": 800},
    {"judul": "The Pragmatic Programmer",    "kategori": "Pemrograman",  "rating": 4.6, "halaman": 352},
    {"judul": "Data Science from Scratch",   "kategori": "Data Science", "rating": 4.5, "halaman": 330},
    {"judul": "Introduction to Algorithms",  "kategori": "Algoritma",    "rating": 4.7, "halaman": 1292},
    {"judul": "Computer Networking",         "kategori": "Jaringan",     "rating": 4.6, "halaman": 856},
]

# SET : kategori yang tersedia (unik, tidak ada duplikat)
kategori_tersedia = {"Pemrograman", "AI", "Data Science", "Algoritma", "Jaringan"}

# TUPLE : level preferensi pembaca (immutable, tidak bisa diubah)
level_pembaca = ("Pemula", "Menengah", "Mahir")


# ============================================================
# FUNGSI - USER DEFINED FUNCTION
# ============================================================

def tampilkan_header():
    print("=" * 55)
    print("       SISTEM REKOMENDASI PEMILIHAN BUKU")
    print("         Praktikum Kecerdasan Buatan")
    print("=" * 55)

def hitung_skor(rating, halaman, level):
    """
    Menghitung skor rekomendasi buku menggunakan library math.
    Skor dihitung berdasarkan rating dan kompleksitas halaman.
    """
    # math.log10 : menormalkan jumlah halaman agar tidak terlalu besar
    bobot_halaman = math.log10(halaman)

    # Bobot level pembaca
    # STRUKTUR KONTROL - IF/ELIF/ELSE
    if level == "Pemula":
        bobot_level = 0.6
    elif level == "Menengah":
        bobot_level = 0.8
    else:
        bobot_level = 1.0

    # Rumus skor : (rating * bobot_level) + (log10(halaman) * 0.3)
    skor = (rating * bobot_level) + (bobot_halaman * 0.3)

    # math.floor : membulatkan skor ke bawah 2 desimal
    skor = math.floor(skor * 100) / 100
    return skor

def tampilkan_buku(buku, nomor, skor):
    print(f"\n  [{nomor}] {buku['judul']}")
    print(f"      Kategori : {buku['kategori']}")
    print(f"      Rating   : {buku['rating']}")
    print(f"      Halaman  : {buku['halaman']} hal")
    print(f"      Skor     : {skor}")


# ============================================================
# PROGRAM UTAMA
# ============================================================

tampilkan_header()

# --- INPUT NAMA ---
nama = input("\nMasukkan nama kamu: ")

# --- PILIH LEVEL ---
print("\nLevel Pembaca:")
# STRUKTUR KONTROL - FOR LOOP pada TUPLE
for i, level in enumerate(level_pembaca, start=1):
    print(f"  {i}. {level}")

pilih_level = input("Pilih level (1/2/3): ")

# STRUKTUR KONTROL - IF/ELIF/ELSE untuk validasi input
if pilih_level == "1":
    level = "Pemula"
elif pilih_level == "2":
    level = "Menengah"
elif pilih_level == "3":
    level = "Mahir"
else:
    print("Input tidak valid, level diset ke Pemula.")
    level = "Pemula"

# --- PILIH KATEGORI ---
print("\nKategori Buku:")
# Konversi SET ke LIST agar bisa ditampilkan dengan nomor urut
list_kategori = list(kategori_tersedia)
# STRUKTUR KONTROL - FOR LOOP pada LIST
for i, kat in enumerate(list_kategori, start=1):
    print(f"  {i}. {kat}")

pilih_kat = input(f"Pilih kategori (1-{len(list_kategori)}), atau 0 untuk semua: ")

# STRUKTUR KONTROL - IF/ELSE untuk filter kategori
if pilih_kat == "0":
    buku_filter = daftar_buku
    kategori_dipilih = "Semua Kategori"
else:
    # Validasi input dengan WHILE LOOP
    counter = 0
    while counter < 3:
        try:
            idx = int(pilih_kat) - 1
            if 0 <= idx < len(list_kategori):
                kategori_dipilih = list_kategori[idx]
                # LIST COMPREHENSION : filter buku berdasarkan kategori
                buku_filter = [b for b in daftar_buku if b["kategori"] == kategori_dipilih]
                break
            else:
                print("Nomor tidak valid, coba lagi.")
                pilih_kat = input(f"Pilih kategori (1-{len(list_kategori)}): ")
        except ValueError:
            print("Input harus angka, coba lagi.")
            pilih_kat = input(f"Pilih kategori (1-{len(list_kategori)}): ")
        counter += 1
    else:
        buku_filter = daftar_buku
        kategori_dipilih = "Semua Kategori"

# ============================================================
# PROSES REKOMENDASI
# ============================================================

print("\n" + "=" * 55)
print(f"  Halo, {nama}! | Level: {level} | Kategori: {kategori_dipilih}")
print("=" * 55)

# Hitung skor setiap buku
buku_dengan_skor = []
# STRUKTUR KONTROL - FOR LOOP
for buku in buku_filter:
    skor = hitung_skor(buku["rating"], buku["halaman"], level)
    buku_dengan_skor.append((buku, skor))   # Operasi LIST : append

# Urutkan berdasarkan skor tertinggi - WHILE LOOP (bubble sort)
n = len(buku_dengan_skor)
i = 0
while i < n - 1:
    j = 0
    while j < n - i - 1:
        if buku_dengan_skor[j][1] < buku_dengan_skor[j + 1][1]:
            buku_dengan_skor[j], buku_dengan_skor[j + 1] = \
                buku_dengan_skor[j + 1], buku_dengan_skor[j]
        j += 1
    i += 1

# Tampilkan semua buku beserta skor
print("\nDaftar Buku & Skor Rekomendasi:")
for idx, (buku, skor) in enumerate(buku_dengan_skor, start=1):
    tampilkan_buku(buku, idx, skor)

# ============================================================
# REKOMENDASI ACAK - LIBRARY random
# ============================================================

print("\n" + "=" * 55)

# Ambil top 3 buku terbaik
top_buku = [b for b, _ in buku_dengan_skor[:3]]

if len(top_buku) == 0:
    print("  Tidak ada buku ditemukan untuk kategori ini.")
else:
    # random.choice : pilih 1 buku secara acak dari top 3
    rekomendasi = random.choice(top_buku)

    print(f"\n  REKOMENDASI UNTUKMU, {nama.upper()}:")
    print(f"  \"{rekomendasi['judul']}\"")
    print(f"  Kategori : {rekomendasi['kategori']}")
    print(f"  Rating   : {rekomendasi['rating']}")
    print(f"  Halaman  : {rekomendasi['halaman']} hal")

    # STRUKTUR KONTROL - IF/ELIF/ELSE untuk pesan tambahan
    if level == "Pemula":
        print("\n  Cocok banget buat kamu yang baru mulai belajar!")
    elif level == "Menengah":
        print("\n  Pas banget untuk tingkatkan skill kamu lebih jauh!")
    else:
        print("\n  Buku yang tepat untuk kamu yang sudah mahir!")

print("\n" + "=" * 55)
print("  Selamat membaca! Semangat belajar!")
print("=" * 55)