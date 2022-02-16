
import Die

class DieGame(object):
    def __init__(self):
        pass

    def play(self):
        self.D1 = Die.Die(0)
        self.D2 = Die.Die(0)

    def PrintResult(self):
        fv1: self.D1.GetFaceValue()
        fv2: self.D2.GetFaceValue()
        result = fv1 + fv2

        print("trace Die/printResult")
        print(fv1)
        print(fv2)
        print("result is : " + str(result))

