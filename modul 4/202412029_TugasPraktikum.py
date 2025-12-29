from abc import ABC, abstractmethod


# =========================
# Custom Exception
# =========================
class PoinTidakValidError(Exception):
    """Kesalahan jika poin tidak valid (negatif)."""
    pass


# =========================
# Abstract Class
# =========================
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


# =========================
# Class Turunan
# =========================
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        return "Hak akses member: dapat mengakses fitur member."

    # Special Methods
    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)


# =========================
# Program Utama
# =========================
def input_poin():
    nilai = input("Masukkan poin member: ").strip()

    if nilai == "":
        raise ValueError("Input poin tidak boleh kosong.")

    poin = int(nilai)

    if poin < 0:
        raise PoinTidakValidError("Poin tidak boleh bernilai negatif.")

    return poin


if __name__ == "__main__":
    try:
        # Input poin dari user
        poin1 = input_poin()
        poin2 = input_poin()

        # Membuat objek Member
        m1 = Member("Andi", poin1)
        m2 = Member("Budi", poin2)

    except ValueError as ve:
        print("Kesalahan input:", ve)

    except PoinTidakValidError as pe:
        print("Kesalahan poin:", pe)

    else:
        # a. Info Member
        print(m1)
        print(m2)

        # Hak akses
        print(m1.akses())

        # b. Jumlah poin
        print("Jumlah poin:", m1 + m2)

        # c. Panjang nama
        print("Panjang nama member 1:", len(m1))

    finally:
        print("Program selesai dijalankan.")
