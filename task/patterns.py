#Q1
for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()    

# output = 
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *

#Q2
r = 5
for i in range(1,r+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

# # output =
# * 
# * *
# * * *
# * * * *
# * * * * *

#Q3

n = 5
for i in range(n, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()

# output =
# * * * * * 
# * * * *
# * * *
# * *
# *


# Q4    

n= 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# output =
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Q5

n= 6

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

# output =
# 6 5 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1    

# Q6

for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end=" ")
    for k in range(1,(2*i-1)+1):
        print("*", end=" ")    
    print("\n")

# x=-1

# if x > 0:
#      print("Positive number")
# else:
#      print("Negative number")  

for i in range(5):
    print(i)


for i in range(10):
    if i == 9:
        break
    print(i)


for i in range(5):
    if i ==3:
         continue
    print(i)

def greet(name):
    print("Hello, " + name)
greet("John")

def get_coordinates():
    return(10,20)
x,y = get_coordinates()

print(x)

print(y)

result="hello"+ " " + "world"
print(result)

text="hello"
print(text[0])


reversed_text="python"[::-1]
print(reversed_text)


my=[1,2,3]
my.append(10)
print(my)

my1=[1,2,3]
my1.remove(1)
print(my1)


my2=[1,2,3,4,5]
my21=my2[1:5]
print(my21)

list1=[1,2,3]

for item in list1:
    print(item)


my_dict={"name":"John", "age":30}
print(my_dict["age"])


value=my_dict["age"]
print(value)

my_dict={"apple":10, "banana":20, "orange":30}
for key, value in my_dict.items():
    print(key, value)


students = [("John", 90), ("Jenny", 80), ("Tom", 70)]
scores = []

for student in students:
    name, score = student
    print(f"{name} scored {score}")
    scores.append(score)

average = sum(scores) / len(scores)
print(f"\nThe average score is {average:.2f}")




