# =======================================
# TUGAS 3 - SISTEM MANAJEMEN PROYEK SEDERHANA
# =======================================

# Kelas utama yang merepresentasikan perusahaan
class Perusahaan:
    def __init__(self, nama):
        # Inisialisasi nama perusahaan
        self.nama = nama
        # Menyimpan daftar proyek yang dimiliki perusahaan
        self.proyek = []
        # Menyimpan daftar tim yang ada di perusahaan
        self.tim = []

    def buat_proyek(self, nama_proyek, deskripsi):
        # Membuat objek proyek baru
        proyek_baru = Proyek(nama_proyek, deskripsi)
        # Menambahkan proyek ke daftar proyek perusahaan
        self.proyek.append(proyek_baru)
        print(f"Proyek '{nama_proyek}' berhasil dibuat.")
        return proyek_baru

    def buat_tim(self, nama_tim):
        # Membuat objek tim baru
        tim_baru = Tim(nama_tim)
        # Menambahkan tim ke daftar tim perusahaan
        self.tim.append(tim_baru)
        print(f"Tim '{nama_tim}' berhasil dibuat.")
        return tim_baru


# Kelas Proyek menyimpan informasi tentang proyek dan tugas-tugasnya
class Proyek:
    def __init__(self, nama, deskripsi):
        # Inisialisasi nama dan deskripsi proyek
        self.nama = nama
        self.deskripsi = deskripsi
        # Menyimpan daftar tugas di proyek
        self.tugas = []

    def tambah_tugas(self, deskripsi_tugas):
        # Membuat objek tugas baru
        tugas_baru = Tugas(deskripsi_tugas)
        # Menambahkan ke daftar tugas proyek
        self.tugas.append(tugas_baru)
        print(f"Tugas '{deskripsi_tugas}' berhasil ditambahkan ke proyek '{self.nama}'.")
        return tugas_baru


# Kelas Tim menyimpan daftar developer yang tergabung di dalam tim
class Tim:
    def __init__(self, nama):
        # Inisialisasi nama tim
        self.nama = nama
        # Daftar developer dalam tim
        self.developer = []

    def tambah_developer(self, developer):
        # Menambahkan developer ke tim
        self.developer.append(developer)
        print(f"Developer '{developer.nama}' ditambahkan ke tim '{self.nama}'.")


# Kelas Developer merepresentasikan seorang programmer/developer
class Developer:
    def __init__(self, nama, keahlian):
        # Inisialisasi nama dan keahlian developer
        self.nama = nama
        self.keahlian = keahlian


# Kelas Tugas merepresentasikan tugas dalam proyek
class Tugas:
    def __init__(self, deskripsi):
        # Inisialisasi deskripsi tugas
        self.deskripsi = deskripsi
        # Developer yang ditugaskan (default: None)
        self.developer = None

    def tugaskan_ke(self, developer):
        # Mengaitkan tugas ini dengan developer tertentu
        self.developer = developer
        print(f"Tugas '{self.deskripsi}' telah ditugaskan ke {developer.nama} ({developer.keahlian}).")


# =======================================
# Bagian utama program (contoh penggunaan)
# =======================================
if __name__ == "__main__":
    # Membuat perusahaan baru
    perusahaan = Perusahaan("TechNova")

    # Membuat tim baru
    tim_backend = perusahaan.buat_tim("Backend Team")

    # Membuat developer
    dev1 = Developer("Aldi", "Backend Developer")
    dev2 = Developer("Sinta", "Database Engineer")

    # Menambahkan developer ke tim
    tim_backend.tambah_developer(dev1)
    tim_backend.tambah_developer(dev2)

    # Membuat proyek baru
    proyek1 = perusahaan.buat_proyek("Sistem Inventori", "Aplikasi untuk manajemen stok barang")

    # Menambahkan tugas ke proyek
    tugas1 = proyek1.tambah_tugas("Desain struktur database")
    tugas2 = proyek1.tambah_tugas("Implementasi API produk")

    # Menugaskan tugas ke developer
    tugas1.tugaskan_ke(dev2)
    tugas2.tugaskan_ke(dev1)
