
# Python program to illustrate
# getting input from user
name = input("Enter your name: ")
# user entered the name 'harssh'
print("hello", name)
print(type(name))

# Python3 program to get input from user
# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = num1 * num2
print("Product is: ", num3)


a = int(input("Enter num1: "))
b =float(input("Enter num2: "))
c= a *b
print(f"Product is: {c}")

# Python program to illustrate
# selection statement
num1 = 34
if(num1>12):
 print("Num1 is good")
elif(num1>35):
 print("Num2 is not gooooo....")
else:
 print("Num2 is great")




#getting value from user
a = int(input("Enter te value of a:"))
if(a<15):
 print("Num1 is good")
elif(a>15 and a<35):
 print("Num2 is not gooooo....")
else:
 print("Num2 is great")