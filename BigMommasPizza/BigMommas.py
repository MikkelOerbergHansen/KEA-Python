
from MenuKort import MenuKort


def testrun():
    Menu = MenuKort()
    Menu.MakeMenuKort()
    Menu.AddPizza("Meat Lovers Pizza",["Tomat", "Ost","skinke","pepperoni","kebab","cocktail-Pølser"], 80)
    Menu.ShowMenuKort()


    Menu.AddOrder([6], "mikkel", True)
    print(Menu.TakeOrderCatalog[0])

    Menu.AddOrder([3,6], "mikkel", True)

    for order in Menu.TakeOrderCatalog:
        print(order)


def run():
    print( "\nVelkommen Til Big Mommas Pizza !!! \n")
    Menu = MenuKort()
    Menu.AddPizza("Margherita",["Tomat", "Ost"], 69)
    Menu.AddPizza("Vesuvio",["Tomat", "Ost","skinke"], 75)
    Menu.AddPizza("Capricciosa",["Tomat", "Ost","skinke", "champignon"], 80)
    Menu.AddPizza("Calzone",["Tomat", "Ost","skinke", "champignon"], 80)
    Menu.AddPizza("Quattro Stagioni",["Tomat", "Ost","skinke", "champignon", "rejer", "peberfrugt"], 85)
    Menu.AddPizza("Marinara",["Tomat", "Ost","rejer", "muslinger", "hvidløg"], 85)
    Menu.AddPizza("Vegetarian",["Tomat", "Ost","grøntsager"], 80)
    Menu.AddPizza("Italiana",["Tomat", "Ost","løg", "kødsauce"], 75)
    Menu.AddPizza("Gorgonzola",["Tomat", "gorgonzola","løg", "champignon"], 75)
    Menu.AddPizza("Contadina",["Tomat", "Ost","Oliven", "champignon"], 75)
    Menu.AddPizza("Naples",["Tomat", "Ost","ansjoser", "oliven"], 79)
    Menu.AddPizza("Vichinga",["Tomat", "Ost","skinke", "champignon","peberfrugt","hvidløg", "chili (stærk)"], 80)
    Menu.AddPizza("Calzone Special",["Tomat", "Ost","skinke", "rejer", "kødsauce"], 80)
    Menu.AddPizza("Esotica",["Tomat", "Ost","skinke", "rejer", "annanas"], 80)
    Menu.AddPizza("Tonno",["Tomat", "Ost","Tun", "rejer"], 85)
    Menu.AddPizza("Sardegna",["Tomat", "Ost","cocktail pølser", "bacon", "løg", "æg"], 80)
    Menu.AddPizza("Romana",["Tomat", "Ost","skinke", "bacon", "løg"], 78)
    Menu.AddPizza("sole",["Tomat", "Ost","skinke", "bacon", "æg"], 78)
    Menu.AddPizza("Big Mamma",["Tomat", "Gorgonzola","rejer", "Asparges", "parma skinke"], 90)



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

    ##### tag imod ordre





######################
##### program start

choice = input("ønsker du \n 1: test run \n 2: run \n >> ")
if choice == str(1):
    testrun()
elif choice == str(2):
    run()
else:
    exit