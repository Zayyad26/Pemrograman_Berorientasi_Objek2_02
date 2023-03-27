class Binatang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def bergerak(self):
        print(self.nama, "Berlari")

class Kuda(Binatang):
    def __init__(self, nama, umur, jenis_kuda):
        super().__init__(nama, umur)
        self.jenis_kuda = jenis_kuda
    
    def bersuara(self):
        print(f"{self.nama} Yang Berumur {self.umur} Tahun Dengan Jenis {self.jenis_kuda} Berlari dengan cepat")

kudaA = Kuda("Flawless", 3, "Morgan")
kudaA.bergerak()
kudaA.bersuara()
