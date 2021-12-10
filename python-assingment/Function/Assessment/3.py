# program to determine the greatest among thee bnumber uisng function
def g(x,y,z):
    if(x>y and x>z):
        print(f"{x} is greatest number among {x},{y} and {z}")
    elif(y>x and y>z):
        print(f"{y} is greatest number among {x},{y} and {z}")
    else:
        print(f"{z} is greatest number among {x},{y} and {z}")

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of a:"))
c=int(input("Enter the value of a:"))
g(a,b,c)