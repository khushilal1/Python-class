#append
l2=[1,2,3,34,4,6]
l4=["mohan","ram",3,4,5,6,7,6]
l2.append(l4)
print(l2)

# extend
l2=[1,2,3,34,4,6]
l4=["mohan","ram",3,4,5,6,7,6]
l4.extend(l2)
print(l4)



# insert
l2=[1,2,3,34,4,6]
l2.insert(4,"mohan")
print(l2)

# remmove
l2=[1,2,3,34,4,6]
l2.remove(34)
print(l2)


# prop

l2=[1,2,3,34,4,"mohan",6]
l2.pop(5)
print(l2)


# sort
l2=[1,2,3,34,4,5,6]
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)

l2.sort(reverse=False)
print(l2)



l2=[1,2,3,34,4,5,6]
l2.reverse()
print(l2)  #printing the element from the last


# copy
l1=[1,2,3,4,5,67]
l2=l1.copy()
print(l1)
print(l2)

l1=[1,2,3,4,5,67]
l2=[3,4,5,68]
l1.append(l2)
print(l1)
# print(l2)

import copy
l1=[1,2,3,4,5,6]
l2=l1.copy()
print(l2)


l1=[1,2,3,4,5,6]
l2=[]
l2=l1
print(l1)
print(l2)

