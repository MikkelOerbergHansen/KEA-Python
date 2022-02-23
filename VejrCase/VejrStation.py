from Målinger import Måling


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

    def PrintData(self,indexstart, indexslut):
        print("="*114)
        print("| {0:20} | {1:15} | {2:20} | {3:12} | {4:13} | {5:15} | ".format(self.måletyper[0],self.måletyper[1], self.måletyper[2], self.måletyper[3], self.måletyper[4], self.måletyper[5]))
        for i in range(indexstart, indexslut+1):
            print("| {0:20} | {1:15} | {2:20} | {3:12} | {4:13} | {5:15} | ".format(self.målinger[i].getAllMåling()[0], self.målinger[i].getAllMåling()[1], self.målinger[i].getAllMåling()[2], self.målinger[i].getAllMåling()[3], self.målinger[i].getAllMåling()[4], self.målinger[i].getAllMåling()[5]))



