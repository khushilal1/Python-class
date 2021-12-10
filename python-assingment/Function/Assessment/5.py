# 5. Program to Find the Sum of Natural Numbers using function

n=int(input("Enter the value of n:\n"))
def natural(n):   #N() is  a userdefined fnction 
    sum=0
    for i in range(0,n+1):
        sum=sum+i
        i=i+1
    print(f"the sum of  natural number be:{sum}")
natural(n)