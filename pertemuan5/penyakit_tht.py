import tkinter as tk
from tkinter import messagebox

# DATABASE PENYAKIT 
database_penyakit = {
    "Tonsilitis": ["G37","G12","G5","G27","G6","G21"],
    "Sinusitis Maksilaris": ["G37","G12","G27","G17","G33","G36","G29"],
    "Sinusitis Frontalis": ["G37","G12","G27","G17","G33","G36","G21","G26"],
    "Sinusitis Etmoidalis": ["G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"],
    "Sinusitis Sfenoidalis": ["G37","G12","G27","G17","G33","G36","G29","G7"],
    "Abses Peritonsiler": ["G37","G12","G6","G15","G2","G29","G10"],
    "Faringitis": ["G37","G5","G6","G7","G15"],
    "Kanker Laring": ["G5","G27","G6","G15","G2","G19","G1"],
    "Deviasi Septum": ["G37","G17","G20","G8","G18","G25"],
    "Laringitis": ["G37","G5","G15","G16","G32"],
    "Kanker Leher & Kepala": ["G5","G22","G8","G28","G3","G11"],
    "Otitis Media Akut": ["G37","G20","G35","G31"],
    "Contact Ulcers": ["G5","G2"],
    "Abses Parafaringeal": ["G5","G16"],
    "Barotitis Media": ["G12","G20"],
    "Kanker Nasofaring": ["G17","G8"],
    "Kanker Tonsil": ["G6","G29"],
    "Neuronitis Vestibularis": ["G35","G24"],
    "Meniere": ["G20","G35","G14","G4"],
    "Tumor Syaraf Pendengaran": ["G12","G34","G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Otosklerosis": ["G34","G9"],
    "Vertigo Postural": ["G24"],
}

# DATA GEJALA
semua_gejala = [
    ("G1","Nafas abnormal"),("G2","Suara serak"),("G3","Perubahan kulit"),
    ("G4","Telinga penuh"),("G5","Nyeri bicara/menelan"),("G6","Nyeri tenggorokan"),
    ("G7","Nyeri leher"),("G8","Pendarahan hidung"),("G9","Telinga berdenging"),
    ("G10","Air liur menetes"),("G11","Perubahan suara"),("G12","Sakit kepala"),
    ("G13","Nyeri pinggir hidung"),("G14","Serangan vertigo"),("G15","Getah bening"),
    ("G16","Leher bengkak"),("G17","Hidung tersumbat"),("G18","Infeksi sinus"),
    ("G19","Berat badan turun"),("G20","Nyeri telinga"),("G21","Selaput lendir merah"),
    ("G22","Benjolan leher"),("G23","Tubuh tak seimbang"),("G24","Bola mata bergerak"),
    ("G25","Nyeri wajah"),("G26","Dahi sakit"),("G27","Batuk"),
    ("G28","Tumbuh di mulut"),("G29","Benjolan di leher"),("G30","Nyeri antara mata"),
    ("G31","Radang gendang telinga"),("G32","Tenggorokan gatal"),
    ("G33","Hidung meler"),("G34","Tuli"),("G35","Mual/muntah"),
    ("G36","Letih lesu"),("G37","Demam"),
]

class AplikasiPakarTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar THT")
        self.root.geometry("520x300")
        self.root.resizable(False, False)

        self.gejala_terpilih = []
        self.index = 0

        tk.Label(root, text="SISTEM PAKAR DIAGNOSA PENYAKIT THT",
                 font=("Arial", 11, "bold")).pack(pady=10)

        self.label = tk.Label(root, text="Selamat Datang di Sistem Pakar\nDiagnosa Penyakit Telinga, Hidung & Tenggorokan",
                              font=("Arial", 11), wraplength=450, justify="center")
        self.label.pack(pady=15)

        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa",
                                   command=self.mulai)
        self.btn_mulai.pack()

        self.frame_btn = tk.Frame(root)
        self.btn_yes = tk.Button(self.frame_btn, text="YA", width=10,
                                 command=lambda: self.jawab(True))
        self.btn_no = tk.Button(self.frame_btn, text="TIDAK", width=10,
                                command=lambda: self.jawab(False))
        self.btn_yes.pack(side=tk.LEFT, padx=10)
        self.btn_no.pack(side=tk.LEFT, padx=10)

    # MULAI DIAGNOSA
    def mulai(self):
        self.gejala_terpilih = []
        self.index = 0
        self.btn_mulai.pack_forget()
        self.frame_btn.pack(pady=20)
        self.tanya()

    # TANYA GEJALA
    def tanya(self):
        if self.index < len(semua_gejala):
            kode, nama = semua_gejala[self.index]
            self.label.config(
                text=f"Apakah Anda mengalami {nama} ?"
            )
        else:
            self.diagnosa()

    # JAWABAN USER
    def jawab(self, ya):
        if ya:
            kode = semua_gejala[self.index][0]
            self.gejala_terpilih.append(kode)
        self.index += 1
        self.tanya()

    # PROSES DIAGNOSA 
    def diagnosa(self):
        hasil = []

        for penyakit, rule in database_penyakit.items():
            if all(g in self.gejala_terpilih for g in rule):
                hasil.append(penyakit)

        if hasil:
            pesan = "Diagnosa ditemukan:\n\n"
            for p in hasil:
                pesan += f"- {p}\n"
        else:
            pesan = ("Tidak ada penyakit yang cocok secara pasti.\n\n"
                     "Silakan konsultasi ke dokter THT.")

        messagebox.showinfo("Hasil Diagnosa", pesan)

        # reset
        self.frame_btn.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label.config(text="Diagnosa selesai.\nKlik MULAI untuk ulangi.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPakarTHT(root)
    root.mainloop()
    