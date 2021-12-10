# 2. Program to Exchange the Values of Two Numbers With Using a Temporary Variable

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(f"The value of a before exachange is {a}")
print(f"The value of b before exachange is {b}")


tem=a
a=b
b=tem
print(f"The value of a after exachange is {a}")
print(f"The value of b after exachange is {b}")
