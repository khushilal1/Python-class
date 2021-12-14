# elemt can be ad in the peredefined list
# method of addind element as append,extend,insert\
l1=[1,2,"mohan"]
l1.append(6)
print(l1)

l2=[2,3,5,6,7]
l3=["mohan",3]
l2.extend(l3)  #using the  extend function
print(l2)

l2=[2,3,5,6,7]
l3=("mohan",3) 
 #tuple can also be append
l2.extend(l3)  #using the  extend function
print(l2)

# appendng every element of the list
l1=[0]

for i in range(1,10):
    l1.append(i)  #appending one by one elemnt
    print(l1)
print(l1)

# insert
l3=[2,3,4,5,6]
l3.insert(1,"computer ") #insert require the position and value
print(l3)