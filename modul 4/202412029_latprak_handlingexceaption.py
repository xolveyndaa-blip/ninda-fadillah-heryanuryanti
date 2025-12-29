def operasi():
    print("=== Operasi Matematika Aman ===")
    print("Pilih operasi:")
    print("1. Pembagian")
    print("2. Perkalian")

    pilihan = input("Masukkan pilihan (1/2): ").strip()
    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()

    try:
        # b. Pesan khusus jika input kosong
        if x == "" or y == "":
            raise ValueError("Input tidak boleh kosong. Silakan masukkan angka.")

        a = float(x)
        b = float(y)

        # c. Validasi angka positif
        if a < 0 or b < 0:
            raise ValueError("Angka harus bernilai positif.")

        if pilihan == "1":
            hasil = a / b   # bisa memicu ZeroDivisionError
        elif pilihan == "2":
            hasil = a * b
        else:
            raise ValueError("Pilihan operasi tidak valid. Gunakan 1 atau 2.")

    except ValueError as ve:
        print("Input salah:", ve)

    except ZeroDivisionError:
        print("Penyebut tidak boleh nol pada operasi pembagian!")

    except Exception as e:
        print("Terjadi kesalahan:", e)

    # d. Else hanya jalan jika tidak ada exception
    else:
        print(f"Hasil operasi: {hasil}")

    # e. Finally selalu dijalankan
    finally:
        print("Selesai memproses input.")


if __name__ == "__main__":
    operasi()
