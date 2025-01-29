
# #string methods

#s="hello vaidik"

# print(s.upper())
# print(s.lower())
#print(s.title())
# print(s.capitalize())
# print(s.swapcase())
# print(s.replace("hello","hi"))
# print(s.find("vaidik"))
# print(s.count("l"))
# print(s.split(" "))
# print(s.splitlines())
# print(s.startswith("hello"))
# print(s.endswith("vaidik"))
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.islower())
# print(s.isupper())
# print(s.isspace())
# print(s.istitle())
# print(s.isprintable())
# print(s.isidentifier())
# print(s.isdecimal())
# print(s.isnumeric())
# print(s.isascii())
# print(s.isidentifier())
# print(s.isprintable())

# #list methods
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst.append(11))
print(lst)

lst.insert(2,12)
print(lst)

lst.remove(12)
print(lst)

lst.pop(2)
print(lst)

lst.clear()
print(lst)

lst=[1,2,3,4,5,6,8,9,10,5]
#print(lst.index(5))
print(lst)
#print(lst.count(5))

lst.sort()
print(lst)

lst.reverse()  
print(lst)

lst1=lst.copy()
print(lst1)

lst.extend([11,12,13,14,15])
print(lst)

# #tuple methods

tup=(1,2,3,4,5,6,7,8,9,10)
print(tup.count(5))

print(tup.index(5))


# #set methods


st={1,2,3,4,5,6,7,8,9,10}

st.add(11)
print(st)

st.update([12,13,14,15])
print(st)

st.remove(15)
print(st)

st.discard(14)
print(st)

st.pop()
print(st)

st.clear()
print(st)

st1={1,2,3,4,5,6,7,8,9,10}

st2={1,2,13,14,15}

print(st1.union(st2))

print(st1.intersection(st2))

print(st1.difference(st2))

print(st1.symmetric_difference(st2))

print(st1.issubset(st2))

print(st1.issuperset(st2))

print(st1.isdisjoint(st2))

print(len(st1))

print(st1.copy())


# #dictionary methods   

dict1={"name":"vaidik","age":20,"city":"surat","country":"india"}

print(dict1.get("name"))

print(dict1.items())

print(dict1.keys())

print(dict1.values())

print(dict1.pop("name"))

print(dict1)

print(dict1.popitem())

print(dict1)

dict1={"name":"vaidik","age":20,"city":"surat","country":"india"}

dict2={"name":"vaidik","age":20,"city":"surat","country":"india"}

print(dict1==dict2)

print(dict1.copy())

dict1.clear()

print(dict1)

dict1={"name":"vaidik","age":20,"city":"surat","country":"india"}

dict2={"name":"jay","age":25,"city":"surat","country":"india"}

dict1.update(dict2)
print(dict1)


del dict1["name"]
print(dict1)

dict1={"name":"vaidik","age":20,"city":"surat","country":"india"}


print(dict1.setdefault("name"))


# #string formatting

name="vaidik"

age=20

city="surat"

country="india"

print("my name is {} and my age is {} and i live in {} and my country is {}".format(name,age,city,country))

print(f"my name is {name} and my age is {age} and i live in {city} and my country is {country}")

print("my name is {0} and my age is {1} and i live in {2} and my country is {3}".format(name,age,city,country))

print("my name is {name} and my age is {age} and i live in {city} and my country is {country}".format(name=name,age=age,city=city,country=country))


# #list comprehension

lst=[i for i in range(1,11)]
print(lst)

lst=[i for i in range(1,11) if i%2==0]
print(lst)

lst=[i if i%2==0 else "odd" for i in range(1,11)]
print(lst)

lst=[i for i in range(1,11)]
print(lst)


# #dictionary comprehension

dict1={i:i**2 for i in range(1,11)}
print(dict1)

dict1={i:i**2 for i in range(1,11) if i%2==0}
print(dict1)


# #set comprehension

st={i for i in range(1,11)}
print(st)

st={i for i in range(1,11) if i%2==0}
print(st)


# #generator comprehension

gen=(i for i in range(1,11))
print(gen)

for i in gen:
    print(i)

gen=(i for i in range(1,11) if i%2==0)
print(gen)



# #map function

def square(n):
    return n**2

lst=[1,2,3,4,5,6,7,8,9,10]

result=map(square,lst)
print(list(result))

result=map(lambda n:n**2,lst)
print(list(result))


# #filter function

def even(n):
    return n%2==0

