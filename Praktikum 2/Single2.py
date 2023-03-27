class Pakaian:
  def __init__(self, jenis, merk, warna):
    self.jenis = jenis
    self.merk = merk
    self.warna = warna
  def berpakaian(self):
    print("Pakaian ini sedang dipakai.")

class Kemeja(Pakaian):
  def __init__(self, jenis, merk, warna, cc):
    super().__init__(jenis, merk, warna)
    self.cc = cc
  def dicuci(self):
    print("Pakaian ini sedang dicuci.")

bajuA = Kemeja("Sepeda Motor", "Honda", "Merah", 150)
bajuA.berpakaian()
bajuA.dicuci() 
