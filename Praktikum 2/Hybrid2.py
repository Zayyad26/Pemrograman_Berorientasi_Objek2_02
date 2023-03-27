
class University:
  def __init__(self):
    print("Pembuat kelas Dasar")
    self.univ = "Bina Sarana Informatika"
  def display(self):  
    print(f"Nama Universitasnya adalah : {self.univ}")

class Course(University):
  def __init__(self):
    print("Pembina Anak Kelas 1 Kelas Universitas")
    University.__init__(self)
    self.course = "Computer Education"
  def display(self): 
    print(f"Nama Kursusnya adalah : {self.course}")
    University.display(self)

class Branch(University):
  def __init__(self):
    print("Pembina Anak Kelas 2 Kelas Universitas")
    self.branch = "Data Science"
  def display(self): 
    print(f"Nama cabangnya adalah: {self.branch}")


class Student(Course, Branch):
  def __init__(self):
    print("Konstruktor kelas Anak dari Kursus dan Cabang dipanggil")
    self.name = "Tony"
    Branch.__init__(self)
    Course.__init__(self)
  def display(self):
    print(f"Nama Mahasiswa : {self.name}")
    Branch.display(self)
    Course.display(self)

ob = Student()  
print()
ob.display()    
