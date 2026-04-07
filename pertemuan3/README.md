# Sistem Inferensi Fuzzy — Mamdani
**Implementasi Logika Fuzzy dengan Python & scikit-fuzzy**

---

## Deskripsi Proyek

Repositori ini berisi dua studi kasus implementasi **Sistem Inferensi Fuzzy (FIS) metode Mamdani** menggunakan Python. Setiap studi kasus memiliki variabel, membership function, dan aturan fuzzy yang berbeda sesuai domain permasalahannya.

| Studi Kasus | Domain | File |
|---|---|---|
| Studi Kasus 1 | Rekomendasi Stok Makanan Toko Hewan | `fuzzy_toko_hewan.py` |
| Studi Kasus 2 | Evaluasi Kepuasan Pelayanan Masyarakat | `fuzzy_pelayanan_masyarakat.py` |

---

## Instalasi & Kebutuhan Sistem

### Prasyarat
Python 3.8 atau lebih baru. Pastikan pip tersedia.

### Instalasi Dependensi
```bash
pip install numpy scikit-fuzzy matplotlib
```

| Library | Versi Minimum | Fungsi |
|---|---|---|
| numpy | 1.21.0 | Komputasi array dan numerik |
| scikit-fuzzy (skfuzzy) | 0.4.2 | Engine logika fuzzy |
| matplotlib | 3.4.0 | Visualisasi grafik membership function |

---

## Cara Menjalankan

```bash
# Studi Kasus 1
python fuzzy_toko_hewan.py

# Studi Kasus 2
python fuzzy_pelayanan_masyarakat.py
```

---

---

# Studi Kasus 1 — Rekomendasi Stok Makanan Toko Hewan

## Deskripsi

Sistem fuzzy untuk merekomendasikan jumlah stok makanan hewan yang optimal berdasarkan kondisi penjualan dan keuntungan toko.

## Variabel Fuzzy

### Input (Antecedent)

| Variabel | Range | Himpunan Fuzzy |
|---|---|---|
| barang_terjual | 0 – 100 | rendah, sedang, tinggi |
| permintaan | 0 – 300 | rendah, sedang, tinggi |
| harga_item | 0 – 100.000 | murah, sedang, mahal |
| profit | 0 – 4.000.000 | rendah, sedang, banyak |

### Output (Consequent)

| Variabel | Range | Himpunan Fuzzy |
|---|---|---|
| stok_makanan | 0 – 1000 | sedang, banyak |

## Membership Functions

### Barang Terjual [0 – 100]
| Himpunan | Tipe | Parameter |
|---|---|---|
| rendah | trimf | [0, 0, 40] |
| sedang | trimf | [30, 50, 70] |
| tinggi | trimf | [60, 100, 100] |

### Permintaan [0 – 300]
| Himpunan | Tipe | Parameter |
|---|---|---|
| rendah | trimf | [0, 0, 100] |
| sedang | trimf | [50, 150, 250] |
| tinggi | trimf | [200, 300, 300] |

### Harga per Item [0 – 100.000]
| Himpunan | Tipe | Parameter |
|---|---|---|
| murah | trimf | [0, 0, 40.000] |
| sedang | trimf | [30.000, 50.000, 80.000] |
| mahal | trimf | [60.000, 100.000, 100.000] |

### Profit [0 – 4.000.000]
| Himpunan | Tipe | Parameter |
|---|---|---|
| rendah | trimf | [0, 0, 1.000.000] |
| sedang | trimf | [1.000.000, 2.000.000, 2.500.000] |
| banyak | trapmf | [1.500.000, 2.500.000, 4.000.000, 4.000.000] |

### Stok Makanan / Output [0 – 1000]
| Himpunan | Tipe | Parameter |
|---|---|---|
| sedang | trimf | [100, 500, 900] |
| banyak | trimf | [600, 1000, 1000] |

## Aturan Fuzzy (6 Rules)

| Rule | Kondisi (IF) | Aksi (THEN) |
|---|---|---|
| 1 | barang_terjual=tinggi AND permintaan=tinggi AND harga_item=murah AND profit=banyak | stok_makanan=banyak |
| 2 | barang_terjual=tinggi AND permintaan=tinggi AND harga_item=murah AND profit=sedang | stok_makanan=sedang |
| 3 | barang_terjual=tinggi AND permintaan=sedang AND harga_item=murah AND profit=sedang | stok_makanan=sedang |
| 4 | barang_terjual=sedang AND permintaan=tinggi AND harga_item=murah AND profit=sedang | stok_makanan=sedang |
| 5 | barang_terjual=sedang AND permintaan=tinggi AND harga_item=murah AND profit=banyak | stok_makanan=banyak |
| 6 | barang_terjual=rendah AND permintaan=rendah AND harga_item=sedang AND profit=sedang | stok_makanan=sedang |

## Contoh Input & Output

| Variabel Input | Nilai | Kategori Fuzzy Dominan |
|---|---|---|
| Barang Terjual | 80 unit | Tinggi |
| Permintaan | 255 unit | Tinggi |
| Harga per Item | Rp 25.000 | Murah |
| Profit | Rp 3.500.000 | Banyak |

**Rule 1** aktif → output terdorong ke `stok_makanan = banyak`.

## Referensi & Metode

| Aspek | Detail |
|---|---|
| Metode Fuzzy | Mamdani (skfuzzy ControlSystem) |
| Defuzzifikasi | Centroid of Area |
| Operator Rule | AND (minimum) |
| Aggregasi | Maximum |
| Jumlah Rules | 6 aturan |

