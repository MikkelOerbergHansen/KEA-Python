import csv

class ExcelReader(object):

    def __init__(self):
        pass

    def prepareData(self, Filnavn): 
        file = open(Filnavn)
        csvreader = csv.reader(file, delimiter=";")
        header = next(csvreader)
        header = ["Dato/Tidspunkt", "GlobalStråling", "Relativ Fugtighed", "Temperatur", "Vindretning", "VindHastighed"]
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        file.close()

        return rows

    

