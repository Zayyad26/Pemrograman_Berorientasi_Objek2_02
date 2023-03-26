class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def bergerak(self):
        print(self.nama, "Berjalan")

class Kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    
    def bersuara(self):
        print(f"{self.nama} Yang Berumur {self.umur} Tahun Dengan Jenis {self.jenis_bulu} Bersuara Meow")

kucingA = Kucing("Komeng", 3, "British Short Hair")
kucingA.bergerak()
kucingA.bersuara()
