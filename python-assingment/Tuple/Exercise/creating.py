# Creating a tuple
t=()
print(t)
print(type(t))

t1= (1,4, 2,7)
print(t1)
print(type(t1))


t2 = ("hello", "world")
print(t2)
print(type(t2))


l = [1, 2, 3]  #givintg the value inthe form of list
l2 = tuple(l)
print(l2) #returning th  value in the form of tuple due using of the tuple function



s = "pyhtonprogramming"
t3 = tuple(s)
print(t3)
print(len(t3))

#tuple packing
t5=2,3,5,6,7,89
print(t5)
print(type(t5))
a,b,c,d,e,f=t5
print(t5)
print(a)
print(e)



# Creating a Tuple with Mixed Datatypes and nested tuple

t6 = (5, 'Welcome', [2.3,44,5],4.5, 'Everyone')
print(t6)
print(len(t6))


t1 = (0, 1, 2, 3)
t2 = ('python', 'google')
t3 = (t1, t2)
print(t3)


#with repetition
t = ('python programmoer',) * 5  #"*" multiply the number of tuple
print(t)