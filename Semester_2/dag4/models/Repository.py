import pandas as pd
from models.Kunde import *

df = pd.read_excel('Tværfagligdag/static/Tværfaglig.xlsx', sheet_name='Kunder', usecols="A, B, C, D, E")

#print(df)
KundeListe = []

mytable = df.values.tolist()

for i in range(0, len(mytable)):
    row = (mytable[i][0], mytable[i][1], mytable[i][2], mytable[i][3], mytable[i][4])
    KundeListe.append(tuple(row))  



import sqlite3

drop_Kunde_table = """DROP TABLE IF EXISTS Kunder"""

Kunde_table = """CREATE TABLE Kunder (
                id INTEGER PRIMARY  KEY AUTOINCREMENT,
                Navn TEXT,
                Adresse TEXT,
                Postnummer TEXT, 
                Mobilnummer INTEGER,
                Driftsstatus TEXT
                );
                """

with sqlite3.connect('Tværfagligdag/static/Clever.db') as connection:
    cur = connection.cursor()
    cur.execute(drop_Kunde_table)
    cur.execute(Kunde_table)

    for k in KundeListe:
        cur.execute("INSERT INTO Kunder (Navn, Adresse, Postnummer, Mobilnummer, Driftsstatus) VALUES (?,?,?,?,?);", 
            (k[0], k[1], k[2], k[3], k[4]))

class Repository:
    def __init__(self):
        self.KundeObjekter = self.setKundeObjekter()

    def setKundeObjekter(self):
        with sqlite3.connect("Tværfagligdag/static/Clever.db") as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Kunder;"
            kunder = cursor.execute(query)
        Kunder1 = []
        for k in kunder:
            kunde1 = Kunde(k[1], k[2], k[3], k[4], k[5]) 
            Kunder1.append(kunde1)
        return Kunder1
    

