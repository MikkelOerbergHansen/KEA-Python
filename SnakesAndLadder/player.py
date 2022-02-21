
class player():
    def __init__(self, name, color, position):
        self.name = name 
        self.color = color 
        self.position = position 

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getPosition(self):
        return self.position

    def setPosition(self, ETTal):
        self.position = ETTal