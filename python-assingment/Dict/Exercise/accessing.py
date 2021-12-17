# accessing of the dic
#axcessing the element by the keys
d={1:"STRING",2:"string",3:"mohan",4:"hari"}
print(d)
print(d[1])
print(d[3])


# Python program to demonstrate

d = {1: 'python', 'name': 'c++', 3: 'javascript'}
# accessing a element using key
print("Accessing a element using key:")
print(d['name'])

# using get()
d = {1: 'python', 'name': 'c++', 3: 'javascript'}
print(d.get(1))


a= {1: 'python', 'name': 'c++', 3: 'javascript'}
print(a.get(3))

# Accessing an element of a nested dictionary.

a= {1: 'python', 'name': 'c++', 3:{5:"mohan",6:"ram"} ,4:'javascript'}
print(a.get(3))
print(a[3][5])



# Removing Elements from Dictionary

# del keyword, pop(), popitem(), clear()
# del keyword
a= {1: 'python', 'name': 'c++', 3:{5:"mohan",6:"ram"} ,4:'javascript'}
del(a[1])
print(a)


# using pop()
a= {1: 'python', 'name': 'c++', 3:{5:"mohan",6:"ram"} ,4:'javascript'}
pop_element=a.pop(1)
print(b)
print(a)

# using popitem()

a= {1: 'python', 'name': 'c++', 3:{5:"mohan",6:"ram"} ,4:'javascript'}
del a[3][6]
print(a)


pop_element=a.popitem()
print(f"the key value which is pop out from the above duct be:{pop_element}")
print(f"the set which remain after poping element be:{a}")


# using clear()
a= {1: 'python', 'name': 'c++', 3:{5:"mohan",6:"ram"} ,4:'javascript'}
a.clear()
print(a)
b=a.copy()
b[2]="4"
print(b)
print(type(b))