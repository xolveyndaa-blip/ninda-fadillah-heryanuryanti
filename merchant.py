class Pelanggan:
    def __init__(self, nama, email):
        # Inisialisasi pelanggan dengan nama, email, keranjang, dan riwayat pesanan
        self.nama = nama
        self.email = email
        self.keranjang = Keranjang()  # Komposisi: setiap pelanggan punya keranjang sendiri
        self.riwayat_pesanan = []

    def buat_pesanan(self):
        # Buat pesanan dari keranjang
        if not self.keranjang.daftar_item:
            print("❌ Keranjang masih kosong.")
            return None

        pesanan = Pesanan(self)
        self.riwayat_pesanan.append(pesanan)
        self.keranjang.kosongkan()
        print("✅ Pesanan berhasil dibuat!")
        return pesanan


class Produk:
    def __init__(self, nama, harga, stok):
        # Inisialisasi produk dengan nama, harga, dan stok
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"{self.nama} - Rp{self.harga} (Stok: {self.stok})"


class Keranjang:
    def __init__(self):
        # Inisialisasi keranjang kosong
        self.daftar_item = []

    def tambah_produk(self, produk, jumlah):
        # Tambahkan produk ke keranjang
        if produk.stok < jumlah:
            print(f"❌ Stok {produk.nama} tidak cukup.")
            return

        item = ItemPesanan(produk, jumlah)
        self.daftar_item.append(item)
        print(f"✅ {jumlah} x {produk.nama} ditambahkan ke keranjang.")

    def kosongkan(self):
        self.daftar_item = []

    def __str__(self):
        if not self.daftar_item:
            return "Keranjang kosong."
        return "\n".join(str(item) for item in self.daftar_item)


class Pesanan:
    def __init__(self, pelanggan):
        # Inisialisasi pesanan dari pelanggan
        self.pelanggan = pelanggan
        self.item_pesanan = pelanggan.keranjang.daftar_item.copy()
        self.total = sum(item.total_harga() for item in self.item_pesanan)

        # Kurangi stok produk
        for item in self.item_pesanan:
            item.produk.stok -= item.jumlah

    def __str__(self):
        detail = "\n".join(str(item) for item in self.item_pesanan)
        return f"Pesanan oleh {self.pelanggan.nama}:\n{detail}\nTotal: Rp{self.total}"


class ItemPesanan:
    def __init__(self, produk, jumlah):
        # Inisialisasi item pesanan
        self.produk = produk
        self.jumlah = jumlah

    def total_harga(self):
        return self.produk.harga * self.jumlah

    def __str__(self):
        return f"{self.jumlah} x {self.produk.nama} = Rp{self.total_harga()}"
# ===================== TESTING =====================
if __name__ == "__main__":
    # 1. Membuat beberapa produk
    produk1 = Produk("Keyboard", 250000, 10)
    produk2 = Produk("Monitor", 1200000, 5)
    produk3 = Produk("Mouse", 150000, 8)

    # 2. Membuat pelanggan
    pelanggan1 = Pelanggan("Dina", "dina@student.ac.id")

    # 3. Menambahkan produk ke keranjang pelanggan
    pelanggan1.keranjang.tambah_produk(produk1, 1)
    pelanggan1.keranjang.tambah_produk(produk2, 2)

    # 4. Membuat pesanan dari keranjang
    pesanan = pelanggan1.buat_pesanan()

    # 5. Menampilkan detail pesanan dan total harga
    if pesanan:
        print("\n=== Detail Pesanan ===")
        print(pesanan)

    # Menampilkan stok produk terkini
    print("\n=== Stok Produk Sekarang ===")
    print(produk1)
    print(produk2)
    print(produk3)
