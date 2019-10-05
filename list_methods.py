# append: Appends object at the end.
x = [1, 2, 3]
x.append(7)
x.append([4, 5])
x.append(8)
print(x)
# [1, 2, 3, [4, 5]]

# extend: Extends list by appending elements
x = [1, 2, 3]
x.extend([24, 35])
print(x)
# [1, 2, 3, 24, 35]

# insert
a = [123, 'xyz', 'John', 'abc', 123, 123, 'abc']
a.insert( 3, 2019)
print("list : ", a)
# [123, 'xyz', 2019, 'abc', 123, 123, 'abc']

a.remove('zara')
print("list : ", a)
print("index ", a.index(2019))
print("count ", a.count(123))

# pop
print(a)
a.pop(1)
print(a)

# reverse
a.reverse()
print(a)

# sort
a = [3,6,8,1,3,0,2]
print(a)
a.sort()
print(a)

# copy
# The problem with copying the list in this way
# is that if you modify the new_list,
# the old_list is also modified.
old_list = [1, 2, 3]
new_list = old_list
# add element to list
new_list.append('a')
print('New List:', new_list )
print('Old List:', old_list )

# clear
a.clear()
print(a)












