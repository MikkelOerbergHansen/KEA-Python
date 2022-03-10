

from Pizza import MYpizza
import random



class MenuKort(object):
    
    def __init__(self):
        
        self.PizzaCatalog = []
        self.TakeOrderCatalog=[]





    def MakeRandomPizzas(self):
        PizzaList = []
        ExtraToppings = ["Annanas", "Skinke", "Pepperoni", "Champignon", "Løg", "Dressing", "Salat", "Bacon"]
        ToppingList = ["Tomat", "Ost"]
        for i in range(1,len(ExtraToppings)+1):
            randInt = random.randint(0, len(ExtraToppings)-1)
            ToppingList.append(ExtraToppings[randInt])
            del ExtraToppings[randInt]
            NewPizza = MYpizza(i, "Pizza" + str(i), ToppingList, 50)
            PizzaList.append(NewPizza)
            ToppingList = ["Tomat", "Ost"]
        return PizzaList


    def MakeMenuKort(self):
        self.PizzaCatalog = self.MakeRandomPizzas()


    def ShowMenuKort(self):
        print("\n========================================================\n")
        for pizza in self.PizzaCatalog:
            print(pizza)
        print("\n========================================================\n")

    



