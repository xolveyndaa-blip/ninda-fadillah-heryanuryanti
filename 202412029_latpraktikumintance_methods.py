class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah > 0:
            if nama_barang in self.inventori:
                self.inventori[nama_barang] += jumlah
            else:
                self.inventori[nama_barang] = jumlah
            return f"{jumlah} {nama_barang} berhasil ditambahkan."
        return "Jumlah harus lebih dari 0."

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang not in self.inventori:
            return f"{nama_barang} tidak ada dalam inventori."

        if 0 < jumlah <= self.inventori[nama_barang]:
            self.inventori[nama_barang] -= jumlah
            if self.inventori[nama_barang] == 0:
                del self.inventori[nama_barang]
            return f"{jumlah} {nama_barang} berhasil dikurangi."
        
        return "Jumlah tidak valid atau melebihi stok."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."
        return f"Daftar inventori: {self.inventori}"


# Demonstrasi
manajer = ManajerInventori()

print(manajer.tambah_barang("Laptop", 10))
print(manajer.tambah_barang("Mouse", 25))
print(manajer.tambah_barang("Laptop", 5))

print(manajer.lihat_inventori())

print(manajer.hapus_barang("Mouse", 10))
print(manajer.hapus_barang("Laptop", 15))

print(manajer.lihat_inventori())
