from player import player 



NumPlayers = int(input("Hvor mange spillere er med? "))
PlayerList ={}

        
for x in range (1, NumPlayers+1):
    pname = input("hvad er dit navn? ")
    pcolor = input("hvilken farve er du? ")
    PlayerList["Player{}".format(x)] = player(pname, pcolor, 0)

print(PlayerList.keys())
print(PlayerList.items())

##print(PlayerList["Player1"])