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