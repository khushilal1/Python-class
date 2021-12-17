# Accessing of Tuples

t = (1, 2, 3)
print(t[0])
print(t[1])
print(t[2])
print(t[-2])
print(t[-1])


t1= ("c++", "c#", "machine learning","python")
a,b,c,e = t1
print(a)
print(b)
print(c)


# Concatenation

# Concatenation of tuples using + operator
t1 = (0, 1, 2, 3)
t2 = ('python', 'hello', 'world')
t3 = t1 + t2
print(f"the first tuple be :{t1}")
print(f"The second tuple be:{t2}")
print(f"The concteneted tuple be:{t3}")
#only same datatypes are allowed to concatenate
