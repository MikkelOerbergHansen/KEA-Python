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
        p1name = input("hvad er dit navn?")
        p1color = input("hvilken farve er du?")
        p2name = input("hvad er dit navn?")
        p2color = input("hvilken farve er du?")

        player1 = player(p1name, p1color, 0)
        player2 = player(p2name, p2color, 0)

        finish = False
        while finish == False:
            self.D1.Roll()
            fv1 = self.D1.GetFaceValue()
            self.D2.Roll()
            fv2 = self.D2.GetFaceValue()
            print(fv1)
            print(fv2)
            fvSum = fv1 + fv2

            TempPosition = fvSum + player1.getPosition()
            player1=player(p1name, p1color, TempPosition)
            if TempPosition>=100:
                finish = True
                print("**********Hurra {} win*********".format(player1.getName()))
                break
            else:
                print("************ {} position er: {} ***********".format(player1.getName(), player1.getPosition()))
                print("************next player turn ************")
            
            self.D1.Roll()
            fv1 = self.D1.GetFaceValue()
            self.D2.Roll()
            fv2 = self.D2.GetFaceValue()
            print(fv1)
            print(fv2)
            fvSum = fv1 + fv2

            TempPosition = fvSum + player2.getPosition()
            player2=player(p2name, p2color, TempPosition)
            if TempPosition>=100:
                finish = True
                print("**********Hurra {} win*********".format(player2.getName()))
                break
            else:
                print("************ {} position er: {} ***********".format(player2.getName(), player2.getPosition()))
                print("************next player turn************")