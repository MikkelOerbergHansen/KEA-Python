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
                if int(NumPlayers) <= 1 or int(NumPlayers) > 4:
                    print("input skal være > 1 og < 5 !! ")
                    is_num = False                  
            except ValueError:
                print("input skal være et tal !! ")

        # Lav player list som er tom
        PlayerList =[]
        # fyld player list i et loop og spørg efter nødvendige inputs (navn og color)
        # bliv ved med at spørge efter input hvis navn er tomt
        # bliv ved med at spørge efter input hvis color ikke er en godkendt farve
        Approved_colors = ["red", "blue", "green", "yellow", "pink", "silver", "black", "orange", "purple", "white"]

        for x in range (1, int(NumPlayers)+1):
            empty_string = True
            while empty_string == True:
                pname = input("hvad er dit navn? ")
                if pname != "":
                    empty_string = False
                else:
                    print("input can not be empty !!")

            approve_col = False
            while approve_col ==False:
                pcolor = input("hvilken farve er du? ")
                if pcolor in Approved_colors:
                    approve_col = True
                else:
                    print("din farve skal være i denne liste:")
                    print(Approved_colors)

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
                print("first dice: " + str(fv1))
                print("second dice: " + str(fv2))
                fvSum = fv1 + fv2
                NewPosition = fvSum + Player.getPosition()

                if NewPosition == 100:
                    finish = True
                    print("{} stod i position: {} og flytter nu til position: {}".format(Player.getName(), Player.getPosition(), NewPosition))
                    print()
                    print("**********Hurra {} win*********".format(Player.getName()))
                    print()
                    break


                elif NewPosition > 100:
                    tempPosition = NewPosition - 100
                    NewPosition = 100 - tempPosition
                    print("{} stod i position: {} og flytter nu til position: {}".format(Player.getName(), Player.getPosition(), NewPosition))
                    Player.setPosition(int(NewPosition))
                    print()
                    print("************next player turn ************")
                    
                    ## Error handling for inputs
                    ## input must be empty since it only prompts for next users turn
                    empty_string = False
                    while empty_string == False:
                        var = input()
                        if var == "":
                            empty_string = True
                        else:
                            empty_string = False


                else:
                    print("{} stod i position: {} og flytter nu til position: {}".format(Player.getName(), Player.getPosition(), NewPosition))
                    Player.setPosition(int(NewPosition))
                    print()
                    print("************next player turn ************")

                    ## Error handling for inputs
                    ## input must be empty since it only prompts for next users turn
                    empty_string = False
                    while empty_string == False:
                        var = input()
                        if var == "":
                            empty_string = True
                        else:
                            empty_string = False


            