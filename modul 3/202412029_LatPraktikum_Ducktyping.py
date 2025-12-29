class Burung:
    def terbang(self):
        return "Burung terbang tinggi"


class Pesawat:
    def terbang(self):
        return "Pesawat lepas landas"


def uji_terbang(obj):
    print(obj.terbang())


# Duck typing dalam aksi
b = Burung()
p = Pesawat()

uji_terbang(b)
uji_terbang(p)


class Laptop:
    def nyalakan(self):
        return "Laptop menyala dengan sistem operasi booting..."


class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala, logo muncul di layar..."


def tes_nyala(obj):
    print(obj.nyalakan())


# Duck typing dalam aksi untuk Laptop & Smartphone
l = Laptop()
s = Smartphone()

tes_nyala(l)
tes_nyala(s)
