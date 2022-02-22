from VejrStation import VejrStation
from Målinger import Målinger
from ExcelReader import ExcelReader

class vejr(object):
    def __init__(self):
        pass
        #self.vejrstation = "tom"
        #self.Målinger = "tom"

    def run(self):

        ExcelFilData = ExcelReader()

        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataKøbenhavn.csv")

        print(dataframe[1])


        
        Måling1 = Målinger(28, 78, 2.5, 285, 1.6, 10.30)
        Måling2 = Målinger(138, 64, 2.7, 138, 2.1, 10.30)
        Måling3 = Målinger(100, 75, 2.8, 152, 1.5, 10.30)


        vejrStation1 = VejrStation("København", "København C", "DK", ["Globalstråling", "RelativFugtighed", "Temperatur", "Vindretning", "Vindhastighed"], Måling1)
        vejrStation2 = VejrStation("Odense", "Odense C", "DK", ["Globalstråling", "RelativFugtighed", "Temperatur", "Vindretning", "Vindhastighed"], Måling2)
        vejrStation3 = VejrStation("Aalborg", "Aalborg C", "DK", ["Globalstråling", "RelativFugtighed", "Temperatur", "Vindretning", "Vindhastighed"], Måling3)

        print("Vejr Stationen i {} har klokken {:.2f} målt følgende data: ".format(vejrStation1.getBy(), vejrStation1.getMåling().getTidspunkt()))
        print(vejrStation1.getMåling().getAllMåling())
        print("Vejr Stationen i {} har klokken {:.2f} målt følgende data: ".format(vejrStation2.getBy(), vejrStation2.getMåling().getTidspunkt()))
        print(vejrStation2.getMåling().getAllMåling())
        print("Vejr Stationen i {} har klokken {:.2f} målt følgende data: ".format(vejrStation3.getBy(), vejrStation3.getMåling().getTidspunkt()))
        print(vejrStation3.getMåling().getAllMåling())
        

        

        



