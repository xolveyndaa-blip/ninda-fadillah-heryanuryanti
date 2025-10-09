class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []
        self.tanggal_pinjam = tanggal_pinjam 
        # Implementasi: tambahkan atribut untuk koleksi
buku dan daftar anggota
    def tambah_buku(self, buku):
        # Implementasi: tambahkan buku ke koleksi
        pass
    def daftar_anggota(self, anggota):
        # Implementasi: tambahkan anggota ke daftar
        pass
    def pinjam_buku(self, anggota, buku):
        # Implementasi: proses peminjaman buku oleh anggota
        pass
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul 
        self.penulis = penulis
        self.status = "tersedia"

    def __init__(self):
        return f"s{elf.judul} oleh {self penulis} (Status: {self.status})"
        # Implementasi: inisialisasi atribut buku
        pass
class Anggota:
    def __init__(self, nama):
        self.nama = nama 

    def __str__(self):
        return f"Anggota: {self.nama}"
        # Implementasi: inisialisasi atribut anggota
        pass
class Peminjaman:
    def __init__(self, anggota, buku, tanggal_pinjam):
        self.anggota = anggota 
        self.buku = buku 
        self.tanggal_pinjam = tanggal_pinjam

    def __str__(self):
        return f"{self.anggota.nama} meminjam '{self.buku.judul}' pada {self.tanggal_pinjam}"
        # Implementasi: inisialisasi transaksi peminjaman
        pass