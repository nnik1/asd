dict={1:"John",2:"Smith",3:"Mark"}
print(dict)

print(dict.items())

k=dict.keys()
for i in k:
    print(i)

v=dict.values()
for i in v:
    print(i)

print(dict[3])

del dict[2]
print(dict)
