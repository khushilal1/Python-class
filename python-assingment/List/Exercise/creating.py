# creating of list
# list can be cretyin by using the sqare brackets
# list can take any value : string,list,tuple
l=[]
print(f"the empty list be:{l}")
print(type(l))

# list with string and ruple value also;
l1=["mohan",(2,3,4,),["1,2,3,4"]]
print(l1)
print(len(l1))


# mutlidimensional list
l2=[2,3,45,
    'mohan',{2,3,4,5,6}]
print(l2)
print(len(l2))
#   acessing the list 
print(l2[0])
print(l2[4])
print(l2[-1])  #acessung from the lsasst using the negative indexing


# nested lis
l3=[2,[3,"54","ram"],7]
print(l3[1][1])
