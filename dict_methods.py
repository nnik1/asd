# clear
dict1 = {'Name': 'John', 'Age': 25};
print(dict1)
dict1.clear()
print(dict1)

# copy
dict1 = {'Name': 'John', 'Age': 25};
dict2 = dict1.copy()
print("New Dictionary : ", str(dict2))

# fromkeys -- this method returns the list
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print("New Dictionary : ", str(dict))
dict = dict.fromkeys(seq, 10)
print("New Dictionary : ",  str(dict))

# get
dic = {"A":1, "B":2} 
print(dic.get("A")) 
print(dic.get("C")) 
print(dic.get("C","Not Found ! ")) 
# 1, None, Not Found !


# items
d = {'Name': 'John', 'Age': 37}
print("Value items: ", d.items())

# keys
d = {'Name': 'John', 'Age': 27}
print("Value keys: ", d.keys())

# pop
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)

# popitem
person = {'name': 'John', 'age': 25, 'salary': 3500.0}
result = person.popitem()
print('person = ',person)
print('Return Value = ',result)

# setdefault
person = {'name': 'John', 'age': 25}
# person.add({'name': 'Bob', 'age': 30})
print(person)
age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)

# The setdefault() method returns
# the value for key if key is in the dictionary.
# If not, it inserts key with a value of default
# and returns default.
D = {'name': 'Bob', 'age': 30}
v = D.setdefault('name')
print(v)    # Bob

# update
d = {1: "one", 2: "three"}
d1 = {2: "two"}
# updates the value of key 2
d.update(d1)
print(d)

# values
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales)
print(sales.values())

# Sorted() function in Python
x = [2, 8, 1, 4, 6, 3, 7]
print(x)
print("Sorted List returned :", sorted(x)) 
print("Reverse sort :", sorted(x, reverse = True)) 
print("Original list not modified :", x)

