# Sistem Pakar Diagnosa Penyakit THT

## Identitas
Nama: Intan Ayu Tsalisatul Arifah  
NIM: H1D024027  
Shift KRS : F
Shift Baru :E

## Deskripsi
Aplikasi ini merupakan sistem pakar berbasis GUI yang digunakan untuk mendiagnosa penyakit Telinga, Hidung, dan Tenggorokan (THT) berdasarkan gejala yang dialami pengguna.

Aplikasi dibuat menggunakan bahasa pemrograman Python dengan library Tkinter.

## Metode

### Forward Chaining
Metode forward chaining digunakan untuk menarik kesimpulan dari fakta (gejala yang dipilih user) menuju kesimpulan (penyakit). Sistem akan mencocokkan gejala yang dipilih dengan aturan (rule) pada basis pengetahuan.

## Rule-Based System (Aturan Nyata)
Berikut adalah rule yang digunakan dalam sistem:

1. IF G37 AND G12 AND G5 AND G27 AND G6 AND G21 THEN Tonsilitis  
2. IF G37 AND G12 AND G27 AND G17 AND G33 AND G36 AND G29 THEN Sinusitis Maksilaris  
3. IF G37 AND G12 AND G27 AND G17 AND G33 AND G36 AND G21 AND G26 THEN Sinusitis Frontalis  
4. IF G37 AND G12 AND G27 AND G17 AND G33 AND G36 AND G21 AND G30 AND G13 AND G26 THEN Sinusitis Etmoidalis  
5. IF G37 AND G12 AND G27 AND G17 AND G33 AND G36 AND G29 AND G7 THEN Sinusitis Sfenoidalis  
6. IF G37 AND G12 AND G6 AND G15 AND G2 AND G29 AND G10 THEN Abses Peritonsiler  
7. IF G37 AND G5 AND G6 AND G7 AND G15 THEN Faringitis  
8. IF G5 AND G27 AND G6 AND G15 AND G2 AND G19 AND G1 THEN Kanker Laring  
9. IF G37 AND G17 AND G20 AND G8 AND G18 AND G25 THEN Deviasi Septum  
10. IF G37 AND G5 AND G15 AND G16 AND G32 THEN Laringitis  
11. IF G5 AND G22 AND G8 AND G28 AND G3 AND G11 THEN Kanker Leher & Kepala  
12. IF G37 AND G20 AND G35 AND G31 THEN Otitis Media Akut  
13. IF G5 AND G2 THEN Contact Ulcers  
14. IF G5 AND G16 THEN Abses Parafaringeal  
15. IF G12 AND G20 THEN Barotitis Media  
16. IF G17 AND G8 THEN Kanker Nasofaring  
17. IF G6 AND G29 THEN Kanker Tonsil  
18. IF G35 AND G24 THEN Neuronitis Vestibularis  
19. IF G20 AND G35 AND G14 AND G4 THEN Meniere  
20. IF G12 AND G34 AND G23 THEN Tumor Syaraf Pendengaran  
21. IF G29 THEN Kanker Leher Metastatik  
22. IF G34 AND G9 THEN Otosklerosis  
23. IF G24 THEN Vertigo Postural  

## Cara Kerja Sistem
1. User menekan tombol "Mulai Diagnosa"
2. Sistem menampilkan pertanyaan gejala satu per satu
3. User menjawab YA atau TIDAK
4. Sistem menyimpan gejala yang dipilih
5. Sistem mencocokkan dengan rule
6. Jika semua gejala pada suatu rule terpenuhi, maka penyakit ditampilkan

## Kesimpulan
Sistem pakar ini menggunakan metode forward chaining berbasis rule untuk menentukan diagnosa penyakit THT berdasarkan gejala yang dipilih pengguna.