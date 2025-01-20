# # Parent class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "I make sounds"

# # Child class inheriting from Animal
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# # Creating an object of Dog
# dog = Dog(input("Enter the name of the dog: "))
# print(dog.name)   # Output: Buddy
# print(dog.speak())  # Output: Woof!

# Parent class 1
# class Animal:
#     def __init__(self, name):
#         self.name = name

# # Parent class 2
# class Pet:
#     def __init__(self, owner):
#         self.owner = owner

# # Child class inheriting from both Animal and Pet
# class Dog(Animal, Pet):
#     def __init__(self, name, owner):
#         Animal.__init__(self, name)
#         Pet.__init__(self, owner)

# dog = Dog("Buddy", "Alice")
# print(dog.name)  # Output: Buddy
# print(dog.owner)  # Output: Alice
# Grandparent class
class Animal:
    def __init__(self, name):
        self.name = name

# Parent class
class Mammal(Animal):
    def has_fur(self):
        return True

# Child class
class Dog(Mammal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.name)    # Output: Buddy
print(dog.has_fur()) # Output: True
print(dog.speak()) # Output: Woof!



