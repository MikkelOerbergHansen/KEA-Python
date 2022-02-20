from DiceGame import DieGame

def main():
    print("==============================================")
    Game=DieGame()
    DieGame.play(Game)
    result = DieGame.PrintResult(Game)
    
    print()

    if result == 7:
        print("congratulations!! You Are A Winner")
    else:
        print("Sorry :( You Are A Looser")

    print("==============================================")



if __name__ == '__main__':
    main()

