import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# =======================
# CLASS MAHASISWA
# =======================
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = float(ipk)

    def info(self):
        return f"{self.nim} - {self.nama} - {self.jurusan} - {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = float(ipk_baru)


# =======================
# DATA COLLECTIONS
# =======================
data_mhs = {}  # dictionary: nim -> object Mahasiswa


# =======================
# FUNGSI CRUD
# =======================
def tambah_mahasiswa():
    nim = entry_nim.get()
    nama = entry_nama.get()
    jurusan = entry_jurusan.get()
    ipk = entry_ipk.get()

    if nim in data_mhs:
        messagebox.showerror("Error", "NIM sudah terdaftar!")
        return
    if not (nim and nama and jurusan and ipk):
        messagebox.showwarning("Warning", "Semua field harus diisi!")
        return

    try:
        data_mhs[nim] = Mahasiswa(nim, nama, jurusan, float(ipk))
        tampilkan_semua()
        clear_input()
    except:
        messagebox.showerror("Error", "IPK harus berupa angka!")


def tampilkan_semua():
    tree.delete(*tree.get_children())
    for mhs in data_mhs.values():
        tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))


def hapus_mahasiswa():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Pilih data yang akan dihapus!")
        return

    nim = tree.item(selected)['values'][0]
    del data_mhs[nim]
    tampilkan_semua()


def update_mahasiswa():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Pilih data yang akan diupdate!")
        return

    nim = entry_nim.get()
    ipk_baru = entry_ipk.get()

    try:
        data_mhs[nim].update_ipk(float(ipk_baru))
        tampilkan_semua()
    except:
        messagebox.showerror("Error", "IPK harus berupa angka!")


# =======================
# FITUR TAMBAHAN
# =======================
def cari_mhs():
    keyword = entry_search.get().lower()
    tree.delete(*tree.get_children())

    for mhs in data_mhs.values():
        if keyword in mhs.nim.lower() or keyword in mhs.nama.lower():
            tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))


def filter_jurusan():
    jur = entry_filter.get().lower()
    tree.delete(*tree.get_children())

    for mhs in data_mhs.values():
        if jur in mhs.jurusan.lower():
            tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))


def hitung_rata_ipk():
    if not data_mhs:
        messagebox.showinfo("Info", "Data kosong!")
        return
    avg = sum(m.ipk for m in data_mhs.values()) / len(data_mhs)
    messagebox.showinfo("Rata-rata IPK", f"Rata-rata IPK: {avg:.2f}")


def ipk_tertinggi():
    if not data_mhs:
        messagebox.showinfo("Info", "Data kosong!")
        return
    mhs = max(data_mhs.values(), key=lambda x: x.ipk)
    messagebox.showinfo("IPK Tertinggi", f"Mahasiswa dengan IPK tertinggi:\n{mhs.info()}")


def export_data():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
    if file:
        with open(file, "w") as f:
            for m in data_mhs.values():
                f.write(m.info() + "\n")
        messagebox.showinfo("Export", "Data berhasil diexport!")


def clear_input():
    entry_nim.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    entry_jurusan.delete(0, tk.END)
    entry_ipk.delete(0, tk.END)


# =======================
# GUI TKINTER
# =======================
root = tk.Tk()
root.title("Sistem Manajemen Mahasiswa - Modul GUI & Collections")
root.geometry("800x500")

# Frame Input
frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
frame_input.pack(fill="x")

tk.Label(frame_input, text="NIM").grid(row=0, column=0)
entry_nim = tk.Entry(frame_input)
entry_nim.grid(row=0, column=1)

tk.Label(frame_input, text="Nama").grid(row=1, column=0)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=1, column=1)

tk.Label(frame_input, text="Jurusan").grid(row=2, column=0)
entry_jurusan = tk.Entry(frame_input)
entry_jurusan.grid(row=2, column=1)

tk.Label(frame_input, text="IPK").grid(row=3, column=0)
entry_ipk = tk.Entry(frame_input)
entry_ipk.grid(row=3, column=1)

# Tombol CRUD
frame_btn = tk.Frame(root)
frame_btn.pack()

tk.Button(frame_btn, text="Tambah", command=tambah_mahasiswa).grid(row=0, column=0)
tk.Button(frame_btn, text="Update IPK", command=update_mahasiswa).grid(row=0, column=1)
tk.Button(frame_btn, text="Hapus", command=hapus_mahasiswa).grid(row=0, column=2)
tk.Button(frame_btn, text="Tampil Semua", command=tampilkan_semua).grid(row=0, column=3)

# Treeview
tree = ttk.Treeview(root, columns=("nim", "nama", "jurusan", "ipk"), show="headings")
for col in ("nim", "nama", "jurusan", "ipk"):
    tree.heading(col, text=col)
tree.pack(fill="both", expand=True)

# Cari & Filter
frame_search = tk.Frame(root)
frame_search.pack(fill="x")

tk.Entry(frame_search, text="", width=25, textvariable=tk.StringVar(), name="search").pack(side="left")
entry_search = frame_search.children["search"]

tk.Button(frame_search, text="Cari NIM/Nama", command=cari_mhs).pack(side="left", padx=5)

entry_filter = tk.Entry(frame_search)
entry_filter.pack(side="left", padx=5)
tk.Button(frame_search, text="Filter Jurusan", command=filter_jurusan).pack(side="left")

# Fitur tambahan
frame_extra = tk.Frame(root)
frame_extra.pack(fill="x", pady=10)

tk.Button(frame_extra, text="Rata-rata IPK", command=hitung_rata_ipk).pack(side="left")
tk.Button(frame_extra, text="IPK Tertinggi", command=ipk_tertinggi).pack(side="left", padx=5)
tk.Button(frame_extra, text="Export ke TXT", command=export_data).pack(side="left")

root.mainloop()
