from VejrStation import VejrStation
from Målinger import Måling
from ExcelReader import ExcelReader

class vejr(object):
    def __init__(self):
        pass
        #self.vejrstation = "tom"
        #self.Målinger = "tom"

    def runvejr(self):

        ExcelFilData = ExcelReader()
        dataframe = ExcelFilData.prepareData("Semester_1/VejrCase/VejrDataKøbenhavn.csv")

        ###
        ### datasættet skal konverteres til en liste af målinger
        ### som kan bruges ved oprettelse af vejrstationer
        ### 

        MålingerKBH =[]
        for i in range(1, len(dataframe)):
            MålingerKBH.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

        # Vi gentager for datasættet for hhv. Aalborg og odense
        dataframe = ExcelFilData.prepareData("Semester_1/VejrCase/VejrDataAalborg.csv")

        MålingerAA =[]
        for i in range(1, len(dataframe)):
            MålingerAA.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

        dataframe = ExcelFilData.prepareData("Semester_1/VejrCase/VejrDataOdense.csv")

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
        print("=============")
        print()

        tempVar = False
        while tempVar == False:

            Byvalg = input("Fra hvilken by ønsker du at se vejr data?: ")
            print("fra hvilket tidspunkt ønsker du at se data?: ")
            tidsIntervalstart = input("start: ")
            tidsIntervalslut = input("slut: ")

            print()
            print()

            if Byvalg == "København":
                tempVar = True
                print("Du har valgt at se vejr data fra {} i perioden {} - {} ".format(Byvalg, tidsIntervalstart, tidsIntervalslut))
                indexStart = 0
                indexSlut = 0

                for i in range(0,len(vejrStation1.getMålinger())):
                    if tidsIntervalslut == vejrStation1.getMålinger()[i].getTidspunkt():
                        indexSlut = i

                        for j in range(0,len(vejrStation1.getMålinger())):

                            if tidsIntervalstart == vejrStation1.getMålinger()[j].getTidspunkt():
                                indexStart = j
                                break 

                        break

                if indexStart == 0 or indexSlut == 0:
                    print("Det var ikke et gyldigt tidsinterval -- beklager!!")
                    print("Tidsintervaller for denne by er på formen: 22-02-2022 04:30:00")
                    print("For København er det tidligst: {} og senest: {}".format(vejrStation1.getMålinger()[len(vejrStation1.getMålinger())-1].getTidspunkt(),vejrStation1.getMålinger()[0].getTidspunkt()))
                    tempVar = False
                    print()

                else:
                    vejrStation1.PrintData(indexStart,indexSlut)
                   

            
            elif Byvalg == "Aalborg":
                tempVar = True
                print("Du har valgt at se vejr data fra {} i perioden {} - {} ".format(Byvalg, tidsIntervalstart, tidsIntervalslut))
                indexStart = 0
                indexSlut = 0

                for i in range(0,len(vejrStation3.getMålinger())):
                    if tidsIntervalslut == vejrStation3.getMålinger()[i].getTidspunkt():
                        indexSlut = i
                        

                        for j in range(0,len(vejrStation3.getMålinger())):

                            if tidsIntervalstart == vejrStation3.getMålinger()[j].getTidspunkt():
                                indexStart = j
                                break 

                        break

                if indexStart == 0 or indexSlut == 0:
                    print("Det var ikke et gyldigt tidsinterval -- beklager!!")
                    print("Tidsintervaller for denne by er på formen: 22-02-2022 04:30:00")
                    print("For Aalborg er det tidligst: {} og senest: {}".format(vejrStation3.getMålinger()[len(vejrStation3.getMålinger())-1].getTidspunkt(),vejrStation3.getMålinger()[0].getTidspunkt()))
                    tempVar = False
                    print()

                else:
                    vejrStation3.PrintData(indexStart,indexSlut)



            elif Byvalg == "Odense":
                tempVar = True
                print("Du har valgt at se vejr data fra {} i perioden {} - {} ".format(Byvalg, tidsIntervalstart, tidsIntervalslut))
                indexStart = 0
                indexSlut = 0

                for i in range(0,len(vejrStation2.getMålinger())):
                    if tidsIntervalslut == vejrStation2.getMålinger()[i].getTidspunkt():
                        indexSlut = i

                        for j in range(0,len(vejrStation2.getMålinger())):

                            if tidsIntervalstart == vejrStation2.getMålinger()[j].getTidspunkt():
                                indexStart = j
                                break 

                        break

                if indexStart == 0 or indexSlut == 0:
                    print("Det var ikke et gyldigt tidsinterval -- beklager!!")
                    print("Tidsintervaller for denne by er på formen: 22-02-2022 04:30")
                    print("For Odense er det tidligst: {} og senest: {}".format(vejrStation2.getMålinger()[len(vejrStation2.getMålinger())-1].getTidspunkt(),vejrStation2.getMålinger()[0].getTidspunkt()))
                    tempVar = False
                    print()

                else:
                    vejrStation2.PrintData(indexStart,indexSlut)



            else:
                print("Vi har intet vejr data for den valgte by - beklager!!")
                print("Prøv evt. at skrive København, Aalborg eller Odense")


        print()
        print()

dg = vejr()
dg.runvejr()

        

        



