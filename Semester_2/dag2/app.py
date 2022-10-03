import sqlite3
from flask import Flask, request, render_template, redirect, session

class Produkt:
    def __init__(self, uid, ItemNo, Attributes, Billede, PrisPrivat, PrisRetailer):
        self.uid = uid
        self.ItemNo = ItemNo
        self.Attributes = Attributes 
        self.Billede = Billede
        self.PrisPrivat = PrisPrivat
        self.PrisRetailer = PrisRetailer



with sqlite3.connect("Semester_2/dag2/Gubi.db") as connection:
    cursor = connection.cursor()
    query = "SELECT * FROM Products WHERE PrisPrivat < 2000 ORDER BY PrisPrivat;" #Skal laves om til userinput i stedet.
    Products = cursor.execute(query)

ProduktObjects = []
for d in Products:
    produkt = Produkt(d[0], d[1], d[2], d[3], d[4], d[5])
    ProduktObjects.append(produkt)



app = Flask(__name__)
@app.route("/")
def Data():
    return render_template('Startside.html', data=ProduktObjects)




# til at køre koden direkte
if __name__== '__main__':
    app.run()