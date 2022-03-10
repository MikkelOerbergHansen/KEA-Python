
from MenuKort import MenuKort



Menu = MenuKort()
Menu.MakeMenuKort()
Menu.AddPizza("Meat Lovers Pizza",["skinke","pepperoni","kebab","cocktail-Pølser"], 80)
Menu.ShowMenuKort()


Menu.AddOrder([6], "mikkel", True)
print(Menu.TakeOrderCatalog[0])

Menu.AddOrder([3,6], "mikkel", True)

for order in Menu.TakeOrderCatalog:
    print(order)





def testrun():
    print( "\nVelkommen Til Big Mommas Pizza !!! \n")
    print("Vil du se MenuKortet ? \n")
    BrugerSvar = input("y = yes eller n = no\n>>>> " )
    tempSvar = False
    while tempSvar == False:
        if BrugerSvar == "y":
            Menu.ShowMenuKort()
            tempSvar = True
        elif BrugerSvar == "n":
            print("\nVi er Klar til at tage din ordre")
            tempSvar = True
        else:
            print("\nDet Forstår vi ikke")
            BrugerSvar = input("y = yes eller n = no\n>>>> ")
            tempSvar = False


#testrun()