from Pizza import MYpizza
from TakeOrder import *
from MenuKort import *


print( "\nVelkommen Til Big Mommas Pizza !!! \n")

print("Vil du se MenuKortet ? \n")
BrugerSvar = input("y = yes eller n = no\n")
tempSvar = False
while tempSvar == False:
    if BrugerSvar == "y":
        Menu = MenuKort()
        Menu.MakeMenuKort()
        Menu.ShowMenuKort()
        tempSvar = True
    elif BrugerSvar == "n":
        print("\nVi er Klar til at tage din ordre")
        tempSvar = True
    else:
        print("\nDet Forstår vi ikke")
        BrugerSvar = input("y = yes eller n = no\n")
        tempSvar = False


