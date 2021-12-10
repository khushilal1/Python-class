# 3. Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(f"The value of a before exachange is {a}")
print(f"The value of b before exachange is {b}")

a=a+b
b=a-b
a=a-b


print(f"The value of a before exachange is {a}")
print(f"The value of b before exachange is {b}")