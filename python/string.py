## string methods ##

#capitalize = converts the first character to upper case
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)  #output: Hello, and welcome to my world.


# casefold = converts string into lover case
txt = "Hello, And Welcome To My World!"
x=txt.casefold()
print(x)  #Output: hello, and welcome to my world!


#center = Returns a centerd string
txt= "vadik"
x= txt.center(35)
print(x)  #Output:                vadik


#count  - returns the number of times a specified value occurs in a string
txt = "I love apple, apple are my favorite fruit"
x=txt.count("apple")
print(x)  #Output : 2


#endswith - returns true  if the string ends with the specified value
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)  #Output: True


# find - searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."

x = txt.find("e")

print(x)  #Output: 1


#index - searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x) #output: 7


#Join - converts the elements of an iteravle into a string

x=("vaidik","vivek","preet")
y="#".join(x)
print(y)  #Output:vaidik#vivek#preet


#lower - converts a string into lover case
txt= "HELLO VAIDIK"
x=txt.lower()
print(x)  #Output: hello vaidik

#replace - returns a string where a specified value is replaced with a specified value
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)  #output: I like apples


# split  - splits the string at the specified separator and returns a list
txt = "welcome to the jungle"

x = txt.split()

print(x)  #Output: ['welcome', 'to', 'the', 'jungle']

#########################################################
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)  #Output:['apple', 'banana', 'cherry', 'orange']
