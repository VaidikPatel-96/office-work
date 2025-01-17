#values - returns a list of all values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)  #Output: dict_values(['Ford', 'Mustang', 1964])



#update - updates the dictionary with the specifide key - value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})
print(car)  #Output:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}



#setdefault - returns the value of the specified key. if the key does not exist:insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")
print(x)  #Output:  withe



#popitem - removes the last inserted key-value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
print(car) #Output: {'brand': 'Ford', 'model': 'Mustang'}



#pop - removes the element with the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")
print(car) #Output: {'brand': 'Ford', 'year': 1964}



#keys  - returns a list containing the dictionary's keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print(x)  #Output:dict_keys(['brand', 'model', 'year'])



#itlems - returns a list containing a tuple for each key value pair
car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1943
}
x=car.items()
print(x)  #Output: dict_items([('brand', 'ford'), ('model', 'mustang'), ('year', 1943)])



#get - returns the value of the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)   #Output: Mustang


#fromkeys - returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)  #Output: {'key1': 0, 'key2': 0, 'key3': 0}


# copy - returns a copy of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
print(x) #Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964} 



#clear - removes all the elements form dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)  #Output: {}
