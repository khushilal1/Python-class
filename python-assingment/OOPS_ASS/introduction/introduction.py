#creating of the class
class Item:
    def Total(self,x,y,n):
        print(f"the type of phone be:{n}")
        return x*y

#craeting of the boject
obj1=Item()
n=input("Enter the typ[e of phone\n")
a=int(input("Enter the price of phone\n"))
b=int(input("Enter the quantitiy of phone\n"))
all=obj1.Total(a,b,n)
print(f"the total price be:{all}")

obj2=Item()
n=input("Enter the typ[e of phone\laptop\n")
a=int(input("Enter the price of phone\n"))
b=int(input("Enter the quantitiy of phone\n"))
all=obj2.Total(a,b,n)
print(f"the total price be:{all}")
