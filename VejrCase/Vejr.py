from VejrStation import VejrStation
from Målinger import Måling
from ExcelReader import ExcelReader

class vejr(object):
    def __init__(self):
        pass
        #self.vejrstation = "tom"
        #self.Målinger = "tom"

    def run(self):

        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataKøbenhavn.csv")
        ###
        ### datasættet skal konverteres til en liste af målinger
        ### som kan bruges ved oprettelse af vejrstationer
        ### 

        MålingerKBH =[]
        for i in range(1, len(dataframe)):
            MålingerKBH.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

        # Vi gentager for datasættet for hhv. Aalborg og odense
        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataAalborg.csv")

        MålingerAA =[]
        for i in range(1, len(dataframe)):
            MålingerAA.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

        dataframe = ExcelFilData.prepareData("VejrCase/VejrDataOdense.csv")

        MålingerOD = []
        for i in range(1, len(dataframe)):
            MålingerOD.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

        ### vi kan nu oprette tre vejrstations objekter

        vejrStation1 = VejrStation("København", "København C", "DK", MålingerKBH)
        vejrStation2 = VejrStation("Odense", "Odense C", "DK", MålingerOD)
        vejrStation3 = VejrStation("Aalborg", "Aalborg C", "DK", MålingerAA)


        ### Vi byder nu vores bruger velkommen til dettee fantastiske vejr målings informations program
        print()
        print()
        print("Velkommen Til")
        Byvalg = input("Fra hvilken by ønsker du at se vejr data?: ")
        print("fra hvilket tidspunkt ønsker du at se data?: ")
        tidsIntervalstart = input("start: ")
        tidsIntervalslut = input("slut: ")



        print(vejrStation1.getBy())
        print(vejrStation1.getMåling()[0].getTidspunkt())
        print(vejrStation1.getMåling()[0].getAllMåling()[0])

        #print("Vejr Stationen i {} har klokken {:.2f} målt følgende data: ".format(vejrStation1.getBy(), vejrStation1.getMåling().getTidspunkt()))
        #print(vejrStation1.getMåling().getAllMåling())
        #print("Vejr Stationen i {} har klokken {:.2f} målt følgende data: ".format(vejrStation2.getBy(), vejrStation2.getMåling().getTidspunkt()))
        #print(vejrStation2.getMåling().getAllMåling())
        #print("Vejr Stationen i {} har klokken {:.2f} målt følgende data: ".format(vejrStation3.getBy(), vejrStation3.getMåling().getTidspunkt()))
        #print(vejrStation3.getMåling().getAllMåling())
        



dg = vejr()
dg.run()

        

        



