
#constructor
#__init__ method

class Car:
    a="bmw"
    b="mercedes"#a,b,c are class variable as global variable
    c="audi"
    def __init__(self):  #this constructoer call executed at ws soon as the object is called
        print("hello")
        print(f"I am a {self.b} of class car")

    def start(self):
      print("car started")
      print(f"I am a {self.a} of class car")
      go=self.c  #instanst variable as local variable
      print(go)
obj1=Car()
obj1.start()


# Class and Instance Variables
# from typing import ParamSpecArgs


class vehicle:
    #class variable
    vehicle_type="Car"

    #constructor
    def __init__(self,company,color):
        self.company=company
        self.color=color
        print(f"the color of car be:{self.color}")
        print(f"the company of car be:{self.company}")

        pass
obj1=vehicle("tesla","black")


# Defining instance variable using the normal method



class vehicle:
    #class variable
    vehicle_type="Car"

# The init method or constructor
    def __init__(self, company):
    # Instance Variable
        self.company = company
    # Adds an instance variable
    def setColor(self, color):
        self.color = color
        # Retrieves instance variable
    def getColor(self):
       return self.color
        
Obj1 = vehicle("BMW")
Obj1.setColor("brown")
print(Obj1.getColor())

class sum:

    first=0
    second=0
    third=0
    def __init__(self,f,s):
      self.first=f
      self.seconds=s

    def display(self):
        print(f"The fis element be:{self.first}")

    def second(self):
        print(f"The second elemnt be :{self.seconds}")    
    def Total(self):
        print(f"The sum of two number be:{self.first+self.seconds}")


x=int(input("Enter the value of x:\n"))
y=int(input("Enter the value of y:\n"))

obl1=sum(x,y)
# obl1.display()
# obl1.second()
obl1.Total()

