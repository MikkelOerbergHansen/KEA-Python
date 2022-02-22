
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


    def setGlobalStråling(self, opdaterMåling):
        self.Globalstråling = opdaterMåling

    def getGlobalStråling(self):
        return self.Globalstråling
    

    def setrelativFugtighed(self, opdaterMåling):
        self.relativFugtighed = opdaterMåling

    def getrelativFugtighed(self):
        return self.relativFugtighed



    def setTempereatur(self, opdaterMåling):
        self.Temperatur = opdaterMåling

    def getTempereatur(self):
        return self.Temperatur



    def setVindretning(self, opdaterMåling):
        self.Vindretning = opdaterMåling

    def getVindretning(self):
        return self.Vindretning

 

    def setVindhastighed(self, opdaterMåling):
        self.Vindhastighed = opdaterMåling

    def getVindhastighed(self):
        return self.Vindhastighed

    
    def getTidspunkt(self):
        return self.Tidspunkt





