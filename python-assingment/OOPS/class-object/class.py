
#defiing a class
class Phone:
    a="samsung"
    b="apple"
    c="motorola"

# Phone.a
# obj1=Phone.a
# print(obj1)
# print(Phone.b)
# print(Phone.c)


class Phone:
    a="samsung"
    print(a)  #calling the class as function
    b="apple"
    c="motorola"
Phone()

#accessing the required eattribute from the constructed class

class Phone:
    a="samsung"
    #calling the class as function
    b="apple"
    c="motorola"
obj1=Phone()
print(obj1.a)
print(obj1.b) 
print(obj1.c)


# by defautlt self function  using the method 

class Phone:
    a="samsung"
    #calling the class as function
    b="apple"
    c="motorola"
    def samsung(self):
        print(f"I am {self.a}")

obj1=Phone()
# print(obj1.a)
# print(obj1.c)
obj1.samsung()   #=>Phone.samsung[obj1]  #calling the function of class






class Phone:
    a="samsung"
    #calling the class as function
    b="apple"
    c="motorola"
    d="mohan"

    def samsung(self):
        print(f"I am {self.a}")
    def mohan(self):
        print("i am mohan")
        print(f"My name is {self.d}")

obj1=Phone()
# print(obj1.a)
# print(obj1.c)
# obj1.samsung()   #=>Phone.samsung[obj1]  #calling the function of class
obj1.mohan()



class Phone:
    a="samsung"
    #calling the class as function
    b="apple"
    c="motorola"
    d="mohan"
    def samsung(self):
        print(f"I am {self.a}")
    def mohan(self):
        # print("i am mohan")
        print(f"My name is {self.d}")

obj1=Phone()
# print(obj1.a)
obj1.samsung()
obj2=Phone()
obj2.mohan()

# Class objects

# class Car:
#     print("hello")
#     pass

# Car()

#aainding attribute
class Car:
    a="bmw"
    b="mercedes"
    c="audi"
    def start(self):
      print("car started")
obj1=Car()
# print(obj1.a)
#calling funccction
obj1.start()
# print(obj1.start())
class animal:
    print("Animal")


    def cow(self):
        print("This is cow")

    def dog(self):
        print("I am dog  of the created of  above class")


obj1=animal()
obj1.cow()
obj1.dog()



class Friend():
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def namecaller(self,name):
        # self.place=place
        print(self.name)
        print(self.age)
        print(self.address)

    def __del__(self):
        print("hllo")
obj1=Friend("khushila",20,"dharan")
obj1.namecaller()




#acessing bothe the instant variable and  class variable

class parrot:
    species="bird"

    def __init__(self,name,age) -> None:
        
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
blue=parrot("blue",34)
print(blue.__class__.species)  #acesssing the class variable