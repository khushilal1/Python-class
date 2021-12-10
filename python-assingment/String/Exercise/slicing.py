#colon(:) is used as slicing operator
s1="python developer"
# print(s1)
# a=s1[0:3]
print(s1[-9:-1])
# print(a)



print(s1[-1:-9])
print(s1[3:14])  #slicing the character from the position 3 to 14
print(f"the string at the even place only be:{s1[0:17:2]}")  #aceesin the elembt in even place

# Deleting/Updating from a String

s1="python programming"
# s1[2]="hello"  #we cannot upadte new  into that variable
print(s1)  #TypeError: 'str' object does not support item assignment
#we cannot change the written string
s2=s1+ "  " +"hello"  #we can reassing it
print(s2)


s1="python"
del s1[3]  #elemt of item cannot delete but entire string can delete usin the del keyword
print(s1)


s1="python"
del s1  #deleting the s1 string
print(s1)
l1=[1,2,3,4,56,7]
print(l1)
del l1  #deleting of the list
print(l1)  #NameError: name 'l1' is not defined
# l1=[1,2,3,4,5,6]
# print(l1[2:5])