# Constructors and Destructors
# Constructor
class Simple:


    surname="yadav"
    def __init__(self,name): #this is constructor
        self.name=name
        print("This is  constructor")
        print(f"hello {name}")
        print(self.surname)
        

    def __del__(self):
        print(f"hello {self.name} {self.surname}")
        print("this is destructor")
     

object=Simple("mohan")