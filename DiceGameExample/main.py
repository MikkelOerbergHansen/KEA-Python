from DiceGame import DieGame

def main():
    print("================================")
    Game=DieGame()
    DieGame.play(Game)
    DieGame.PrintResult(Game)
    print("================================")

    if DieGame.PrintResult.result == 7:
        print("congratulationS!! You Are A Winner")
    else:
        print("Sorry :( You Are A Looser")



if __name__ == '__main__':
    main()

