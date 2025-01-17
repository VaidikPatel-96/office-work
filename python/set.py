##  Set methods ##

fru= {"apple", "banana", "cherry"}

#add = adds an element to the set
fru.add("orange")
print(fru)   #Output : {'orange', 'banana', 'apple', 'cherry'}


#clear = removes all the elements from the set
fru= {"apple", "banana", "cherry"}
fru.clear()
print(fru)  #OUTPUT : set()


#copy = returns a copy of the set
fru= {"apple", "banana", "cherry"}
x=fru.copy()
print(x)  #Output: {'banana', 'apple', 'cherry'}


#difference = Returns a sest containing the difference between two or more sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.difference(y)
print(z)  #Output: {'banana', 'cherry'}


#difference update = Removes the items in this set that are also included in another,specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)  #Output: {'cherry', 'banana'}


#discard = remove the specified item
x = {"apple", "banana", "cherry"}
x.discard("cherry")
print(x) #output : {'apple', 'banana'}


# intersection = returns a set, that is the intersection of tow other sets\
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y)
print(z) #Output: {'apple'}


#intersection update= removes the item in this set that are not present in other, specified sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)  #Output: {'apple'}


#pop = removes an element from the set /The pop() method removes a random item from the set
x = {"apple", "banana", "cherry"}
x.pop()
print(x) #Output: {'apple', 'cherry'}


#remove = removes the specified element
x = {"apple", "banana", "cherry"}
x.remove("cherry")
print(x) # output: {'banana', 'apple'}


#symmetric difference= returns a set with the symmetric difference of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.symmetric_difference(y)
print(z)  #Output: {'cherry', 'google', 'microsoft', 'banana'}


#symmetric difference update = Inserts symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)  #Output: {'cherry', 'google', 'microsoft', 'banana'}



#union = return a set containing the union of sets/Return a set that contains all items from both sets, duplicates are
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)
print(z) #OUtput :{'microsoft', 'banana', 'apple', 'cherry', 'google'}


#update = Update the set with the union of the set and other
#The update() method updates the current set, by adding items from another set (or any other iterable).
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x) #Output:{'banana', 'cherry', 'microsoft', 'apple', 'google'}


