# acessing the element of list

l2=[2,3,45,
    'mohan',{2,3,4,5,6}]
print(l2)
print(len(l2))
#   acessing the list 
print(l2[0])
print(l2[4])

#negative indexing
print(l2[-1])  #acessung from the lsasst using the negative indexing



l4=[2,3,45,
    'mohan',{2,3,4,5,6},["pyhton","programming",["developer","creator"],3],5]
print(l4)
print(l4[5])
print(l4[5][2][1])


# Removing the element of the list
#remove,clear,pop 

l1=[1,2,3,43,4,5,67]
l1.pop(2)  #the value  under the pop is teh positiona of the liat value as thei indexing
print(l1)

# clear
l5=[1,2,3,43,4,5,67]
l5.clear()
print(l5)


#remove
l6=[1,2,3,4,5,6,6,7,"khu",7]
l6.remove("khu")  #removing the written elemnt
print(l6)


