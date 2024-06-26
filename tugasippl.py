import math

class Bentuk:
    def __init__(self, nama):
        self.nama = nama

    def hitung_luas(self):
        pass

class Segitiga(Bentuk):
    def __init__(self, nama, alas, tinggi):
        super().__init__(nama)
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

class Lingkaran(Bentuk):
    def __init__(self, nama, radius):
        super().__init__(nama)
        self.radius = radius

    def hitung_luas(self):
        return math.pi * self.radius ** 2

class Persegi(Bentuk):
    def __init__(self, nama, sisi):
        super().__init__(nama)
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2
    
class PersegiPanjang(Bentuk):
    def __init__(self, nama, panjang, lebar):
        super().__init__(nama)
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

class Trapesium(Bentuk):
    def __init__(self, nama, alas1, alas2, tinggi):
        super().__init__(nama)
        self.alas1 = alas1
        self.alas2 = alas2
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * (self.alas1 + self.alas2) * self.tinggi

def main():
    print("\n")
    segitiga1 = Segitiga("Segitiga ABC", 5, 8)
    lingkaran1 = Lingkaran("Lingkaran O", 4)
    persegi1 = Persegi("Persegi PQR", 6)
    persegi_panjang1 = PersegiPanjang("Persegi Panjang XYZ", 7, 9)
    trapesium1 = Trapesium("Trapesium MNO", 4, 6, 5)

    print("Luas", segitiga1.nama, ":", segitiga1.hitung_luas())
    print("Luas", lingkaran1.nama, ":", lingkaran1.hitung_luas())
    print("Luas", persegi1.nama, ":", persegi1.hitung_luas())
    print("Luas", persegi_panjang1.nama, ":", persegi_panjang1.hitung_luas())
    print("Luas", trapesium1.nama, ":", trapesium1.hitung_luas())
    print("\n")

if __name__ == "__main__":
    main()