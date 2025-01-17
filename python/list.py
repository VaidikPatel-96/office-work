#list methods

lst=[1,2,3,4,5,5,6,7,99]

#append = adds an element at the end of the list

lst.append(100)
print(lst)  #output:[1, 2, 3, 4, 5, 5, 6, 7, 99, 100]


#clear = Removes all the elements form the lise

lst.clear()
print(lst)  #Output:[]


#copy  = Returns a copy of the list
lst=[1,2,3,4,5,5,6,7,99]
copy_1=lst.copy()
print(copy_1)  #Output:[1, 2, 3, 4, 5, 5, 6, 7, 99]


#count = Returns the number of elements with the specified value
lst=[1,2,3,4,5,5,6,7,99]
x=lst.count(5)
print(x)  #Output: 2


#extend = Add the elements of the a list,
#         to the end of the current list
lst=[1,2,3,4,5,5,6,7,99]
lst2=['apple', 'banana', 'cherry']
lst.extend(lst2)
print(lst)  #Output: [1, 2, 3, 4, 5, 5, 6, 7, 99, 'apple', 'banana', 'cherry']


#index = Returns the index of the first element with the specified value
lst=[1,2,3,4,5,5,6,7,99]
x=lst.index(4)
print(x)  #Output: 3


#insert = Adds an element at the specified position
lst=[1,2,3,4,5,5,6,7,99]
lst.insert(3,44)
print(lst)  #Output: [1, 2, 3, 44, 4, 5, 5, 6, 7, 99]


#pop = Removes the element at the specified value /index position
lst=[1,2,3,4,5,5,6,7,99]
lst.pop(1)
print(lst) #OUtput: lst=[1,3,4,5,5,6,7,99]


#remove = Removes the first item with the specified value
lst=[1,2,3,4,5,5,6,7,99]
lst.remove(5)  # first 5 remove
print(lst) #Output:lst=[1,2,3,4,5,6,7,99]


#reverse = reverses the order of the list
lst=[1,2,3,4,5,5,6,7,99]
lst.reverse()
print(lst)  #output: [99, 7, 6, 5, 5, 4, 3, 2, 1]


#sort = sort the list
lst=[5,8,1,6,9,4,3]
lst.sort()
print(lst)  #Output: [1, 3, 4, 5, 6, 8, 9]