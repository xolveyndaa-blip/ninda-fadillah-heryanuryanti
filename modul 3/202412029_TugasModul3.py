# ==============================
# 1. Class Parent: Karyawan
# ==============================

class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        print(f"{self.nama} - Gaji Pokok: Rp{self.gaji_pokok:,}")


# ==============================
# 2. Child Class: Manager
# ==============================

class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    # Override method
    def info_gaji(self):
        gaji_total = self.gaji_pokok + self.tunjangan
        print(f"{self.nama} - Gaji Total (Gaji Pokok + Tunjangan): Rp{gaji_total:,}")


# ==============================
# 3. Child Class: Programmer
# ==============================

class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    # Override method
    def info_gaji(self):
        gaji_total = self.gaji_pokok + self.bonus
        print(f"{self.nama} - Gaji Total (Gaji Pokok + Bonus): Rp{gaji_total:,}")


# ==============================
# 4. Composition: Departemen
# ==============================

class Departemen:
    def __init__(self, nama_departemen):
        self.nama_departemen = nama_departemen
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"\nDepartemen: {self.nama_departemen}")
        print("-" * 40)
        for k in self.daftar_karyawan:
            k.info_gaji()
        print("-" * 40)


# ==============================
# 5. Instansiasi
# ==============================

# a. Buat 2 Manager
manager1 = Manager("Musya", 10000000, 3000000)
manager2 = Manager("Ninda", 12000000, 4000000)

# b. Buat 2 Programmer
programmer1 = Programmer("Yovita", 9000000, 2000000)
programmer2 = Programmer("Tika", 7000000, 2500000)

# Buat departemen
departemen_it = Departemen("IT")

# Masukkan semua karyawan
departemen_it.tambah_karyawan(manager1)
departemen_it.tambah_karyawan(manager2)
departemen_it.tambah_karyawan(programmer1)
departemen_it.tambah_karyawan(programmer2)


# ==============================
# 6. Tampilkan info gaji semua karyawan
# ==============================

departemen_it.tampilkan_karyawan()
