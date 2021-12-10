# 2 program to check the number is odd or even using thre function
def oddeven(n):  #pn is a user defined function which determine odd or even number
    if(n%2==0):
        print(f"{n} is a even number:")
    else:
        print(f"{n} is oddd  number:")

x=int(input("Enter the value of x to be detrmined odd or even\n"))
oddeven(x)