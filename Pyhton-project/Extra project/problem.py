'''
#1 Python Program to Calculate the Average of Numbers in a Given List
l=[1,2,3,4]
sum=0
for i in l:
    print(i)
    sum=sum+i
print(sum)
avg=sum/len(l)
print(f"the average valu eo f the list Be:{avg}")


# Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
a=int(input("Ente the value of a:"))
b=int(input("Ente the value of b:"))
print("beforte swapping")
print(a)
print(b)
a=a+b
b=a-b
a=a-b
print("After swapping")
print(a)
print(b)

# 
# usinfg function
def swap(a,b):
    print("before  swapppinng")
    a=a+b
    b=a-b
    a=a-b
    print("after  swapppinng")
    print(a)
    print(b)
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
swap(x,y)


# Python Program to Read a Number n and Compute n+nn+nnn
n=int(input("Enter the value of n:"))
t=str(n)+str(n)
t1=str(n)+str(n)+str(n)
com=n+int(t)+int(t1)
print(com)


# using funcion
def val(x):
    t=str(x)+str(x)
    t1=str(x)+str(x)+str(x)
    com=x+int(t)+int(t1)
    print(com)
n=int(input("Enter the value of n:"))
val(n)


a=int(input("Enter the valur of a:"))
for i in range(1,10):
    if(i%a==0):
        print(i)


# //using fuunction
def div(a):
    for i in range(1,10):
        if(i%a==0):
            print(i)
      
n=int(input("Enter the value of n:"))      
div(n)


n=int(input("Enter the value of x:"))
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

t=str(n)+str(a)+str(b)
print(t)
# Python Program to Accept Three Digits and Print all Possibl
# Combinations from the  Digit

def take(*a):
    print(a)
    for i in a:
        print(i)
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
z=int(input("Enter the value of z:"))
take(x,y,z)


# Python Program to Print Odd Numbers Within a Given Range
n=int(input("Enter the valuer of n:"))
for i in range(0,n):
    if(i%2==0):
        continue
    else:
        print(i)


        # using function
def odd(n):
    for i in range(0,n):
        if(i%2==0):
         continue
    else:
        print(i)
n=int(input("Enter the value of n:"))
odd(n)

# Python Program to Count the Number of Digits in a Number
count=0
n=int(input("Enter the value of n:"))
s=0
while(n>0):
    r=n%10
    n=n//10
    s=s+r
    count =count+1
print(s)
print(count)



'''
rev=0
n=int(input("Ente the value to  be checkpalindrome or not"))
while(n>0):
    r=n%10
    rev=10*rev+r
    n=n//10

if(rev==n):
    print("it is pallindrome number")
else:
    print("it is not pallindrome number")