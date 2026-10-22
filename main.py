import tkinter as tk

# Membuat jendela aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x550")

# Label judul
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold")
)
judul.pack(pady=15)

# Daftar mata pelajaran
mapel = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Informatika",
    "Ekonomi",
    "Sosiologi",
    "Geografi"
]

# Membuat input nilai
input_nilai = []

for pelajaran in mapel:
    frame = tk.Frame(root)
    frame.pack(pady=3)

    label = tk.Label(frame, text=pelajaran, width=18, anchor="w")
    label.pack(side="left")

    entry = tk.Entry(frame, width=15)
    entry.pack(side="left")

    input_nilai.append(entry)

# Fungsi hasil prediksi
def hasil_prediksi():
    hasil.config(text="Hasil Prediksi: Teknologi Informasi")

# Tombol prediksi
tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
tombol.pack(pady=15)

# Label hasil prediksi
hasil = tk.Label(
    root,
    text="Hasil prediksi akan muncul di sini",
    font=("Arial", 11, "bold")
)
hasil.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()