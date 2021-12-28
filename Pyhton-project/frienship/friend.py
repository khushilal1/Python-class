class Friend():
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def namecaller(self):
        # self.place=place
        print(self.name)
        print(self.age)
        print(self.address)



x=input("Enter the name of your friend:\n")
y=int(input("Enter the age of your friend:\n"))
z=input("Enter the address of your friend:\n")
obj1=Friend(x,y,z)
print("The detail of your friend be :")
obj1.namecaller()
