from Pizza import MYpizza
from TakeOrder import *
import random



class MenuKort(object):
    
    def __init__(self):
        
        self.PizzaCatalog = []
        self.TakeOrderCatalog=[]





    def MakeRandomPizzas(self):
        PizzaList = []
        StaticToppings = ["Tomat", "Ost"]
        ExtraToppings = ["Annanas", "Skinke", "Pepperoni", "Champignon", "Løg", "Dressing", "Salat", "Bacon"]
        ToppingList = StaticToppings
        for i in range(1,10):
            randInt = random.randint(0, len(ExtraToppings)-1)
            ToppingList.append(ExtraToppings[randInt])
            NewPizza = MYpizza(i, "NewPizza" + i, ToppingList, 50)
            PizzaList.append(NewPizza)
        return PizzaList




    def MakeMenuKort(self):
        self.PizzaCatalog = self.MakeRandomPizzas()


    def ShowMenuKort(self):
        for pizza in self.PizzaCatalog:
            print(pizza)

    



