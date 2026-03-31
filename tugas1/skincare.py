# ============================================================
# PROGRAM : Sistem Rekomendasi Skincare
# PRAKTIKUM: Kecerdasan Buatan - Pertemuan 1
# LIBRARY  : random, math
# ============================================================

import random
import math

# ============================================================
# STRUKTUR DATA
# ============================================================

# TUPLE: jenis kulit (immutable, tidak bisa diubah)
jenis_kulit = ("berminyak", "kering", "normal", "kombinasi", "sensitif")

# LIST: produk skincare beserta kandungan utamanya
produk_skincare = [
    {"nama": "Gentle Foam Cleanser",      "jenis": "berminyak", "kandungan": "Salicylic Acid"},
    {"nama": "Hydrating Cream Cleanser",  "jenis": "kering",    "kandungan": "Ceramide"},
    {"nama": "Balancing Gel Cleanser",    "jenis": "normal",    "kandungan": "Green Tea"},
    {"nama": "Micellar Water",            "jenis": "kombinasi", "kandungan": "Niacinamide"},
    {"nama": "Soothing Milk Cleanser",    "jenis": "sensitif",  "kandungan": "Centella Asiatica"},
    {"nama": "Oil Control Toner",         "jenis": "berminyak", "kandungan": "Witch Hazel"},
    {"nama": "Rose Water Toner",          "jenis": "kering",    "kandungan": "Hyaluronic Acid"},
    {"nama": "Brightening Serum",         "jenis": "normal",    "kandungan": "Vitamin C"},
    {"nama": "Barrier Repair Moisturizer","jenis": "sensitif",  "kandungan": "Allantoin"},
    {"nama": "Matte Finish Moisturizer",  "jenis": "berminyak", "kandungan": "Zinc"},
    {"nama": "Rich Moisture Cream",       "jenis": "kering",    "kandungan": "Shea Butter"},
    {"nama": "Water Gel Moisturizer",     "jenis": "kombinasi", "kandungan": "Aloe Vera"},
]

# SET: masalah kulit yang umum (unik, tidak ada duplikat)
masalah_kulit_umum = {"jerawat", "kusam", "kerutan", "pori besar", "kemerahan", "flek hitam"}

# ============================================================
# FUNGSI-FUNGSI (user-defined function)
# ============================================================

def tampilkan_judul():
    print("=" * 50)
    print("     SISTEM REKOMENDASI SKINCARE SEDERHANA")
    print("=" * 50)

def hitung_skor_kulit(kelembapan, minyak, sensitivitas):
    """
    Menghitung skor kondisi kulit menggunakan library math.
    Skor dihitung dengan rumus berbasis logaritma dan akar.
    """
    skor_minyak       = math.log(minyak + 1) * 10       # math.log
    skor_kelembapan   = math.sqrt(kelembapan) * 5        # math.sqrt
    skor_sensitivitas = math.pow(sensitivitas, 1.2)      # math.pow

    total = round(skor_minyak + skor_kelembapan - skor_sensitivitas, 2)
    return total

def rekomendasi_produk(jenis):
    """Merekomendasikan produk berdasarkan jenis kulit."""
    cocok = [p for p in produk_skincare if p["jenis"] == jenis]

    # random.sample: pilih 2 produk acak
    if len(cocok) >= 2:
        pilihan = random.sample(cocok, 2)
    else:
        pilihan = cocok
    return pilihan

def tips_random(jenis):
    """Memberikan tips perawatan kulit secara acak."""
    tips = {
        "berminyak" : [
            "Cuci muka maksimal 2x sehari agar tidak over-cleansing.",
            "Gunakan moisturizer berbahan dasar air (water-based).",
            "Hindari produk yang mengandung alkohol tinggi.",
        ],
        "kering"    : [
            "Minum air putih minimal 8 gelas per hari.",
            "Gunakan moisturizer setelah mandi saat kulit masih lembap.",
            "Hindari mandi dengan air terlalu panas.",
        ],
        "normal"    : [
            "Tetap pakai sunscreen setiap hari meski kulit normal.",
            "Lakukan eksfoliasi ringan 1-2x seminggu.",
            "Pertahankan pola makan bergizi untuk kulit sehat.",
        ],
        "kombinasi" : [
            "Gunakan produk berbeda untuk zona T dan area pipi.",
            "Double cleansing bisa membantu menyeimbangkan kulit.",
            "Hindari over-moisturizing di area hidung dan dahi.",
        ],
        "sensitif"  : [
            "Selalu patch test produk baru sebelum dipakai.",
            "Hindari bahan aktif keras seperti AHA/BHA konsentrasi tinggi.",
            "Pilih produk berlabel hypoallergenic.",
        ],
    }
    return random.choice(tips[jenis])  # random.choice

def cek_masalah_kulit(masalah_pengguna):
    """Mengecek masalah kulit menggunakan operasi SET."""
    dikenali       = masalah_pengguna & masalah_kulit_umum   # intersection
    tidak_dikenali = masalah_pengguna - masalah_kulit_umum   # difference
    return dikenali, tidak_dikenali

