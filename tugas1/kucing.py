# ============================================================
# PROGRAM : Simulasi Kucing Peliharaan
# PRAKTIKUM: Kecerdasan Buatan - Pertemuan 1
# DESKRIPSI: Program simulasi sederhana kucing peliharaan yang
#            mengimplementasikan struktur kontrol, struktur data,
#            dan library Python (random & math).
# ============================================================

import random   # Library 1: untuk perilaku acak kucing
import math     # Library 2: untuk perhitungan matematis

# ============================================================
# STRUKTUR DATA
# ============================================================

# TUPLE: ras kucing yang tersedia (immutable, tidak bisa diubah)
ras_kucing = ("Persian", "Maine Coon", "Siamese", "Anggora", "British Shorthair")

# LIST: daftar nama kucing peliharaan
nama_kucing = ["Mochi", "Boba", "Nala", "Leo", "Luna"]

# SET: aktivitas yang bisa dilakukan kucing (unik, tidak ada duplikat)
aktivitas = {"tidur", "makan", "bermain", "menjilat bulu", "menggaruk sofa"}

# ============================================================
# GENERATE DATA KUCING
# ============================================================

print("=" * 55)
print("       SIMULASI KUCING PELIHARAAN")
print("=" * 55)

# Dictionary untuk menyimpan data tiap kucing
data_kucing = {}

# STRUKTUR KONTROL - FOR LOOP
# Membuat data untuk setiap kucing
for i, nama in enumerate(nama_kucing):
    ras   = random.choice(ras_kucing)           # random: pilih ras acak dari tuple
    umur  = random.randint(1, 10)               # random: umur 1-10 tahun
    berat = round(random.uniform(2.5, 6.5), 2) # random: berat 2.5-6.5 kg

    data_kucing[nama] = {
        "ras"  : ras,
        "umur" : umur,
        "berat": berat
    }

# ============================================================
# TAMPILKAN DATA & KONDISI KUCING
# ============================================================

print("\n Data Kucing Peliharaan:")
print("-" * 55)

for nama, info in data_kucing.items():
    berat = info["berat"]
    umur  = info["umur"]

    # math: hitung BMI kucing (berat / tinggi^2, estimasi tinggi 0.3m)
    tinggi_estimasi = 0.3
    bmi = round(berat / math.pow(tinggi_estimasi, 2), 2)

    # STRUKTUR KONTROL - IF/ELIF/ELSE
    # Cek kondisi berat badan berdasarkan BMI
    if bmi < 30:
        kondisi_berat = "Kurus"
    elif bmi <= 50:
        kondisi_berat = "Ideal"
    else:
        kondisi_berat = "Gemuk"

    # Cek kategori umur
    if umur <= 2:
        kategori_umur = "Kitten (anak kucing)"
    elif umur <= 7:
        kategori_umur = "Adult (dewasa)"
    else:
        kategori_umur = "Senior"

    print(f"\n Nama   : {nama}")
    print(f"  Ras    : {info['ras']}")
    print(f"  Umur   : {umur} tahun  -> {kategori_umur}")
    print(f"  Berat  : {berat} kg    -> {kondisi_berat} (BMI: {bmi})")

# ============================================================
# SIMULASI AKTIVITAS HARIAN KUCING
# ============================================================

print("\n" + "=" * 55)
print(" Aktivitas Harian Kucing:")
print("-" * 55)

# FOR LOOP: simulasikan aktivitas tiap kucing
for nama in nama_kucing:
    # random: pilih 2 aktivitas acak dari set aktivitas
    aktivitas_hari_ini = random.sample(sorted(aktivitas), 2)
    energi_terpakai    = round(random.uniform(10, 100), 1)

    # math: hitung sisa energi dalam persen menggunakan log
    sisa_energi = round(math.log(energi_terpakai + 1) / math.log(101) * 100, 1)

    print(f"\n {nama}")
    print(f"  Aktivitas : {aktivitas_hari_ini[0]} & {aktivitas_hari_ini[1]}")
    print(f"  Energi    : {sisa_energi}%", end=" -> ")

    # IF/ELIF/ELSE: cek kondisi energi
    if sisa_energi >= 70:
        print("Semangat!")
    elif sisa_energi >= 40:
        print("Biasa aja.")
    else:
        print("Ngantuk banget...")

# ============================================================
# STATISTIK MENGGUNAKAN MATH
# ============================================================

print("\n" + "=" * 55)
print(" Statistik Berat Badan Kucing:")
print("-" * 55)

berat_list = [info["berat"] for info in data_kucing.values()]

# math: hitung rata-rata manual
rata_rata = sum(berat_list) / len(berat_list)

# math: hitung standar deviasi manual menggunakan math.sqrt
variansi  = sum(math.pow(b - rata_rata, 2) for b in berat_list) / len(berat_list)
std_dev   = round(math.sqrt(variansi), 2)

print(f"  Berat semua kucing : {berat_list}")
print(f"  Rata-rata berat    : {round(rata_rata, 2)} kg")
print(f"  Standar deviasi    : {std_dev} kg")
print(f"  Berat tertinggi    : {max(berat_list)} kg")
print(f"  Berat terendah     : {min(berat_list)} kg")

# ============================================================
# CEK KUCING FAVORIT MENGGUNAKAN WHILE & SET
# ============================================================

print("\n" + "=" * 55)
print(" Kucing Mana yang Paling Aktif Hari Ini?")
print("-" * 55)

# SET: kumpulkan kucing yang sudah dapat aktivitas unik
kucing_aktif   = set()
kucing_malas   = set()
semua_kucing   = set(nama_kucing)

# WHILE LOOP: cek satu per satu sampai semua terklasifikasi
index = 0
while index < len(nama_kucing):
    nama  = nama_kucing[index]
    skor  = random.randint(1, 10)  # random: skor keaktifan 1-10

    # IF/ELSE: klasifikasikan kucing
    if skor >= 6:
        kucing_aktif.add(nama)
    else:
        kucing_malas.add(nama)
    index += 1

# SET DIFFERENCE & INTERSECTION
print(f"  Aktif  : {', '.join(sorted(kucing_aktif))  or '-'}")
print(f"  Santai : {', '.join(sorted(kucing_malas)) or '-'}")

# Konfirmasi semua kucing sudah terklasifikasi (union harus = semua_kucing)
terklasifikasi = kucing_aktif | kucing_malas
if terklasifikasi == semua_kucing:
    print(f"\n  Semua {len(semua_kucing)} kucing sudah terklasifikasi!")

print("\n" + "=" * 55)
print("  Program selesai. Meong! <(=^.w.^=)>")
print("=" * 55)