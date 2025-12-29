# Custom Exception
class UmurTidakValidError(Exception):
    """Kesalahan umum untuk umur tidak valid."""
    pass


class UmurTerlaluMudaError(Exception):
    """Kesalahan jika umur terlalu muda."""
    pass


class UmurTerlaluTuaError(Exception):
    """Kesalahan jika umur terlalu tua."""
    pass


class AkunTidakDiizinkanError(Exception):
    """Kesalahan jika umur tidak memenuhi syarat pembuatan akun."""
    pass


def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda (minimal 5 tahun).")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua (maksimal 100 tahun).")
    return umur


def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Akun tidak diizinkan untuk umur di bawah 18 tahun.")
    return "Akun berhasil dibuat."


if __name__ == "__main__":
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)

            # jika umur valid, lanjut daftar akun
            pesan = daftar_akun(umur)

        except ValueError:
            print("Input harus berupa bilangan bulat!")

        except UmurTerlaluMudaError as e:
            print(e)

        except UmurTerlaluTuaError as e:
            print(e)

        except UmurTidakValidError as e:
            print(e)

        except AkunTidakDiizinkanError as e:
            print(e)
            break

        else:
            print("Umur valid:", umur)
            print(pesan)
            break

        finally:
            print("Proses input selesai.\n")

