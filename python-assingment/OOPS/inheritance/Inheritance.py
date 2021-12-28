# Inheritance
# A Python program to demonstrate 


class Person():
    def __init__(self,name):
        self.name=name

    def getName(self):
        print(f"{self.name}")
          #return the value of self.name
    
    def isEmployee(self):
        return False

class Employee(Person):  #single line inhritence
    def isEmployee(self):
        print(self.name)

obj1=Person("khushilal")
obj1.getName()
obj2=Employee("hari")
obj2.isEmployee()


# Subclassing (Calling constructor of parent class)
# from typing_extensions import Self



# Types of Inheritance
# Single Inheritance
class father:
    def father(self):
        pass
        father=""
        print(father)
        self.fataher=father

        print("i am father")
        

class mother:
    def mother(self,name1):
        mother=""
        print(mother)
        self.name1=mother

class son:
    def parent(self):
        print(f"my father is :{self.father}")
        print(f"my father is :{self.mother}")

        # print(f"my mother is :{self.name1}")
        print("  I am their son")

obj1=son()
obj1.father="mohan"
obj1.mother="gita"
# obj1.mother="gita"
obj1.parent()