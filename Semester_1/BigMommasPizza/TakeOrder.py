from datetime import datetime


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
        

        return str("****************************************************************************************************\n" +
                    "{0:30} {1:22} {2:30} ".format("", "BIG MOMMAS GASTRONOMIA", "") + "\n" +
                    "{0:32} {1:22} {2:30} ".format("", "Frederikværksgade 4", "") + "\n" +
                    "{0:35} {1:22} {2:30} ".format("", "3400 Hillerød", "") + "\n" +
                    "{0:33} {1:22} {2:30} ".format("", "tlf: 40 12 40 03", "") + "\n" +
                    "{0:36} {1:22} {2:30} ".format("", datetime.today().strftime('%d-%m-%Y'), "") + "\n" + "\n" +
                    "Order number: " + str(self.OrderId) + "\n" +
                    "navn: " + self.name + "\n" + 
                    "takeAway: " + str(self.ToGo) + "\n" + 
                    PizzaString + "\n" + 
                    "{0:44} {1:>6.2f} {2:3}".format("Total Price:", float(self.TotalPrice), "Kr.") + "\n" +
                    "{0:44} {1:>6.2f} {2:3}".format("25% moms udgør", self.TotalPrice*0.25, "Kr.") + "\n" + "\n" +
                    "{0:35} {1:22} {2:30}".format("","CVR: 39405016 ", "")  + "\n" +
                    "{0:34} {1:22} {2:30}".format("","Tak For Besøget ", "")  + "\n" +
                    "****************************************************************************************************")


