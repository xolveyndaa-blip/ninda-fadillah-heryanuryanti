import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# ======== CLASS TUGAS (OBJECT) ========
class Tugas:
    def __init__(self, nama, status="Belum Selesai"):
        self.nama = nama
        self.status = status

    def selesai(self):
        self.status = "Selesai"

    def edit(self, nama_baru):
        self.nama = nama_baru


# ======== GUI TO-DO LIST APP ========
class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("500x400")

        # List of objects untuk menyimpan tugas
        self.daftar_tugas = []

        # ====== FRAME INPUT ======
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Nama Tugas:").grid(row=0, column=0)
        self.entry_tugas = tk.Entry(frame_input, width=40)
        self.entry_tugas.grid(row=0, column=1, padx=5, pady=5)

        # ====== FRAME TOMBOL ======
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah", command=self.tambah_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.selesai_tugas).pack(side=tk.LEFT, padx=5)

        # ====== TREEVIEW ======
        frame_tabel = tk.Frame(root)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_tabel, columns=("Nama", "Status"), show="headings")
        self.tree.heading("Nama", text="Nama Tugas")
        self.tree.heading("Status", text="Status")

        self.tree.pack(fill=tk.BOTH, expand=True)

    # ====== FUNGSI TAMBAH ======
    def tambah_tugas(self):
        nama = self.entry_tugas.get()
        if nama:
            tugas = Tugas(nama)
            self.daftar_tugas.append(tugas)
            self.tree.insert("", tk.END, values=(tugas.nama, tugas.status))
            self.entry_tugas.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama tugas tidak boleh kosong!")

    # ====== FUNGSI HAPUS ======
    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            del self.daftar_tugas[index]
            self.tree.delete(selected[0])
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus!")

    # ====== FUNGSI EDIT ======
    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]

            nama_baru = simpledialog.askstring("Edit Tugas", "Masukkan nama tugas baru:", initialvalue=tugas.nama)

            if nama_baru:
                tugas.edit(nama_baru)
                self.tree.item(selected[0], values=(tugas.nama, tugas.status))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin diedit!")

    # ====== FUNGSI TANDAI SELESAI ======
    def selesai_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]
            tugas.selesai()
            self.tree.item(selected[0], values=(tugas.nama, tugas.status))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin ditandai selesai!")


# ====== MAIN PROGRAM ======
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
