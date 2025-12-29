class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul          
        self.penulis = penulis      
        self.kode_buku = kode_buku 
        self._stok = stok           
        self.__lokasi_rak = lokasi_rak  

    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi):
        if lokasi == "":
            raise ValueError("Lokasi tidak boleh kosong")
        self.__lokasi_rak = lokasi

    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah
        else:
            raise ValueError("Stok tidak cukup!")

    def info_buku(self):
        return f"{self.judul} ({self.kode_buku}) - Stok: {self._stok}, Rak: {self.__lokasi_rak}"


class Peminjaman:
    def __init__(self, buku: Buku, tanggal_pinjam, tanggal_kembali=None, status="Dipinjam"):
        self.buku = buku                     
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return (
            f"Buku: {self.buku.judul} | Kode: {self.buku.kode_buku} | "
            f"Pinjam: {self.tanggal_pinjam} | Kembali: {self.tanggal_kembali} | Status: {self.status}"
        )


class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam, status_aktif=True):
        self.id_anggota = id_anggota      
        self.nama = nama                 
        self._maks_pinjam = maks_pinjam   
        self.__status_aktif = status_aktif  
        self.daftar_peminjaman = []      

    
    def get_status(self):
        return self.__status_aktif

    
    def set_status(self, status):
        self.__status_aktif = status

    def pinjam_buku(self, buku: Buku, tanggal_pinjam):
        if not self.__status_aktif:
            print(f"Anggota {self.nama} tidak aktif!")
            return

        if buku._stok <= 0:
            print(f"Stok habis untuk buku: {buku.judul}")
            return

        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print("Melebihi batas maksimal pinjam!")
            return

        buku.kurangi_stok(1)

        pem = Peminjaman(buku, tanggal_pinjam)
        self.daftar_peminjaman.append(pem)

    def kembalikan_buku(self, kode_buku, tanggal_kembali):
        for pem in self.daftar_peminjaman:
            if pem.buku.kode_buku == kode_buku and pem.status == "Dipinjam":
                pem.status = "Dikembalikan"
                pem.tanggal_kembali = tanggal_kembali
                pem.buku.tambah_stok(1)
                return
        print("Tidak ditemukan peminjaman buku tersebut.")


class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []  

    def tambah_buku(self, buku: Buku):
        self.daftar_buku.append(buku)

    def info_buku(self):
        for b in self.daftar_buku:
            print(b.info_buku())


if __name__ == "__main__":

    buku1 = Buku("Algoritma", "Darmawan", "B001", 3, "Rak A")
    buku2 = Buku("Python Dasar", "Suryo", "B002", 2, "Rak B")
    buku3 = Buku("Basis Data", "Hadi", "B003", 5, "Rak C")

    perpus = Perpustakaan("Perpus PBO")
    perpus.tambah_buku(buku1)
    perpus.tambah_buku(buku2)
    perpus.tambah_buku(buku3)

    a1 = Anggota("A01", "ninda", maks_pinjam=3)
    a2 = Anggota("A02", "tika", maks_pinjam=2)

    a1.pinjam_buku(buku1, "2024-12-01")
    a1.pinjam_buku(buku2, "2024-12-01")

    a2.pinjam_buku(buku3, "2024-12-02")

    a1.kembalikan_buku("B002", "2024-12-05")

    print("\n=== INFORMASI BUKU ===")
    perpus.info_buku()

    print("\n=== INFORMASI ANGGOTA ===")
    print(f"{a1.id_anggota} - {a1.nama} - Status: {a1.get_status()}")
    print(f"{a2.id_anggota} - {a2.nama} - Status: {a2.get_status()}")

    print("\n=== DAFTAR PEMINJAMAN ANGGOTA 1 ===")
    for p in a1.daftar_peminjaman:
        print("-", p.info_peminjaman())

    print("\n=== DAFTAR PEMINJAMAN ANGGOTA 2 ===")
    for p in a2.daftar_peminjaman:
        print("-", p.info_peminjaman())
