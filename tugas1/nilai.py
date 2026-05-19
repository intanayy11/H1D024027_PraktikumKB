# ============================================================
# PROGRAM: Sistem Manajemen Nilai Mahasiswa Informatika
# MATA KULIAH: Praktikum Kecerdasan Buatan - Pertemuan 1
# DESKRIPSI: Program ini mengimplementasikan struktur kontrol,
#            struktur data, dan library Python.
# ============================================================

import random       # Library 1: untuk generate nilai acak
import statistics   # Library 2: untuk perhitungan statistik

# ============================================================
# DATA AWAL MENGGUNAKAN STRUKTUR DATA
# ============================================================

# LIST: daftar nama mahasiswa (mutable, terurut)
mahasiswa = ["Andi", "Budi", "Citra", "Deni", "Eka"]

# TUPLE: daftar mata kuliah (immutable, tidak bisa diubah)
mata_kuliah = ("Rekayasa Perangkat Lunak", "Struktur Data", "Kecerdasan Buatan", "Basis Data", "Jaringan Komputer")

# SET: daftar mahasiswa yang sudah mengumpulkan tugas (unik, tidak terurut)
sudah_kumpul = {"Andi", "Citra", "Eka"}

# ============================================================
# GENERATE NILAI MENGGUNAKAN LIBRARY random
# ============================================================

print("=" * 60)
print("   SISTEM MANAJEMEN NILAI MAHASISWA INFORMATIKA")
print("=" * 60)

# Dictionary untuk menyimpan nilai setiap mahasiswa
data_nilai = {}

# STRUKTUR KONTROL - FOR LOOP
# Iterasi setiap mahasiswa untuk generate nilai
for nama in mahasiswa:
    nilai_per_matkul = []

    # FOR LOOP nested: generate nilai untuk setiap mata kuliah
    for matkul in mata_kuliah:
        nilai = random.randint(55, 100)  # Library random: nilai antara 55-100
        nilai_per_matkul.append(nilai)  # Operasi LIST: append

    data_nilai[nama] = nilai_per_matkul

# ============================================================
# TAMPILKAN NILAI SETIAP MAHASISWA
# ============================================================

print("DAFTAR NILAI MAHASISWA:")
print("-" * 60)

for nama in mahasiswa:
    nilai_list = data_nilai[nama]
    rata_rata = statistics.mean(nilai_list)  # Library statistics: hitung rata-rata

    # STRUKTUR KONTROL - IF/ELIF/ELSE
    # Menentukan grade berdasarkan rata-rata
    if rata_rata >= 80:
        grade = "A"
        keterangan = "Sangat Baik"
    elif rata_rata >= 70:
        grade = "B"
        keterangan = "Baik"
    elif rata_rata >= 60:
        grade = "C"
        keterangan = "Cukup"
    else:
        grade = "D"
        keterangan = "Perlu Peningkatan"

    print(f"   Mahasiswa : {nama}")
    print(f"   Nilai     : {nilai_list}")
    print(f"   Rata-rata : {rata_rata:.2f}")
    print(f"   Grade     : {grade} ({keterangan})")

# ============================================================
# STATISTIK KELAS MENGGUNAKAN LIBRARY statistics
# ============================================================

print("\n" + "=" * 60)
print("STATISTIK KELAS:")
print("-" * 60)

semua_rata = [statistics.mean(data_nilai[n]) for n in mahasiswa]
print(f"  Rata-rata kelas   : {statistics.mean(semua_rata):.2f}")
print(f"  Nilai tertinggi   : {max(semua_rata):.2f}")
print(f"  Nilai terendah    : {min(semua_rata):.2f}")
print(f"  Standar deviasi   : {statistics.stdev(semua_rata):.2f}")

# ============================================================
# CEK STATUS PENGUMPULAN TUGAS MENGGUNAKAN SET
# ============================================================

print("\n" + "=" * 60)
print("STATUS PENGUMPULAN TUGAS:")
print("-" * 60)

# Konversi list mahasiswa ke set untuk operasi himpunan
semua_mahasiswa_set = set(mahasiswa)

# SET DIFFERENCE: mahasiswa yang belum kumpul
belum_kumpul = semua_mahasiswa_set - sudah_kumpul

# SET INTERSECTION: konfirmasi siapa saja yang sudah kumpul
konfirmasi_kumpul = semua_mahasiswa_set & sudah_kumpul

print(f"  Sudah kumpul   : {', '.join(sorted(konfirmasi_kumpul))}")
print(f"  Belum kumpul   : {', '.join(sorted(belum_kumpul))}")

# ============================================================
# PENCARIAN MAHASISWA TERBAIK MENGGUNAKAN WHILE LOOP
# ============================================================

print("\n" + "=" * 60)
print("PERINGKAT MAHASISWA (Tertinggi ke Terendah):")
print("-" * 60)

# Buat salinan list untuk diurutkan
nama_dan_nilai = [(nama, statistics.mean(data_nilai[nama])) for nama in mahasiswa]

# STRUKTUR KONTROL - WHILE LOOP
# Bubble sort manual untuk menampilkan peringkat
n = len(nama_dan_nilai)
i = 0
while i < n - 1:
    j = 0
    while j < n - i - 1:
        if nama_dan_nilai[j][1] < nama_dan_nilai[j + 1][1]:
            # Tukar posisi
            nama_dan_nilai[j], nama_dan_nilai[j + 1] = nama_dan_nilai[j + 1], nama_dan_nilai[j]
        j += 1
    i += 1

# Tampilkan peringkat
for peringkat, (nama, nilai) in enumerate(nama_dan_nilai, start=1):
    print(f"  Peringkat {peringkat}: {nama} ({nilai:.2f})")

# ============================================================
# INFO MATA KULIAH MENGGUNAKAN TUPLE
# ============================================================

print("\n" + "=" * 60)
print("DAFTAR MATA KULIAH (Tuple - Tidak Dapat Diubah):")
print("-" * 60)

# FOR LOOP dengan enumerate pada TUPLE
for idx, matkul in enumerate(mata_kuliah, start=1):
    # Hitung rata-rata seluruh mahasiswa untuk mata kuliah ini
    nilai_matkul = [data_nilai[nama][idx - 1] for nama in mahasiswa]
    rata_matkul = statistics.mean(nilai_matkul)

    # IF/ELSE: tandai mata kuliah dengan rata-rata < 70
    status = "Perlu Perhatian" if rata_matkul < 70 else "Baik"
    print(f"  {idx}. {matkul:<30} | Rata-rata: {rata_matkul:.2f} | {status}")

print("\n" + "=" * 60)
print("   Program selesai. Terima kasih!")
print("=" * 60)