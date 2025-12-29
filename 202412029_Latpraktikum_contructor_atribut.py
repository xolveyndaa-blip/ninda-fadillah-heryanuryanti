class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def info_dosen(self):
        return f"Dosen: {self.nama} | NIDN: {self.nidn}"


# Contoh pembuatan object
dsn1 = Dosen("ABD.RAHIM,,S.ST., M.M.", "23020753")
dsn2 = Dosen("FIKY ANGGARA, S.Kom, M,Kom.", "25080183")

print(dsn1.info_dosen("kewirausahaan"))
print(dsn2.info_dosen("matematika diskrit"))

