
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
