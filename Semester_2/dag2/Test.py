import sqlite3
class Produkt:
    def __init__(self, uid, ItemNo, Attributes, Billede, PrisPrivat, PrisRetailer):
        self.uid = uid
        self.ItemNo = ItemNo
        self.Attributes = Attributes 
        self.Billede = Billede
        self.PrisPrivat = PrisPrivat
        self.PrisRetailer = PrisRetailer


with sqlite3.connect("Gubi.db") as connection:
    cursor = connection.cursor()
    query = "SELECT * FROM Products WHERE PrisPrivat > 90000;"
    Products = cursor.execute(query)

ProduktObjects = []
for d in Products:
    produkt = Produkt(d[0], d[1], d[2], d[3], d[4], d[5])
    ProduktObjects.append(produkt)

for i in range(0,len(ProduktObjects)):
    print("===================")
    print("{} {} {} {} {} {}".format(ProduktObjects[i].uid, ProduktObjects[i].ItemNo, ProduktObjects[i].Attributes, ProduktObjects[i].Billede,
                                    ProduktObjects[i].PrisPrivat, ProduktObjects[i].PrisRetailer))

with sqlite3.connect("Gubi.db") as connection:
    cursor = connection.cursor()
    delete_comment="DELETE FROM Products WHERE  PrisPrivat > 100000"          
    cursor.execute(delete_comment)

print("=======================================================================================================================")


with sqlite3.connect("Gubi.db") as connection:
    cursor = connection.cursor()
    query = "SELECT * FROM Products WHERE PrisPrivat > 90000;"
    Products = cursor.execute(query)

ProduktObjects = []
for d in Products:
    produkt = Produkt(d[0], d[1], d[2], d[3], d[4], d[5])
    ProduktObjects.append(produkt)

for i in range(0,len(ProduktObjects)):
    print("===================")
    print("{} {} {} {} {} {}".format(ProduktObjects[i].uid, ProduktObjects[i].ItemNo, ProduktObjects[i].Attributes, ProduktObjects[i].Billede,
                                    ProduktObjects[i].PrisPrivat, ProduktObjects[i].PrisRetailer))

 
