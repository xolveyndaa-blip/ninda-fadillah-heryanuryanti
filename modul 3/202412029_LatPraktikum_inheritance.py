class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Kendaraan: {self.merk} ({self.tahun})"


class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_pintu):
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        return f"Mobil: {self.merk}, {self.jumlah_pintu} pintu ({self.tahun})"


# Instansiasi Kendaraan & Mobil
k = Kendaraan("Yamaha", 2020)
m = Mobil("Toyota", 2022, 4)

print(k.info())
print(m.info())


class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}"


class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)   # memanggil konstruktor parent class
        self.nim = nim

    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur}, NIM: {self.nim}"


# Instansiasi Person & Mahasiswa
p = Person("Andi", 30)
mhs = Mahasiswa("Budi", 20, "123456789")

print(p.info())
print(mhs.info())
