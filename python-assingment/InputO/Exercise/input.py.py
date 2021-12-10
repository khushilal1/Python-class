

# input output

string="khushilal Mahato"
print(string)

string="khushilal\'s Mahato" #\ represent once gap
print(string)

string="khushilal\nMahato"  #\n represent tyhe nnew break line
print(string)


string="khushilal\rMahato"
print(string)


string="      khushilal\rMahato"   #\r This represents a carriage return (move the cursor at the beginning of the line

# without moving the cursor to the new line.)


print(string)


string="khushilal\bMahato"
print(string)

string="khushilal\b\bMahato"
print(string)

string="khushilal Mahato\b"
print(string)


string="khushilal\\Mahato"
print(string)


string="khushilal\fMahato"
print(string)

# Inpu/output in python

n=input("What is your name?\n")
print(type(n))

a=input("Enter a number\n")
print(a)

a=input("Enter the value of number\n")
print(a)
print(type(a))
 
 
#  conversion of data type
a=input("Enter the value of data\n")
b=int(a)
c=float(a)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

a=input("Enter the value of  data")
b=list(a)
print(b)
c=set(a)
print(c)
d=tuple(a)
print(d)

# typecasting
a=int(input("Enter the value of data:"))
b=int(input("Enter the value of data:"))
sum=a+b
print("the sum of a and b is",sum)
print(type(sum))


a=float(input("Enter the value of data:"))
b=float(input("Enter the value of data:"))
sum=a+b
print("the sum of a and b is",sum)
print(type(sum))

print(1,2,3,4,5,6,7,8,9,0)
print(1,2,3,4,5,6,7,8,9,0,sep="*")    #s=separation between the number 
print(1,2,3,4,5,6,7,8,9,0,end="..$\n")
print(1,2,3,4,5,6,7,8,9,0,sep="*",end="@")



# formatting
x=5
y=4
print("the value of x is {} and y is {}".format(x,y))
print("the value of y is {} and x is {}".format(y,x))


x=int(input("Enter the value of x:"))
y=int(input("Enter the  value of y:"))
print("the value of x is {} and y is {}".format(x,y))
print("the value of y is {} and x is {}".format(y,x))

# order of  {}
print("i love {} and {}".format("bread","butter"))
print("i love {} and {}".format("butter"," bread"))

print("i love {0} and {1}".format("bread","butter"))
print("i love {1} and {0}".format("bread","butter"))

# argument
print("hello, {name} {greeting}".format(greeting='goood morning',name="khushilal"))

# f-string
x=int(input("Enter the value of x:"))
y=float(input("enter the value of y:"))
print(f"the value of x is {x} and y is {y}")

