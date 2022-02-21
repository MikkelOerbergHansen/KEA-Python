from Die import Die
from player import player

# DiceGame Class
class DiceGame (object):
    # constructor makes 2 instances of the die with d1 and d2 name 
    def __init__(self):
        self.D1= Die()
        self.D2 = Die()
    
        
     # class play to roll and display values. 
    def Play(self):

        NumPlayers = int(input("Hvor mange spillere er med? "))
        PlayerList =[]

        for x in range (1, NumPlayers+1):
            pname = input("hvad er dit navn? ")
            pcolor = input("hvilken farve er du? ")
            PlayerList.append(player(pname, pcolor, 0))


        finish = False
        while finish == False:
            for Player in PlayerList:
                self.D1.Roll()
                fv1 = self.D1.GetFaceValue()
                self.D2.Roll()
                fv2 = self.D2.GetFaceValue()
                print()
                print("==== Det er nu {}'s tur ====".format(Player.getName()))
                print("first dice:" + str(fv1))
                print("second dice: " + str(fv2))
                fvSum = fv1 + fv2
                TempPosition = fvSum + Player.getPosition()
                print("{} stod i position: {} og flytter nu til position: {}".format(Player.getName(), Player.getPosition(), TempPosition))
                Player.setPosition(int(TempPosition))

                if TempPosition>=100:
                    finish = True
                    print()
                    print("**********Hurra {} win*********".format(Player.getName()))
                    break
                else:
                    print("************next player turn ************")


            