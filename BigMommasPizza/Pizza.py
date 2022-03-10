from TakeOrder import *
from MenuKort import *




class Pizza(object):
    def __init__(self,id,name,toppings,price):
        self.Id = id
        self.Name = name
        self.toppings = toppings
        self.Price=price

    def getPrice(self):
        return self.Price

    def getName(self):
        return self.Name

    def __str__(self):
        PizzaString = self.Id + "\n" + self.Name + "\n" + "tomat, ost"
        for topping in self.toppings:
            PizzaString = PizzaString + ", " + topping
        return PizzaString