class Mahasiswa:
    universitas = "STITIEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        return (
            f"Perkenalkan, saya {self.nama} (NIM: {self.nim}) "
            f"dari jurusan {self.jurusan} - {Mahasiswa.universitas}."
        )

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}"

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


mhs1 = Mahasiswa("ninda", "20231001", "Informatika", 3.6)
mhs2 = Mahasiswa("tika", "20231002", "Sistem Informasi", 3.1)
mhs3 = Mahasiswa("Musya", "20231003", "Teknik Komputer", 2.4)


print(mhs1.perkenalan_diri())
print("Predikat:", mhs1.predikat_kelulusan())
print(mhs1.update_ipk(3.7))
print("Predikat baru:", mhs1.predikat_kelulusan())
print()

print(mhs2.perkenalan_diri())
print("Predikat:", mhs2.predikat_kelulusan())
print()

print(mhs3.perkenalan_diri())
print("Predikat:", mhs3.predikat_kelulusan())
print(mhs3.update_ipk(2.6))
print("Predikat baru:", mhs3.predikat_kelulusan())
