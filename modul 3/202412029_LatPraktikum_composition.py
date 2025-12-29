class Mesin:
    def __init__(self, jenis):
        self.jenis = jenis

    def hidupkan(self):
        return f"Mesin {self.jenis} hidup"


class Mobil:
    def __init__(self, merk, mesin):
        self.merk = merk
        self.mesin = mesin  # Composition

    def info(self):
        return f"Mobil {self.merk} dengan {self.mesin.hidupkan()}"


# Instansiasi
mesin = Mesin("Bensin")
mobil = Mobil("Honda", mesin)

print(mobil.info())


# a. Class Penulis
class Penulis:
    def __init__(self, nama):
        self.nama = nama


# b. Class Buku yang memiliki Penulis (composition)
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis  # Composition: Buku memiliki Penulis

    def info_buku(self):
        return f"'{self.judul}' ditulis oleh {self.penulis.nama}"


# c. Demonstrasi mengakses data penulis melalui objek buku
penulis1 = Penulis("Tere Liye")
buku1 = Buku("Bumi", penulis1)

print(buku1.info_buku())
