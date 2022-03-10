from Pizza import *
from TakeOrder import *



class MenuKort(object):
    
    def __init__(self):
        
        self.PizzaCatalog = []
        self.TakeOrderCatalog=[]

    def MakeMenuKort(self):
        self.PizzaCatalog = MakeRandomPizzas()

        print()


    

    def ShowMenuKort(self):
        for pizza in self.PizzaCatalog:
            print(pizza)

    def MakeRandomPizzas(self):
        StaticToppings = ["Tomat", "Ost"]
        ExtraToppings = ["Annanas", "Skinke", "Pepperoni", "Champignon", "Løg", "Dressing", "Salat", "Bacon"]
        PizzaList = []
        return PizzaList



