  #boolean expression and comparision operator

print(5==6)
print(5==5)
print(5!=5)
print(5>=5)
print('khushilal'=='khushilal')

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
# print(a>b)
print(a<b)
print(a==b)
print(a<=b) # it is the combination of two equality that is less than or equal to
print(a>=b) # it is the combination of two equality that is greater than or equal to
print(a==b)
print(a!=b)
print(a is b)
print(a is not b)



print(a<b or a<b)
print(a<b or a>b)
print(a>b or a<b)
print(a>b or a>b)


print(a<b and a<b)
print(a<b and a>b)
print(a>b and a<b)
print(a>b and a>b)

# chain comparision
print(a<b<c)
print(a<b>c)
print(a>b>c)
print(a<b<c)
a=int(input("Enter the value of a:"))
b= not(a)
print(b)

a = 'Python is fun!'
b = 'Python is fun!'
print(a == b)

a="gamma"
b="OMEGA"
print(a>b)
print(a<b)

a='gamma'
b="Gamma"
a='gamma'
b="gaMma"
print(a>b)
print(a<b)


# logical operator
x=True
y=False
print(x and y)
print(x or y)


x=1
y=0
print(x and y)
print(x or y)


x=0
y=1
print(x and y)
print(x or y)


x=True
y=False
print(not x)
print(not y)

# Conditional executions
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
if a > b:  #If block starts here
 print(f"the value of a:{a}") #This is part of the if block
else: #else must be at the same level as if
 print(f"the value of b:{b}")


a=int(input("Enter the  value of a:"))
b=int(input("Enter tyhe value of b:"))

if a<b:
  print(f"The value of a:{a}")
else:
  print(f"the value of b:{b}") 

a=int(input("Enter the vaalue of a:"))
b=int(input("Enter the vaalue of b:"))
sum=a+b
if a+b==sum:
 print(f"it is true")
else:
  print(f"it  is false")


a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
if a>b:
  print(f"The entered number is bigger  than {a}")
elif a==b:
  print(f"The entered number is equal to {b}")
else:
  print(f"The entered number is smaller  than {b}")
  
  
  # this is the ternary operator
n =int(input('ENter a number:'))
print("Greater than 2") if n > 2 else print("Smaller than or equal to 2")# Out: 'Greater than 2'



#  Control Flow
i = 10
if (i > 15):
    print("10 is less than 15")
print("I am Not in if")

a= int(input("Enter the value of a:"))
if (a > 15):
    print("10 is less than 15")
print("I am Not in if")


# if-else
# python program to illustrate If else statement
a= float(input("Enter the value of a:"))

if (a<=15):
    print(f"{a} is less than 15:")
else:
    print(f"{a} is  greater than 15:")

# nested-if

a = int(input("Enter the value of a:"))
if (a >= 0):
    print(f"{a} is positive integer")
    if(a == 0):
        print(f"{a} is a zero value")

print("The given value is id determined")


# if-elif-else ladder

a =int(input("Enter the value of a:"))
if (a%3==0):
    print(f"{a} is divisible by 3:")
elif(a%5==0):
    print(f"{a} is divisible by 5:")
else:
    print(f"{a} is neither divisibel by 5 nor divisible  by 3:")


# Chaining comparison operators


# import keyword
# print(keyword.kwlist)
x = 5
print(1 < x < 10)
print(10 < x < 20 )
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)



# 6. for Loop

a=[1.,3,4,5,6]
sum=0
for e in a:
    print(e)
    sum=sum+e
print(sum)



s="pyhton"
for i in s:
    print(i)
    print(s)



d =["python","4",3,"khushi",3.4]
for i in d:
    print(f"{i} :{d[i]}")

import keyword
print(keyword.kwlist)
