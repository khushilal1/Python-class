#python program to interchange the first annd the last elemnt in the list
l1=[1,2,3,4,5,6,7,8,9]
a=l1.pop(0)
print(f"The elemnet which was remove from list at first element be:{a} ")
print(l1)

b=l1.pop(-1)
print(f"The elemnet which was remove from list at first element be:{b} ")
print(l1)

l1.insert(7,a)
print(f"The elemnet which was addded in list at last element be: ")
print(l1)

l1.insert(0,b)
print(f"The interchanged list be:{l1}")



# print(b)
# print(l1)
# l1.insert(0,a)
# print(l1)

# l1.insert(0,b)

# print(l1)


# l1.insert(0,a)
# print(l1)