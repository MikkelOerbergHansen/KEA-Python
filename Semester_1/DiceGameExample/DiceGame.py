
import Die

class DieGame(object):
    def __init__(self):
        pass

    def play(self):
        self.D1 = Die.Die(1)
        self.D2 = Die.Die(0)
        self.D1.roll()
        self.D2.roll()
    

    def PrintResult(self):
        fv1 = self.D1.GetFaceValue()
        fv2 = self.D2.GetFaceValue()
        result = fv1 + fv2

        print("trace Die/printResult")
        print("Die 1 = " + str(fv1))
        print("Die 2 = " + str(fv2))
        print("result is : " + str(result))
        return result

