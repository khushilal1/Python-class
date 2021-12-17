# write a program to change the set into tuple and vce versa

l1=["python","program"]
print(f"The given eleemrenytt in the form of list be:{l1}")
s=set(l1)
print(f"original set which is gieven:{s}")
print(type(s))

# conersion of set into tuple
t=tuple(s)
print(t)
print(type(t))


# conersion of set into tuple
s1=set(t)
print(s1)
print(type(s1))
