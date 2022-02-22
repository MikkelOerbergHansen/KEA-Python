
class VejrStation(object):
    def __init__(self, by, adresse, land, måletyper, målinger):
        self.by = by
        self.adresse = adresse
        self.land = land
        self.måletyper = måletyper
        self.målinger = målinger

    def getBy(self):
        return self.by

    def setMåling(self, målingsListe):
        self.målinger = målingsListe

    def getMåling(self):
        return self.målinger


