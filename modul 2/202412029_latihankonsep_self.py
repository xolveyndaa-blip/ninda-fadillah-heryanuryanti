class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


# Membuat beberapa mata kuliah
mk1 = MataKuliah("TI101", "Pemrograman Dasar")
mk2 = MataKuliah("TI102", "Struktur Data")
mk3 = MataKuliah("TI103", "Basis Data")

# Membuat beberapa mahasiswa
m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Andi")

# Menambahkan mahasiswa ke masing-masing mata kuliah
mk1.tambah_mahasiswa(m1)
mk1.tambah_mahasiswa(m2)

mk2.tambah_mahasiswa(m2)
mk2.tambah_mahasiswa(m3)

mk3.tambah_mahasiswa(m1)
mk3.tambah_mahasiswa(m3)

# Menampilkan hasil
print("=== DATA MATA KULIAH ===")
for mk in [mk1, mk2, mk3]:
    print(f"\nMata Kuliah : {mk.nama} ({mk.kode})")
    print("Daftar Mahasiswa :", mk.daftar_mahasiswa())
    print("Jumlah Mahasiswa :", mk.jumlah_mahasiswa())
