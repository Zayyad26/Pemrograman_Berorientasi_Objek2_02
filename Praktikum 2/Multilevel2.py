class Family:
    def show_family(self):
        print("Inilah keluarga kami:")
 

class Father(Family):
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
 
class Mother(Family):
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
 
class Son(Father, Mother):
    def show_parent(self):
        print("Ayah :", self.fathername)
        print("Ibu :", self.mothername)
 
 
s1 = Son()  # Object of Son class
s1.fathername = "Soleh"
s1.mothername = "Rusmiati"
s1.show_family()
s1.show_parent()
