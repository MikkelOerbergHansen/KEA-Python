import csv

class ExcelReader(object):

    def __init__(self):
        pass

    def prepareData(self, Filnavn): 
        file = open(Filnavn)
        csvreader = csv.reader(file, delimiter=";")
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        #print(rows)
        file.close()

        return rows

    

