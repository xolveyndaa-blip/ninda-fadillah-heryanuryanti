class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.nama} ({self.email})"


# b. Dictionary untuk menyimpan objek pelanggan
data_pelanggan = {}


# c. Fungsi menambah pelanggan
def tambah_pelanggan(id_pelanggan, nama, email):
    data_pelanggan[id_pelanggan] = Pelanggan(id_pelanggan, nama, email)


# Fungsi menghapus pelanggan
def hapus_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("Pelanggan tidak ditemukan.")


# Fungsi mencari pelanggan
def cari_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        return data_pelanggan[id_pelanggan]
    else:
        return None


# Menambahkan data pelanggan
tambah_pelanggan("PL001", "Andi", "andi@email.com")
tambah_pelanggan("PL002", "Budi", "budi@email.com")
tambah_pelanggan("PL003", "Citra", "citra@email.com")


# d. Menampilkan seluruh daftar pelanggan
print("=== Daftar Pelanggan ===")
for id_pel, pelanggan in data_pelanggan.items():
    print(f"{id_pel}: {pelanggan.info()}")


# Contoh pencarian pelanggan
id_cari = "PL002"
hasil = cari_pelanggan(id_cari)

if hasil:
    print(f"\nPelanggan ditemukan: {hasil.info()}")
else:
    print("\nPelanggan tidak ditemukan.")
