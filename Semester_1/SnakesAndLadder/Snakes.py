

class snakes(object):
    def __init__(self):
        self.snakeIN = [30, 56, 88]
        self.snakeOUT = [23, 38, 10]

    def getSnakeIN(self):
        return self.snakeIN

    def getSnakeOUT(self,index):
        return self.snakeOUT[index]
