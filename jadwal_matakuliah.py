import tkinter as tk

def tampilkan_jadwal():
    hari = input_hari.get().lower()
    jadwal = {
        "senin": [
            {"Mata_Kuliah": "Arsitektur dan Organisasi Komputer", "Waktu": "08.00-10.00"},
            {"Mata_Kuliah": "AIK II", "Waktu": "10.00-11.40"}
        ],
        "selasa": [
            {"Mata_Kuliah": "PBO II", "Waktu": "13.00-15.30"}
        ],
        "rabu": [
            {"Mata_Kuliah": "Kalkulus II", "Waktu": "08.00-10.00"},
            {"Mata_Kuliah": "Sistem Informasi (APSI)", "Waktu": "13.00-15.30"}
        ],
        "kamis": [
            {"Mata_Kuliah": "Libur"}
        ],
        "jumat": [
            {"Mata_Kuliah": "Komunikasi Data", "Waktu": "10.00-11.40"},
            {"Mata_Kuliah": "Statistika dan Probabilitas", "Waktu": "13.00-14.40"},
            {"Mata_Kuliah": "Struktur Data", "Waktu": "15.00-17.30"}
        ]
    }
    jadwal_hari = jadwal.get(hari, [{"Mata_Kuliah": "Tidak ada mata kuliah"}])
    
    text_jadwal.delete(1.0, tk.END)
    
    for mata in jadwal_hari:
        if 'Waktu' in mata:
            text_jadwal.insert(tk.END, f"{mata['Mata_Kuliah']} ({mata['Waktu']})\n")
        else:
            text_jadwal.insert(tk.END, f"{mata['Mata_Kuliah']}\n")

# Membuat jendela utama
root = tk.Tk()
root.title("Jadwal Mata Kuliah Universitas Muhammadiyah Cirebon")

# Membuat elemen-elemen UI
label = tk.Label(root, text="Masukkan hari:", font=("Arial", 14))
label.pack(pady=10)

input_hari = tk.Entry(root, font=("Arial", 12), width=20)
input_hari.pack(pady=10)

tampilkan_button = tk.Button(root, text="Tampilkan Jadwal", command=tampilkan_jadwal, font=("Arial", 12), bg="#4CAF50", fg="white")
tampilkan_button.pack(pady=20)

text_jadwal = tk.Text(root, width=70, height=10, font=("Arial", 12))
text_jadwal.pack(pady=10)

label_nama = tk.Label(root, text="Marsilo Danang W_220511102:", font=("Arial", 12))
label_nama.pack()

# Menjalankan aplikasi
root.mainloop()
