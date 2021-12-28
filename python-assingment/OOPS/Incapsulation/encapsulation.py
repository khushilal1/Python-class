# # Encapsulation
# # Public members / Public Access Modifier

# class developer:
#     def __init__(self,name,age) -> None:
#         self.name=name#can be access publically
#         # print(self.name)
#         self.age=age
#         pass
#     def display(self):
#         print(self.name)
    
#     def displayage(self):
#        print(self.age)


# obj1=developer("khi",664)
# obj1.display()
# obj1.displayage()


# # Protected members/ Protected Access
# # Modifier
# # from _typeshed import Self


# class student:
#     # _name=None
#     # _roll=None
#     # _branch=None
#     def __init__(self,name,roll,branch) -> None:
#         self._name=name
#         self._roll=roll
#         self._branch=branch
#         pass
#     def display(self):
#         print(self._name)
#         print(self._roll)
#         print(self._branch)
    
#     # def displayage(self):
#     #    print(self.age)
#     #derive class

# class  developer:
#     def __init__(self,name,roll,branch) -> None:
#         student.__init__(self,name,roll,branch)

#     def display1(self):
#         print(self._name)
#         print(self._roll)
#         print(self._branch)

# obj2=developer("khush",657,"health")
# obj2.display1()
# # obj1.displayage




# #

# class student:
#     # _name=None
#     # _roll=None
#     # _branch=None
#     def __init__(self,name,roll,branch) -> None:
#         self._name=name
#         self._roll=roll
#         self._branch=branch
#         pass
#     def display(self):
#         print(self._name)
#         print(self._roll)
#         print(self._branch)
    
#     # def displayage(self):
#     #    print(self.age)
#     #derive class

# class  developer:
#     def __init__(self,name,roll,branch) -> None:
#         student.__init__(self,name,roll,branch)

#     def display1(self):
#         print(self._name)
#         print(self._roll)
#         print(self._branch)

# obj2=developer("khush",657,"health")
# obj2.display1()
# # obj1.displayage


# from typing import AsyncGenerator


# from _typeshed import Self

#  restriction on any program is eencapsultion
#prevent the  direct acees s method
#acess modifier
# type of modifier
# public protective and 
# from os import name


# class  develper:
#     def __init__(self,name,age):
#         self.developer=name
#         self.developerage=age

#     def displayage(self):
#         print(f"name:{self.developer} and age: {self.developerage}")


# obj1=develper("mah",23)
# obj1.displayage()

# from types import BuiltinMethodType


# class computer:
#     def __init__(self) -> None:
#         self._maxprice=900
#     def selling(self):
#         print(f"the the maxprice be: {self._maxprice}")
#         pass

# c=computer()
# c.selling()
# #changing the valueof price
# c._maxprice=1000
# c.selling()




#private 
class computer:
    def __init__(self) -> None:
        self.__maxprice=900
    def selling(self):
        print(f"the the maxprice be: {self.__maxprice}")
        pass

        c=computer()
        c.selling()
        #changing the valueof price
        c.__maxprice=1000
        c.selling()
        #as the result we can change the value of publlic and protecteted  bu canot change the cvalue of private
        # inprder to change the value o fprivare function we  mst use set method
        c.setMaxprice(10000)
        c.selling()