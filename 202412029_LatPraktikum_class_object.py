class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    # Method untuk menampilkan info kendaraan
    def info(self):
        return f"{self.merk} | Warna: {self.warna} | Tahun: {self.tahun}"


# Membuat object (instance)
kend1 = Kendaraan("Toyota Avanza", "Hitam", 2020)
kend2 = Kendaraan("Honda Beat", "Merah", 2022)

# Akses instance attribute
print("=== Instance Attribute ===")
print(kend1.info())
print(kend2.info())

# Akses class attribute
print("\n=== Class Attribute ===")
print(f"Bahan Bakar (akses via class): {Kendaraan.bahan_bakar}")
print(f"Bahan Bakar (akses via object): {kend1.bahan_bakar}")