lst=[1,2,3,4,5,6,7,8,9,10]

result=filter(even,lst)

print(list(result))

result=filter(lambda n:n%2==0,lst)

print(list(result))


# #reduce function

from functools import reduce

def add(a,b):
    return a+b

lst=[1,2,3,4,5,6,7,8,9,10]

result=reduce(add,lst)
print(result)

result=reduce(lambda a,b:a+b,lst)
print(result)


# #decorators

def decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper

@decorator
def hello():
    print("hello world")

@decorator
def hello1():
    print("hello1")    

hello()
hello1()


# #decorators with arguments

def decorator(func):
    def wrapper(*args,**kwargs):
        print("before function")
        func(*args,**kwargs)
        print("after function")
    return wrapper

@decorator
def hello(name):
    print(f"hello {name}")

hello("vaidik")



# #decorators with arguments

def decorator(func):
    def wrapper(*args,**kwargs):
        print("before function")
        func(*args,**kwargs)
        print("after function")
    return wrapper

@decorator
def hello(name,age):
    print(f"hello {name} and your age is {age}")

hello("vaidik",20)


# #decorators with arguments

def decorator(func):
    def wrapper(*args,**kwargs):
        print("before function")
        func(*args,**kwargs)
        print("after function")
    return wrapper

@decorator
def hello(name,age,city):
    print(f"hello {name} and your age is {age} and you live in {city}")

hello("vaidik",20,"surat")


# #staticmethod

class Person:
    @staticmethod
    def hello():
        print("hello world")

Person.hello()


# #classmethod

class Person:
    @classmethod
    def hello(cls):
        print(f"hello {cls.__name__}")

Person.hello()


# #constructor

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def hello(self):
        print(f"hello {self.name} and your age is {self.age}")

p1=Person("vaidik",20)
p1.hello()


# #inheritance

class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return "I make sounds"
    
class Mammal(Animal):
    def has_fur(self):
        return True
    
class Dog(Mammal):
    def speak(self):
        return "Woof!"
    
dog=Dog("Buddy")
print(dog.name)
print(dog.has_fur())
print(dog.speak())


# #multiple inheritance

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


# #multilevel inheritance

class Animal:
    def __init__(self,name):
        self.name=name

class Mammal(Animal):
    def has_fur(self):
        return True
    
class Dog(Mammal):
    def speak(self):
        return "Woof!"
    
dog=Dog("Buddy")

print(dog.name)
print(dog.has_fur())
print(dog.speak())


# # method overriding
class Parent:
    def greet(self):
        return "Hello from the Parent class!"

class Child(Parent):
    def greet(self):
        return "Hello from the Child class!"

# Creating instances
parent = Parent()
child = Child()

# Method calls
print(parent.greet())  # Output: Hello from the Parent class!
print(child.greet())   # Output: Hello from the Child class!


# #method overloading

class Parent:
    def greet(self, name=None):
        if name is not None:
            return f"Hello, {name}!"
        return "Hello!"
    
# Creating instances
parent = Parent()

# Method calls
print(parent.greet())  # Output: Hello!
print(parent.greet("Vaidik"))  # Output: Hello, Vaidik!


# #encapsulation

class Person:
    def __init__(self):
        self.name = "Vaidik"
        self.age = 20

    def display(self):
        return self.name, self.age
    
p1 = Person()
print(p1.name)
print(p1.display())
print(p1.age)


# #polymorphism

class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
def get_pet_sound(pet):
    return pet.speak()

dog = Dog()
cat = Cat()

print(get_pet_sound(dog))  # Output: Woof!
print(get_pet_sound(cat))  # Output: Meow!


# #abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!


# #exception handling

try:
    print(x)
except:
    print("An exception occurred")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


# #user defined exception

class MyError(Exception):
    def __init__(self,message):
        self.message=message

num=10

try:
    if num<20:
        raise MyError("Number is less than 20")
except MyError as e:

    print(e.message)


# #2.) Write a Python program to check if a number is a palindrome. sort method

def is_palindrome(num):
    return num==num[::-1]

print(is_palindrome(input("Enter the number: ")))





## __init__ method

class person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

person1=person("vaidik",20)
print(person1.name)
print(person1.age)


## self parameter

class person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("hello my name is "+self.name)

person1=person("vaidik",20)
person1.myfunc()


## modify object properties

class person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("hello my name is "+self.name)

person1=person("vaidik",20)
person1.age=21
person1.myfunc()























