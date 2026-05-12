# Praktikum 6 - Jaringan Syaraf Tiruan (JST)
Implementasi **Perceptron** dan **Backpropagation** menggunakan Python untuk menyelesaikan masalah OR dan XOR.

Nama  : Intan Ayu Tsalisatul Arifah 
NIM   : H1D024027  
Shift KRS : F
Shift Baru : E
---

## Struktur File

```
├── Perceptron.py           # Kelas utama model Perceptron
├── Perceptron_or.py        # Runner masalah OR dengan Perceptron
├── Backpropagation.py      # Kelas utama model Backpropagation
├── Backpropagation_xor.py  # Runner masalah XOR dengan Backpropagation
├── HasilPerceptron.txt     # Output hasil pelatihan Perceptron (auto-generated)
├── hasilBackpropagation.txt # Output hasil pelatihan Backpropagation (auto-generated)
└── README.md
```

---

## Requirements

- Python 3.x
- NumPy
- Matplotlib

Install dependencies:
```bash
pip install numpy matplotlib
```

---

## Cara Menjalankan

### 1. Masalah OR — Perceptron

```bash
python Perceptron_or.py
```

**Konfigurasi:**
| Parameter     | Nilai |
|---------------|-------|
| Input         | Bipolar (1, -1) |
| Learning rate | 0.1   |
| Epoch         | 10    |
| Bobot awal    | 0     |

**Data OR Bipolar:**
| x1 | x2 | target |
|----|----|--------|
| 1  | 1  | 1      |
| 1  | -1 | 1      |
| -1 | 1  | 1      |
| -1 | -1 | -1     |

**Output:**
- Grafik *decision boundary* setiap epoch ditampilkan
- Hasil perhitungan tersimpan di `HasilPerceptron.txt`

---

### 2. Masalah XOR — Backpropagation

```bash
python Backpropagation_xor.py
```

**Konfigurasi:**
| Parameter     | Nilai  |
|---------------|--------|
| Input         | Bipolar (1, -1) |
| Learning rate | 0.3    |
| Max Epoch     | 1000   |
| Target Error  | 0.001  |
| Hidden Layer  | 2 neuron |
| Bobot awal    | Random (0–1) |

**Data XOR Bipolar:**
| x1 | x2 | target |
|----|----|--------|
| 1  | 1  | -1     |
| 1  | -1 | 1      |
| -1 | 1  | 1      |
| -1 | -1 | -1     |

**Output:**
- Grafik penurunan *Sum Square Error* (SSE) per epoch ditampilkan
- Hasil perhitungan tersimpan di `hasilBackpropagation.txt`

---

## Konsep

### Perceptron
Model jaringan berlayer tunggal dengan pembelajaran terawasi. Menggunakan **Delta Rule** untuk memperbarui bobot:

```
Δwi = α * (ti - yi) * xi
wi  = wi + Δwi
```

Fungsi aktivasi yang digunakan: **Bipolar Step Function**
- Output = 1 jika y_in ≥ 0
- Output = -1 jika y_in < 0

### Backpropagation
Model jaringan multi-layer dengan hidden layer. Terdiri dari dua fase:

- **Forward Propagation** — menghitung output dari input layer → hidden layer → output layer
- **Backward Propagation** — menghitung error dan memperbarui bobot dari output layer → hidden layer

Fungsi aktivasi yang digunakan: **Tanh (Sigmoid Bipolar)**
```
y = tanh(y_in)
y' = 1 - y²
```

---

## Kondisi Berhenti

| Model              | Kondisi Berhenti                        |
|--------------------|-----------------------------------------|
| Perceptron         | SSE = 0 **atau** max epoch tercapai     |
| Backpropagation    | SSE < target error **atau** max epoch tercapai |

---

## Catatan

- Bobot awal Backpropagation bersifat **random**, sehingga jumlah epoch hingga konvergen bisa berbeda setiap kali dijalankan.
- Perceptron **tidak dapat** menyelesaikan masalah XOR karena keterbatasan pemisahan linier — itulah mengapa Backpropagation dengan hidden layer diperlukan.
