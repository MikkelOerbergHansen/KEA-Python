from TakeOrder import TakeOrder
from MenuKort import MenuKort



Menu = MenuKort()
#Menu.MakeMenuKort()
Menu.AddPizza("Meat Lovers Pizza",["skinke","pepperoni","kebab","cocktail-Pølser"], 80)
Menu.ShowMenuKort()





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