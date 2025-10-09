# Parent class: Karyawan
class Karyawan:  
    # Membuat class induk bernama Karyawan
    def __init__(self, nama, id_karyawan, gaji_pokok):
        # Fungsi __init__ adalah konstruktor yang otomatis dijalankan saat objek dibuat
        # Inisialisasi atribut dasar karyawan: nama, id_karyawan, dan gaji_pokok
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        # Method dasar untuk menghitung gaji
        # Di class induk, gaji hanya berdasarkan gaji pokok
        return self.gaji_pokok

    def info(self):
        # Method untuk menampilkan informasi lengkap karyawan
        # f-string digunakan agar bisa menampilkan variabel langsung di dalam teks
        return f"Karyawan : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji():,.1f}"


# Child class: Manager (turunan dari Karyawan)
class Manager(Karyawan):
    # Membuat class Manager yang mewarisi class Karyawan
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        # super() digunakan untuk memanggil konstruktor dari class induk (Karyawan)
        super().__init__(nama, id_karyawan, gaji_pokok)
        # Menambahkan atribut baru khusus untuk Manager, yaitu tunjangan
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        # Override method dari class Karyawan
        # Pada Manager, gaji adalah gaji pokok ditambah tunjangan
        return self.gaji_pokok + self.tunjangan

    def info(self):
        # Override method info untuk menampilkan informasi Manager
        return f"Manager : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji():,.1f}"


# Child class: Programmer (turunan dari Karyawan)
class Programmer(Karyawan):
    # Membuat class Programmer yang juga mewarisi class Karyawan
    def __init__(self, nama, id_karyawan, gaji_pokok, bonus):
        # super() memanggil konstruktor dari class Karyawan
        super().__init__(nama, id_karyawan, gaji_pokok)
        # Menambahkan atribut baru khusus Programmer, yaitu bonus
        self.bonus = bonus

    def hitung_gaji(self):
        # Override method dari class Karyawan
        # Pada Programmer, gaji adalah gaji pokok ditambah bonus
        return self.gaji_pokok + self.bonus

    def info(self):
        # Override method info untuk menampilkan informasi Programmer
        return f"Programmer : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji():,.1f}"


# ==== Bagian utama program ====
if __name__ == "__main__":
    # Baris ini memastikan kode di bawah hanya dijalankan jika file ini dijalankan langsung
    # bukan saat diimpor sebagai modul di file lain

    # Membuat objek dari class Manager dan Programmer
    manager1 = Manager("Ninda", "M002", 12_000_000, 3_000_000)   # Membuat objek Manager dengan nama, ID, gaji, dan tunjangan
    programmer1 = Programmer("Fadillah", "P001", 10_000_000, 2_000_000)  # Membuat objek Programmer dengan nama, ID, gaji, dan bonus

    # Polymorphism: menyimpan objek Manager dan Programmer dalam satu list
    daftar_karyawan = [manager1, programmer1]

    # Menggunakan perulangan untuk menampilkan informasi semua karyawan
    # Meskipun kedua objek berbeda class, mereka bisa menggunakan method info() yang sama
    for karyawan in daftar_karyawan:
        print(karyawan.info())  # Menampilkan hasil info sesuai class masing-masing
