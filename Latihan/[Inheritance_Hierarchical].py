class Animal:
    def _init_(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    
class Mammal(Animal):
    def _init_(self, name, color, fur):
        super()._init_(name, color)
        self.fur = fur
    def get_fur(self):
        return self.fur
    
class Cat(Animal):
    def _init_(self, name, color):
        super()._init_(name)
        self.color = color
    def get_color(self):
        return self.color
    
# Hierarchical Inheritance
class Reptile(Mammal):
    def _init_(self, name, color, age):
        super()._init_(name, color, age)
        self.age = age
    def get_details(self):
        print(f"Name : {self.name}")
        print(f"Color : {self.color}")
        print(f"Age : {self.age}")
        return self.age
    
animalA = Reptile("Dog", "White", 4)
animalA.get_details()
