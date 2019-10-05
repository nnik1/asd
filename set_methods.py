ss=set([1,2,3,4,5])
print(ss)
# {1, 2, 3, 4, 5}
type(ss)

# add
ss.add(9)
print(ss)
# {1, 2, 3, 4, 5, 9}

ss=set([1,2,3,4,5])
ss2=ss
print(ss2)

# difference
ss1 = set([1, 2, 3, 4, 5])
ss2 = set([4,5,6,7,8])
print(ss1,ss2)
#({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8})
ss3 = ss1.difference(ss2)
#({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8})
ss3=ss1.difference(ss2)
print(ss3)
# {1, 2, 3}

# union
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}
print("A ", A)
print("B ", B)
A.union(B)
print("union", A)

s1 = set([1, 2, 3, 5, 7])
s2 = set([5, 6, 7])  
print("update", s1,s2)  
s1.update(s2) 
print(s1)  

# intersection
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}
A.intersection(B)
print("intersection ",A)

# difference_update
A.difference_update(B)
print("difference_update", A)

# set-discard
numbers = {2, 3, 4, 5}

numbers.discard(3)
print('discard = ', numbers)

numbers.discard(10)
print('discard = ', numbers)

# isdisjoint
A = {1, 5, 9, 0}
B = {2, 4, -5}

print("isdisjoint ", A, B)
print("isdisjoint is ", A.isdisjoint(B))

# issubset
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print("issubset ", A, B)
print("issubset is ", A.issubset(B))
print("A issubset B ", A.issubset(B))
print("B issubset A ", B.issubset(A))

# issuperset
print("B issuperset A ", B.issuperset(A))

# pop
# Pops a random element from S
# and returns it.
s = set([1, 5, 9, 2, 4, -5])
# print(s)
#s1 = s.pop()
#s2 = s.pop()
#s3 = s.pop()
#print(s1,s2,s3)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())

# remove
animal = {'cat', 'dog', 'fish', 'rabbit'}
print('Animal set: ', animal)
animal.remove('fish')
print('Updated animal set: ', animal)

# symmetric_difference
# symmetric_difference() method returns a new set
# which contains symmetric difference of two sets.
# The symmetric_difference_update() method updates
# the set calling symmetric_difference_update()
# with the symmetric difference of sets.
A = {1, 2, 3, 4}
B = {3, 4, 5}
print(A, B)
print("symmetric_difference ", A, B)
print(A.symmetric_difference(B))

# symmetric_difference_update
A.symmetric_difference_update(B)
print(A,B)

