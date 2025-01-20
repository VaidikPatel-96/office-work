class Animal:
    def __init__(self,name):
        self.name=name

class Mammal(Animal):
    def has_fur(self):
        return True
    
class Pet:
    def __init__(self,owner):
        self.owner=owner

class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

dog=Dog("Buddy","Alice")
print(dog.name)
print(dog.owner)