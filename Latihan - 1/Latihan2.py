class Hobi :
    def __init__(self,nama,kegiatan):
        self.nama = nama
        self.kegiatan = kegiatan
        
    def info(self): 
        print(f"Nama : {self.nama}\nKegiatan :{self.kegiatan}")
        
kegiatan1 = Hobi ("Zayyad","Tenis Meja")
kegiatan1.info()
