class Item:
    def __init__(self,name:str,price:float,quantity=0) -> None:
        assert price >=0 ,f"price{price} is not greater or equal to zero"
        assert quantity>=0,f"Quantity {quantity} is not egrater or eqial to zero"
        
        self.name=name
        self.price=price
        self.quantity=quantity

    def total(self):
        return self.price*self.quantity
    
obj1=Item("phone",100,4)
t=obj1.total()
print(t)

        