# ============================================================
# PROGRAM UTAMA
# ============================================================

tampilkan_judul()

# --- Input jenis kulit ---
print("\nJenis kulit yang tersedia:")
for i, jenis in enumerate(jenis_kulit, start=1):
    print(f"  {i}. {jenis.capitalize()}")

# WHILE LOOP: validasi input
pilihan_valid = False
while not pilihan_valid:
    try:
        pilihan = int(input("\nPilih nomor jenis kulitmu (1-5): "))
        if 1 <= pilihan <= 5:
            kulit_user = jenis_kulit[pilihan - 1]
            pilihan_valid = True
        else:
            print("Nomor tidak valid, masukkan angka 1-5.")
    except ValueError:
        print("Input tidak valid, masukkan angka saja.")

print(f"\nJenis kulitmu: {kulit_user.upper()}")

# --- Input kondisi kulit (skala 1-10) ---
print("\nIsi kondisi kulitmu sekarang (skala 1-10):")

while True:
    try:
        kelembapan   = int(input("  Tingkat kelembapan    (1=sangat kering, 10=sangat lembap)    : "))
        minyak       = int(input("  Tingkat minyak        (1=sangat kering, 10=sangat berminyak) : "))
        sensitivitas = int(input("  Tingkat sensitivitas  (1=tidak sensitif, 10=sangat sensitif) : "))

        if all(1 <= x <= 10 for x in [kelembapan, minyak, sensitivitas]):
            break
        else:
            print("Semua nilai harus antara 1-10, coba lagi.")
    except ValueError:
        print("Masukkan angka saja.")

# --- Hitung skor kulit ---
skor = hitung_skor_kulit(kelembapan, minyak, sensitivitas)

print("\n" + "-" * 50)
print("HASIL ANALISIS KONDISI KULITMU")
print("-" * 50)
print(f"  Kelembapan   : {'█' * kelembapan} ({kelembapan}/10)")
print(f"  Minyak       : {'█' * minyak} ({minyak}/10)")
print(f"  Sensitivitas : {'█' * sensitivitas} ({sensitivitas}/10)")
print(f"  Skor kulit   : {skor}")

# IF/ELIF/ELSE: kategorikan skor
if skor >= 40:
    kondisi = "Berminyak & Lembap"
elif skor >= 25:
    kondisi = "Seimbang"
elif skor >= 10:
    kondisi = "Cenderung Kering"
else:
    kondisi = "Sangat Kering & Sensitif"

print(f"  Kondisi      : {kondisi}")

# --- Rekomendasi produk ---
print("\n" + "-" * 50)
print("REKOMENDASI PRODUK UNTUKMU")
print("-" * 50)

produk_rekomendasi = rekomendasi_produk(kulit_user)

for i, produk in enumerate(produk_rekomendasi, start=1):
    print(f"  {i}. {produk['nama']}")
    print(f"     Kandungan utama : {produk['kandungan']}")

# --- Tips perawatan ---
print("\n" + "-" * 50)
print("TIPS PERAWATAN HARI INI")
print("-" * 50)
print(f"  {tips_random(kulit_user)}")

# --- Cek masalah kulit ---
print("\n" + "-" * 50)
print("CEK MASALAH KULITMU")
print("-" * 50)
print("Masalah yang bisa dicek:", ", ".join(sorted(masalah_kulit_umum)))

masalah_input = input("\nTulis masalah kulitmu (pisah koma, contoh: jerawat, kusam): ").lower()
masalah_user  = set(m.strip() for m in masalah_input.split(",") if m.strip())

dikenali, tidak_dikenali = cek_masalah_kulit(masalah_user)

saran = {
    "jerawat"    : "Gunakan produk dengan Salicylic Acid atau Niacinamide.",
    "kusam"      : "Coba serum Vitamin C di pagi hari.",
    "kerutan"    : "Gunakan retinol di malam hari secara bertahap.",
    "pori besar" : "Toner dengan Witch Hazel bisa membantu mengecilkan pori.",
    "kemerahan"  : "Hindari bahan iritan, coba Centella Asiatica.",
    "flek hitam" : "Gunakan sunscreen SPF 30+ setiap hari tanpa skip.",
}

if dikenali:
    print(f"\n  Masalah terdeteksi : {', '.join(sorted(dikenali))}")
    print("\n  Saran:")
    for masalah in sorted(dikenali):
        print(f"  - {masalah.capitalize()}: {saran[masalah]}")

if tidak_dikenali:
    print(f"\n  Masalah tidak dikenali: {', '.join(sorted(tidak_dikenali))}")
    print("  Sebaiknya konsultasikan ke dokter kulit ya!")

# --- Penutup ---
print("\n" + "=" * 50)
kode_rekomendasi = random.randint(1000, 9999)   # random.randint
print(f"  Kode rekomendasimu hari ini : SK-{kode_rekomendasi}")
print("  Selamat merawat kulitmu! Konsisten adalah kunci.")
print("=" * 50)