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


        #loop for input og check at det et korrekt input ellers bliv ved med at prompte for nyt input
        is_num = False
        while is_num == False:
            NumPlayers = input("Hvor mange spillere er med? ")
            try:
                int(NumPlayers)
                is_num = True
                if int(NumPlayers) <= 1:
                    print("input skal være > 1 !! ")
                    is_num = False                  
            except ValueError:
                print("input skal være et tal !! ")

        # Lav player list som er tom
        PlayerList =[]
        # fyld player list i et loop og spørg efter nødvendige inputs (navn og color)
        for x in range (1, int(NumPlayers)+1):
            pname = input("hvad er dit navn? ")
            pcolor = input("hvilken farve er du? ")
            PlayerList.append(player(pname, pcolor, 0))



        ## start selve spillets procedure
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

                if TempPosition == 100:
                    finish = True
                    print("{} stod i position: {} og flytter nu til position: {}".format(Player.getName(), Player.getPosition(), TempPosition))
                    print()
                    print("**********Hurra {} win*********".format(Player.getName()))
                    print()
                    break
                elif TempPosition > 100:
                    newPosition = TempPosition - 100
                    TempPosition = 100 - newPosition
                    print("{} stod i position: {} og flytter nu til position: {}".format(Player.getName(), Player.getPosition(), TempPosition))
                    Player.setPosition(int(TempPosition))
                    print()
                    print("************next player turn ************")
                    var = input()
                else:
                    print("{} stod i position: {} og flytter nu til position: {}".format(Player.getName(), Player.getPosition(), TempPosition))
                    Player.setPosition(int(TempPosition))
                    print()
                    print("************next player turn ************")
                    var = input()


            