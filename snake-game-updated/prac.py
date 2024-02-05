class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")
        

class Fish(Animal):
    def __init__(self):
        super().__init__() ## this line is recommended but not strictly required when inheriting super class
        
    def breathe(self):
        super().breathe()
        print("doing this underwater.")
    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()

print(nemo.num_eyes)

class Dog:
    def __init__(self):
        self.temperament = "loyal"
     
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"
        
doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")