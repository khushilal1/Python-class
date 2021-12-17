l1=["pythonforweb","23",3,4,54]
t1 = tuple(l1)
print(type(t1))
#printing all the elememt of list
print(t1[:])
#printing the element starting frm the iindexing 1
print(t1[1:])
#printing upto the 6th element

print(t1[:6])


# Reversing the Tuple
print(t1[::-1])


# Printing elements of a Range
print(t1[1:5])

# Deleting

# Deleting a Tuple
t = (0, 1, 2, 3, 4)
del t
print(t)