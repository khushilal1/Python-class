# Polymorphism is type process of making the name of function  same but different work at their different place

class bird:
   
    def fly():
        print("parot acn fly")

    def swim(self):
        print("parrot ccan swim")
    
class crow:
    def fly():
        print("crow can fly")
    
    def swim(self):
        print("crow cannot swim")

blue=bird()


# There are four ways of implementing
# Polymorphism in Python that is duck typing,method oveloading,opertator overloading,method of overriding
# 1. Duck typing
class Nepal():
    def capital(self):
        print("Kathmandu is the capital of Nepal.")
    def language(self):
       print("Nepali is the most widely spoken language of Nepal.")
    def type(self):
       print("Nepal is a developing country.")


    class USA():
        def capital(self):
            print("Washington, D.C. is the capital of USA.")
        def language(self):
            print("English is the primary language of USA.")
        def type(self):
                print("USA is a developed country.")
obj_nep = Nepal()
obj_usa = USA()
for country in (obj_nep, obj_usa):
    country.capital()
    country.language()
    country.type()




    # Method Overloading

class add:
    def sum(self,x,y,z=0,a=0):
        # s=0
        return x+y+z+a
obj1=add()
# a=obj1.sum(2,3)  #few more step to call function
# print(a)
print(obj1.sum(2,4))
print(obj1.sum(2,4,6))
print(obj1.sum(2,4,6,65)) #overloading means incresing  the paameter

# Method Overriding
class programming:

    def practice(self):
        print("practices increae your idea")
    
    def consistency(self):
        print("hard work makes you expertise in your field")
class python(programming):
    def consistency(self):
        print("hark work  make you graet")

py=python()
py.consistency()
py.practice()
py.consistency()
