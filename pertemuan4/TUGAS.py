import tkinter as tk
from tkinter import messagebox

# Knowledge Base Kerusakan Komputer
database_kerusakan = {
    "RAM Rusak": {
        "gejala": ["blue_screen", "sering_restart", "gagal_booting", "bunyi_beep"],
        "solusi": "Coba bersihkan pin RAM dengan penghapus karet, lalu pasang kembali. Jika masih bermasalah, ganti RAM dengan yang baru."
    },
    "Overheat (Prosesor)": {
        "gejala": ["mati_sendiri", "kipas_berisik", "lambat", "panas_berlebih"],
        "solusi": "Bersihkan heatsink dan kipas dari debu. Ganti thermal paste pada prosesor. Pastikan ventilasi laptop/PC tidak tertutup."
    },
    "Hardisk Corrupt": {
        "gejala": ["lambat", "gagal_booting", "file_hilang", "bunyi_klik"],
        "solusi": "Jalankan CHKDSK untuk memeriksa bad sector. Segera backup data penting. Pertimbangkan mengganti HDD dengan SSD."
    },
    "VGA Bermasalah": {
        "gejala": ["layar_artefak", "blue_screen", "layar_hitam", "resolusi_berubah"],
        "solusi": "Update atau reinstall driver VGA. Jika masalah berlanjut, cek koneksi kabel VGA atau ganti kartu grafis."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["mati_sendiri", "gagal_booting", "sering_restart", "tidak_menyala"],
        "solusi": "Periksa kabel daya dan konektor PSU. Ukur tegangan output PSU dengan multimeter. Jika tidak stabil, ganti PSU dengan yang baru."
    },
    "Motherboard Bermasalah": {
        "gejala": ["tidak_menyala", "bunyi_beep", "blue_screen", "port_tidak_berfungsi"],
        "solusi": "Reset BIOS dengan melepas baterai CMOS selama 5 menit. Periksa kapasitor yang kembung. Jika parah, bawa ke teknisi."
    },
    "Infeksi Virus/Malware": {
        "gejala": ["lambat", "file_hilang", "program_aneh", "iklan_muncul"],
        "solusi": "Jalankan antivirus terpercaya (Windows Defender / Malwarebytes). Pertimbangkan install ulang sistem operasi jika infeksi parah."
    }
}

# GEJALA DAN PERTANYAAN
semua_gejala = [
    ("blue_screen",        "Apakah komputer/laptop sering mengalami Blue Screen (BSOD)?"),
    ("sering_restart",     "Apakah komputer/laptop sering restart sendiri secara tiba-tiba?"),
    ("gagal_booting",      "Apakah komputer/laptop gagal atau lama saat booting?"),
    ("bunyi_beep",         "Apakah terdengar bunyi beep panjang/berulang saat dinyalakan?"),
    ("mati_sendiri",       "Apakah komputer/laptop mati sendiri tanpa peringatan?"),
    ("kipas_berisik",      "Apakah kipas/fan terdengar sangat berisik dan kencang?"),
    ("lambat",             "Apakah komputer/laptop terasa sangat lambat saat digunakan?"),
    ("panas_berlebih",     "Apakah badan laptop/PC terasa sangat panas saat digunakan?"),
    ("file_hilang",        "Apakah ada file yang tiba-tiba hilang atau tidak bisa dibuka?"),
    ("bunyi_klik",         "Apakah terdengar bunyi klik-klik dari dalam laptop/PC?"),
    ("layar_artefak",      "Apakah layar menampilkan garis, kotak, atau warna aneh?"),
    ("layar_hitam",        "Apakah layar tiba-tiba menjadi hitam saat digunakan?"),
    ("resolusi_berubah",   "Apakah resolusi layar berubah sendiri atau tampak buram?"),
    ("tidak_menyala",      "Apakah komputer/laptop sama sekali tidak mau menyala?"),
    ("port_tidak_berfungsi","Apakah ada port USB/HDMI/audio yang tiba-tiba tidak berfungsi?"),
    ("program_aneh",       "Apakah ada program asing yang berjalan sendiri tanpa Anda buka?"),
    ("iklan_muncul",       "Apakah sering muncul iklan pop-up secara tiba-tiba?"),
]

class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Kerusakan Komputer")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # Label Judul
        self.label_judul = tk.Label(root, text="SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER", font=("Arial", 11, "bold"))
        self.label_judul.pack(pady=10)

        # Label Pertanyaan
        self.label_tanya = tk.Label(root, text="Selamat Datang di Sistem Pakar\nDiagnosa Kerusakan Komputer/Laptop", font=("Arial", 11), wraplength=450, justify="center")
        self.label_tanya.pack(pady=15)

        # Tombol Mulai
        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", font=("Arial", 10), command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        # Frame Tombol Jawaban
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, font=("Arial", 10), command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10, font=("Arial", 10), command=lambda: self.jawab('t'))
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget() 
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil = []
        for kerusakan, data in database_kerusakan.items():
            # untuk cek gejala_terpilih mengandung semua syarat kerusakan ngga
            if all(s in self.gejala_terpilih for s in data["gejala"]):
                hasil.append((kerusakan, data["solusi"]))

        if hasil:
            pesan = "Berdasarkan gejala Anda:\n\n"
            for nama, solusi in hasil:
                pesan += f">> Terdeteksi: {nama}\n"
                pesan += f"   Solusi: {solusi}\n\n"
        else:
            pesan = ("Tidak terdeteksi kerusakan spesifik berdasarkan gejala yang Anda masukkan.\n\n"
                     "Saran: Coba konsultasikan ke teknisi komputer terdekat untuk pemeriksaan lebih lanjut.")

        messagebox.showinfo("Hasil Diagnosa", pesan)

        # Reset ke awal
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mengulang?")

# Menjalankan Aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x280")
    app = AplikasiPakar(root)
    root.mainloop()