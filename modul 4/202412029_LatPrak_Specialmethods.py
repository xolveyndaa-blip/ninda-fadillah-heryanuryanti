class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __eq__(self, other):
        return self.nilai == other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    def __len__(self):
        return len(self.nama)


# Membuat objek Mahasiswa
m1 = Mahasiswa("Pouster", 80)
m2 = Mahasiswa("Ahmad", 80)
m3 = Mahasiswa("Budi", 90)

# a) Representasi string
print(m1)
print(m2)
print(m3)

# b) Perbandingan kesetaraan nilai
print("m1 == m2 :", m1 == m2)
print("m1 == m3 :", m1 == m3)

# c) Operasi matematika
print("m1 + m2 =", m1 + m2)
print("m1 * 2 =", m1 * 2)

# Menggunakan __len__
print("Panjang nama m1:", len(m1))

# d) Mengurutkan tanpa __lt__
list_mahasiswa = [m1, m2, m3]
sorted_mahasiswa = sorted(list_mahasiswa, key=lambda x: x.nilai)

print("Hasil pengurutan berdasarkan nilai:")
for m in sorted_mahasiswa:
    print(m)
