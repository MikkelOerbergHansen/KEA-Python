
class Måling(object):
    def __init__(self, Tidspunkt, Globalstråling, relativFugtighed, Temperatur, Vindretning, Vindhastighed):
        self.Tidspunkt = Tidspunkt
        self.Globalstråling = Globalstråling
        self.relativFugtighed = relativFugtighed
        self.Temperatur = Temperatur
        self.Vindretning = Vindretning
        self.Vindhastighed = Vindhastighed

        self.AllMåling = [Tidspunkt, Globalstråling, relativFugtighed,Temperatur, Vindretning, Vindhastighed]

    def getAllMåling(self):
        return self.AllMåling

    
    def getTidspunkt(self):
        return self.Tidspunkt





