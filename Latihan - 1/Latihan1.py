class Pakaian : 
    
    def __init__(self,kategori,warna):
        self.kategori = kategori
        self.warna = warna 
        
    def info(self):
        print(f"Kemeja {self.kategori} berwarna {self.warna}")
        
pakaian1 = Pakaian("Kemeja","Hitam")
pakaian1.info() 
