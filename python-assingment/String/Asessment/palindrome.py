

print("Program cheking the inpu t is pallindrome not")


s1=input("ENTER THE STRING TOP CHECK IT IS PALLINDROME OR NOT\n")
a=s1[0:len(s1)]
b=s1[::-1]

if (a==b):
    print(f"The {s1} is pallindrome")
else:
    print(f"The {s1} is not pallindrome")