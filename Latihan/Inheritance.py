class BangunDatar:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luasArea(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        super().__init__(sisi)

    def luasArea(self):
        return self.sisi * self.sisi
    
    def Nilaikeliling(self):
        return 4 * self.sisi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        super().__init__(jari_jari)

    def luasArea(self):
        return 3.14 * self.sisi * self.sisi

    def Nilaikeliling(self):
        return 2 * 3.14 * self.sisi

persegi = Persegi(24)
lingkaran = Lingkaran(14)

print("====================================")
print("|MENGHITUNG LUAS  DAN KELILING|\n") 
print("====================================")
print("Luas persegi:", persegi.luasArea())
print("====================================")
print("Keliling persegi:", persegi.Nilaikeliling())
print("====================================")
print("Luas lingkaran:", lingkaran.luasArea())
print("====================================")
print("Keliling lingkaran:", lingkaran.Nilaikeliling())
print("====================================")
print("\n|  Zayyad    |") 
print("|    210510002 |") 
print("|    D3 TIF    |") 
print("====================================")
