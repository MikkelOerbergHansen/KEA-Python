
class VejrStation(object):
    def __init__(self, by, adresse, land, målinger):
        self.by = by
        self.adresse = adresse
        self.land = land
        self.måletyper = ["Dato/Tidspunkt", "GlobalStråling", "Relativ Fugtighed", "Temperatur", "Vindretning", "VindHastighed"]
        self.målinger = målinger  #[] liste af målings objekter

    def getBy(self):
        return self.by

    def setMåling(self, målingsListe):
        self.målinger = målingsListe

    def getMålinger(self):
        return self.målinger


