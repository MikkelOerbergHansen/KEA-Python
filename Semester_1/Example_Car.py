# class example
# Data-Typer:
# - String = tekst
# - Boolean = sandt/falsk
# - Integer = hele tal
# - Float = decimaltal



#definer en class
class Car:
    def __init__(self, color, brand, model, OnSale, MarketPrice, SellingPrice ,KmPerLitre):
        self.color = color                  # definer Attributter
        self.brand = brand
        self.model = model
        self.OnSale = OnSale
        self.MarketPrice = MarketPrice
        self.SellingPrice = SellingPrice
        self.KmPerLitre = KmPerLitre

    def salesBonus(self):
        print("Salesbonus for salget er " + 
        str((self.MarketPrice-self.SellingPrice)*0.20) + " Kr")

    def getBrand(self):
        return self.brand



#definer variabler af vores Car class
car1 = Car("Green", "volkswagen", "Golf", True, 28000, 24000, 18.1)
car2 = Car("Blue", "Toyota", "Prius", True, 50000, 40000,15.8 )
car3 = Car("Red", "Ford", "Mustang", False, 44500, 30000, 16.5 )

#tomme print kald for at skabe mellemrum
print()
print()

print(car1.getBrand())

#tomme print kald for at skabe mellemrum
print()
print()

# eksempel på at regne med værdierne gemt under variablerne
car1SalesBonus = (car1.MarketPrice - car1.SellingPrice)*0.20
car2SalesBonus = (car2.MarketPrice - car2.SellingPrice)*0.20

# eksempel med metoden i klassen
car1.salesBonus()
car2.salesBonus()
car3.salesBonus()


#tomme print kald for at skabe mellemrum
print()
print()



#print værdier for valgte attributter på de valgte variable
print(car1.brand)
print(car2.brand)
print(car3.brand)

#tomme print kald for at skabe mellemrum
print()
print()

# En lang Print
print("kære bilsælger")
print("Velkommen på arbejde")
print("bilen af mærket " + car1.brand + " i farven " + car1.color + 
" koster " + str(car1.MarketPrice) + 
" men du kan sælge den for " + str(car1.SellingPrice))

print("Bonus for salg af Bilen er " + str(car1SalesBonus) + " Kr")

#tomme print kald for at skabe mellemrum
print()
print()

#tjek typer af attributter
print(type(car1))
print(type(car1.MarketPrice))
print(type(car1.KmPerLitre))
print(type(car1.OnSale))


#tomme print kald for at skabe mellemrum
print()
print()




