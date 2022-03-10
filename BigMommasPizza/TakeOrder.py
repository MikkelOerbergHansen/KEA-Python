from Pizza import *
from MenuKort import *



class TakeOrder(object):
    def __init__(self, id, pizza, name, toGo):
        self.OrderId = id
        self.Pizzas = pizza
        self.name = name
        self.ToGo = toGo
        self.TotalPrice = self.CalculatePrice()
        
    def CalculatePrice(self):
        totalPrice = 0
        for pizza in self.Pizzas:
            totalPrice = totalPrice + pizza.getPrice()
        return totalPrice   


    def __str__(self):
        PizzaString = ""
        for pizza in self.Pizzas:
            PizzaString = PizzaString + "\n" + " {0:20} kr: {1:10} ".format(pizza.getName() , pizza.getPrice()) 
        PizzaString = PizzaString + "\n" + "========================================================"

        return str("Order number: " + self.OrderId + "\n" +
                    "for " + self.name + "\n" + 
                    "takeAway: " + self.ToGo + "\n" + 
                    PizzaString + "\n" + 
                    "Total Price: " + self.TotalPrice + "Kr." + "\n")