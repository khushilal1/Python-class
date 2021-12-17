#acessing the elemnt of the set using the for loop
s={1,2,3,4,5,6}
for ele in s:
    print(ele)
    print(s)
# print(s[0]) #TypeError: 'set' object is not subscriptable

# removing the element
#using the remove and discard ,pop and clear   function
s1={2,3,4,5,'MOHAN'}
s1.remove( "MOHAN")
print(s1)

# USIN G THE LooP
s2={1,2,3,4,5,6,5,7,7,8,6,9,0}
for ele in range(3,10):
    s2.remove(ele)
    print(s2)

# pop()
a=set("pythonprogramming")
print(a)
a.pop()
print(a)
a=set("pythonprogramming")
print(a)
a.clear()
print(a)