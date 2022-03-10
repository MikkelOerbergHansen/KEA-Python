


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
            PizzaString = PizzaString + "\n" + " {0:40} kr: {1:2} ".format(pizza.getName() , pizza.getPrice()) 
        PizzaString = PizzaString + "\n" + "========================================================"

        return str("Order number: " + str(self.OrderId) + "\n" +
                    "for " + self.name + "\n" + 
                    "takeAway: " + str(self.ToGo) + "\n" + 
                    PizzaString + "\n" + 
                    "Total Price: " + "{0:33}{1:4}Kr".format("",str(self.TotalPrice)) + "\n")


