# 1. Program to Check if a Number is Positive, Negative or 0 using function
def pn(n):  #pn is a user defined function which determine the positive and negtaive number
    if(n==0):
        print(f"{n} is a zero number:")
    elif(n>0):
            print(f"{n} is positive number:")
    else:
        print(f"{n} is negative number:")

x=int(input("Enter the value of x to be detrmined positiva or negative\n"))
pn(x)