
class Measurements(object):
    def __init__(self, Globalstråling, relativFugtighed, Temperatur, Vindretning, Vindhastighed):
        self.Globalstråling = Globalstråling
        self.relativFugtighed = relativFugtighed
        self.Temperatur = Temperatur
        self.Vindretning = Vindretning
        self.Vindhastighed = Vindhastighed
        self.AllMeasures = []

    def getALLMeasures(self):
        self.AllMeasures.append(self.Globalstråling)
        self.AllMeasures.append(self.relativFugtighed)
        self.AllMeasures.append(self.Temperatur)
        self.AllMeasures.append(self.Vindretning)
        self.AllMeasures.append(self.Vindhastighed)
        return self.AllMeasures

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


