

import random

class Die(object):
    def __init__(self, eye):
        self.FaceValue = eye
    
    def roll(self):
        self.FaceValue = random.randint(1,6)

    def GetFaceValue(self):
        return self.FaceValue