---

---

# Studi Kasus 2 (Evaluasi Kepuasan Pelayanan Masyarakat)

## Deskripsi

Sistem fuzzy untuk mengukur tingkat kepuasan masyarakat terhadap pelayanan publik berdasarkan empat aspek penilaian. Dirancang untuk membantu instansi pemerintah atau lembaga pelayanan publik mengevaluasi kualitas layanan secara objektif.

## Variabel Fuzzy

### Input (Antecedent)

| Variabel | Range | Himpunan Fuzzy | Keterangan |
|---|---|---|---|
| kejelasan_informasi | 0 – 100 | tidak_memuaskan, cukup_memuaskan, memuaskan | Kejelasan informasi layanan |
| kejelasan_persyaratan | 0 – 100 | tidak_memuaskan, cukup_memuaskan, memuaskan | Kejelasan persyaratan administrasi |
| kemampuan_petugas | 0 – 100 | tidak_memuaskan, cukup_memuaskan, memuaskan | Kompetensi petugas |
| ketersediaan_sarpras | 0 – 100 | tidak_memuaskan, cukup_memuaskan, memuaskan | Ketersediaan sarana & prasarana |

### Output (Consequent)

| Variabel | Range | Himpunan Fuzzy |
|---|---|---|
| kepuasan_pelayanan | 0 – 400 | tidak_memuaskan, kurang_memuaskan, cukup_memuaskan, memuaskan, sangat_memuaskan |

## Membership Functions

### Input — Semua Variabel Input [0 – 100]

Keempat variabel input menggunakan pola membership function yang sama:

| Himpunan | Tipe | Parameter |
|---|---|---|
| tidak_memuaskan | trapmf | [0, 0, 60, 75] |
| cukup_memuaskan | trimf | [60, 75, 90] |
| memuaskan | trapmf | [75, 90, 100, 100] |

### Output — Kepuasan Pelayanan [0 – 400]

| Himpunan | Tipe | Parameter |
|---|---|---|
| tidak_memuaskan | trapmf | [0, 0, 50, 75] |
| kurang_memuaskan | trapmf | [50, 75, 100, 150] |
| cukup_memuaskan | trapmf | [100, 150, 250, 275] |
| memuaskan | trapmf | [250, 275, 325, 350] |
| sangat_memuaskan | trapmf | [325, 350, 400, 400] |

## Aturan Fuzzy (81 Rules)

Sistem menggunakan **81 aturan** — kombinasi lengkap dari 3 himpunan × 4 variabel input (3⁴ = 81).

### Pola Logika Umum

| Kondisi Input | Output |
|---|---|
| Semua tidak_memuaskan | kurang_memuaskan |
| Mayoritas tidak_memuaskan / cukup | cukup_memuaskan |
| Campuran memuaskan & tidak_memuaskan | cukup_memuaskan atau memuaskan |
| Mayoritas memuaskan | memuaskan |
| Semua memuaskan | sangat_memuaskan |

### Ringkasan Blok Aturan

| Blok (kejelasan_informasi) | Jumlah Aturan | Rentang Output |
|---|---|---|
| tidak_memuaskan (aturan 1–27) | 27 | kurang_memuaskan → sangat_memuaskan |
| cukup_memuaskan (aturan 28–54) | 27 | cukup_memuaskan → sangat_memuaskan |
| memuaskan (aturan 55–81) | 27 | cukup_memuaskan → sangat_memuaskan |

### Contoh Aturan Kunci

| Rule | Kondisi (IF) | Aksi (THEN) |
|---|---|---|
| 1 | info=tidak & syarat=tidak & petugas=tidak & sarpras=tidak | kurang_memuaskan |
| 9 | info=tidak & syarat=tidak & petugas=memuaskan & sarpras=memuaskan | memuaskan |
| 27 | info=tidak & syarat=memuaskan & petugas=memuaskan & sarpras=memuaskan | sangat_memuaskan |
| 41 | info=cukup & syarat=cukup & petugas=cukup & sarpras=cukup | memuaskan |
| 81 | info=memuaskan & syarat=memuaskan & petugas=memuaskan & sarpras=memuaskan | sangat_memuaskan |

## Contoh Input & Output

| Variabel Input | Nilai | Kategori Fuzzy Dominan |
|---|---|---|
| Kejelasan Informasi | 80 | Memuaskan |
| Kejelasan Persyaratan | 60 | Cukup Memuaskan (batas) |
| Kemampuan Petugas | 50 | Tidak Memuaskan |
| Ketersediaan Sarpras | 90 | Memuaskan |

Beberapa aturan aktif secara parsial; hasil akhir ditentukan melalui defuzzifikasi centroid dari agregasi seluruh output yang aktif.

## Referensi & Metode

| Aspek | Detail |
|---|---|
| Metode Fuzzy | Mamdani (skfuzzy ControlSystem) |
| Defuzzifikasi | Centroid of Area |
| Operator Rule | AND (minimum) |
| Aggregasi | Maximum |
| Jumlah Rules | 81 aturan (3⁴ kombinasi lengkap) |

---

## Struktur Repositori

```
.
├── fuzzy_toko_hewan.py            # Studi Kasus 1
├── fuzzy_pelayanan_masyarakat.py  # Studi Kasus 2
└── README.md                      # Dokumentasi ini
```

---

*Implementasi Logika Fuzzy Metode Mamdani — Python & scikit-fuzzy*
