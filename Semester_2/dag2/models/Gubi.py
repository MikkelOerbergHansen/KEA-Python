import pandas as pd


df2 = pd.read_excel('Dag2/static/GUBI.xlsx', sheet_name='Master data EU', usecols = "A, E, T, BF, BJ")
df3 = pd.read_excel('Dag2/static/GUBI.xlsx', sheet_name='Master data EU', usecols = "D")
df4 = pd.read_excel('Dag2/static/GUBI.xlsx', sheet_name='Master data EU', usecols = "N, Q")
df5 = pd.read_excel('Dag2/static/GUBI.xlsx', sheet_name='Master data EU', usecols = "P")
df6 = pd.read_excel('Dag2/static/GUBI.xlsx', sheet_name='Master data EU', usecols = "L")

mytableProdukt = df2.values.tolist()
productList= []
for i in range(0, len(mytableProdukt)):
    row = (mytableProdukt[i][0], mytableProdukt[i][1], mytableProdukt[i][2], mytableProdukt[i][3], mytableProdukt[i][4] )
    productList.append(tuple(row))

mytableProduktNavn = df3.values.tolist()
produktNavnList= []
for i in range(0, len(mytableProduktNavn)):
    row = (mytableProduktNavn[i][0])
    produktNavnList.append(tuple(row))

mytableKollektion = df4.values.tolist()
KollektionList= []
for i in range(0, len(mytableKollektion)):
    row = (mytableKollektion[i][0], mytableKollektion[i][1])
    KollektionList.append(tuple(row))

mytableDesigner = df5.values.tolist()
DesignerList= []
for i in range(0, len(mytableDesigner)):
    row = (mytableDesigner[i][0])
    DesignerList.append(tuple(row))

mytableKategori = df6.values.tolist()
KategoriList= []
for i in range(0, len(mytableKategori)):
    row = (mytableKategori[i][0])
    KategoriList.append(tuple(row))

#### database

import sqlite3

drop_table_Produkt = """DROP TABLE IF EXISTS Products"""
drop_table_ProduktNavn = """DROP TABLE IF EXISTS ProduktNavn"""
drop_table_Kollektion = """DROP TABLE IF EXISTS Kollektion"""
drop_table_Designer = """DROP TABLE IF EXISTS Designer"""
drop_table_Kategori = """DROP TABLE IF EXISTS Kategori"""

create_table_Produkt = """CREATE TABLE Products (
                        Produkt_ID INTEGER PRIMARY  KEY AUTOINCREMENT,
                        ItemNo INTEGER NOT NULL,
                        Attributes TEXT,
                        Billede TEXT,
                        PrisPrivat INTEGER,
                        PrisRetailer INTEGER
                        );
                        """
create_table_ProduktNavn = """CREATE TABLE ProduktNavn (
                        ProduktNavn_ID INTEGER PRIMARY  KEY AUTOINCREMENT,
                        ProduktNavn TEXT
                        );
                        """
create_table_Kollektion = """CREATE TABLE Kollektion (
                        Kollektion_ID INTEGER PRIMARY  KEY AUTOINCREMENT,
                        Kollektion TEXT,
                        DesignetÅrstal INTEGER
                        );
                        """
create_table_Designer = """CREATE TABLE Designer (
                        Designer_ID INTEGER PRIMARY  KEY AUTOINCREMENT,
                        Designer TEXT
                        );
                        """

create_table_Kategori = """CREATE TABLE Kategori (
                        Kategori_ID INTEGER PRIMARY  KEY AUTOINCREMENT,
                        Kategori TEXT
                        );
                        """

with sqlite3.connect('Dag2/Gubi.db') as connection:
    cur = connection.cursor()
    cur.execute(drop_table_Produkt)
    cur.execute(drop_table_ProduktNavn)
    cur.execute(drop_table_Kollektion)
    cur.execute(drop_table_Designer)
    cur.execute(drop_table_Kategori)
    cur.execute(create_table_Produkt)
    cur.execute(create_table_ProduktNavn)
    cur.execute(create_table_Kollektion)
    cur.execute(create_table_Designer)
    cur.execute(create_table_Kategori)

    for r in productList:
        cur.execute("INSERT INTO Products (ItemNo, Attributes, Billede, PrisPrivat, PrisRetailer) VALUES (?,?,?,?,?);", 
                (r[0], r[1], r[2], r[3], r[4]))
    
    for r in produktNavnList:
        cur.execute("INSERT INTO ProduktNavn (ProduktNavn) VALUES (?);", 
                (r[0]))

    for r in KollektionList:
        cur.execute("INSERT INTO Kollektion (Kollektion, DesignetÅrstal) VALUES (?,?);", 
                (r[0], r[1]))

    for r in DesignerList:
        cur.execute("INSERT INTO Designer (Designer) VALUES (?);", 
                (r[0]))

    for r in KategoriList:
        cur.execute("INSERT INTO Kategori (Kategori) VALUES (?);", 
                (r[0]))


#Mangler alle FK, samt få designer og produktnavn og kategori til at virke




