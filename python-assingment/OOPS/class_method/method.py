# @method be used to wite the class method
#by default we used to use the "cls" in the fu nction
class mobile:
    brand="apple"
    price=599990

    def property(self):
        print(f"the brand of mobile be:{self.brand}")
        print(f"the price of {self.brand} is:{self.price}")
    #using the class method 

    
    @classmethod
    def full(cls):
        return(f"{cls.brand}")

b=mobile()
b.property()
c=b.full()
print(c)
