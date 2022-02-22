

class by(object):
    def __init__(self, by):
        self.by = by
        self.byerne = []

    def addBy(self, VælgBY):
        self.byerne.append(VælgBY)

    def getBy(self, Index):
        return self.byerne[Index]

    