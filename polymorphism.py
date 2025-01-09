class Animal:
    def move(self):
        pass #This will be overridden

class Dog(Animal):
    def move(self):
        return "Running 🐕"
    
class Bird(Animal):
    def move(self):
        return "Flying 🐦"
    
class Fish(Animal):
    def move(self):
         return "Swimming 🐟"
    
#Test
animals=[Dog(),Bird(),Fish()]

for animal in animals:
    print(animal.move())