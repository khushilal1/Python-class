print("getting the string in reversed orderd")

s1=input("Enter the string to get the string in reversed order\n")
s2=s1[::-1]
print(F"the reversed of the enteerd string is {s2}")




s1=input("Enter the string to get their in reversed order\n")
s2=""
for i in reversed(s1):
    print(i)
    s2=s2+i
print(s2)