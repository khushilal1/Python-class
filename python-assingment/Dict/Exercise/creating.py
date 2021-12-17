# Creating a Dictionary
d={} #empty set s not a set ist is dictionary
print(type(d))
print(d)

#idct with the key value pais
d1={1:"ram",2:"mohan"}
print(d1)
print(type(d1))  

#keys and the value cab be of aby darta typed
d2={2.3:"hari","name":3}
print(d2)
print(type(d2))  


# conversion of the list into the dict
l1=[(1,2),(34,5)]  #tuple  of only two value in which 1firs t ecome the key and otgher bcome val of that keycan oly be change into dic
d=dict(l1)
print(d)
print(type(d))

# Nested Dictionary:

d4 = {1: 'python', 2: 'c++',
3:{'A' : 'hello', 'B' : 'world', },4:"django"}
print(d4)
print(type(d4))